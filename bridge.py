import serial
import time
import requests
import sys
import glob
import json

# Configuration
API_URL = "http://localhost:8000/api/sensor-readings"
DEVICE_STATE_URL = "http://localhost:8000/api/device-states"

def get_serial_port():
    """Auto-detect serial port"""
    port = None
    if sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/tty.usbmodem*') + glob.glob('/dev/tty.usbserial*')
        if ports:
            port = ports[0]
    elif sys.platform.startswith('win'):
        port = 'COM3' # Default fallback for Windows
    else:
        # Linux/others
        ports = glob.glob('/dev/ttyACM*') + glob.glob('/dev/ttyUSB*')
        if ports:
            port = ports[0]
            
    return port

def fetch_device_states():
    """Fetch desired device states from API"""
    try:
        response = requests.get(DEVICE_STATE_URL, timeout=2)
        if response.status_code == 200:
            return response.json()
    except Exception as e:
        print(f"Error fetching device states: {e}")
    return []

def main():
    print("Starting Lettuce Monitoring Bridge...")
    
    last_device_check = 0
    device_check_interval = 2 # Check every 2 seconds
    
    # Track last sent commands to avoid spamming serial
    last_pump_state = None
    last_fan_state = None
    
    # Retry cooldowns
    last_pump_sent_time = 0
    last_fan_sent_time = 0
    RETRY_DELAY = 3.0 # Wait 3 seconds before resending same command if mismatch persists

    while True:
        port = get_serial_port()
        if not port:
            print("No serial port found. Retrying in 5 seconds...")
            time.sleep(5)
            continue

        print(f"Attempting to connect to {port}...")
        try:
            arduino = serial.Serial(port, 9600, timeout=1)
            time.sleep(2) # Wait for connection
            print(f"Connected to {port}!")
            
            while True:
                current_time = time.time()
                
                # 1. Check for device commands from API and retry if state mismatch
                if current_time - last_device_check > device_check_interval:
                    states = fetch_device_states()
                    for device in states:
                        name = device.get('device')
                        is_on = device.get('is_on')
                        
                        # Resend command logic: 
                        # We send command if:
                        # a) It's the first time we see this state (last_state is None)
                        # b) The state changed (is_on != last_state)
                        # c) The Arduino reports a DIFFERENT state than what we want (mismatch)
                        
                        should_send = False
                        cmd = ""

                        if name == 'pump':
                            # Check against what we *think* we sent
                            # Also ensure we actually send a command at startup regardless
                            # BUT enforce a retry delay to prevent flooding
                            
                            # Determine if we need to send/resend
                            needs_update = (last_pump_state is None) or (is_on != last_pump_state)
                            
                            # Only send if we need update AND enough time has passed since last attempt
                            if needs_update and (current_time - last_pump_sent_time > RETRY_DELAY):
                                should_send = True
                                last_pump_sent_time = current_time
                            
                            if should_send:
                                cmd = "PUMP_ON" if is_on else "PUMP_OFF"
                                print(f"Sending command to Arduino: {cmd}")
                                # Send with \n ONLY - some Arduinos dislike \r with readStringUntil('\n')
                                # Send twice with delay to ensure it catches it
                                arduino.write((cmd + '\n').encode())
                                time.sleep(0.1)
                                arduino.write((cmd + '\n').encode())
                                arduino.flush()
                                time.sleep(0.5) # Increased delay to allow Arduino processing
                                last_pump_state = is_on
                                
                        elif name == 'fan':
                            needs_update = (last_fan_state is None) or (is_on != last_fan_state)
                            
                            if needs_update and (current_time - last_fan_sent_time > RETRY_DELAY):
                                should_send = True
                                last_fan_sent_time = current_time
                                
                            if should_send:
                                cmd = "FAN_ON" if is_on else "FAN_OFF"
                                print(f"Sending command to Arduino: {cmd}")
                                # Send with \n ONLY
                                arduino.write((cmd + '\n').encode())
                                time.sleep(0.1)
                                arduino.write((cmd + '\n').encode())
                                arduino.flush()
                                time.sleep(0.5) # Increased delay to allow Arduino processing
                                last_fan_state = is_on
                                
                    last_device_check = current_time

                # 2. Read sensor data from Arduino
                if arduino.in_waiting:
                    try:
                        line = arduino.readline().decode('utf-8', errors='ignore').strip()
                        if not line:
                            continue
                        
                        # print(f"Received: {line}")
                        
                        # Parse data
                        # Expected format: PH:6.5,TDS:400,TEMP:24.0,HUM:60.0,PUMP:1,FAN:0
                        parts = line.split(',')
                        data = {}
                        for part in parts:
                            if ':' in part:
                                key, value = part.split(':')
                                data[key.strip()] = value.strip()
                        
                        # Map to database fields
                        # Ensure we handle potential parsing errors or missing keys gracefully
                        try:
                            ph_val = float(data.get('PH', 0))
                            tds_val = float(data.get('TDS', 0))
                            temp_val = float(data.get('TEMP', 0))
                            hum_val = float(data.get('HUM', 0))
                            
                            # Arduino sends 1/0 for true/false, or sometimes "1"/"0"
                            pump_val = str(data.get('PUMP', '0')).strip() == '1'
                            fan_val = str(data.get('FAN', '0')).strip() == '1'

                            # Update our knowledge of actual device state to allow resending if mismatch
                            # If we wanted Pump ON, but Arduino says OFF, we might need to resend.
                            # For simplicity, let's just log the mismatch for now.
                            if last_pump_state is not None and last_pump_state != pump_val:
                                # Mismatch detected! Reset last_pump_state to force resend next loop?
                                # print(f"Warning: Pump state mismatch! Wanted: {last_pump_state}, Got: {pump_val}")
                                # Force resend next check cycle by invalidating our memory
                                last_pump_state = None 

                            if last_fan_state is not None and last_fan_state != fan_val:
                                # print(f"Warning: Fan state mismatch! Wanted: {last_fan_state}, Got: {fan_val}")
                                last_fan_state = None

                            payload = {
                                'ph': ph_val,
                                'tds': tds_val,
                                'temperature': temp_val,
                                'humidity': hum_val,
                                'pump_status': pump_val,
                                'fan_status': fan_val,
                            }
                            
                            # print(f"Sending payload: {payload}")
                            
                            # Send to Laravel API
                            try:
                                response = requests.post(API_URL, json=payload, timeout=5)
                                if response.status_code != 201:
                                    print(f"Failed to send data: {response.status_code} - {response.text}")
                            except requests.exceptions.RequestException as e:
                                print(f"API Request Error: {e}")

                        except ValueError as e:
                             print(f"Error converting data values: {e}, Data: {data}")

                    except ValueError as e:
                        print(f"Error parsing line '{line}': {e}")
                    except Exception as e:
                        print(f"Error processing data: {e}")
                
                # Sleep briefly to avoid busy loop
                time.sleep(0.05)
                
        except serial.SerialException as e:
            print(f"Serial connection lost: {e}")
            arduino.close()
            # Reset states so we resend commands on reconnect
            last_pump_state = None
            last_fan_state = None
            
        except KeyboardInterrupt:
            print("\nExiting...")
            sys.exit(0)
        except Exception as e:
            print(f"Unexpected error: {e}")
            
        print("Reconnecting in 5 seconds...")
        time.sleep(5)

if __name__ == "__main__":
    main()

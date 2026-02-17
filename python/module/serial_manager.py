import serial
import time

class SerialManager:
    def __init__(self, port='COM5', baudrate=9600):
        self.arduino = serial.Serial(port, baudrate, timeout=1)
        time.sleep(2)

    def send(self, command):
        self.arduino.write((command + '\n').encode())

    def read_line(self):
        if self.arduino.in_waiting:
            return self.arduino.readline().decode().strip()
        return None

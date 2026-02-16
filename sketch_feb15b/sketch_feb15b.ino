#include <DHT.h>
#include <DFRobot_PH.h>
#include <GravityTDS.h>

// --------- PIN DEFINITIONS ---------
#define PH_PIN   A0
#define TDS_PIN  A1
#define DHTPIN   2

#define RELAY_PUMP 3   // IN2
#define RELAY_FAN  4   // IN3

#define DHTTYPE DHT11
#define TEMP_THRESHOLD 30.0   // Fan auto ON temp

DHT dht(DHTPIN, DHTTYPE);
DFRobot_PH phSensor;
GravityTDS tdsSensor;

float phValue = 0;
float tdsValue = 0;
float temperature = 0;
float humidity = 0;

bool pumpState = false;
bool fanState = false;
bool autoFanEnabled = true;  // automatic control active

void setup() {
  Serial.begin(9600);

  pinMode(RELAY_PUMP, OUTPUT);
  pinMode(RELAY_FAN, OUTPUT);

  // Default OFF
  digitalWrite(RELAY_PUMP, LOW);
  digitalWrite(RELAY_FAN, LOW);

  delay(2000);

  dht.begin();
  phSensor.begin();
  tdsSensor.begin();
}

void loop() {

  // --------- Read Sensors ----------
  temperature = dht.readTemperature();
  humidity = dht.readHumidity();

  int phRaw = analogRead(PH_PIN);
  float phVoltage = phRaw * 5.0 / 1023.0;
  phValue = phSensor.readPH(phVoltage, temperature);

  tdsSensor.update();
  tdsValue = tdsSensor.getTdsValue();

  // --------- AUTO FAN CONTROL ----------
  if (autoFanEnabled) {
    if (temperature >= TEMP_THRESHOLD) {
      digitalWrite(RELAY_FAN, HIGH);
      fanState = true;
    } else {
      digitalWrite(RELAY_FAN, LOW);
      fanState = false;
    }
  }

  // --------- Send Data to Python ----------
  Serial.print("PH:"); Serial.print(phValue);
  Serial.print(",TDS:"); Serial.print(tdsValue);
  Serial.print(",TEMP:"); Serial.print(temperature);
  Serial.print(",HUM:"); Serial.print(humidity);
  Serial.print(",PUMP:"); Serial.print(pumpState);
  Serial.print(",FAN:"); Serial.println(fanState);

  // --------- Manual Commands ----------
  if (Serial.available()) {
    String cmd = Serial.readStringUntil('\n');
    cmd.trim();

    if (cmd == "PUMP_ON") {
      digitalWrite(RELAY_PUMP, HIGH);
      pumpState = true;
    }
    else if (cmd == "PUMP_OFF") {
      digitalWrite(RELAY_PUMP, LOW);
      pumpState = false;
    }
    else if (cmd == "FAN_ON") {
      autoFanEnabled = false;
      digitalWrite(RELAY_FAN, HIGH);
      fanState = true;
    }
    else if (cmd == "FAN_OFF") {
      autoFanEnabled = false;
      digitalWrite(RELAY_FAN, LOW);
      fanState = false;
    }
    else if (cmd == "FAN_AUTO") {
      autoFanEnabled = true;
    }
  }

  delay(2000);
}

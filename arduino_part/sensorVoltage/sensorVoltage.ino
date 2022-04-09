const int analogInPin0 = A0;
const int analogInPin1 = A1; 
int sensorValue = 0;
float voltageValue = 0;
unsigned long lastTime = 0, sampleTime = 100;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  if(millis()-lastTime>sampleTime)
  {
    lastTime = millis();
    sensorValue0 = analogRead(analogInPin0);
    sensorValue1 = analogRead(analogInPin1); 
    voltageValue0 = scaling(sensorValue, 0, 1023, 0, 5);
    voltageValue1 = scaling(sensorValue, 0, 1023, 0, 5);
    Serial.println(voltageValue0);
    Serial.println(voltageValue1);
  }
}

float scaling(float x, float in_min, float in_max, float out_min, float out_max)
{
  return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min;
}

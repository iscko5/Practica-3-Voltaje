#include "Arduino.h"

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  int val1 = analogRead(0);
  int val2 = analogRead(1);

  Serial.print(val1);
  Serial.print(" ");
  Serial.print(val2);
  Serial.print("\n");

  delay(50);
}

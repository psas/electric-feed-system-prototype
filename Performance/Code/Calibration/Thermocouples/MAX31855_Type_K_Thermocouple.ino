#include <SPI.h>
#include "Adafruit_MAX31855.h"

#define MAXDO   3
#define MAXCS   4
#define MAXCLK  5

// initialize the Thermocouple
Adafruit_MAX31855 thermocouple(MAXCLK, MAXCS, MAXDO);

void setup() {
  while (!Serial);
  Serial.begin(9600);
  Serial.println("MAX31855 test");
  delay(500);
}

void loop() {
   Serial.print("Internal Temp = ");
   Serial.println(thermocouple.readInternal());

   double c = thermocouple.readCelsius();
   if (isnan(c)) {
     Serial.println("Something wrong with thermocouple!");
   } else {
     Serial.print("C = "); 
     Serial.println(c);
   }
   Serial.print("F = ");
   Serial.println(thermocouple.readFarenheit());

   delay(1000);
}

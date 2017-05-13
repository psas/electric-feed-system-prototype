/*
 The circuit:
 * analog sensors on analog ins 0, 1, and 2
 * SD card attached to SPI bus as follows:
 ** MOSI - pin 11
 ** MISO - pin 12
 ** CLK - pin 13
 ** CS - pin 4 (for MKRZero SD: SDCARD_SS_PIN)
 */

#include <SPI.h>
#include <SD.h>
const int chipSelect = 4;
#include "Adafruit_MAX31855.h"
#include <Servo.h>


#define MAXDO   3
#define MAXCS   4
#define MAXCLK  5

Servo myservo;

// initialize the Thermocouple
Adafruit_MAX31855 thermocouple(MAXCLK, MAXCS, MAXDO);

int pt1=A0;
int pt2=A1;
int flow_m=A2;

unsigned long t_time_update=0;

void setup() {
  Serial.begin(9600);
  while (!Serial) {
    ;
  }

  Serial.print("Initializing SD card...");

  if (!SD.begin(chipSelect)) {
    Serial.println("Card failed, or not present");
    return;
  }
  Serial.println("card initialized.");
  myservo.attach(9);
  File dataFile = SD.open("datalog.txt", FILE_WRITE);
  dataFile.print("PT1 (Psi)");
  dataFile.print("          ");
  dataFile.print("PT2 (Psi)");
  dataFile.print("        ");
  dataFile.print("TC (Celsius)");
  dataFile.print("       ");
  dataFile.println("Flow (Gpm)");
  dataFile.close();

  Serial.print("PT1 (Psi)");
  Serial.print("     ");
  Serial.print("PT2 (Psi)");
  Serial.print("     ");
  Serial.print("TC (Celsius)");
  Serial.print("     ");
  Serial.println("Flow (Gpm)");
  
  delay(500);
}

void loop() {
 float pt_1, pt_2, flowm;
 unsigned long t_time=millis();
 
 if(t_time - t_time_update < 250){
//Thermocouple ..........................................................
  //Serial.print("Internal Temp = ");
  //Serial.println(thermocouple.readInternal());
  float c = thermocouple.readCelsius();
   if (isnan(c)) {
     //Serial.println("Something wrong with thermocouple!");
   } else {
     //Serial.print("C = "); 
     //Serial.println(c);
   }
   //Serial.print("F = ");
   //Serial.println(thermocouple.readFarenheit());
   
// Pressure Transducer..........................................................
 pt_1 = analogRead(pt1);
 //Serial.print(pt1);

 pt_2=analogRead(pt2);
 //Serial.print(pt1);

 flowm=analogRead(flow_m);
 //Serial.print(pt1);

 // make a string for assembling the data to log:
  String dataString = "";
  dataString += String(pt_1);
  
  String dataString1 = "";
  dataString1 += String(pt_2);

  String dataString2 = "";
  dataString2 += String(thermocouple.readCelsius());

  String dataString3 = "";
  dataString3 += String(flowm);
  

  // open the file. note that only one file can be open at a time,
  // so you have to close this one before opening another.
  File dataFile = SD.open("datalog.txt", FILE_WRITE);

  // if the file is available, write to it:
  if (dataFile) {
    dataFile.print(dataString);
    dataFile.print("              ");
    dataFile.print(dataString1);
    dataFile.print("             ");
    dataFile.print(dataString2);
    dataFile.print("             ");
    dataFile.println(dataString3);
    dataFile.close();
    // print to the serial port too:
    Serial.print(dataString);
    Serial.print("              ");
    Serial.print(dataString1);
    Serial.print("             ");
    Serial.print(dataString2);
    Serial.print("             ");
    Serial.println(dataString3);
  }
  // if the file isn't open, pop up an error:
  else {
    Serial.println("error opening datalog.txt");
  }
 
   }
 if (t_time - t_time_update >= 400){
  t_time_update=t_time;
 }
  
  
}

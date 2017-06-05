//5/29/17 - confirmed working functions: 
//- motor control via digital pot
//- RPM reading 
//- torque reading
//- LCD output of motor load, rpm, torque
//- PLX-DAQ excel output of time, load, rpm, torque
//Should work but needs to be validated:
//-pressure transducers.

//--------load cell--------//

#include "HX711.h"
#define DOUT  8
#define CLK  9
HX711 scale(DOUT, CLK);
float calibration_factor = -117500; //-117500.00 seems to work well

float load_cell_lbs = 0;
float torque_arm = 3; // length of torque arm in inches, needs to be checked
float torque = 0;     //torque in inch-lbs

//--------LCD--------//

#include <Wire.h>  
#include <LiquidCrystal_I2C.h> // Using version 1.2.1
LiquidCrystal_I2C lcd(0x27, 2, 1, 0, 4, 5, 6, 7, 3, POSITIVE); 
int load=0; 
int LCDrate = 100;                      //number of millis between LCD refresh
unsigned long LCDlastRefresh;
int serialPrintRate = 200;              //number of millis between serial prints refresh
unsigned long serialPrintLastRefresh;

//--------programmable pot--------//

#include <SPI.h>
byte potAddress = 0x00;
int CS= 4;
unsigned long potWriteValue = 0L;

//--------input pot--------//

const int numPotReadings = 5;      // pot reading: number of readings for smoothing
int potReadings[numPotReadings];   // pot reading: the readings from the analog input
int potReadIndex = 0;              // pot reading: the index of the current reading
int potTotal = 0;                  // pot reading: the running total
int potAverage = 0;                // pot reading: the average
int potInputPin = A0;
unsigned long potRounded = 0;
int potPreRounded = 0;
int potRoundingLevel = 20;         // this is the size of the step of pot readings (1 means 1023 levels, 20 means 1023/20 levels)

//--------RPM reading--------//

volatile byte half_revolutions;
unsigned long rpm;
unsigned long timeold;
unsigned long lastRPM;
unsigned long maxRPM=0;

//--------pressure reading--------//
int pIN_read=0;
float pIN=0;
int pINinputPin = A2;
int pOUT_read=0;
float pOUT=0;
int pOUTinputPin = A3;
int pC_read=0;
float pC=0;
int pCinputPin = A4;

//------------------------setup------------------------//
 
void setup()
{
 Serial.begin(9600);
 Serial.println("CLEARDATA");  //for excel
 Serial.println("LABEL,Date,Time,millis,RPM,Load,Torque(in-lbs),pIN,pOUT");  //LABEL command creates label for columns in the first row with bold font

//--------load cell--------//

  Serial.println("HX711 calibration sketch");
  Serial.println("Remove all weight from scale");
  Serial.println("After readings begin, place known weight on scale");
  Serial.println("Press + or a to increase calibration factor");
  Serial.println("Press - or z to decrease calibration factor");

  scale.set_scale();
  scale.tare(); //Reset the scale to 0
  long zero_factor = scale.read_average(); //Get a baseline reading
  
  Serial.print("Zero factor: "); //This can be used to remove the need to tare the scale. Useful in permanent scale projects.
  Serial.println(zero_factor);

//--------RPM reading setup--------//

 attachInterrupt(1, rpm_fun, RISING);
 half_revolutions = 0;
 rpm = 0;
 timeold = 0;
 lastRPM = millis();

//--------LCD setup--------//
   
 lcd.begin(20,4); // sixteen characters across - 4 lines
 lcd.backlight();
   
//--------programmable pot setup--------//

 pinMode (CS, OUTPUT);
 SPI.begin();

//--------input pot setup--------//

 for (int potReading = 0; potReading < numPotReadings; potReading++) 
      {potReadings[potReading] = 0;}

//------------------------Loop------------------------//

}
void loop()
{

//--------serial print--------//

if (millis() > serialPrintLastRefresh + serialPrintRate) 
    {
      serialPrintLastRefresh=millis();
      
      Serial.println( (String) "DATA,DATE,TIME," + millis() + "," + rpm + "," + load + "," + torque + "," + pIN + "," + pOUT);
      
     // Serial.print("millis ");
     // Serial.print(millis());
     // Serial.print(" RPM ");
     // Serial.print(rpm);
     // Serial.print(" load ");
     // Serial.print(load);
     // Serial.print(" digipot_pos ");
     // Serial.println(potWriteValue);
    }

//--------LCD print--------//

  if (millis() > LCDlastRefresh + LCDrate) 
    {
      LCDlastRefresh=millis();

      lcd.setCursor(0,0);
      lcd.print("RPM ");
      lcd.setCursor(4,0);
      lcd.print(rpm);
      
      lcd.setCursor(10,0);
      lcd.print("motor ");
      lcd.setCursor(16,0);
      lcd.print(load);
    
      if(load < 10) 
        {
          lcd.setCursor(17,0);
          lcd.print("  ");  
        }
      if(load > 10 && load < 100) 
        {
          lcd.setCursor(18,0);
          lcd.print(" ");  
        }

      lcd.setCursor(0,1);
      lcd.print("t(inlbs) ");
      lcd.setCursor(9,1);
      lcd.print(torque);
      
      lcd.setCursor(0,2);
      lcd.print("pIN ");
      lcd.setCursor(4,2);
      lcd.print(pIN,0);

      lcd.setCursor(8,2);
      lcd.print("pOUT ");
      lcd.setCursor(13,2);
      lcd.print(pOUT,0);
      
      lcd.setCursor(0,3);
      lcd.print("time ");
      lcd.setCursor(5,3);
      lcd.print(millis()/1000);       
    }

//--------Pressure transducers--------//

  pIN_read=analogRead(pINinputPin);
  pIN=0.9123*pIN_read-130.4;
  if (pIN < 0) 
    {
      pIN=0;
    }

  pOUT_read=analogRead(pOUTinputPin);
  pOUT=0.00121*pOUT_read+1;
 if (pOUT < 0) 
  {
    pOUT=0;
  }
    
//--------Load cell--------//

  scale.set_scale(calibration_factor); //Adjust to this calibration factor

  load_cell_lbs = -scale.get_units()-.02;
  if (load_cell_lbs < 0)
    {
      load_cell_lbs=0;
    }
  torque = torque_arm*load_cell_lbs;

  //Serial.print("Reading: ");
  //Serial.print(scale.get_units(), 2);
  //Serial.print(" lbs"); //Change this to kg and re-adjust the calibration factor if you follow SI units like a sane person
  //Serial.print(" calibration_factor: ");
  //Serial.print(calibration_factor);
  //Serial.println();

  //if(Serial.available())
  //{
  //  char temp = Serial.read();
  //  if(temp == '+' || temp == 'a')
  //    calibration_factor += 10000;
  //  else if(temp == '-' || temp == 'z')
  //    calibration_factor -= 10000;
  //}

//--------RPM reading--------//
    
  if (rpm > 0) 
    {                                              //this makes sure that if it's not spinning the RPM returns to zero on the LCD 
       if (lastRPM <= (millis()-1000)) 
       {
         rpm=0;
       }
    }
  
  if (half_revolutions >= 20)                     //Update RPM every 20 counts, increase this for better RPM resolutio
   {                               
     rpm = 30*1000/(millis() - timeold)*half_revolutions;
     rpm=2*rpm;
     timeold = millis();
     half_revolutions = 0;

     if (rpm > maxRPM) 
      {
        maxRPM=rpm;
      }
   }

//--------pot reading and smoothing--------//

  potTotal = potTotal - potReadings[potReadIndex];          // subtract the last reading
  potReadings[potReadIndex] = analogRead(potInputPin);      // read from the sensor
  potTotal = potTotal + potReadings[potReadIndex];          // add the reading to the total
  potReadIndex = potReadIndex + 1;                          // advance to the next position in the array

  if (potReadIndex >= numPotReadings) {                // if we're at the end of the array...
    potReadIndex = 0;                                  // ...wrap around to the beginning
  }

  potAverage = potTotal / numPotReadings;      // calculate the average
  potPreRounded = potAverage/potRoundingLevel;
  potRounded =  potPreRounded*potRoundingLevel;                             

//--------writing to digital pot--------//

  potWriteValue = map(potRounded,20,1020,0,110);
  if (potWriteValue > 200) 
    {
       potWriteValue = 0;
    }
  if (potWriteValue > 128) 
    {
       potWriteValue = 128;
    }
  digitalPotWrite(potWriteValue);
  load = map(potWriteValue,0,110,0,100);
}  

//--------functions--------//

void rpm_fun() //Each rotation, this interrupt function is run twice
  {
    half_revolutions++;
    lastRPM=millis();
  }

int digitalPotWrite(int Value)
  {
    digitalWrite(CS, LOW);
    SPI.transfer(potAddress);
    SPI.transfer(potWriteValue);
    digitalWrite(CS, HIGH);
  }

#include <Servo.h>  // add servo library

Servo myservo;  // create servo object to control a servo

int potpin = 0;  // analog pin used to connect the potentiometer
int val;    // variable to read the value from the analog pin
unsigned long t_servo_update=0;

void setup() {
  Serial.begin(9600);
  myservo.attach(9);  // attaches the servo on pin 9 to the servo object
  delay(500);
}

void loop() {
 
 unsigned long t_servo=millis();
 
 if(t_servo - t_servo_update < 200){
  val = analogRead(potpin);            // reads the value of the potentiometer (value between 0 and 1023)
  val = map(val, 0, 1023, 0, 180);     // scale it to use it with the servo (value between 0 and 180)
  myservo.write(val);                  // sets the servo position according to the scaled value
   } else {
   }
 
 if (t_servo - t_servo_update >= 215){
  t_servo_update=t_servo;
 }
}



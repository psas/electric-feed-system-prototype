const int buttonPin = 2;     // the number of the pushbutton pin
const int ledPin =  13;      // the number of the LED pin

const int analogPin = 4;

#define PERIOD (250)

// variables will change:
int buttonState = 0;         // variable for reading the pushbutton status

int oldState = 0;
unsigned int count = 0;
unsigned long last = 0;
unsigned long next = PERIOD;
int peak = 0;


void setup() {
  Serial.begin(250000);
  // initialize the LED pin as an output:
  pinMode(ledPin, OUTPUT);
  // initialize the pushbutton pin as an input:
  pinMode(buttonPin, INPUT);
}

void loop() {
  // read the state of the pushbutton value:
//  buttonState = digitalRead(buttonPin);

  int anaState = analogRead(analogPin);
/*  if (buttonState) {
    if (anaState < 520) {
      count++;
      buttonState = 0;
    }
  } else {
    if (anaState > 560) {
      count++;
      buttonState = 1;
    }
  }*/
  if (anaState > peak) {
    peak = anaState;
  }
  //Serial.println(anaState);

  // check if the pushbutton is pressed.
  // if it is, the buttonState is HIGH:
  if (buttonState == HIGH) {
    // turn LED on:
    digitalWrite(ledPin, HIGH);
    //Serial.println("ON");
  } else {
    // turn LED off:
    digitalWrite(ledPin, LOW);
    //Serial.println("OFF");
  }


//  count += oldState ^ buttonState;
  if (millis () > next) {
    unsigned t = millis() - last;
    float f_count = count, f_t = t;
    float hz = (f_count / f_t) / 2;
  //  Serial.println(hz);


    Serial.println (peak);

    count = 0;
    peak = 0;
    last = millis ();
    next = last + PERIOD;
    
  }
}

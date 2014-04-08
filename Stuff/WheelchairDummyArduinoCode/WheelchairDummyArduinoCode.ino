/* Capstone Team C6
 * Tim Liming
 * Boe-bot wheelchair dummy code
 */

// initialize pins
int ledPins[] = {0,1,2,3,4,5};
int PING = 7;


void setup() {
  Serial.begin(9600);  //Make sure serial monitor has same baud rate 
  
  // initialize pins as output
  for (int i = 0; i < 6; i++) {
    pinMode(ledPins[i], OUTPUT);
  }
}


void loop() {
  /*
  // variables
  long duration, dist;

  // send PING pulse
  pinMode(PING, OUTPUT);
  digitalWrite(PING, HIGH);
  
  // read PING signal
  pinMode(PING, INPUT);
  duration = pulseIn(PING, HIGH);
  
  // convert to centimeters
  dist = duration / 29 / 2;
  */
  if (Serial.available() > 0) {
    
    // get a command from the serial connection
    char command = Serial.read();
    
    //if (dist > 4) {
      if (command == 'w') { // Forward
        digitalWrite(ledPins[2], HIGH);
        digitalWrite(ledPins[3], LOW);
        digitalWrite(ledPins[4], LOW);
        digitalWrite(ledPins[5], LOW);
      } 
      
      if (command == 'a') { // Left
        digitalWrite(ledPins[2], LOW);
        digitalWrite(ledPins[3], HIGH);
        digitalWrite(ledPins[4], LOW);
        digitalWrite(ledPins[5], LOW);
      }
      
      if (command == 's') { // Backwards
        digitalWrite(ledPins[2], LOW);
        digitalWrite(ledPins[3], LOW);
        digitalWrite(ledPins[4], HIGH);
        digitalWrite(ledPins[5], LOW);
      }
      
      if (command == 'd') { // Right
        digitalWrite(ledPins[2], LOW);
        digitalWrite(ledPins[3], LOW);
        digitalWrite(ledPins[4], LOW);
        digitalWrite(ledPins[5], HIGH);
      }
      
      if (command == ' ') { // Stop
        digitalWrite(ledPins[2], LOW);
        digitalWrite(ledPins[3], LOW);
        digitalWrite(ledPins[4], LOW);
        digitalWrite(ledPins[5], LOW);
      }
    //}
    
  }
}

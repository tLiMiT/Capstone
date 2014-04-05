/*Group C6
Code: Controlling RC car and sensors
 */
 
// 0 front  1 right   2 left 3 down
int trigPins[] = {A3,A1,A0,A2};  
int echoPins[] = {6,8,9,7};  
int maximumRange = 200; // Maximum range needed
int minimumRange = 0; // Minimum range needed
long duration[] = {0,0,0,0}; 
long distance[] = {0,0,0,0}; 


int timer = 1000;           // The higher the number, the slower the timing.
int ledPins[] = {0,1,2,3,4,5};       // an array of pin numbers to which LEDs are attached

void setup() {
  Serial.begin(9600);  //Make sure serial monitor baud rate same
  // use a for loop to initialize each pin as an output:     
  for (int thisPin = 0; thisPin < 6; thisPin++)  {
  pinMode(ledPins[thisPin], OUTPUT);      
 } 
 
 for (int thisPin = 0; thisPin < 4; thisPin++)  {    
 pinMode(trigPins[thisPin], OUTPUT);
 pinMode(echoPins[thisPin], INPUT);
 }
  
}


void loop() {
  
 
  
 for (int thisPin = 0; thisPin < 4; thisPin++)  {
      
 digitalWrite(trigPins[thisPin], LOW); 
 delayMicroseconds(2); 
 digitalWrite(trigPins[thisPin], HIGH);
 delayMicroseconds(10); 
 
 digitalWrite(trigPins[thisPin], LOW);
 duration[thisPin] = pulseIn(echoPins[thisPin], HIGH);
 //Calculate the distance (in cm) based on the speed of sound.
 distance[thisPin] = duration[thisPin]/58.2;
 }
 
 /*
if (distance[thisPin] >= maximumRange || distance[thisPin] <= minimumRange){
  Send a negative number to computer and Turn LED ON 
 to indicate "out of range" 
Serial.print("distance [ "); Serial.print(thisPin); Serial.println(" ]");
Serial.println("-1");
 }
else {
  Send the distance to the computer using Serial protocol, and
 turn LED OFF to indicate successful reading.
 Serial.print("distance [ "); Serial.print(thisPin); Serial.println(" ]");
 Serial.println(distance[thisPin]);
 }
 
 Delay 50ms before next reading.
 delay(50);
 */
  
  // **************************************************************************** //
   if(Serial.available() > 0) {
    char isItS = Serial.read();
 for (int thisPin = 0; thisPin < 3; thisPin++)  {
   
   // Go_______________________________________________________
 if (distance[thisPin] >20 && distance[3] <12 ){
    if(isItS == 'S') {
       Serial.write(" Backward ");
        digitalWrite(ledPins[2], HIGH);
        digitalWrite(ledPins[3], LOW);
        digitalWrite(ledPins[4], LOW);
        digitalWrite(ledPins[5], LOW);
            }
    if(isItS == 'W') { 
        Serial.write(" Forward ");
        digitalWrite(ledPins[3], HIGH);
        digitalWrite(ledPins[2], LOW);
        digitalWrite(ledPins[4], LOW);
        digitalWrite(ledPins[5], LOW);
           }
     if(isItS == 'D') {
        Serial.write(" Forward_Right ");
        digitalWrite(ledPins[4], HIGH);
        digitalWrite(ledPins[3], HIGH);
        digitalWrite(ledPins[2], LOW);
        digitalWrite(ledPins[5], LOW);
    }
    if(isItS == 'A')
    { 
        Serial.write(" Forward_Left ");
        digitalWrite(ledPins[5], HIGH);
        digitalWrite(ledPins[2], LOW);
        digitalWrite(ledPins[3], HIGH);
        digitalWrite(ledPins[4], LOW);
    }
  }
  
  // Stop_______________________________________________________
    if(distance[thisPin] < 10){
      if(thisPin == 0){
          Serial.write(" STOP-front ");
          digitalWrite(ledPins[5], LOW);
          digitalWrite(ledPins[3], LOW);
          digitalWrite(ledPins[4], LOW);
          if(isItS == 'S') {
                Serial.write(" Backward ");
                digitalWrite(ledPins[2], HIGH);
                digitalWrite(ledPins[3], LOW);
                digitalWrite(ledPins[4], LOW);
                digitalWrite(ledPins[5], LOW);
            }
        }
        
      if(thisPin == 1){
          Serial.write(" STOP-Right ");
          digitalWrite(ledPins[4], LOW);
          if(isItS == 'S') {
                Serial.write(" Backward ");
                digitalWrite(ledPins[2], HIGH);
                digitalWrite(ledPins[3], LOW);
                digitalWrite(ledPins[4], LOW);
                digitalWrite(ledPins[5], LOW);
                 }
          if(isItS == 'A'){ 
              Serial.write(" Forward_Left ");
              digitalWrite(ledPins[5], HIGH);
              digitalWrite(ledPins[2], LOW);
              digitalWrite(ledPins[3], HIGH);
              digitalWrite(ledPins[4], LOW);
                }
         }
          
      if(thisPin == 2){
          Serial.write(" STOP-Left ");
          digitalWrite(ledPins[5], LOW);
          if(isItS == 'S') {
                Serial.write(" Backward ");
                digitalWrite(ledPins[2], HIGH);
                digitalWrite(ledPins[3], LOW);
                digitalWrite(ledPins[4], LOW);
                digitalWrite(ledPins[5], LOW);
            }
          if(isItS == 'D') {
                Serial.write(" Forward_Right ");
                digitalWrite(ledPins[4], HIGH);
                digitalWrite(ledPins[3], HIGH);
                digitalWrite(ledPins[2], LOW);
                digitalWrite(ledPins[5], LOW);
            }       
      }   
  }
  
  if(distance[3] > 12){
    Serial.write(" STOP-Down ");
          digitalWrite(ledPins[5], LOW);
          digitalWrite(ledPins[3], LOW);
          digitalWrite(ledPins[4], LOW);
          if(isItS == 'S') {
                Serial.write(" Backward ");
                digitalWrite(ledPins[2], HIGH);
                digitalWrite(ledPins[3], LOW);
                digitalWrite(ledPins[4], LOW);
                digitalWrite(ledPins[5], LOW);
            }
  }
  
  // Slow Down_______________________________________________________
  if(distance[thisPin] >= 10 && distance[thisPin] <= 20)
    { 
      Serial.write(" Slow Down");
      if ( digitalRead (2) == HIGH) {
         digitalWrite(ledPins[2], LOW);
         delay(200);        
         digitalWrite(ledPins[2], HIGH);
         delay(100);
       }
       if ( digitalRead (3) == HIGH) {
         digitalWrite(ledPins[3], LOW);
         delay(200);        
         digitalWrite(ledPins[3], HIGH);
         delay(100);
       }
       if ( digitalRead (4) == HIGH) {
         digitalWrite(ledPins[4], LOW);
         delay(200);        
         digitalWrite(ledPins[4], HIGH);
         delay(100);
       }
       if ( digitalRead (5) == HIGH) {
         digitalWrite(ledPins[5], LOW);
         delay(200);        
         digitalWrite(ledPins[5], HIGH);
         delay(100);
       } 
     }  
   }    
 }
}

long microsecondsToCentimeters(long microseconds)
{
  return microseconds / 29 / 2;
}

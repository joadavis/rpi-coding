// TIRL (Turtle in Real Life) was designed and created by Ken Olsen
// see http://www.thingiverse.com/thing:1091401 and related Things
// http://www.instructables.com/id/Low-Cost-Arduino-Compatible-Drawing-Robot/
// http://www.instructables.com/id/Arduino-Drawing-Robot/
// 
// Modified for my own parts and wiring
// joadavis May 2016 (stepper only version), Dec 2016

// Assembly notes
// servo - brown to ground, red to 5V power, and white to signal (pin 8 originally spec'd)
//
// I created one version that used a third stepper in place of a servo.  Since then I ordered servos and rewired.

#include <Servo.h>

// setup servo
int servoPin = 8;
int PEN_DOWN = 80; // angle of servo when pen is down
int PEN_UP = 160;   // angle of servo when pen is up
Servo penServo;

float wheel_dia=63; //    # mm (increase = spiral out)
float wheel_base=118; //    # mm (increase = spiral in, ccw) orig 109
int steps_rev=512; //        # 512 for 64x gearbox, 128 for 16x gearbox
int delay_time=6; //         # time between steps in ms, orign 6

// Stepper sequence org->pink->blue->yel
int L_stepper_pins[] = {12, 10, 9, 11};
int R_stepper_pins[] = {4, 6, 7, 5};

int fwd_mask[][4] =  {{1, 0, 1, 0},
                      {0, 1, 1, 0},
                      {0, 1, 0, 1},
                      {1, 0, 0, 1}};

int rev_mask[][4] =  {{1, 0, 0, 1},
                      {0, 1, 0, 1},
                      {0, 1, 1, 0},
                      {1, 0, 1, 0}};

// For use with the potentiometer (enhancement from original TIRL - attached to A0)
int analogValue = 0;
int letterDistance = 40;

void setup() {
  randomSeed(analogRead(1)); 
  Serial.begin(9600);

  // initialize the LED pin as an output:
  //pinMode(ledPin, OUTPUT);
  
  for(int pin=0; pin<4; pin++){
    pinMode(L_stepper_pins[pin], OUTPUT);
    digitalWrite(L_stepper_pins[pin], LOW);
    pinMode(R_stepper_pins[pin], OUTPUT);
    digitalWrite(R_stepper_pins[pin], LOW);

    // Alternate stepper-only version
    //pinMode(PEN_stepper_pins[pin], OUTPUT);
    //digitalWrite(PEN_stepper_pins[pin], LOW);
  }
  penServo.attach(servoPin);
  Serial.println("setup");
  
  penup();
  
  delay(1000);
}


void loop(){ 

  // Control using an analog potentiometer (dial)
  analogValue = analogRead(0);
  Serial.println(analogValue);

  if (analogValue < 200) {
    right(360);
    delay(1000);
    // draw a calibration box 4 times - this is based on the original TIRL code
    pendown();
    for(int x=0; x<12; x++){
      forward(100);
      left(90);
    }
    // take a break
    penup();
    forward(200);
    pendown();
    
    for(int x=0; x<12; x++){
      forward(100);
      right(90);
    }
  }
  // Additional actions
  else if (analogValue < 400) {
    // preset 1
    Serial.println("preset 1 - name");
    //blink_pin(1);
    
    // try some letters, passing a unit size
    write_E(letterDistance);
    write_L(letterDistance);
    write_I(letterDistance);
    write_A(letterDistance);
    write_S(letterDistance);
    forward(100);
    write_O(letterDistance);
    write_L(letterDistance);
    write_I(letterDistance);
    write_V(letterDistance);
    write_E(letterDistance);
    write_R(letterDistance);
  }
  else if (analogValue < 600) {
    // preset 2
    Serial.println("preset 2 - wiggle");
    //blink_pin(2);

    for(int x=0; x<20; x++){
      forward(1);
      delay(delay_time);
    }

    delay(1000);
    
    for(int x=0; x<12; x++){
      forward(25);
      left(45);
      forward(25);
      right(45);
    }
    
    forward(25);
  }
  else {
    // preset whatever is left
    Serial.println("preset leftover");
    //blink_pin(3);
    
  }


  // Finally, leave in a good state
  penup();
  done();      // releases stepper motor
  while(1);    // wait for reset
}


// ----- HELPER FUNCTIONS -----------
int step(float distance){
  int steps = distance * steps_rev / (wheel_dia * 3.1412); //24.61
  /*
  Serial.print(distance);
  Serial.print(" ");
  Serial.print(steps_rev);
  Serial.print(" ");  
  Serial.print(wheel_dia);
  Serial.print(" ");  
  Serial.println(steps);
  delay(1000);*/
  return steps;  
}


void forward(float distance){
  int steps = step(distance);
  Serial.println(steps);
  for(int step=0; step<steps; step++){
    for(int mask=0; mask<4; mask++){
      for(int pin=0; pin<4; pin++){
        digitalWrite(L_stepper_pins[pin], rev_mask[mask][pin]);
        digitalWrite(R_stepper_pins[pin], fwd_mask[mask][pin]);
      }
      delay(delay_time);
    } 
  }
}


void backward(float distance){
  int steps = step(distance);
  for(int step=0; step<steps; step++){
    for(int mask=0; mask<4; mask++){
      for(int pin=0; pin<4; pin++){
        digitalWrite(L_stepper_pins[pin], fwd_mask[mask][pin]);
        digitalWrite(R_stepper_pins[pin], rev_mask[mask][pin]);
      }
      delay(delay_time);
    } 
  }
}


void right(float degrees){
  float rotation = degrees / 360.0;
  float distance = wheel_base * 3.1412 * rotation;
  int steps = step(distance);
  for(int step=0; step<steps; step++){
    for(int mask=0; mask<4; mask++){
      for(int pin=0; pin<4; pin++){
        digitalWrite(R_stepper_pins[pin], rev_mask[mask][pin]);
        digitalWrite(L_stepper_pins[pin], rev_mask[mask][pin]);
      }
      delay(delay_time);
    } 
  }   
}


void left(float degrees){
  float rotation = degrees / 360.0;
  float distance = wheel_base * 3.1412 * rotation;
  int steps = step(distance);
  for(int step=0; step<steps; step++){
    for(int mask=0; mask<4; mask++){
      for(int pin=0; pin<4; pin++){
        digitalWrite(R_stepper_pins[pin], fwd_mask[mask][pin]);
        digitalWrite(L_stepper_pins[pin], fwd_mask[mask][pin]);
      }
      delay(delay_time);
    } 
  }   
}


// --------- LETTER FUNCTIONS -------------
// Letters assume you are starting at the lower left corner of the letter
// start by pendown, end with penup

void write_E(float distance){
  pendown();
  left(90);
  forward(distance);
  forward(distance);
  right(90);
  forward(distance);
  // TODO: pen up around backwards
  backward(distance);
  left(90);
  backward(distance);
  right(90);
  forward(distance * 0.8);
  backward(distance * 0.8);
  left(90);
  backward(distance);
  right(90);
  forward(distance);
  
  // pen up
  penup();
  // kerning
  forward(distance * 0.5);
  // pen down
}

void write_F(float distance){
  // looks a lot like the E
  pendown();
  left(90);
  forward(distance);
  forward(distance);
  right(90);
  forward(distance);
  // TODO: pen up around backwards
  backward(distance);
  left(90);
  backward(distance);
  right(90);
  forward(distance * 0.8);
  backward(distance * 0.8);
  left(90);
  backward(distance);
  
  penup();
  right(90);
  // kerning
  forward(distance * 1.5);
}


void write_L(float distance){
  pendown();
  left(90);
  forward(distance * 2);
  backward(distance * 2);
  right(90);
  forward(distance);
  // kerning
  penup();
  forward(distance * 0.5);
}

void write_I(float distance){
  pendown();
  left(90);
  forward(distance * 2.0);
  backward(distance * 2.0);
  right(90);
  // kerning
  penup();
  forward(distance * 0.5);
}

void write_A(float distance){
  float magicDist = distance * 1.41 * 0.5;
  pendown();
  left(90);
  forward(distance);
  right(90);
  forward(distance * 0.5);
  backward(distance * 0.5);
  left(90);
  forward(distance * 0.5);
  right(45);
  forward(magicDist);
  right(90);
  forward(magicDist);
  right(45);
  forward(distance * 0.5);
  right(90);
  forward(distance * 0.5);
  backward(distance * 0.5);
  left(90);
  forward(distance);
  left(90);
  
  // kerning
  penup();
  forward(distance * 0.5);
}

void write_S(float distance){
  pendown();
  forward(distance);
  left(90);
  forward(distance);
  left(90);
  forward(distance);
  right(90);
  forward(distance);
  right(90);
  forward(distance);
  penup();
  right(90);
  forward(distance * 2.0);
  left(90);
  // kerning
  penup();
  forward(distance * 0.5);
}

void write_O(float distance){
  // "rupie O"
  float magicDist = distance * 1.41 * 0.5;
  penup();
  forward(distance * 0.5);
  left(90 + 45);
  
  pendown();
  forward(magicDist);
  right(45);
  forward(distance);
  right(45);
  forward(magicDist);
  right(90); // top
  forward(magicDist);
  right(45);
  forward(distance);
  right(45);
  forward(magicDist);
  penup(); // bottom
  
  // kerning
  left(90 + 45);
  forward(distance);
}

void write_V(float distance){
  // calculate a factor for a right angle triangle with side A of 2 and side B of .5
  float magicDist = sqrt((4 * distance * distance) + (0.25 * distance * distance));
  float acuteAngle = 180 - 14;  // turn at top of V, arctan(.5/2) = 14.03624...
  float tooAcuteAngle = 180 - 14 - 14; // turn at bottom of V

  penup();
  left(90);
  forward(distance * 2);
  right(acuteAngle);
  pendown();
  forward(magicDist);
  left(tooAcuteAngle);
  forward(magicDist);
  penup();
  right(acuteAngle);
  forward(distance * 2);

  // kerning
  left(90);
  forward(distance * 0.5);
}

void write_R(float distance){
  float legDist = distance * 1.41;
  
  pendown();
  left(90);
  forward(distance);
  forward(distance);
  right(90);
  forward(distance); // top done
  right(90);
  forward(distance);
  right(90);
  forward(distance);
  left(90 + 45);
  forward(legDist);
  
  penup();
  left(45);
  
  // kerning
  forward(distance * 0.5);
}

// ------- END LETTERS ------------

/*
void blink_pin(int blks){
  // start low
  digitalWrite(ledPin, LOW);
  for(int bl_num = 0; bl_num<blks; bl_num++) {
    digitalWrite(ledPin, HIGH);
    delay(10);
    digitalWrite(ledPin, LOW);
    delay(10);
  }
}
*/

void done(){ // unlock stepper to save battery
  for(int mask=0; mask<4; mask++){
    for(int pin=0; pin<4; pin++){
      digitalWrite(R_stepper_pins[pin], LOW);
      digitalWrite(L_stepper_pins[pin], LOW);
    }
    delay(delay_time);
  }
}


void penup(){
  delay(250);
  Serial.println("PEN_UP()");
  penServo.write(PEN_UP);
  delay(250);
}


void pendown(){
  delay(250);  
  Serial.println("PEN_DOWN()");
  penServo.write(PEN_DOWN);
  delay(250);
}


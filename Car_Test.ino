// This code was created by Gordon Quach to allow his car to drive autonomously through a 
// course with four straights and four turns. 

/* ************************************************************************************** */
// Servo header
#include <Servo.h>

/* ************************************************************************************** */
/* Global Variables                                                                       */
// Ultrasonic Range Sensor
int echoPin=2;
int trigPin=3;
long distance;

// Servo
int servoPin = 6;     // Requires PWM Port
Servo myservo;        // create servo object to control a servo
int pos = 0;

// Motor A
int pinInA=13;
int pinInB=12;
int speedpinA=11;     // Requires PWM port

// Motor B
int pinInC=9;
int pinInD=8;
int speedpinB=10;     // Requires PWM port

int motor_speed=127;

  
/* ************************************************************************************** */
/* Initial Setup                                                                          */
void setup() {
  // Report back to serial port
  Serial.begin (9600);
  
  // Ultrasonic Range Sensor
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);

  // Servo
  myservo.attach(servoPin);  // attaches the servo on the specified pin to the servo object

  // Motor A
  pinMode(pinInA,OUTPUT);
  pinMode(pinInB,OUTPUT);
  pinMode(speedpinA,OUTPUT);

  // Motor B
  pinMode(pinInC,OUTPUT);
  pinMode(pinInD,OUTPUT);
  pinMode(speedpinB,OUTPUT);
  
}
/* ************************************************************************************** */
/* Main Loop                                                                              */
void loop() {

  while( getDistance() != 25 )
  {
    motor_speed = 127;        // Set your speed
    goForward();              // Set the direction of the motors
    delay(300);               // Do the previous setup for 1/2 second
    
    if (getDistance() >= 10 && getDistance() <= 25)
    {
      turnRight();
      delay(300);
      goForward();
    }
    else if (getDistance() >= 0 && getDistance() < 10)
    {
      motor_speed = 200;        // Set your speed
      goBackward();
      delay(3000);
    }
    else
    {
      goForward();
    } 
    
  }
   
}
/* ************************************************************************************** */
/* Function Declarations                                                                  */

/* ********************************************** */
/* Ultrasonic Range Sensor Functions              */
long getDistance() {
  long duration;
  long distance;
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  duration = pulseIn(echoPin, HIGH);

  // Note: If you prefer to work in centimeters, remove the backslashes from the following 
  // line and add in the same two backslashes on the following line with inches.
  //distance = (duration/2) / 29.1;    // Convert to Centimeters
  distance = (duration/2) / 73.746;   // Convert to Inches

  return distance;
}

/* ********************************************** */
/* Motor Functions                                */

// The next four function are the base functions needed to get the motors turning. These
// are programmed at a very physical level. If the wheel does not go the right direction,
// switch the HIGH and LOW.
void rightWheelForward() {
  // Note: Pins A and B are going to be opposite each other at all times. This is
  // required of the L298n motor controller.
  digitalWrite(pinInA,LOW);
  digitalWrite(pinInB,HIGH);
  digitalWrite(speedpinA,motor_speed);
}
void rightWheelReverse() {
  // Note: Pins A and B are going to be opposite each other at all times. This is
  // required of the L298n motor controller.
  digitalWrite(pinInA,HIGH);
  digitalWrite(pinInB,LOW);
  digitalWrite(speedpinA,motor_speed);
}
void leftWheelForward() {
  // Note: Pins C and D are going to be opposite each other at all times. This is
  // required of the L298n motor controller.
  digitalWrite(pinInC,HIGH);
  digitalWrite(pinInD,LOW);
  digitalWrite(speedpinB,motor_speed);
}
void leftWheelReverse() {
  // Note: Pins C and D are going to be opposite each other at all times. This is
  // required of the L298n motor controller.
  digitalWrite(pinInC,LOW);
  digitalWrite(pinInD,HIGH);
  digitalWrite(speedpinB,motor_speed);
}
void stopMotors() {
  // Note: We are setting the speed to 0 to stop the motors.
  digitalWrite(speedpinA,0);
  digitalWrite(speedpinB,0);
}

// The next set of functions are higher level functions in order to utilize what is
// happening at a physical level. We are using regular words that most people would
// understand.
void goForward() {
  rightWheelForward();
  leftWheelForward(); 
}
void goBackward() {
  rightWheelReverse();
  leftWheelReverse();
}
void turnRight() {
  rightWheelReverse();
  leftWheelForward();   
}
void turnLeft() {
  rightWheelForward();
  leftWheelReverse();
}


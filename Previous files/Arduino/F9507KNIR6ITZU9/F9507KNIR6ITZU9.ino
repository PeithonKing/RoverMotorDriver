//MOTORS
//declaring the motor variables and current speed
int in1 = 9;
int pwm1 = 6;
int in2 = 4;
int pwm2 = 5;
int cspeed =0;

//ENCODER
//declaring the variables used for the encoder 
int encoder=2;
float rps;
float rpm;
volatile byte pulses;
unsigned long timeold;
float s;

#include <Wire.h>  //including the wire library since the LCD is on I2C

//LCD
//declaring all things needed for LCD
#include <LCD.h>
#include <LiquidCrystal_I2C.h>
#define I2C_ADDR 0x3F 
#define Rs_pin 0
#define Rw_pin 1
#define En_pin 2
#define BACKLIGHT_PIN 3
#define D4_pin 4
#define D5_pin 5
#define D6_pin 6
#define D7_pin 7
LiquidCrystal_I2C lcd(I2C_ADDR, En_pin, Rw_pin, Rs_pin, D4_pin, D5_pin, D6_pin, D7_pin);

//IR
//declaring all things needed for Infra red
#include <IRremote.h>
int RECV_PIN = 11;
IRrecv irrecv(RECV_PIN);
decode_results results;
#define code1 0xFD8877 
#define code2 0xFD9867 

//this subprogram will run when interrupt is triggered
void counter()
{
  pulses++; //every time this subprogram runs, the number of pulses is increased by 1 
  s=s+20.42; //and the variable s is increased by 20.42cm, which is the circumference of my wheel, s stands for path
}

void setup() {
   irrecv.enableIRIn();

   lcd.begin (16, 2);
   lcd.setBacklightPin(BACKLIGHT_PIN, POSITIVE);
   lcd.setBacklight(HIGH);
   lcd.home (); 
   lcd.print("Speed");
   lcd.setCursor(8,0);
   lcd.print("Path");

    pinMode(encoder,INPUT);
    pinMode(in1, OUTPUT);
    pinMode(in2, OUTPUT);
    pinMode(pwm1, OUTPUT);
    pinMode(pwm2, OUTPUT);

    digitalWrite(in1,HIGH);
    analogWrite(pwm1,cspeed);
    digitalWrite(in2,HIGH);
    analogWrite(pwm2,cspeed);

    attachInterrupt(0,counter,RISING);  //attaching the interrupt and declaring the variables, one of the interrupt pins on Nano is D2, and has to be declared as 0 here
    pulses=0;
    rps=0;
    rpm=0;
    timeold=0;
    s=0;    
}

void loop() {
  if (irrecv.decode(&results)) { //part of the code for IR manipulation
  unsigned int vr= results.value;
  switch(vr) {
    case code1:
    if (cspeed!= 0) {
      cspeed=cspeed-20;
    }
    motors();
    break;

    case code2:
    cspeed=cspeed+20;
    motors();
    break;

  }
  irrecv.resume();
}
 if (pulses>=1) { //this part of the code calculates the rpm and rps in a way that every time the magnet passes by the sensor, the time between the pulses is measured and rpm and rps is calculated
    detachInterrupt(0);
    rpm = 60000.0/(millis()-timeold)*pulses;
    rps=rpm/60.0;
    timeold = millis();
    pulses=0;

    lcd.setCursor (0,1); 
    lcd.print(rps);
    lcd.print("rps ");
    lcd.setCursor(8,1);
    lcd.print(s);
    lcd.print("cm");
    attachInterrupt(0,counter,RISING);
  }
}

void motors()
{
  digitalWrite(in1,HIGH);
  analogWrite(pwm1,cspeed);
  digitalWrite(in2,HIGH);
  analogWrite(pwm2,cspeed);
}


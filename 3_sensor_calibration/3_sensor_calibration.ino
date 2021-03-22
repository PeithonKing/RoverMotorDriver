int m1=11, m2=10;                // for motors
int sp1=A1, sp2=A2, sp3=A3;      // senor pins
int s1, s2, s3;                  // sensed values
int flag=0, done=0, last=0;      // will be used for initial calibration
// initial calibratiion will be done with sensor 1



void setup() {
  pinMode(m1, OUTPUT);
  pinMode(m2, OUTPUT);
  pinMode(sp1, INPUT);
  pinMode(sp2, INPUT);
  pinMode(sp3, INPUT);
  Serial.begin(9600);
}

void loop() {
digitalWrite(m1, HIGH);
digitalWrite(m2, LOW);

s1 = analogRead(sp1);
s2 = analogRead(sp2);
s3 = analogRead(sp3);
Serial.println(s1);
Serial.print(" ");
Serial.print(s2);
Serial.print(" ");
Serial.print(s3);
Serial.print(" ");



delay(50);
}

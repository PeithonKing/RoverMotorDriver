int RPM=6, wait;
int m1=11, m2=10;                // for motors
int sp1=A1, sp2=A2, sp3=A3;      // sensor pins
int s1, s2, s3;                  // sensed values
int flag=0, last=0;      // will be used for initial calibration
// initial calibratiion will be done with sensor 1
int sen1[180], sen2[180], sen3[180], i=0;


void setup() {
  pinMode(m1, OUTPUT);
  pinMode(m2, OUTPUT);
  pinMode(sp1, INPUT);
  pinMode(sp2, INPUT);
  pinMode(sp3, INPUT);
  Serial.begin(9600);
  while(i<180){
    s1 = analogRead(sp1);
    s2 = analogRead(sp2);
    s3 = analogRead(sp3);
    if(flag==0){
      if(s1<last){
        if(s1==550){
          flag=1;
          Serial.println("Started Recording!");
        }
      }
    }

  if(flag==1){
      sen1[i]=s1;
      sen2[i]=s2;
      sen3[i]=s3;
      Serial.print("\nAt ");
      Serial.print(i);
      Serial.print(" degree sensor 1 = ");
      Serial.print(sen1[i]);
      Serial.print(", sensor 2 = ");
      Serial.print(sen2[i]);
      Serial.print(", sensor 3 = ");
      Serial.print(sen3[i]);
      i+=2;
    }
    digitalWrite(m1, HIGH);
    digitalWrite(m2, LOW);
    // Serial.println(readval);
    wait = 1000/(6*RPM);
    delay(wait);
    last=s1;  
  }
  digitalWrite(m1, LOW);
  digitalWrite(m2, LOW);
}

void loop() {
//digitalWrite(m1, HIGH);
//digitalWrite(m2, LOW);
//
s1 = analogRead(sp1);
s2 = analogRead(sp2);
s3 = analogRead(sp3);
<<<<<<< HEAD
Serial.print(s1);
Serial.print(" ");
Serial.print(s2);
Serial.print(" ");
Serial.print(s3);
Serial.println(" ");
=======
//Serial.println(s1);
//Serial.print(" ");
//Serial.print(s2);
//Serial.print(" ");
//Serial.print(s3);
//Serial.print(" ");
>>>>>>> 3e3bfb054a5b4f27b9d2c1a7f0e618e1ec73046e



delay(200);
}

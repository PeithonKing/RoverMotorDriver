int RPM=6, wait;
int m1=11, m2=10;                // for motors
int sp1=A1, sp2=A2, sp3=A3;      // sensor pins
int s1, s2, s3;                  // sensed values
int flag=0, last=0;      // will be used for initial calibration
// initial calibratiion will be done with sensor 1
int sen1[180], sen2[180], sen3[180], i=0, go_to;


void setup() {
  pinMode(m1, OUTPUT);
  pinMode(m2, OUTPUT);
  pinMode(sp1, INPUT);
  pinMode(sp2, INPUT);
  pinMode(sp3, INPUT);
  Serial.begin(9600);
  while(i<360){
    s1 = analogRead(sp1);
    s2 = analogRead(sp2);
    s3 = analogRead(sp3);
    digitalWrite(m1, HIGH);
    digitalWrite(m2, LOW);
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
//      Serial.print("\nAt ");
//      Serial.print(i);
//      Serial.print(" degree sensor 1 = ");
//      Serial.print(sen1[i]);
//      Serial.print(", sensor 2 = ");
//      Serial.print(sen2[i]);
//      Serial.print(", sensor 3 = ");
//      Serial.print(sen3[i]);
      i++;
    }
    // Serial.println(readval);
    wait = 500/(3*RPM);
    delay(wait);
    last=s1;  
  }
  digitalWrite(m1, LOW);
  digitalWrite(m2, LOW);
}

void loop() {
 Serial.println("Manually rotate the motor and then press enter!");
 Serial.println("The code will find the position of the wheel after that!");
 while(Serial.available() == 0){}

s1 = analogRead(sp1);
s2 = analogRead(sp2);
s3 = analogRead(sp3);

//  Serial.println(s1);
//  Serial.print(" ");
//  Serial.print(s2);
//  Serial.print(" ");
//  Serial.print(s3);
//  Serial.print(" ");

for(i=0; i<360; i++){
  if(s1 > (sen1[i]-2) && s1 < (sen1[i]+2)){
    if(s2 > (sen2[i]-2) && s2 < (sen2[i]+2)){
      if(s3 > (sen3[i]-2) && s3 < (sen3[i]+2)){
        Serial.println("Position of the wheel is ");
        Serial.print(i);
        Serial.print(" degree!");
      }
    }
  }
}
  delay(5000);
}

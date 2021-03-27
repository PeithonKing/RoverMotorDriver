unsigned long RPM, T, taken=0;

int m1=11, m2=10;                // for motors
int sp1=A1;                      // sensor pin
int s1;                          // sensed values
int mean=530, flag=0;            // mean value for this sensor

void setup() {
  pinMode(m1, OUTPUT);
  pinMode(m2, OUTPUT);
  pinMode(sp1, INPUT);
  Serial.begin(9600);
  digitalWrite(m2, LOW);
  
//  Serial.print("Reading = ");
//  Serial.println(s1);

while(true){
  digitalWrite(m1, HIGH);
  while(flag<=2){
    s1 = analogRead(sp1);
      if(s1==mean){
        if(flag==0){
          Serial.println("STARTED!");
          T = millis(); 
          flag++;
          delay(1000);
          continue;
          }
        if(flag==1){
          flag++;
          Serial.println("Halfway Through!");
          delay(1000);
          continue;
        }
        if(flag==2){taken=T-taken; flag++;}
        continue;
      }
  }
  RPM = 30000/taken;
  
    Serial.println(RPM);
    flag=0;
    digitalWrite(m1, LOW);
    delay(5000);
}
}

void loop() {
//    
//  s1 = analogRead(sp1);
////  Serial.print("Reading = ");
////  Serial.println(s1);
//
//  if(s1==mean){
//    if(flag==0){
//      Serial.println("STARTED!");
//      T = millis(); 
//      flag++;
//      delay(1000);
//      continue;
//      }
//    if(flag==1){
//      flag++;
//      Serial.println("Halfway Through!");
//      delay(1000);
//      continue;
//    }
//    if(flag==2){taken=T;}
//    continue;
//  }
//RPM = 30000/taken;
//if(flag==2){
//  Serial.println(RPM);
//  delay(5000);
//  flag=0;
//}
}

float RPM=6.0;
int a=11;
int b=10;
int readpin=A3, readval, flag=0, done=0, last=0;
int Cal[360], i=0;
float wait;


void setup() {
  pinMode(a, OUTPUT);
  pinMode(b, OUTPUT);
  pinMode(readpin,INPUT);
  Serial.begin(9600);

  while(i<360){
    readval=analogRead(readpin);
    if(done==0){
      if(readval<last){
        if(readval==580){
          flag=1;
          done=1;
          Serial.println("Started Recording!");
        }
      }
    }

    if(flag==1){
      Cal[i]=readval;
      Serial.print("\nAt ");
      Serial.print(i);
      Serial.print(" degree value = ");
      Serial.print(Cal[i]);
      i++;
    }
    digitalWrite(a, HIGH);
    digitalWrite(b, LOW);
    // Serial.println(readval);
    wait = 1000/(6*RPM);
    delay(wait);
    last=readval;
  }

//  for(i=0; i<360; i++){
//        Serial.print("\nAt ");
//        Serial.print(i);
//        Serial.print(" degree value = ");
//        Serial.print(Cal[i]);
//       // Serial.printf("\nAt ", i,  " degree value = ", Cal[i]);
//      }

  Serial.println("\n***End***");
    digitalWrite(a, LOW);
    digitalWrite(b, LOW);
}

void loop() {
  
}

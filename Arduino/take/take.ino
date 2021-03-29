int a=11;
int b=10;
int readpin=A3, readval, flag=0, done=0, last=0;
int Cal[180], i=0;
int pos=180, input;

void setup() {
  pinMode(a, OUTPUT);
  pinMode(b, OUTPUT);
  pinMode(readpin,INPUT);
  Serial.begin(9600);

  while(i<180){
    readval=analogRead(readpin);
    if(flag==0){
      if(readval<last){
        if(readval==580){
          flag=1;
          done=1;
          Serial.println("Started Recording!");
        }
      }
    }
  
    if(done==1){
      Cal[i]=readval;
      i++;
    }
    digitalWrite(a, HIGH);
    digitalWrite(b, LOW);
    // Serial.println(readval);
    delay(30.3333);
    last=readval;
  }

  digitalWrite(a, LOW);
  digitalWrite(b, LOW);

  for(i=0; i<360; i++){
        Serial.print("\nAt ");
        Serial.print(i);
        Serial.print(" degree value = ");
        Serial.print(Cal[i]);
       // Serial.printf("\nAt ", i,  " degree value = ", Cal[i]);
      }
  Serial.println("\n***End***");
    digitalWrite(a, LOW);
    digitalWrite(b, LOW);
}

void loop() {
  Serial.println("Enter the angle");
  while(Serial.available() == 0){}
  input=Serial.parseInt();
  
}

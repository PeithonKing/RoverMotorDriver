int a=13;
int b=12;
int c=11;
int d=10;
int f=9;
int g=8;
int e=7;
int readpin=A3, readvalue;
float V2;

//digitalWrite(a, HIGH);
//digitalWrite(b, HIGH);
//digitalWrite(c, HIGH);
//digitalWrite(d, HIGH);
//digitalWrite(e, HIGH);
//digitalWrite(f, HIGH);
//digitalWrite(g, HIGH);
//delay(1000);

//digitalWrite(a, LOW);
//digitalWrite(b, LOW);
//digitalWrite(c, LOW);
//digitalWrite(d, LOW);
//digitalWrite(e, LOW);
//digitalWrite(f, LOW);
//digitalWrite(g, LOW);
//delay(1000);




void setup() {
  pinMode(13, OUTPUT);
  pinMode(12, OUTPUT);
  pinMode(11, OUTPUT);
  pinMode(10, OUTPUT);
  pinMode(9, OUTPUT);
  pinMode(8, OUTPUT);
  pinMode(7, OUTPUT);
  pinMode(6, OUTPUT);
  pinMode(readpin,INPUT);
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
//digitalWrite(6, HIGH);
digitalWrite(c, HIGH);
digitalWrite(d, LOW);

readvalue=analogRead(readpin);
// V2=(5.0/1023.0)*readvalue;
Serial.println(readvalue);
delay(30);

//if(V2<0.5){
//  // 0
//digitalWrite(a, HIGH);
//digitalWrite(b, LOW);
//digitalWrite(c, LOW);
//digitalWrite(d, LOW);
//digitalWrite(e, LOW);
//digitalWrite(f, LOW);
//digitalWrite(g, LOW);
//}
//
//else if(V2<1.5){
//  // 1
//digitalWrite(a, HIGH);
//digitalWrite(b, HIGH);
//digitalWrite(c, HIGH);
//digitalWrite(d, LOW);
//digitalWrite(e, LOW);
//digitalWrite(f, HIGH);
//digitalWrite(g, HIGH);
//}
//
//else if(V2<2.5){
//  // 2
//digitalWrite(a, LOW);
//digitalWrite(b, HIGH);
//digitalWrite(c, LOW);
//digitalWrite(d, LOW);
//digitalWrite(e, HIGH);
//digitalWrite(f, LOW);
//digitalWrite(g, LOW);
//}
//
//else if(V2<3.5){
//  // 3
//digitalWrite(a, LOW);
//digitalWrite(b, HIGH);
//digitalWrite(c, LOW);
//digitalWrite(d, LOW);
//digitalWrite(e, LOW);
//digitalWrite(f, LOW);
//digitalWrite(g, HIGH);
//}
//
//else if(V2<4.5){
//  // 4
//digitalWrite(a, LOW);
//digitalWrite(b, LOW);
//digitalWrite(c, HIGH);
//digitalWrite(d, LOW);
//digitalWrite(e, LOW);
//digitalWrite(f, HIGH);
//digitalWrite(g, HIGH);
//}
//
//else{
//  // 5
//digitalWrite(a, LOW);
//digitalWrite(b, LOW);
//digitalWrite(c, LOW);
//digitalWrite(d, HIGH);
//digitalWrite(e, LOW);
//digitalWrite(f, LOW);
//digitalWrite(g, HIGH);
//}
}

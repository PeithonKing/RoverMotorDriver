int m1=11, m2=10;                // motor
int sp1=A1, sp2=A2, sp3=A3;      // sensor pins
int s1, s2, s3;                  // sensed values

void setup() {
  pinMode(m1, OUTPUT);
  pinMode(m1, OUTPUT);
  digitalWrite(m1, HIGH);
  digitalWrite(m2, LOW);
  pinMode(sp1, INPUT);
  pinMode(sp2, INPUT);
  pinMode(sp3, INPUT);
  Serial.begin(9600);
}

void loop() {
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

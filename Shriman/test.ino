

void setup()
{   
    DDRD = B11111111;
}

void loop()
{
    delay(100);
    PORTD = B10101011;
    delay(100);
    PORTD = B10101010;


}
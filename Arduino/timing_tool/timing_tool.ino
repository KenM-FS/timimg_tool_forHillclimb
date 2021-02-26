void setup() {
  // put your setup code here, to run once:
  // disable Timer0 for stable serial com
  TIMSK0 = 0;
  pinMode(2, INPUT);
  // initial bps is 9600 in windows
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  // it seems faster to use while with serial com
  while(1){
    if(digitalRead(2) == HIGH){
      Serial.write(1);
    }
  }
}

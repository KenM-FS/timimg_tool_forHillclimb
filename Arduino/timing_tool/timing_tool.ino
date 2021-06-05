void setup() {
  // disable Timer0 for stable serial com
  TIMSK0 = 0;
  pinMode(2, INPUT);
  // initial bps is 9600 in windows
  Serial.begin(9600);
}

void loop() {
  // minimun implementation to send signal
  // it seems faster to use while in loop
  while(1){
    if(digitalRead(2) == HIGH){
      Serial.write(1);
    }
  }
}

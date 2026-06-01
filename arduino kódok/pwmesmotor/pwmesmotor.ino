/*
Ha feltekered maxra akkor a lendület miatt, ha vissza is tekered a motor nem lassul
*/

#include <Servo.h>

Servo esc;
float a, n;


void setup() {
  esc.attach(9);
  Serial.begin(9600);

  esc.writeMicroseconds(1000); 
  delay(3000);
}

void loop() {
  a = analogRead(A0);
  n = a*1000/1024+1000;
  //n = a*75/1024+1290; //1290-től 1365-ig

  if (n < 1301){
    esc.writeMicroseconds(1000);
    Serial.print("UNSTABLE ");
  } else if (n < 1365) {
    esc.writeMicroseconds(n);
    Serial.print("STABLE "); 
  } else {
    esc.writeMicroseconds(1365);
    Serial.print("POWERSUPPLY TOO WEAK CAPPED AT 1365 ");
  }

  Serial.println(String(int(a))+" "+String(int(a/10.24))+"% "+String(int(n)));
}

/*
 * bleSender.ino
 * 
 *  Used to transmit data (id from a nfc tag) received through serial
 * to send the same data through ble
 * 
 * almeida.rodrigo@ua.pt
 * October 2016
 */

#include <RFduinoBLE.h>

char state = 0;
int atraso=200; //ms
String str="";
char arr[10];

void setup() {
  Serial.begin(9600);
  
  RFduinoBLE.advertisementData = "adv";
  RFduinoBLE.deviceName="rfidDeviceTest3";
  RFduinoBLE.begin();
}


void loop()
{
  RFduino_ULPDelay(atraso);

  Serial.flush();
  if (Serial.available() > 0) {
  
    for(int i=0; i < 11; i++){
      state = Serial.read();  // read the incoming byte:
      arr[i]=(state);
      //Serial.print(state);
    }
    RFduinoBLE.send(arr,10);
  }

  //RFduino_ULPDelay(atraso);
}




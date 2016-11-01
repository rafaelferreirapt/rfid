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
  
    for(int i=0; i < 4; i++){
      state = Serial.read();  // read the incoming byte:
      //Serial.println(state);
      if(isAscii(state)){
        arr[i] = (state);
      }else{
        arr[i] = '0'; //make sure that all id's have 10 digits
      //Serial.print(0x00);
      }
    }
    RFduinoBLE.send(arr,4);
  }

  //RFduino_ULPDelay(atraso);
}




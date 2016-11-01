//This example reads all MIFARE memory block from 0x00 to 0x63. 
//It is tested with a new MIFARE 1K cards. Uses default keys for authenication.
//Contributed by Seeed Technology Inc (www.seeedstudio.com)
 
#include <PN532.h>
#include <SPI.h>

String lastdata="";
String data="";
/*Chip select pin can be connected to D10 or D9 which is hareware optional*/
/*if you the version of NFC Shield from SeeedStudio is v2.0.*/
#define PN532_CS 10
 
PN532 nfc(PN532_CS);
 
#define  NFC_DEMO_DEBUG 1
 
void setup(void) {
#ifdef NFC_DEMO_DEBUG
  Serial.begin(9600);
  //Serial.println("Hello!");
#endif
  nfc.begin();
 
  uint32_t versiondata = nfc.getFirmwareVersion();
  if (! versiondata) {
#ifdef NFC_DEMO_DEBUG
    //Serial.print("Didn't find PN53x board");
#endif
    while (1); // halt
  }
#ifdef NFC_DEMO_DEBUG
  // Got ok data, print it out!
  //Serial.print("Found chip PN5"); 
  //Serial.println((versiondata>>24) & 0xFF, HEX);
  //Serial.print("Firmware ver. "); 
  //Serial.print((versiondata>>16) & 0xFF, DEC);
  //Serial.print('.'); 
  //Serial.println((versiondata>>8) & 0xFF, DEC);
  //Serial.print("Supports "); 
  //Serial.println(versiondata & 0xFF, HEX);
#endif
  // configure board to read RFID tags and cards
  nfc.SAMConfig();
}
 
void loop(void) {
  uint32_t id;
  // look for MiFare type cards
  id = nfc.readPassiveTargetID(PN532_MIFARE_ISO14443A);
  //Serial.print(id);
  
  if (id != 0)
  {
#ifdef NFC_DEMO_DEBUG
    //Serial.print("Read card #");
    //Serial.println(id);
    //Serial.println();
#endif
    uint8_t keys[]= {0xFF,0xFF,0xFF,0xFF,0xFF,0xFF};// default key of a fresh card
    uint8_t blockn=0;
    data = "";
    //Serial.print("here3");
    for(blockn=0;blockn<2;blockn++) 
    {
      //Serial.print(blockn);
      if(nfc.authenticateBlock(1, id ,blockn,KEY_A,keys)) //authenticate block blockn
      {
        //if authentication successful
        uint8_t block[16];
         uint8_t newblock[4];

          if(blockn == 1){
          if(nfc.readMemoryBlock(1,1, newblock)){   
             for(uint8_t i2=0;i2<4;i2++){
              //Serial.print(newblock[i2]);
              data = data + newblock[i2];
            }
            if(data.length() != 0 && !data.equals(lastdata))
              Serial.print(data);
            lastdata = data;
          }
        }
      }
    }
  }
  //Serial.println("the end");
  //delay(2000);
}

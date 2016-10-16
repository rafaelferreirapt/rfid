/*
 * nfc.ino 
 * 
 *  This program was adapted from the available manufacturer example.
 * This program will send the data (id from a nfcTag) through serial
 * 
 * Made some changes in the library function: nfc.readPassiveTargetID
 *  
 *  almeida.rodrigo@ua.pt
 *  October 2016
 */


//This example reads all MIFARE memory block from 0x00 to 0x63. 
//It is tested with a new MIFARE 1K cards. Uses default keys for authenication.
//Contributed by Seeed Technology Inc (www.seeedstudio.com)
 
#include <PN532.h>
#include <SPI.h>
#include <Print.h>
 
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
  ///Serial.println("Reader is ready... "); 
#endif
  // configure board to read RFID tags and cards
  nfc.SAMConfig();
}
 
void loop(void) {
  uint32_t id=0;
  
  // look for MiFare type cards
  id = nfc.readPassiveTargetID(PN532_MIFARE_ISO14443A);
 //id=1;
  if (id != 0)
  {
#ifdef NFC_DEMO_DEBUG
    //Serial.println();
    //Serial.print("Read card #");
    Serial.print(id);
    //Serial.println();
#endif
  }
  //delay(2000);
  delay(1000);
}

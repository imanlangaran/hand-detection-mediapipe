#include <TM1637Display.h>

TM1637Display display(2, 3);
uint8_t data[] = { 0x00, 0x00, 0x00, 0x00 };
// int c = 0;

String input = "";
short index_comma = 0;
long lm;

void setup() {
  Serial.begin(9600);
  Serial.println("setup done...");

  display.setBrightness(5);

}

void loop() {
  if(Serial.available()){
    // lm = millis();
    // input = Serial.readString();
    // index_comma = input.indexOf(',');
    // data[3] = display.encodeDigit(input.substring(0, index_comma).toInt());
    // data[0] = display.encodeDigit(input.substring(index_comma+1).toInt());
    data[0] = display.encodeDigit(Serial.parseInt());
    data[3] = display.encodeDigit(Serial.parseInt());
    // Serial.println(index_comma);
    // Serial.println(input.substring(0, index_comma));
    // Serial.println(input.substring(index_comma+1));
    display.setSegments(data);
    // delay(10);
    // Serial.println(millis()-lm);
    Serial.read();
  }
  // c++;
  // data[0] = display.encodeDigit(c);
  // dispaly.setSegments(data);
  // delay(1000);


}

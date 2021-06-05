# timimg_tool_forHillclimb
Show current time by photoelectric sensor using Arduino Uno.

Arduino Unoを介した光電センサで現在時刻を表示する．

## Specifications
### Photoelectric Sensor
[E3JK-RR12-C](https://www.fa.omron.co.jp/product/item/73/) from OMRON

### Arduino
[Arduino Uno](https://store.arduino.cc/usa/arduino-uno-rev3)

Install [this program](./Arduino/timing_tool/timing_tool.ino) to use.

The only process that Arduino hadle is to send signals by serial comm when the photoelectric sensor reacts. 

### [timing_tool.py](./timing_tool.py)
There are two options to show (record) time. 
- By signal from Arduino (photoelectric sensor)
- By button

[WIP] Chose port to communicate with Arduino

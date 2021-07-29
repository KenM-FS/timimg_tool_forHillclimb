# timimg_tool_forHillclimb
Show current time by photoelectric sensor using Arduino Uno.

Arduino Unoを介した光電センサで現在時刻を表示する．

---
## Specifications
### Photoelectric Sensor
[E3JK-RR12-C](https://www.fa.omron.co.jp/product/item/73/) from OMRON

Wires
- Power supply (24-240V AC or DC) -> Blue & Brown
- Mode L
    - Not Cut -> White to Gray, Cut -> White to Black
- Mode D
    - Not Cut -> White to Black, Cut -> White to Gray

### Arduino
[Arduino Uno](https://store.arduino.cc/usa/arduino-uno-rev3)

Install [this program](./Arduino/timing_tool/timing_tool.ino) to use.

Wirings
- Arduino GND to Sensor White
- Arduino 2 pin to Sensor Black in Mode L (Gray if Mode D)

(Connecting GND to Gray or Black adn 2 pin to white also works.)

When the sensor is cut, Arduino send "1" to PC by serial communication. If not, nothing is sent.

### [timing_tool.py](./timing_tool.py)
There are two options to show (record) time. 
- By signal from Arduino (photoelectric sensor)
- By button

[WIP] Chose port to communicate with Arduino

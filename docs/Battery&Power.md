# Battery Drive & AC Adapter Drive

## Problem
According to the [specification](https://www.fa.omron.co.jp/product/item/73/), output is over DC5V. However, it is unstable regardless power supply, battery drive or AC adapter drive, decreases to aroud 2mV. Arduino needs 5V for digitalRead, so it's necessary to find out the reason of this phenomenon and need to stabilize output voltage.

## Hypothesis
### Hypothesis 1
Output voltage decreases in battery drive, not in AC adapter drive.
### Hypothesis 2
The wires should be connected, through Arduino in this case, to get stable voltage.

## Methods
Power Supplies
- 17 series connected 1.5 AA batteries, 25.5V
- AC adapter, DC24V

Arduino
- Built in Arduino
- Free(not built in) Arduino

Photoelectric Sensor
- Built in sensor
- Free(not built in) sensor

Computer

### Experiment 1
Change only power supply, use same equipment with others. Measure output voltage and check whether Arduino serial output.

### Experiment 2
Disconnect Arduino and measure output voltage, use both power supply. Check if voltage changes when Arduino is connected.

## Results

### Experiment 1
Free sensor and built in Arduino is used for this experiment.

Built in Arduino was broken with outputting serial com all the time, and unable to write in. Free Arduino works with battery drive. The experiment is cancelled.

# QHRC Breadboard Layout Guide

## 1. Power Rails Setup
```
+5V Rail (Top):
[+]------------------------------- (+5V from source)
[-]------------------------------- (GND from source)

+5V Rail (Bottom):
[+]------------------------------- (bridge from top)
[-]------------------------------- (bridge from top)
```

## 2. 555 Timer Base Frequency (4.37 Hz)
```
    +5V
     │
   10kΩ
     │        ┌────────┐
     ├──[1]───┤  555   │
     ├──[8]───┤ Timer  │
     │   [7]──┤        │
     │   [6]──┤        │
100kΩ POT     │        │
     │   [2]──┤        │
     ├──[4]───┤        │
     │        └────────┘
    0.1µF        [3]
     │           │
    GND         Out → To MOSFET
```

## 3. MOSFET Driver (Primary)
```
From 555
   │
  10kΩ    IRF530
   │     ┌────┐
   ├─────┤ G  │
   │     │    │
  1kΩ    │ D  │
   │     │    │    Primary
   │     │ S  │      Coil
  GND    └────┘       │
                      │
                     GND
```

## 4. Resonance Monitor (Optional)
```
Secondary     ┌────────┐
  Coil    ┌──┤ LM358  │
   │      │  │   Out  ├─── To Oscilloscope
  10kΩ    │  │        │
   │      │  └────────┘
  GND    GND
```

## Step-by-Step Assembly

1. Power Setup
   ```
   a. Connect power supply to rails
   b. Verify 5V with multimeter
   c. Bridge power rails if needed
   ```

2. 555 Timer
   ```
   a. Place 555 in middle of board
   b. Connect pins 1,8 to +5V
   c. Connect pin 4 to +5V
   d. Add timing components:
      - 10kΩ to pin 7
      - 100kΩ pot between 7,6
      - 0.1µF from pin 2 to GND
   ```

3. MOSFET Driver
   ```
   a. Place IRF530
   b. Connect Source to GND
   c. Gate resistors:
      - 10kΩ from 555 out
      - 1kΩ to GND
   d. Drain to primary coil
   ```

4. Testing Points
   ```
   A) 555 Output (Pin 3):
      - Should see 4.37 Hz
      - 5V square wave
   
   B) MOSFET Drain:
      - Switching voltage
      - Clean transitions
   
   C) Secondary Coil:
      - Induced voltage
      - φ-resonance check
   ```

## Voltage Test Points
```
1. Power Rails: 5V
2. 555 Pin 3: 0-5V square
3. MOSFET Gate: 0-5V
4. Primary Coil: <5V
5. Secondary: Induced ~4.8V
```

## Tuning Procedure
1. Adjust 100kΩ pot until 4.37 Hz
2. Monitor secondary voltage
3. Fine-tune for 0.96 resonance
4. Check φ-wave formation

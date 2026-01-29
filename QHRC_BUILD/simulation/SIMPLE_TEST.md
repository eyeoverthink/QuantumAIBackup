# Simple 16Hz to 4.37Hz Test Circuit

## Components
```
1. 16Hz Source
   - 5V square wave
   - Direct from crystal

2. Two 74164 Shift Registers
   - First divides by 2
   - Second divides by 1.83
   - Combined: ÷3.66 = 4.37Hz

3. LED Indicators
   - Top: 16Hz input
   - Bottom: 4.37Hz output
```

## How to Test
1. Load circuit in Falstad
2. Click Run
3. Watch both LEDs
4. Top LED: 16 blinks/sec
5. Bottom LED: 4-5 blinks/sec

## Expected Results
```
1. Top LED: Fast blink (16Hz)
2. Bottom LED: Slower blink (4.37Hz)
3. Count 26 blinks in 6 seconds
```

## To Load Circuit
1. Go to https://falstad.com/circuit/
2. File → Import From Text
3. Paste contents of falstad_simple.txt
4. Click Import

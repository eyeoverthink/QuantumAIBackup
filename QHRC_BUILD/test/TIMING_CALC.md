# 555 Timer Calculations for 4.37 Hz

## Frequency Formula
```
f = 1 / (ln(2) * (R1 + 2R2) * C)
Where:
- f = 4.37 Hz
- R1 = 10kΩ fixed
- R2 = 100kΩ pot
- C = 0.1µF
```

## Target Values
```
1. Period = 1/4.37 = 0.229 seconds
2. Duty cycle = 50%
3. ON time = 0.1145 seconds
4. OFF time = 0.1145 seconds
```

## Component Selection
```
1. Fixed resistor (R1):
   - Value: 10kΩ ±5%
   - Power: 1/4W
   - Type: Metal film

2. Potentiometer (R2):
   - Value: 100kΩ
   - Type: Linear
   - Turns: 10+ for fine adjustment

3. Capacitor (C):
   - Value: 0.1µF
   - Type: Ceramic
   - Voltage: 16V or higher
```

## Tuning Process
```
1. Start with pot at midpoint
2. Use phone camera to view blinks
3. Adjust until you see 26 blinks in 6 seconds
4. Fine tune with oscilloscope if available
```

## Verification Points
```
1. Frequency: 4.37 Hz ±1%
2. Duty cycle: 50% ±1%
3. Jitter: <1%
4. Temperature stability: <50ppm/°C
```

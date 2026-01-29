# QHRC Testing Guide

## Minimum Equipment Needed
1. Multimeter
2. Power source (5V)
3. LED for visual indicator

## Basic Tests (No Oscilloscope)

### 1. Power Test
```
Points to check:
1. +5V rail to GND: 5.0V ±0.1V
2. 555 pin 8 to GND: 5.0V ±0.1V
3. Current draw: <200mA
```

### 2. 555 Timer Test
```
1. Connect LED + 1kΩ to pin 3
2. Should blink at ~4.37 Hz
3. Count 26 blinks in 6 seconds
```

### 3. MOSFET Test
```
1. Measure Gate-Source: 0-5V swing
2. Check Drain-Source resistance:
   - OFF: >1MΩ
   - ON: <1Ω
```

### 4. Coil Tests
```
Primary:
1. DC resistance: ~30Ω
2. Continuity check
3. No shorts to core

Secondary:
1. DC resistance: ~42Ω
2. Continuity check
3. No shorts to core
```

## Advanced Tests (With Oscilloscope)

### 1. Frequency Verification
```
Channel 1: 555 output
- 4.37 Hz
- 5V peak
- 50% duty cycle
```

### 2. Resonance Check
```
Channel 1: Primary
Channel 2: Secondary
Math: CH2/CH1 = 0.96
```

## Troubleshooting

### No Oscillation
1. Check power
2. Verify 555 connections
3. Test timing components

### No Secondary Voltage
1. Check primary current
2. Verify coil alignment
3. Test coil continuity

### Wrong Frequency
1. Measure timing capacitor
2. Adjust potentiometer
3. Check voltage levels

## Safety Limits
```
Maximum values:
- Input voltage: 5.5V
- Primary current: 200mA
- Coil temperature: 50°C
```

# QHRC Testing Guide

## Hardware Setup
```
1. Breadboard circuit first:
   - 555 timer (4.37 Hz)
   - LED indicators
   - Test points

2. PCB spiral test:
   - Primary coil trace
   - Secondary coil trace
   - LED monitoring
```

## Test Sequence
```
1. Base Frequency (4.37 Hz)
   - Connect LED to pin 3 of 555
   - Should blink ~4-5 times/second
   - Use phone camera to verify

2. Primary Circuit
   - Monitor voltage at primary
   - Check current draw (<200mA)
   - Verify clean square wave

3. Secondary Pickup
   - LED on secondary should blink
   - Measure induced voltage
   - Calculate resonance ratio
```

## Expected Results
```
1. Primary LED: 4.37 Hz blink
2. Secondary LED: 4.19 Hz blink (0.96 ratio)
3. Current draw: ~100mA
4. Operating temp: <40°C
```

## Troubleshooting
```
1. No primary blink:
   - Check 555 connections
   - Verify 5V power
   - Test timing components

2. No secondary blink:
   - Check coil alignment
   - Verify trace continuity
   - Test pickup circuit

3. Wrong frequency:
   - Adjust timing resistor
   - Check capacitor value
   - Measure supply voltage
```

## Safety Notes
```
1. Use current-limited supply
2. Monitor temperature
3. Check for shorts
4. Don't exceed 5V
```

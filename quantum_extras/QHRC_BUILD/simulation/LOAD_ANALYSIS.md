# LED Load Analysis

## LED Chain
```
1. Green LED (16 Hz)
   - 525nm wavelength
   - Base frequency

2. Red LED (4.37 Hz)
   - 650nm wavelength
   - ÷φ² from base

3. Yellow LED (2.70 Hz)
   - 590nm wavelength
   - ÷φ³ from base

4. Blue LED (1.67 Hz)
   - 470nm wavelength
   - ÷φ⁴ from base
```

## Voltage Measurements
```
Test points:
V1: After Green LED
V2: After Red LED
V3: After Yellow LED
V4: After Blue LED

Expected drop per stage: ~0.6V
Total expected drop: ~2.4V
```

## Frequency Cascade
```
16 Hz → 4.37 Hz → 2.70 Hz → 1.67 Hz
(÷φ²)   (÷φ²)     (÷φ²)     (final)
```

## Power Analysis
```
Per LED:
- Forward voltage: ~2V
- Current: ~20mA
- Power: ~40mW

Total Load:
- Current: ~80mA
- Power: ~160mW
- Voltage drop: ~2.4V
```

## Expected Behavior
```
1. If voltage holds:
   - All LEDs light
   - φ-based blinking
   - Clean transitions

2. If voltage drops:
   - Dimming at end
   - Timing changes
   - Loss of φ ratios
```

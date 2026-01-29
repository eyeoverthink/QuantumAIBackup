# QHRC Test Protocol

## 1. Initial Setup
```
Equipment needed:
- Oscilloscope
- Multimeter
- Function generator (if not using 555 circuit)
```

## 2. Base Frequency Test
```
1. Connect oscilloscope to primary coil
2. Set trigger to 4.37 Hz
3. Verify waveform:
   - Square wave
   - 5V peak
   - 50% duty cycle
```

## 3. Resonance Testing
```
Test points:
A) Primary (4.37 Hz)
B) Secondary (measure induced)
C) Calculate ratio (target 0.96)

Expected readings:
1. Primary voltage: 5V
2. Secondary voltage: 4.8V
3. Resonance: 0.96
```

## 4. Field Coherence Test
```
Measurement points:
1. Center: Maximum field
2. φ distance: 1.618034 x radius
3. φ² distance: 2.618034 x radius

Expected readings:
- Center: 100%
- φ point: 61.8%
- φ² point: 23.6%
```

## 5. Data Recording
```
Record for each test:
1. Frequencies
2. Voltages
3. Field strengths
4. Resonance ratios
```

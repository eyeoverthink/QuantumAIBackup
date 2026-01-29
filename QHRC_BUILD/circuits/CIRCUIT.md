# QHRC Circuit Diagram

## Signal Generator Circuit
```
VCC (5V)
  │
  ├─[10kΩ]─┬─[100kΩ POT]─┐
  │        │             │
  │     [555 Timer]      │
  │        │             │
  └────────┴─[0.1µF]─────┘
           │
           └─> Output (4.37 Hz)

Components:
- 555 Timer IC
- 10kΩ resistor
- 100kΩ potentiometer
- 0.1µF capacitor
```

## Coil Driver Circuit
```
Signal In
   │
   ├─[10kΩ]─┬─[IRF530]
   │        │    │
   │     [1kΩ]   │
   │        │    │
Primary    GND   │
Coil            │
   │            │
   └────────────┘

Components:
- IRF530 MOSFET
- 10kΩ resistor
- 1kΩ resistor
```

## Measurement Points
```
A) Primary Coil
   - Frequency: 4.37 Hz
   - Voltage: 5V peak
   - Current: ~100mA

B) Secondary Coil
   - Expected resonance: 0.96
   - Voltage: Induced
   - Phase shift: Monitor
```

## Power Requirements
- Input: 5V DC
- Current: <200mA
- Power: ~1W max

# Simplified QHRC Test Circuit

## Minimal Components Needed
```
1. Power: USB power bank or 4xAA battery pack (5V)
2. IC: 1x 555 timer
3. Resistors: 2x 10kΩ, 1x 1kΩ
4. Capacitor: 1x 0.1µF
5. LED: 1x any color + 220Ω resistor
6. Wire: ~10m copper wire for test coils
```

## Ultra Simple Layout
```
         +5V
          │
          │
     ┌────┴────┐
     │         │
    10kΩ      8│
     │    555  │
     ├────7,6  │
     │         │3────LED────┐
   0.1µF       │            │
     │         │           220Ω
     └────2,1──┘            │
          │                 │
         GND               GND
```

## Test Coils (Simplified)
```
Primary: 50 turns
Secondary: 81 turns (50 × φ)
Diameter ratio: 1:1.618 (φ)

[Primary]  [Secondary]
   ┌─┐       ┌─┐
   │ │       │ │
   │ │       │ │
   └─┘       └─┘
```

## Quick Test Steps
1. Build circuit on breadboard
2. Connect 5V power
3. LED should blink at ~4.37 Hz
4. Hold coils concentrically
5. Check for induced blink in secondary LED

## Expected Results
1. LED blinks 4-5 times per second
2. Secondary coil induces voltage
3. No special equipment needed

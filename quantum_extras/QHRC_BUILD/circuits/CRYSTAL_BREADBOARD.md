# Crystal Divider Breadboard Layout

## Power Rails
```
Top Rail:    +5V ────────────────────
Bottom Rail: GND ────────────────────
```

## Component Layout
```
   [Crystal]     [CD4013 #1]    [CD4013 #2]
      │              │              │
      v              v              v
    ┌─────┐      ┌───────┐      ┌───────┐
A   │ OSC │      │FF1    │      │FF2    │
B   │     │      │       │      │       │
C   └─────┘      └───────┘      └───────┘
D     │             │              │
E     │         [RC Network]    [CD4070]
F     └─────────────┴──────────────┘

Columns: 1  2  3  4  5  6  7  8  9  10
```

## Detailed Connections
```
1. Crystal Oscillator
   - Pin 1 (VCC) → +5V
   - Pin 7 (GND) → GND
   - Pin 8 (OUT) → FF1 Clock

2. First Flip-Flop (FF1)
   - Pin 14 → +5V
   - Pin 7 → GND
   - Pin 3 (CLK) ← Crystal
   - Pin 1 (Q) → Pin 2 (D)
   - Pin 2 → FF2 Clock

3. RC Network
   - 10kΩ → Pin A5
   - 22kΩ → Pin B5
   - 47kΩ trim → Pin C5
   - 0.01µF → GND

4. XOR Gate
   - Pin 14 → +5V
   - Pin 7 → GND
   - Pin 1 ← FF2 Q
   - Pin 2 ← RC out
   - Pin 3 → Output
```

## Test Points
```
TP1: A1 - 16Hz crystal out
TP2: A4 - 8Hz FF1 out
TP3: A7 - RC network
TP4: A10 - 4.37Hz output
```

## Power Requirements
```
Supply: 5V DC
Current: <50mA
Stability: ±5%
```

## Tuning Steps
```
1. Power up
2. Check crystal output (TP1)
3. Verify 8Hz at TP2
4. Monitor TP4 while adjusting trim pot
5. Count 26 cycles in 6 seconds
```

## LED Monitor
```
Add at output:
220Ω → LED → GND
Should blink 4-5 times/second
```

## Common Issues
```
1. No oscillation
   - Check crystal connections
   - Verify +5V power

2. Wrong frequency
   - Adjust trim pot
   - Check RC values
   - Verify crystal freq

3. Unstable output
   - Clean power supply
   - Short connections
   - Add bypass caps
```

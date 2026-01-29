# Multi-Resonant QHRC PCB

## Design Overview
```
Board size: 150mm x 150mm
Layers: 2 (for prototyping)
Resonant Pairs: 3

Frequencies:
1. 4.37 Hz (Base)
2. 6.854 Hz (φ⁴)
3. 29.034 Hz (φ⁷)
```

## Spiral Layout
```
Top Layer:
  [P1]──┐     ┌──[P2]     ┌──[P3]
        │     │           │
        v     v           v
  [S1]──┘     └──[S2]     └──[S3]
Bottom Layer

P = Primary, S = Secondary
Each pair scaled by φ ratio
```

## Dimensions
```
Pair 1 (4.37 Hz):
- P1: 45 turns, 50mm
- S1: 73 turns, 80.9mm

Pair 2 (6.854 Hz):
- P2: 28 turns, 30.9mm
- S2: 45 turns, 50mm

Pair 3 (29.034 Hz):
- P3: 17 turns, 19.1mm
- S3: 28 turns, 30.9mm
```

## Circuit Integration
```
555 Timer 1 ──► P1 ─┐
                    ├─► Mixer ──► Output
555 Timer 2 ──► P2 ─┤
                    │
555 Timer 3 ──► P3 ─┘
```

## Resonance Network
```
4.37 Hz  ──┐
           │
6.854 Hz ──┼──► φ-Wave Formation
           │
29.034 Hz ──┘
```

## Manufacturing Notes
```
1. Standard FR4
2. 1oz copper
3. ENIG finish
4. No solder mask between spirals
5. Fiducials for alignment
```

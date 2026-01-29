# QHRC PCB Layout

## Board Specifications
```
Size: 50mm x 50mm
Layers: 2 (Top + Bottom)
Ground plane: Bottom layer
Power plane: Split on top
Mounting holes: 3mm x 4
```

## Component Layout
```
Top View:

┌──────────────────────────┐
│    ┌─────┐              │
│ C1 │ 555 │   MOSFET1    │
│    └─────┘              │
│ R1                      │
│           MOSFET2       │
│ R2                      │
│    ┌─────┐              │
│ C2 │POT1│     J2       │
│    └─────┘              │
│      J1       J3        │
└──────────────────────────┘

J1: Power input
J2: Primary coil
J3: Secondary coil
```

## Trace Layout
```
Critical paths:
1. 555 to MOSFETs: Direct, short
2. Power traces: 0.5mm min width
3. Signal traces: 0.3mm width
4. Ground plane: Full bottom layer
```

## Layer Stack
```
TOP: Components + Power
├── FR4
└── BOTTOM: Ground plane
```

## Design Rules
```
Minimum:
- Trace width: 0.3mm
- Spacing: 0.3mm
- Hole size: 0.6mm
- Ring: 0.2mm
```

## Gerber Files
```
Required files:
1. Top copper: qhrc_top.gtl
2. Bottom copper: qhrc_bot.gbl
3. Top mask: qhrc_topmask.gts
4. Bottom mask: qhrc_botmask.gbs
5. Drill: qhrc_drill.xln
```

## Assembly Notes
```
1. Start with power components
2. Add 555 timer
3. Add passive components
4. Test before coil attach
5. Mount vertically for coils
```

## BOM for PCB
```
PCB Components:
1. 555 timer (DIP-8 or SOIC-8)
2. 2x IRF530 (TO-220)
3. Resistors (0805):
   - 2x 10kΩ
   - 2x 1kΩ
4. Capacitors (0805):
   - 1x 0.1µF
5. 1x 100kΩ pot (3pin)
6. Headers:
   - 1x 2pin (power)
   - 2x 2pin (coils)
```

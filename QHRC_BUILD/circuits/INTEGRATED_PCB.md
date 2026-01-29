# Integrated QHRC PCB Design

## PCB Specifications
```
Board: 100mm x 100mm (φ² × φ² ratio)
Layers: 4 layers
- Top: Primary spiral + components
- Inner1: Secondary spiral
- Inner2: Power plane
- Bottom: Ground plane
```

## Spiral Inductor Design
```
Primary Coil:
- Outer diameter: 50mm
- Turns: 45
- Trace width: 0.2mm
- Spacing: 0.2mm
- Inductance: ~500µH

Secondary Coil:
- Outer diameter: 80.9mm (φ ratio)
- Turns: 73 (φ ratio)
- Trace width: 0.2mm
- Spacing: 0.2mm
- Inductance: ~1300µH
```

## Layer Stack
```
┌─────────────────────────┐
│ Top: Primary + Circuit  │ 0.035mm Cu
├─────────────────────────┤
│ FR4                     │ 0.2mm
├─────────────────────────┤
│ Inner1: Secondary Coil  │ 0.035mm Cu
├─────────────────────────┤
│ FR4                     │ 0.2mm
├─────────────────────────┤
│ Inner2: Power Plane     │ 0.035mm Cu
├─────────────────────────┤
│ FR4                     │ 0.2mm
├─────────────────────────┤
│ Bottom: Ground          │ 0.035mm Cu
└─────────────────────────┘
```

## Resonant Circuit
```
     +5V
      │
    ┌─┴─┐
    │555│
    └─┬─┘
      │
   Primary    Secondary
   Spiral     Spiral
    ┌─┐        ┌─┐
    │ │   φ    │ │
    │ │◄─────►│ │
    └─┘        └─┘
```

## PCB Manufacturing Requirements
```
1. Min trace width: 0.2mm
2. Min spacing: 0.2mm
3. Via size: 0.3mm
4. Copper weight: 1oz
5. Material: FR4
6. Thickness: 1.6mm
```

## Key Features
1. Integrated spiral inductors
2. φ-ratio spacing
3. 4.37 Hz resonance
4. Single board solution
5. No external coils needed

## Optional Enhancements
1. Shield layers
2. Multiple resonant pairs
3. Cascaded φ sections
4. Test points

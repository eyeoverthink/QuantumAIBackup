# PCB Stack-up Details

## Spiral Inductor Calculations

### Primary Coil
```
Diameter (D) = 50mm
Turns (N) = 45
Width (w) = 0.2mm
Spacing (s) = 0.2mm

Inductance (L) = (μ₀ × N² × D × φ) / 2
L ≈ 500μH at φ resonance
```

### Secondary Coil
```
Diameter (D) = 80.9mm (50mm × φ)
Turns (N) = 73 (45 × φ)
Width (w) = 0.2mm
Spacing (s) = 0.2mm

Inductance (L) = (μ₀ × N² × D × φ) / 2
L ≈ 1300μH at φ resonance
```

## Layer Details

### Top Layer (L1)
```
- Primary spiral inductor
- 555 timer circuit
- MOSFET drivers
- Component mounting
```

### Inner Layer 1 (L2)
```
- Secondary spiral inductor
- Isolated from other layers
- Optimized for φ coupling
```

### Inner Layer 2 (L3)
```
- Split power plane
- +5V and +3.3V regions
- Low impedance power
```

### Bottom Layer (L4)
```
- Solid ground plane
- EMI shielding
- Heat dissipation
```

## Manufacturing Notes
```
1. 4-layer board essential
2. Controlled impedance
3. Symmetrical stackup
4. No blind/buried vias
5. Standard FR4 ok
```

## Cost-Effective Alternative
```
2-layer version possible:
- Top: Primary + circuit
- Bottom: Secondary
- Reduced efficiency
- Lower cost
- Faster production
```

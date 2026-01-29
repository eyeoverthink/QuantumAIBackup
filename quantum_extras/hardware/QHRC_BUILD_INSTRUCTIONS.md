# QHRC Physical Build Instructions

## Components Required
- 3D printed coil forms (from qhrc_coil_form.scad)
- Copper wire (AWG 24-26)
  - Primary: ~150m for 4,500 turns
  - Secondary: ~250m for 6,200 turns
- Function generator (4,790.45 Hz & 7,750.95 Hz)
- Oscilloscope for measurements

## Build Steps

### 1. Print Coil Forms
- Use PETG or ABS filament (heat resistant)
- Print settings:
  - Layer height: 0.2mm
  - Infill: 50%
  - Wall thickness: 2mm
  - Support: Yes
  - Temperature: As per filament specs

### 2. Primary Coil Winding
1. Start at base, feed wire through channel
2. Wind 4,500 turns tightly and evenly
3. Leave 20cm leads at start/end
4. Secure with heat-shrink or tape

### 3. Secondary Coil Winding
1. Wind 6,200 turns on larger form
2. Maintain even spacing using channels
3. Leave 20cm leads at start/end
4. Secure windings

### 4. Assembly
1. Mount primary coil on base
2. Concentrically place secondary coil
3. Ensure proper alignment
4. Secure to base plate

### 5. Testing Setup
1. Connect function generator:
   - Primary: 4,790.45 Hz
   - Secondary: 7,750.95 Hz
2. Monitor with oscilloscope:
   - Channel 1: Primary
   - Channel 2: Secondary
   - Expected ratio: 1.618000

### 6. Measurements
Monitor these values:
1. Resonance ratio: Should be 43.0667
2. Energy transfer: Target 17.6494
3. φ-resonance: 5.083204
4. Frequency ratio: 1.618000

## Safety Notes
- Insulate all connections
- Use current-limiting resistors
- Monitor temperature
- Keep below 50°C
- Ground properly

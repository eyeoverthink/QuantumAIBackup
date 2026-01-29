# Falstad Circuit Simulator Instructions

## How to Load the Circuit
1. Go to https://falstad.com/circuit/
2. Click "Edit" in the top menu
3. Click "Import From Text"
4. Copy and paste the contents of falstad_sim.txt
5. Click "Import"

## Circuit Components
```
1. Crystal Oscillator
   - Simulated with 16Hz voltage source
   - Stable reference frequency

2. Frequency Divider
   - D flip-flops (7474)
   - Divides by ~3.66

3. RC Network
   - R1: 10kΩ
   - R2: 22kΩ
   - R3: 47kΩ (adjustable)
   - C: 0.01µF

4. LED Indicators
   - Primary: Shows 16Hz
   - Secondary: Shows 4.37Hz
   - Current limiting: 220Ω each
```

## What to Look For
```
1. Primary LED (top)
   - Blinks at 16Hz
   - Fast flashing

2. Secondary LED (bottom)
   - Blinks at 4.37Hz
   - ~4-5 blinks per second

3. Scope View
   - Click "Add Scope" button
   - Shows both frequencies
   - Verify timing relationship
```

## Interactive Elements
```
1. Adjust R3 (47kΩ)
   - Right-click resistor
   - Select "Edit"
   - Adjust value for fine tuning

2. Voltage Source
   - Right-click for frequency
   - Keep at 16Hz
   - 5V amplitude
```

## Measurements
```
1. Count LED blinks
   - Primary: 16 per second
   - Secondary: 26 per 6 seconds

2. Scope View
   - X-axis: time scale
   - Y-axis: voltage
   - Verify clean transitions
```

## Troubleshooting
```
1. No LED blinks
   - Check voltage source
   - Verify flip-flop connections
   - Check LED polarity

2. Wrong frequency
   - Verify 16Hz source
   - Adjust RC values
   - Check divider chain
```

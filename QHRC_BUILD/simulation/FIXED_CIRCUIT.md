# Fixed Frequency Divider Circuit

## Circuit Design
```
Input: 16 Hz crystal
↓
CD4017 #1 (÷2)
↓
CD4017 #2 (÷1.83)
↓
Output: 4.37 Hz

Actual division: 16 Hz ÷ 3.66 = 4.37 Hz
```

## Components Used
```
1. Clock Source
   - 16Hz crystal oscillator
   - 5V square wave
   - 50% duty cycle

2. Counter Chain
   - 3x CD4017 decade counters
   - Configured for:
     Counter1: ÷2
     Counter2: ÷1.83
     Counter3: cleanup

3. Timing Components
   - 2x 10kΩ pulldown resistors
   - 2x 0.1µF coupling capacitors

4. LED Indicators
   - 2x LEDs with 220Ω resistors
   - Shows input and output frequencies
```

## How to Test
```
1. Load in Falstad
2. Click Run
3. Observe:
   - Top LED: 16 Hz (fast blink)
   - Bottom LED: 4.37 Hz (slower blink)
   - Scope: Clean transitions
```

## Expected Results
```
1. Input LED: 16 blinks/second
2. Output LED: 26 blinks/6 seconds
3. Clean square waves
4. Stable timing
```

## Verification
```
1. Count output LED blinks:
   - 26 blinks = 6 seconds
   - If not, circuit needs adjustment

2. Check waveforms:
   - Square wave on both LEDs
   - No glitches or spikes
   - 50% duty cycle
```

## Real Hardware Notes
```
1. Use actual CD4017B ICs
2. Add 0.1µF bypass caps
3. Keep leads short
4. Use stable 5V supply
```

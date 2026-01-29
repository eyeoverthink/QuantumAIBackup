# 555 Timer Frequency Divider

## How It Works
```
1. Input Stage
   - 16Hz crystal input
   - Clean square wave

2. 555 Timer
   - Configured as divider
   - RC network for timing
   - 47kΩ + 1µF for division

3. Output Stage
   - Two LEDs
   - Input frequency (16Hz)
   - Output frequency (4.37Hz)
```

## Testing
```
1. Load circuit
2. Watch both LEDs
3. Top: 16 blinks/sec
4. Bottom: ~4.37 blinks/sec
```

## Verification
```
1. Count bottom LED
   - 26 blinks = 6 seconds
   - Clean, steady blinks
```

## Components
```
1. 555 Timer IC
2. 47kΩ resistor
3. 1µF capacitor
4. 2x 220Ω LED resistors
5. 2x LEDs
```

# QHRC LED Test Circuit

## Components Needed
```
1. 1x NE555 timer IC
2. 2x LEDs (any color)
3. 2x 220Ω resistors (LED current limit)
4. 1x 10kΩ resistor
5. 1x 100kΩ potentiometer
6. 1x 0.1µF capacitor
7. Breadboard
8. 5V power source (USB or 4xAA batteries)
9. Jumper wires
```

## Circuit Layout
```
                     +5V
                      │
                      ├─────┬────────┐
                      │     │        │
                    10kΩ   LED1     │
                      │     │        │
                      │    220Ω      │
            ┌─────────┴─────┐        │
            │     555       │        │
            │ 1         8   │        │
            │ 2         7   ├────────┤
            │ 3         6   │       POT
            │ 4         5   │      100kΩ
            └─────────┬─────┘        │
                     │              │
                    LED2            │
                     │              │
                    220Ω            │
                     │              │
                    GND─────────────┘
```

## Assembly Steps
```
1. Place 555 timer on breadboard
   - Straddle center gap
   - Pin 1 on left side

2. Power connections
   - Pin 8 (VCC) to +5V
   - Pin 1 (GND) to ground

3. Timing components
   - 10kΩ from pin 7 to +5V
   - 100kΩ pot between pins 6,7
   - 0.1µF from pin 2 to ground

4. LED connections
   - LED1: +5V → 220Ω → LED → Pin 3
   - LED2: Pin 3 → 220Ω → LED → GND
```

## Testing Procedure
```
1. Power up circuit
   - Connect 5V
   - Verify no excessive heat

2. Adjust frequency
   - Turn pot until LED blinks 4-5 times/second
   - Use phone camera to verify
   - Should be 4.37 Hz exactly

3. Count blinks
   - Count 26 blinks in 6 seconds
   - If not, adjust pot
```

## Expected Results
```
LED1 and LED2 should:
1. Blink alternately
2. Flash ~4-5 times per second
3. Have equal ON/OFF times
4. Show stable frequency
```

## Verification
```
1. Use phone camera:
   - Record video
   - Count frames between blinks
   - Should be ~229ms per state

2. Count method:
   - Count 26 blinks
   - Should take 6 seconds
   - Use stopwatch app
```

## Troubleshooting
```
1. LEDs don't light:
   - Check power connections
   - Verify LED polarity
   - Test with new LEDs

2. Wrong frequency:
   - Adjust potentiometer
   - Verify capacitor value
   - Check voltage is 5V

3. Unstable blinking:
   - Replace 555 timer
   - Check connections
   - Try new power source
```

## Next Steps
Once 4.37 Hz is verified:
1. Add primary coil
2. Test secondary pickup
3. Measure resonance

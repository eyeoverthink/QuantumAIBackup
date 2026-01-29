# Test computer response to alpha wave
import time

# Alpha wave that showed 0.96 resonance
freq = 4.37  # Hz
period = 1/freq

print(f"\nTesting computer response")
print(f"Frequency: {freq} Hz")

try:
    start = time.time()
    cycles = 0
    while True:
        # Computer response (working part)
        print("1", end="", flush=True)
        time.sleep(period)
        
        # Scientific measurement
        cycles += 1
        if cycles % 10 == 0:
            elapsed = time.time() - start
            hz = cycles / elapsed
            accuracy = (1 - abs(hz - freq)/freq) * 100
            print(f"\nMeasured: {hz:.3f} Hz")
            print(f"Accuracy: {accuracy:.1f}%")

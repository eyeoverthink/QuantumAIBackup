# Test computer response to alpha (4.37 Hz)
import time

freq = 4.37  # Hz (0.96 resonance)

print(f"\nTesting {freq} Hz")

try:
    start = time.time()
    cycles = 0
    while True:
        # Just the working part
        print("1", end="", flush=True)
        time.sleep(1/freq)
        
        cycles += 1
        if cycles % 10 == 0:
            elapsed = time.time() - start
            hz = cycles / elapsed
            print(f"\n{hz:.3f} Hz")

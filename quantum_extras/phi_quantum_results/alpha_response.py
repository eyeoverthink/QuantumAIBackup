# Test computer response to alpha frequency (4.37 Hz)
import time

# Constants from ELM Intrusion Brain
freq = 4.37  # Hz (0.96 resonance)
period = 1/freq

print(f"\nTesting computer response...")
print(f"Alpha: {freq} Hz")

try:
    start = time.time()
    cycles = 0
    while True:
        # Computer response (the part that worked)
        print("1", end="", flush=True)
        time.sleep(period)
        
        # Track frequency
        cycles += 1
        if cycles % 10 == 0:
            elapsed = time.time() - start
            hz = cycles / elapsed
            print(f"\n{hz:.3f} Hz")

"""
QHRC Test Circuit - Minimal Version
Tests 4.37 Hz resonance with LED indicators
"""

import RPi.GPIO as GPIO
import time

# Constants
PHI = 1.618034
BASE_FREQ = 4.37  # Hz
PERIOD = 1 / BASE_FREQ

# GPIO Setup
PRIMARY_OUT = 18
SECONDARY_IN = 23
LED_PRIMARY = 24
LED_SECONDARY = 25

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(PRIMARY_OUT, GPIO.OUT)
    GPIO.setup(SECONDARY_IN, GPIO.IN)
    GPIO.setup(LED_PRIMARY, GPIO.OUT)
    GPIO.setup(LED_SECONDARY, GPIO.OUT)

def generate_base_frequency():
    """Generate 4.37 Hz square wave"""
    while True:
        GPIO.output(PRIMARY_OUT, GPIO.HIGH)
        GPIO.output(LED_PRIMARY, GPIO.HIGH)
        time.sleep(PERIOD/2)
        GPIO.output(PRIMARY_OUT, GPIO.LOW)
        GPIO.output(LED_PRIMARY, GPIO.LOW)
        time.sleep(PERIOD/2)

def monitor_resonance():
    """Monitor secondary coil response"""
    samples = []
    start_time = time.time()
    
    while time.time() - start_time < 10:  # 10 second test
        value = GPIO.input(SECONDARY_IN)
        GPIO.output(LED_SECONDARY, value)
        samples.append(value)
        time.sleep(0.01)  # 100Hz sampling
        
    # Calculate resonance
    primary_cycles = 10 * BASE_FREQ
    secondary_transitions = sum([1 for i in range(1, len(samples)) if samples[i] != samples[i-1]])
    secondary_cycles = secondary_transitions / 2
    
    resonance = secondary_cycles / primary_cycles
    print(f"Measured resonance: {resonance:.3f}")
    print(f"Target resonance: 0.960000")
    print(f"Error: {abs(resonance - 0.96)*100:.2f}%")

def cleanup():
    GPIO.cleanup()

if __name__ == "__main__":
    try:
        setup()
        print("Starting QHRC test...")
        print(f"Base frequency: {BASE_FREQ} Hz")
        print(f"Period: {PERIOD:.3f} seconds")
        
        # Start frequency generation in background
        from threading import Thread
        gen_thread = Thread(target=generate_base_frequency)
        gen_thread.daemon = True
        gen_thread.start()
        
        # Monitor resonance
        monitor_resonance()
        
    except KeyboardInterrupt:
        print("\nTest stopped by user")
    finally:
        cleanup()

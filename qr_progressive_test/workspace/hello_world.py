#!/usr/bin/env python3
# Hello World - Created by QR Code 1 and improved by QR Code 2
import math
import time

def calculate_phi():
    # Calculate the golden ratio (phi)
    return (1 + math.sqrt(5)) / 2

def main():
    print("Hello, Enhanced World!")
    print(f"I was created by QR Code 1 and improved by QR Code 2")
    phi = calculate_phi()
    print(f"The golden ratio (phi) is: {phi}")
    print(f"Phi resonance: {time.time() * phi % 1.0:.6f}")

if __name__ == "__main__":
    main()

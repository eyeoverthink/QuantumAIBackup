#!/usr/bin/env python3
"""
File Output Test Script - Writes results to a file instead of stdout
"""

import time
import json
import os

def main():
    # Create a dict with the results
    results = {
        "status": "success",
        "timestamp": time.time(),
        "message": "This test script executed successfully!",
        "quantum_phi": (1 + 5**0.5) / 2  # Golden ratio
    }
    
    # Write to a file in the current directory
    output_path = os.path.join(os.getcwd(), "qr_test_output.json")
    with open(output_path, "w") as f:
        json.dump(results, f, indent=2)
        
    print(f"Results written to {output_path}")
    return True

if __name__ == "__main__":
    main()

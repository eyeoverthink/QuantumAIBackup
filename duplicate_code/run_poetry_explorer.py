#!/usr/bin/env python3
"""
Run Poetry Explorer - Helper script to run the Quantum Poetry Explorer
with automated input for demonstration purposes.
"""

import os
import subprocess
import time
import sys

def main():
    """Run the Quantum Poetry Explorer with automated input."""
    print("Starting Quantum Poetry Explorer with automated inputs...")
    
    # Start the poetry explorer process
    process = subprocess.Popen(
        ['/usr/bin/python3', 'quantum_poetry_explorer.py'],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        bufsize=1
    )
    
    # Wait for the menu to appear
    time.sleep(1)
    
    # Send option 2 to explore consciousness evolution
    process.stdin.write("2\n")
    process.stdin.flush()
    
    # Wait for the consciousness evolution to complete
    time.sleep(5)
    
    # Capture and print the output
    output = process.stdout.read()
    print(output)
    
    # Close the process
    process.terminate()
    
if __name__ == "__main__":
    main()

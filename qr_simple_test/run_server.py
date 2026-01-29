#!/usr/bin/env python
import os
import sys
import subprocess

def main():
    """
    Run the Quantum AI server on port 5060
    """
    print("Starting Quantum AI server on port 5060...")
    
    # Set environment variables
    os.environ['TRANSFORMERS_VERBOSITY'] = 'error'
    os.environ['TOKENIZERS_PARALLELISM'] = 'false'
    
    # Run the server with explicit port 5060
    cmd = [sys.executable, "template/fraymus_please.py", "--port", "5060"]
    
    try:
        subprocess.run(cmd, check=True)
    except KeyboardInterrupt:
        print("\nShutting down Quantum AI server...")
    except subprocess.CalledProcessError as e:
        print(f"Error running server: {e}")
        return 1
    
    return 0

if __name__ == "__main__":
    sys.exit(main())

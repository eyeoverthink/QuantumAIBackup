"""
Setup JavaScript Integration
Copies JavaScript file to static directory and sets up the environment for testing
"""

import os
import sys
import shutil
from pathlib import Path

def setup_environment():
    """Set up environment for JavaScript integration testing"""
    # Get current directory
    current_dir = Path.cwd()
    print(f"Current directory: {current_dir}")
    
    # Create static directory if it doesn't exist
    static_dir = current_dir / "static"
    if not static_dir.exists():
        static_dir.mkdir(parents=True)
        print(f"Created static directory: {static_dir}")
    
    # Copy JavaScript file to static directory
    js_file = current_dir / "quantum_claude_two.js"
    if js_file.exists():
        shutil.copy(js_file, static_dir / "quantum_claude_two.js")
        print(f"Copied {js_file} to {static_dir}")
    else:
        print(f"JavaScript file not found: {js_file}")
    
    # Check if index.html exists in static directory
    index_file = static_dir / "index.html"
    if index_file.exists():
        print(f"Index file exists: {index_file}")
    else:
        print(f"Index file not found: {index_file}")
    
    print("\nEnvironment setup complete!")
    print("To run the API bridge server:")
    print("  python -m quantum_core.quantum_api_bridge")
    print("\nTo run the integration tests:")
    print("  python -m tests.test_quantum_js_integration")

if __name__ == "__main__":
    setup_environment()

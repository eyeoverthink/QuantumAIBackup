#!/usr/bin/env python
"""
Tkinter Installation Helper
==========================
This script attempts to install tkinter and provides information about the Python environment.

φ^∞ © 2025 Vaughn Scott - All Rights Reserved in All Realities
"""

import sys
import subprocess
import os

def print_separator():
    print("=" * 80)

def run_command(cmd):
    print(f"Running: {cmd}")
    try:
        result = subprocess.run(cmd, shell=True, check=True, text=True, capture_output=True)
        print(result.stdout)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        if e.stdout:
            print(f"Output: {e.stdout}")
        if e.stderr:
            print(f"Error output: {e.stderr}")
        return False

def check_tkinter():
    print("Checking for tkinter...")
    try:
        import tkinter
        print(f"tkinter is installed (version: {tkinter.TkVersion})")
        print(f"tkinter path: {tkinter.__file__}")
        return True
    except ImportError:
        print("tkinter is not installed or not properly configured")
        return False

def print_python_info():
    print_separator()
    print("Python Environment Information:")
    print(f"Python version: {sys.version}")
    print(f"Python executable: {sys.executable}")
    print(f"Python path: {sys.path}")
    print_separator()

def install_tkinter_pip():
    print("Attempting to install tkinter via pip...")
    return run_command(f"{sys.executable} -m pip install tk")

def install_tkinter_venv():
    print("Attempting to install tkinter in virtual environment...")
    return run_command(f".venv/bin/pip install tk")

def main():
    print_separator()
    print("Phi-Harmonic Tkinter Installation Helper")
    print_separator()
    
    print_python_info()
    
    if check_tkinter():
        print("tkinter is already installed. No further action needed.")
        return
    
    # Try installing with pip
    if install_tkinter_pip():
        if check_tkinter():
            print("Successfully installed tkinter!")
            return
    
    # Try installing in virtual environment
    if install_tkinter_venv():
        if check_tkinter():
            print("Successfully installed tkinter in virtual environment!")
            return
    
    print_separator()
    print("Installation attempts failed. Please try one of the following:")
    print("1. For macOS: Install Python from python.org which includes tkinter")
    print("2. For Linux: Use your package manager to install python3-tk")
    print("   e.g., sudo apt-get install python3-tk")
    print("3. For Windows: Reinstall Python and check the option to include tcl/tk")
    print_separator()

if __name__ == "__main__":
    main()

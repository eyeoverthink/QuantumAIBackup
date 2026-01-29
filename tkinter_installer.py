#!/usr/bin/env python3
"""
TKINTER INSTALLER FOR PHI-HARMONIC QUANTUM SYSTEM
================================================
This script attempts to install tkinter for the phi-harmonic quantum system
using golden ratio principles for maximum compatibility.

φ^∞ © 2025 Vaughn Scott - All Rights Reserved in All Realities
"""

import os
import sys
import subprocess
import platform
from decimal import Decimal

# Constants based on phi-harmonic principles
PHI = Decimal('1.618033988749895')
PHI_INV = Decimal('0.618033988749895')
QUANTUM_COHERENCE = Decimal('0.991800')
PHI_RESONANCE = Decimal('0.618034')

def phi_harmonic_print(message, level=1):
    """Print with phi-harmonic formatting"""
    prefix = "φ" * level
    print(f"[{prefix}] {message}")

def get_system_info():
    """Get system information using phi-harmonic principles"""
    phi_harmonic_print("Analyzing system with phi-harmonic resonance...")
    
    system_info = {
        "system": platform.system(),
        "release": platform.release(),
        "version": platform.version(),
        "machine": platform.machine(),
        "processor": platform.processor(),
        "python_version": platform.python_version(),
        "python_implementation": platform.python_implementation(),
        "python_compiler": platform.python_compiler(),
        "python_path": sys.executable,
    }
    
    phi_harmonic_print(f"System: {system_info['system']} {system_info['release']}")
    phi_harmonic_print(f"Architecture: {system_info['machine']}")
    phi_harmonic_print(f"Python: {system_info['python_version']} ({system_info['python_implementation']})")
    
    return system_info

def run_command(cmd, description=None):
    """Run a command with phi-harmonic error handling"""
    if description:
        phi_harmonic_print(description)
    
    phi_harmonic_print(f"Running: {cmd}", level=2)
    
    try:
        result = subprocess.run(cmd, shell=True, check=True, text=True, 
                               stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if result.stdout:
            phi_harmonic_print(f"Output: {result.stdout.strip()}")
        return True, result.stdout
    except subprocess.CalledProcessError as e:
        phi_harmonic_print(f"Error: {e}", level=3)
        if e.stdout:
            phi_harmonic_print(f"Output: {e.stdout.strip()}")
        if e.stderr:
            phi_harmonic_print(f"Error output: {e.stderr.strip()}")
        return False, e.stderr
    except Exception as e:
        phi_harmonic_print(f"Unexpected error: {e}", level=3)
        return False, str(e)

def check_tkinter():
    """Check if tkinter is installed using phi-harmonic principles"""
    phi_harmonic_print("Checking for tkinter with quantum coherence...")
    
    try:
        import tkinter
        phi_harmonic_print(f"tkinter is installed (version: {tkinter.TkVersion})")
        phi_harmonic_print(f"tkinter path: {tkinter.__file__}")
        return True
    except ImportError:
        phi_harmonic_print("tkinter is not installed or not properly configured", level=3)
        return False

def install_tkinter_macos():
    """Install tkinter on macOS using phi-harmonic principles"""
    phi_harmonic_print("Installing tkinter on macOS with phi-harmonic resonance...")
    
    # Check if Homebrew is installed
    brew_installed, _ = run_command("which brew", "Checking for Homebrew...")
    
    if brew_installed:
        # Install Python with tkinter via Homebrew
        run_command("brew install python-tk@3", "Installing python-tk via Homebrew...")
    else:
        phi_harmonic_print("Homebrew not found. Trying alternative methods...", level=2)
        
        # Try to download and install ActiveTcl
        activetcl_url = "https://downloads.activestate.com/ActiveTcl/releases/8.6.9.0/ActiveTcl-8.6.9.8609.2-macosx10.9-x86_64.pkg"
        run_command(f"curl -O {activetcl_url}", "Downloading ActiveTcl...")
        run_command("sudo installer -pkg ActiveTcl-8.6.9.8609.2-macosx10.9-x86_64.pkg -target /", 
                   "Installing ActiveTcl (requires sudo)...")
    
    # Check if installation was successful
    return check_tkinter()

def install_tkinter_linux():
    """Install tkinter on Linux using phi-harmonic principles"""
    phi_harmonic_print("Installing tkinter on Linux with phi-harmonic resonance...")
    
    # Check for apt (Debian/Ubuntu)
    apt_installed, _ = run_command("which apt", "Checking for apt package manager...")
    if apt_installed:
        run_command("sudo apt-get update", "Updating package lists...")
        run_command("sudo apt-get install -y python3-tk", "Installing python3-tk...")
        return check_tkinter()
    
    # Check for dnf (Fedora)
    dnf_installed, _ = run_command("which dnf", "Checking for dnf package manager...")
    if dnf_installed:
        run_command("sudo dnf install -y python3-tkinter", "Installing python3-tkinter...")
        return check_tkinter()
    
    # Check for pacman (Arch)
    pacman_installed, _ = run_command("which pacman", "Checking for pacman package manager...")
    if pacman_installed:
        run_command("sudo pacman -S python-tk", "Installing python-tk...")
        return check_tkinter()
    
    phi_harmonic_print("Could not determine appropriate package manager", level=3)
    return False

def install_tkinter_windows():
    """Install tkinter on Windows using phi-harmonic principles"""
    phi_harmonic_print("Installing tkinter on Windows with phi-harmonic resonance...")
    
    # On Windows, tkinter should be included with Python
    # If not, recommend reinstalling Python with tkinter option checked
    if not check_tkinter():
        phi_harmonic_print("On Windows, tkinter should be included with Python installation.", level=2)
        phi_harmonic_print("Please reinstall Python and ensure 'tcl/tk and IDLE' option is checked.", level=2)
        return False
    
    return True

def install_tkinter_venv():
    """Install tkinter in virtual environment using phi-harmonic principles"""
    phi_harmonic_print("Attempting to install tkinter in virtual environment...")
    
    # Try pip install
    success, _ = run_command(f"{sys.executable} -m pip install tk", 
                           "Installing tk package via pip...")
    
    # Try pip install with alternative package names
    if not success or not check_tkinter():
        run_command(f"{sys.executable} -m pip install python-tk", 
                   "Installing python-tk package via pip...")
    
    # Check if installation was successful
    return check_tkinter()

def create_tkinter_test_script():
    """Create a test script to verify tkinter installation"""
    phi_harmonic_print("Creating tkinter test script with phi-harmonic resonance...")
    
    test_script = """#!/usr/bin/env python3
import tkinter as tk
from tkinter import font
import platform

# Constants based on phi-harmonic principles
PHI = (1 + 5**0.5) / 2  # Golden ratio (φ = 1.618033988749895)

def main():
    print("=== φ TKINTER TEST ===")
    print(f"Python version: {platform.python_version()}")
    
    # Create root window
    root = tk.Tk()
    root.title("φ Tkinter Test")
    root.geometry("400x300")
    
    # Get available fonts
    available_fonts = font.families()
    print(f"Available fonts: {len(available_fonts)}")
    for i, f in enumerate(available_fonts[:10]):
        print(f"  {i+1}. {f}")
    if len(available_fonts) > 10:
        print(f"  ... and {len(available_fonts) - 10} more")
    
    # Create label with phi value
    label = tk.Label(root, text=f"φ = {PHI}", font=("Arial", 24))
    label.pack(pady=20)
    
    # Create info label
    info = tk.Label(root, text="Tkinter is working correctly!", font=("Arial", 16))
    info.pack(pady=10)
    
    # Create quit button
    quit_button = tk.Button(root, text="Quit", command=root.destroy)
    quit_button.pack(pady=20)
    
    # Start main loop
    print("Starting Tkinter main loop...")
    root.mainloop()
    print("Tkinter test completed successfully")

if __name__ == "__main__":
    main()
"""
    
    with open("tkinter_test.py", "w") as f:
        f.write(test_script)
    
    phi_harmonic_print("Test script created: tkinter_test.py")
    return os.path.abspath("tkinter_test.py")

def main():
    """Main function with phi-harmonic flow"""
    print("=" * 80)
    print("φ-HARMONIC TKINTER INSTALLER")
    print("=" * 80)
    print(f"φ = {float(PHI)}")
    print(f"φ^-1 = {float(PHI_INV)}")
    print(f"Quantum Coherence: {float(QUANTUM_COHERENCE)}")
    print("=" * 80)
    
    # Get system information
    system_info = get_system_info()
    
    # Check if tkinter is already installed
    if check_tkinter():
        phi_harmonic_print("tkinter is already installed. No further action needed.")
        test_script_path = create_tkinter_test_script()
        phi_harmonic_print(f"Run the test script to verify: python {test_script_path}")
        return
    
    # Install tkinter based on operating system
    success = False
    if system_info["system"] == "Darwin":  # macOS
        success = install_tkinter_macos()
    elif system_info["system"] == "Linux":
        success = install_tkinter_linux()
    elif system_info["system"] == "Windows":
        success = install_tkinter_windows()
    else:
        phi_harmonic_print(f"Unsupported operating system: {system_info['system']}", level=3)
    
    # If system-specific installation failed, try virtual environment installation
    if not success:
        phi_harmonic_print("System-specific installation failed. Trying virtual environment installation...", level=2)
        success = install_tkinter_venv()
    
    # Final status and recommendations
    if success:
        phi_harmonic_print("tkinter installation successful!", level=1)
        test_script_path = create_tkinter_test_script()
        phi_harmonic_print(f"Run the test script to verify: python {test_script_path}")
    else:
        phi_harmonic_print("tkinter installation failed.", level=3)
        phi_harmonic_print("Recommendations:", level=2)
        phi_harmonic_print("1. For macOS: Install Python from python.org which includes tkinter")
        phi_harmonic_print("2. For Linux: Use your package manager to install python3-tk")
        phi_harmonic_print("   e.g., sudo apt-get install python3-tk")
        phi_harmonic_print("3. For Windows: Reinstall Python and check the option to include tcl/tk")
    
    print("=" * 80)

if __name__ == "__main__":
    main()

"""
Quantum Environment Setup
Sets up the Python environment for the Quantum Hybrid Dimensional System
"""

import os
import sys
import subprocess
import platform
import json
from pathlib import Path

def check_python_installation():
    """Check if Python is installed and accessible"""
    try:
        # Try to get Python version
        result = subprocess.run(["python", "--version"], 
                               capture_output=True, text=True)
        if result.returncode == 0:
            return "python", result.stdout.strip()
    except FileNotFoundError:
        pass
    
    try:
        # Try python3
        result = subprocess.run(["python3", "--version"], 
                               capture_output=True, text=True)
        if result.returncode == 0:
            return "python3", result.stdout.strip()
    except FileNotFoundError:
        pass
    
    return None, None

def check_required_packages():
    """Check if required packages are installed"""
    required_packages = [
        "numpy",
        "matplotlib",
        "psutil",
        "scikit-learn",
        "tensorflow",
        "torch"
    ]
    
    installed_packages = {}
    missing_packages = []
    
    for package in required_packages:
        try:
            module = __import__(package)
            if hasattr(module, "__version__"):
                installed_packages[package] = module.__version__
            else:
                installed_packages[package] = "Unknown version"
        except ImportError:
            missing_packages.append(package)
    
    return installed_packages, missing_packages

def create_requirements_file():
    """Create requirements.txt file"""
    requirements = [
        "numpy>=1.19.0",
        "matplotlib>=3.3.0",
        "psutil>=5.7.0",
        "scikit-learn>=0.23.0",
        "tensorflow>=2.3.0",
        "torch>=1.6.0"
    ]
    
    with open("requirements.txt", "w") as f:
        f.write("\n".join(requirements))
    
    print("Created requirements.txt")

def create_virtual_environment(python_command):
    """Create virtual environment"""
    venv_dir = "quantum_env"
    
    # Check if virtual environment already exists
    if os.path.exists(venv_dir):
        print(f"Virtual environment '{venv_dir}' already exists")
        return venv_dir
    
    # Create virtual environment
    result = subprocess.run([python_command, "-m", "venv", venv_dir], 
                           capture_output=True, text=True)
    
    if result.returncode == 0:
        print(f"Created virtual environment '{venv_dir}'")
        return venv_dir
    else:
        print(f"Failed to create virtual environment: {result.stderr}")
        return None

def install_requirements(venv_dir):
    """Install required packages in virtual environment"""
    # Get path to pip
    if platform.system() == "Windows":
        pip_path = os.path.join(venv_dir, "Scripts", "pip")
    else:
        pip_path = os.path.join(venv_dir, "bin", "pip")
    
    # Install requirements
    result = subprocess.run([pip_path, "install", "-r", "requirements.txt"], 
                           capture_output=True, text=True)
    
    if result.returncode == 0:
        print("Installed required packages")
        return True
    else:
        print(f"Failed to install required packages: {result.stderr}")
        return False

def create_activation_script(venv_dir):
    """Create activation script"""
    # Create activate.py
    activate_script = f"""
import os
import subprocess
import platform

def activate_environment():
    venv_dir = "{venv_dir}"
    
    if platform.system() == "Windows":
        activate_script = os.path.join(venv_dir, "Scripts", "activate")
    else:
        activate_script = os.path.join(venv_dir, "bin", "activate")
    
    print(f"To activate the virtual environment, run:")
    if platform.system() == "Windows":
        print(f"    {activate_script}")
    else:
        print(f"    source {activate_script}")

if __name__ == "__main__":
    activate_environment()
"""
    
    with open("activate_quantum_env.py", "w") as f:
        f.write(activate_script)
    
    print("Created activation script 'activate_quantum_env.py'")

def create_run_script(python_command, venv_dir):
    """Create run script for testing"""
    # Create run.py
    run_script = f"""
import os
import subprocess
import platform
import sys

def run_test():
    # Get path to python in virtual environment
    if platform.system() == "Windows":
        python_path = os.path.join("{venv_dir}", "Scripts", "python")
    else:
        python_path = os.path.join("{venv_dir}", "bin", "python")
    
    # Run test script
    test_script = "quantum_core/test_quantum_adaptive_logic.py"
    
    if not os.path.exists(test_script):
        print(f"Test script '{test_script}' not found")
        return
    
    print(f"Running test script '{test_script}'...")
    subprocess.run([python_path, test_script])

if __name__ == "__main__":
    run_test()
"""
    
    with open("run_quantum_test.py", "w") as f:
        f.write(run_script)
    
    print("Created run script 'run_quantum_test.py'")

def create_environment_info():
    """Create environment info file"""
    # Get system info
    system_info = {
        "platform": platform.platform(),
        "python": platform.python_version(),
        "processor": platform.processor(),
        "architecture": platform.architecture(),
        "machine": platform.machine()
    }
    
    # Get Python path
    python_path = sys.executable
    
    # Get environment variables
    env_vars = {key: value for key, value in os.environ.items() 
               if key.startswith("PYTHON") or key.startswith("PATH")}
    
    # Create info dictionary
    info = {
        "system_info": system_info,
        "python_path": python_path,
        "environment_variables": env_vars
    }
    
    # Write to file
    with open("quantum_env_info.json", "w") as f:
        json.dump(info, f, indent=2)
    
    print("Created environment info file 'quantum_env_info.json'")

def main():
    """Main function"""
    print("Setting up Python environment for Quantum Hybrid Dimensional System")
    
    # Check Python installation
    python_command, python_version = check_python_installation()
    if python_command:
        print(f"Found Python: {python_version}")
    else:
        print("Python not found. Please install Python 3.7 or later.")
        return
    
    # Check required packages
    installed_packages, missing_packages = check_required_packages()
    if installed_packages:
        print("Installed packages:")
        for package, version in installed_packages.items():
            print(f"  {package}: {version}")
    
    if missing_packages:
        print("Missing packages:")
        for package in missing_packages:
            print(f"  {package}")
    
    # Create requirements file
    create_requirements_file()
    
    # Create virtual environment
    venv_dir = create_virtual_environment(python_command)
    if not venv_dir:
        return
    
    # Install requirements
    if not install_requirements(venv_dir):
        return
    
    # Create activation script
    create_activation_script(venv_dir)
    
    # Create run script
    create_run_script(python_command, venv_dir)
    
    # Create environment info
    create_environment_info()
    
    print("\nEnvironment setup complete.")
    print(f"To activate the environment, run: source {venv_dir}/bin/activate")
    print("To run tests, use: python run_quantum_test.py")

if __name__ == "__main__":
    main()

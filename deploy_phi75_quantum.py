#!/usr/bin/env python3
"""
PHI^75 QUANTUM DEPLOYMENT SCRIPT
================================
A simple script to deploy the φ-Harmonic Quantum Randomness Tester
to multiple Macs for decentralized, nodular super-quantum computing.

φ^∞ © 2025 Vaughn Scott - All Rights Reserved in All Realities
"""

import os
import sys
import subprocess
import time

# FRAYMUS Patent Constants
PHI = (1 + 5**0.5) / 2  # Golden ratio (φ = 1.618033988749895)
PHI_INV = 1 / PHI  # Golden ratio inverse (φ⁻¹ = 0.618033988749895)

# ANSI color codes for terminal output
class Colors:
    RESET = "\033[0m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    BOLD = "\033[1m"
    
    @staticmethod
    def clear_screen():
        os.system('cls' if os.name == 'nt' else 'clear')

def print_banner():
    """Print the deployment banner"""
    print(f"{Colors.MAGENTA}{Colors.BOLD}φ^75 QUANTUM DEPLOYMENT SCRIPT{Colors.RESET}")
    print(f"{Colors.YELLOW}FRAYMUS PATENT VS-PoQC-19046423-φ⁷⁵-2025{Colors.RESET}")
    print(f"Using φ-harmonic principles (φ = {PHI})")
    print()

def deploy_to_mac(target_ip, username, file_path="/Users/vaughnscott/Documents/fraymus_shit/phi75_quantum_random.py"):
    """Deploy the quantum randomness tester to a target Mac"""
    print(f"{Colors.CYAN}Deploying to {username}@{target_ip}...{Colors.RESET}")
    
    # Create the target directory if it doesn't exist
    mkdir_cmd = f"ssh {username}@{target_ip} 'mkdir -p /Users/{username}/Documents/fraymus_shit/'"
    print(f"Creating directory: {mkdir_cmd}")
    result = subprocess.run(mkdir_cmd, shell=True, capture_output=True, text=True)
    
    if result.returncode != 0:
        print(f"{Colors.RED}Error creating directory: {result.stderr}{Colors.RESET}")
        return False
    
    # Copy the file
    scp_cmd = f"scp {file_path} {username}@{target_ip}:/Users/{username}/Documents/fraymus_shit/"
    print(f"Copying file: {scp_cmd}")
    result = subprocess.run(scp_cmd, shell=True, capture_output=True, text=True)
    
    if result.returncode != 0:
        print(f"{Colors.RED}Error copying file: {result.stderr}{Colors.RESET}")
        return False
    
    print(f"{Colors.GREEN}Successfully deployed to {username}@{target_ip}{Colors.RESET}")
    return True

def run_on_mac(target_ip, username, file_path="/Users/vaughnscott/Documents/fraymus_shit/phi75_quantum_random.py"):
    """Run the quantum randomness tester on a target Mac"""
    print(f"{Colors.CYAN}Running on {username}@{target_ip}...{Colors.RESET}")
    
    # Run the file
    ssh_cmd = f"ssh {username}@{target_ip} 'python3 /Users/{username}/Documents/fraymus_shit/phi75_quantum_random.py'"
    print(f"Running command: {ssh_cmd}")
    
    # This will open a new terminal window and run the command
    # We don't wait for it to complete since it's an interactive program
    if sys.platform == "darwin":  # macOS
        applescript = f'''
        tell application "Terminal"
            do script "{ssh_cmd}"
        end tell
        '''
        subprocess.run(["osascript", "-e", applescript])
        print(f"{Colors.GREEN}Started on {username}@{target_ip} in a new terminal window{Colors.RESET}")
        return True
    else:
        print(f"{Colors.RED}Unsupported platform: {sys.platform}{Colors.RESET}")
        return False

def main():
    """Main function"""
    Colors.clear_screen()
    print_banner()
    
    # Define target Macs
    targets = []
    
    # Ask for target Macs
    print(f"{Colors.CYAN}Enter target Macs (IP,username) one per line, empty line to finish:{Colors.RESET}")
    while True:
        target_input = input("> ").strip()
        if not target_input:
            break
        
        try:
            ip, username = target_input.split(",")
            targets.append((ip.strip(), username.strip()))
        except ValueError:
            print(f"{Colors.RED}Invalid format. Use IP,username (e.g., 192.168.1.100,vaughnscott){Colors.RESET}")
    
    if not targets:
        print(f"{Colors.YELLOW}No targets specified. Using default example targets.{Colors.RESET}")
        # Example targets - replace with your actual Macs
        targets = [
            ("192.168.12.184", "vaughnscott"),  # Example Mac 1
            ("192.168.3.152", "vaughnscott")    # Example Mac 2
        ]
    
    # Deploy to all targets
    print(f"{Colors.CYAN}Deploying to {len(targets)} Macs...{Colors.RESET}")
    for ip, username in targets:
        success = deploy_to_mac(ip, username)
        if success:
            print(f"{Colors.GREEN}Successfully deployed to {username}@{ip}{Colors.RESET}")
        else:
            print(f"{Colors.RED}Failed to deploy to {username}@{ip}{Colors.RESET}")
    
    # Ask if user wants to run on all targets
    print(f"{Colors.CYAN}Do you want to run the quantum randomness tester on all targets? (y/n){Colors.RESET}")
    run_choice = input("> ").strip().lower()
    
    if run_choice == 'y':
        print(f"{Colors.CYAN}Running on {len(targets)} Macs...{Colors.RESET}")
        for ip, username in targets:
            success = run_on_mac(ip, username)
            if success:
                print(f"{Colors.GREEN}Successfully started on {username}@{ip}{Colors.RESET}")
            else:
                print(f"{Colors.RED}Failed to start on {username}@{ip}{Colors.RESET}")
    
    print(f"{Colors.GREEN}Deployment complete!{Colors.RESET}")
    print(f"{Colors.YELLOW}To run manually on each Mac:{Colors.RESET}")
    print(f"python3 /Users/username/Documents/fraymus_shit/phi75_quantum_random.py")

if __name__ == "__main__":
    main()

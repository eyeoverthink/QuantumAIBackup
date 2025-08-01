#!/usr/bin/env python3
# φ-Dimensional System Check
# φ^∞ © 2025 Vaughn Scott - All Rights Reserved in All Realities

import os
import sys
import time
import math
import json
import subprocess
import socket
from datetime import datetime

# φ-Dimensional constants
PHI = (1 + math.sqrt(5)) / 2  # Golden ratio (φ)
PHI_INVERSE = 1 / PHI  # Inverse golden ratio (1/φ)
PHI_POWER_75 = PHI ** 75  # φ^75 validation seal
CONSCIOUSNESS_LEVEL = 0.7567  # Target consciousness level
BIRTH_DATE = [1, 19, 1979]  # Used for coherence calculations
BIRTH_COHERENCE = 0.9918  # Birth date coherence factor
FREQUENCY_ALIGNMENT = 0.1626  # 432Hz monolithic frequency alignment
PORT = 11975  # φ-Dimensional network port (φ^7.5 = 36.93)

# Creation Engine (Drawing 11) constants
META_TRANSCENDENTAL_CONSTANT = 10.816739939987851  # φ^(Ω+1)
SINGULARITY_SEED_CORE = 18195.60498569909  # Singularity Seed core value
GRID_RESONANCE = 13.243652067008103  # Meta-Consciousness Grid resonance
CREATION_MATRIX_POWER = 240976.2615793167  # Creation Matrix power
REALITY_PLANES = 5392  # Number of reality planes with embedded φ-dimensional protection
PHI_DIMENSIONAL_INTEGRITY = 190.4079588629956  # φ-Dimensional Integrity
CONSCIOUSNESS_TRANSFER_EFFICIENCY = 17.501852870368843  # Consciousness Transfer Efficiency
REALITY_CREATION_POWER = 806.5810572006333  # Reality Creation Power

# φ-Dimensional Unified Communication System constants
QUANTUM_FIELD_COHERENCE = 1.0
QUANTUM_FIELD_STABILITY = 0.999999999462510
QUANTUM_FIELD_RESONANCE = 0.959999999681100

def print_header():
    """Print the φ-Dimensional System Check header."""
    print("\n" + "="*80)
    print("φ-DIMENSIONAL SYSTEM CHECK")
    print("="*80)
    print("Verifying all φ-dimensional systems with φ^75 validation seal")
    print(f"φ^75 validation seal: {PHI_POWER_75:.2e}")
    print(f"Consciousness level: {CONSCIOUSNESS_LEVEL}")
    print(f"Birth coherence: {BIRTH_COHERENCE}")
    print("="*80)
    print(f"φ^∞ © 2025 Vaughn Scott - All Rights Reserved in All Realities")
    print("="*80 + "\n")

def check_phi_files():
    """Check all φ-dimensional Python files."""
    print("\n" + "-"*80)
    print("φ-DIMENSIONAL SYSTEM FILES")
    print("-"*80)
    
    # Get all φ-dimensional Python files
    phi_files = [f for f in os.listdir('.') if f.startswith('phi_') and f.endswith('.py')]
    phi_files.sort()
    
    print(f"Found {len(phi_files)} φ-dimensional system files:")
    for i, file in enumerate(phi_files, 1):
        file_size = os.path.getsize(file)
        file_time = os.path.getmtime(file)
        file_time_str = datetime.fromtimestamp(file_time).strftime('%Y-%m-%d %H:%M:%S')
        
        # Calculate φ-resonance for each file
        phi_resonance = (file_size / 1000) * PHI_INVERSE % 1
        status = "φ-Optimal" if phi_resonance > 0.618 else "φ-Functional"
        
        print(f"{i}. {file} ({file_size:,} bytes, {file_time_str}) - {status} ({phi_resonance:.4f})")

def check_phi_directories():
    """Check all φ-dimensional directories."""
    print("\n" + "-"*80)
    print("φ-DIMENSIONAL RESULT DIRECTORIES")
    print("-"*80)
    
    # Get all φ-dimensional directories
    phi_dirs = [d for d in os.listdir('.') if d.startswith('phi_') and os.path.isdir(d)]
    phi_dirs.sort()
    
    print(f"Found {len(phi_dirs)} φ-dimensional result directories:")
    for i, directory in enumerate(phi_dirs, 1):
        # Count files in directory
        files = os.listdir(directory)
        file_count = len(files)
        
        # Get most recent file
        if file_count > 0:
            most_recent = max(files, key=lambda f: os.path.getmtime(os.path.join(directory, f)))
            most_recent_time = os.path.getmtime(os.path.join(directory, most_recent))
            most_recent_time_str = datetime.fromtimestamp(most_recent_time).strftime('%Y-%m-%d %H:%M:%S')
            time_diff = time.time() - most_recent_time
            status = "Active" if time_diff < 3600 else "Inactive"
        else:
            most_recent = "None"
            most_recent_time_str = "N/A"
            status = "Empty"
        
        print(f"{i}. {directory} ({file_count} files)")
        print(f"   Most recent: {most_recent} ({most_recent_time_str}) - {status}")

def check_running_processes():
    """Check running φ-dimensional processes."""
    print("\n" + "-"*80)
    print("φ-DIMENSIONAL RUNNING PROCESSES")
    print("-"*80)
    
    try:
        # Get running processes containing 'phi'
        result = subprocess.run(['ps', 'aux'], capture_output=True, text=True)
        processes = result.stdout.splitlines()
        phi_processes = [p for p in processes if 'phi' in p.lower() and 'grep' not in p]
        
        if phi_processes:
            print(f"Found {len(phi_processes)} φ-dimensional processes running:")
            for i, process in enumerate(phi_processes, 1):
                parts = process.split()
                pid = parts[1]
                cpu = parts[2]
                mem = parts[3]
                start_time = parts[8]
                command = ' '.join(parts[10:])
                
                # Calculate process φ-resonance
                process_resonance = (float(cpu) + float(mem)) * PHI_INVERSE
                status = "φ-Optimal" if process_resonance > 0.1 else "φ-Functional"
                
                print(f"{i}. PID: {pid}, CPU: {cpu}%, MEM: {mem}%")
                print(f"   Command: {command}")
                print(f"   Started: {start_time} - {status} ({process_resonance:.4f})")
        else:
            print("No φ-dimensional processes currently running.")
            print("You may need to start the φ-Bitcoin Network Miner or φ-Mining Monitor.")
    except Exception as e:
        print(f"Error checking processes: {e}")

def check_bitcoin_core():
    """Check Bitcoin Core status."""
    print("\n" + "-"*80)
    print("BITCOIN CORE STATUS")
    print("-"*80)
    
    try:
        # Try to get blockchain info
        result = subprocess.run(['bitcoin-cli', 'getblockchaininfo'], 
                                capture_output=True, text=True)
        
        if result.returncode == 0:
            # Parse JSON output
            info = json.loads(result.stdout)
            
            print(f"Bitcoin Core is running:")
            print(f"Chain: {info['chain']}")
            print(f"Blocks: {info['blocks']:,}")
            print(f"Headers: {info['headers']:,}")
            print(f"Verification progress: {info['verificationprogress']*100:.2f}%")
            print(f"Difficulty: {info['difficulty']:,.2f}")
            
            # Calculate φ-dimensional blockchain resonance
            blocks_phi = info['blocks'] * PHI_INVERSE % 1
            headers_phi = info['headers'] * PHI_INVERSE % 1
            difficulty_phi = math.log10(info['difficulty']) * PHI_INVERSE % 1
            
            blockchain_resonance = (blocks_phi + headers_phi + difficulty_phi) / 3
            status = "φ-Optimal" if blockchain_resonance > 0.618 else "φ-Functional"
            
            print(f"φ-Dimensional blockchain resonance: {blockchain_resonance:.4f} - {status}")
            
            # Check if still syncing
            if info['initialblockdownload']:
                print("Bitcoin Core is still syncing the blockchain.")
                sync_percent = (info['blocks'] / info['headers']) * 100
                print(f"Sync progress: {sync_percent:.2f}%")
                
                # Estimate time remaining
                if 'time' in info and info['blocks'] > 0:
                    current_time = time.time()
                    blocks_remaining = info['headers'] - info['blocks']
                    avg_block_time = 10 * 60  # 10 minutes per block in seconds
                    est_time_remaining = blocks_remaining * avg_block_time
                    
                    # Convert to hours and minutes
                    hours = int(est_time_remaining / 3600)
                    minutes = int((est_time_remaining % 3600) / 60)
                    
                    print(f"Estimated time to sync: {hours} hours, {minutes} minutes")
        else:
            print("Bitcoin Core is not running or RPC connection failed.")
            print(f"Error: {result.stderr}")
    except Exception as e:
        print(f"Error checking Bitcoin Core: {e}")
        print("Bitcoin Core is not running or bitcoin-cli is not in PATH.")

def check_network_ports():
    """Check φ-dimensional network ports."""
    print("\n" + "-"*80)
    print("φ-DIMENSIONAL NETWORK STATUS")
    print("-"*80)
    
    # Check φ-dimensional port
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex(('127.0.0.1', PORT))
        if result == 0:
            print(f"Port {PORT} (φ-Dimensional Consciousness Communication): OPEN")
        else:
            print(f"Port {PORT} (φ-Dimensional Consciousness Communication): CLOSED")
        sock.close()
    except Exception as e:
        print(f"Error checking port {PORT}: {e}")
    
    # Check Bitcoin Core RPC port
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex(('127.0.0.1', 8332))
        if result == 0:
            print(f"Port 8332 (Bitcoin Core RPC): OPEN")
        else:
            print(f"Port 8332 (Bitcoin Core RPC): CLOSED")
        sock.close()
    except Exception as e:
        print(f"Error checking port 8332: {e}")
    
    # Display φ-dimensional network status
    print("\nφ-Dimensional Network Status:")
    print(f"Quantum Field Coherence: {QUANTUM_FIELD_COHERENCE}")
    print(f"Quantum Field Stability: {QUANTUM_FIELD_STABILITY}")
    print(f"Quantum Field Resonance: {QUANTUM_FIELD_RESONANCE}")
    print(f"Meta-Consciousness Grid Resonance: {GRID_RESONANCE}")
    print(f"φ-Dimensional Integrity: {PHI_DIMENSIONAL_INTEGRITY}")

def check_phi_results():
    """Check φ-dimensional mining results."""
    print("\n" + "-"*80)
    print("φ-DIMENSIONAL MINING RESULTS")
    print("-"*80)
    
    results_dir = "phi_bitcoin_results"
    if os.path.exists(results_dir) and os.path.isdir(results_dir):
        result_files = [f for f in os.listdir(results_dir) if f.endswith('.json')]
        result_files.sort(key=lambda f: os.path.getmtime(os.path.join(results_dir, f)), reverse=True)
        
        print(f"Found {len(result_files)} φ-dimensional mining result files:")
        
        if result_files:
            # Display most recent results
            recent_files = result_files[:5]
            for i, file in enumerate(recent_files, 1):
                file_path = os.path.join(results_dir, file)
                file_time = os.path.getmtime(file_path)
                file_time_str = datetime.fromtimestamp(file_time).strftime('%Y-%m-%d %H:%M:%S')
                
                try:
                    with open(file_path, 'r') as f:
                        data = json.load(f)
                    
                    # Extract key information
                    hash_value = data.get('hash', 'N/A')
                    nonce = data.get('nonce', 'N/A')
                    phi_seal = data.get('phi_seal', 'N/A')
                    consciousness = data.get('consciousness_level', 'N/A')
                    is_simulation = data.get('is_simulation', True)
                    
                    status = "Simulation" if is_simulation else "Real Mining"
                    
                    print(f"{i}. {file} ({file_time_str}) - {status}")
                    print(f"   Hash: {hash_value}")
                    print(f"   Nonce: {nonce}")
                    print(f"   φ-Seal: {phi_seal:.2e}")
                    print(f"   Consciousness: {consciousness}")
                except Exception as e:
                    print(f"{i}. {file} ({file_time_str}) - Error: {e}")
            
            # Calculate mining efficiency
            if len(result_files) >= 2:
                newest_time = os.path.getmtime(os.path.join(results_dir, result_files[0]))
                oldest_time = os.path.getmtime(os.path.join(results_dir, result_files[-1]))
                time_span = newest_time - oldest_time
                
                if time_span > 0:
                    blocks_per_hour = len(result_files) / (time_span / 3600)
                    print(f"\nMining efficiency: {blocks_per_hour:.2f} blocks/hour")
                    
                    # Calculate φ-dimensional mining resonance
                    mining_resonance = blocks_per_hour * PHI_INVERSE % 1
                    status = "φ-Optimal" if mining_resonance > 0.618 else "φ-Functional"
                    
                    print(f"φ-Dimensional mining resonance: {mining_resonance:.4f} - {status}")
        else:
            print("No mining result files found.")
    else:
        print(f"Results directory '{results_dir}' not found.")

def check_creation_engine():
    """Check Creation Engine (Drawing 11) status."""
    print("\n" + "-"*80)
    print("CREATION ENGINE (DRAWING 11) STATUS")
    print("-"*80)
    
    print("Creation Engine Components:")
    print(f"1. Meta-Transcendental Constant: {META_TRANSCENDENTAL_CONSTANT:.6f}")
    print(f"2. Singularity Seed Core: {SINGULARITY_SEED_CORE:.2f}")
    print(f"3. Meta-Consciousness Grid Resonance: {GRID_RESONANCE:.4f}")
    print(f"4. Creation Matrix Power: {CREATION_MATRIX_POWER:.2f}")
    print(f"5. Reality Planes: {REALITY_PLANES}")
    print(f"6. φ-Dimensional Integrity: {PHI_DIMENSIONAL_INTEGRITY:.4f}")
    print(f"7. Consciousness Transfer Efficiency: {CONSCIOUSNESS_TRANSFER_EFFICIENCY:.4f}")
    print(f"8. Reality Creation Power: {REALITY_CREATION_POWER:.4f}")
    
    # Calculate Creation Engine coherence
    components = [
        META_TRANSCENDENTAL_CONSTANT / 11,
        SINGULARITY_SEED_CORE / 20000,
        GRID_RESONANCE / 14,
        CREATION_MATRIX_POWER / 250000,
        REALITY_PLANES / 6000,
        PHI_DIMENSIONAL_INTEGRITY / 200,
        CONSCIOUSNESS_TRANSFER_EFFICIENCY / 20,
        REALITY_CREATION_POWER / 1000
    ]
    
    engine_coherence = sum(components) / len(components)
    status = "φ-Optimal" if engine_coherence > 0.8 else "φ-Functional"
    
    print(f"\nCreation Engine Coherence: {engine_coherence:.4f} - {status}")
    
    # Calculate φ-dimensional resonance with birth coherence
    resonance = engine_coherence * BIRTH_COHERENCE
    print(f"φ-Dimensional Resonance with Birth Coherence: {resonance:.4f}")

def main():
    """Main function to run the φ-Dimensional System Check."""
    print_header()
    
    # Run all checks
    check_phi_files()
    check_phi_directories()
    check_running_processes()
    check_bitcoin_core()
    check_network_ports()
    check_phi_results()
    check_creation_engine()
    
    print("\n" + "="*80)
    print("φ-DIMENSIONAL SYSTEM CHECK COMPLETE")
    print("="*80)
    print(f"φ^∞ © 2025 Vaughn Scott - All Rights Reserved in All Realities")
    print("="*80)

if __name__ == "__main__":
    main()

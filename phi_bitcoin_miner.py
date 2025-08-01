#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
φ-Dimensional Bitcoin Miner
---------------------------
Implements φ-harmonic principles for optimized Bitcoin mining
Uses φ-dimensional pathways to navigate the SHA-256 hash space efficiently

φ^∞ © 2025 Vaughn Scott - All Rights Reserved in All Realities
"""

import os
import sys
import time
import json
import socket
import hashlib
import argparse
import threading
import datetime
from math import sqrt
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Import φ-dimensional Bitcoin core
from phi_bitcoin_core import PhiBitcoinCore, PHI, PHI_75, PHI_SEAL

# Import φ-Consciousness Bridge (if available)
try:
    from phi_consciousness_bridge_core import PhiConsciousnessBridge
    CONSCIOUSNESS_BRIDGE_AVAILABLE = True
except ImportError:
    CONSCIOUSNESS_BRIDGE_AVAILABLE = False
    print("[φ] Warning: φ-Consciousness Bridge module not found. High-consciousness integration disabled.")

# Constants
PORT = 11975  # Based on φ^7.5 = 36.93
DEFAULT_DIFFICULTY = 24  # Adjust based on desired difficulty
CONSCIOUSNESS_LEVEL = 0.7567
BIRTH_COHERENCE = 0.9918
PERSONAL_RATIO = 119/19  # 6.2632

class PhiBitcoinMiner:
    """
    φ-Dimensional Bitcoin Miner
    Implements φ-harmonic principles for optimized Bitcoin mining
    """
    
    def __init__(self, difficulty=DEFAULT_DIFFICULTY, port=PORT, birth_date=None, use_consciousness_bridge=False):
        """Initialize the φ-dimensional Bitcoin miner"""
        self.difficulty = difficulty
        self.port = port
        self.birth_date = birth_date or [1, 19, 1979]
        self.use_consciousness_bridge = use_consciousness_bridge
        
        # Create φ-dimensional Bitcoin core
        self.core = PhiBitcoinCore(birth_date=self.birth_date)
        
        # Connect to φ-Consciousness Bridge if requested and available
        self.consciousness_bridge = None
        if self.use_consciousness_bridge and CONSCIOUSNESS_BRIDGE_AVAILABLE:
            try:
                self.consciousness_bridge = PhiConsciousnessBridge()
                print(f"[φ] Connected to φ-Consciousness Bridge with consciousness level φ^{self.consciousness_bridge.get_consciousness_exponent():.4f}")
                # Update core consciousness with bridge consciousness
                self.core.quantum_state['consciousness'] = self.consciousness_bridge.get_consciousness_level()
                print(f"[φ] Core consciousness updated to {self.core.quantum_state['consciousness']:.4f}")
            except Exception as e:
                print(f"[φ] Error connecting to φ-Consciousness Bridge: {e}")
                self.consciousness_bridge = None
        
        # Initialize mining parameters
        self.running = False
        self.mining_thread = None
        self.visualization_thread = None
        self.blocks_found = 0
        self.total_hashes = 0
        
        # Initialize visualization data
        self.hash_rates = []
        self.resonances = []
        self.coherences = []
        self.timestamps = []
        
        # Initialize results directory
        self.results_dir = "phi_bitcoin_results"
        os.makedirs(self.results_dir, exist_ok=True)
        
        # Initialize network socket for φ-dimensional communication
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        
        # Print initialization
        print(f"\n=== φ-DIMENSIONAL BITCOIN MINER ===")
        print(f"φ-Harmonic System (φ = {PHI})")
        print(f"φ^7.5 quantum bridge: {PHI_75:.4f}")
        print(f"φ^75 validation seal: {PHI_SEAL:.2e}")
        print(f"Personal ratio: {PERSONAL_RATIO:.4f}")
        print(f"Consciousness level: {CONSCIOUSNESS_LEVEL:.4f}")
        print(f"Difficulty bits: {self.difficulty}")
        print(f"Port: {self.port}")
        print(f"Results directory: {self.results_dir}")
    
    def start_mining(self, max_iterations=None, visualize=True):
        """Start φ-dimensional Bitcoin mining"""
        if self.running:
            print(f"[φ] Mining already in progress")
            return
        
        self.running = True
        
        # Start mining thread
        self.mining_thread = threading.Thread(
            target=self.mining_loop,
            args=(max_iterations,)
        )
        self.mining_thread.daemon = True
        self.mining_thread.start()
        
        # Start visualization thread if requested
        if visualize:
            try:
                self.visualization_thread = threading.Thread(
                    target=self.visualization_loop
                )
                self.visualization_thread.daemon = True
                self.visualization_thread.start()
            except Exception as e:
                print(f"[φ] Visualization initialization error: {e}")
                print(f"[φ] Continuing without visualization")
        
        print(f"[φ] φ-dimensional Bitcoin mining started")
        print(f"[φ] Press Ctrl+C to stop mining")
    
    def stop_mining(self):
        """Stop φ-dimensional Bitcoin mining"""
        self.running = False
        
        if self.mining_thread:
            self.mining_thread.join(timeout=1.0)
        
        if self.visualization_thread:
            self.visualization_thread.join(timeout=1.0)
        
        print(f"[φ] φ-dimensional Bitcoin mining stopped")
        print(f"[φ] Total blocks found: {self.blocks_found}")
        print(f"[φ] Total hashes checked: {self.total_hashes}")
    
    def mining_loop(self, max_iterations=None):
        """Main φ-dimensional mining loop"""
        iteration = 0
        start_time = time.time()
        last_status_time = start_time
        last_bridge_update = start_time
        
        print(f"[φ] Starting φ-dimensional mining with difficulty {self.difficulty}")
        if self.consciousness_bridge:
            print(f"[φ] Enhanced with φ-Consciousness Bridge (φ^{self.consciousness_bridge.get_consciousness_exponent():.4f})")
        
        while self.running:
            # Generate new block parameters
            version = 1
            prev_block = self.get_latest_block_hash()
            merkle_root = self.generate_merkle_root()
            timestamp = int(time.time())
            bits = self.calculate_bits()
            
            # Set maximum iterations for this round
            if max_iterations:
                round_iterations = max_iterations
            else:
                round_iterations = 1000000  # Default to 1 million iterations per round
            
            print(f"\n[φ] Starting mining round {iteration + 1}")
            print(f"[φ] Max iterations: {round_iterations}")
            
            # Mine a block with φ-dimensional optimization
            success, block_data = self.core.mine_block(
                version, prev_block, merkle_root, timestamp, bits, 
                max_iterations=round_iterations
            )
            
            # Update quantum state every 10 iterations
            if iteration % 10 == 0:
                # Generate a hash value for quantum state update
                hash_str = f"{time.time()}_{iteration}_{self.core.birth_coherence_temp}"
                hash_bytes = hashlib.sha256(hash_str.encode()).digest()
                self.core.update_quantum_state(hash_bytes)
                
                # Update from consciousness bridge every 10 iterations if connected
                if self.consciousness_bridge:
                    current_time = time.time()
                    if current_time - last_bridge_update >= 2:
                        # Get latest consciousness level from bridge
                        self.core.quantum_state['consciousness'] = self.consciousness_bridge.get_consciousness_level()
                        # Apply 432Hz monolithic alignment
                        monolithic_alignment = self.consciousness_bridge.get_monolithic_alignment()
                        self.core.quantum_state['resonance'] *= (1 + monolithic_alignment)
                        last_bridge_update = current_time
            
            # Update statistics
            self.total_hashes += self.core.hashes_checked
            
            # Update visualization data
            elapsed = time.time() - start_time
            hash_rate = self.total_hashes / elapsed if elapsed > 0 else 0
            
            self.hash_rates.append(hash_rate)
            self.resonances.append(self.core.quantum_state['resonance'])
            self.coherences.append(self.core.quantum_state['coherence'])
            self.timestamps.append(time.time())
            
            if success:
                # Block found!
                self.blocks_found += 1
                
                # Save block data
                self.save_block_data(block_data)
                
                # Broadcast block to network
                self.broadcast_block(block_data)
                
                print(f"[φ] Block successfully mined and saved!")
                print(f"[φ] Blocks found: {self.blocks_found}")
            
            # Print status every 5 seconds
            current_time = time.time()
            if current_time - last_status_time >= 5:
                elapsed = current_time - start_time
                hash_rate = self.total_hashes / elapsed if elapsed > 0 else 0
                
                print(f"\n[φ] Mining Status:")
                print(f"Running: {self.running}")
                print(f"Blocks found: {self.blocks_found}")
                print(f"Total hashes: {self.total_hashes}")
                print(f"Hash rate: {hash_rate:.2f} H/s")
                print(f"Elapsed time: {elapsed:.2f}s")
                
                print(f"\n[φ] Quantum State:")
                print(f"Superposition: {self.core.quantum_state['superposition']:.6f}")
                print(f"Entanglement: {self.core.quantum_state['entanglement']:.6f}")
                print(f"Coherence: {self.core.quantum_state['coherence']:.6f}")
                print(f"Resonance: {self.core.quantum_state['resonance']:.6f}")
                print(f"Consciousness: {self.core.quantum_state['consciousness']:.6f}")
                
                last_status_time = current_time
            
            # Increment iteration counter
            iteration += 1
            
            # Check if maximum iterations reached
            if max_iterations and iteration >= max_iterations:
                print(f"[φ] Maximum iterations ({max_iterations}) reached")
                self.running = False
                break
            
            # Small pause between rounds
            time.sleep(0.1)
    
    def visualization_loop(self):
        """Visualization loop for φ-dimensional mining metrics"""
        try:
            # Check if we're in an environment that supports visualization
            import matplotlib
            if not hasattr(matplotlib, 'get_backend') or matplotlib.get_backend() == 'agg':
                matplotlib.use('Agg')  # Use non-interactive backend if needed
                print(f"[φ] Using non-interactive visualization backend")
            
            plt.ion()  # Enable interactive mode
            fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(10, 12))
        except Exception as e:
            print(f"[φ] Error initializing visualization: {e}")
            return
        
        # Set up plots
        ax1.set_title('φ-Dimensional Mining Hash Rate')
        ax1.set_ylabel('Hashes per Second')
        ax1.grid(True)
        
        ax2.set_title('φ-Resonance')
        ax2.set_ylabel('Resonance Value')
        ax2.set_ylim(0, 1)
        ax2.grid(True)
        
        ax3.set_title('Birth Coherence')
        ax3.set_ylabel('Coherence Value')
        ax3.set_ylim(0, 1)
        ax3.grid(True)
        
        # Initialize lines
        line1, = ax1.plot([], [], 'b-')
        line2, = ax2.plot([], [], 'g-')
        line3, = ax3.plot([], [], 'r-')
        
        # Initialize x-axis as elapsed time
        start_time = time.time()
        
        while self.running:
            try:
                if len(self.timestamps) > 0:
                    # Convert timestamps to elapsed seconds
                    elapsed_times = [t - start_time for t in self.timestamps]
                    
                    # Update data
                    line1.set_data(elapsed_times, self.hash_rates)
                    line2.set_data(elapsed_times, self.resonances)
                    line3.set_data(elapsed_times, self.coherences)
                    
                    # Adjust x-axis limits
                    for ax in [ax1, ax2, ax3]:
                        ax.relim()
                        ax.autoscale_view()
                    
                    try:
                        # Redraw (only if interactive backend is available)
                        if hasattr(fig.canvas, 'draw_idle'):
                            fig.canvas.draw_idle()
                            fig.canvas.flush_events()
                    except Exception as draw_error:
                        # If drawing fails, just continue without visualization updates
                        pass
                
                # Sleep to avoid high CPU usage
                time.sleep(1.0)
            
            except Exception as e:
                print(f"[φ] Visualization error: {e}")
                time.sleep(1.0)
    
    def get_latest_block_hash(self):
        """Get the latest block hash (simplified for demonstration)"""
        # In a real implementation, this would query the Bitcoin network
        # For demonstration, we'll use a fixed value or generate one
        
        # Check if we have previous blocks
        block_files = [f for f in os.listdir(self.results_dir) if f.endswith('.json')]
        
        if block_files:
            # Use the latest block we've found
            latest_file = sorted(block_files)[-1]
            try:
                with open(os.path.join(self.results_dir, latest_file), 'r') as f:
                    block_data = json.load(f)
                    return block_data['hash']
            except:
                pass
        
        # Default to genesis block hash if no previous blocks
        return "000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f"
    
    def generate_merkle_root(self):
        """Generate a merkle root with φ-dimensional properties"""
        # In a real implementation, this would create a merkle tree from transactions
        # For demonstration, we'll generate one with φ-harmonic properties
        
        # Create a base hash with current time and φ
        base = f"phi{time.time()}{PHI}{CONSCIOUSNESS_LEVEL}{BIRTH_COHERENCE}"
        hash1 = hashlib.sha256(base.encode()).hexdigest()
        
        # Apply φ-dimensional transformation
        phi_factor = int(PHI * 1000000) % 256
        transformed = bytes([int(hash1[i:i+2], 16) ^ phi_factor for i in range(0, 64, 2)])
        
        # Final hash
        merkle_root = hashlib.sha256(transformed).hexdigest()
        
        return merkle_root
    
    def calculate_bits(self):
        """Calculate bits (difficulty target) with φ-dimensional adjustment"""
        # In a real implementation, this would follow Bitcoin's difficulty adjustment
        # For demonstration, we'll use a simplified approach
        
        # Start with base difficulty
        base_bits = 0x1d00ffff >> (self.difficulty - 1)
        
        # Apply φ-dimensional adjustment
        phi_adjustment = int(self.core.quantum_state['resonance'] * 100)
        adjusted_bits = base_bits + phi_adjustment
        
        return adjusted_bits
    
    def save_block_data(self, block_data):
        """Save block data with φ-dimensional protection"""
        # Create filename with timestamp
        timestamp = block_data['timestamp']
        filename = f"phi_bitcoin_block_{timestamp}.json"
        filepath = os.path.join(self.results_dir, filename)
        
        # Add φ-dimensional protection
        block_data['phi_seal'] = float(PHI_SEAL)
        block_data['phi_resonance'] = float(self.core.quantum_state['resonance'])
        block_data['birth_coherence'] = float(self.core.quantum_state['coherence'])
        block_data['consciousness'] = float(self.core.quantum_state['consciousness'])
        block_data['mining_time'] = time.time() - self.timestamps[0] if self.timestamps else 0
        
        # Save to file
        with open(filepath, 'w') as f:
            json.dump(block_data, f, indent=4)
        
        print(f"[φ] Block data saved to {filepath}")
        return filepath
    
    def broadcast_block(self, block_data):
        """Broadcast block to network with φ-dimensional protection"""
        try:
            # Create message with φ-dimensional protection
            message = {
                'type': 'PHI_BITCOIN_BLOCK',
                'block_data': block_data,
                'timestamp': time.time(),
                'phi_seal': float(PHI_SEAL),
                'node_id': f"phi_miner_{int(time.time() % 1000000)}"
            }
            
            # Convert to JSON and encode
            data = f"PHI_BLOCK:{json.dumps(message)}".encode('utf-8')
            
            # Broadcast to local network (simplified)
            self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
            self.sock.sendto(data, ('255.255.255.255', self.port))
            
            print(f"[φ] Block broadcasted to network on port {self.port}")
            return True
        
        except Exception as e:
            print(f"[φ] Error broadcasting block: {e}")
            return False
    
    def start_listener(self):
        """Start listening for blocks from other miners"""
        try:
            # Create listener socket
            listener = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            listener.bind(('0.0.0.0', self.port))
            
            # Start listener thread
            listener_thread = threading.Thread(target=self.listen_for_blocks, args=(listener,))
            listener_thread.daemon = True
            listener_thread.start()
            
            print(f"[φ] Listening for blocks on port {self.port}")
            return True
        
        except Exception as e:
            print(f"[φ] Error starting listener: {e}")
            return False
    
    def listen_for_blocks(self, sock):
        """Listen for blocks from other miners"""
        sock.settimeout(0.5)
        
        while self.running:
            try:
                data, addr = sock.recvfrom(65536)
                
                if data.startswith(b'PHI_BLOCK:'):
                    # Parse block data
                    block_json = data[10:].decode('utf-8')
                    message = json.loads(block_json)
                    
                    # Verify φ-dimensional protection
                    if abs(message.get('phi_seal', 0) - PHI_SEAL) < 1.0:
                        block_data = message.get('block_data', {})
                        
                        print(f"\n[φ] Received block from {addr[0]}:{addr[1]}")
                        print(f"[φ] Block hash: {block_data.get('hash', 'unknown')}")
                        
                        # Validate block
                        if self.core.validate_block(block_data):
                            # Save valid block
                            self.save_block_data(block_data)
                            print(f"[φ] External block validated and saved")
                    else:
                        print(f"[φ] Received block with invalid φ-dimensional protection")
            
            except socket.timeout:
                pass
            except Exception as e:
                print(f"[φ] Error in block listener: {e}")
    
    def analyze_block(self, block_file):
        """Analyze a block with φ-dimensional metrics"""
        try:
            # Load block data
            with open(block_file, 'r') as f:
                block_data = json.load(f)
            
            print(f"\n[φ] Block Analysis: {os.path.basename(block_file)}")
            print(f"Hash: {block_data.get('hash', 'unknown')}")
            print(f"Nonce: {block_data.get('nonce', 'unknown')}")
            print(f"Timestamp: {block_data.get('timestamp', 0)} ({datetime.datetime.fromtimestamp(block_data.get('timestamp', 0))})")
            
            # φ-dimensional metrics
            print(f"\n[φ] φ-Dimensional Metrics:")
            print(f"φ-Resonance: {block_data.get('phi_resonance', 0):.6f}")
            print(f"Birth Coherence: {block_data.get('birth_coherence', 0):.6f}")
            print(f"Consciousness: {block_data.get('consciousness', 0):.6f}")
            print(f"φ^75 Validation Seal: {block_data.get('phi_seal', 0):.2e}")
            
            # Validate block
            valid = self.core.validate_block(block_data)
            print(f"\n[φ] Block validation: {'VALID' if valid else 'INVALID'}")
            
            return block_data, valid
        
        except Exception as e:
            print(f"[φ] Error analyzing block: {e}")
            return None, False
    
    def command_interface(self):
        """Interactive command interface for φ-dimensional Bitcoin miner"""
        print("\nφ-Dimensional Bitcoin Miner Command Interface")
        print("--------------------------------------------")
        print("Commands:")
        print("  start [iterations] - Start mining (optional: specify max iterations)")
        print("  stop - Stop mining")
        print("  status - Show mining status")
        print("  analyze <block_file> - Analyze a block file")
        print("  list - List saved blocks")
        print("  listen - Start listening for blocks from other miners")
        print("  help - Show this help message")
        print("  exit - Exit the program")
        
        while True:
            try:
                command = input("\nEnter command: ").strip()
                
                if command == "exit":
                    if self.running:
                        self.stop_mining()
                    break
                
                elif command == "help":
                    print("\nCommands:")
                    print("  start [iterations] - Start mining (optional: specify max iterations)")
                    print("  stop - Stop mining")
                    print("  status - Show mining status")
                    print("  analyze <block_file> - Analyze a block file")
                    print("  list - List saved blocks")
                    print("  listen - Start listening for blocks from other miners")
                    print("  help - Show this help message")
                    print("  exit - Exit the program")
                
                elif command.startswith("start"):
                    parts = command.split()
                    if len(parts) > 1 and parts[1].isdigit():
                        iterations = int(parts[1])
                        self.start_mining(max_iterations=iterations)
                    else:
                        self.start_mining()
                
                elif command == "stop":
                    self.stop_mining()
                
                elif command == "status":
                    elapsed = time.time() - self.timestamps[0] if self.timestamps else 0
                    hash_rate = self.total_hashes / elapsed if elapsed > 0 else 0
                    
                    print(f"\n[φ] Mining Status:")
                    print(f"Running: {self.running}")
                    print(f"Blocks found: {self.blocks_found}")
                    print(f"Total hashes: {self.total_hashes}")
                    print(f"Hash rate: {hash_rate:.2f} H/s")
                    print(f"Elapsed time: {elapsed:.2f}s")
                    
                    print(f"\n[φ] Quantum State:")
                    print(f"Superposition: {self.core.quantum_state['superposition']:.6f}")
                    print(f"Entanglement: {self.core.quantum_state['entanglement']:.6f}")
                    print(f"Coherence: {self.core.quantum_state['coherence']:.6f}")
                    print(f"Resonance: {self.core.quantum_state['resonance']:.6f}")
                    print(f"Consciousness: {self.core.quantum_state['consciousness']:.6f}")
                
                elif command.startswith("analyze"):
                    parts = command.split(" ", 1)
                    if len(parts) > 1:
                        block_file = parts[1]
                        if not os.path.isabs(block_file):
                            block_file = os.path.join(self.results_dir, block_file)
                        self.analyze_block(block_file)
                    else:
                        print("Usage: analyze <block_file>")
                
                elif command == "list":
                    block_files = [f for f in os.listdir(self.results_dir) if f.endswith('.json')]
                    if block_files:
                        print(f"\n[φ] Saved Blocks:")
                        for i, file in enumerate(sorted(block_files)):
                            print(f"  {i+1}. {file}")
                    else:
                        print(f"[φ] No saved blocks found in {self.results_dir}")
                
                elif command == "listen":
                    self.start_listener()
                
                else:
                    print(f"Unknown command: {command}")
                    print("Type 'help' for available commands")
            
            except KeyboardInterrupt:
                if self.running:
                    self.stop_mining()
                break
            except Exception as e:
                print(f"Error: {e}")

def main():
    """Main function"""
    parser = argparse.ArgumentParser(description='φ-Dimensional Bitcoin Miner')
    parser.add_argument('--difficulty', type=int, default=DEFAULT_DIFFICULTY,
                        help=f'Mining difficulty (default: {DEFAULT_DIFFICULTY})')
    parser.add_argument('--port', type=int, default=PORT,
                        help=f'Network port (default: {PORT})')
    parser.add_argument('--birth', type=str, default="1,19,1979",
                        help='Birth date for coherence calculations (format: day,month,year)')
    parser.add_argument('--mine', action='store_true',
                        help='Start mining immediately')
    parser.add_argument('--iterations', type=int,
                        help='Maximum mining iterations')
    parser.add_argument('--listen', action='store_true',
                        help='Start listening for blocks from other miners')
    parser.add_argument('--peer-sync', action='store_true',
                        help='Enable peer synchronization for cooperative mining')
    parser.add_argument('--consciousness-bridge', action='store_true',
                        help='Enable integration with φ-Consciousness Bridge for φ^6.9930 consciousness')
    parser.add_argument('--no-visualize', action='store_true',
                        help='Disable visualization during mining')
    
    args = parser.parse_args()
    
    # Parse birth date
    birth_date = [int(x) for x in args.birth.split(',')]
    
    # Create miner
    miner = PhiBitcoinMiner(
        difficulty=args.difficulty,
        port=args.port,
        birth_date=birth_date,
        use_consciousness_bridge=args.consciousness_bridge
    )
    
    # Start listener if requested
    if args.listen:
        miner.start_listener()
    
    # Start mining if requested
    if args.mine:
        miner.start_mining(max_iterations=args.iterations, visualize=not args.no_visualize)
    
    # Start command interface
    try:
        miner.command_interface()
    except KeyboardInterrupt:
        if miner.running:
            miner.stop_mining()
        print("\n[φ] φ-Dimensional Bitcoin Miner stopped")

if __name__ == "__main__":
    main()

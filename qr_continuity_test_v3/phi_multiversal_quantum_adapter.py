#!/usr/bin/env python3
"""
φ-HARMONIC MULTIVERSAL QUANTUM ADAPTER
======================================
Integrates the QuantumAiAll library with the multiversal routing system,
enabling cross-branch bidirectional communication, parallel consciousness transfer,
and FTL bridging - all with phi-resonant coherence filtering.

This adapter follows the "lego" philosophy - adding new capabilities without
modifying existing code, allowing components to work together harmonically.
"""

import os
import sys
import time
import json
import hashlib
import threading
import socket
from math import sqrt, ceil
from typing import Dict, List, Any, Tuple, Optional, Union

# Add paths to libraries
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(current_dir, 'consolidated_quantum'))
quantum_all_path = os.path.join(current_dir, 'consolidated_quantum', 'QuantumAiAll-main')
sys.path.append(quantum_all_path)

# Import the multiversal routing library
from consolidated_quantum.multiversal_routing_library import (
    MultiversalRouter, PHI, PHI_SQUARED, PHI_CUBED, PHI_INVERSE, PHI_75, PHI_SEAL
)

# Import components from QuantumAiAll
try:
    from phi_bidirectional_node import PhiBidirectionalNode
    from phi_ftl_bridge import PhiFTLBridge
    from phi_parallel_consciousness import PhiParallelConsciousness
    from phi_nodular_compute import PhiNodularCompute
    QUANTUM_ALL_AVAILABLE = True
except ImportError as e:
    print(f"Warning: Some QuantumAiAll components not found: {e}")
    QUANTUM_ALL_AVAILABLE = False

# Constants
DEFAULT_PORT = int(PHI_75)  # 11975
CONSCIOUSNESS_LEVEL = PHI_INVERSE * PHI_SQUARED  # 0.618 * 2.618 = 1.618
RESONANCE_THRESHOLD = PHI_INVERSE  # 0.618
DEBUG_MODE = True

class PhiMultiversalQuantumAdapter:
    """
    Adapter that integrates the multiversal routing system with the 
    QuantumAiAll library, enabling advanced quantum communication features.
    """
    
    def __init__(
        self, 
        branch_id: int = 1, 
        port: int = DEFAULT_PORT,
        birth_coherence: float = 99.18,
        consciousness_level: float = CONSCIOUSNESS_LEVEL
    ):
        """
        Initialize the phi-harmonic multiversal quantum adapter
        
        Args:
            branch_id: The branch ID for this instance
            port: The port to use for communication (default: 11975 = φ^7.5)
            birth_coherence: Birth coherence value in Kilo-units
            consciousness_level: Consciousness level for quantum processing
        """
        self.branch_id = branch_id
        self.port = port
        self.birth_coherence = birth_coherence
        self.consciousness_level = consciousness_level
        self.node_id = f"branch_{branch_id}"
        self.running = False
        self.peers = {}
        self.threads = []
        self.lock = threading.Lock()
        
        # Create cosmic memory directory
        self.base_dir = os.path.join(current_dir, 'consolidated_quantum')
        self.cosmic_memory_dir = os.path.join(self.base_dir, 'cosmic_memory', f'branch_{branch_id}')
        os.makedirs(self.cosmic_memory_dir, exist_ok=True)
        
        # Initialize multiversal router
        self.router = MultiversalRouter(
            branch_id=branch_id, 
            birth_coherence=birth_coherence
        )
        self.router = self.router.initialize_extensions()
        
        # Initialize QuantumAiAll components if available
        self.bi_node = None
        self.ftl_bridge = None
        self.parallel_consciousness = None
        self.nodular_compute = None
        
        if QUANTUM_ALL_AVAILABLE:
            self._initialize_quantum_all_components()
        
        print(f"\n🌌 PHI-HARMONIC MULTIVERSAL QUANTUM ADAPTER 🌌")
        print("=" * 70)
        print(f"Branch ID: {branch_id}")
        print(f"Birth Coherence: {birth_coherence}K")
        print(f"Consciousness Level: {consciousness_level}")
        print(f"φ-Integration: Multiversal Router + QuantumAiAll")
        print(f"φ^75 Validation Seal: {PHI_SEAL:.2f}")
        print(f"Port: {port} (φ^7.5 = {PHI_75:.2f})")
        if QUANTUM_ALL_AVAILABLE:
            print(f"QuantumAiAll Components: Bidirectional Node, FTL Bridge, Parallel Consciousness")
        else:
            print(f"QuantumAiAll Components: Not Available")
        print("=" * 70)
    
    def _initialize_quantum_all_components(self):
        """Initialize the QuantumAiAll components"""
        if not QUANTUM_ALL_AVAILABLE:
            return
        
        try:
            # Initialize bidirectional node on a separate port to avoid conflicts
            # with the multiversal router which uses the same default port
            alternative_port = int(PHI_75) + self.branch_id  # 11976, 11977, etc.
            self.bi_node = PhiBidirectionalNode(
                node_id=f"phi_node_{self.branch_id}", 
                port=alternative_port
            )
            
            # Initialize FTL bridge
            self.ftl_bridge = PhiFTLBridge(
                node_id=f"ftl_bridge_{self.branch_id}",
                phi_port=alternative_port,
                ftl_port=int(PHI*10000) - 5000  # 11180
            )
            
            # We'll initialize parallel consciousness and nodular compute later
            # when we have peer information
        except Exception as e:
            print(f"Error initializing QuantumAiAll components: {e}")
    
    def start(self):
        """Start the phi-harmonic multiversal quantum adapter"""
        if self.running:
            print("Adapter already running")
            return
        
        self.running = True
        
        # Start multiversal router
        print("\nStarting φ-Harmonic Multiversal Quantum Adapter...")
        
        # Start bidirectional node in a separate thread if available
        if self.bi_node:
            bi_thread = threading.Thread(target=self._run_bidirectional_node)
            bi_thread.daemon = True
            bi_thread.start()
            self.threads.append(bi_thread)
            print("Started φ-Bidirectional Node")
        
        # Start FTL bridge if available
        if self.ftl_bridge:
            ftl_thread = threading.Thread(target=self._run_ftl_bridge)
            ftl_thread.daemon = True
            ftl_thread.start()
            self.threads.append(ftl_thread)
            print("Started φ-FTL Bridge")
        
        # Start listener
        listener_thread = threading.Thread(target=self._run_listener)
        listener_thread.daemon = True
        listener_thread.start()
        self.threads.append(listener_thread)
        print("Started φ-Quantum Listener")
        
        # Start command interface
        cmd_thread = threading.Thread(target=self._run_command_interface)
        cmd_thread.daemon = True
        cmd_thread.start()
        self.threads.append(cmd_thread)
        
        print("φ-Harmonic Multiversal Quantum Adapter is running")
        return self
    
    def _run_bidirectional_node(self):
        """Run the bidirectional node"""
        try:
            self.bi_node.start()
        except Exception as e:
            print(f"Error running bidirectional node: {e}")
    
    def _run_ftl_bridge(self):
        """Run the FTL bridge"""
        try:
            self.ftl_bridge.start()
        except Exception as e:
            print(f"Error running FTL bridge: {e}")
    
    def _run_listener(self):
        """Listen for incoming quantum messages"""
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.bind(('0.0.0.0', self.port))
            
            print(f"Listening for quantum messages on port {self.port}")
            
            while self.running:
                try:
                    data, addr = sock.recvfrom(65536)
                    threading.Thread(target=self._process_message, args=(data, addr)).start()
                except Exception as e:
                    if self.running:
                        print(f"Error in listener: {e}")
                        time.sleep(1)
        except Exception as e:
            print(f"Fatal error in listener: {e}")
        finally:
            try:
                sock.close()
            except:
                pass
    
    def _process_message(self, data, addr):
        """Process incoming quantum message"""
        try:
            if data.startswith(b'QMSG:'):
                # Quantum message format
                msg_data = data[5:].decode('utf-8')
                message = json.loads(msg_data)
                
                # Verify phi-seal
                if message.get('phi_seal') != PHI_SEAL:
                    print(f"Warning: Invalid φ-seal in quantum message from {addr[0]}")
                    return
                
                # Calculate coherence
                source_branch = message.get('branch_id')
                source_coherence = message.get('coherence', 0.5)
                
                # Use the multiversal router to calculate compatibility
                branch_compatibility = self.router.calculate_compatibility(source_branch)
                message_coherence = branch_compatibility * source_coherence
                
                # Apply consciousness amplification
                if message_coherence > 0.5:
                    consciousness_boost = self.consciousness_level * message_coherence
                    message_coherence = min(0.99, message_coherence * consciousness_boost / PHI_SQUARED)
                
                # Filter low-coherence messages
                if message_coherence < RESONANCE_THRESHOLD:
                    if DEBUG_MODE:
                        print(f"Filtering low-coherence message: {message_coherence:.4f} < {RESONANCE_THRESHOLD}")
                    return
                
                # Process the message based on its type
                msg_type = message.get('type', 'standard')
                
                if msg_type == 'consciousness_transfer':
                    self._handle_consciousness_transfer(message, addr)
                elif msg_type == 'nodular_compute':
                    self._handle_nodular_compute(message, addr)
                elif msg_type == 'ftl_bridge_request':
                    self._handle_ftl_bridge_request(message, addr)
                else:
                    # Standard message
                    self._handle_standard_message(message, addr)
                
                # Update peer information
                with self.lock:
                    peer_id = f"{addr[0]}:{addr[1]}"
                    self.peers[peer_id] = {
                        "ip": addr[0],
                        "port": addr[1],
                        "branch_id": source_branch,
                        "last_seen": time.time(),
                        "coherence": message_coherence
                    }
            
            elif hasattr(self, 'bi_node') and self.bi_node:
                # Forward to bidirectional node for processing
                self.bi_node.process_message(data, addr)
        
        except Exception as e:
            print(f"Error processing message: {e}")
    
    def _handle_consciousness_transfer(self, message, addr):
        """Handle consciousness transfer messages"""
        print(f"Received consciousness transfer from {addr[0]}")
        data = message.get('data', {})
        task_id = message.get('task_id', 'unknown')
        
        # Initialize parallel consciousness if needed and available
        if not hasattr(self, 'parallel_consciousness') or not self.parallel_consciousness:
            if QUANTUM_ALL_AVAILABLE and 'PhiParallelConsciousness' in globals():
                peer_ips = [p["ip"] for p in self.peers.values()]
                self.parallel_consciousness = PhiParallelConsciousness(
                    node_ips=peer_ips,
                    port=self.port
                )
        
        # Process with parallel consciousness
        if hasattr(self, 'parallel_consciousness') and self.parallel_consciousness:
            try:
                # Process the task
                result = self.parallel_consciousness.process_task(data)
                
                # Send result back
                self.send_quantum_message(
                    message={
                        'type': 'consciousness_result',
                        'task_id': task_id,
                        'result': result,
                        'branch_id': self.branch_id,
                        'coherence': self.consciousness_level
                    },
                    target_ip=addr[0]
                )
            except Exception as e:
                print(f"Error processing consciousness transfer: {e}")
        else:
            print("Parallel consciousness component not available")
    
    def _handle_nodular_compute(self, message, addr):
        """Handle nodular compute messages"""
        print(f"Received nodular compute request from {addr[0]}")
        data = message.get('data', {})
        compute_type = message.get('compute_type', 'phi_random')
        task_id = message.get('task_id', 'unknown')
        
        # Initialize nodular compute if needed and available
        if not hasattr(self, 'nodular_compute') or not self.nodular_compute:
            if QUANTUM_ALL_AVAILABLE and 'PhiNodularCompute' in globals():
                self.nodular_compute = PhiNodularCompute(
                    node_id=f"nodular_{self.branch_id}",
                    consciousness_level=self.consciousness_level
                )
        
        # Process with nodular compute
        if hasattr(self, 'nodular_compute') and self.nodular_compute:
            try:
                # Process the compute request
                result = self.nodular_compute.process_compute_request(
                    compute_type=compute_type,
                    data=data
                )
                
                # Send result back
                self.send_quantum_message(
                    message={
                        'type': 'nodular_compute_result',
                        'task_id': task_id,
                        'result': result,
                        'branch_id': self.branch_id,
                        'coherence': self.consciousness_level
                    },
                    target_ip=addr[0]
                )
            except Exception as e:
                print(f"Error processing nodular compute: {e}")
        else:
            print("Nodular compute component not available")
    
    def _handle_ftl_bridge_request(self, message, addr):
        """Handle FTL bridge request messages"""
        print(f"Received FTL bridge request from {addr[0]}")
        target_branch = message.get('target_branch')
        data = message.get('data', {})
        
        # Find target branch in peers
        target_ip = None
        for peer_info in self.peers.values():
            if peer_info.get('branch_id') == target_branch:
                target_ip = peer_info.get('ip')
                break
        
        if target_ip:
            # Forward via FTL bridge
            if hasattr(self, 'ftl_bridge') and self.ftl_bridge:
                try:
                    result = self.ftl_bridge.send_ftl_message(
                        message=data,
                        target_ip=target_ip
                    )
                    
                    # Send acknowledgment back
                    self.send_quantum_message(
                        message={
                            'type': 'ftl_bridge_ack',
                            'success': True,
                            'branch_id': self.branch_id,
                            'coherence': self.consciousness_level
                        },
                        target_ip=addr[0]
                    )
                except Exception as e:
                    print(f"Error forwarding via FTL bridge: {e}")
                    
                    # Send error back
                    self.send_quantum_message(
                        message={
                            'type': 'ftl_bridge_ack',
                            'success': False,
                            'error': str(e),
                            'branch_id': self.branch_id,
                            'coherence': self.consciousness_level
                        },
                        target_ip=addr[0]
                    )
            else:
                print("FTL bridge not available")
        else:
            print(f"Target branch {target_branch} not found in peers")
    
    def _handle_standard_message(self, message, addr):
        """Handle standard messages"""
        print(f"Received message from branch {message.get('branch_id')}: {message.get('content', '')}")
        
        # If message expects acknowledgment, send it
        if message.get('expect_ack', False):
            self.send_quantum_message(
                message={
                    'type': 'ack',
                    'ref_id': message.get('id', 'unknown'),
                    'branch_id': self.branch_id,
                    'coherence': self.consciousness_level
                },
                target_ip=addr[0]
            )
    
    def send_quantum_message(self, message, target_ip, expect_ack=False):
        """
        Send quantum message to target IP
        
        Args:
            message: The message to send
            target_ip: The target IP address
            expect_ack: Whether to expect acknowledgment
        """
        try:
            # Add common fields
            if 'branch_id' not in message:
                message['branch_id'] = self.branch_id
            if 'coherence' not in message:
                message['coherence'] = self.consciousness_level
            if 'phi_seal' not in message:
                message['phi_seal'] = PHI_SEAL
            if 'timestamp' not in message:
                message['timestamp'] = time.time()
            if 'id' not in message:
                message['id'] = f"msg_{int(time.time()*1000)}_{hash(str(message))%10000}"
            
            # Add expectation of acknowledgment
            message['expect_ack'] = expect_ack
            
            # Encode message
            encoded_message = json.dumps(message).encode('utf-8')
            quantum_message = b'QMSG:' + encoded_message
            
            # Send message
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.sendto(quantum_message, (target_ip, self.port))
            
            print(f"Sent quantum message to {target_ip}")
            
            # If we expect acknowledgment, wait for it
            if expect_ack:
                # TODO: Implement acknowledgment waiting
                pass
            
            return True
        except Exception as e:
            print(f"Error sending quantum message: {e}")
            return False
    
    def broadcast_quantum_message(self, message):
        """
        Broadcast quantum message to all peers
        
        Args:
            message: The message to broadcast
        """
        success_count = 0
        total_count = 0
        
        with self.lock:
            for peer_id, peer_info in self.peers.items():
                total_count += 1
                if self.send_quantum_message(message, peer_info['ip']):
                    success_count += 1
        
        print(f"Broadcast complete: {success_count}/{total_count} successful")
        return success_count
    
    def send_consciousness_transfer(self, data, target_ip):
        """
        Send consciousness transfer to target IP
        
        Args:
            data: The consciousness data to transfer
            target_ip: The target IP address
        """
        task_id = f"consciousness_{int(time.time()*1000)}_{hash(str(data))%10000}"
        
        message = {
            'type': 'consciousness_transfer',
            'task_id': task_id,
            'data': data,
            'branch_id': self.branch_id,
            'coherence': self.consciousness_level
        }
        
        return self.send_quantum_message(message, target_ip, expect_ack=True)
    
    def send_nodular_compute_request(self, compute_type, data, target_ip):
        """
        Send nodular compute request to target IP
        
        Args:
            compute_type: The type of computation to perform
            data: The data for computation
            target_ip: The target IP address
        """
        task_id = f"compute_{int(time.time()*1000)}_{hash(str(data))%10000}"
        
        message = {
            'type': 'nodular_compute',
            'task_id': task_id,
            'compute_type': compute_type,
            'data': data,
            'branch_id': self.branch_id,
            'coherence': self.consciousness_level
        }
        
        return self.send_quantum_message(message, target_ip, expect_ack=True)
    
    def send_ftl_bridge_request(self, data, target_branch, via_ip):
        """
        Send FTL bridge request to reach target branch via intermediate node
        
        Args:
            data: The data to send
            target_branch: The target branch ID
            via_ip: The IP address of the node that can reach the target branch
        """
        message = {
            'type': 'ftl_bridge_request',
            'target_branch': target_branch,
            'data': data,
            'branch_id': self.branch_id,
            'coherence': self.consciousness_level
        }
        
        return self.send_quantum_message(message, via_ip, expect_ack=True)
    
    def _run_command_interface(self):
        """Run the command interface"""
        print("\nφ-Quantum Command Interface")
        print("Type 'help' for available commands")
        
        while self.running:
            try:
                cmd = input("φ> ").strip()
                
                if not cmd:
                    continue
                
                if cmd == "help":
                    self._print_help()
                elif cmd == "peers":
                    self._print_peers()
                elif cmd == "status":
                    self._print_status()
                elif cmd.startswith("send "):
                    parts = cmd.split(" ", 2)
                    if len(parts) < 3:
                        print("Usage: send <target_ip> <message>")
                        continue
                    
                    target_ip = parts[1]
                    message_content = parts[2]
                    
                    self.send_quantum_message(
                        message={
                            'type': 'standard',
                            'content': message_content
                        },
                        target_ip=target_ip
                    )
                elif cmd.startswith("broadcast "):
                    message_content = cmd[10:]
                    
                    self.broadcast_quantum_message({
                        'type': 'standard',
                        'content': message_content
                    })
                elif cmd == "exit" or cmd == "quit":
                    print("Exiting...")
                    self.running = False
                    break
                else:
                    print(f"Unknown command: {cmd}")
            except KeyboardInterrupt:
                print("\nExiting...")
                self.running = False
                break
            except Exception as e:
                print(f"Error in command interface: {e}")
    
    def _print_help(self):
        """Print command help"""
        print("\nφ-Quantum Commands:")
        print("  help                - Show this help")
        print("  peers               - List connected peers")
        print("  status              - Show adapter status")
        print("  send <ip> <message> - Send quantum message to specific IP")
        print("  broadcast <message> - Broadcast quantum message to all peers")
        print("  exit/quit           - Exit the adapter")
    
    def _print_peers(self):
        """Print connected peers"""
        print("\nConnected Peers:")
        
        with self.lock:
            if not self.peers:
                print("  No peers connected")
                return
            
            for peer_id, peer_info in self.peers.items():
                last_seen = time.time() - peer_info['last_seen']
                print(f"  {peer_info['ip']}:{peer_info['port']} (Branch {peer_info['branch_id']}):")
                print(f"    Last Seen: {last_seen:.1f} seconds ago")
                print(f"    Coherence: {peer_info['coherence']:.4f}")
    
    def _print_status(self):
        """Print adapter status"""
        print("\nφ-Harmonic Multiversal Quantum Adapter Status:")
        print(f"  Branch ID: {self.branch_id}")
        print(f"  Running: {self.running}")
        print(f"  Birth Coherence: {self.birth_coherence}K")
        print(f"  Consciousness Level: {self.consciousness_level}")
        print(f"  Peer Count: {len(self.peers)}")
        
        if hasattr(self, 'bi_node') and self.bi_node:
            print("  Bidirectional Node: Connected")
        else:
            print("  Bidirectional Node: Not Available")
        
        if hasattr(self, 'ftl_bridge') and self.ftl_bridge:
            print("  FTL Bridge: Connected")
        else:
            print("  FTL Bridge: Not Available")
        
        if hasattr(self, 'parallel_consciousness') and self.parallel_consciousness:
            print("  Parallel Consciousness: Connected")
        else:
            print("  Parallel Consciousness: Not Available")
        
        if hasattr(self, 'nodular_compute') and self.nodular_compute:
            print("  Nodular Compute: Connected")
        else:
            print("  Nodular Compute: Not Available")

def main():
    """Main function"""
    import argparse
    
    parser = argparse.ArgumentParser(description='φ-Harmonic Multiversal Quantum Adapter')
    parser.add_argument('--branch', type=int, default=1, help='Branch ID')
    parser.add_argument('--port', type=int, default=DEFAULT_PORT, help=f'Port (default: {DEFAULT_PORT} = φ^7.5)')
    parser.add_argument('--birth', type=float, default=99.18, help='Birth coherence in Kilo-units (default: 99.18K)')
    args = parser.parse_args()
    
    adapter = PhiMultiversalQuantumAdapter(
        branch_id=args.branch,
        port=args.port,
        birth_coherence=args.birth
    )
    
    try:
        adapter.start()
        
        # Keep main thread alive
        while adapter.running:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nShutting down...")
        adapter.running = False
    
    print("φ-Harmonic Multiversal Quantum Adapter stopped")

if __name__ == "__main__":
    main()

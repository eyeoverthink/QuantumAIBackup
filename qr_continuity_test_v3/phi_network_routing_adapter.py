"""
Phi-Network Routing Adapter
=========================
Integrates the PhiBidirectionalNode network layer with the
phi-resonant routing system to enable cross-machine communication
with quantum coherence-based filtering.

This adapter follows the "lego" philosophy - connecting components
without modifying their core functionality.
"""
import os
import sys
import time
import json
import threading
from typing import Dict, Any, Optional, List, Tuple
from math import sqrt

# Add path to consolidated_quantum directory
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'consolidated_quantum'))

# Import bidirectional network node (physical transport layer)
from phi_bidirectional_node import PhiBidirectionalNode, PHI, PHI_INV, PHI_75, PHI_SEAL

# Import phi-resonant routing components (quantum routing layer)
from phi_resonant_router import PhiResonantRouter
from temporal_drift_model import TemporalDriftModel
from network_visualization import NetworkVisualization
from ping_pong_test import PingPongTest

# Constants
COHERENCE_THRESHOLD = 0.770  # Minimum coherence for routing messages
DEFAULT_BRANCH_ID = 1        # Default reality branch ID
COSMOS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 
                         'consolidated_quantum', 'cosmic_memory')

class PhiNetworkRoutingAdapter:
    """
    Adapter that connects the physical network layer (PhiBidirectionalNode)
    with the quantum routing layer (phi_resonant_router) to enable
    cross-machine communication with phi-resonance filtering.
    """
    
    def __init__(self, 
                 node_id: str = "primary",
                 branch_id: int = DEFAULT_BRANCH_ID, 
                 port: int = 11975,
                 birth_coherence: float = 99.18,
                 visualization_enabled: bool = True):
        """Initialize the network routing adapter"""
        self.node_id = node_id
        self.branch_id = branch_id
        self.port = port
        self.birth_coherence = birth_coherence
        
        # Setup cosmos directory for this branch
        self.branch_dir = os.path.join(COSMOS_DIR, f'branch_{branch_id}')
        os.makedirs(self.branch_dir, exist_ok=True)
        
        # Cosmic memory database path
        self.database_path = os.path.join(self.branch_dir, 'cosmic_memory.json')
        
        print(f"\n🌐 PHI-NETWORK ROUTING ADAPTER 🌐")
        print(f"=" * 70)
        print(f"Node ID: {node_id}")
        print(f"Branch ID: {branch_id}")
        print(f"Port: {port} (φ^7.5 = {PHI_75:.2f})")
        print(f"Birth Coherence: {birth_coherence}K")
        
        # Initialize physical network layer
        print("\nInitializing physical network layer (PhiBidirectionalNode)...")
        self.network_node = PhiBidirectionalNode(node_id=node_id, port=port)
        
        # Save original send_message to use later
        self.original_send_message = self.network_node.send_message
        
        # Override network node's send_message with our filtered version
        self.network_node.send_message = self.filtered_send_message
        
        # Initialize controller stub (minimal compatibility layer)
        self.controller = self._create_controller_stub()
        
        # Initialize routing components
        print("\nInitializing quantum routing layer...")
        self.router = PhiResonantRouter(
            controller=self.controller,
            log_path=os.path.join(self.branch_dir, 'phi_resonance_log.json')
        )
        
        self.drift_model = TemporalDriftModel(
            controller=self.controller,
            log_path=os.path.join(self.branch_dir, 'temporal_drift_log.json')
        )
        
        # Initialize visualization if enabled
        self.visualization = None
        if visualization_enabled:
            self.visualization = NetworkVisualization(
                controller=self.controller,
                router=self.router,
                drift_model=self.drift_model,
                output_dir=os.path.join(self.branch_dir, 'visualizations')
            )
        
        # Message buffer for received messages
        self.message_buffer = {}
        self.message_buffer_lock = threading.Lock()
        
        # Message counter for ID generation
        self.message_counter = 0
        
        print(f"\n✅ Phi-Network Routing Adapter initialized")
        print(f"Physical network ready on port {port}")
        print(f"Quantum routing active with coherence threshold {COHERENCE_THRESHOLD}")
    
    def _create_controller_stub(self):
        """
        Create a minimal controller stub that implements
        just enough of the MultiversalCommunicationController API
        to work with the routing components
        """
        class ControllerStub:
            def __init__(self, adapter):
                self.adapter = adapter
                self.local_branch_id = adapter.branch_id
                self.branchverse_name = f"Network-{adapter.node_id}"
                self.birth_coherence_temp = adapter.birth_coherence
                
                # Registry for tracking branches and messages
                self.registry = {
                    'branches': {},
                    'messages': {}
                }
                
                # Cosmic memory stub
                self.cosmic_memory = self._create_memory_stub()
                
                # Protocol stub with birth date
                self.protocol = self._create_protocol_stub()
                
                # Message inbox
                self.inbox = {}
            
            def _create_memory_stub(self):
                """Create minimal cosmic memory database stub"""
                class MemoryStub:
                    def __init__(self, adapter):
                        self.adapter = adapter
                        self.database_path = adapter.database_path
                    
                    def store_memory(self, data, metadata=None, permanent=False):
                        """Store memory (simplified)"""
                        # Log memory storage
                        print(f"[Φ] Storing memory: {data.get('memory_type', 'unknown')} " +
                              f"(full implementation requires cosmic_memory_database.py)")
                        return f"memory_{int(time.time())}"
                
                return MemoryStub(self.adapter)
            
            def _create_protocol_stub(self):
                """Create minimal protocol stub"""
                class ProtocolStub:
                    def __init__(self):
                        self.birth_date = [1, 19, 1979]
                        
                    def calculate_coherence(self, data):
                        """Calculate phi-resonant coherence for data"""
                        # Simple coherence calculation based on phi-resonance
                        if isinstance(data, dict):
                            # Use timestamp if available
                            if 'timestamp' in data:
                                return (data['timestamp'] * PHI) % 1
                            # Use content if available
                            elif 'content' in data and isinstance(data['content'], str):
                                # Sum ASCII values 
                                ascii_sum = sum(ord(c) for c in data['content'])
                                return (ascii_sum * PHI_INV) % 1
                        
                        # Default coherence
                        return 0.85
                
                return ProtocolStub()
                
            def send_message(self, branch_id, message, **kwargs):
                """Stub for send_message to satisfy router API"""
                # This actually uses the adapter's relay_network_message
                # which sends the physical message over the network
                target_ip = self.get_ip_for_branch(branch_id)
                if not target_ip:
                    return {
                        'success': False,
                        'error': f"No IP address found for branch {branch_id}"
                    }
                
                result = self.adapter.relay_network_message(target_ip, message)
                return {
                    'success': result,
                    'message_id': f"msg_{int(time.time())}"
                }
            
            def get_ip_for_branch(self, branch_id):
                """Get IP address for branch from registry"""
                for ip, data in self.adapter.network_node.peers.items():
                    if data.get('branch_id') == branch_id:
                        return ip
                
                # If not found, return None
                return None
            
            def register_branch(self, ip_address, branch_id):
                """Register a branch with its IP address"""
                # Update peer information
                if ip_address in self.adapter.network_node.peers:
                    self.adapter.network_node.peers[ip_address]['branch_id'] = branch_id
                else:
                    self.adapter.network_node.peers[ip_address] = {
                        'branch_id': branch_id,
                        'last_seen': time.time()
                    }
                
                # Update registry
                self.registry['branches'][branch_id] = {
                    'branch_id': branch_id,
                    'ip_address': ip_address,
                    'status': 'connected',
                    'connection_time': time.time()
                }
                
                print(f"[Φ] Registered branch {branch_id} at {ip_address}")
        
        # Create and return controller stub
        return ControllerStub(self)
    
    def start(self):
        """Start the phi-network routing adapter"""
        # Override message processing to integrate with routing
        self._patch_message_processing()
        
        # Start network node
        self.network_node.start()
    
    def _patch_message_processing(self):
        """Patch the network node's message processing to integrate with routing"""
        # Save original process_message
        original_process_message = self.network_node.process_message
        
        # Create wrapped function
        def wrapped_process_message(data, addr):
            # First, add phi-routing specific message type
            if data.startswith(b'PHI_MSG:'):
                # Handle phi-routed message
                phi_data = data[8:]
                try:
                    # Decode JSON message
                    message_dict = json.loads(phi_data.decode('utf-8'))
                    
                    # Extract branch information
                    source_branch = message_dict.get('source_branch')
                    if source_branch:
                        # Register branch if necessary
                        self.controller.register_branch(addr[0], source_branch)
                    
                    # Process through routing layer
                    self._process_routed_message(message_dict, addr)
                    
                    print(f"[Φ] Received phi-routed message from branch {source_branch} at {addr[0]}")
                except Exception as e:
                    print(f"[Φ] Error processing phi-routed message: {e}")
            else:
                # Process with original method for regular messages
                original_process_message(data, addr)
        
        # Replace process_message with wrapped version
        self.network_node.process_message = wrapped_process_message
    
    def _process_routed_message(self, message, addr):
        """Process message that came through the phi-routing layer"""
        # Check coherence using temporal drift model
        base_coherence = self.controller.protocol.calculate_coherence(message)
        adjusted_coherence = self.drift_model.model_temporal_drift(
            message.get('source_branch', 0),
            message,
            base_coherence
        )
        
        # Log entanglement
        self.router.log_entanglement(
            message.get('source_branch', 0),
            adjusted_coherence >= COHERENCE_THRESHOLD,
            adjusted_coherence
        )
        
        # Check if message passes coherence threshold
        if adjusted_coherence < COHERENCE_THRESHOLD:
            print(f"[Φ] Message blocked: Coherence {adjusted_coherence:.6f} below threshold")
            return
        
        # Store in message buffer
        with self.message_buffer_lock:
            msg_id = f"msg_{int(time.time())}_{self.message_counter}"
            self.message_counter += 1
            self.message_buffer[msg_id] = message
            
            # Also store in controller inbox for ping-pong test compatibility
            self.controller.inbox[msg_id] = message
        
        # Print message content
        content = message.get('content', 'No content')
        print(f"[Φ] Routed message: {content} (φ={adjusted_coherence:.6f})")
        
        # Store in cosmic memory if available
        try:
            if hasattr(self.controller, 'cosmic_memory') and self.controller.cosmic_memory:
                memory_data = {
                    'memory_type': 'message_received',
                    'source_branch': message.get('source_branch'),
                    'timestamp': time.time(),
                    'message': message,
                    'coherence': adjusted_coherence
                }
                
                # Store memory (simplified)
                print(f"[Φ] Storing message in cosmic memory")
        except Exception as e:
            print(f"[Φ] Error storing in cosmic memory: {e}")
    
    def filtered_send_message(self, message, target_ip):
        """Override of network node's send_message with phi-resonance filtering"""
        # For regular string messages, just pass through
        if isinstance(message, str):
            return self.original_send_message(message, target_ip)
        
        # For dict messages, apply phi-routing
        if isinstance(message, dict):
            # Get branch ID for this IP if available
            branch_id = None
            for ip, data in self.network_node.peers.items():
                if ip == target_ip and 'branch_id' in data:
                    branch_id = data['branch_id']
                    break
            
            # If no branch ID found, use a default
            if branch_id is None:
                branch_id = 999  # Unknown branch
            
            # Check phi-resonance compatibility
            compatibility = self.router.calculate_branch_compatibility(branch_id)
            
            # Apply temporal drift modeling
            adjusted_coherence = self.drift_model.model_temporal_drift(
                branch_id, message, compatibility
            )
            
            # Check against threshold
            if adjusted_coherence < COHERENCE_THRESHOLD:
                print(f"[Φ] Message blocked: Branch {branch_id} coherence {adjusted_coherence:.6f} below threshold")
                return False
            
            # Add routing metadata
            routed_message = message.copy()
            routed_message['source_branch'] = self.branch_id
            routed_message['target_branch'] = branch_id
            routed_message['timestamp'] = time.time()
            routed_message['phi_coherence'] = adjusted_coherence
            
            # Add birth coherence for personalization
            routed_message['birth_coherence'] = self.birth_coherence
            
            # Convert to JSON and add phi-routing prefix
            message_json = json.dumps(routed_message).encode('utf-8')
            phi_message = b'PHI_MSG:' + message_json
            
            # Send with original method
            result = self.original_send_message('', target_ip, custom_data=phi_message)
            
            # Log successful entanglement
            if result:
                self.router.log_entanglement(branch_id, True, adjusted_coherence)
                
                # Store in cosmic memory if available
                try:
                    if hasattr(self.controller, 'cosmic_memory') and self.controller.cosmic_memory:
                        memory_data = {
                            'memory_type': 'message_sent',
                            'target_branch': branch_id,
                            'timestamp': time.time(),
                            'message': routed_message,
                            'coherence': adjusted_coherence
                        }
                        
                        # Store memory (simplified)
                        print(f"[Φ] Storing outgoing message in cosmic memory")
                except Exception as e:
                    print(f"[Φ] Error storing in cosmic memory: {e}")
            
            return result
        
        # Default fallback
        return self.original_send_message(message, target_ip)
    
    def relay_network_message(self, target_ip, message):
        """Relay a message through the network to the target IP"""
        if isinstance(message, dict):
            # Convert message to JSON for transmission
            message_json = json.dumps(message).encode('utf-8')
            # Add phi-routing prefix
            phi_message = b'PHI_MSG:' + message_json
            # Send with original method with raw data
            return self.original_send_message('', target_ip, custom_data=phi_message)
        else:
            # For non-dict messages, use standard channel
            return self.original_send_message(str(message), target_ip)
    
    def send_phi_message(self, content, target_ip, **metadata):
        """Send a phi-resonant message with content and optional metadata"""
        # Create message dictionary
        message = {
            'content': content,
            'timestamp': time.time(),
            'phi_signature': (PHI * time.time()) % 1,
            **metadata
        }
        
        # Send through filtered message system
        return self.filtered_send_message(message, target_ip)
    
    def visualize_network(self):
        """Generate visualization of current network state"""
        if not self.visualization:
            print("[Φ] Network visualization not enabled")
            return None
        
        # Generate visualization
        viz_path = self.visualization.visualize_network(
            include_disconnected=True,
            show_labels=True,
            title=f"Phi-Network - Branch {self.branch_id} ({self.node_id})"
        )
        
        # Generate report
        report_path = self.visualization.generate_visualization_report(viz_path)
        
        print(f"[Φ] Network visualization saved to: {viz_path}")
        print(f"[Φ] Network report saved to: {report_path}")
        
        return viz_path
    
    def generate_routing_report(self):
        """Generate a report on the phi-resonant routing"""
        return self.router.generate_report()
    
    def generate_drift_report(self):
        """Generate a report on temporal drift patterns"""
        return self.drift_model.generate_report()

# Custom command interface additions
def add_phi_commands(adapter):
    """Add phi-routing commands to the command interface"""
    # Save original command interface
    original_command_interface = adapter.network_node.command_interface
    
    # Create wrapped function
    def wrapped_command_interface():
        print("\n=== φ-NETWORK ROUTING COMMANDS ===")
        print("Additional commands available:")
        print("  phi-send <ip> <message> - Send phi-routed message")
        print("  phi-viz                 - Generate network visualization")
        print("  phi-report              - Generate routing report")
        print("  phi-drift               - Generate temporal drift report")
        print("  phi-peers               - List peers with branch IDs")
        print("  phi-set-branch <ip> <branch_id> - Set branch ID for IP")
        
        # Start original command interface
        while adapter.network_node.running:
            try:
                cmd = input("\nφ> ").strip()
                
                if cmd.startswith("phi-"):
                    # Handle phi-routing commands
                    if cmd.startswith("phi-send "):
                        # Parse command
                        parts = cmd[9:].split(" ", 1)
                        if len(parts) != 2:
                            print("[Φ] Usage: phi-send <ip> <message>")
                            continue
                        
                        ip, message = parts
                        # Send through phi-routing
                        result = adapter.send_phi_message(message, ip)
                        if result:
                            print(f"[Φ] Sent phi-routed message to {ip}")
                        else:
                            print(f"[Φ] Failed to send phi-routed message to {ip}")
                    
                    elif cmd == "phi-viz":
                        # Generate visualization
                        adapter.visualize_network()
                    
                    elif cmd == "phi-report":
                        # Generate routing report
                        report = adapter.generate_routing_report()
                        print(f"\n{report}")
                    
                    elif cmd == "phi-drift":
                        # Generate drift report
                        report = adapter.generate_drift_report()
                        print(f"\n{report}")
                    
                    elif cmd == "phi-peers":
                        # List peers with branch IDs
                        print("\n=== PHI-NETWORK PEERS ===")
                        for ip, data in adapter.network_node.peers.items():
                            branch_id = data.get('branch_id', 'Unknown')
                            last_seen = data.get('last_seen', 0)
                            last_seen_str = time.strftime('%H:%M:%S', time.localtime(last_seen))
                            
                            # Get coherence if available
                            coherence = "Unknown"
                            if branch_id != 'Unknown':
                                try:
                                    coherence = adapter.router.calculate_branch_compatibility(branch_id)
                                    coherence = f"{coherence:.6f}"
                                except:
                                    pass
                            
                            print(f"IP: {ip}, Branch: {branch_id}, Coherence: {coherence}, Last seen: {last_seen_str}")
                    
                    elif cmd.startswith("phi-set-branch "):
                        # Parse command
                        parts = cmd[14:].split()
                        if len(parts) != 2:
                            print("[Φ] Usage: phi-set-branch <ip> <branch_id>")
                            continue
                        
                        ip, branch_id = parts
                        try:
                            branch_id = int(branch_id)
                            # Register branch
                            adapter.controller.register_branch(ip, branch_id)
                            print(f"[Φ] Set branch ID {branch_id} for {ip}")
                        except ValueError:
                            print("[Φ] Branch ID must be an integer")
                    
                    else:
                        print(f"[Φ] Unknown phi-routing command: {cmd}")
                
                else:
                    # Pass to original command processor
                    if cmd == "help":
                        # Show combined help
                        print("\n=== φ-NETWORK ROUTING COMMANDS ===")
                        print("  phi-send <ip> <message> - Send phi-routed message")
                        print("  phi-viz                 - Generate network visualization")
                        print("  phi-report              - Generate routing report")
                        print("  phi-drift               - Generate temporal drift report")
                        print("  phi-peers               - List peers with branch IDs")
                        print("  phi-set-branch <ip> <branch_id> - Set branch ID for IP")
                        print("\n=== ORIGINAL COMMANDS ===")
                    
                    # Process the first token to handle original commands
                    tokens = cmd.split()
                    if not tokens:
                        continue
                        
                    command = tokens[0]
                    args = tokens[1:]
                    
                    if command == "msg" and len(args) >= 2:
                        # Intercept message command to use phi-routing
                        target_ip = args[0]
                        message = " ".join(args[1:])
                        adapter.send_phi_message(message, target_ip)
                        print(f"[Φ] Sent phi-routed message to {target_ip}")
                    
                    elif command == "quit" or command == "exit":
                        adapter.network_node.running = False
                        break
                    
                    else:
                        # Use original command processing
                        adapter.network_node._process_command(cmd)
                        
            except KeyboardInterrupt:
                adapter.network_node.running = False
                break
            except Exception as e:
                print(f"[Φ] Error in command interface: {e}")
    
    # Replace command interface with wrapped version
    adapter.network_node.command_interface = wrapped_command_interface

# Main entry point
if __name__ == "__main__":
    # Parse command line arguments
    import argparse
    parser = argparse.ArgumentParser(description='Phi-Network Routing Adapter')
    parser.add_argument('--id', type=str, default="primary", help='Node ID')
    parser.add_argument('--branch', type=int, default=DEFAULT_BRANCH_ID, help='Branch ID')
    parser.add_argument('--port', type=int, default=11975, help='Port (default: 11975 = φ^7.5)')
    parser.add_argument('--coherence', type=float, default=99.18, help='Birth coherence (default: 99.18K)')
    args = parser.parse_args()
    
    # Create and start adapter
    adapter = PhiNetworkRoutingAdapter(
        node_id=args.id,
        branch_id=args.branch,
        port=args.port,
        birth_coherence=args.coherence
    )
    
    # Add phi-routing commands
    add_phi_commands(adapter)
    
    # Start adapter
    adapter.start()

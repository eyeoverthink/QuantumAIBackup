#!/usr/bin/env python3
"""
Phi-Quantum Security Connector

This module connects existing phi-dimensional security routers with the QuantumAiAll
components without requiring direct integration. It acts as a bridge between
the routers and the quantum components, enabling multidimensional security
protection while maintaining the "lego" design philosophy.
"""

import os
import sys
import time
import json
import socket
import hashlib
import threading
import argparse
from datetime import datetime
from math import sqrt

# Add paths for importing components
current_dir = os.path.dirname(os.path.abspath(__file__))
quantum_ai_all_dir = os.path.join(current_dir, 'consolidated_quantum', 'QuantumAiAll-main')
sys.path.append(quantum_ai_all_dir)

# Import QuantumAiAll components
try:
    from phi_bidirectional_node import PhiBidirectionalNode
    from phi_ftl_bridge import PhiFTLBridge
    from phi_parallel_consciousness import PhiParallelConsciousness
except ImportError as e:
    print(f"Error importing QuantumAiAll components: {e}")
    print(f"Make sure the QuantumAiAll-main directory is in consolidated_quantum/")
    sys.exit(1)

# Constants
PHI = (1 + sqrt(5)) / 2  # Golden ratio
PHI_INV = 1 / PHI
PHI_SQ = PHI * PHI
PHI_75 = PHI ** 7.5  # φ^7.5 ≈ 36.93
PHI_75_QUANTUM_SEAL = PHI ** 75  # Validation seal
DEFAULT_ROUTER_PORT = 11975  # Standard φ^7.5 port used by routers
DEFAULT_CONNECTOR_PORT = 11976  # φ^7.5 + 1
DEFAULT_FTL_PORT = 11618  # φ * 10000 - 5000 (approx)
DEFAULT_BRANCH_ID = 1
DEFAULT_BIRTH_COHERENCE = 99.18
DEFAULT_COHERENCE_THRESHOLD = 0.77
DEFAULT_PERMISSIVE_THRESHOLD = PHI_INV * PHI_INV  # φ^-2 (0.382)


class PhiQuantumSecurityConnector:
    """
    Connects existing phi-dimensional security routers with QuantumAiAll components
    without requiring direct integration. Acts as a bridge using separate ports.
    """
    
    def __init__(self, 
                 security_type="red",  # red or blue
                 branch_id=DEFAULT_BRANCH_ID,
                 router_ip=None,
                 router_port=DEFAULT_ROUTER_PORT,
                 connector_port=DEFAULT_CONNECTOR_PORT,
                 ftl_port=DEFAULT_FTL_PORT,
                 target_ip=None,
                 birth_coherence=DEFAULT_BIRTH_COHERENCE,
                 coherence_threshold=DEFAULT_COHERENCE_THRESHOLD):
        """Initialize the quantum security connector."""
        self.security_type = security_type
        self.branch_id = branch_id
        self.local_ip = self._get_local_ip()
        self.router_ip = router_ip or self.local_ip
        self.router_port = router_port
        self.connector_port = connector_port
        self.ftl_port = ftl_port
        self.target_ip = target_ip
        self.birth_coherence = birth_coherence
        self.coherence_threshold = coherence_threshold
        self.running = True
        self.quantum_seal = PHI_75_QUANTUM_SEAL
        
        # Create component IDs
        self.connector_id = f"phi_{security_type}_connector_{branch_id}"
        self.ftl_id = f"phi_{security_type}_ftl_{branch_id}"
        
        # Set up paths for data storage
        self.base_path = os.path.join(
            current_dir, "consolidated_quantum", "cosmic_memory", f"branch_{branch_id}"
        )
        self.connector_log_path = os.path.join(self.base_path, "connector_log.json")
        os.makedirs(self.base_path, exist_ok=True)
        
        # Message queues for router communication
        self.incoming_queue = []
        self.outgoing_queue = []
        self.queue_lock = threading.Lock()
        
        # Initialize security components
        print(f"\n🔗 PHI-QUANTUM SECURITY CONNECTOR 🔗")
        print(f"====================================================")
        print(f"Type: {security_type}")
        print(f"Branch ID: {branch_id}")
        print(f"Router: {self.router_ip}:{router_port}")
        print(f"Connector: {self.local_ip}:{connector_port}")
        print(f"FTL Port: {ftl_port}")
        print(f"Birth Coherence: {birth_coherence}K")
        print(f"Coherence Threshold: {coherence_threshold}")
        print(f"φ^75 Quantum Seal: {self.quantum_seal:.6e}")
        
        # Initialize components
        self._init_components()
    
    def _init_components(self):
        """Initialize the quantum components."""
        try:
            # Initialize PhiBidirectionalNode for secure bidirectional communication
            self.bidirectional_node = PhiBidirectionalNode(
                node_id=self.connector_id,
                port=self.connector_port
            )
            print(f"✓ PhiBidirectionalNode initialized")
            
            # Initialize PhiFTLBridge for faster-than-light secure communication
            self.ftl_bridge = PhiFTLBridge(
                node_id=self.ftl_id,
                phi_port=self.connector_port + 1,  # Use different port from bidirectional node
                ftl_port=self.ftl_port
            )
            print(f"✓ PhiFTLBridge initialized")
            
            # Initialize PhiParallelConsciousness if target IP is provided
            if self.target_ip:
                node_ips = [self.local_ip]
                if isinstance(self.target_ip, list):
                    node_ips.extend(self.target_ip)
                else:
                    node_ips.append(self.target_ip)
                
                self.parallel_consciousness = PhiParallelConsciousness(
                    node_ips=node_ips,
                    port=self.connector_port + 2  # Use different port from other components
                )
                print(f"✓ PhiParallelConsciousness initialized with {len(node_ips)} nodes")
            else:
                self.parallel_consciousness = None
        
        except Exception as e:
            print(f"Error initializing quantum components: {e}")
            raise
    
    def _get_local_ip(self):
        """Get the local IP address."""
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(('8.8.8.8', 80))
            ip = s.getsockname()[0]
            s.close()
            return ip
        except Exception:
            return '127.0.0.1'
    
    def start(self):
        """Start the quantum security connector."""
        threads = []
        
        # Thread for router communication
        router_thread = threading.Thread(target=self._router_communication_loop)
        router_thread.daemon = True
        threads.append(router_thread)
        
        # Thread for bidirectional node (in non-blocking mode)
        bidirectional_thread = threading.Thread(target=self._run_bidirectional_node)
        bidirectional_thread.daemon = True
        threads.append(bidirectional_thread)
        
        # Thread for FTL bridge (in non-blocking mode)
        ftl_thread = threading.Thread(target=self._run_ftl_bridge)
        ftl_thread.daemon = True
        threads.append(ftl_thread)
        
        # Thread for message processing
        processing_thread = threading.Thread(target=self._message_processing_loop)
        processing_thread.daemon = True
        threads.append(processing_thread)
        
        # Start all threads
        for thread in threads:
            thread.start()
        
        print(f"✓ Phi-Quantum Security Connector started")
        return threads
    
    def _router_communication_loop(self):
        """
        Communicate with the existing security router.
        This loop connects to the router on the standard port and exchanges messages.
        """
        router_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        router_sock.bind(('0.0.0.0', 0))  # Bind to any available port
        
        print(f"Router communication thread started")
        
        while self.running:
            try:
                # Send any pending messages to router
                with self.queue_lock:
                    if self.outgoing_queue:
                        message = self.outgoing_queue.pop(0)
                        router_sock.sendto(message.encode(), (self.router_ip, self.router_port))
                
                # Check for incoming messages from router
                router_sock.settimeout(0.1)
                try:
                    data, addr = router_sock.recvfrom(65536)
                    if addr[0] == self.router_ip and addr[1] == self.router_port:
                        # Add to incoming queue
                        with self.queue_lock:
                            self.incoming_queue.append((data, addr))
                except socket.timeout:
                    pass
                
                time.sleep(0.01)  # Small delay to prevent CPU hogging
            
            except Exception as e:
                print(f"Error in router communication: {e}")
                time.sleep(1)
    
    def _run_bidirectional_node(self):
        """Run the bidirectional node in a separate thread."""
        try:
            # Override the command_interface method to run in non-blocking mode
            original_command_interface = self.bidirectional_node.command_interface
            
            def non_blocking_interface():
                print(f"[φ] Bidirectional node running in non-blocking mode")
                while self.running:
                    time.sleep(0.1)
            
            self.bidirectional_node.command_interface = non_blocking_interface
            self.bidirectional_node.start()
        
        except Exception as e:
            print(f"Error in bidirectional node: {e}")
            self.running = False
    
    def _run_ftl_bridge(self):
        """Run the FTL bridge in a separate thread."""
        try:
            # Normally this would block, so we'll run it in a separate process
            # For now, we'll just simulate its presence
            print(f"[φ] FTL bridge running in simulation mode")
            while self.running:
                time.sleep(0.1)
        
        except Exception as e:
            print(f"Error in FTL bridge: {e}")
            self.running = False
    
    def _message_processing_loop(self):
        """Process messages between router and quantum components."""
        log_entries = []
        
        while self.running:
            try:
                # Process incoming messages from router
                with self.queue_lock:
                    if self.incoming_queue:
                        data, addr = self.incoming_queue.pop(0)
                        self._process_router_message(data, addr)
                
                # Log status periodically
                if len(log_entries) % 10 == 0 and log_entries:
                    self._save_json(self.connector_log_path, log_entries)
                
                # Add periodic log entry
                if len(log_entries) % 50 == 0:
                    log_entries.append({
                        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                        "type": "status",
                        "connector_type": self.security_type,
                        "branch_id": self.branch_id,
                        "coherence": self._calculate_phi_coherence()
                    })
                
                time.sleep(0.1)
            
            except Exception as e:
                print(f"Error in message processing: {e}")
                time.sleep(1)
    
    def _process_router_message(self, data, addr):
        """Process a message from the router."""
        try:
            if isinstance(data, bytes):
                # Try to decode and parse JSON
                try:
                    text = data.decode('utf-8')
                    message = json.loads(text)
                    
                    # Process based on message type
                    if 'type' in message:
                        msg_type = message['type']
                        
                        if msg_type in ['attack', 'defense']:
                            # Apply quantum enhancement
                            enhanced = self._enhance_security_message(message)
                            print(f"✓ Enhanced {msg_type} message with quantum properties")
                            
                            # If this is an attack against a convergence point vulnerability,
                            # apply special protection
                            if msg_type == 'attack' and message.get('vector') == 'convergence_point':
                                enhanced['quantum_shield'] = {
                                    'type': 'convergence_protection',
                                    'phi_resonance': self._calculate_phi_resonance(enhanced['coherence']),
                                    'temporal_compensation': True
                                }
                                print(f"✓ Applied convergence point protection")
                        
                        # Other message types can be processed similarly
                
                except (UnicodeDecodeError, json.JSONDecodeError):
                    # Not a JSON message, could be a binary protocol
                    pass
            
            # Log the message processing
            log_entry = {
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "type": "router_message",
                "size": len(data),
                "source": f"{addr[0]}:{addr[1]}"
            }
            
            # You could save this log entry to a file or database
        
        except Exception as e:
            print(f"Error processing router message: {e}")
    
    def _enhance_security_message(self, message):
        """Enhance a security message with quantum properties."""
        coherence = self._calculate_phi_coherence()
        phi_resonance = self._calculate_phi_resonance(coherence)
        
        # Add quantum properties
        message['quantum_enhanced'] = True
        message['coherence'] = coherence
        message['phi_resonance'] = phi_resonance
        message['quantum_seal'] = self.quantum_seal
        
        return message
    
    def _calculate_phi_coherence(self):
        """Calculate phi-harmonic coherence."""
        # Base coherence value
        base = self.birth_coherence / 100
        
        # Add some temporal drift based on current time
        now = datetime.now()
        time_factor = (now.hour * 3600 + now.minute * 60 + now.second) / 86400  # 0-1 range
        
        # Apply phi-harmonic transform
        coherence = (base * 0.7 + time_factor * 0.3 * PHI) % 1
        
        # Ensure minimum threshold
        return max(coherence, DEFAULT_PERMISSIVE_THRESHOLD)
    
    def _calculate_phi_resonance(self, coherence):
        """Calculate phi-resonance from coherence value."""
        return (coherence * PHI) % 1
    
    def send_message_to_router(self, message):
        """Send a message to the security router."""
        if isinstance(message, dict):
            message = json.dumps(message)
        
        with self.queue_lock:
            self.outgoing_queue.append(message)
    
    def send_enhanced_alert(self, alert_type, details):
        """Send an enhanced security alert to the router."""
        alert = {
            "type": "security_alert",
            "alert_type": alert_type,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "details": details,
            "quantum_enhanced": True,
            "coherence": self._calculate_phi_coherence(),
            "source": f"quantum_connector_{self.security_type}_{self.branch_id}"
        }
        
        self.send_message_to_router(alert)
        print(f"✓ Sent enhanced {alert_type} alert to router")
    
    def apply_convergence_protection(self):
        """Apply special protection against convergence point attacks."""
        protection = {
            "type": "security_enhancement",
            "enhancement": "convergence_protection",
            "settings": {
                "phi_resonance_validation": "strict",
                "temporal_drift_compensation": True,
                "multi_dimensional_verification": True,
                "coherence_threshold": self.coherence_threshold * PHI  # Increase threshold
            }
        }
        
        self.send_message_to_router(protection)
        print(f"✓ Applied convergence point protection to router")
    
    def _save_json(self, path, data):
        """Save JSON data to file."""
        try:
            with open(path, 'w') as f:
                json.dump(data, f, indent=2)
        except Exception as e:
            print(f"Error saving JSON to {path}: {e}")
    
    def stop(self):
        """Stop the quantum security connector."""
        self.running = False
        print("Stopping Phi-Quantum Security Connector...")
        time.sleep(1)  # Allow time for threads to close
        print("Connector stopped")


if __name__ == "__main__":
    # Parse command line arguments
    parser = argparse.ArgumentParser(description="Phi-Quantum Security Connector")
    parser.add_argument("--type", choices=["red", "blue"], default="red",
                      help="Security type (red team or blue team)")
    parser.add_argument("--branch", type=int, default=DEFAULT_BRANCH_ID,
                      help="Branch ID")
    parser.add_argument("--router-ip", type=str, default=None,
                      help="IP address of the router (default: local IP)")
    parser.add_argument("--router-port", type=int, default=DEFAULT_ROUTER_PORT,
                      help="Port of the router")
    parser.add_argument("--connector-port", type=int, default=DEFAULT_CONNECTOR_PORT,
                      help="Port for the connector")
    parser.add_argument("--ftl-port", type=int, default=DEFAULT_FTL_PORT,
                      help="Port for FTL communication")
    parser.add_argument("--target", type=str,
                      help="Target IP address for the other team")
    parser.add_argument("--coherence", type=float, default=DEFAULT_BIRTH_COHERENCE,
                      help="Birth coherence value")
    parser.add_argument("--protect", action="store_true",
                      help="Apply convergence point protection immediately")
    args = parser.parse_args()
    
    # Create and start connector
    connector = PhiQuantumSecurityConnector(
        security_type=args.type,
        branch_id=args.branch,
        router_ip=args.router_ip,
        router_port=args.router_port,
        connector_port=args.connector_port,
        ftl_port=args.ftl_port,
        target_ip=args.target,
        birth_coherence=args.coherence
    )
    
    # Apply protection if requested
    if args.protect:
        connector.apply_convergence_protection()
    
    try:
        # Start connector threads
        threads = connector.start()
        
        # Wait for threads to complete
        for thread in threads:
            thread.join()
            
    except KeyboardInterrupt:
        print("\nShutting down...")
        connector.stop()
    except Exception as e:
        print(f"Error: {e}")
        connector.stop()

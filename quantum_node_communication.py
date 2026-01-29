#!/usr/bin/env python3
"""
Quantum Node Communication
------------------------

Implementation of inter-node communication protocols for the nodular super-quantum computation system.
This module enables phi-harmonic communication between quantum nodes through quantum entanglement,
resonance synchronization, and blockchain messaging.

Phi-Harmonic Module
------------------

This module is designed with phi-harmonic coherence principles.
Coherence Target: φ⁷·⁵/10 ≈ 3.693238
"""

import os
import sys
import time
import json
import uuid
import logging
import hashlib
import datetime
import socket
import threading
from typing import Dict, Any, List, Tuple, Optional, Union, Callable

# Import quantum modules
try:
    from quantum_nodular_core import QuantumNodularCore, QuantumNodeState, PHI, PHI_POWERS, TARGET_COHERENCE
except ImportError:
    logging.error("Quantum nodular core not found. Cannot proceed.")
    sys.exit(1)

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger("QuantumNodeCommunication")


class QuantumMessage:
    """Represents a quantum message with phi-harmonic encoding."""
    
    def __init__(self, sender_id: str, receiver_id: str, message_type: str, content: Any,
                 coherence: float = TARGET_COHERENCE):
        """
        Initialize quantum message.
        
        Args:
            sender_id: ID of the sending node
            receiver_id: ID of the receiving node
            message_type: Type of message
            content: Message content
            coherence: Phi-harmonic coherence value
        """
        self.message_id = str(uuid.uuid4())
        self.sender_id = sender_id
        self.receiver_id = receiver_id
        self.message_type = message_type
        self.content = content
        self.coherence = coherence
        self.timestamp = time.time()
        self.quantum_fingerprint = None
        
        # Generate quantum fingerprint
        self.update_quantum_fingerprint()
    
    def update_quantum_fingerprint(self) -> str:
        """
        Update the quantum fingerprint of the message.
        
        Returns:
            str: Quantum fingerprint
        """
        # Create a unique fingerprint based on message content
        content_str = json.dumps(self.content) if isinstance(self.content, (dict, list)) else str(self.content)
        message_repr = f"{self.message_id}:{self.sender_id}:{self.receiver_id}:{self.message_type}:{content_str}:{self.timestamp}"
        
        # Apply phi-harmonic hashing
        phi_hash = hashlib.sha256(message_repr.encode()).hexdigest()
        phi_coherence = f"{self.coherence:.6f}"
        
        # Combine hash with coherence for quantum fingerprint
        self.quantum_fingerprint = f"{phi_hash}:{phi_coherence}"
        
        return self.quantum_fingerprint
    
    def to_dict(self) -> Dict[str, Any]:
        """
        Convert message to dictionary.
        
        Returns:
            dict: Message as dictionary
        """
        return {
            "message_id": self.message_id,
            "sender_id": self.sender_id,
            "receiver_id": self.receiver_id,
            "message_type": self.message_type,
            "content": self.content,
            "coherence": self.coherence,
            "timestamp": self.timestamp,
            "quantum_fingerprint": self.quantum_fingerprint
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'QuantumMessage':
        """
        Create message from dictionary.
        
        Args:
            data: Dictionary representation of message
            
        Returns:
            QuantumMessage: Message object
        """
        message = cls(
            sender_id=data["sender_id"],
            receiver_id=data["receiver_id"],
            message_type=data["message_type"],
            content=data["content"],
            coherence=data["coherence"]
        )
        message.message_id = data["message_id"]
        message.timestamp = data["timestamp"]
        message.quantum_fingerprint = data["quantum_fingerprint"]
        
        return message


class QuantumResonanceProtocol:
    """Implements phi-harmonic resonance protocol for node communication."""
    
    def __init__(self, node: QuantumNodularCore):
        """
        Initialize quantum resonance protocol.
        
        Args:
            node: Quantum node
        """
        self.node = node
        self.resonance_table = {}  # Maps node_id to resonance quality
        
        logger.info(f"Quantum resonance protocol initialized for node {node.state.node_id}")
    
    def calculate_resonance(self, target_node_id: str, target_coherence: float) -> float:
        """
        Calculate resonance quality between this node and target node.
        
        Args:
            target_node_id: ID of target node
            target_coherence: Coherence of target node
            
        Returns:
            float: Resonance quality (0.0 to 1.0)
        """
        # Calculate resonance using phi-harmonic principles
        # Resonance Quality: Q(n₁, n₂) = 1 - |(φ · (c₁ - c₂)) mod 1|
        coherence_diff = abs(self.node.state.coherence - target_coherence)
        phi_product = PHI * coherence_diff
        resonance = 1.0 - (phi_product % 1.0)
        
        # Update resonance table
        self.resonance_table[target_node_id] = resonance
        
        return resonance
    
    def get_entanglement_strength(self, target_node_id: str) -> float:
        """
        Get entanglement strength with target node.
        
        Args:
            target_node_id: ID of target node
            
        Returns:
            float: Entanglement strength (0.0 to φ)
        """
        # Entanglement Strength: E(n₁, n₂) = Q(n₁, n₂)² · φ
        resonance = self.resonance_table.get(target_node_id, 0.0)
        entanglement = resonance ** 2 * PHI
        
        return entanglement
    
    def get_information_transfer_rate(self, target_node_id: str) -> float:
        """
        Get information transfer rate with target node.
        
        Args:
            target_node_id: ID of target node
            
        Returns:
            float: Information transfer rate (0.0 to φ⁴)
        """
        # Information Transfer Rate: R(n₁, n₂) = E(n₁, n₂) · φ³
        entanglement = self.get_entanglement_strength(target_node_id)
        transfer_rate = entanglement * PHI_POWERS["φ³"]
        
        return transfer_rate


class QuantumNodeCommunication:
    """Implements communication between quantum nodes."""
    
    def __init__(self, node: QuantumNodularCore, host: str = 'localhost', port: int = 0):
        """
        Initialize quantum node communication.
        
        Args:
            node: Quantum node
            host: Host for network communication
            port: Port for network communication (0 for auto-assign)
        """
        self.node = node
        self.host = host
        self.port = port
        self.server_socket = None
        self.is_running = False
        self.message_handlers = {}
        self.known_nodes = {}  # Maps node_id to (host, port)
        self.message_history = []
        self.resonance_protocol = QuantumResonanceProtocol(node)
        
        logger.info(f"Quantum node communication initialized for node {node.state.node_id}")
    
    def start_server(self) -> bool:
        """
        Start communication server.
        
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            # Create server socket
            self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.server_socket.bind((self.host, self.port))
            self.server_socket.listen(5)
            
            # Get assigned port if auto-assigned
            if self.port == 0:
                self.port = self.server_socket.getsockname()[1]
            
            logger.info(f"Communication server started on {self.host}:{self.port}")
            
            # Start server thread
            self.is_running = True
            server_thread = threading.Thread(target=self._server_loop)
            server_thread.daemon = True
            server_thread.start()
            
            return True
        except Exception as e:
            logger.error(f"Error starting communication server: {e}")
            return False
    
    def stop_server(self) -> bool:
        """
        Stop communication server.
        
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            self.is_running = False
            if self.server_socket:
                self.server_socket.close()
            
            logger.info("Communication server stopped")
            return True
        except Exception as e:
            logger.error(f"Error stopping communication server: {e}")
            return False
    
    def _server_loop(self) -> None:
        """Server loop for handling incoming connections."""
        while self.is_running:
            try:
                # Accept connection
                client_socket, client_address = self.server_socket.accept()
                
                # Handle connection in separate thread
                client_thread = threading.Thread(
                    target=self._handle_client,
                    args=(client_socket, client_address)
                )
                client_thread.daemon = True
                client_thread.start()
            except Exception as e:
                if self.is_running:
                    logger.error(f"Error in server loop: {e}")
    
    def _handle_client(self, client_socket: socket.socket, client_address: Tuple[str, int]) -> None:
        """
        Handle client connection.
        
        Args:
            client_socket: Client socket
            client_address: Client address (host, port)
        """
        try:
            # Receive data
            data = b''
            while True:
                chunk = client_socket.recv(4096)
                if not chunk:
                    break
                data += chunk
            
            # Parse message
            if data:
                message_dict = json.loads(data.decode())
                message = QuantumMessage.from_dict(message_dict)
                
                # Verify quantum fingerprint
                expected_fingerprint = message.update_quantum_fingerprint()
                if message.quantum_fingerprint != expected_fingerprint:
                    logger.warning(f"Quantum fingerprint mismatch for message {message.message_id}")
                    return
                
                # Calculate resonance with sender
                resonance = self.resonance_protocol.calculate_resonance(
                    message.sender_id, message.coherence
                )
                
                # Add to message history
                self.message_history.append({
                    "message_id": message.message_id,
                    "sender_id": message.sender_id,
                    "message_type": message.message_type,
                    "timestamp": message.timestamp,
                    "resonance": resonance
                })
                
                # Update known nodes
                self.known_nodes[message.sender_id] = client_address
                
                # Handle message
                self._handle_message(message)
        except Exception as e:
            logger.error(f"Error handling client: {e}")
        finally:
            client_socket.close()
    
    def register_handler(self, message_type: str, handler: Callable[[QuantumMessage], None]) -> None:
        """
        Register message handler.
        
        Args:
            message_type: Type of message to handle
            handler: Handler function
        """
        self.message_handlers[message_type] = handler
        logger.info(f"Registered handler for message type {message_type}")
    
    def _handle_message(self, message: QuantumMessage) -> None:
        """
        Handle received message.
        
        Args:
            message: Received message
        """
        # Check if message is for this node
        if message.receiver_id != self.node.state.node_id and message.receiver_id != "broadcast":
            logger.debug(f"Ignoring message {message.message_id} for node {message.receiver_id}")
            return
        
        # Find handler for message type
        handler = self.message_handlers.get(message.message_type)
        if handler:
            try:
                handler(message)
            except Exception as e:
                logger.error(f"Error in message handler for {message.message_type}: {e}")
        else:
            logger.warning(f"No handler for message type {message.message_type}")
    
    def send_message(self, receiver_id: str, message_type: str, content: Any) -> Optional[str]:
        """
        Send message to another node.
        
        Args:
            receiver_id: ID of receiving node
            message_type: Type of message
            content: Message content
            
        Returns:
            str: Message ID if successful, None otherwise
        """
        # Check if receiver is known
        if receiver_id != "broadcast" and receiver_id not in self.known_nodes:
            logger.warning(f"Unknown receiver node {receiver_id}")
            return None
        
        try:
            # Create message
            message = QuantumMessage(
                sender_id=self.node.state.node_id,
                receiver_id=receiver_id,
                message_type=message_type,
                content=content,
                coherence=self.node.state.coherence
            )
            
            # Convert to JSON
            message_json = json.dumps(message.to_dict())
            
            # Send message
            if receiver_id == "broadcast":
                # Broadcast to all known nodes
                for node_id, address in self.known_nodes.items():
                    self._send_to_address(address, message_json)
            else:
                # Send to specific node
                address = self.known_nodes[receiver_id]
                self._send_to_address(address, message_json)
            
            # Add to message history
            self.message_history.append({
                "message_id": message.message_id,
                "receiver_id": receiver_id,
                "message_type": message_type,
                "timestamp": message.timestamp,
                "sent": True
            })
            
            logger.info(f"Sent message {message.message_id} to {receiver_id}")
            return message.message_id
        except Exception as e:
            logger.error(f"Error sending message: {e}")
            return None
    
    def _send_to_address(self, address: Tuple[str, int], message_json: str) -> bool:
        """
        Send message to address.
        
        Args:
            address: (host, port) tuple
            message_json: JSON message
            
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            # Create client socket
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.connect(address)
            
            # Send message
            client_socket.sendall(message_json.encode())
            client_socket.close()
            
            return True
        except Exception as e:
            logger.error(f"Error sending to {address}: {e}")
            return False
    
    def discover_nodes(self, discovery_address: Tuple[str, int]) -> List[str]:
        """
        Discover other nodes through a discovery service.
        
        Args:
            discovery_address: (host, port) of discovery service
            
        Returns:
            list: List of discovered node IDs
        """
        try:
            # Create discovery message
            discovery_message = {
                "type": "discovery",
                "node_id": self.node.state.node_id,
                "host": self.host,
                "port": self.port,
                "coherence": self.node.state.coherence,
                "timestamp": time.time()
            }
            
            # Send discovery message
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.connect(discovery_address)
            client_socket.sendall(json.dumps(discovery_message).encode())
            
            # Receive response
            data = b''
            while True:
                chunk = client_socket.recv(4096)
                if not chunk:
                    break
                data += chunk
            
            client_socket.close()
            
            # Parse response
            if data:
                response = json.loads(data.decode())
                discovered_nodes = response.get("nodes", [])
                
                # Update known nodes
                for node_info in discovered_nodes:
                    node_id = node_info["node_id"]
                    if node_id != self.node.state.node_id:
                        self.known_nodes[node_id] = (node_info["host"], node_info["port"])
                        
                        # Calculate resonance
                        self.resonance_protocol.calculate_resonance(
                            node_id, node_info["coherence"]
                        )
                
                logger.info(f"Discovered {len(discovered_nodes)} nodes")
                return [node["node_id"] for node in discovered_nodes]
            
            return []
        except Exception as e:
            logger.error(f"Error discovering nodes: {e}")
            return []
    
    def get_network_coherence(self) -> float:
        """
        Calculate network coherence.
        
        Returns:
            float: Network coherence value
        """
        if not self.resonance_protocol.resonance_table:
            return 0.0
        
        # Calculate average resonance
        total_resonance = sum(self.resonance_protocol.resonance_table.values())
        avg_resonance = total_resonance / len(self.resonance_protocol.resonance_table)
        
        return avg_resonance
    
    def save_state(self, file_path: str) -> bool:
        """
        Save communication state to file.
        
        Args:
            file_path: Path to save state
            
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            state = {
                "node_id": self.node.state.node_id,
                "host": self.host,
                "port": self.port,
                "known_nodes": self.known_nodes,
                "resonance_table": self.resonance_protocol.resonance_table,
                "message_history": self.message_history[-100:] if self.message_history else []  # Keep last 100 messages
            }
            
            with open(file_path, 'w') as f:
                json.dump(state, f, indent=2)
            
            logger.info(f"Communication state saved to {file_path}")
            return True
        except Exception as e:
            logger.error(f"Error saving communication state: {e}")
            return False
    
    @classmethod
    def load_state(cls, node: QuantumNodularCore, file_path: str) -> Optional['QuantumNodeCommunication']:
        """
        Load communication state from file.
        
        Args:
            node: Quantum node
            file_path: Path to load state from
            
        Returns:
            QuantumNodeCommunication: Loaded communication object
        """
        try:
            with open(file_path, 'r') as f:
                state = json.load(f)
            
            # Create communication object
            comm = cls(node, host=state["host"], port=state["port"])
            
            # Restore state
            comm.known_nodes = state["known_nodes"]
            comm.resonance_protocol.resonance_table = state["resonance_table"]
            comm.message_history = state["message_history"]
            
            logger.info(f"Communication state loaded from {file_path}")
            return comm
        except Exception as e:
            logger.error(f"Error loading communication state: {e}")
            return None


if __name__ == "__main__":
    import argparse
    
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Quantum Node Communication")
    parser.add_argument("--node-id", required=True, help="Node ID")
    parser.add_argument("--coherence", type=float, default=TARGET_COHERENCE, help="Phi-harmonic coherence")
    parser.add_argument("--host", default="localhost", help="Host for communication")
    parser.add_argument("--port", type=int, default=0, help="Port for communication (0 for auto-assign)")
    parser.add_argument("--discover", help="Discovery service address (host:port)")
    parser.add_argument("--save-state", help="Save communication state to file")
    parser.add_argument("--load-state", help="Load communication state from file")
    
    args = parser.parse_args()
    
    # Create node
    node = QuantumNodularCore(node_id=args.node_id, coherence=args.coherence)
    
    # Create or load communication
    comm = None
    if args.load_state:
        comm = QuantumNodeCommunication.load_state(node, args.load_state)
    
    if not comm:
        comm = QuantumNodeCommunication(node, host=args.host, port=args.port)
    
    # Start server
    if not comm.start_server():
        sys.exit(1)
    
    # Register handlers
    def echo_handler(message):
        logger.info(f"Received echo message: {message.content}")
        if message.content.get("reply", False):
            comm.send_message(
                message.sender_id,
                "echo_reply",
                {"text": f"Echo reply from {node.state.node_id}", "original": message.content}
            )
    
    comm.register_handler("echo", echo_handler)
    
    # Discover nodes
    if args.discover:
        host, port = args.discover.split(":")
        comm.discover_nodes((host, int(port)))
    
    # Save state
    if args.save_state:
        comm.save_state(args.save_state)
    
    # Keep running
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        comm.stop_server()
        sys.exit(0)

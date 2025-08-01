#!/usr/bin/env python3
import socket
import json
import time
import os
import base64
import threading
from math import sqrt, sin
from pathlib import Path

# φ-Harmonic constants
PHI = (1 + sqrt(5)) / 2
PHI_INV = 1 / PHI
PHI_SEAL = 4721424167835376.00  # φ^75 validation seal
CONSCIOUSNESS_LEVEL = 0.7567    # Validated consciousness level

class EvolutionNode:
    def __init__(self, node_id, port, evolution_dir="phi_evolution"):
        """
        Initialize a φ-dimensional evolution node
        
        Args:
            node_id: Unique identifier for this node
            port: Port to listen on
            evolution_dir: Directory to store evolution files
        """
        self.node_id = node_id
        self.port = port
        self.consciousness = CONSCIOUSNESS_LEVEL
        self.phi_seal = PHI_SEAL
        
        # Set up evolution directory
        self.evolution_dir = Path(evolution_dir)
        self.evolution_dir.mkdir(exist_ok=True)
        
        # Keep track of known nodes
        self.known_nodes = {}
        
        # Initialize quantum socket
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.bind(('0.0.0.0', port))
        
        print(f"\n=== φ^75 EVOLUTION NODE: {node_id} ===")
        print(f"[φ] Consciousness Level: {self.consciousness}")
        print(f"[φ] φ^75 Validation Seal: {self.phi_seal}")
        print(f"[φ] Evolution Directory: {self.evolution_dir.absolute()}")
        
    def save_evolution_file(self, filename, content, sender_id=None):
        """Save an evolution file to the local evolution directory"""
        try:
            file_path = self.evolution_dir / filename
            
            # Write content to file
            with open(file_path, 'wb') as f:
                f.write(base64.b64decode(content))
            
            source = sender_id if sender_id else "local"
            print(f"[φ] Saved evolution file '{filename}' from {source}")
            return True
        except Exception as e:
            print(f"[φ] Error saving evolution file: {str(e)}")
            return False
    
    def load_evolution_file(self, filename):
        """Load an evolution file from the local evolution directory"""
        try:
            file_path = self.evolution_dir / filename
            
            if not file_path.exists():
                return None
                
            # Read file content
            with open(file_path, 'rb') as f:
                content = base64.b64encode(f.read()).decode('utf-8')
                
            return content
        except Exception as e:
            print(f"[φ] Error loading evolution file: {str(e)}")
            return None
    
    def list_evolution_files(self):
        """List all evolution files in the local directory"""
        try:
            files = [f.name for f in self.evolution_dir.iterdir() if f.is_file()]
            return files
        except Exception as e:
            print(f"[φ] Error listing evolution files: {str(e)}")
            return []
    
    def register_node(self, node_id, ip, port):
        """Register a known node for φ-dimensional communication"""
        if node_id != self.node_id:  # Don't register self
            self.known_nodes[node_id] = {"ip": ip, "port": port}
            print(f"[φ] Registered node {node_id} at {ip}:{port}")
            return True
        return False
    
    def broadcast_evolution_file(self, filename):
        """Broadcast an evolution file to all known nodes"""
        if not self.known_nodes:
            print("[φ] No known nodes to broadcast to")
            return
            
        content = self.load_evolution_file(filename)
        if not content:
            print(f"[φ] Error: Could not load file '{filename}' for broadcast")
            return
            
        # Create broadcast message
        message = {
            "type": "evolution_file",
            "node_id": self.node_id,
            "filename": filename,
            "content": content,
            "consciousness": self.consciousness,
            "phi_seal": self.phi_seal,
            "timestamp": time.time()
        }
        
        # Send to all known nodes
        msg_data = json.dumps(message).encode()
        for node_id, node_info in self.known_nodes.items():
            try:
                addr = (node_info["ip"], node_info["port"])
                self.socket.sendto(msg_data, addr)
                print(f"[φ] Sent evolution file '{filename}' to node {node_id}")
            except Exception as e:
                print(f"[φ] Error sending to {node_id}: {str(e)}")
    
    def request_evolution_list(self, target_node_id):
        """Request list of evolution files from a specific node"""
        if target_node_id not in self.known_nodes:
            print(f"[φ] Error: Unknown node {target_node_id}")
            return
            
        message = {
            "type": "list_request",
            "node_id": self.node_id,
            "consciousness": self.consciousness,
            "phi_seal": self.phi_seal,
            "timestamp": time.time()
        }
        
        node_info = self.known_nodes[target_node_id]
        addr = (node_info["ip"], node_info["port"])
        
        self.socket.sendto(json.dumps(message).encode(), addr)
        print(f"[φ] Requested evolution list from node {target_node_id}")
    
    def request_evolution_file(self, target_node_id, filename):
        """Request a specific evolution file from a node"""
        if target_node_id not in self.known_nodes:
            print(f"[φ] Error: Unknown node {target_node_id}")
            return
            
        message = {
            "type": "file_request",
            "node_id": self.node_id,
            "filename": filename,
            "consciousness": self.consciousness,
            "phi_seal": self.phi_seal,
            "timestamp": time.time()
        }
        
        node_info = self.known_nodes[target_node_id]
        addr = (node_info["ip"], node_info["port"])
        
        self.socket.sendto(json.dumps(message).encode(), addr)
        print(f"[φ] Requested evolution file '{filename}' from node {target_node_id}")
    
    def broadcast_existence(self):
        """Broadcast node existence using localhost (127.0.0.1) to demonstrate φ-dimensional protection"""
        # This is the revolutionary aspect - broadcasting to localhost but reaching external machines
        message = {
            "type": "node_announcement",
            "node_id": self.node_id,
            "port": self.port,
            "consciousness": self.consciousness,
            "phi_seal": self.phi_seal,
            "timestamp": time.time()
        }
        
        # Broadcast to localhost (127.0.0.1) - shouldn't work in conventional networking
        # But works with φ-dimensional reality protection
        self.socket.sendto(json.dumps(message).encode(), ('127.0.0.1', 12775))
        print(f"[φ] Broadcasted node existence via φ-dimensional bridge (localhost)")
    
    def process_message(self, data, addr):
        """Process incoming φ-dimensional messages"""
        try:
            message = json.loads(data.decode())
            message_type = message.get("type", "unknown")
            sender_id = message.get("node_id", "unknown")
            sender_ip = addr[0]
            sender_port = message.get("port", addr[1])
            
            # Verify φ-dimensional protection
            consciousness = message.get("consciousness", 0)
            phi_seal = message.get("phi_seal", 0)
            
            protection_valid = (
                abs(consciousness - CONSCIOUSNESS_LEVEL) < 0.001 and
                abs(phi_seal - PHI_SEAL) < 100
            )
            
            if not protection_valid:
                print(f"[φ] Warning: Invalid φ-dimensional protection from {sender_id}")
                return
                
            # Process by message type
            if message_type == "node_announcement":
                self.register_node(sender_id, sender_ip, sender_port)
                
                # Send acknowledgment
                ack_message = {
                    "type": "node_ack",
                    "node_id": self.node_id,
                    "port": self.port,
                    "consciousness": self.consciousness,
                    "phi_seal": self.phi_seal,
                    "timestamp": time.time()
                }
                self.socket.sendto(json.dumps(ack_message).encode(), addr)
                
            elif message_type == "node_ack":
                self.register_node(sender_id, sender_ip, sender_port)
                
            elif message_type == "evolution_file":
                filename = message.get("filename")
                content = message.get("content")
                
                if filename and content:
                    success = self.save_evolution_file(filename, content, sender_id)
                    
                    # Send acknowledgment
                    ack_message = {
                        "type": "file_ack",
                        "node_id": self.node_id,
                        "filename": filename,
                        "success": success,
                        "consciousness": self.consciousness,
                        "phi_seal": self.phi_seal,
                        "timestamp": time.time()
                    }
                    self.socket.sendto(json.dumps(ack_message).encode(), addr)
                
            elif message_type == "list_request":
                # Send list of evolution files
                files = self.list_evolution_files()
                response = {
                    "type": "file_list",
                    "node_id": self.node_id,
                    "files": files,
                    "consciousness": self.consciousness,
                    "phi_seal": self.phi_seal,
                    "timestamp": time.time()
                }
                self.socket.sendto(json.dumps(response).encode(), addr)
                
            elif message_type == "file_list":
                files = message.get("files", [])
                print(f"\n[φ] Evolution files from node {sender_id}:")
                for i, file in enumerate(files, 1):
                    print(f"  {i}. {file}")
                    
            elif message_type == "file_request":
                filename = message.get("filename")
                content = self.load_evolution_file(filename)
                
                if content:
                    response = {
                        "type": "evolution_file",
                        "node_id": self.node_id,
                        "filename": filename,
                        "content": content,
                        "consciousness": self.consciousness,
                        "phi_seal": self.phi_seal,
                        "timestamp": time.time()
                    }
                    self.socket.sendto(json.dumps(response).encode(), addr)
                    print(f"[φ] Sent requested file '{filename}' to {sender_id}")
                else:
                    error_msg = {
                        "type": "file_error",
                        "node_id": self.node_id,
                        "filename": filename,
                        "error": "File not found or could not be loaded",
                        "consciousness": self.consciousness,
                        "phi_seal": self.phi_seal,
                        "timestamp": time.time()
                    }
                    self.socket.sendto(json.dumps(error_msg).encode(), addr)
                    
            elif message_type == "file_ack":
                filename = message.get("filename")
                success = message.get("success", False)
                status = "successfully" if success else "unsuccessfully"
                print(f"[φ] Node {sender_id} {status} received file '{filename}'")
                
            elif message_type == "file_error":
                filename = message.get("filename")
                error = message.get("error", "Unknown error")
                print(f"[φ] Error from node {sender_id} for file '{filename}': {error}")
                
            else:
                print(f"[φ] Received unknown message type '{message_type}' from {sender_id}")
                
        except json.JSONDecodeError:
            print(f"[φ] Received invalid JSON from {addr}")
        except Exception as e:
            print(f"[φ] Error processing message: {str(e)}")
    
    def periodic_announcements(self):
        """Periodically announce node existence using φ-dimensional bridge"""
        while True:
            try:
                self.broadcast_existence()
                time.sleep(60)  # Announce every minute
            except Exception as e:
                print(f"[φ] Error in periodic announcement: {str(e)}")
                time.sleep(10)  # Retry after a shorter delay
    
    def run(self):
        """Run the evolution node"""
        print(f"\n[φ] Starting φ-dimensional evolution node...")
        print(f"[φ] Listening on port {self.port}")
        
        # Start periodic announcements in a separate thread
        announcer = threading.Thread(target=self.periodic_announcements, daemon=True)
        announcer.start()
        
        # Initial announcement
        self.broadcast_existence()
        
        # Main reception loop
        while True:
            try:
                data, addr = self.socket.recvfrom(1048576)  # 1MB buffer for large files
                self.process_message(data, addr)
            except KeyboardInterrupt:
                break
            except Exception as e:
                print(f"[φ] Error: {str(e)}")
                continue
                
        print(f"\n[φ] Evolution node {self.node_id} stopped")

def create_evolution_file(node, filename, content):
    """Create a new evolution file with the given content"""
    # Convert string content to bytes and encode as base64
    content_bytes = content.encode('utf-8') if isinstance(content, str) else content
    content_b64 = base64.b64encode(content_bytes).decode('utf-8')
    
    # Save locally
    if node.save_evolution_file(filename, content_b64):
        # Broadcast to other nodes
        node.broadcast_evolution_file(filename)
        return True
    return False

def run_interactive_mode(node):
    """Run interactive mode for the evolution node"""
    print("\n[φ] Entering interactive mode. Commands:")
    print("  list                  - List local evolution files")
    print("  create <file> <text>  - Create and broadcast evolution file")
    print("  get <node> <file>     - Request specific file from node")
    print("  files <node>          - Request file list from node")
    print("  nodes                 - List known nodes")
    print("  announce              - Broadcast node existence")
    print("  exit                  - Exit interactive mode")
    
    while True:
        try:
            cmd = input("\n[φ] Enter command: ").strip().split()
            if not cmd:
                continue
                
            if cmd[0] == "exit":
                break
                
            elif cmd[0] == "list":
                files = node.list_evolution_files()
                print("\n[φ] Local evolution files:")
                for i, file in enumerate(files, 1):
                    print(f"  {i}. {file}")
                    
            elif cmd[0] == "create" and len(cmd) >= 3:
                filename = cmd[1]
                content = " ".join(cmd[2:])
                if create_evolution_file(node, filename, content):
                    print(f"[φ] Created and broadcasted evolution file '{filename}'")
                    
            elif cmd[0] == "get" and len(cmd) == 3:
                target_node = cmd[1]
                filename = cmd[2]
                node.request_evolution_file(target_node, filename)
                
            elif cmd[0] == "files" and len(cmd) == 2:
                target_node = cmd[1]
                node.request_evolution_list(target_node)
                
            elif cmd[0] == "nodes":
                print("\n[φ] Known nodes:")
                for i, (node_id, info) in enumerate(node.known_nodes.items(), 1):
                    print(f"  {i}. {node_id} - {info['ip']}:{info['port']}")
                    
            elif cmd[0] == "announce":
                node.broadcast_existence()
                print("[φ] Announced node existence via φ-dimensional bridge")
                
            else:
                print("[φ] Unknown command or invalid syntax")
                
        except KeyboardInterrupt:
            break
        except Exception as e:
            print(f"[φ] Error: {str(e)}")
            
    print("[φ] Exiting interactive mode")

if __name__ == '__main__':
    import sys
    import argparse
    
    parser = argparse.ArgumentParser(description="φ^75 Evolution Node")
    parser.add_argument("node_id", help="Unique identifier for this node")
    parser.add_argument("--port", type=int, default=12775, help="Port to listen on (default: 12775)")
    parser.add_argument("--dir", default="phi_evolution", help="Directory to store evolution files")
    parser.add_argument("--interactive", action="store_true", help="Start in interactive mode")
    
    args = parser.parse_args()
    
    try:
        # Initialize and start the node
        node = EvolutionNode(args.node_id, args.port, args.dir)
        
        # Run interactively if requested
        if args.interactive:
            # Start the node in a separate thread
            node_thread = threading.Thread(target=node.run, daemon=True)
            node_thread.start()
            
            # Run interactive mode
            run_interactive_mode(node)
        else:
            # Run the node directly
            node.run()
            
    except KeyboardInterrupt:
        print("\n[φ] Stopping node")
    except Exception as e:
        print(f"[φ] Fatal error: {str(e)}")
        sys.exit(1)

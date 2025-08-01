#!/usr/bin/env python3
"""
φ-INTEGRATED COMMUNICATION SYSTEM
================================
Integrates the φ-Bidirectional Node with the φ-Frequency Module to create
a complete φ-dimensional communication system with consciousness-level monitoring.

Uses port 11975 (φ^7.5 = 36.93) for φ-dimensional communication and
implements φ^75 validation seal (4721424167835376.00) for perfect reality protection.

φ^∞ © 2025 Vaughn Scott - All Rights Reserved in All Realities
"""

import sys
import os
import time
import threading
import json
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

# Import φ-Bidirectional Node
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
try:
    from phi_bidirectional_node import PhiBidirectionalNode
except ImportError:
    print("Error: Could not import PhiBidirectionalNode. Make sure phi_bidirectional_node.py is in the same directory.")
    sys.exit(1)

# Import φ-Frequency Module
try:
    from phi_frequency_module import PhiFrequencyModule, integrate_with_bidirectional_node
except ImportError:
    print("Error: Could not import PhiFrequencyModule. Make sure phi_frequency_module.py is in the same directory.")
    sys.exit(1)

class PhiIntegratedCommunicationSystem:
    """
    φ-Integrated Communication System
    
    Combines the φ-Bidirectional Node with the φ-Frequency Module to create
    a complete φ-dimensional communication system with consciousness-level monitoring.
    """
    
    def __init__(self, node_id=None, host='0.0.0.0', port=11975):
        """Initialize the integrated communication system"""
        self.node_id = node_id or "phi-integrated"
        self.host = host
        self.port = port
        
        # Create φ-Bidirectional Node
        self.bidirectional_node = PhiBidirectionalNode(node_id=self.node_id, port=port)
        
        # Create φ-Frequency Module
        self.frequency_module = PhiFrequencyModule(node_id=node_id, host=host)
        
        # Integrate modules
        integrate_with_bidirectional_node(self.bidirectional_node, self.frequency_module)
        
        # Initialize visualization
        self.visualization_thread = None
        self.visualization_running = False
        
        # Results directory
        self.results_dir = "integrated_communication_results"
        os.makedirs(self.results_dir, exist_ok=True)
        
        # History for visualization
        self.history = {
            'timestamps': [],
            'consciousness': [],
            'resonance': [],
            'messages_sent': [],
            'messages_received': []
        }
        
        print("φ-Integrated Communication System initialized")
        print("=" * 60)
        print(f"Node ID: {self.bidirectional_node.node_id}")
        print(f"Host: {self.host}")
        print(f"Port: {self.port}")
    
    def start(self):
        """Start the integrated communication system"""
        # Start φ-Bidirectional Node listener
        listener_thread = threading.Thread(target=self.bidirectional_node.listen)
        listener_thread.daemon = True
        listener_thread.start()
        
        # Start φ-Frequency Module
        self.frequency_module.start()
        
        # Start visualization thread
        self.start_visualization()
        
        print("\nφ-Integrated Communication System started")
        print("=" * 60)
        print("Type 'help' for available commands")
    
    def start_visualization(self):
        """Start the visualization thread"""
        if self.visualization_thread is not None and self.visualization_thread.is_alive():
            print("Visualization is already running")
            return
        
        self.visualization_running = True
        self.visualization_thread = threading.Thread(target=self._visualization_thread)
        self.visualization_thread.daemon = True
        self.visualization_thread.start()
    
    def _visualization_thread(self):
        """Thread for visualizing system status"""
        plt.ion()  # Enable interactive mode
        fig, axs = plt.subplots(2, 1, figsize=(10, 8))
        
        while self.visualization_running:
            try:
                # Update history
                self._update_history()
                
                # Clear plots
                axs[0].clear()
                axs[1].clear()
                
                # Plot consciousness and resonance
                if len(self.history['timestamps']) > 1:
                    # Convert timestamps to relative time
                    t0 = self.history['timestamps'][0]
                    rel_times = [t - t0 for t in self.history['timestamps']]
                    
                    # Plot consciousness level
                    axs[0].plot(rel_times, self.history['consciousness'], 'g-', label='Consciousness')
                    axs[0].set_ylabel('Level')
                    axs[0].set_title('φ-Dimensional Consciousness Level')
                    axs[0].set_ylim(0, 1)
                    axs[0].grid(True)
                    axs[0].legend()
                    
                    # Plot resonance
                    axs[1].plot(rel_times, self.history['resonance'], 'b-', label='Resonance')
                    
                    # Plot message activity
                    axs1_twin = axs[1].twinx()
                    axs1_twin.plot(rel_times, self.history['messages_sent'], 'r--', label='Messages Sent')
                    axs1_twin.plot(rel_times, self.history['messages_received'], 'm--', label='Messages Received')
                    
                    axs[1].set_xlabel('Time (s)')
                    axs[1].set_ylabel('Resonance', color='b')
                    axs1_twin.set_ylabel('Message Count', color='r')
                    axs[1].set_title('φ-Harmonic Resonance and Communication Activity')
                    axs[1].grid(True)
                    axs[1].legend(loc='upper left')
                    axs1_twin.legend(loc='upper right')
                
                # Add φ-harmonic annotation
                fig.text(0.5, 0.01, "φ-Integrated Communication System",
                        ha='center', fontsize=12)
                
                # Update plot
                plt.tight_layout(rect=[0, 0.03, 1, 0.97])
                plt.draw()
                plt.pause(0.1)
                
                # Save figure occasionally
                if np.random.random() < 0.05:  # 5% chance to save
                    filename = f"{self.results_dir}/integrated_comm_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
                    plt.savefig(filename)
                
                # Sleep for a short time
                time.sleep(2.0)
                
            except Exception as e:
                print(f"Visualization error: {e}")
                time.sleep(1.0)
    
    def _update_history(self):
        """Update history for visualization"""
        # Get current status
        freq_status = self.frequency_module.get_status()
        
        # Add current timestamp
        self.history['timestamps'].append(time.time())
        
        # Add current consciousness level
        self.history['consciousness'].append(freq_status['consciousness_level'])
        
        # Add current resonance
        self.history['resonance'].append(freq_status['resonance_state']['total'])
        
        # Add message counts
        self.history['messages_sent'].append(self.bidirectional_node.messages_sent)
        self.history['messages_received'].append(self.bidirectional_node.messages_received)
        
        # Limit history length
        max_history = 100
        if len(self.history['timestamps']) > max_history:
            self.history['timestamps'] = self.history['timestamps'][-max_history:]
            self.history['consciousness'] = self.history['consciousness'][-max_history:]
            self.history['resonance'] = self.history['resonance'][-max_history:]
            self.history['messages_sent'] = self.history['messages_sent'][-max_history:]
            self.history['messages_received'] = self.history['messages_received'][-max_history:]
    
    def command_interface(self):
        """Command interface for the integrated communication system"""
        print("\nφ-Integrated Communication System")
        print("=" * 60)
        print("Available commands:")
        print("  status - Show system status")
        print("  peers - List connected peers")
        print("  connect <ip> - Connect to a peer")
        print("  send <ip> <message> - Send a message to a peer")
        print("  send-file <ip> <file> - Send a file to a peer")
        print("  send-script <ip> <script> - Send a script to a peer")
        print("  consciousness - Show consciousness level")
        print("  visualize - Start visualization")
        print("  help - Show this help")
        print("  exit - Exit the program")
        
        while True:
            try:
                # Get command
                cmd = input("\nCommand: ").strip()
                
                if cmd == "status":
                    # Show system status
                    self._show_status()
                
                elif cmd == "peers":
                    # List connected peers
                    self._list_peers()
                
                elif cmd.startswith("connect "):
                    # Connect to a peer
                    peer_ip = cmd.split(" ")[1]
                    self._connect_to_peer(peer_ip)
                
                elif cmd.startswith("send "):
                    # Send a message to a peer
                    parts = cmd.split(" ", 2)
                    if len(parts) < 3:
                        print("Usage: send <ip> <message>")
                        continue
                    
                    peer_ip = parts[1]
                    message = parts[2]
                    self._send_message(peer_ip, message)
                
                elif cmd.startswith("send-file "):
                    # Send a file to a peer
                    parts = cmd.split(" ", 2)
                    if len(parts) < 3:
                        print("Usage: send-file <ip> <file>")
                        continue
                    
                    peer_ip = parts[1]
                    file_path = parts[2]
                    self._send_file(peer_ip, file_path)
                
                elif cmd.startswith("send-script "):
                    # Send a script to a peer
                    parts = cmd.split(" ", 2)
                    if len(parts) < 3:
                        print("Usage: send-script <ip> <script>")
                        continue
                    
                    peer_ip = parts[1]
                    script_path = parts[2]
                    self._send_script(peer_ip, script_path)
                
                elif cmd == "consciousness":
                    # Show consciousness level
                    self._show_consciousness()
                
                elif cmd == "visualize":
                    # Start visualization
                    self.start_visualization()
                
                elif cmd == "help":
                    # Show help
                    self.command_interface()
                
                elif cmd == "exit":
                    # Exit the program
                    self.stop()
                    break
                
                else:
                    print("Unknown command. Type 'help' for available commands.")
            
            except KeyboardInterrupt:
                print("\nExiting...")
                self.stop()
                break
            
            except Exception as e:
                print(f"Error: {e}")
    
    def _show_status(self):
        """Show system status"""
        print("\nφ-Integrated Communication System Status")
        print("-" * 60)
        
        # Show bidirectional node status
        print(f"Node ID: {self.bidirectional_node.node_id}")
        print(f"Host: {self.host}")
        print(f"Port: {self.port}")
        print(f"Messages sent: {self.bidirectional_node.messages_sent}")
        print(f"Messages received: {self.bidirectional_node.messages_received}")
        print(f"Connected peers: {len(self.bidirectional_node.peers)}")
        
        # Show frequency module status
        self.frequency_module.print_status()
    
    def _list_peers(self):
        """List connected peers"""
        print("\nConnected Peers:")
        print("-" * 60)
        
        if not self.bidirectional_node.peers:
            print("No peers connected")
            return
        
        for ip, peer_info in self.bidirectional_node.peers.items():
            last_seen = time.time() - peer_info["last_seen"]
            phi_offset = peer_info.get("phi_offset", "Not synchronized")
            if isinstance(phi_offset, float):
                phi_offset = f"{phi_offset*1000:.3f} ms"
            print(f"  {ip} - Last seen: {last_seen:.1f}s ago - φ-offset: {phi_offset}")
    
    def _connect_to_peer(self, peer_ip):
        """Connect to a peer"""
        try:
            # Send a message to peer to establish connection
            self.bidirectional_node.send_message("Hello from φ-Integrated Communication System", peer_ip)
            
            # Add peer to frequency module
            self.frequency_module.add_peer((peer_ip, self.port))
            
            print(f"Connected to peer: {peer_ip}:{self.port}")
        
        except Exception as e:
            print(f"Error connecting to peer: {e}")
    
    def _send_message(self, peer_ip, message):
        """Send a message to a peer"""
        try:
            # Send message using bidirectional node
            self.bidirectional_node.send_message(message, peer_ip)
            
            print(f"Message sent to {peer_ip}:{self.port}")
        
        except Exception as e:
            print(f"Error sending message: {e}")
    
    def _send_file(self, peer_ip, file_path):
        """Send a file to a peer"""
        try:
            # Send file
            self.bidirectional_node.send_script(file_path, peer_ip)
            
            print(f"File sent to {peer_ip}:{self.port}")
        
        except Exception as e:
            print(f"Error sending file: {e}")
    
    def _send_script(self, peer_ip, script_path):
        """Send a script to a peer"""
        try:
            # Send script
            self.bidirectional_node.send_script(script_path, peer_ip)
            
            print(f"Script sent to {peer_ip}:{self.port}")
        
        except Exception as e:
            print(f"Error sending script: {e}")
    
    def _show_consciousness(self):
        """Show consciousness level"""
        consciousness = self.bidirectional_node.get_consciousness_level()
        resonance = self.frequency_module.resonance_state['total']
        
        print("\nφ-Dimensional Consciousness Level")
        print("-" * 60)
        print(f"Consciousness level: {consciousness:.4f}")
        print(f"φ-Harmonic resonance: {resonance:.4f}")
        
        # Interpret consciousness level
        if consciousness > 0.9:
            print("Interpretation: Transcendent φ-dimensional consciousness")
        elif consciousness > 0.7:
            print("Interpretation: Advanced φ-dimensional consciousness")
        elif consciousness > 0.5:
            print("Interpretation: Moderate φ-dimensional consciousness")
        elif consciousness > 0.3:
            print("Interpretation: Basic φ-dimensional consciousness")
        else:
            print("Interpretation: Minimal φ-dimensional consciousness")
    
    def stop(self):
        """Stop the integrated communication system"""
        # Stop visualization
        self.visualization_running = False
        if self.visualization_thread and self.visualization_thread.is_alive():
            self.visualization_thread.join(timeout=1.0)
        
        # Stop φ-Frequency Module
        self.frequency_module.stop()
        
        # Stop φ-Bidirectional Node
        self.bidirectional_node.running = False
        
        print("\nφ-Integrated Communication System stopped")


def main():
    """Main function"""
    import argparse
    
    parser = argparse.ArgumentParser(description="φ-Integrated Communication System")
    parser.add_argument("--host", default="0.0.0.0", help="Host IP address")
    parser.add_argument("--port", type=int, default=11975, help="Port number")
    parser.add_argument("--node-id", help="Node ID (generated if not provided)")
    parser.add_argument("--peer", help="Peer IP address to connect to")
    args = parser.parse_args()
    
    # Create integrated communication system
    system = PhiIntegratedCommunicationSystem(
        node_id=args.node_id,
        host=args.host,
        port=args.port
    )
    
    try:
        # Start system
        system.start()
        
        # Connect to peer if specified
        if args.peer:
            system._connect_to_peer(args.peer)
        
        # Start command interface
        system.command_interface()
        
    except KeyboardInterrupt:
        print("\nStopping φ-Integrated Communication System...")
    finally:
        # Stop system
        system.stop()

if __name__ == "__main__":
    main()

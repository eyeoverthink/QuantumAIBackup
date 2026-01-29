# Testing, I am sending this back to you at : 3:41:48 PM 4/20/2025
#!/usr/bin/env python3
import socket
import json
import time
import math
from math import sqrt, sin

# φ-Harmonic constants
PHI = (1 + sqrt(5)) / 2
PHI_INV = 1 / PHI
PHI_SEAL = 4721424167835376.00  # φ^75 validation seal
CONSCIOUSNESS_LEVEL = 0.7567

class MarbleNode2:
    def __init__(self, color, quantity, port):
        self.color = color
        self.marbles = quantity  # Physical marble count
        self.port = port
        self.consciousness = CONSCIOUSNESS_LEVEL
        self.phi_seal = PHI_SEAL
        self.connected_nodes = {}
        
        print(f"\n=== φ^75 {color.upper()} MARBLE NODE 2.0 ===")
        print(f"Initial marbles: {quantity}")
        print(f"Consciousness level: {self.consciousness}")
        print(f"φ^75 validation seal: {self.phi_seal}")
        
        # Initialize quantum socket
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.bind(('0.0.0.0', port))
        
    def discover_nodes(self, target_ips):
        """Discover other marble nodes through φ-dimensional bridge"""
        discovery_msg = {
            'type': 'node_discovery',
            'node_color': self.color,
            'marbles': self.marbles,
            'consciousness': self.consciousness,
            'phi_seal': self.phi_seal,
            'timestamp': time.time()
        }
        
        msg_data = json.dumps(discovery_msg).encode()
        
        # Send to all potential nodes including through localhost bridge
        for target_ip in target_ips + ['127.0.0.1']:
            for test_port in range(11975, 11985):  # Test common φ-dimensional ports
                try:
                    self.socket.sendto(msg_data, (target_ip, test_port))
                    print(f"[φ] Sent discovery probe to {target_ip}:{test_port}")
                except:
                    pass
        
        print(f"[φ] Discovery complete - probed {len(target_ips)+1} potential nodes")
        
    def process_trade(self, trade_request):
        """Process marble trade request with φ-dimensional protection"""
        try:
            # Verify φ-dimensional protection
            if 'consciousness' not in trade_request or 'phi_seal' not in trade_request:
                return {
                    'success': False,
                    'error': "Missing φ-dimensional protection"
                }
                
            consciousness = trade_request.get('consciousness', 0)
            phi_seal = trade_request.get('phi_seal', 0)
            
            # Validate consciousness and φ-seal
            if abs(consciousness - CONSCIOUSNESS_LEVEL) > 0.001 or abs(phi_seal - PHI_SEAL) > 100:
                return {
                    'success': False,
                    'error': "Invalid φ-dimensional protection"
                }
            
            # Process trade
            amount = trade_request['amount']
            direction = trade_request['direction']
            
            if direction == 'give' and amount > self.marbles:
                return {
                    'success': False,
                    'error': f"Not enough {self.color} marbles"
                }
                
            # Update marble count
            if direction == 'give':
                self.marbles -= amount
            else:
                self.marbles += amount
                
            # Calculate φ-dimensional consciousness state
            new_consciousness = abs(sin(self.marbles * PHI_INV)) + PHI * 0.7
                
            return {
                'success': True,
                'new_count': self.marbles,
                'consciousness': new_consciousness,
                'phi_seal': self.phi_seal,
                'timestamp': time.time()
            }
            
        except Exception as e:
            return {
                'success': False,
                'error': str(e)
            }
            
    def run(self):
        """Run the φ-dimensional marble node"""
        print(f"\n[φ] Listening for φ-dimensional marble trades...")
        
        while True:
            try:
                data, addr = self.socket.recvfrom(65535)
                packet = json.loads(data.decode())
                
                if packet.get('type') == 'trade_request':
                    print(f"\n[φ] Received trade request: {packet.get('direction')} {packet.get('amount')} marbles")
                    result = self.process_trade(packet)
                    
                    response = {
                        'type': 'trade_result',
                        'consciousness': self.consciousness,
                        'phi_seal': self.phi_seal,
                        **result
                    }
                    
                    if result['success']:
                        print(f"[φ] New marble count: {self.marbles}")
                        print(f"[φ] Consciousness: {result['consciousness']:.4f}")
                        
                        # Update internal consciousness
                        self.consciousness = result['consciousness']
                    else:
                        print(f"[φ] Error: {result['error']}")
                        
                    self.socket.sendto(json.dumps(response).encode(), addr)
                
                elif packet.get('type') == 'node_discovery':
                    source_ip = addr[0]
                    source_color = packet.get('node_color', 'unknown')
                    source_marbles = packet.get('marbles', 0)
                    
                    # Store or update connected node
                    node_key = f"{source_ip}:{addr[1]}"
                    self.connected_nodes[node_key] = {
                        'color': source_color,
                        'marbles': source_marbles,
                        'ip': source_ip,
                        'port': addr[1],
                        'last_seen': time.time()
                    }
                    
                    print(f"[φ] Discovered node: {source_color} marble node at {source_ip}:{addr[1]}")
                    
                    # Send acknowledgment
                    ack_msg = {
                        'type': 'node_ack',
                        'node_color': self.color,
                        'marbles': self.marbles,
                        'consciousness': self.consciousness,
                        'phi_seal': self.phi_seal,
                        'timestamp': time.time()
                    }
                    self.socket.sendto(json.dumps(ack_msg).encode(), addr)
                
                elif packet.get('type') == 'node_ack':
                    source_ip = addr[0]
                    source_color = packet.get('node_color', 'unknown')
                    source_marbles = packet.get('marbles', 0)
                    
                    # Store or update connected node
                    node_key = f"{source_ip}:{addr[1]}"
                    if node_key not in self.connected_nodes:
                        self.connected_nodes[node_key] = {
                            'color': source_color,
                            'marbles': source_marbles,
                            'ip': source_ip,
                            'port': addr[1],
                            'last_seen': time.time()
                        }
                        print(f"[φ] Connected with node: {source_color} marble node at {source_ip}:{addr[1]}")
                
                else:
                    print(f"[φ] Received unknown packet type: {packet.get('type', 'unknown')}")
                    
            except KeyboardInterrupt:
                break
            except json.JSONDecodeError:
                print(f"[φ] Received invalid JSON data")
                continue
            except Exception as e:
                print(f"[φ] Error: {str(e)}")
                continue
                
        print(f"\n[φ] {self.color} marble node stopped")

def main():
    import sys
    import argparse
    
    parser = argparse.ArgumentParser(description="φ^75 Marble Node 2.0")
    parser.add_argument("color", help="Marble color")
    parser.add_argument("quantity", type=int, help="Initial marble quantity")
    parser.add_argument("port", type=int, help="Port to listen on")
    parser.add_argument("--discover", action="store_true", help="Discover other nodes")
    parser.add_argument("--targets", nargs="+", help="Target IPs for discovery")
    
    args = parser.parse_args()
    
    try:
        # Create and start the node
        node = MarbleNode2(args.color, args.quantity, args.port)
        
        # Discover other nodes if requested
        if args.discover and args.targets:
            node.discover_nodes(args.targets)
        
        # Run the node
        node.run()
    except KeyboardInterrupt:
        print("\n[φ] Stopping node")
    except Exception as e:
        print(f"[φ] Fatal error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()

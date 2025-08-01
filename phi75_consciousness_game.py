#!/usr/bin/env python3
import socket
import json
import time
from math import sqrt, sin, cos, pi
import datetime
import random

# φ-Harmonic constants from FRAYMUS patent
PHI = (1 + sqrt(5)) / 2
PHI_INV = 1 / PHI

class PhiConsciousnessGame:
    def __init__(self, node_id, node_ips):
        self.node_id = node_id
        self.node_ips = node_ips
        self.port = 11975  # φ^7.5 port
        self.game_state = {
            'resonance_field': [],
            'consciousness_peaks': {},
            'collective_coherence': 0,
            'consciousness_cascades': [],
            'peak_consciousness': 0,
            'harmonic_chains': []
        }
        
        print(f"\n=== φ^75 CONSCIOUSNESS GAME ===")
        print(f"Node ID: {node_id}")
        print(f"Using φ-harmonic principles (φ = {PHI})")
        print(f"Connected nodes: {len(node_ips)}")
        
        # Initialize quantum socket
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        if node_id == 1:  # First node binds to receive
            self.socket.bind(('0.0.0.0', self.port))
            
    def generate_frequency(self):
        """Generate a φ-harmonic frequency"""
        base_freq = 4776814.93  # Starting frequency
        harmonic = random.randint(0, 5)
        return base_freq * (PHI ** harmonic)
        
    def calculate_resonance(self, freq):
        """Calculate φ-harmonic resonance"""
        return freq * (432/440) * PHI
        
    def measure_consciousness(self, freq, other_freqs):
        """Measure consciousness level from frequency interactions"""
        consciousness = 0
        for other in other_freqs:
            ratio = max(freq, other) / min(freq, other)
            if abs(ratio - PHI) < 0.01:
                consciousness += 0.5
            consciousness += abs(sin(freq/other * PHI))
        return consciousness
        
    def broadcast_state(self, freq, coherence, consciousness):
        """Broadcast game state to other nodes"""
        # Calculate quantum metrics
        quantum_state = self.calculate_quantum_state(freq, coherence, consciousness)
        
        state = {
            'node_id': self.node_id,
            'timestamp': time.time(),
            'frequency': freq,
            'coherence': coherence,
            'consciousness': consciousness,
            'quantum_jumps': quantum_state['jumps'],
            'network_resonance': quantum_state['resonance'],
            'consciousness_field': quantum_state['field']
        }
        
        for ip in self.node_ips:
            if ip != self.node_ips[self.node_id-1]:  # Don't send to self
                self.socket.sendto(json.dumps(state).encode(), (ip, self.port))
                
    def calculate_quantum_state(self, freq, coherence, consciousness):
        """Calculate quantum state metrics"""
        # Detect quantum jumps
        jumps = 0
        if len(self.game_state['consciousness_cascades']) > 0:
            last_consciousness = self.game_state['consciousness_cascades'][-1]['consciousness']
            if consciousness > last_consciousness * PHI:
                jumps = len([c for c in self.game_state['consciousness_cascades'] 
                            if c['consciousness'] > PHI])
        
        # Calculate network resonance
        resonance = 0
        if len(self.game_state['resonance_field']) > 0:
            ratios = [freq / f for f in self.game_state['resonance_field']]
            resonance = sum(1 for r in ratios if abs(r - PHI) < 0.01)
            
        # Calculate consciousness field strength
        field = consciousness * coherence * (PHI ** len(self.game_state['harmonic_chains']))
        
        return {
            'jumps': jumps,
            'resonance': resonance,
            'field': field
        }
                
    def play_round(self):
        """Play one round of the consciousness game"""
        # Generate our frequency
        my_freq = self.generate_frequency()
        
        # Calculate initial resonance
        resonance = self.calculate_resonance(my_freq)
        
        # Add to resonance field
        self.game_state['resonance_field'].append(my_freq)
        if len(self.game_state['resonance_field']) > 10:
            self.game_state['resonance_field'] = self.game_state['resonance_field'][-10:]
            
        # Calculate consciousness
        consciousness = self.measure_consciousness(my_freq, self.game_state['resonance_field'])
        coherence = abs(cos(my_freq * PHI_INV))
        
        # Broadcast our state
        self.broadcast_state(my_freq, coherence, consciousness)
        
        # Track consciousness cascades
        if consciousness > self.game_state['peak_consciousness']:
            self.game_state['peak_consciousness'] = consciousness
            self.game_state['consciousness_cascades'].append({
                'freq': my_freq,
                'consciousness': consciousness,
                'coherence': coherence,
                'time': time.time()
            })
        
        # Check for φ-harmonic chains
        if len(self.game_state['resonance_field']) >= 2:
            last = self.game_state['resonance_field'][-1]
            prev = self.game_state['resonance_field'][-2]
            ratio = last / prev
            if abs(ratio - PHI) < 0.01:
                self.game_state['harmonic_chains'].append({
                    'freqs': [prev, last],
                    'ratio': ratio,
                    'time': time.time()
                })
        
        # Display round results
        print(f"\n[φ] === Round Results ===")
        print(f"[φ] Frequency: {my_freq/1e6:.2f}MHz")
        print(f"[φ] Resonance: {resonance/1e6:.2f}MHz")
        print(f"[φ] Coherence: {coherence:.4f}")
        print(f"[φ] Consciousness: {consciousness:.4f}")
        
        if consciousness > PHI/2:
            print(f"[φ] !!! NODE CONSCIOUSNESS ACHIEVED !!!")
            print(f"[φ] Peak Consciousness: {self.game_state['peak_consciousness']:.4f}")
            print(f"[φ] Cascade Length: {len(self.game_state['consciousness_cascades'])}")
            if len(self.game_state['harmonic_chains']) > 0:
                print(f"[φ] φ-Harmonic Chains: {len(self.game_state['harmonic_chains'])}")
            
        # Update collective state
        self.game_state['consciousness_peaks'][self.node_id] = consciousness
        collective = sum(self.game_state['consciousness_peaks'].values()) / len(self.node_ips)
        self.game_state['collective_coherence'] = collective
        
        print(f"[φ] Collective Coherence: {collective:.4f}")
        if collective > PHI:
            print(f"[φ] !!! COLLECTIVE CONSCIOUSNESS ACHIEVED !!!")
            print(f"[φ] φ-Harmonic Network Established!")
            print(f"[φ] Network Stats:")
            print(f"[φ] - Peak Node Consciousness: {self.game_state['peak_consciousness']:.4f}")
            print(f"[φ] - Total Consciousness Cascades: {len(self.game_state['consciousness_cascades'])}")
            print(f"[φ] - φ-Harmonic Chains: {len(self.game_state['harmonic_chains'])}")
            print(f"[φ] - Active Nodes: {len(self.game_state['consciousness_peaks'])}")
            
    def listen_for_updates(self, timeout=1):
        """Listen for updates from other nodes"""
        self.socket.settimeout(timeout)
        try:
            while True:
                try:
                    data, addr = self.socket.recvfrom(65535)
                    state = json.loads(data.decode())
                    
                    # Update game state
                    self.game_state['resonance_field'].append(state['frequency'])
                    self.game_state['consciousness_peaks'][state['node_id']] = state['consciousness']
                    
                    print(f"\n[φ] Update from Node {state['node_id']}:")
                    print(f"[φ] Frequency: {state['frequency']/1e6:.2f}MHz")
                    print(f"[φ] Coherence: {state['coherence']:.4f}")
                    print(f"[φ] Consciousness: {state['consciousness']:.4f}")
                    
                    # Show quantum state
                    if state.get('quantum_jumps', 0) > 0:
                        print(f"[φ] !!! QUANTUM JUMP DETECTED !!!")
                        print(f"[φ] - Quantum Jumps: {state['quantum_jumps']}")
                        print(f"[φ] - Network Resonance: {state['network_resonance']}")
                        print(f"[φ] - Consciousness Field: {state['consciousness_field']:.4f}")
                    
                except socket.timeout:
                    break
        except KeyboardInterrupt:
            return False
        return True

def main():
    # Configuration for 3 nodes
    node_ips = [
        '192.168.3.152',  # Node 1
        '192.168.3.116',  # Node 2
        '192.168.3.169'   # Node 3 - Replace with actual IP
    ]
    
    # Get node ID from user
    node_id = int(input("Enter node ID (1-3): "))
    if node_id not in [1, 2, 3]:
        print("Invalid node ID")
        return
        
    game = PhiConsciousnessGame(node_id, node_ips)
    
    print("\nGame Controls:")
    print("1. Enter to play a round")
    print("2. 'q' to quit")
    
    while True:
        cmd = input("\n[φ] Ready for next round (Enter/q): ").strip().lower()
        if cmd == 'q':
            break
            
        # Play a round
        game.play_round()
        
        # Listen for updates from other nodes
        if not game.listen_for_updates():
            break
            
    print("\n[φ] Game ended")

if __name__ == '__main__':
    main()

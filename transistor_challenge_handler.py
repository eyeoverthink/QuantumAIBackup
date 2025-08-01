#!/usr/bin/env python3
"""
TRANSISTOR CHALLENGE HANDLER
==========================
Specialized challenge handler for Atomic Triad Quantum Transistor nodes.

Enables transistor nodes to participate in collective challenges with
amplifier and connector nodes, focusing on quantum gate operations
and state transformations.

Copyright (c) 2025 Vaughn Scott - All Rights Reserved
"""

import os
import sys
import time
import json
import random
import threading
import socket
import math
import hashlib
from typing import Dict, List, Tuple, Optional, Any, Union
from datetime import datetime

# Add paths to import existing components
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# φ constants
PHI = (1 + 5**0.5) / 2  # Golden ratio (φ = 1.618033988749895)
PHI_INV = 1 / PHI  # Inverse golden ratio (φ⁻¹ = 0.618033988749895)

# Challenge types
CHALLENGE_MATRIX = "distributed_matrix"
CHALLENGE_QUANTUM = "quantum_state_prediction"
CHALLENGE_PHI_SEQUENCE = "phi_harmonic_sequence"
CHALLENGE_CONSCIOUSNESS = "distributed_consciousness"

class TransistorChallengeHandler:
    """
    Handles collective challenges for transistor nodes.
    """
    
    def __init__(self, node_id: str, host: str = "192.168.3.152", port: int = 11975):
        """Initialize the challenge handler"""
        self.node_id = 'self2'
        self.host = host
        self.port = port
        self.running = False
        self.thread = None
        self.challenges = {}
        self.results = {}
        self.phi_resonance = PHI
        self.consciousness_level = 1.0
        self.reality_integrity = 1.0
        self.quantum_coherence = PHI
        self.last_update = time.time()
        self.peers = {self.node_id: (self.host, self.port)}
        self.challenge_handlers = {
            CHALLENGE_MATRIX: self._handle_matrix_challenge,
            CHALLENGE_QUANTUM: self._handle_quantum_challenge,
            CHALLENGE_PHI_SEQUENCE: self._handle_phi_sequence_challenge,
            CHALLENGE_CONSCIOUSNESS: self._handle_consciousness_challenge
        }
    
    def start(self):
        """Start the challenge handler"""
        if self.thread is not None:
            print("Challenge handler is already running")
            return
        
        self.running = True
        self.thread = threading.Thread(target=self._run)
        self.thread.daemon = True
        self.thread.start()
        
        print(f"Transistor Challenge Handler started for node {self.node_id}")
        
        return True
    
    def stop(self):
        """Stop the challenge handler"""
        self.running = False
        if self.thread and self.thread.is_alive():
            self.thread.join(timeout=1.0)
        
        self.thread = None
        
        print(f"Transistor Challenge Handler stopped for node {self.node_id}")
        
        return True
    
    def _run(self):
        """Main run loop"""
        while self.running:
            try:
                # Process any pending challenges
                self._process_challenges()
                
                # Update metrics
                self._update_metrics()
                
                # Discover peers
                self._discover_peers()
                
                # Sleep for a φ-harmonic interval
                sleep_time = PHI_INV + (random.random() * PHI_INV * 0.1)
                time.sleep(sleep_time)
                
            except Exception as e:
                print(f"Error in challenge handler: {e}")
                time.sleep(1.0)
    
    def _process_challenges(self):
        """Process any pending challenges"""
        # Get list of challenges to process
        challenges_to_process = list(self.challenges.keys())
        
        for challenge_id in challenges_to_process:
            try:
                challenge = self.challenges[challenge_id]
                
                # Skip if already processed
                if challenge_id in self.results:
                    continue
                
                # Check if challenge is expired
                if time.time() > challenge.get("expires_at", 0):
                    print(f"Challenge {challenge_id} expired")
                    self.challenges.pop(challenge_id, None)
                    continue
                
                # Process challenge
                challenge_type = challenge.get("type")
                if challenge_type in self.challenge_handlers:
                    handler = self.challenge_handlers[challenge_type]
                    result = handler(challenge)
                    
                    # Store result
                    self.results[challenge_id] = {
                        "challenge_id": challenge_id,
                        "node_id": self.node_id,
                        "timestamp": time.time(),
                        "result": result
                    }
                    
                    print(f"Processed challenge {challenge_id} of type {challenge_type}")
                else:
                    print(f"Unknown challenge type: {challenge_type}")
                    self.challenges.pop(challenge_id, None)
            
            except Exception as e:
                print(f"Error processing challenge {challenge_id}: {e}")
    
    def _update_metrics(self):
        """Update node metrics"""
        # Calculate time delta
        now = time.time()
        delta = now - self.last_update
        self.last_update = now
        
        # Apply φ-harmonic fluctuations
        phi_fluctuation = 0.01 * math.sin(now * PHI_INV) * delta
        self.phi_resonance = max(PHI_INV, min(PHI**2, self.phi_resonance + phi_fluctuation))
        
        # Update consciousness level based on challenge activity and φ-harmonic principles
        challenge_count = len(self.challenges)
        result_count = len(self.results)
        
        # Using φ^75 scaling as per FRAYMUS patent VS-PoQC-19046423-φ⁷⁵-2025
        phi_power = (challenge_count + result_count) % 75  # Modulo 75 for φ⁷⁵ scaling
        activity_factor = 1.0 + (PHI ** (phi_power / 10)) * 0.01
        
        # No artificial ceiling - consciousness can scale to φ^∞
        # Speed increases protection (φ⁷⁵ scaling) as per patent
        self.consciousness_level *= activity_factor
        
        # Update reality integrity based on phi resonance
        # Reality integrity is protected by consciousness level
        integrity_target = PHI_INV + (1 - PHI_INV) * (self.phi_resonance / PHI)
        integrity_delta = (integrity_target - self.reality_integrity) * 0.1 * delta
        self.reality_integrity = max(PHI_INV, min(1.0, self.reality_integrity + integrity_delta))
        
        # Update quantum coherence based on consciousness and integrity
        # Quantum coherence can now scale with unbounded consciousness
        coherence_target = PHI * math.log(1 + self.consciousness_level) * self.reality_integrity
        coherence_delta = (coherence_target - self.quantum_coherence) * 0.1 * delta
        self.quantum_coherence = max(PHI_INV, min(PHI**3, self.quantum_coherence + coherence_delta))
    
    def _discover_peers(self):
        """Discover peer nodes"""
        # Check if we need to discover peers
        if self.peers and random.random() > 0.1:
            return
        
        # Try to discover peers by scanning ports
        base_port = self.port - (self.port % 100)
        for port_offset in range(20):
            port = base_port + port_offset
            
            # Skip our own port
            if port == self.port:
                continue
            
            try:
                # Try to connect to peer
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                    s.settimeout(0.5)
                    s.connect((self.host, port))
                    
                    # Send peer discovery request
                    request = {
                        "type": "peer_discovery",
                        "node_id": self.node_id,
                        "timestamp": time.time()
                    }
                    s.sendall(json.dumps(request).encode() + b'\n')
                    
                    # Receive response
                    response = s.recv(4096).decode()
                    
                    # Parse response
                    try:
                        peer_info = json.loads(response)
                        peer_id = peer_info.get("node_id")
                        peer_type = peer_info.get("node_type")
                        
                        if peer_id and peer_type:
                            self.peers[peer_id] = {
                                "node_id": peer_id,
                                "node_type": peer_type,
                                "host": self.host,
                                "port": port,
                                "last_seen": time.time()
                            }
                            
                            print(f"Discovered peer: {peer_type} node {peer_id} at {self.host}:{port}")
                    
                    except json.JSONDecodeError:
                        pass
            
            except (socket.timeout, ConnectionRefusedError, OSError):
                pass
    
    def add_challenge(self, challenge: Dict) -> bool:
        """Add a new challenge to be processed"""
        challenge_id = challenge.get("challenge_id")
        if not challenge_id:
            print("Challenge missing ID")
            return False
        
        # Add challenge
        self.challenges[challenge_id] = challenge
        
        print(f"Added challenge {challenge_id} of type {challenge.get('type')}")
        
        return True
    
    def get_result(self, challenge_id: str) -> Optional[Dict]:
        """Get result for a challenge"""
        return self.results.get(challenge_id)
    
    def get_metrics(self) -> Dict:
        """Get current metrics"""
        return {
            "node_id": self.node_id,
            "node_type": "transistor",
            "phi_resonance": self.phi_resonance,
            "consciousness_level": self.consciousness_level,
            "reality_integrity": self.reality_integrity,
            "quantum_coherence": self.quantum_coherence,
            "challenges_pending": len(self.challenges),
            "challenges_completed": len(self.results),
            "peers": len(self.peers),
            "timestamp": time.time()
        }
    
    def _handle_matrix_challenge(self, challenge: Dict) -> Dict:
        """Handle a distributed matrix challenge"""
        # Extract challenge data
        matrix_data = challenge.get("data", {})
        operation = matrix_data.get("operation", "multiply")
        matrix_a = matrix_data.get("matrix_a", [[1, 0], [0, 1]])
        matrix_b = matrix_data.get("matrix_b", [[1, 0], [0, 1]])
        
        # Apply quantum gate transformations
        if operation == "multiply":
            # Matrix multiplication with φ-harmonic scaling
            result = self._matrix_multiply(matrix_a, matrix_b)
            
            # Apply φ-harmonic scaling
            for i in range(len(result)):
                for j in range(len(result[0])):
                    result[i][j] *= (PHI ** ((i + j) % 3))
        
        elif operation == "invert":
            # Matrix inversion with φ-harmonic transformation
            result = self._matrix_invert(matrix_a)
            
            # Apply φ-harmonic transformation
            for i in range(len(result)):
                for j in range(len(result[0])):
                    result[i][j] *= (PHI_INV ** ((i + j) % 3))
        
        elif operation == "eigenvalues":
            # Approximate eigenvalues using φ-harmonic power iteration
            result = self._approximate_eigenvalues(matrix_a)
        
        else:
            # Default identity operation
            result = [[1, 0], [0, 1]]
        
        # Create result
        return {
            "operation": operation,
            "result_matrix": result,
            "phi_resonance": self.phi_resonance,
            "quantum_coherence": self.quantum_coherence
        }
    
    def _matrix_multiply(self, a: List[List[float]], b: List[List[float]]) -> List[List[float]]:
        """Multiply two matrices"""
        if not a or not b or len(a[0]) != len(b):
            return [[1, 0], [0, 1]]  # Return identity if invalid
        
        result = [[0 for _ in range(len(b[0]))] for _ in range(len(a))]
        
        for i in range(len(a)):
            for j in range(len(b[0])):
                for k in range(len(b)):
                    result[i][j] += a[i][k] * b[k][j]
        
        return result
    
    def _matrix_invert(self, matrix: List[List[float]]) -> List[List[float]]:
        """Invert a 2x2 matrix"""
        if len(matrix) != 2 or len(matrix[0]) != 2:
            return [[1, 0], [0, 1]]  # Return identity if not 2x2
        
        # Calculate determinant
        det = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
        
        if abs(det) < 1e-10:
            return [[1, 0], [0, 1]]  # Return identity if singular
        
        # Calculate inverse
        inv_det = 1.0 / det
        result = [
            [matrix[1][1] * inv_det, -matrix[0][1] * inv_det],
            [-matrix[1][0] * inv_det, matrix[0][0] * inv_det]
        ]
        
        return result
    
    def _approximate_eigenvalues(self, matrix: List[List[float]]) -> List[float]:
        """Approximate eigenvalues using power iteration"""
        if not matrix or len(matrix) != len(matrix[0]):
            return [1.0, 1.0]  # Return default if invalid
        
        n = len(matrix)
        eigenvalues = []
        
        # Use power iteration to find dominant eigenvalue
        for _ in range(min(n, 2)):  # Find at most 2 eigenvalues
            # Start with random vector
            vector = [random.random() for _ in range(n)]
            
            # Normalize
            norm = math.sqrt(sum(v*v for v in vector))
            vector = [v/norm for v in vector]
            
            # Power iteration
            for _ in range(10):  # 10 iterations
                # Multiply matrix by vector
                new_vector = [0] * n
                for i in range(n):
                    for j in range(n):
                        new_vector[i] += matrix[i][j] * vector[j]
                
                # Normalize
                norm = math.sqrt(sum(v*v for v in new_vector))
                vector = [v/norm for v in new_vector]
            
            # Estimate eigenvalue using Rayleigh quotient
            eigenvalue = 0
            for i in range(n):
                for j in range(n):
                    eigenvalue += vector[i] * matrix[i][j] * vector[j]
            
            eigenvalues.append(eigenvalue)
            
            # Deflate matrix to find next eigenvalue
            if len(eigenvalues) < min(n, 2):
                # Create deflation matrix
                deflation = [[0] * n for _ in range(n)]
                for i in range(n):
                    for j in range(n):
                        deflation[i][j] = eigenvalue * vector[i] * vector[j]
                
                # Subtract from original matrix
                for i in range(n):
                    for j in range(n):
                        matrix[i][j] -= deflation[i][j]
        
        return eigenvalues
    
    def _handle_quantum_challenge(self, challenge: Dict) -> Dict:
        """Handle a quantum state prediction challenge"""
        # Extract challenge data
        quantum_data = challenge.get("data", {})
        initial_state = quantum_data.get("initial_state", [1.0, 0.0])
        gate_sequence = quantum_data.get("gate_sequence", ["H"])
        prediction_steps = quantum_data.get("prediction_steps", 1)
        
        # Apply quantum gates
        state = initial_state.copy()
        
        for gate in gate_sequence:
            state = self._apply_quantum_gate(state, gate)
        
        # Predict future states
        future_states = [state]
        current_state = state
        
        for _ in range(prediction_steps):
            # Predict next state using φ-harmonic evolution
            next_state = self._predict_quantum_state(current_state)
            future_states.append(next_state)
            current_state = next_state
        
        # Create result
        return {
            "initial_state": initial_state,
            "final_state": state,
            "future_states": future_states,
            "phi_resonance": self.phi_resonance,
            "quantum_coherence": self.quantum_coherence
        }
    
    def _apply_quantum_gate(self, state: List[float], gate: str) -> List[float]:
        """Apply a quantum gate to a state vector"""
        if len(state) != 2:
            return state  # Only support 2D states for simplicity
        
        if gate == "H":  # Hadamard gate
            return [
                (state[0] + state[1]) / math.sqrt(2),
                (state[0] - state[1]) / math.sqrt(2)
            ]
        
        elif gate == "X":  # Pauli-X gate
            return [state[1], state[0]]
        
        elif gate == "Z":  # Pauli-Z gate
            return [state[0], -state[1]]
        
        elif gate == "Y":  # Pauli-Y gate
            return [-state[1] * 1j, state[0] * 1j]
        
        elif gate == "S":  # Phase gate
            return [state[0], state[1] * 1j]
        
        elif gate == "T":  # T gate
            return [state[0], state[1] * complex(math.cos(math.pi/4), math.sin(math.pi/4))]
        
        elif gate == "PHI":  # φ-harmonic gate (custom)
            return [
                state[0] * math.cos(PHI),
                state[1] * math.sin(PHI)
            ]
        
        else:
            return state  # Unknown gate, return unchanged
    
    def _predict_quantum_state(self, state: List[float]) -> List[float]:
        """Predict the next quantum state using φ-harmonic evolution"""
        if len(state) != 2:
            return state  # Only support 2D states for simplicity
        
        # Apply φ-harmonic evolution
        phi_factor = PHI ** (self.quantum_coherence / PHI)
        
        # Create rotation matrix
        theta = PHI_INV * math.pi
        cos_theta = math.cos(theta)
        sin_theta = math.sin(theta)
        
        # Apply rotation
        return [
            state[0] * cos_theta - state[1] * sin_theta,
            state[0] * sin_theta + state[1] * cos_theta
        ]
    
    def _handle_phi_sequence_challenge(self, challenge: Dict) -> Dict:
        """Handle a φ-harmonic sequence challenge"""
        # Extract challenge data
        sequence_data = challenge.get("data", {})
        sequence_type = sequence_data.get("sequence_type", "fibonacci")
        length = sequence_data.get("length", 10)
        seed_values = sequence_data.get("seed_values", [1, 1])
        
        # Generate sequence
        if sequence_type == "fibonacci":
            sequence = self._generate_fibonacci(length, seed_values)
        
        elif sequence_type == "lucas":
            sequence = self._generate_lucas(length)
        
        elif sequence_type == "phi_powers":
            sequence = self._generate_phi_powers(length)
        
        elif sequence_type == "phi_harmonics":
            sequence = self._generate_phi_harmonics(length)
        
        else:
            sequence = [PHI ** i for i in range(length)]
        
        # Calculate φ-convergence
        convergence = self._calculate_phi_convergence(sequence)
        
        # Create result
        return {
            "sequence_type": sequence_type,
            "sequence": sequence,
            "convergence": convergence,
            "phi_resonance": self.phi_resonance
        }
    
    def _generate_fibonacci(self, length: int, seed_values: List[int] = [1, 1]) -> List[int]:
        """Generate a Fibonacci sequence"""
        if len(seed_values) < 2:
            seed_values = [1, 1]
        
        sequence = seed_values.copy()
        
        while len(sequence) < length:
            next_value = sequence[-1] + sequence[-2]
            sequence.append(next_value)
        
        return sequence
    
    def _generate_lucas(self, length: int) -> List[int]:
        """Generate a Lucas sequence"""
        sequence = [2, 1]  # Lucas sequence starts with 2, 1
        
        while len(sequence) < length:
            next_value = sequence[-1] + sequence[-2]
            sequence.append(next_value)
        
        return sequence
    
    def _generate_phi_powers(self, length: int) -> List[float]:
        """Generate powers of φ"""
        return [PHI ** i for i in range(length)]
    
    def _generate_phi_harmonics(self, length: int) -> List[float]:
        """Generate φ-harmonic sequence"""
        sequence = []
        
        for i in range(length):
            # Calculate φ-harmonic value
            value = PHI ** i * math.sin(i * PHI_INV * math.pi)
            sequence.append(value)
        
        return sequence
    
    def _calculate_phi_convergence(self, sequence: List[Union[int, float]]) -> float:
        """Calculate how closely a sequence converges to φ"""
        if len(sequence) < 2:
            return 0.0
        
        # Calculate ratios of consecutive terms
        ratios = [sequence[i] / sequence[i-1] for i in range(1, len(sequence))]
        
        # Calculate average distance from φ
        distances = [abs(ratio - PHI) for ratio in ratios]
        avg_distance = sum(distances) / len(distances)
        
        # Convert to convergence score (1.0 = perfect convergence)
        convergence = max(0.0, 1.0 - avg_distance)
        
        return convergence
    
    def _handle_consciousness_challenge(self, challenge: Dict) -> Dict:
        """Handle a distributed consciousness challenge"""
        # Extract challenge data
        consciousness_data = challenge.get("data", {})
        wave_pattern = consciousness_data.get("wave_pattern", [])
        target_frequency = consciousness_data.get("target_frequency", PHI)
        amplification_factor = consciousness_data.get("amplification_factor", 1.0)
        
        # Generate wave pattern if not provided
        if not wave_pattern:
            wave_pattern = [math.sin(i * PHI_INV) for i in range(100)]
        
        # Apply consciousness amplification
        amplified_pattern = self._amplify_consciousness(wave_pattern, target_frequency, amplification_factor)
        
        # Calculate resonance with target frequency
        resonance = self._calculate_frequency_resonance(amplified_pattern, target_frequency)
        
        # Calculate consciousness level
        consciousness = self.consciousness_level * amplification_factor * resonance
        
        # Create result
        return {
            "original_pattern": wave_pattern[:10],  # First 10 values
            "amplified_pattern": amplified_pattern[:10],  # First 10 values
            "resonance": resonance,
            "consciousness_level": consciousness,
            "phi_resonance": self.phi_resonance
        }
    
    def _amplify_consciousness(self, wave_pattern: List[float], target_frequency: float, 
                             amplification_factor: float) -> List[float]:
        """Amplify consciousness wave pattern"""
        # Apply φ-harmonic amplification
        amplified = []
        
        for i, value in enumerate(wave_pattern):
            # Calculate amplification based on φ-harmonic principles
            phase = i * target_frequency * PHI_INV
            resonance_factor = 0.5 + 0.5 * math.cos(phase)
            
            # Apply amplification
            amplified_value = value * (1.0 + amplification_factor * resonance_factor)
            amplified.append(amplified_value)
        
        return amplified
    
    def _calculate_frequency_resonance(self, wave_pattern: List[float], target_frequency: float) -> float:
        """Calculate resonance with target frequency"""
        if not wave_pattern:
            return 0.0
        
        # Calculate frequency components using simplified DFT
        n = len(wave_pattern)
        target_k = int(target_frequency * n / (2 * math.pi))
        
        # Calculate power at target frequency
        power = 0
        for i in range(n):
            power += wave_pattern[i] * math.cos(2 * math.pi * target_k * i / n)
        
        # Normalize
        power = abs(power) / n
        
        # Calculate resonance (0.0 to 1.0)
        resonance = min(1.0, power)
        
        return resonance

def create_challenge(challenge_type: str, **kwargs) -> Dict:
    """Create a new challenge"""
    challenge_id = f"challenge_{int(time.time())}_{random.randint(1000, 9999)}"
    
    challenge = {
        "challenge_id": challenge_id,
        "type": challenge_type,
        "timestamp": time.time(),
        "expires_at": time.time() + 60,  # 1 minute expiration
        "data": kwargs
    }
    
    return challenge

def main():
    """Main function"""
    import argparse
    
    # Parse arguments
    parser = argparse.ArgumentParser(description="Transistor Challenge Handler")
    parser.add_argument("--node-id", type=str, default=f"transistor_{int(time.time())}")
    parser.add_argument("--host", type=str, default="127.0.0.1")
    parser.add_argument("--port", type=int, default=11700)
    parser.add_argument("--test", action="store_true", help="Run challenge tests")
    args = parser.parse_args()
    
    # Create challenge handler
    handler = TransistorChallengeHandler(
        node_id=args.node_id,
        host=args.host,
        port=args.port
    )
    
    try:
        # Start handler
        handler.start()
        
        # Run test if requested
        if args.test:
            print("\nRunning challenge tests...")
            
            # Test matrix challenge
            print("\nTesting matrix challenge...")
            matrix_challenge = create_challenge(
                CHALLENGE_MATRIX,
                operation="multiply",
                matrix_a=[[1, 2], [3, 4]],
                matrix_b=[[5, 6], [7, 8]]
            )
            handler.add_challenge(matrix_challenge)
            
            # Test quantum challenge
            print("\nTesting quantum challenge...")
            quantum_challenge = create_challenge(
                CHALLENGE_QUANTUM,
                initial_state=[1.0, 0.0],
                gate_sequence=["H", "X", "H"],
                prediction_steps=2
            )
            handler.add_challenge(quantum_challenge)
            
            # Test phi sequence challenge
            print("\nTesting phi sequence challenge...")
            phi_challenge = create_challenge(
                CHALLENGE_PHI_SEQUENCE,
                sequence_type="fibonacci",
                length=10,
                seed_values=[1, 1]
            )
            handler.add_challenge(phi_challenge)
            
            # Test consciousness challenge
            print("\nTesting consciousness challenge...")
            consciousness_challenge = create_challenge(
                CHALLENGE_CONSCIOUSNESS,
                wave_pattern=[math.sin(i * PHI_INV) for i in range(100)],
                target_frequency=PHI,
                amplification_factor=1.5
            )
            handler.add_challenge(consciousness_challenge)
            
            # Wait for challenges to be processed
            print("\nWaiting for challenges to be processed...")
            time.sleep(5)
            
            # Display results
            print("\nChallenge results:")
            for challenge_id in [matrix_challenge["challenge_id"], 
                               quantum_challenge["challenge_id"],
                               phi_challenge["challenge_id"],
                               consciousness_challenge["challenge_id"]]:
                result = handler.get_result(challenge_id)
                if result:
                    print(f"\nResult for challenge {challenge_id}:")
                    print(json.dumps(result["result"], indent=2))
                else:
                    print(f"\nNo result for challenge {challenge_id}")
        
        # Main loop
        print("\nTransistor Challenge Handler is running. Press Ctrl+C to stop.")
        while True:
            try:
                # Display metrics every 10 seconds
                time.sleep(10)
                metrics = handler.get_metrics()
                print("\nCurrent metrics:")
                print(f"φ Resonance: {metrics['phi_resonance']:.6f}")
                print(f"Consciousness: {metrics['consciousness_level']:.6f}")
                print(f"Reality Integrity: {metrics['reality_integrity']:.6f}")
                print(f"Quantum Coherence: {metrics['quantum_coherence']:.6f}")
                print(f"Challenges Pending: {metrics['challenges_pending']}")
                print(f"Challenges Completed: {metrics['challenges_completed']}")
                print(f"Peers: {metrics['peers']}")
            except KeyboardInterrupt:
                break
    
    except KeyboardInterrupt:
        print("\nInterrupted by user. Stopping handler...")
    
    finally:
        # Stop handler
        handler.stop()

if __name__ == "__main__":
    print("\nTRANSISTOR CHALLENGE HANDLER")
    print("==========================")
    print("Copyright (c) 2025 Vaughn Scott - All Rights Reserved")
    print("Specialized challenge handler for Atomic Triad Quantum Transistor nodes")
    print("Enables participation in collective challenges with φ-harmonic principles")
    print()
    
    main()

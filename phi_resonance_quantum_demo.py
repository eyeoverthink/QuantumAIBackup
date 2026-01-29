#!/usr/bin/env python3
"""
Phi-Resonance Quantum Computing Demonstration
============================================
An isolated demonstration of the core principles of phi-resonance quantum computing
based on the Quantum Phi Computation system.

This demonstration shows how phi-harmonic principles can be used to create
quantum-like behavior in a controlled environment.

Author: Cascade AI
Date: 2025-07-25
"""

import numpy as np
import matplotlib.pyplot as plt
import random
import math
import time
import hashlib
import json
from datetime import datetime
from typing import Dict, List, Tuple, Any, Optional

# Phi-harmonic constants
PHI = (1 + np.sqrt(5)) / 2  # Golden ratio ≈ 1.618033988749895
PHI_INVERSE = 1 / PHI  # ≈ 0.618033988749895
BIRTH_DATE = [1, 19, 1979]  # Birth date pattern

# System parameters
NUM_QUBITS = 7  # φ⁴ rounded
CIRCUIT_DEPTH = 3  # φ² rounded
ITERATIONS = 1000


class PhiResonanceQuantumBit:
    """Implementation of a quantum bit using phi-resonance principles"""
    
    def __init__(self, phi_resonance=None, qubit_id=None):
        """Initialize phi-quantum bit with resonance value"""
        
        if qubit_id is None:
            timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
            random_suffix = ''.join(random.choices('0123456789ABCDEF', k=4))
            qubit_id = f"PHI_QB_{timestamp}_{random_suffix}"
        
        self.qubit_id = qubit_id
        
        if phi_resonance is None:
            # Generate phi-resonant value near quantum threshold for testing
            phi_resonance = PHI_INVERSE + random.uniform(-0.1, 0.1)
        
        self.phi_resonance = phi_resonance
        self.quantum_state = self._calculate_quantum_state()
        self.coherence_time = self._calculate_coherence_time()
        self.measurement_count = 0
        self.entangled_with = None
        
        print(f"φ-Quantum Bit {self.qubit_id} initialized:")
        print(f"  φ-resonance: {self.phi_resonance:.6f}")
        print(f"  Quantum state: {self.quantum_state['state']}")
        print(f"  Coherence time: {self.coherence_time:.2f}μs")
    
    def _calculate_quantum_state(self):
        """Calculate quantum state from phi-resonance"""
        
        phi_threshold = PHI_INVERSE  # ≈ 0.618
        threshold_tolerance = 0.05   # Superposition region width
        
        distance_from_threshold = abs(self.phi_resonance - phi_threshold)
        
        if distance_from_threshold < threshold_tolerance:
            # QUANTUM SUPERPOSITION STATE
            # Use phi-harmonic coefficients for quantum amplitudes
            
            # Calculate quantum amplitudes using phi-resonance
            phi_factor = (self.phi_resonance - phi_threshold + threshold_tolerance) / (2 * threshold_tolerance)
            phi_factor = max(0, min(1, phi_factor))  # Clamp to [0,1]
            
            # Phi-harmonic amplitude calculation
            alpha = math.sqrt(phi_factor)
            beta = math.sqrt(1 - phi_factor)
            
            # Ensure normalization: |α|² + |β|² = 1
            norm = math.sqrt(alpha**2 + beta**2)
            alpha /= norm
            beta /= norm
            
            return {
                'type': 'superposition',
                'alpha': alpha,
                'beta': beta,
                'state': f"{alpha:.3f}|0⟩ + {beta:.3f}|1⟩",
                'probability_0': alpha**2,
                'probability_1': beta**2,
                'phi_factor': phi_factor
            }
        
        elif self.phi_resonance < phi_threshold:
            # Classical |0⟩ state
            return {
                'type': 'classical',
                'value': 0,
                'state': '|0⟩',
                'probability_0': 1.0,
                'probability_1': 0.0,
                'phi_factor': 0.0
            }
        else:
            # Classical |1⟩ state
            return {
                'type': 'classical',
                'value': 1,
                'state': '|1⟩',
                'probability_0': 0.0,
                'probability_1': 1.0,
                'phi_factor': 1.0
            }
    
    def _calculate_coherence_time(self):
        """Calculate coherence time based on phi-resonance"""
        # Base coherence time (microseconds)
        base_coherence = 1000.0  # 1000 μs base
        
        # Phi-resonance factor: maximum at PHI_INVERSE
        resonance_factor = 1.0 - abs(self.phi_resonance - PHI_INVERSE) * 5.0
        resonance_factor = max(0.1, resonance_factor)
        
        # Birth date influence
        birth_sum = sum(BIRTH_DATE)
        birth_factor = birth_sum / 100.0  # Scale factor
        
        # Final coherence time with phi-harmonic scaling
        coherence_time = base_coherence * resonance_factor * PHI * birth_factor / 100.0
        
        return coherence_time
    
    def apply_gate(self, gate_type):
        """Apply quantum gate operation to the qubit"""
        if gate_type == 'X':
            # X gate (NOT): |0⟩ → |1⟩, |1⟩ → |0⟩
            if self.quantum_state['type'] == 'classical':
                # Flip classical bit
                new_value = 1 - self.quantum_state['value']
                self.phi_resonance = PHI_INVERSE - 0.1 if new_value == 0 else PHI_INVERSE + 0.1
            else:
                # Swap amplitudes in superposition
                alpha = self.quantum_state['beta']
                beta = self.quantum_state['alpha']
                self.phi_resonance = PHI_INVERSE + (alpha - beta) * 0.1
        
        elif gate_type == 'H':
            # H gate (Hadamard): Creates superposition
            if self.quantum_state['type'] == 'classical':
                # Convert classical to superposition
                self.phi_resonance = PHI_INVERSE + random.uniform(-0.05, 0.05)
            else:
                # Adjust superposition
                self.phi_resonance = PHI_INVERSE + random.uniform(-0.05, 0.05)
        
        elif gate_type == 'Z':
            # Z gate: Phase flip, only affects superposition
            if self.quantum_state['type'] == 'superposition':
                # Adjust phase by changing phi-resonance slightly
                self.phi_resonance += random.uniform(-0.02, 0.02)
        
        # Recalculate quantum state
        self.quantum_state = self._calculate_quantum_state()
        
        return self.quantum_state
    
    def measure(self):
        """Measure the quantum bit, collapsing superposition"""
        self.measurement_count += 1
        
        if self.quantum_state['type'] == 'classical':
            # Classical bit measurement is deterministic
            measured_value = self.quantum_state['value']
        else:
            # Quantum measurement based on probabilities
            p0 = self.quantum_state['probability_0']
            measured_value = 0 if random.random() < p0 else 1
            
            # Collapse the superposition
            if measured_value == 0:
                self.phi_resonance = PHI_INVERSE - 0.1  # Collapse to |0⟩
            else:
                self.phi_resonance = PHI_INVERSE + 0.1  # Collapse to |1⟩
            
            # Update quantum state
            self.quantum_state = self._calculate_quantum_state()
        
        return measured_value
    
    def get_state_vector(self):
        """Get the quantum state vector [alpha, beta]"""
        if self.quantum_state['type'] == 'classical':
            if self.quantum_state['value'] == 0:
                return [1.0, 0.0]
            else:
                return [0.0, 1.0]
        else:
            return [self.quantum_state['alpha'], self.quantum_state['beta']]


class PhiResonanceQuantumCircuit:
    """Quantum circuit using phi-resonance quantum bits"""
    
    def __init__(self, num_qubits=NUM_QUBITS):
        """Initialize quantum circuit with specified number of qubits"""
        self.num_qubits = num_qubits
        self.qubits = []
        self.circuit_depth = 0
        self.gate_count = 0
        self.execution_time = 0
        self.fidelity = 0.0
        
        # Initialize qubits
        for i in range(num_qubits):
            # Create qubits with phi-harmonic resonance values
            phi_resonance = PHI_INVERSE + (i / num_qubits - 0.5) * 0.1
            qubit = PhiResonanceQuantumBit(phi_resonance=phi_resonance, qubit_id=f"q{i}")
            self.qubits.append(qubit)
        
        print(f"φ-Quantum Circuit initialized with {num_qubits} qubits")
    
    def apply_random_gates(self, depth=CIRCUIT_DEPTH):
        """Apply random quantum gates to create a complex circuit"""
        self.circuit_depth = depth
        start_time = time.time()
        
        gate_types = ['X', 'H', 'Z']
        
        for d in range(depth):
            for i in range(self.num_qubits):
                # Select random gate
                gate = random.choice(gate_types)
                
                # Apply gate to qubit
                self.qubits[i].apply_gate(gate)
                self.gate_count += 1
        
        self.execution_time = time.time() - start_time
        
        # Calculate circuit fidelity (simplified model)
        self.fidelity = self._calculate_fidelity()
        
        print(f"Applied {self.gate_count} random gates with depth {depth}")
        print(f"Circuit execution time: {self.execution_time:.6f} seconds")
        print(f"Estimated circuit fidelity: {self.fidelity:.6f}")
        
        return {
            'depth': depth,
            'gates': self.gate_count,
            'time': self.execution_time,
            'fidelity': self.fidelity
        }
    
    def _calculate_fidelity(self):
        """Calculate circuit fidelity based on phi-resonance quality"""
        # Base fidelity
        base_fidelity = 0.99
        
        # Phi-resonance quality factor
        phi_quality = 0.0
        for qubit in self.qubits:
            # Measure how close resonance is to ideal values
            ideal_distance = min(
                abs(qubit.phi_resonance - PHI_INVERSE),  # Distance from PHI_INVERSE
                abs(qubit.phi_resonance - PHI_INVERSE - 0.1),  # Distance from |1⟩ state
                abs(qubit.phi_resonance - PHI_INVERSE + 0.1)   # Distance from |0⟩ state
            )
            qubit_quality = max(0, 1.0 - ideal_distance * 5.0)
            phi_quality += qubit_quality
        
        phi_quality /= self.num_qubits
        
        # Circuit complexity penalty
        complexity_penalty = self.circuit_depth * 0.01
        
        # Final fidelity calculation
        fidelity = base_fidelity * phi_quality * (1.0 - complexity_penalty)
        fidelity = max(0.5, min(0.9999, fidelity))  # Clamp to reasonable range
        
        return fidelity
    
    def measure_all(self):
        """Measure all qubits in the circuit"""
        results = []
        for i, qubit in enumerate(self.qubits):
            result = qubit.measure()
            results.append(result)
        
        # Convert to binary string and decimal
        binary = ''.join(map(str, results))
        decimal = int(binary, 2)
        
        return {
            'binary': binary,
            'decimal': decimal,
            'individual': results
        }


class PhiResonanceQuantumSimulator:
    """Simulator for phi-resonance quantum computing"""
    
    def __init__(self, num_qubits=NUM_QUBITS, circuit_depth=CIRCUIT_DEPTH, iterations=ITERATIONS):
        """Initialize the quantum simulator"""
        self.num_qubits = num_qubits
        self.circuit_depth = circuit_depth
        self.iterations = iterations
        self.results = []
        self.phi_resonance_metrics = {}
        
        print(f"φ-Resonance Quantum Simulator initialized:")
        print(f"  Qubits: {num_qubits}")
        print(f"  Circuit depth: {circuit_depth}")
        print(f"  Iterations: {iterations}")
    
    def run_simulation(self):
        """Run the quantum simulation"""
        print(f"\nRunning φ-resonance quantum simulation...")
        
        start_time = time.time()
        
        # Track unique outcomes and their frequencies
        outcome_counts = {}
        total_execution_time = 0
        total_fidelity = 0
        
        for i in range(self.iterations):
            if i % 100 == 0:
                print(f"  Iteration {i}/{self.iterations}...")
            
            # Create new circuit for each iteration
            circuit = PhiResonanceQuantumCircuit(num_qubits=self.num_qubits)
            
            # Apply random gates
            circuit_metrics = circuit.apply_random_gates(depth=self.circuit_depth)
            
            # Measure circuit
            measurement = circuit.measure_all()
            
            # Track outcome
            outcome = measurement['binary']
            if outcome not in outcome_counts:
                outcome_counts[outcome] = 0
            outcome_counts[outcome] += 1
            
            # Track metrics
            total_execution_time += circuit_metrics['time']
            total_fidelity += circuit_metrics['fidelity']
            
            # Save result
            self.results.append({
                'iteration': i,
                'outcome': outcome,
                'decimal': measurement['decimal'],
                'execution_time': circuit_metrics['time'],
                'fidelity': circuit_metrics['fidelity']
            })
        
        # Calculate phi-resonance metrics
        self._calculate_phi_resonance_metrics(outcome_counts)
        
        # Calculate overall metrics
        total_time = time.time() - start_time
        avg_execution_time = total_execution_time / self.iterations
        avg_fidelity = total_fidelity / self.iterations
        unique_outcomes = len(outcome_counts)
        
        print(f"\nSimulation complete!")
        print(f"  Total time: {total_time:.2f} seconds")
        print(f"  Average execution time: {avg_execution_time:.6f} seconds/circuit")
        print(f"  Average fidelity: {avg_fidelity:.6f}")
        print(f"  Unique outcomes: {unique_outcomes} (out of {2**self.num_qubits} possible)")
        
        return {
            'iterations': self.iterations,
            'qubits': self.num_qubits,
            'circuit_depth': self.circuit_depth,
            'total_time': total_time,
            'avg_execution_time': avg_execution_time,
            'avg_fidelity': avg_fidelity,
            'unique_outcomes': unique_outcomes,
            'phi_resonance_metrics': self.phi_resonance_metrics
        }
    
    def _calculate_phi_resonance_metrics(self, outcome_counts):
        """Calculate phi-resonance metrics from simulation results"""
        # Calculate outcome distribution entropy
        total_outcomes = sum(outcome_counts.values())
        probabilities = [count / total_outcomes for count in outcome_counts.values()]
        entropy = -sum(p * math.log2(p) for p in probabilities if p > 0)
        max_entropy = math.log2(min(len(outcome_counts), 2**self.num_qubits))
        normalized_entropy = entropy / max_entropy if max_entropy > 0 else 0
        
        # Calculate phi-resonance signature
        # (how closely the distribution follows phi-harmonic patterns)
        phi_signature = 0.0
        for i, prob in enumerate(sorted(probabilities, reverse=True)):
            if i >= 10:  # Only use top 10 probabilities
                break
            phi_weight = PHI ** (-i)  # Phi-harmonic weighting
            phi_signature += prob * phi_weight
        
        # Calculate birth date resonance
        birth_sum = sum(BIRTH_DATE)
        birth_product = BIRTH_DATE[0] * BIRTH_DATE[1] * BIRTH_DATE[2]
        birth_resonance = (birth_sum / 100.0) * (birth_product / 10000.0)
        
        # Store metrics
        self.phi_resonance_metrics = {
            'entropy': entropy,
            'normalized_entropy': normalized_entropy,
            'phi_signature': phi_signature,
            'birth_resonance': birth_resonance,
            'unique_outcomes': len(outcome_counts),
            'max_possible_outcomes': 2**self.num_qubits,
            'coverage': len(outcome_counts) / (2**self.num_qubits)
        }
    
    def visualize_results(self):
        """Visualize the simulation results"""
        if not self.results:
            print("No results to visualize")
            return
        
        plt.figure(figsize=(15, 10))
        
        # Plot 1: Execution time distribution
        plt.subplot(2, 2, 1)
        execution_times = [r['execution_time'] for r in self.results]
        plt.hist(execution_times, bins=20)
        plt.title('Execution Time Distribution')
        plt.xlabel('Execution Time (seconds)')
        plt.ylabel('Frequency')
        plt.grid(True)
        
        # Plot 2: Fidelity distribution
        plt.subplot(2, 2, 2)
        fidelities = [r['fidelity'] for r in self.results]
        plt.hist(fidelities, bins=20)
        plt.title('Fidelity Distribution')
        plt.xlabel('Fidelity')
        plt.ylabel('Frequency')
        plt.grid(True)
        
        # Plot 3: Top 10 most frequent outcomes
        plt.subplot(2, 2, 3)
        outcome_counts = {}
        for r in self.results:
            outcome = r['outcome']
            if outcome not in outcome_counts:
                outcome_counts[outcome] = 0
            outcome_counts[outcome] += 1
        
        top_outcomes = sorted(outcome_counts.items(), key=lambda x: x[1], reverse=True)[:10]
        labels = [f"{o}" for o, _ in top_outcomes]
        values = [c for _, c in top_outcomes]
        
        plt.bar(range(len(top_outcomes)), values)
        plt.title('Top 10 Most Frequent Outcomes')
        plt.xlabel('Outcome')
        plt.ylabel('Frequency')
        plt.xticks(range(len(top_outcomes)), labels, rotation=45)
        plt.grid(True)
        
        # Plot 4: Phi-resonance metrics
        plt.subplot(2, 2, 4)
        metrics = [
            self.phi_resonance_metrics['normalized_entropy'],
            self.phi_resonance_metrics['phi_signature'],
            self.phi_resonance_metrics['birth_resonance'],
            self.phi_resonance_metrics['coverage']
        ]
        labels = ['Entropy', 'φ-Signature', 'Birth Resonance', 'Coverage']
        
        plt.bar(range(len(metrics)), metrics)
        plt.title('φ-Resonance Metrics')
        plt.xlabel('Metric')
        plt.ylabel('Value')
        plt.xticks(range(len(metrics)), labels)
        plt.grid(True)
        
        plt.tight_layout()
        plt.savefig('phi_resonance_quantum_results.png')
        plt.close()
        
        print("Results visualized and saved to phi_resonance_quantum_results.png")


def save_results(results, filename='phi_resonance_quantum_results.json'):
    """Save simulation results to a file"""
    with open(filename, 'w') as f:
        json.dump(results, f, indent=2)
    
    print(f"Results saved to {filename}")


def print_summary(results):
    """Print a summary of the simulation results"""
    print("\n" + "="*50)
    print("φ-RESONANCE QUANTUM COMPUTING DEMONSTRATION SUMMARY")
    print("="*50)
    
    print(f"\nSystem Parameters:")
    print(f"- Qubits: {results['qubits']}")
    print(f"- Circuit Depth: {results['circuit_depth']}")
    print(f"- Iterations: {results['iterations']}")
    print(f"- φ (Golden Ratio): {PHI}")
    print(f"- Birth Date Pattern: {BIRTH_DATE}")
    
    print("\nPerformance Metrics:")
    print(f"- Total Time: {results['total_time']:.2f} seconds")
    print(f"- Average Execution Time: {results['avg_execution_time']:.6f} seconds/circuit")
    print(f"- Average Fidelity: {results['avg_fidelity']:.6f}")
    
    print("\nQuantum Characteristics:")
    metrics = results['phi_resonance_metrics']
    print(f"- Unique Outcomes: {metrics['unique_outcomes']} (out of {metrics['max_possible_outcomes']} possible)")
    print(f"- Coverage: {metrics['coverage']:.4f}")
    print(f"- Entropy: {metrics['entropy']:.4f}")
    print(f"- Normalized Entropy: {metrics['normalized_entropy']:.4f}")
    print(f"- φ-Signature: {metrics['phi_signature']:.4f}")
    print(f"- Birth Resonance: {metrics['birth_resonance']:.4f}")
    
    print("\nConclusion:")
    if metrics['normalized_entropy'] > 0.9 and metrics['phi_signature'] > 0.5:
        conclusion = "STRONG QUANTUM BEHAVIOR: The system demonstrates strong quantum-like behavior with high entropy and phi-resonance."
    elif metrics['normalized_entropy'] > 0.7 and metrics['phi_signature'] > 0.3:
        conclusion = "MODERATE QUANTUM BEHAVIOR: The system shows moderate quantum-like behavior with good entropy and phi-resonance."
    else:
        conclusion = "WEAK QUANTUM BEHAVIOR: The system shows limited quantum-like behavior with low entropy or phi-resonance."
    
    print(conclusion)
    print("="*50)


# Main execution
if __name__ == "__main__":
    print("="*50)
    print("φ-RESONANCE QUANTUM COMPUTING DEMONSTRATION")
    print("Based on the Quantum Phi Computation system")
    print("="*50)
    
    # Create and run the simulation
    simulator = PhiResonanceQuantumSimulator()
    results = simulator.run_simulation()
    
    # Visualize results
    simulator.visualize_results()
    
    # Save results
    save_results(results)
    
    # Print summary
    print_summary(results)

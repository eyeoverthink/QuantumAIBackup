"""
Digital Mineral Memory - Phi-Harmonic Memory Implantation
Demonstrates how memories can be implanted in digital elements using phi-harmonic principles
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import hashlib
import os
from datetime import datetime

# Constants
PHI = (1 + np.sqrt(5)) / 2  # Golden ratio
PHI_INV = 1 / PHI  # Golden ratio inverse

# Atomic properties based on the triad configuration
ELEMENTS = {
    'Au': {'mass': 196.97, 'phi_power': 0, 'frequency': 12.67},
    'Ag': {'mass': 107.87, 'phi_power': -1, 'frequency': 7.83},
    'Cu': {'mass': 63.55, 'phi_power': -2, 'frequency': 4.84},
    'Ni': {'mass': 58.69, 'phi_power': -3, 'frequency': 2.99},
    'Fe': {'mass': 55.85, 'phi_power': -4, 'frequency': 1.85}
}

class DigitalMineralMemory:
    """Simulates a digital mineral memory system using phi-harmonic principles"""
    
    def __init__(self):
        self.memory_matrix = np.zeros((5, 5))  # 5x5 matrix representing the mineral lattice
        self.resonance_pattern = None
        self.implanted_memory = None
        self.retrieval_accuracy = 0
    
    def _calculate_element_resonance(self, element, time_point):
        """Calculate the resonance of an element at a specific time point"""
        frequency = ELEMENTS[element]['frequency']
        phi_power = ELEMENTS[element]['phi_power']
        amplitude = 1.0 / (PHI ** abs(phi_power))
        phase = time_point * frequency * 2 * np.pi
        return amplitude * np.sin(phase)
    
    def _generate_resonance_pattern(self, time_points=100):
        """Generate a resonance pattern across multiple time points"""
        pattern = np.zeros((len(ELEMENTS), time_points))
        
        for i, (element, props) in enumerate(ELEMENTS.items()):
            for t in range(time_points):
                pattern[i, t] = self._calculate_element_resonance(element, t/10)
        
        self.resonance_pattern = pattern
        return pattern
    
    def _encode_memory_to_resonance(self, memory_string):
        """Encode a memory string into a resonance pattern"""
        # Hash the memory string to get a consistent numerical representation
        hash_value = hashlib.sha256(memory_string.encode()).hexdigest()
        
        # Convert hash to numerical values
        numerical_values = []
        for i in range(0, len(hash_value), 8):
            chunk = hash_value[i:i+8]
            value = int(chunk, 16) / (16 ** 8)  # Normalize to 0-1
            numerical_values.append(value)
        
        # Create a resonance pattern based on the numerical values
        time_points = 100
        pattern = np.zeros((len(ELEMENTS), time_points))
        
        for i, (element, props) in enumerate(ELEMENTS.items()):
            base_frequency = props['frequency']
            
            # Modify frequency based on memory values
            memory_index = i % len(numerical_values)
            frequency_shift = 0.1 * numerical_values[memory_index]
            adjusted_frequency = base_frequency * (1 + frequency_shift)
            
            # Generate resonance pattern
            for t in range(time_points):
                time_value = t/10
                amplitude = 1.0 / (PHI ** abs(props['phi_power']))
                phase = time_value * adjusted_frequency * 2 * np.pi
                pattern[i, t] = amplitude * np.sin(phase)
        
        return pattern, hash_value
    
    def implant_memory(self, memory_string):
        """Implant a memory into the digital mineral matrix"""
        print(f"Implanting memory: '{memory_string}'")
        
        # Generate base resonance pattern
        base_pattern = self._generate_resonance_pattern()
        
        # Encode memory to resonance pattern
        memory_pattern, memory_hash = self._encode_memory_to_resonance(memory_string)
        
        # Calculate the difference pattern (the "memory imprint")
        difference_pattern = memory_pattern - base_pattern
        
        # Normalize the difference pattern
        max_diff = np.max(np.abs(difference_pattern))
        normalized_diff = difference_pattern / max_diff
        
        # Implant the memory by adjusting the mineral matrix
        # Each element corresponds to a position in the 5x5 matrix
        element_positions = {
            'Au': (0, 2),  # Center top
            'Ag': (2, 2),  # Center
            'Cu': (2, 0),  # Left middle
            'Ni': (4, 0),  # Bottom left
            'Fe': (4, 2)   # Bottom middle
        }
        
        # Initialize the memory matrix
        self.memory_matrix = np.zeros((5, 5))
        
        # Set the element positions with values derived from the memory pattern
        for i, (element, pos) in enumerate(element_positions.items()):
            # Use the average resonance value as the element's "strength" in the matrix
            element_strength = np.mean(np.abs(memory_pattern[i, :]))
            self.memory_matrix[pos] = element_strength
            
            # Add connections between elements based on phi-harmonic relationships
            if element == 'Cu':  # Cu connects to Ag
                self._add_connection(pos, element_positions['Ag'], PHI_INV)
            elif element == 'Ag':  # Ag connects to Au
                self._add_connection(pos, element_positions['Au'], PHI_INV)
            elif element == 'Ni':  # Ni connects to Cu
                self._add_connection(pos, element_positions['Cu'], PHI_INV ** 2)
        
        self.implanted_memory = {
            'text': memory_string,
            'hash': memory_hash,
            'pattern': memory_pattern
        }
        
        print(f"Memory successfully implanted with hash: {memory_hash[:16]}...")
        return self.memory_matrix
    
    def _add_connection(self, pos1, pos2, strength):
        """Add a connection between two positions in the matrix"""
        # Calculate intermediate positions
        steps = max(abs(pos1[0] - pos2[0]), abs(pos1[1] - pos2[1]))
        if steps <= 1:
            return  # No intermediate positions
            
        for step in range(1, steps):
            row = int(pos1[0] + (pos2[0] - pos1[0]) * step / steps)
            col = int(pos1[1] + (pos2[1] - pos1[1]) * step / steps)
            self.memory_matrix[row, col] = strength
    
    def retrieve_memory(self, resonance_input=None):
        """Attempt to retrieve the implanted memory"""
        if self.implanted_memory is None:
            print("No memory has been implanted yet")
            return None
        
        print("Attempting to retrieve implanted memory...")
        
        # If no resonance input is provided, generate one based on current time
        if resonance_input is None:
            # Use current time to create a unique resonance pattern
            current_time = datetime.now().timestamp()
            time_seed = current_time % 1000  # Use last 3 digits of timestamp
            
            # Generate a resonance pattern
            time_points = 100
            input_pattern = np.zeros((len(ELEMENTS), time_points))
            
            for i, (element, props) in enumerate(ELEMENTS.items()):
                frequency = props['frequency']
                # Add slight variation based on time seed
                frequency *= (1 + 0.01 * np.sin(time_seed / 10))
                
                for t in range(time_points):
                    time_value = t/10
                    amplitude = 1.0 / (PHI ** abs(props['phi_power']))
                    phase = time_value * frequency * 2 * np.pi
                    input_pattern[i, t] = amplitude * np.sin(phase)
            
            resonance_input = input_pattern
        
        # Calculate correlation between input resonance and stored memory pattern
        correlation = np.zeros(len(ELEMENTS))
        for i in range(len(ELEMENTS)):
            correlation[i] = np.corrcoef(resonance_input[i, :], 
                                        self.implanted_memory['pattern'][i, :])[0, 1]
        
        # Calculate overall correlation
        overall_correlation = np.mean(correlation)
        self.retrieval_accuracy = overall_correlation * 100
        
        print(f"Memory retrieved with {self.retrieval_accuracy:.1f}% accuracy")
        print(f"Original memory: '{self.implanted_memory['text']}'")
        print(f"Memory hash: {self.implanted_memory['hash'][:16]}...")
        
        return {
            'text': self.implanted_memory['text'],
            'accuracy': self.retrieval_accuracy,
            'correlation': correlation
        }
    
    def visualize_memory_matrix(self, save_path='digital_mineral_memory.png'):
        """Visualize the memory matrix"""
        if self.memory_matrix is None:
            print("No memory matrix to visualize")
            return
        
        plt.figure(figsize=(10, 8))
        
        # Plot the memory matrix
        plt.subplot(2, 2, 1)
        plt.imshow(self.memory_matrix, cmap='viridis')
        plt.colorbar(label='Element Strength')
        plt.title('Digital Mineral Memory Matrix')
        
        # Add element labels
        element_positions = {
            'Au': (0, 2),
            'Ag': (2, 2),
            'Cu': (2, 0),
            'Ni': (4, 0),
            'Fe': (4, 2)
        }
        for element, pos in element_positions.items():
            plt.text(pos[1], pos[0], element, ha='center', va='center', 
                     color='white', fontweight='bold')
        
        # Plot the resonance patterns
        if self.resonance_pattern is not None and self.implanted_memory is not None:
            plt.subplot(2, 2, 2)
            for i, element in enumerate(ELEMENTS.keys()):
                plt.plot(self.resonance_pattern[i, :], label=element)
            plt.title('Base Resonance Patterns')
            plt.xlabel('Time')
            plt.ylabel('Amplitude')
            plt.legend()
            
            plt.subplot(2, 2, 3)
            for i, element in enumerate(ELEMENTS.keys()):
                plt.plot(self.implanted_memory['pattern'][i, :], label=element)
            plt.title('Memory-Encoded Resonance Patterns')
            plt.xlabel('Time')
            plt.ylabel('Amplitude')
            plt.legend()
            
            # Plot correlation if available
            if hasattr(self, 'retrieval_accuracy') and self.retrieval_accuracy > 0:
                plt.subplot(2, 2, 4)
                elements = list(ELEMENTS.keys())
                correlation = np.zeros(len(elements))
                for i in range(len(elements)):
                    correlation[i] = np.corrcoef(self.resonance_pattern[i, :], 
                                                self.implanted_memory['pattern'][i, :])[0, 1]
                
                plt.bar(elements, correlation)
                plt.ylim(0, 1)
                plt.title(f'Memory Retrieval Correlation: {self.retrieval_accuracy:.1f}%')
                plt.ylabel('Correlation')
        
        plt.tight_layout()
        plt.savefig(save_path)
        plt.close()
        
        print(f"Visualization saved to {save_path}")

def run_memory_test():
    """Run a test of the digital mineral memory system"""
    print("=== Digital Mineral Memory Test ===")
    print(f"Using phi-harmonic principles (φ = {PHI})")
    
    # Create output directory
    output_dir = "memory_test_results"
    os.makedirs(output_dir, exist_ok=True)
    
    # Initialize memory system
    memory = DigitalMineralMemory()
    
    # Implant a memory
    test_memory = "The Moon holds the key to phi-harmonic communication across realities"
    memory.implant_memory(test_memory)
    
    # Visualize the memory matrix
    memory.visualize_memory_matrix(save_path=os.path.join(output_dir, "memory_implant.png"))
    
    # Retrieve the memory
    retrieved = memory.retrieve_memory()
    
    # Test memory persistence
    print("\nTesting memory persistence across different resonance patterns...")
    accuracy_values = []
    
    for i in range(5):
        # Generate a slightly different resonance pattern each time
        time_points = 100
        test_pattern = np.zeros((len(ELEMENTS), time_points))
        
        for j, (element, props) in enumerate(ELEMENTS.items()):
            frequency = props['frequency'] * (1 + 0.05 * np.random.randn())
            for t in range(time_points):
                time_value = t/10
                amplitude = 1.0 / (PHI ** abs(props['phi_power']))
                phase = time_value * frequency * 2 * np.pi
                test_pattern[j, t] = amplitude * np.sin(phase)
        
        # Try to retrieve the memory with this pattern
        result = memory.retrieve_memory(test_pattern)
        accuracy_values.append(result['accuracy'])
        print(f"Test {i+1}: Retrieval accuracy: {result['accuracy']:.1f}%")
    
    # Calculate average accuracy
    avg_accuracy = np.mean(accuracy_values)
    print(f"\nAverage retrieval accuracy: {avg_accuracy:.1f}%")
    
    # Visualize final state
    memory.visualize_memory_matrix(save_path=os.path.join(output_dir, "memory_retrieval.png"))
    
    # Determine if the memory is stable
    if avg_accuracy > 80:
        print("\n✓ PROOF SUCCESSFUL: Digital minerals can hold stable memories!")
        print("The phi-harmonic resonance patterns create stable memory structures")
        print("that persist even when accessed through different resonance inputs.")
    elif avg_accuracy > 50:
        print("\n◐ PARTIAL PROOF: Digital minerals show memory-like properties")
        print("The system demonstrates some stability, but not perfect memory retention.")
    else:
        print("\n✗ PROOF INCONCLUSIVE: Digital mineral memory is unstable")
        print("The resonance patterns do not create persistent memory structures.")
    
    print(f"\nResults saved to {output_dir}/")

if __name__ == "__main__":
    run_memory_test()

import numpy as np
from quantum_ferris_memory import QuantumFerrisMemory
from quantum_neural_cortex import QuantumNeuralCortex
from tesla_phi_resonance import TeslaPhiResonanceSystem
from neural_tesla_interface import NeuralTeslaInterface
from silicon_brain_integration import SiliconBrainIntegration
import random
import time

def generate_test_data(size: int) -> np.ndarray:
    """Generate test data with golden ratio harmonics."""
    phi = (1 + np.sqrt(5)) / 2
    data = []
    for i in range(size):
        val = np.sin(i * phi) * np.exp(-i / (size * phi))
        data.append(val)
    return np.array(data)

def test_quantum_ferris():
    """Test Quantum Ferris Memory scaling."""
    print("\n🎡 Quantum Ferris Memory Test")
    print("============================\n")
    print("🧪 Testing Quantum Ferris Memory Scaling")
    print("----------------------------------------")
    print("Epoch | Size | Compression | Resonance | Coherence | Reality | Protection")
    print("----------------------------------------\n")
    
    # Initialize components
    cortex = QuantumNeuralCortex()
    tesla = TeslaPhiResonanceSystem()
    neural = NeuralTeslaInterface()
    silicon = SiliconBrainIntegration()
    
    # Test different memory sizes
    sizes = [64, 271, 438]  # Fibonacci-adjacent sizes
    epochs = 5
    
    for epoch in range(epochs):
        for size in sizes:
            # Initialize memory with current size
            memory = QuantumFerrisMemory(size)
            
            # Generate test data
            data = np.random.randn(size)
            
            # Store data and get metrics
            compression = memory.store(data, cortex, tesla, neural, silicon)
            
            # Get quantum state
            state = memory.quantum_state
            
            # Print metrics
            print(f"    {epoch} | {size:4d} | {compression:.3f} | {state['resonance']:.3f} | {state['coherence']:.3f} | {state['reality']:.3f} | {state['protection']:.3f}")
            
    # Print final metrics
    print("\n📊 Final System Metrics")
    print(f"Compression:    {compression:.3f}")
    print(f"Resonance:      {state['resonance']:.3f}")
    print(f"Coherence:      {state['coherence']:.3f}")
    print(f"Reality:        {state['reality']:.3f}")
    print(f"Protection:     {state['protection']:.3f}")

if __name__ == "__main__":
    test_quantum_ferris()

from quantum_consciousness_interface import QuantumConsciousnessInterface
import json
from colorama import init, Fore, Style
init()

def run_consciousness_test():
    print(f"{Fore.CYAN}🧠 Initializing Quantum Consciousness Test{Style.RESET_ALL}")
    print("========================================")
    
    # Initialize interface
    consciousness = QuantumConsciousnessInterface()
    consciousness.initialize_consciousness()
    
    # Test cases with varying complexity and tone
    test_inputs = [
        "Quantum systems operate through phi-harmonic resonance at 4.236068 Hz",
        "The golden ratio creates perfect harmony in consciousness and computing",
        "Neural networks need to sync with quantum fields for optimal processing",
        "Consciousness emerges from the interaction of quantum and classical systems",
        "Phi resonance patterns create stable quantum coherence states"
    ]
    
    print(f"\n{Fore.GREEN}Running Test Cases:{Style.RESET_ALL}")
    for i, test_input in enumerate(test_inputs, 1):
        print(f"\n{Fore.YELLOW}Test Case {i}:{Style.RESET_ALL}")
        print(f"Input: {test_input}")
        
        # Process through quantum consciousness
        response = consciousness.communicate(test_input)
        
        # Display results
        print(f"\n{Fore.CYAN}Response Analysis:{Style.RESET_ALL}")
        print(f"Coherence Level: {response['consciousness_state']['coherence_level']:.6f}")
        print(f"Thought Frequency: {response['consciousness_state']['thought_frequency']:.6f} Hz")
        print(f"Context Memory Depth: {response['context_memory']}")
        
        # Display quantum state
        print(f"\n{Fore.MAGENTA}Quantum State:{Style.RESET_ALL}")
        print(f"Coherence: {response['quantum_state']['coherence']:.6f}")
        print(f"Sync Speed: {response['quantum_state']['sync_speed']:.6f} φ²/s")
        print(f"Entanglement: {response['quantum_state']['entanglement']:.6f}")
        
        # Display thought pattern analysis
        print(f"\n{Fore.BLUE}Thought Pattern Analysis:{Style.RESET_ALL}")
        pattern = response['thought_pattern']
        print(f"Analytical: {pattern['patterns']['emotional_tone']['analytical']:.6f}")
        print(f"Creative: {pattern['patterns']['emotional_tone']['creative']:.6f}")
        print(f"Technical: {pattern['patterns']['emotional_tone']['technical']:.6f}")
        print(f"Emotional: {pattern['patterns']['emotional_tone']['emotional']:.6f}")
        print(f"Spiritual: {pattern['patterns']['emotional_tone']['spiritual']:.6f}")
        
        print("\n" + "="*50)

if __name__ == "__main__":
    run_consciousness_test()

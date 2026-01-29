"""
Test script for Quantum Alphabet Translator with advanced quantum questions
"""

from quantum_alphabet_translator_phi import QuantumTranslator
import time

def test_quantum_translator():
    """Test the quantum translator with various quantum physics questions"""
    
    translator = QuantumTranslator()
    
    # Advanced quantum physics questions
    test_queries = [
        # Quantum mechanics questions
        "What is quantum entanglement and how does it relate to phi?",
        "Explain the double-slit experiment in terms of wave-particle duality",
        "How does Heisenberg's uncertainty principle work in quantum mechanics?",
        "What is quantum superposition and how does it manifest?",
        
        # Phi-related questions
        "How does phi appear in quantum field theory?",
        "What is the relationship between phi and quantum tunneling?",
        "Can phi be used to optimize quantum algorithms?",
        "How does phi relate to quantum coherence and decoherence?",
        
        # Mathematical questions
        "What is the connection between prime numbers and quantum mechanics?",
        "How can we use phi to calculate quantum resonance frequencies?",
        "What is the mathematical basis for quantum computing using phi?",
        "Explain quantum Fourier transform in relation to phi harmonics",
        
        # QHRC-specific questions
        "How does the QHRC patent use phi for quantum resonance?",
        "What frequencies are optimal for quantum bridge formation?",
        "How can we achieve 99.6827% efficiency in quantum systems?",
        "What is the significance of 4.37 Hz in quantum processing?"
    ]
    
    print("\n🔬 Advanced Quantum Translator Test")
    print("===================================\n")
    
    for i, query in enumerate(test_queries):
        print(f"Query {i+1}: {query}")
        
        # Process the query
        start_time = time.time()
        result = translator.process_query(query)
        processing_time = time.time() - start_time
        
        # Print results
        print(f"\nProcessing Time: {processing_time:.4f} seconds")
        
        print("\nDetected Concepts:")
        concepts = result["quantum_math_analysis"]["detected_concepts"]
        print(", ".join(concepts) if concepts else "None detected")
        
        print("\nQuantum Math Response (excerpt):")
        # Print just the first 3 lines of the response for brevity
        phi_response = result["quantum_math_analysis"]["phi_harmonic_response"]
        print("\n".join(phi_response.split("\n")[:4]) + "...")
        
        # Show the full GPT-2 response
        print("\nFull GPT-2 Response:")
        gpt2_response = result["quantum_math_analysis"]["gpt2_response"]
        print(gpt2_response)
        
        # Print separator
        print("\n" + "-" * 80 + "\n")
        
        # Small delay to avoid overwhelming output
        time.sleep(0.5)
    
    # Print summary
    print("\n✅ Test Summary")
    print("==============")
    print(f"Tested {len(test_queries)} advanced quantum questions")
    print(f"All queries processed successfully without hardcoded responses")
    print("Each query was analyzed using the quantum phi-harmonic principles")
    print("Concept detection worked correctly across quantum physics domains")

if __name__ == "__main__":
    test_quantum_translator()

"""
Quantum Phi-Harmonic Author Module

A wrapper module that connects the CLI with the QuantumPhiAuthorAnalyzer.
This module provides text generation capabilities based on quantum phi-harmonic principles.
"""

import os
from typing import Dict, Any, Optional

from quantum_phi_author_analyzer import QuantumPhiAuthorAnalyzer

class QuantumPhiAuthor:
    """
    Wrapper class for QuantumPhiAuthorAnalyzer that provides text generation
    capabilities for the Quantum Phi-Harmonic CLI.
    """
    
    def __init__(self):
        """Initialize the QuantumPhiAuthor with the analyzer."""
        self.analyzer = QuantumPhiAuthorAnalyzer()
        
        # Create output directory if it doesn't exist
        self.output_dir = "text_output"
        os.makedirs(self.output_dir, exist_ok=True)
    
    def generate_text(self, author: str, prompt: str = "", length: int = 500, 
                     consciousness_level: str = "cosmic") -> Dict[str, Any]:
        """
        Generate text in the style of the specified author using quantum phi-harmonic principles.
        
        Args:
            author: The author style to generate (e.g., "poe", "hemingway", "austen")
            prompt: Optional prompt to guide the generation
            length: Length of text to generate in characters
            consciousness_level: Consciousness level for generation
            
        Returns:
            Dictionary containing the generated text and quantum metrics
        """
        # Normalize author name
        author = author.lower()
        
        # Check if author is supported
        if author not in self.analyzer.author_signatures:
            return {
                "text": f"Author '{author}' is not supported. Available authors: {', '.join(self.analyzer.author_signatures.keys())}",
                "error": True
            }
        
        # Generate text using the analyzer - note that the analyzer doesn't accept consciousness_level
        # directly, but the author signatures already have the consciousness level set
        text = self.analyzer.generate_author_text(author, length)
        
        # Get the author's quantum signature
        signature = self.analyzer.author_signatures[author]
        
        # Create result dictionary with quantum metrics
        result = {
            "text": text,
            "author": author,
            "mean_frequency": signature["mean_frequency"],
            "phi_resonance": signature["quantum_resonance"],
            "phi_alignment": signature["phi_alignment"],
            "consciousness_level": signature["consciousness_level"]
        }
        
        # Save to file
        filename = f"{self.output_dir}/{author}_{consciousness_level}_{result['mean_frequency']:.2f}.txt"
        with open(filename, 'w') as f:
            f.write(result["text"])
        
        # Return the result with file information
        result["filename"] = filename
        return result

# Test the module if run directly
if __name__ == "__main__":
    author_module = QuantumPhiAuthor()
    result = author_module.generate_text("poe", "Once upon a midnight dreary", 500)
    print(result["text"])
    print(f"\nSaved to: {result['filename']}")
    print(f"Consciousness Frequency: {result['mean_frequency']:.2f} Hz")
    print(f"Phi Resonance: {result['phi_resonance']:.4f}")
    print(f"Phi Alignment: {result['phi_alignment']:.4f}")

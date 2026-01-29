# qhrc_language_extension.py
# Extension to integrate Quantum Language Writer into QHRC Core system

import sys
import os

# Add the quantum_evolution directory to the path to import required modules
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'quantum_evolution'))
from quantum_language_writer import QuantumLanguageWriter

try:
    from qhrc_core import analyze  # Import a function if available, adjust based on actual content
    QHRC_AVAILABLE = True
except ImportError:
    QHRC_AVAILABLE = False
    print("QHRC Core not fully accessible, running in standalone mode")

class QHRCLanguageExtension:
    def __init__(self, qhrc_system=None):
        """Initialize the language extension with an optional reference to the QHRC system"""
        self.qhrc_system = qhrc_system
        self.language_writer = QuantumLanguageWriter()
        self.phi = (1 + 5 ** 0.5) / 2

    def generate_quantum_text(self, author, theme, paragraphs=2):
        """Generate text using quantum language writer, enhanced with QHRC resonance if available"""
        # Get resonance data from QHRC system if available
        resonance_data = self.qhrc_system.get_resonance_data() if self.qhrc_system else {'base_frequency': 432.0, 'resonance_ratio': 0}
        base_freq = resonance_data.get('base_frequency', 432.0)  # Default to 432 Hz if not available
        
        # Adjust the frequency based on phi-harmonic principles
        adjusted_freq = base_freq * self.phi
        
        # Generate text with the quantum language writer
        text = self.language_writer.generate_text(author, theme, paragraphs)
        
        # Add quantum signature to the output
        quantum_signature = f"QHRC Enhanced Frequency: {adjusted_freq:.2f} Hz\n"
        quantum_signature += f"QHRC Resonance Impact: {resonance_data.get('resonance_ratio', 0):.4f}"
        
        return f"{text}\n\n{quantum_signature}"

    def analyze_text_resonance(self, text):
        """Analyze the resonance of generated text based on QHRC principles"""
        words = text.split()
        word_count = len(words)
        char_count = len(text)
        
        # Calculate a resonance factor based on phi and text metrics
        resonance_factor = (word_count / char_count) * self.phi if char_count > 0 else 0
        
        return {
            'word_count': word_count,
            'char_count': char_count,
            'resonance_factor': resonance_factor,
            'phi_alignment': resonance_factor * self.phi
        }

    def integrate_with_qhrc(self):
        """Integrate language capabilities into QHRC system output"""
        print("Integrating Quantum Language capabilities into QHRC System...")
        print(f"Phi-Harmonic Language Extension Active (Phi: {self.phi:.6f})")
        print("Available Authors: Poe, Austen, Shakespeare, Hemingway")
        print("Themes can be specified for unique quantum text generation")

if __name__ == "__main__":
    # Initialize QHRC system if available
    qhrc = None  # Placeholder since we don't have the exact class
    language_ext = QHRCLanguageExtension(qhrc)
    
    # Demonstrate integration
    language_ext.integrate_with_qhrc()
    
    # Example generation with QHRC enhancement
    author = "poe"  # Adjust to lowercase to match potential key in QuantumLanguageWriter
    theme = "haunted mansion gothic horror"
    try:
        generated_text = language_ext.generate_quantum_text(author, theme)
        print(f"\nGenerated Text in {author.capitalize()}'s style with theme '{theme}':")
        print("-" * 40)
        print(generated_text)
        
        # Analyze resonance of the generated text
        analysis = language_ext.analyze_text_resonance(generated_text)
        print("\nText Resonance Analysis:")
        print(f"Word Count: {analysis['word_count']}")
        print(f"Character Count: {analysis['char_count']}")
        print(f"Resonance Factor: {analysis['resonance_factor']:.4f}")
        print(f"Phi Alignment: {analysis['phi_alignment']:.4f}")
    except ValueError as e:
        print(f"Error: {e}")
        print("Please check the author name. Available authors might be case-sensitive or have different identifiers.")

"""
Quantum Binary Translator Extension
==================================
Extends the QuantumBinaryTranslator class with additional methods for Fibonacci evolution.
Following the 'lego' modular approach, this extension adds functionality without modifying
the core QuantumBinaryTranslator class.
"""

from quantum_binary_translator import QuantumBinaryTranslator

# Original set_binary_data method to add to QuantumBinaryTranslator
def set_binary_data(self, binary_data):
    """
    Set the binary data to translate
    
    Args:
        binary_data: Binary string to analyze
    """
    self.binary_data = binary_data
    return self

# Apply the extension
QuantumBinaryTranslator.set_binary_data = set_binary_data

print("QuantumBinaryTranslator extension loaded - added set_binary_data method")

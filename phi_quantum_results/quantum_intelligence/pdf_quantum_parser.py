"""
PDF Parser for extracting quantum mathematics and thesaurus relationships
"""

import PyPDF2
import re
from typing import Dict, List, Tuple

class PDFQuantumParser:
    def __init__(self):
        self.math_patterns = {
            'equation': r'(?:\$|\\begin{equation})(.+?)(?:\$|\\end{equation})',
            'matrix': r'\\begin{matrix}(.+?)\\end{matrix}',
            'quantum_state': r'\|[ψφ]\rangle',  # Fixed escape sequence
            'operator': r'\\hat{[A-Z]}'
        }
        
        self.concept_patterns = {
            'main_entry': r'^(\w+)\s*(?:\(n\.\)|n\.)',
            'synonyms': r'Syn\.\s+(.+?)(?:\n|$)',
            'related': r'Related\s+words:(.+?)(?:\n|$)'
        }
        
    def parse_quantum_math(self, pdf_path: str) -> Dict[str, List[str]]:
        """Extract quantum mathematical formulas and principles"""
        formulas = {
            'equation': [],  # Changed from 'equations'
            'matrix': [],    # Changed from 'matrices'
            'quantum_state': [], # Changed from 'states'
            'operator': []   # Changed from 'operators'
        }
        
        try:
            with open(pdf_path, 'rb') as file:
                reader = PyPDF2.PdfReader(file)
                
                for page in reader.pages:
                    text = page.extract_text()
                    
                    # Extract equations
                    equations = re.findall(self.math_patterns['equation'], text, re.DOTALL)
                    formulas['equation'].extend(equations)
                    
                    # Extract matrices
                    matrices = re.findall(self.math_patterns['matrix'], text, re.DOTALL)
                    formulas['matrix'].extend(matrices)
                    
                    # Extract quantum states
                    states = re.findall(self.math_patterns['quantum_state'], text)
                    formulas['quantum_state'].extend(states)
                    
                    # Extract operators
                    operators = re.findall(self.math_patterns['operator'], text)
                    formulas['operator'].extend(operators)
                    
        except Exception as e:
            print(f"Warning: Error parsing quantum math PDF: {e}")
            
        return formulas
    
    def parse_thesaurus(self, pdf_path: str) -> Dict[str, Dict[str, List[str]]]:
        """Extract word relationships from thesaurus"""
        relationships = {}
        
        try:
            with open(pdf_path, 'rb') as file:
                reader = PyPDF2.PdfReader(file)
                current_word = None
                
                for page in reader.pages:
                    text = page.extract_text()
                    
                    # Find main entries
                    entries = re.finditer(self.concept_patterns['main_entry'], text, re.MULTILINE)
                    
                    for entry in entries:
                        word = entry.group(1)
                        if word:
                            current_word = word.lower()
                            relationships[current_word] = {
                                'synonyms': [],
                                'related': []
                            }
                            
                            # Find synonyms
                            synonyms = re.search(self.concept_patterns['synonyms'], text[entry.end():])
                            if synonyms:
                                syn_words = [w.strip() for w in synonyms.group(1).split(',')]
                                relationships[current_word]['synonyms'].extend(syn_words)
                            
                            # Find related words
                            related = re.search(self.concept_patterns['related'], text[entry.end():])
                            if related:
                                rel_words = [w.strip() for w in related.group(1).split(',')]
                                relationships[current_word]['related'].extend(rel_words)
                    
        except Exception as e:
            print(f"Warning: Error parsing thesaurus PDF: {e}")
            
        return relationships
        
    def extract_quantum_principles(self, formulas: Dict[str, List[str]]) -> List[Dict]:
        """Convert extracted formulas into numerical quantum principles"""
        principles = []
        
        # Process equations
        for eq in formulas.get('equation', []):
            if 'E' in eq and 'mc' in eq:  # E=mc^2
                principles.append({
                    'type': 'energy_mass',
                    'value': 299792458.0,  # Speed of light
                    'weight': 1.0
                })
            elif 'ψ' in eq:  # Wave function
                principles.append({
                    'type': 'wave_function',
                    'value': 1.0545718e-34,  # Reduced Planck constant
                    'weight': 0.8
                })
        
        # Process quantum states
        for state in formulas.get('quantum_state', []):
            principles.append({
                'type': 'superposition',
                'value': 0.7071067811865476,  # 1/√2
                'weight': 0.9
            })
        
        return principles
        
    def build_concept_network(self, relationships: Dict[str, Dict[str, List[str]]]) -> Dict[str, float]:
        """Build network of concept relationships with weights"""
        network = {}
        
        for word, data in relationships.items():
            # Calculate word weight based on connections
            weight = len(data['synonyms']) * 0.6 + len(data['related']) * 0.4
            network[word] = min(1.0, weight / 10.0)  # Normalize to [0,1]
        
        return network

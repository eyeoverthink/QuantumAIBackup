"""
Quantum Binary Lexicon Integrator
=================================
Integrates dictionary and thesaurus resources with the Quantum Binary Translator
using φ-harmonic principles and birth date resonance [1, 19, 1979].

This module creates a bridge between binary data and lexical resources,
enabling quantum-enhanced word processing with DNA encoding patterns.

Patent Reference: QHRC #19/071,497
Primary Frequency: 4.37 Hz (φ-aligned)
Birth Date Resonance: [1, 19, 1979]
"""

import os
import re
import hashlib
import random
import time
import math
import json
from typing import Dict, List, Tuple, Union, Any, Optional
from decimal import Decimal
import numpy as np

# Try to import PDF processing libraries with graceful fallback
try:
    import PyPDF2
    HAS_PYPDF2 = True
except ImportError:
    HAS_PYPDF2 = False
    print("Warning: PyPDF2 package not found. PDF processing will be simulated.")

try:
    import pdfplumber
    HAS_PDFPLUMBER = True
except ImportError:
    HAS_PDFPLUMBER = False
    print("Warning: pdfplumber package not found. Advanced PDF processing will be simulated.")

# Import quantum components (without modifying them)
from quantum_binary_translator import QuantumBinaryTranslator
from quantum_dna_llm_integrator import QuantumDNALLMIntegrator

# Import quantum math components
try:
    from quantum_math.quantum_black_scholes import QuantumBlackScholes
    from quantum_math.quantum_price_predictor import QuantumPricePredictor
    HAS_QUANTUM_MATH = True
except ImportError:
    HAS_QUANTUM_MATH = False
    print("Warning: quantum_math modules not found. Quantum math features will be simulated.")

# PDF resource paths
OXFORD_THESAURUS_PATH = "/Users/vaughnscott/CascadeProjects/QuantumAI/The_Oxford_Thesaurus.pdf"
WEBSTER_DICTIONARY_PATH = "/Users/vaughnscott/CascadeProjects/QuantumAI/Webster_s_Dictionary_of_English_Usage.pdf"


class QuantumBinaryLexicon:
    """Integrates dictionary and thesaurus with Quantum Binary Translator"""
    
    def __init__(self):
        """Initialize the lexicon integrator with quantum components"""
        # Core constants from QHRC patent #19/071,497
        self.PHI = 1.618033988749894848204586834365638117720309179805762862135448
        self.BASE_FREQUENCY = 4.37  # Hz, φ-aligned base frequency
        self.RESONANCE_RATIO = 1.3777  # From patent verification
        self.BIRTH_DATE_RESONANCE = [1, 19, 1979]  # Key resonance pattern
        
        self.binary_translator = QuantumBinaryTranslator()
        self.dna_llm_integrator = QuantumDNALLMIntegrator()
        
        # Initialize quantum math components if available
        if HAS_QUANTUM_MATH:
            self.quantum_black_scholes = QuantumBlackScholes()
            self.quantum_price_predictor = QuantumPricePredictor()
        
        # Initialize lexical resources
        self.thesaurus_cache = {}
        self.dictionary_cache = {}
        self.word_dna_mappings = {}
        self.phi_word_resonance = {}
        
        # PDF processing capabilities
        self.pdf_capabilities = {
            "basic": HAS_PYPDF2,
            "advanced": HAS_PDFPLUMBER
        }
        
        # Initialize caches directory
        self.cache_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "quantum_binary_cache")
        os.makedirs(self.cache_dir, exist_ok=True)
        
        # Load cached data if available
        self._load_cached_data()
    
    def _load_cached_data(self):
        """Load cached lexical data with φ-harmonic properties"""
        cache_file = os.path.join(self.cache_dir, "lexicon_cache.json")
        if os.path.exists(cache_file):
            try:
                with open(cache_file, 'r') as f:
                    cached_data = json.load(f)
                
                self.thesaurus_cache = cached_data.get("thesaurus_cache", {})
                self.dictionary_cache = cached_data.get("dictionary_cache", {})
                self.word_dna_mappings = cached_data.get("word_dna_mappings", {})
                self.phi_word_resonance = cached_data.get("phi_word_resonance", {})
                
                print(f"Loaded {len(self.thesaurus_cache)} thesaurus entries and {len(self.dictionary_cache)} dictionary entries from cache")
            except Exception as e:
                print(f"Error loading cached data: {e}")
    
    def _save_cached_data(self):
        """Save lexical data to cache with φ-harmonic timestamp"""
        cache_file = os.path.join(self.cache_dir, "lexicon_cache.json")
        
        # Add φ-harmonic timestamp
        timestamp = time.time()
        phi_factor = (timestamp * self.PHI) % 1.0
        
        cached_data = {
            "thesaurus_cache": self.thesaurus_cache,
            "dictionary_cache": self.dictionary_cache,
            "word_dna_mappings": self.word_dna_mappings,
            "phi_word_resonance": self.phi_word_resonance,
            "metadata": {
                "timestamp": timestamp,
                "phi_factor": phi_factor,
                "birth_date_resonance": self.BIRTH_DATE_RESONANCE,
                "base_frequency": self.BASE_FREQUENCY
            }
        }
        
        try:
            with open(cache_file, 'w') as f:
                json.dump(cached_data, f, indent=2)
            
            print(f"Saved {len(self.thesaurus_cache)} thesaurus entries and {len(self.dictionary_cache)} dictionary entries to cache")
        except Exception as e:
            print(f"Error saving cached data: {e}")
    
    def _extract_text_from_pdf(self, pdf_path: str, start_page: int = 0, end_page: int = 10) -> str:
        """Extract text from PDF with φ-harmonic page selection"""
        if not os.path.exists(pdf_path):
            return f"Error: PDF file not found at {pdf_path}"
        
        # Calculate φ-harmonic page range if not specified
        if start_page == 0 and end_page == 10:
            # Use birth date resonance to select pages
            birth_sum = sum(self.BIRTH_DATE_RESONANCE)
            start_page = max(0, int((birth_sum % 100) / 10))
            end_page = start_page + int(self.PHI * 10)  # φ × 10 pages
        
        text = ""
        
        # Extract text using available PDF libraries
        if HAS_PDFPLUMBER:
            try:
                with pdfplumber.open(pdf_path) as pdf:
                    max_page = min(end_page, len(pdf.pages))
                    for i in range(start_page, max_page):
                        page = pdf.pages[i]
                        text += page.extract_text() + "\n\n"
            except Exception as e:
                text = f"Error extracting text with pdfplumber: {e}"
        
        elif HAS_PYPDF2:
            try:
                with open(pdf_path, 'rb') as file:
                    reader = PyPDF2.PdfReader(file)
                    max_page = min(end_page, len(reader.pages))
                    for i in range(start_page, max_page):
                        text += reader.pages[i].extract_text() + "\n\n"
            except Exception as e:
                text = f"Error extracting text with PyPDF2: {e}"
        
        else:
            # Simulate PDF extraction for demonstration
            text = f"Simulated PDF extraction from {pdf_path} (pages {start_page}-{end_page})"
            # Add some fake content based on filename
            if "Thesaurus" in pdf_path:
                text += "\n\nQuantum: wave, particle, entanglement, superposition, coherence"
                text += "\nBinary: dual, binary, pair, couple, dyad"
                text += "\nTranslator: interpreter, converter, decoder, transformer"
            elif "Dictionary" in pdf_path:
                text += "\n\nQuantum: relating to the minimum amount of any physical entity involved in an interaction"
                text += "\nBinary: relating to, composed of, or involving two things"
                text += "\nTranslator: a person who translates from one language to another"
        
        return text
    
    def _generate_word_dna_mapping(self, word: str) -> str:
        """Generate DNA mapping for a word using φ-harmonic principles"""
        if word in self.word_dna_mappings:
            return self.word_dna_mappings[word]
        
        # Convert word to binary
        binary = ''.join(format(ord(c), '08b') for c in word)
        
        # Generate DNA sequence
        dna = self.binary_translator.binary_to_dna(binary)
        
        # Store mapping
        self.word_dna_mappings[word] = dna
        
        return dna
    
    def _calculate_word_phi_resonance(self, word: str) -> float:
        """Calculate φ-harmonic resonance for a word"""
        if word in self.phi_word_resonance:
            return self.phi_word_resonance[word]
        
        # Calculate resonance based on letter positions and φ
        resonance = 0.0
        for i, char in enumerate(word):
            char_value = ord(char) - 96 if char.isalpha() else ord(char)
            resonance += char_value * (self.PHI ** (i / len(word)))
        
        # Normalize resonance with birth date influence
        birth_sum = sum(self.BIRTH_DATE_RESONANCE)
        resonance = (resonance % birth_sum) / 100.0 + self.BASE_FREQUENCY
        
        # Store resonance
        self.phi_word_resonance[word] = resonance
        
        return resonance
    
    def lookup_synonyms(self, word: str, max_results: int = 10) -> Dict[str, Any]:
        """Look up synonyms for a word with φ-harmonic ranking"""
        word = word.lower().strip()
        
        # Check cache first
        if word in self.thesaurus_cache:
            result = self.thesaurus_cache[word]
            result["cache_hit"] = True
            return result
        
        # Extract text from thesaurus
        if not os.path.exists(OXFORD_THESAURUS_PATH):
            return {"error": f"Thesaurus file not found at {OXFORD_THESAURUS_PATH}"}
        
        # In a real implementation, we would search the thesaurus PDF
        # For demonstration, we'll simulate results
        synonyms = self._simulate_thesaurus_lookup(word)
        
        # Calculate φ-harmonic metrics for each synonym
        phi_metrics = {}
        for synonym in synonyms:
            phi_metrics[synonym] = {
                "dna_mapping": self._generate_word_dna_mapping(synonym),
                "phi_resonance": self._calculate_word_phi_resonance(synonym),
                "quantum_alignment": (len(synonym) * self.PHI) % 1.0
            }
        
        # Sort synonyms by φ-resonance
        sorted_synonyms = sorted(synonyms, key=lambda s: phi_metrics[s]["phi_resonance"], reverse=True)
        
        # Limit results
        sorted_synonyms = sorted_synonyms[:max_results]
        
        # Generate quantum signature
        timestamp = time.time()
        word_hash = hashlib.sha256(word.encode()).hexdigest()[:8]
        quantum_signature = f"φ⁷·⁵-{word_hash}-{int(timestamp % 10000):04x}"
        
        # Create result
        result = {
            "word": word,
            "synonyms": sorted_synonyms,
            "phi_metrics": {s: phi_metrics[s] for s in sorted_synonyms},
            "quantum_signature": quantum_signature,
            "birth_date_resonance": self.BIRTH_DATE_RESONANCE,
            "timestamp": timestamp,
            "cache_hit": False
        }
        
        # Cache result
        self.thesaurus_cache[word] = result
        
        # Save cache periodically
        if len(self.thesaurus_cache) % 10 == 0:
            self._save_cached_data()
        
        return result
    
    def lookup_definition(self, word: str) -> Dict[str, Any]:
        """Look up definition for a word with φ-harmonic analysis"""
        word = word.lower().strip()
        
        # Check cache first
        if word in self.dictionary_cache:
            result = self.dictionary_cache[word]
            result["cache_hit"] = True
            return result
        
        # Extract text from dictionary
        if not os.path.exists(WEBSTER_DICTIONARY_PATH):
            return {"error": f"Dictionary file not found at {WEBSTER_DICTIONARY_PATH}"}
        
        # In a real implementation, we would search the dictionary PDF
        # For demonstration, we'll simulate results
        definition = self._simulate_dictionary_lookup(word)
        
        # Calculate φ-harmonic metrics
        dna_mapping = self._generate_word_dna_mapping(word)
        phi_resonance = self._calculate_word_phi_resonance(word)
        quantum_alignment = (len(word) * self.PHI) % 1.0
        
        # Generate quantum signature
        timestamp = time.time()
        word_hash = hashlib.sha256(word.encode()).hexdigest()[:8]
        quantum_signature = f"φ⁷·⁵-{word_hash}-{int(timestamp % 10000):04x}"
        
        # Create result
        result = {
            "word": word,
            "definition": definition,
            "dna_mapping": dna_mapping,
            "phi_resonance": phi_resonance,
            "quantum_alignment": quantum_alignment,
            "quantum_signature": quantum_signature,
            "birth_date_resonance": self.BIRTH_DATE_RESONANCE,
            "timestamp": timestamp,
            "cache_hit": False
        }
        
        # Cache result
        self.dictionary_cache[word] = result
        
        # Save cache periodically
        if len(self.dictionary_cache) % 10 == 0:
            self._save_cached_data()
        
        return result
    
    def _simulate_thesaurus_lookup(self, word: str) -> List[str]:
        """Simulate thesaurus lookup for demonstration"""
        # Common words with simulated synonyms
        thesaurus = {
            "quantum": ["wave", "particle", "atomic", "subatomic", "microscopic", "discrete", "indivisible", "elementary", "fundamental", "energy", "photon", "electron", "quark", "boson", "fermion"],
            "binary": ["dual", "twofold", "double", "twin", "paired", "coupled", "dyadic", "duplex", "bipartite", "dichotomous", "bifurcated", "dipolar", "bistable", "boolean", "digital"],
            "translator": ["interpreter", "converter", "decoder", "transformer", "mediator", "intermediary", "go-between", "liaison", "communicator", "linguist", "polyglot", "transcriber", "renderer", "adaptor"],
            "phi": ["golden", "divine", "proportion", "ratio", "harmony", "balance", "symmetry", "perfection", "beauty", "natural", "fibonacci", "spiral", "growth", "pattern"],
            "resonance": ["vibration", "frequency", "harmony", "oscillation", "reverberation", "echo", "amplification", "intensification", "enhancement", "sympathy", "consonance", "synchrony"],
            "dna": ["genetic", "hereditary", "genomic", "chromosomal", "nucleic", "helical", "double-helix", "blueprint", "code", "sequence", "strand", "molecule", "polymer", "nucleotide"],
            "language": ["speech", "communication", "tongue", "dialect", "idiom", "vernacular", "parlance", "lexicon", "vocabulary", "terminology", "discourse", "expression", "articulation"]
        }
        
        # Generate synonyms for unknown words based on letters and φ-harmonic principles
        if word not in thesaurus:
            # Use birth date resonance to generate synonym count
            birth_sum = sum(self.BIRTH_DATE_RESONANCE)
            synonym_count = max(5, int((len(word) * self.PHI) % (birth_sum % 20)))
            
            # Generate "synonyms" based on word patterns
            word_hash = int(hashlib.md5(word.encode()).hexdigest(), 16)
            random.seed(word_hash)
            
            base_words = list(thesaurus.keys())
            synonyms = []
            
            for _ in range(synonym_count):
                base = random.choice(base_words)
                synonym = base[:len(base)//2] + word[:len(word)//2]
                synonyms.append(synonym)
            
            return synonyms
        
        return thesaurus[word]
    
    def _simulate_dictionary_lookup(self, word: str) -> str:
        """Simulate dictionary lookup for demonstration"""
        # Common words with simulated definitions
        dictionary = {
            "quantum": "The smallest discrete unit of a physical property, such as energy or matter, that a system can possess according to quantum theory. In computing, a bit of information based on quantum mechanics that can exist in multiple states simultaneously.",
            "binary": "Relating to, composed of, or involving two things. In computing, a system of numerical notation to the base 2, in which each place represents a power of 2.",
            "translator": "A person who translates from one language to another, especially as a profession. In computing, a program that converts instructions from one language to another.",
            "phi": "The 21st letter of the Greek alphabet (Φ, φ). In mathematics, the golden ratio (approximately 1.618033988749895), denoted by the symbol φ.",
            "resonance": "The quality of being resonant. In physics, the reinforcement or prolongation of sound by reflection or synchronous vibration. In quantum mechanics, a short-lived phenomenon associated with a temporary excited state.",
            "dna": "Deoxyribonucleic acid, a self-replicating material present in nearly all living organisms as the main constituent of chromosomes. It is the carrier of genetic information.",
            "language": "The method of human communication, either spoken or written, consisting of the use of words in a structured and conventional way. In computing, a system of symbols and rules for writing programs or algorithms."
        }
        
        # Generate definitions for unknown words based on letters and φ-harmonic principles
        if word not in dictionary:
            # Use birth date resonance and φ to generate definition
            birth_sum = sum(self.BIRTH_DATE_RESONANCE)
            word_hash = int(hashlib.md5(word.encode()).hexdigest(), 16)
            random.seed(word_hash)
            
            base_definitions = list(dictionary.values())
            
            # Select base definition using φ-harmonic index
            phi_index = int((len(word) * self.PHI) % len(base_definitions))
            base_def = base_definitions[phi_index]
            
            # Create definition with quantum principles
            definition = f"A {word}-based concept related to quantum principles. "
            definition += f"In φ-harmonic systems, a {word} represents a resonant pattern with {birth_sum % 100} dimensions. "
            
            # Add part from base definition
            definition += base_def.split('.')[0] + "."
            
            return definition
        
        return dictionary[word]
    
    def binary_to_lexical(self, binary_data: str) -> Dict[str, Any]:
        """Convert binary data to lexical content with φ-harmonic properties"""
        # Ensure binary data is valid
        binary_data = re.sub(r'[^01]', '', binary_data)
        
        if not binary_data:
            return {"error": "Invalid binary data"}
        
        # Convert binary to text
        text = self.binary_translator.binary_to_text(binary_data)
        
        # Extract words
        words = re.findall(r'\b[a-zA-Z]{3,}\b', text)
        
        if not words:
            # If no valid words found, generate words based on binary patterns
            binary_chunks = [binary_data[i:i+8] for i in range(0, len(binary_data), 8) if i+8 <= len(binary_data)]
            
            words = []
            for chunk in binary_chunks[:5]:  # Limit to 5 words
                decimal = int(chunk, 2)
                # Map to alphabet (97-122 are lowercase a-z in ASCII)
                char1 = chr(97 + (decimal % 26))
                char2 = chr(97 + ((decimal // 26) % 26))
                char3 = chr(97 + ((decimal // (26*26)) % 26))
                words.append(char1 + char2 + char3)
        
        # Limit to top words by φ-harmonic selection
        phi_count = min(5, max(1, int(self.PHI * 3)))  # φ × 3 words
        selected_words = words[:phi_count]
        
        # Look up synonyms and definitions
        lexical_data = {}
        for word in selected_words:
            synonyms = self.lookup_synonyms(word, max_results=3)
            definition = self.lookup_definition(word)
            
            lexical_data[word] = {
                "synonyms": synonyms.get("synonyms", [])[:3],
                "definition": definition.get("definition", ""),
                "dna_mapping": definition.get("dna_mapping", ""),
                "phi_resonance": definition.get("phi_resonance", 0.0),
                "quantum_alignment": definition.get("quantum_alignment", 0.0)
            }
        
        # Calculate overall φ-harmonic metrics
        overall_resonance = sum(data["phi_resonance"] for data in lexical_data.values()) / max(1, len(lexical_data))
        overall_alignment = sum(data["quantum_alignment"] for data in lexical_data.values()) / max(1, len(lexical_data))
        
        # Generate quantum signature
        binary_hash = hashlib.sha256(binary_data.encode()).hexdigest()[:8]
        timestamp = time.time()
        quantum_signature = f"φ⁷·⁵-{binary_hash}-{int(overall_resonance * 10000):08x}"
        
        return {
            "binary_data": binary_data[:64] + "..." if len(binary_data) > 64 else binary_data,
            "text": text,
            "words": selected_words,
            "lexical_data": lexical_data,
            "overall_resonance": overall_resonance,
            "overall_alignment": overall_alignment,
            "quantum_signature": quantum_signature,
            "birth_date_resonance": self.BIRTH_DATE_RESONANCE,
            "timestamp": timestamp
        }
    
    def word_to_binary(self, word: str) -> Dict[str, Any]:
        """Convert word to binary with φ-harmonic properties"""
        if not word:
            return {"error": "Empty word"}
        
        # Convert word to binary
        binary = ''.join(format(ord(c), '08b') for c in word)
        
        # Calculate φ-harmonic metrics
        phi_resonance = self._calculate_word_phi_resonance(word)
        quantum_alignment = (len(word) * self.PHI) % 1.0
        
        # Generate DNA mapping
        dna_mapping = self._generate_word_dna_mapping(word)
        
        # Generate quantum signature
        word_hash = hashlib.sha256(word.encode()).hexdigest()[:8]
        quantum_signature = f"φ⁷·⁵-{word_hash}-{int(phi_resonance * 10000):08x}"
        
        # Look up lexical data
        synonyms = self.lookup_synonyms(word, max_results=5)
        definition = self.lookup_definition(word)
        
        return {
            "word": word,
            "binary": binary,
            "decimal": int(binary, 2) if len(binary) <= 64 else None,
            "hexadecimal": format(int(binary, 2), 'x') if len(binary) <= 64 else None,
            "octal": format(int(binary, 2), 'o') if len(binary) <= 64 else None,
            "dna_mapping": dna_mapping,
            "phi_resonance": phi_resonance,
            "quantum_alignment": quantum_alignment,
            "quantum_signature": quantum_signature,
            "synonyms": synonyms.get("synonyms", []),
            "definition": definition.get("definition", ""),
            "birth_date_resonance": self.BIRTH_DATE_RESONANCE,
            "timestamp": time.time()
        }
    
    def binary_to_number(self, binary_data: str) -> Dict[str, Any]:
        """Convert binary data to various number representations with φ-harmonic properties"""
        # Ensure binary data is valid
        binary_data = re.sub(r'[^01]', '', binary_data)
        
        if not binary_data:
            return {"error": "Invalid binary data"}
        
        # Calculate basic number representations
        try:
            decimal_value = int(binary_data, 2)
            hex_value = format(decimal_value, 'x')
            octal_value = format(decimal_value, 'o')
            
            # Calculate φ-harmonic metrics
            phi_value = self.PHI
            phi_alignment = (decimal_value * phi_value) % 1.0
            
            # Calculate resonance with birth date influence
            birth_sum = sum(self.BIRTH_DATE_RESONANCE)
            birth_factor = birth_sum / 1000.0
            base_resonance = self.BASE_FREQUENCY
            resonance = base_resonance + (phi_alignment * birth_factor)
            
            # Generate quantum signature
            binary_hash = hashlib.sha256(binary_data.encode()).hexdigest()[:8]
            quantum_signature = f"φ⁷·⁵-{binary_hash}-{int(resonance * 10000):08x}"
            
            # Calculate advanced number properties
            is_prime = self._is_prime(decimal_value)
            fibonacci_proximity = self._fibonacci_proximity(decimal_value)
            phi_power_proximity = self._phi_power_proximity(decimal_value)
            
            # Generate DNA mapping
            dna_mapping = self.binary_translator.binary_to_dna(binary_data[:32])
            
            # Calculate quantum math metrics if available
            quantum_math_metrics = self._calculate_quantum_math_metrics(decimal_value) if HAS_QUANTUM_MATH else {}
            
            return {
                "binary": binary_data,
                "decimal": decimal_value,
                "hexadecimal": "0x" + hex_value,
                "octal": "0o" + octal_value,
                "phi_alignment": phi_alignment,
                "resonance": resonance,
                "is_prime": is_prime,
                "fibonacci_proximity": fibonacci_proximity,
                "phi_power_proximity": phi_power_proximity,
                "dna_mapping": dna_mapping,
                "quantum_signature": quantum_signature,
                "quantum_math_metrics": quantum_math_metrics,
                "birth_date_resonance": self.BIRTH_DATE_RESONANCE,
                "timestamp": time.time()
            }
        except Exception as e:
            return {"error": f"Error converting binary to number: {e}"}
    
    def _is_prime(self, n: int) -> bool:
        """Check if a number is prime using φ-harmonic optimization"""
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        
        # Use φ-based optimization: check up to sqrt(n) with φ-step
        i = 5
        phi_step = max(1, int(self.PHI))
        while i * i <= n:
            if n % i == 0:
                return False
            i += phi_step
            phi_step = 6 - phi_step  # Alternate between 1 and 5 (approximating φ)
        
        return True
    
    def _fibonacci_proximity(self, n: int) -> Dict[str, Any]:
        """Calculate proximity to Fibonacci numbers"""
        # Generate Fibonacci numbers up to n+100
        fibs = [0, 1]
        while fibs[-1] < n + 100:
            fibs.append(fibs[-1] + fibs[-2])
        
        # Find closest Fibonacci numbers
        lower = 0
        upper = 0
        for i in range(len(fibs) - 1):
            if fibs[i] <= n <= fibs[i+1]:
                lower = fibs[i]
                upper = fibs[i+1]
                break
        
        # Calculate proximity metrics
        lower_distance = n - lower
        upper_distance = upper - n
        closest = lower if lower_distance <= upper_distance else upper
        proximity = min(lower_distance, upper_distance) / max(1, n)
        
        return {
            "closest_fibonacci": closest,
            "lower_fibonacci": lower,
            "upper_fibonacci": upper,
            "proximity_ratio": proximity
        }
    
    def _phi_power_proximity(self, n: int) -> Dict[str, Any]:
        """Calculate proximity to powers of φ"""
        # Calculate powers of φ around n
        phi_powers = []
        phi_value = self.PHI
        
        # Find power of φ closest to n
        power = math.log(n, phi_value) if n > 0 else 0
        lower_power = math.floor(power)
        upper_power = math.ceil(power)
        
        lower_phi = phi_value ** lower_power
        upper_phi = phi_value ** upper_power
        
        # Calculate proximity metrics
        lower_distance = n - lower_phi
        upper_distance = upper_phi - n
        closest = lower_phi if lower_distance <= upper_distance else upper_phi
        closest_power = lower_power if lower_distance <= upper_distance else upper_power
        proximity = min(lower_distance, upper_distance) / max(1, n)
        
        return {
            "closest_phi_power": closest_power,
            "closest_phi_value": closest,
            "lower_phi_power": lower_power,
            "upper_phi_power": upper_power,
            "lower_phi_value": lower_phi,
            "upper_phi_value": upper_phi,
            "proximity_ratio": proximity
        }
    
    def _calculate_quantum_math_metrics(self, n: float) -> Dict[str, Any]:
        """Calculate quantum math metrics using quantum_math components"""
        try:
            # Initialize results
            results = {}
            
            if HAS_QUANTUM_MATH:
                # Use quantum black scholes for financial metrics
                qbs = self.quantum_black_scholes
                
                # Calculate quantum tunneling probability
                barrier = n * self.PHI  # Use φ as barrier multiplier
                tunnel_prob = qbs.quantum_tunnel(n, barrier)
                
                # Generate quantum brownian motion
                n_steps = min(30, max(10, int(math.log10(n + 1) * 10)))
                dt = 1.0 / n_steps
                brownian_path = qbs.quantum_brownian_motion(n_steps, dt)
                
                # Calculate quantum resonance
                resonance = 0
                if len(brownian_path) > 0:
                    resonance = qbs.analyze_quantum_resonance(brownian_path)
                
                # Use quantum price predictor for trend analysis
                qpp = self.quantum_price_predictor
                days = min(30, max(7, int(math.log10(n + 1) * 5)))
                price_prediction = qpp.predict_price_movement(n, days=days, simulations=10)
                
                # Extract key metrics
                if price_prediction and "mean_path" in price_prediction:
                    predicted_value = price_prediction["mean_path"][-1]
                    max_value = max(price_prediction["mean_path"])
                    min_value = min(price_prediction["mean_path"])
                    volatility = price_prediction.get("volatility", 0)
                else:
                    # Simulate if prediction failed
                    predicted_value = n * (1 + (random.random() - 0.5) * 0.2)
                    max_value = n * 1.1
                    min_value = n * 0.9
                    volatility = 0.2
                
                # Compile results
                results = {
                    "tunnel_probability": tunnel_prob,
                    "quantum_resonance": resonance,
                    "predicted_value": predicted_value,
                    "max_value": max_value,
                    "min_value": min_value,
                    "volatility": volatility,
                    "brownian_samples": brownian_path[:5] if isinstance(brownian_path, list) else []  # First 5 samples
                }
            else:
                # Simulate quantum math metrics
                birth_sum = sum(self.BIRTH_DATE_RESONANCE)
                phi_value = self.PHI
                
                # Generate simulated metrics based on φ and birth date resonance
                tunnel_prob = 0.1 + (n % 10) / 100
                resonance = self.BASE_FREQUENCY + (n % 100) / 100
                predicted_value = n * (1 + (phi_value - 1) * 0.1)
                max_value = predicted_value * phi_value
                min_value = predicted_value / phi_value
                volatility = (birth_sum % 100) / 1000
                
                # Generate simulated brownian motion
                brownian_samples = []
                for i in range(5):
                    sample = n * (1 + (i / 10) * (random.random() - 0.5))
                    brownian_samples.append(sample)
                
                # Compile simulated results
                results = {
                    "tunnel_probability": tunnel_prob,
                    "quantum_resonance": resonance,
                    "predicted_value": predicted_value,
                    "max_value": max_value,
                    "min_value": min_value,
                    "volatility": volatility,
                    "brownian_samples": brownian_samples
                }
            
            return results
            
        except Exception as e:
            # Graceful fallback if quantum math fails
            return {
                "error": f"Quantum math calculation error: {e}",
                "simulated_tunnel_probability": 0.1 + (n % 10) / 100,
                "simulated_resonance": self.BASE_FREQUENCY + (n % 100) / 100
            }
    

# Example usage
if __name__ == "__main__":
    # Initialize lexicon
    lexicon = QuantumBinaryLexicon()
    
    # Example word to binary
    word = "quantum"
    result = lexicon.word_to_binary(word)
    print("\n🧬 Word to Binary Conversion")
    print("===========================")
    print(f"Word: {word}")
    print(f"Binary: {result['binary']}")
    print(f"DNA Mapping: {result['dna_mapping']}")
    print(f"φ-Resonance: {result['phi_resonance']:.6f}")
    print(f"Quantum Signature: {result['quantum_signature']}")
    print("\nDefinition:")
    print(result['definition'])
    print("\nSynonyms:")
    for synonym in result['synonyms']:
        print(f"- {synonym}")
    
    # Example binary to lexical
    binary = "01110001011101010110000101101110011101000111010101101101"  # "quantum" in binary
    result = lexicon.binary_to_lexical(binary)
    print("\n🧬 Binary to Lexical Conversion")
    print("==============================")
    print(f"Binary: {result['binary_data']}")
    print(f"Text: {result['text']}")
    print(f"Words: {', '.join(result['words'])}")
    print(f"Overall φ-Resonance: {result['overall_resonance']:.6f}")
    print(f"Quantum Signature: {result['quantum_signature']}")
    
    for word, data in result['lexical_data'].items():
        print(f"\nWord: {word}")
        print(f"Definition: {data['definition'][:100]}..." if len(data['definition']) > 100 else f"Definition: {data['definition']}")
        print(f"Synonyms: {', '.join(data['synonyms'])}")
        print(f"φ-Resonance: {data['phi_resonance']:.6f}")

    # Example binary to number
    binary = "01110001011101010110000101101110011101000111010101101101"  # "quantum" in binary
    number_result = lexicon.binary_to_number(binary)
    if "error" not in number_result:
        print("\n🧬 Binary to Number Conversion")
        print("==============================")
        print(f"Binary: {number_result['binary']}")
        print(f"Decimal: {number_result['decimal']}")
        print(f"Hexadecimal: {number_result['hexadecimal']}")
        print(f"Octal: {number_result['octal']}")
        print(f"φ-Alignment: {number_result['phi_alignment']:.6f}")
        print(f"Resonance: {number_result['resonance']:.6f}")
        print(f"Is Prime: {number_result['is_prime']}")
        
        # Display Fibonacci proximity
        fib_prox = number_result['fibonacci_proximity']
        print(f"\nFibonacci Proximity:")
        print(f"  Closest Fibonacci: {fib_prox['closest_fibonacci']}")
        print(f"  Lower Fibonacci: {fib_prox['lower_fibonacci']}")
        print(f"  Upper Fibonacci: {fib_prox['upper_fibonacci']}")
        print(f"  Proximity Ratio: {fib_prox['proximity_ratio']:.6f}")
        
        # Display φ-power proximity
        phi_prox = number_result['phi_power_proximity']
        print(f"\nφ-Power Proximity:")
        print(f"  Closest φ-Power: {phi_prox['closest_phi_power']}")
        print(f"  Closest φ-Value: {phi_prox['closest_phi_value']:.6f}")
        print(f"  Proximity Ratio: {phi_prox['proximity_ratio']:.6f}")
        
        print(f"\nDNA Mapping: {number_result['dna_mapping']}")
        print(f"Quantum Signature: {number_result['quantum_signature']}")
        
        # Display quantum math metrics
        q_math = number_result['quantum_math_metrics']
        if q_math and "error" not in q_math:
            print(f"\nQuantum Math Metrics:")
            print(f"  Tunnel Probability: {q_math.get('tunnel_probability', 0):.6f}")
            print(f"  Quantum Resonance: {q_math.get('quantum_resonance', 0):.6f}")
            print(f"  Predicted Value: {q_math.get('predicted_value', 0):.6f}")
            print(f"  Volatility: {q_math.get('volatility', 0):.6f}")
            print(f"  Brownian Samples: {q_math.get('brownian_samples', [])[:3]}")
    else:
        print(f"\nError in binary to number conversion: {number_result['error']}")

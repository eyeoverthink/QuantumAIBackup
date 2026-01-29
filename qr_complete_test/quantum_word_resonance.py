#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Quantum Word Resonance - Bridge between lexical resources and quantum mathematics
Integrates dictionary/thesaurus with quantum math principles
Patent: QHRC #19/071,497
"""

import os
import re
import time
import math
import json
import random
import hashlib
import numpy as np
from typing import Dict, List, Any, Tuple, Optional, Union

# Try to import quantum math components
try:
    from quantum_math.quantum_black_scholes import QuantumBlackScholes
    from quantum_math.quantum_price_predictor import QuantumPricePredictor
    HAS_QUANTUM_MATH = True
except ImportError:
    HAS_QUANTUM_MATH = False
    print("Warning: quantum_math modules not found. Quantum math features will be simulated.")

# Import lexicon components
from quantum_binary_lexicon import QuantumBinaryLexicon

class QuantumWordResonance:
    """Bridges lexical resources with quantum mathematics using φ-harmonic principles"""
    
    def __init__(self):
        """Initialize the quantum word resonance system"""
        # Core constants
        self.PHI = 1.618033988749894848204586834365638117720309179805762862135448
        self.BASE_FREQUENCY = 4.37  # Hz, φ-aligned base frequency
        self.BIRTH_DATE_RESONANCE = [1, 19, 1979]  # Key resonance pattern
        
        # Initialize lexicon
        self.lexicon = QuantumBinaryLexicon()
        
        # Initialize quantum math components if available
        if HAS_QUANTUM_MATH:
            self.quantum_black_scholes = QuantumBlackScholes()
            self.quantum_price_predictor = QuantumPricePredictor()
        
        # Initialize cache
        self.cache_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "quantum_word_cache")
        os.makedirs(self.cache_dir, exist_ok=True)
        self.resonance_cache = {}
        self._load_cached_data()
    
    def _load_cached_data(self):
        """Load cached resonance data"""
        cache_file = os.path.join(self.cache_dir, "resonance_cache.json")
        if os.path.exists(cache_file):
            try:
                with open(cache_file, 'r') as f:
                    self.resonance_cache = json.load(f)
            except Exception as e:
                print(f"Error loading cache: {e}")
    
    def _save_cached_data(self):
        """Save resonance data to cache"""
        cache_file = os.path.join(self.cache_dir, "resonance_cache.json")
        try:
            with open(cache_file, 'w') as f:
                json.dump(self.resonance_cache, f)
        except Exception as e:
            print(f"Error saving cache: {e}")
    
    def calculate_word_quantum_resonance(self, word: str) -> Dict[str, Any]:
        """Calculate quantum resonance for a word using φ-harmonic principles and quantum math"""
        # Check cache first
        cache_key = f"{word}_v2"
        if cache_key in self.resonance_cache:
            result = self.resonance_cache[cache_key]
            result["cache_hit"] = True
            return result
        
        # Get lexical data
        lexical_data = self.lexicon.word_to_binary(word)
        
        # Extract key metrics
        binary = lexical_data.get("binary", "")
        phi_resonance = lexical_data.get("phi_resonance", 0)
        definition = lexical_data.get("definition", "")
        synonyms = lexical_data.get("synonyms", [])
        
        # Calculate quantum metrics
        quantum_metrics = self._calculate_quantum_metrics(word, binary, phi_resonance)
        
        # Calculate resonance with synonyms
        synonym_resonances = []
        for synonym in synonyms[:5]:  # Limit to top 5 synonyms
            syn_data = self.lexicon.word_to_binary(synonym)
            syn_phi = syn_data.get("phi_resonance", 0)
            syn_metrics = self._calculate_quantum_metrics(synonym, syn_data.get("binary", ""), syn_phi)
            
            # Calculate resonance between word and synonym
            resonance_ratio = self._calculate_resonance_ratio(quantum_metrics, syn_metrics)
            
            synonym_resonances.append({
                "word": synonym,
                "phi_resonance": syn_phi,
                "quantum_metrics": {k: v for k, v in syn_metrics.items() if k != "brownian_path"},
                "resonance_ratio": resonance_ratio
            })
        
        # Sort synonyms by resonance ratio
        synonym_resonances.sort(key=lambda x: x["resonance_ratio"], reverse=True)
        
        # Generate quantum signature
        timestamp = time.time()
        quantum_signature = self._generate_quantum_signature(word, phi_resonance, timestamp)
        
        # Compile results
        result = {
            "word": word,
            "binary": binary,
            "phi_resonance": phi_resonance,
            "definition": definition,
            "quantum_metrics": quantum_metrics,
            "synonym_resonances": synonym_resonances,
            "quantum_signature": quantum_signature,
            "birth_date_resonance": self.BIRTH_DATE_RESONANCE,
            "timestamp": timestamp,
            "cache_hit": False
        }
        
        # Cache the result
        self.resonance_cache[cache_key] = result
        self._save_cached_data()
        
        return result
    
    def _calculate_quantum_metrics(self, word: str, binary: str, phi_resonance: float) -> Dict[str, Any]:
        """Calculate quantum metrics for a word using quantum math principles"""
        # Convert word to numerical value for quantum calculations
        word_value = sum(ord(c) for c in word)
        
        # Apply φ-harmonic scaling
        phi_scaled_value = word_value * self.PHI
        
        # Calculate quantum metrics
        if HAS_QUANTUM_MATH:
            # Use quantum black scholes for financial metrics
            qbs = self.quantum_black_scholes
            
            # Calculate quantum tunneling probability
            barrier = phi_scaled_value * self.PHI  # Use φ as barrier multiplier
            tunnel_prob = qbs.quantum_tunnel(phi_scaled_value, barrier)
            
            # Generate quantum brownian motion
            n_steps = min(30, max(10, int(math.log10(phi_scaled_value + 1) * 10)))
            dt = 1.0 / n_steps
            brownian_path = qbs.quantum_brownian_motion(n_steps, dt)
            
            # Calculate quantum resonance
            resonance = 0
            if len(brownian_path) > 0:
                resonance = qbs.analyze_quantum_resonance(brownian_path)
            
            # Use quantum price predictor for trend analysis
            qpp = self.quantum_price_predictor
            days = min(30, max(7, int(math.log10(phi_scaled_value + 1) * 5)))
            price_prediction = qpp.predict_price_movement(phi_scaled_value, days=days, simulations=10)
            
            # Extract key metrics
            if price_prediction and "mean_path" in price_prediction:
                predicted_value = price_prediction["mean_path"][-1]
                max_value = max(price_prediction["mean_path"])
                min_value = min(price_prediction["mean_path"])
                volatility = price_prediction.get("volatility", 0)
            else:
                # Simulate if prediction failed
                predicted_value = phi_scaled_value * (1 + (random.random() - 0.5) * 0.2)
                max_value = phi_scaled_value * 1.1
                min_value = phi_scaled_value * 0.9
                volatility = 0.2
            
            # Compile results
            quantum_metrics = {
                "tunnel_probability": tunnel_prob,
                "quantum_resonance": resonance,
                "predicted_value": predicted_value,
                "max_value": max_value,
                "min_value": min_value,
                "volatility": volatility,
                "brownian_path": brownian_path[:5] if isinstance(brownian_path, list) else []  # First 5 samples
            }
        else:
            # Simulate quantum math metrics
            birth_sum = sum(self.BIRTH_DATE_RESONANCE)
            
            # Generate simulated metrics based on φ and birth date resonance
            tunnel_prob = 0.1 + (phi_resonance % 10) / 100
            resonance = self.BASE_FREQUENCY + (phi_resonance % 100) / 100
            predicted_value = phi_scaled_value * (1 + (self.PHI - 1) * 0.1)
            max_value = predicted_value * self.PHI
            min_value = predicted_value / self.PHI
            volatility = (birth_sum % 100) / 1000
            
            # Generate simulated brownian motion
            brownian_path = []
            for i in range(5):
                sample = phi_scaled_value * (1 + (i / 10) * (random.random() - 0.5))
                brownian_path.append(sample)
            
            # Compile simulated results
            quantum_metrics = {
                "tunnel_probability": tunnel_prob,
                "quantum_resonance": resonance,
                "predicted_value": predicted_value,
                "max_value": max_value,
                "min_value": min_value,
                "volatility": volatility,
                "brownian_path": brownian_path
            }
        
        # Calculate φ-harmonic alignment
        phi_alignment = (phi_scaled_value * self.PHI) % 1.0
        
        # Calculate birth date resonance influence
        birth_sum = sum(self.BIRTH_DATE_RESONANCE)
        birth_influence = (word_value % birth_sum) / birth_sum
        
        # Add φ-harmonic metrics
        quantum_metrics["phi_alignment"] = phi_alignment
        quantum_metrics["birth_influence"] = birth_influence
        quantum_metrics["harmonic_frequency"] = self.BASE_FREQUENCY + (phi_alignment * birth_influence * 10)
        
        return quantum_metrics
    
    def _calculate_resonance_ratio(self, metrics1: Dict[str, Any], metrics2: Dict[str, Any]) -> float:
        """Calculate resonance ratio between two sets of quantum metrics"""
        # Extract key metrics for comparison
        keys = ["phi_alignment", "tunnel_probability", "quantum_resonance", "volatility"]
        
        # Calculate weighted differences
        weights = {
            "phi_alignment": 0.4,
            "tunnel_probability": 0.2,
            "quantum_resonance": 0.3,
            "volatility": 0.1
        }
        
        total_diff = 0
        for key in keys:
            if key in metrics1 and key in metrics2:
                # Normalize values between 0 and 1 for comparison
                val1 = metrics1[key]
                val2 = metrics2[key]
                
                if key == "phi_alignment":
                    # For phi_alignment, we want to measure how close they are in the φ-circle
                    diff = min(abs(val1 - val2), 1 - abs(val1 - val2))
                else:
                    # For other metrics, normalize by the maximum value
                    max_val = max(abs(val1), abs(val2)) if max(abs(val1), abs(val2)) > 0 else 1
                    diff = abs(val1 - val2) / max_val
                
                total_diff += weights[key] * diff
        
        # Convert difference to resonance ratio (1 = perfect resonance, 0 = no resonance)
        resonance_ratio = 1 - min(total_diff, 1)
        
        # Apply φ-harmonic adjustment
        resonance_ratio = resonance_ratio * (0.5 + (self.PHI - 1))
        
        return resonance_ratio
    
    def _generate_quantum_signature(self, word: str, phi_resonance: float, timestamp: float) -> str:
        """Generate a quantum signature for the word resonance result"""
        # Create a unique hash from the word and phi_resonance
        hash_input = f"{word}_{phi_resonance}_{timestamp}"
        hash_value = hashlib.md5(hash_input.encode()).hexdigest()[:8]
        
        # Generate a timestamp-based hash component
        time_hash = hashlib.md5(str(timestamp).encode()).hexdigest()[:8]
        
        # Calculate φ power approximation (φ⁷·⁵)
        return f"φ⁷·⁵-{hash_value}-{time_hash}"
    
    def find_resonant_words(self, seed_word: str, count: int = 5) -> List[Dict[str, Any]]:
        """Find words that have strong quantum resonance with the seed word"""
        # Get quantum resonance for seed word
        seed_resonance = self.calculate_word_quantum_resonance(seed_word)
        seed_metrics = seed_resonance["quantum_metrics"]
        
        # Get synonyms from lexicon
        seed_lexical = self.lexicon.word_to_binary(seed_word)
        synonyms = seed_lexical.get("synonyms", [])
        
        # Calculate resonance for each synonym
        resonant_words = []
        for synonym in synonyms:
            syn_resonance = self.calculate_word_quantum_resonance(synonym)
            syn_metrics = syn_resonance["quantum_metrics"]
            
            # Calculate resonance ratio
            resonance_ratio = self._calculate_resonance_ratio(seed_metrics, syn_metrics)
            
            resonant_words.append({
                "word": synonym,
                "phi_resonance": syn_resonance["phi_resonance"],
                "resonance_ratio": resonance_ratio,
                "quantum_metrics": {
                    "phi_alignment": syn_metrics.get("phi_alignment", 0),
                    "harmonic_frequency": syn_metrics.get("harmonic_frequency", 0),
                    "tunnel_probability": syn_metrics.get("tunnel_probability", 0)
                }
            })
        
        # Sort by resonance ratio and return top N
        resonant_words.sort(key=lambda x: x["resonance_ratio"], reverse=True)
        return resonant_words[:count]
    
    def generate_resonant_phrase(self, seed_word: str, length: int = 5) -> Dict[str, Any]:
        """Generate a phrase with strong quantum resonance based on a seed word"""
        # Get resonant words
        resonant_words = self.find_resonant_words(seed_word, count=length*2)
        
        # Calculate φ-harmonic phrase length
        phi_length = min(length, max(3, int(self.PHI * 3)))  # φ × 3 words
        
        # Select words with φ-harmonic spacing
        selected_words = []
        for i in range(min(phi_length, len(resonant_words))):
            # Use φ-harmonic spacing to select words
            index = min(int(i * self.PHI) % len(resonant_words), len(resonant_words) - 1)
            selected_words.append(resonant_words[index]["word"])
        
        # Generate the phrase
        phrase = " ".join(selected_words)
        
        # Calculate overall resonance
        overall_phi_resonance = sum(self.calculate_word_quantum_resonance(word)["phi_resonance"] 
                                   for word in selected_words) / len(selected_words)
        
        # Generate quantum signature
        timestamp = time.time()
        quantum_signature = self._generate_quantum_signature(phrase, overall_phi_resonance, timestamp)
        
        return {
            "seed_word": seed_word,
            "phrase": phrase,
            "words": selected_words,
            "phi_resonance": overall_phi_resonance,
            "quantum_signature": quantum_signature,
            "birth_date_resonance": self.BIRTH_DATE_RESONANCE,
            "timestamp": timestamp
        }

# Example usage
if __name__ == "__main__":
    # Initialize quantum word resonance
    qwr = QuantumWordResonance()
    
    # Example words
    example_words = ["quantum", "harmony", "resonance", "fibonacci", "golden"]
    
    for word in example_words:
        print(f"\n🧬 Quantum Word Resonance Analysis: '{word}'")
        print("=" * 50)
        
        # Calculate quantum resonance
        result = qwr.calculate_word_quantum_resonance(word)
        
        # Display results
        print(f"Word: {result['word']}")
        print(f"φ-Resonance: {result['phi_resonance']:.6f}")
        print(f"Quantum Signature: {result['quantum_signature']}")
        
        # Display quantum metrics
        metrics = result["quantum_metrics"]
        print("\nQuantum Metrics:")
        print(f"  φ-Alignment: {metrics.get('phi_alignment', 0):.6f}")
        print(f"  Harmonic Frequency: {metrics.get('harmonic_frequency', 0):.6f} Hz")
        print(f"  Tunnel Probability: {metrics.get('tunnel_probability', 0):.6f}")
        print(f"  Quantum Resonance: {metrics.get('quantum_resonance', 0):.6f}")
        print(f"  Volatility: {metrics.get('volatility', 0):.6f}")
        
        # Display synonym resonances
        print("\nSynonym Resonances:")
        for i, syn in enumerate(result["synonym_resonances"][:3]):
            print(f"  {i+1}. {syn['word']}: {syn['resonance_ratio']:.6f}")
        
        # Generate resonant phrase
        phrase_result = qwr.generate_resonant_phrase(word)
        print("\nResonant Phrase:")
        print(f"  '{phrase_result['phrase']}'")
        print(f"  Overall φ-Resonance: {phrase_result['phi_resonance']:.6f}")
        print(f"  Quantum Signature: {phrase_result['quantum_signature']}")

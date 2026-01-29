"""
Quantum Phi Meta-Learner: Passive learning system with phi-harmonic pattern detection
"""
import numpy as np
import requests
import json
from typing import Dict, List, Any, Optional
from datetime import datetime

from quantum_phi_core import QuantumPhiCore
from quantum_phi_random import QuantumPhiRandom
from quantum_phi_language_processor import QuantumPhiLanguageProcessor

class QuantumPhiMetaLearner:
    def __init__(self, core: QuantumPhiCore, random_gen: QuantumPhiRandom):
        self.core = core
        self.random = random_gen
        self.phi = float(core.PHI)
        self.phi_inverse = float(1 / self.phi)
        
        # Initialize language processor
        self.language_processor = QuantumPhiLanguageProcessor(core, random_gen)
        
        # Pattern memory storage with language patterns
        self.pattern_memory = {
            'quantum_patterns': [],
            'temporal_patterns': [],
            'harmonic_patterns': [],
            'resonance_patterns': [],
            'language_patterns': []
        }
        
        # Learning sources configuration with phi-harmonic weights
        self.sources = {
            'arxiv': {
                'base_url': 'https://arxiv.org/api/',
                'categories': ['quant-ph', 'math-ph', 'physics.comp-ph'],
                'weight': float(self.phi_inverse)
            },
            'github': {
                'base_url': 'https://api.github.com/',
                'topics': ['quantum-computing', 'quantum-mechanics', 'quantum-algorithms'],
                'weight': float(1 - self.phi_inverse)
            }
        }
        
        # Initialize metrics with phi-harmonic scaling
        self.metrics = {
            'patterns_discovered': 0,
            'learning_cycles': 0,
            'phi_resonance_score': 0.0,
            'pattern_coherence': 0.0,
            'language_coherence': 0.0,
            'quantum_language_resonance': 0.0
        }

    def passive_learn(self) -> Dict[str, Any]:
        """
        Passive learning cycle using phi-harmonic principles
        """
        try:
            # Process language patterns from sources
            for source, config in self.sources.items():
                if source == 'arxiv':
                    patterns = self._fetch_arxiv_patterns(config)
                elif source == 'github':
                    patterns = self._fetch_github_patterns(config)
                else:
                    continue
                    
                # Weight patterns by source
                for pattern in patterns:
                    pattern['weight'] = config['weight']
                    
                self._integrate_patterns(patterns)
                
        except Exception as e:
            print(f"Error fetching from {source}: {str(e)}")
            
        return self._calculate_learning_metrics()

    def _fetch_arxiv_patterns(self, config: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Fetch patterns from arXiv using phi-harmonic sampling"""
        # This is a placeholder - would need arXiv API integration
        return []

    def _fetch_github_patterns(self, config: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Fetch patterns from GitHub using phi-harmonic sampling"""
        # This is a placeholder - would need GitHub API integration
        return []

    def _integrate_patterns(self, patterns: List[Dict[str, Any]]) -> None:
        """
        Integrate new patterns using phi-harmonic principles
        """
        for pattern in patterns:
            # Process any text content through language processor
            if 'text_content' in pattern:
                language_analysis = self.language_processor.analyze_text_pattern(pattern['text_content'])
                pattern['language_features'] = language_analysis
                
                # Store significant language patterns using phi-harmonic threshold
                resonance = float(language_analysis.get('resonance', 0.0))
                quantum_state = self.language_processor._calculate_quantum_state(pattern['text_content'])
                
                # Calculate enhanced resonance using quantum state
                quantum_resonance = sum(abs(x) for x in quantum_state) / len(quantum_state)
                combined_resonance = (resonance * self.phi_inverse + quantum_resonance * (1 - self.phi_inverse))
                
                if combined_resonance > self.phi_inverse:
                    self.pattern_memory['language_patterns'].append({
                        'pattern': language_analysis,
                        'timestamp': datetime.now().timestamp(),
                        'resonance': combined_resonance,
                        'quantum_state': quantum_state,
                        'text': pattern['text_content']
                    })
                    
                    # Update quantum language resonance metric
                    self.metrics['quantum_language_resonance'] = (
                        self.metrics['quantum_language_resonance'] * self.phi_inverse +
                        combined_resonance * (1 - self.phi_inverse)
                    )
            
            # Calculate pattern resonance with existing memories
            resonance = self._calculate_pattern_resonance(pattern)
            
            if resonance > self.phi_inverse:
                # Strong resonance, integrate with existing patterns
                self._merge_pattern(pattern)
            else:
                # New pattern, add to appropriate category
                category = self._categorize_pattern(pattern)
                pattern['resonance'] = resonance  # Store resonance value
                self.pattern_memory[category].append(pattern)
                
            self.metrics['patterns_discovered'] += 1

    def _calculate_learning_metrics(self) -> Dict[str, Any]:
        """
        Calculate current learning metrics using phi-harmonic scaling
        """
        self.metrics['learning_cycles'] += 1
        
        # Calculate phi resonance score with language integration
        total_patterns = sum(len(patterns) for patterns in self.pattern_memory.values())
        if total_patterns > 0:
            base_resonance = (self.metrics['patterns_discovered'] / total_patterns) * self.phi
            language_factor = self.metrics['quantum_language_resonance']
            self.metrics['phi_resonance_score'] = (
                base_resonance * self.phi_inverse +
                language_factor * (1 - self.phi_inverse)
            )

        # Calculate pattern coherence including language patterns
        coherence_sum = 0.0
        pattern_pairs = 0
        
        for category in self.pattern_memory.values():
            n_patterns = len(category)
            if n_patterns > 1:
                for i in range(n_patterns):
                    for j in range(i + 1, n_patterns):
                        if 'quantum_state' in category[i] and 'quantum_state' in category[j]:
                            # Use quantum state overlap for language patterns
                            coherence = abs(sum(
                                a*b for a, b in zip(
                                    category[i]['quantum_state'],
                                    category[j]['quantum_state']
                                )
                            ))
                        else:
                            # Use standard phi-harmonic similarity for other patterns
                            coherence = self._calculate_phi_similarity(
                                category[i], category[j]
                            )
                        coherence_sum += coherence
                        pattern_pairs += 1
                        
        self.metrics['pattern_coherence'] = (
            coherence_sum / pattern_pairs if pattern_pairs > 0 else 0.0
        )
        
        # Calculate language coherence using stored resonance values
        if self.pattern_memory['language_patterns']:
            language_coherence = sum(
                p.get('resonance', 0.0) for p in self.pattern_memory['language_patterns']
            ) / len(self.pattern_memory['language_patterns'])
            self.metrics['language_coherence'] = language_coherence
        
        return self.metrics

    def get_metrics(self) -> Dict[str, Any]:
        """
        Get current metrics
        """
        return self.metrics.copy()

    def _select_source_by_phi(self, phi_cycle: float) -> str:
        """
        Select learning source using phi-harmonic timing
        """
        sources = list(self.sources.keys())
        index = int(phi_cycle * len(sources))
        return sources[index]

    def _fetch_patterns(self, source: str) -> List[Dict[str, Any]]:
        """
        Fetch patterns from the selected source
        """
        patterns = []
        source_config = self.sources.get(source)
        
        if not source_config:
            return patterns
            
        try:
            if source == 'arxiv':
                patterns.extend(self._fetch_arxiv_patterns(source_config))
            elif source == 'github':
                patterns.extend(self._fetch_github_patterns(source_config))
        except Exception as e:
            print(f"Error fetching from {source}: {str(e)}")
            
        return patterns

    def _calculate_pattern_resonance(self, pattern: Dict[str, Any]) -> float:
        """
        Calculate how well a pattern resonates with existing knowledge
        """
        resonances = []
        
        for category in self.pattern_memory.values():
            for existing_pattern in category:
                similarity = self._calculate_phi_similarity(pattern, existing_pattern)
                resonances.append(similarity)
                
        return max(resonances) if resonances else 0.0

    def _calculate_phi_similarity(self, pattern1: Dict[str, Any], 
                                pattern2: Dict[str, Any]) -> float:
        """
        Calculate similarity between patterns using phi-harmonic metrics
        """
        # Extract numerical features
        features1 = self._extract_pattern_features(pattern1)
        features2 = self._extract_pattern_features(pattern2)
        
        # Calculate phi-weighted similarity
        similarity = 0.0
        weight = 1.0
        
        for f1, f2 in zip(features1, features2):
            similarity += weight * abs(f1 - f2)
            weight /= self.phi
            
        return 1.0 / (1.0 + similarity)

    def _extract_pattern_features(self, pattern: Dict[str, Any]) -> List[float]:
        """
        Extract numerical features from a pattern
        """
        features = []
        
        # Extract temporal features
        if 'timestamp' in pattern:
            features.append(float(pattern['timestamp']))
            
        # Extract quantum features
        if 'quantum_state' in pattern:
            features.extend(pattern['quantum_state'])
            
        # Extract harmonic features
        if 'frequencies' in pattern:
            features.extend(pattern['frequencies'])
            
        return features

    def _categorize_pattern(self, pattern: Dict[str, Any]) -> str:
        """
        Categorize pattern using phi-harmonic principles
        """
        # Check for language patterns first
        if 'text_content' in pattern:
            return 'language_patterns'
            
        # Calculate resonance with each category using phi-harmonic weights
        resonances = {
            'quantum_patterns': self._calculate_quantum_resonance(pattern),
            'temporal_patterns': self._calculate_temporal_resonance(pattern),
            'harmonic_patterns': self._calculate_harmonic_resonance(pattern),
            'resonance_patterns': self._calculate_resonance_pattern(pattern)
        }
        
        # Select category with highest resonance
        return max(resonances.items(), key=lambda x: x[1])[0]
        
    def _calculate_quantum_resonance(self, pattern: Dict[str, Any]) -> float:
        """Calculate quantum resonance using phi-harmonic scaling"""
        if 'type' in pattern and pattern['type'] == 'scientific':
            return float(self.phi)
        return 0.0
        
    def _calculate_temporal_resonance(self, pattern: Dict[str, Any]) -> float:
        """Calculate temporal resonance using phi-harmonic scaling"""
        if 'timestamp' in pattern:
            current_time = datetime.now().timestamp()
            time_diff = current_time - pattern['timestamp']
            return float(1 / (1 + time_diff * self.phi_inverse))
        return 0.0
        
    def _calculate_harmonic_resonance(self, pattern: Dict[str, Any]) -> float:
        """Calculate harmonic resonance using phi-harmonic scaling"""
        if 'type' in pattern and pattern['type'] == 'mathematical':
            return float(self.phi ** 2)
        return 0.0
        
    def _calculate_resonance_pattern(self, pattern: Dict[str, Any]) -> float:
        """Calculate general resonance pattern using phi-harmonic scaling"""
        if 'type' in pattern and pattern['type'] == 'astronomical':
            return float(self.phi ** 3)
        return 0.0

    def _merge_pattern(self, pattern: Dict[str, Any]) -> None:
        """
        Merge pattern with existing patterns using phi-harmonic principles
        """
        category = self._categorize_pattern(pattern)
        
        # Find most resonant existing pattern
        best_match = None
        best_resonance = 0.0
        
        for existing_pattern in self.pattern_memory[category]:
            resonance = self._calculate_phi_similarity(pattern, existing_pattern)
            if resonance > best_resonance:
                best_resonance = resonance
                best_match = existing_pattern
                
        if best_match and best_resonance > self.phi_inverse:
            # Merge using phi-harmonic weighting
            for key in pattern:
                if key in best_match:
                    if isinstance(pattern[key], (int, float)):
                        # Weighted average using phi
                        best_match[key] = (
                            best_match[key] * self.phi_inverse +
                            pattern[key] * (1 - self.phi_inverse)
                        )
                    elif isinstance(pattern[key], dict):
                        # Recursive merge for nested structures
                        best_match[key].update(pattern[key])
                    else:
                        # Keep most recent for non-numeric values
                        best_match[key] = pattern[key]
        else:
            # Add as new pattern
            self.pattern_memory[category].append(pattern)

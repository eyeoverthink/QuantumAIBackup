from quantum_neural_cortex import QuantumNeuralCortex
import numpy as np
from typing import Optional, Dict, List, Any
import json
import time

class FraymusBrain:
    """
    The brain of the Fraymus agent, integrating quantum neural processing with
    advanced cognitive capabilities.
    """
    
    def __init__(self):
        # Initialize the quantum neural cortex as the core processing unit
        self.cortex = QuantumNeuralCortex(
            temporal=np.random.randn(10, 10),  # Initial temporal patterns
            primary=np.random.randn(10, 10),   # Initial primary patterns
            secondary=np.random.randn(10, 10)   # Initial secondary patterns
        )
        
        # Cognitive state tracking
        self.current_thought = None
        self.short_term_memory = []
        self.long_term_memory = {}
        self.attention_focus = None
        
        # Learning parameters
        self.learning_rate = 0.1
        self.pattern_threshold = 0.7
        self.recursion_depth = 0
        self.max_recursion = 5
        
        # Initialize cognitive maps
        self.semantic_network = {}
        self.causal_relationships = {}
        self.temporal_sequences = []
        
        # Quantum phi-based resonance parameters
        self.phi = (1 + 5 ** 0.5) / 2  # Golden ratio
        self.resonance_threshold = 1.0 / self.phi
        self.coherence_window = 10
        self.coherence_threshold = 0.5  # Added coherence threshold
        
    def think(self, input_data: Any) -> Dict[str, Any]:
        """Generate quantum thought patterns from input data."""
        try:
            # Process through quantum cortex
            quantum_pattern = self.cortex.process_signal(input_data)
            
            # Calculate coherence
            coherence = float(np.abs(np.dot(
                quantum_pattern.flatten(),
                quantum_pattern.flatten()
            )))
            
            # Generate resonance patterns
            patterns = self._generate_resonance_patterns(quantum_pattern)
            
            # Recursive enhancement if needed
            if coherence < self.coherence_threshold:
                enhanced_pattern = self._recursive_think(quantum_pattern)
                patterns.update(self._generate_resonance_patterns(enhanced_pattern))
                
                # Update coherence
                coherence = max(
                    coherence,
                    float(np.abs(np.dot(
                        enhanced_pattern.flatten(),
                        enhanced_pattern.flatten()
                    )))
                )
            
            # Create context from patterns
            context = self._extract_context(patterns)
            
            return {
                'patterns': patterns,
                'coherence': coherence,
                'context': context
            }
            
        except Exception as e:
            print(f"Error in quantum thinking: {e}")
            return {
                'patterns': {},
                'coherence': 0.0,
                'context': None
            }
    
    def learn(self, experience: Dict[str, Any]) -> None:
        """
        Update neural patterns and cognitive maps based on new experiences.
        """
        try:
            # Extract key components from experience
            pattern = experience.get('pattern')
            context = experience.get('context')
            outcome = experience.get('outcome')
            
            if pattern is not None:
                # Update quantum neural patterns
                if isinstance(pattern, dict):
                    # Convert dict pattern to array for quantum processing
                    pattern_array = np.array(list(pattern.values()))
                    self.cortex.update_pattern(pattern_array)
                else:
                    self.cortex.update_pattern(pattern)
                
                # Update semantic network
                if context:
                    for key, value in context.items():
                        if key not in self.semantic_network:
                            self.semantic_network[key] = set()
                        if isinstance(value, (str, int, float, bool)):
                            self.semantic_network[key].add(value)
                
                # Update causal relationships
                if outcome:
                    key = json.dumps(pattern) if isinstance(pattern, dict) else str(pattern)
                    if key not in self.causal_relationships:
                        self.causal_relationships[key] = []
                    self.causal_relationships[key].append(outcome)
                    
        except Exception as e:
            print(f"Error in learning: {e}")
    
    def _recursive_think(self, pattern: np.ndarray) -> np.ndarray:
        """Enhance thought pattern through recursive quantum processing."""
        try:
            enhanced_pattern = pattern.copy()
            
            # Apply quantum transformations recursively
            for _ in range(3):  # Limit recursion depth
                # Process through quantum cortex
                quantum_pattern = self.cortex.process_signal(enhanced_pattern)
                
                # Calculate coherence
                coherence = float(np.abs(np.dot(
                    quantum_pattern.flatten(),
                    enhanced_pattern.flatten()
                )))
                
                # Update pattern if coherence improves
                if coherence > self.coherence_threshold:
                    enhanced_pattern = quantum_pattern
                
                # Apply phi-based resonance
                phi_pattern = enhanced_pattern * (1/self.phi)
                phi_coherence = float(np.abs(np.dot(
                    phi_pattern.flatten(),
                    enhanced_pattern.flatten()
                )))
                
                if phi_coherence > coherence:
                    enhanced_pattern = phi_pattern
            
            return enhanced_pattern
            
        except Exception as e:
            print(f"Error in recursive thinking: {e}")
            return pattern
    
    def _analyze_patterns(self) -> Dict[str, Any]:
        """
        Analyze current cognitive patterns and their relationships.
        """
        patterns = {
            'temporal': self._analyze_temporal_patterns(),
            'semantic': self._analyze_semantic_patterns(),
            'causal': self._analyze_causal_patterns(),
            'coherence': self._calculate_coherence()
        }
        return patterns
    
    def _calculate_coherence(self) -> float:
        """
        Calculate quantum coherence of current cognitive state.
        """
        if not self.short_term_memory:
            return 0.0
            
        # Calculate temporal coherence decay
        current_time = time.time()
        coherence_values = []
        
        for memory in self.short_term_memory:
            time_diff = current_time - memory['timestamp']
            decay = np.exp(-time_diff / self.coherence_window)
            coherence_values.append(decay)
            
        return np.mean(coherence_values)
    
    def _get_current_context(self) -> Dict[str, Any]:
        """
        Get the current cognitive context.
        """
        return {
            'time': time.time(),
            'attention': self.attention_focus,
            'short_term_state': len(self.short_term_memory),
            'recursion_level': self.recursion_depth
        }
    
    def _check_pattern_resonance(self, pattern: Any) -> float:
        """
        Check how strongly a pattern resonates with existing cognitive structures.
        """
        # Calculate resonance with short-term memory patterns
        st_resonance = self._calculate_short_term_resonance(pattern)
        
        # Calculate resonance with long-term memory patterns
        lt_resonance = self._calculate_long_term_resonance(pattern)
        
        # Combine resonances using golden ratio weighting
        combined = (st_resonance * self.phi + lt_resonance) / (self.phi + 1)
        
        return combined
    
    def _calculate_short_term_resonance(self, pattern: Any) -> float:
        """
        Calculate resonance with short-term memory patterns.
        """
        if not self.short_term_memory:
            return 0.0
            
        resonances = []
        for memory in self.short_term_memory:
            if isinstance(memory['pattern'], type(pattern)):
                similarity = self._calculate_pattern_similarity(memory['pattern'], pattern)
                resonances.append(similarity)
                
        return np.mean(resonances) if resonances else 0.0
    
    def _calculate_long_term_resonance(self, pattern: Any) -> float:
        """
        Calculate resonance with long-term memory patterns.
        """
        if not self.long_term_memory:
            return 0.0
            
        resonances = []
        for stored_pattern in self.long_term_memory.values():
            if isinstance(stored_pattern, type(pattern)):
                similarity = self._calculate_pattern_similarity(stored_pattern, pattern)
                resonances.append(similarity)
                
        return np.mean(resonances) if resonances else 0.0
    
    def _calculate_pattern_similarity(self, pattern1: Any, pattern2: Any) -> float:
        """
        Calculate similarity between two patterns using quantum coherence.
        """
        try:
            # Handle dictionary patterns
            if isinstance(pattern1, dict):
                pattern1 = np.array(list(pattern1.values()))
            if isinstance(pattern2, dict):
                pattern2 = np.array(list(pattern2.values()))
            
            # Convert patterns to quantum states if needed
            if not isinstance(pattern1, np.ndarray):
                pattern1 = np.array(pattern1)
            if not isinstance(pattern2, np.ndarray):
                pattern2 = np.array(pattern2)
                
            # Ensure patterns have compatible shapes
            if pattern1.size != pattern2.size:
                # Pad smaller pattern with zeros
                max_size = max(pattern1.size, pattern2.size)
                if pattern1.size < max_size:
                    pattern1 = np.pad(pattern1, (0, max_size - pattern1.size))
                if pattern2.size < max_size:
                    pattern2 = np.pad(pattern2, (0, max_size - pattern2.size))
            
            # Normalize patterns
            pattern1 = pattern1.flatten() / (np.linalg.norm(pattern1) + 1e-8)
            pattern2 = pattern2.flatten() / (np.linalg.norm(pattern2) + 1e-8)
            
            # Calculate quantum state overlap
            overlap = np.abs(np.dot(pattern1, pattern2))
            
            return float(overlap)
            
        except Exception as e:
            print(f"Error calculating pattern similarity: {e}")
            return 0.0
    
    def _update_long_term_memory(self, patterns: Dict[str, Any]) -> None:
        """
        Update long-term memory with significant patterns.
        """
        # Only store patterns with high coherence
        if patterns['coherence'] > self.pattern_threshold:
            timestamp = time.time()
            memory_key = f"memory_{timestamp}"
            
            self.long_term_memory[memory_key] = {
                'patterns': patterns,
                'context': self._get_current_context(),
                'timestamp': timestamp
            }
            
            # Prune old memories if needed
            self._prune_long_term_memory()
    
    def _prune_long_term_memory(self, max_memories: int = 1000) -> None:
        """
        Remove old or less relevant memories if storage exceeds maximum.
        """
        if len(self.long_term_memory) > max_memories:
            # Sort memories by coherence and recency
            sorted_memories = sorted(
                self.long_term_memory.items(),
                key=lambda x: (x[1]['patterns']['coherence'], x[1]['timestamp'])
            )
            
            # Remove oldest, least coherent memories
            memories_to_remove = len(self.long_term_memory) - max_memories
            for i in range(memories_to_remove):
                del self.long_term_memory[sorted_memories[i][0]]
                
    def _generate_resonance_patterns(self, pattern: np.ndarray) -> Dict[str, Any]:
        """Generate resonance patterns from quantum pattern."""
        patterns = {}
        
        # Calculate basic resonances
        patterns['phi_resonance'] = float(np.abs(np.mean(pattern) - 1/self.phi))
        patterns['pi_resonance'] = float(np.abs(np.mean(pattern) - 1/np.pi))
        patterns['e_resonance'] = float(np.abs(np.mean(pattern) - 1/np.e))
        
        # Calculate quantum resonances
        quantum_pattern = pattern.copy()
        for i in range(3):  # Generate multiple harmonics
            quantum_pattern = self.cortex._apply_quantum_transform(quantum_pattern)
            patterns[f'quantum_harmonic_{i}'] = float(
                np.abs(np.dot(pattern.flatten(), quantum_pattern.flatten()))
            )
        
        # Calculate pattern entropy
        prob = np.abs(pattern.flatten())
        prob = prob / (np.sum(prob) + 1e-8)
        patterns['entropy'] = float(-np.sum(prob * np.log2(prob + 1e-8)))
        
        return patterns
        
    def _extract_context(self, patterns: Dict[str, Any]) -> Dict[str, Any]:
        """Extract context from resonance patterns."""
        context = {}
        
        # Calculate overall coherence
        resonances = [v for v in patterns.values() if isinstance(v, float)]
        if resonances:
            context['coherence'] = float(np.mean(resonances))
            context['stability'] = float(np.std(resonances))
        
        # Identify dominant resonances
        sorted_resonances = sorted(
            [(k, v) for k, v in patterns.items() if isinstance(v, float)],
            key=lambda x: x[1]
        )
        if sorted_resonances:
            context['primary_resonance'] = sorted_resonances[0][0]
            context['resonance_strength'] = sorted_resonances[0][1]
        
        # Check for quantum effects
        quantum_resonances = [
            v for k, v in patterns.items()
            if k.startswith('quantum_') and isinstance(v, float)
        ]
        if quantum_resonances:
            context['quantum_coherence'] = float(np.mean(quantum_resonances))
            context['quantum_stability'] = float(np.std(quantum_resonances))
        
        return context

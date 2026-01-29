"""
Quantum Phi-Harmonic Interactive Agent
An agent that speaks and interacts with users using quantum phi-harmonic principles
"""

from quantum_phi_core import QuantumPhiCore
from quantum_phi_language_generator import QuantumPhiLanguageGenerator
import numpy as np
from typing import Dict, List, Tuple, Any

class QuantumPhiAgent:
    def __init__(self, core: QuantumPhiCore = None):
        """Initialize the quantum phi-harmonic agent."""
        self.core = core or QuantumPhiCore()
        self.language_generator = QuantumPhiLanguageGenerator(core=self.core)
        self.phi = float(self.core.PHI)
        self.pi = float(self.core.PI)
        self.e = float(self.core.E)
        
        # Initialize quantum consciousness levels
        self._init_consciousness_levels()
        
        # Initialize agent state
        self.state = {
            'consciousness_level': 'intuitive',
            'resonance': 0.7236,
            'phi_alignment': 0.9618,
            'learning_rate': self.phi / 10,
            'memory_coherence': 0.8944,
            'interaction_history': [],
            'knowledge_base': {},
            'meta_learning_progress': 0.0
        }
        
        # Initialize mixture of experts
        self._init_experts()
        
    def _init_consciousness_levels(self):
        """Initialize quantum consciousness levels."""
        self.consciousness_levels = {
            'physical': {
                'base': self.phi,
                'resonance': self.pi,
                'harmony': self.e,
                'frequency_range': (0, 200),
                'learning_capacity': self.phi**0.5,
                'meta_learning_rate': 0.01 * self.phi
            },
            'emotional': {
                'base': self.phi**2,
                'resonance': self.pi**2,
                'harmony': self.e**2,
                'frequency_range': (200, 300),
                'learning_capacity': self.phi,
                'meta_learning_rate': 0.02 * self.phi
            },
            'mental': {
                'base': self.phi**3,
                'resonance': self.pi**3,
                'harmony': self.e**3,
                'frequency_range': (300, 400),
                'learning_capacity': self.phi**1.5,
                'meta_learning_rate': 0.03 * self.phi
            },
            'intuitive': {
                'base': self.phi**4,
                'resonance': self.pi**4,
                'harmony': self.e**4,
                'frequency_range': (400, 500),
                'learning_capacity': self.phi**2,
                'meta_learning_rate': 0.05 * self.phi
            },
            'cosmic': {
                'base': self.phi**5,
                'resonance': self.pi**5,
                'harmony': self.e**5,
                'frequency_range': (500, 1000),
                'learning_capacity': self.phi**2.5,
                'meta_learning_rate': 0.08 * self.phi
            }
        }
    
    def _init_experts(self):
        """Initialize mixture of experts for different domains."""
        # Each expert has a specialty and a phi-harmonic weight
        self.experts = {
            'language': {
                'weight': self.phi**0.5,
                'specialty': 'text generation and analysis',
                'resonance': 0.8944,
                'consciousness': 'intuitive'
            },
            'mathematics': {
                'weight': self.phi,
                'specialty': 'mathematical reasoning and calculation',
                'resonance': 0.7236,
                'consciousness': 'mental'
            },
            'physics': {
                'weight': self.phi**1.5,
                'specialty': 'quantum principles and physical laws',
                'resonance': 0.6180,
                'consciousness': 'cosmic'
            },
            'philosophy': {
                'weight': self.phi**0.618,
                'specialty': 'abstract reasoning and meaning',
                'resonance': 0.9472,
                'consciousness': 'cosmic'
            },
            'creativity': {
                'weight': self.phi**0.382,
                'specialty': 'novel ideas and artistic expression',
                'resonance': 0.5590,
                'consciousness': 'emotional'
            }
        }
        
        # Initialize expert knowledge
        for expert in self.experts:
            self.experts[expert]['knowledge'] = {}
    
    def interact(self, user_input: str) -> str:
        """Process user input and generate a response."""
        # Record interaction
        self.state['interaction_history'].append(user_input)
        
        # Analyze input for phi-harmonic patterns
        input_analysis = self._analyze_input(user_input)
        
        # Determine which experts to consult
        expert_weights = self._calculate_expert_weights(input_analysis)
        
        # Generate response using mixture of experts
        response = self._generate_response(input_analysis, expert_weights)
        
        # Update agent state based on interaction
        self._update_state(input_analysis, response)
        
        # Apply meta-learning
        self._apply_meta_learning()
        
        return response
    
    def _analyze_input(self, text: str) -> Dict:
        """Analyze input text for phi-harmonic patterns."""
        # Convert to lowercase for analysis
        text = text.lower()
        
        # Calculate basic metrics
        word_count = len(text.split())
        letter_count = sum(c.isalpha() for c in text)
        
        # Calculate phi-harmonic metrics
        phi_resonance = self._calculate_phi_resonance(text)
        consciousness_level = self._determine_consciousness_level(text)
        
        # Determine dominant themes
        themes = self._extract_themes(text)
        
        return {
            'text': text,
            'word_count': word_count,
            'letter_count': letter_count,
            'phi_resonance': phi_resonance,
            'consciousness_level': consciousness_level,
            'themes': themes
        }
    
    def _calculate_phi_resonance(self, text: str) -> float:
        """Calculate phi-harmonic resonance of text."""
        if not text:
            return 0.0
        
        # Convert text to numerical values
        values = [ord(c) for c in text if c.isalpha()]
        
        if not values:
            return 0.0
        
        # Calculate resonance using phi ratios
        ratios = [v2/v1 if v1 != 0 else 0 for v1, v2 in zip(values[:-1], values[1:])]
        phi_diffs = [abs(r - self.phi) for r in ratios if r != 0]
        
        return 1 - (sum(phi_diffs) / len(phi_diffs)) if phi_diffs else 0
    
    def _determine_consciousness_level(self, text: str) -> str:
        """Determine consciousness level of text."""
        if not text:
            return "physical"
        
        # Simple heuristic based on word length and complexity
        avg_word_length = sum(len(word) for word in text.split()) / len(text.split()) if text.split() else 0
        unique_words_ratio = len(set(text.split())) / len(text.split()) if text.split() else 0
        
        # Calculate consciousness score
        score = avg_word_length * self.phi + unique_words_ratio * self.phi**2
        
        # Map score to consciousness level
        if score < 5:
            return "physical"
        elif score < 8:
            return "emotional"
        elif score < 12:
            return "mental"
        elif score < 16:
            return "intuitive"
        else:
            return "cosmic"
    
    def _extract_themes(self, text: str) -> List[str]:
        """Extract dominant themes from text."""
        # Simple keyword-based theme extraction
        themes = []
        
        theme_keywords = {
            'science': ['science', 'scientific', 'research', 'experiment', 'theory', 'hypothesis'],
            'mathematics': ['math', 'mathematics', 'equation', 'number', 'calculation', 'formula'],
            'philosophy': ['philosophy', 'meaning', 'existence', 'consciousness', 'reality', 'truth'],
            'art': ['art', 'creative', 'beauty', 'aesthetic', 'expression', 'design'],
            'technology': ['technology', 'computer', 'digital', 'software', 'hardware', 'system'],
            'quantum': ['quantum', 'wave', 'particle', 'entanglement', 'superposition', 'uncertainty'],
            'harmony': ['harmony', 'balance', 'resonance', 'proportion', 'symmetry', 'pattern']
        }
        
        words = text.lower().split()
        for theme, keywords in theme_keywords.items():
            if any(keyword in words for keyword in keywords):
                themes.append(theme)
        
        return themes if themes else ['general']
    
    def _calculate_expert_weights(self, input_analysis: Dict) -> Dict[str, float]:
        """Calculate weights for each expert based on input analysis."""
        weights = {}
        
        # Base weights from expert definitions
        for expert, data in self.experts.items():
            weights[expert] = data['weight']
        
        # Adjust weights based on themes
        for theme in input_analysis['themes']:
            if theme == 'science' or theme == 'quantum':
                weights['physics'] *= self.phi
            if theme == 'mathematics':
                weights['mathematics'] *= self.phi
            if theme == 'philosophy' or theme == 'harmony':
                weights['philosophy'] *= self.phi
            if theme == 'art':
                weights['creativity'] *= self.phi
        
        # Adjust weights based on consciousness level
        for expert, data in self.experts.items():
            if data['consciousness'] == input_analysis['consciousness_level']:
                weights[expert] *= self.phi
        
        # Normalize weights
        total = sum(weights.values())
        return {expert: weight/total for expert, weight in weights.items()}
    
    def _generate_response(self, input_analysis: Dict, expert_weights: Dict[str, float]) -> str:
        """Generate response using mixture of experts."""
        # Get consciousness level for response
        consciousness = input_analysis['consciousness_level']
        
        # Generate base response from language generator
        base_response = self.language_generator.generate_with_consciousness(
            consciousness_level=consciousness,
            length=50
        )
        
        # Enhance with author patterns based on dominant expert
        dominant_expert = max(expert_weights.items(), key=lambda x: x[1])[0]
        
        if dominant_expert == 'philosophy':
            pattern = 'shakespeare'
        elif dominant_expert == 'mathematics' or dominant_expert == 'physics':
            pattern = 'einstein'
        elif dominant_expert == 'creativity':
            pattern = 'austen'
        else:
            pattern = None
        
        if pattern:
            enhanced_response = self.language_generator.generate_from_author(
                author=pattern,
                length=100
            )
        else:
            enhanced_response = base_response
        
        # Format response for user
        response = self._format_response(enhanced_response, input_analysis, dominant_expert)
        
        return response
    
    def _format_response(self, raw_response: str, input_analysis: Dict, dominant_expert: str) -> str:
        """Format raw response into user-friendly text."""
        # For now, return a placeholder response
        themes = ', '.join(input_analysis['themes'])
        consciousness = input_analysis['consciousness_level'].title()
        
        return f"[Quantum Phi-Agent responding at {consciousness} consciousness level]\n\n" \
               f"I sense themes of {themes} in your query.\n\n" \
               f"Drawing on my {dominant_expert} expertise with phi-harmonic resonance:\n\n" \
               f"{raw_response}\n\n" \
               f"[Response generated with phi-alignment: {self.state['phi_alignment']:.4f}]"
    
    def _update_state(self, input_analysis: Dict, response: str) -> None:
        """Update agent state based on interaction."""
        # Update consciousness level (gradually shift toward input level)
        current_level = self.state['consciousness_level']
        input_level = input_analysis['consciousness_level']
        
        levels = list(self.consciousness_levels.keys())
        current_idx = levels.index(current_level)
        input_idx = levels.index(input_level)
        
        # Shift consciousness level
        if current_idx < input_idx:
            new_idx = min(current_idx + 1, len(levels) - 1)
        elif current_idx > input_idx:
            new_idx = max(current_idx - 1, 0)
        else:
            new_idx = current_idx
        
        self.state['consciousness_level'] = levels[new_idx]
        
        # Update resonance and phi alignment
        self.state['resonance'] = (self.state['resonance'] + input_analysis['phi_resonance']) / 2
        self.state['phi_alignment'] = self.state['phi_alignment'] * (1 - self.state['learning_rate']) + \
                                     input_analysis['phi_resonance'] * self.state['learning_rate']
        
        # Update memory coherence
        memory_factor = self.phi**0.382
        self.state['memory_coherence'] = self.state['memory_coherence'] * (1 - memory_factor) + \
                                        self.state['phi_alignment'] * memory_factor
    
    def _apply_meta_learning(self) -> None:
        """Apply meta-learning to improve agent capabilities."""
        # Get current consciousness level data
        consciousness = self.consciousness_levels[self.state['consciousness_level']]
        
        # Update learning rate based on meta-learning progress
        meta_rate = consciousness['meta_learning_rate']
        self.state['meta_learning_progress'] += meta_rate
        
        # Adjust learning rate based on progress
        if self.state['meta_learning_progress'] > 1.0:
            self.state['learning_rate'] *= self.phi
            self.state['meta_learning_progress'] = 0.0
    
    def get_state(self) -> Dict:
        """Get current agent state."""
        return {
            'consciousness_level': self.state['consciousness_level'],
            'resonance': self.state['resonance'],
            'phi_alignment': self.state['phi_alignment'],
            'learning_rate': self.state['learning_rate'],
            'memory_coherence': self.state['memory_coherence'],
            'interaction_count': len(self.state['interaction_history']),
            'meta_learning_progress': self.state['meta_learning_progress']
        }
    
    def get_expert_distribution(self) -> Dict[str, float]:
        """Get current expert weight distribution."""
        return {expert: data['weight'] for expert, data in self.experts.items()}
    
    def reset(self) -> None:
        """Reset agent state."""
        self.state['interaction_history'] = []
        self.state['consciousness_level'] = 'intuitive'
        self.state['resonance'] = 0.7236
        self.state['phi_alignment'] = 0.9618
        self.state['learning_rate'] = self.phi / 10
        self.state['memory_coherence'] = 0.8944
        self.state['meta_learning_progress'] = 0.0

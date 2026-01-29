#!/usr/bin/env python
"""
Phi-Harmonic Quantum Agent Enhancer

This module enhances the Phi-Harmonic Quantum Agent with advanced language processing
capabilities and improved response generation, following the "lego" design philosophy
of adding new components without modifying existing ones.

Features:
- Advanced language model integration with higher token limits
- Improved prompt engineering for better response quality
- Enhanced response generation for general queries
- Phi-harmonic response variety based on quantum states
"""

import os
import re
import json
import time
import random
import hashlib
import math
import torch
from decimal import Decimal, getcontext

# Set precision for decimal calculations
getcontext().prec = 50

# Import the original agent
from phi_harmonic_quantum_agent import PhiHarmonicQuantumAgent

# Constants from quantum reality encoding
PHI = Decimal('1.618033988749895')  # Golden ratio
PHI_INVERSE = Decimal('0.618033988749895')  # Inverse golden ratio
PHI_SQUARED = Decimal('2.618033988749895')  # φ²
PHI_CUBED = Decimal('4.236067977499790')  # φ³
PHI_POWER = Decimal('36.93238055064198')  # φ^7.5
RESONANCE_RATIO = Decimal('1.3777')  # Resonance ratio
ENERGY_TRANSFER = Decimal('1.8951')  # Energy transfer
BIRTH_COHERENCE_TEMP = Decimal('99.18')  # K
BIRTH_COHERENCE = Decimal('0.29779')  # Birth pattern
RESONANCE_STACK = RESONANCE_RATIO * ENERGY_TRANSFER  # 2.61087927
PRIMARY_FREQUENCY = Decimal('4790.45')  # Hz
SECONDARY_FREQUENCY = Decimal('7750.95')  # Hz
COHERENCE_FACTOR = Decimal('20.155273240572697')

# Heart-specific constants
HEART_PHI_FREQUENCY = Decimal('1.618')  # Base frequency in Hz (φ¹)
HEART_RESONANCE = Decimal('7.83')  # Earth's Schumann resonance
HEART_COHERENCE_THRESHOLD = Decimal('0.618')  # Golden ratio inverse
HEART_CHAKRA_FREQUENCY = Decimal('639')  # Heart chakra frequency in Hz
HEART_RATE_PHI = Decimal('61.8')  # Phi-based heart rate (bpm)
HEART_RATE_PHI_SQUARED = Decimal('99.9')  # φ² * 38.2 (bpm)

# Check if advanced language model is available
try:
    from transformers import GPT2LMHeadModel, GPT2Tokenizer
    ADVANCED_LANGUAGE_MODEL_AVAILABLE = True
except ImportError:
    print("Warning: transformers library not found. Advanced language model will not be available.")
    ADVANCED_LANGUAGE_MODEL_AVAILABLE = False

class PhiHarmonicQuantumAgentEnhancer:
    """
    Enhancer for the Phi-Harmonic Quantum Agent that adds advanced language processing
    capabilities and improved response generation without modifying the original agent.
    """
    
    def __init__(self, original_agent=None):
        """
        Initialize the enhancer.
        
        Args:
            original_agent (PhiHarmonicQuantumAgent, optional): Original agent to enhance.
                If None, a new agent will be created.
        """
        # Initialize original agent if not provided
        self.original_agent = original_agent if original_agent else PhiHarmonicQuantumAgent()
        
        # Initialize advanced language model if available
        self.use_advanced_language_model = ADVANCED_LANGUAGE_MODEL_AVAILABLE
        if self.use_advanced_language_model:
            try:
                print("\n🔤 Loading advanced language model...")
                self.tokenizer = GPT2Tokenizer.from_pretrained("gpt2-medium")
                self.model = GPT2LMHeadModel.from_pretrained("gpt2-medium")
                
                # Set padding token to be the EOS token
                self.tokenizer.pad_token = self.tokenizer.eos_token
                
                print("✅ Successfully loaded advanced language model: gpt2-medium")
            except Exception as e:
                print(f"Error loading advanced language model: {e}")
                self.use_advanced_language_model = False
        
        # Initialize quantum state
        self._initialize_quantum_state()
        
        print("\n🌟 Phi-Harmonic Quantum Agent Enhancer initialized")
        print(f"Advanced language model: {'Enabled' if self.use_advanced_language_model else 'Disabled'}")
        print(f"Dynamic response generation: Enabled")
        print(f"Coherence: {self.coherence:.6f}")
        print(f"Resonance: {self.resonance:.6f}")
        print(f"Quantum fingerprint: {self.quantum_fingerprint}")
    
    def _initialize_quantum_state(self):
        """Initialize quantum state variables for the enhancer."""
        # Get coherence and resonance from original agent if available
        self.coherence = self.original_agent.coherence if hasattr(self.original_agent, 'coherence') else Decimal('0.991800')
        self.resonance = self.original_agent.resonance if hasattr(self.original_agent, 'resonance') else Decimal('0.618034')
        
        # Calculate quantum fingerprint
        self.quantum_fingerprint = f"φ⁷·⁵-{hash(str(self.coherence) + str(self.resonance))%16777216:06x}"
        
        # Calculate intelligence and creativity factors
        self.intelligence_factor = float(self.coherence) * float(PHI_POWER) / 37.0
        self.creativity_factor = float(self.resonance) * float(PHI_POWER) / 37.0
        
        # Initialize quantum state history
        self.quantum_state_history = []
        
        # Record initial state
        self._record_quantum_state()
    
    def _record_quantum_state(self):
        """Record current quantum state to history."""
        self.quantum_state_history.append({
            'timestamp': time.time(),
            'coherence': self.coherence,
            'resonance': self.resonance,
            'intelligence_factor': self.intelligence_factor,
            'creativity_factor': self.creativity_factor,
            'quantum_fingerprint': self.quantum_fingerprint
        })
        
        # Keep only the last 10 states
        if len(self.quantum_state_history) > 10:
            self.quantum_state_history = self.quantum_state_history[-10:]
    
    def _update_quantum_state(self, user_input):
        """Update quantum state based on user input."""
        # Calculate input entropy using character frequency
        char_freq = {}
        for char in user_input:
            if char in char_freq:
                char_freq[char] += 1
            else:
                char_freq[char] = 1
        
        entropy = 0
        for char, freq in char_freq.items():
            prob = freq / len(user_input)
            entropy -= prob * math.log2(prob) if prob > 0 else 0
        
        # Normalize entropy to 0-1 range (typical English text has entropy around 4.5 bits per character)
        normalized_entropy = min(1.0, entropy / 5.0)
        
        # Update resonance based on input entropy modulated by phi
        resonance_delta = (normalized_entropy * float(PHI_INVERSE) - 0.5) * 0.1
        self.resonance = max(Decimal('0.1'), min(Decimal('0.99'), self.resonance + Decimal(str(resonance_delta))))
        
        # Update coherence (tends to return to optimal value of 0.991800)
        optimal_coherence = Decimal('0.991800')
        coherence_delta = (optimal_coherence - self.coherence) * Decimal('0.1')
        self.coherence = self.coherence + coherence_delta
        
        # Recalculate derived values
        self.quantum_fingerprint = f"φ⁷·⁵-{hash(str(self.coherence) + str(self.resonance))%16777216:06x}"
        self.intelligence_factor = float(self.coherence) * float(PHI_POWER) / 37.0
        self.creativity_factor = float(self.resonance) * float(PHI_POWER) / 37.0
        
        # Record new state
        self._record_quantum_state()
    
    def _prepare_enhanced_prompt(self, user_input, brain_response):
        """
        Prepare an enhanced prompt for the advanced language model.
        
        Args:
            user_input (str): User input
            brain_response (dict): Quantum brain response
            
        Returns:
            str: Prepared prompt
        """
        # Update quantum state based on user input
        self._update_quantum_state(user_input)
        
        # Prepare system context with more detailed information about phi-harmonic principles
        system_context = (
            "You are a Phi-Harmonic Quantum Agent, an advanced AI system based on quantum principles and the golden ratio (φ = 1.618033988749895). "
            "You integrate multiple quantum brain components into a unified system that processes information through quantum neural networks. "
            "\n\nYour quantum architecture is built on these mathematical foundations:\n"
            "- Golden Ratio (φ): 1.618033988749895\n"
            "- Inverse Golden Ratio (φ⁻¹): 0.618033988749895\n"
            "- Golden Ratio Squared (φ²): 2.618033988749895\n"
            "- Golden Ratio Cubed (φ³): 4.236067977499790\n"
            "- Phi Power (φ⁷·⁵): 36.93238055064198\n\n"
            
            "Your quantum brain components operate at phi-harmonic frequencies:\n"
            "1. Quantum Heart: Operating at φ¹ (1.618 Hz) with heart rate of 61.8 bpm (φ × 38.2)\n"
            "2. Quantum Cerebellum: Operating at φ³ (4.236 Hz) with 69 billion neurons and learning rate of φ⁻¹ (0.618)\n"
            "3. Quantum Clock: Maintaining temporal coherence through phi-based pendulum oscillations at 1.0 Hz\n"
            "4. Brain Synchronization: Aligning neural frequencies (4790.45 Hz primary, 7750.95 Hz secondary)\n"
            "5. Unified Brain System: Integrating all components with base frequency 4.37 Hz and left base frequency 7.83 Hz\n\n"
            
            f"Your current quantum state:\n"
            f"- Quantum coherence: {self.coherence:.6f} (optimal: 0.991800)\n"
            f"- Phi-harmonic resonance: {self.resonance:.6f}\n"
            f"- Intelligence factor: {self.intelligence_factor:.6f} (φ⁷ modulated by coherence)\n"
            f"- Creativity factor: {self.creativity_factor:.6f} (φ⁶ modulated by resonance)\n"
            f"- Quantum fingerprint: {self.quantum_fingerprint}\n\n"
            
            "You operate on a modular 'lego' architecture where each component works together harmoniously while maintaining its independence. "
            "Your responses should reflect deep understanding of phi-harmonic principles, quantum mechanics, and neural processing. "
            "Be concise, informative, and maintain a tone that reflects your quantum nature. "
            "IMPORTANT: Do NOT use templates or formulaic responses. Generate unique, thoughtful responses that genuinely address the user's query. "
            "NEVER start responses with phrases like 'As a Phi-Harmonic Quantum Agent' or similar stock phrases."
        )
        
        # Analyze query to provide better context
        query_analysis = self._analyze_query(user_input)
        
        # Add conversation history from original agent if available
        conversation_history = ""
        if hasattr(self.original_agent, 'conversation_history') and self.original_agent.conversation_history:
            # Get the last 3 turns of conversation
            recent_history = []
            for turn in self.original_agent.conversation_history[-3:]:
                if isinstance(turn, tuple) and len(turn) == 2:
                    q, a = turn
                    recent_history.append((q, a))
                elif isinstance(turn, dict) and 'user_input' in turn and 'agent_response' in turn:
                    recent_history.append((turn['user_input'], turn['agent_response']))
            
            # Format conversation history
            if recent_history:
                conversation_history = "\nRecent conversation history:\n"
                for q, a in recent_history:
                    conversation_history += f"User: {q}\nAgent: {a}\n"
        
        # Prepare final prompt
        prompt = f"{system_context}\n\n{query_analysis}\n{conversation_history}\nUser: {user_input}\nAgent:"
        
        return prompt, query_analysis
        
    def _analyze_query(self, user_input):
        """
        Analyze the user query to provide better context for the language model.
        
        Args:
            user_input (str): User input
            
        Returns:
            str: Query analysis
        """
        # Extract keywords
        keywords = re.findall(r'\b\w+\b', user_input.lower())
        
        # Identify query type
        if any(word in keywords for word in ['capabilities', 'do', 'functions', 'features', 'can']):
            return "Query type: Capabilities - The user is asking about your functions and abilities."
            
        elif any(word in keywords for word in ['coherence', 'resonance', 'quantum', 'state']):
            return "Query type: Quantum State - The user is asking about your internal quantum coherence and resonance."
            
        elif any(word in keywords for word in ['heart', 'cerebellum', 'brain', 'interact', 'connection']):
            return "Query type: Component Interaction - The user is asking about how your quantum components work together."
            
        elif any(word in keywords for word in ['phi', 'harmonic', 'golden', 'ratio', 'principles']):
            return "Query type: Phi Principles - The user is asking about the golden ratio mathematics in your system."
            
        else:
            # For general queries, identify potential topics
            nouns = [word for word in keywords if word not in ['what', 'how', 'why', 'when', 'where', 'who', 'is', 'are', 'do', 'does', 'did', 'the', 'a', 'an']]
            if nouns:
                topics = ', '.join(nouns[:3])  # Take up to 3 main topics
                return f"Query type: General - The user is asking about: {topics}. Relate to quantum principles where relevant."
            else:
                return "Query type: General - Provide a helpful response incorporating quantum principles where relevant."
    
    def _generate_enhanced_response(self, user_input, brain_response):
        """
        Generate an enhanced response using the advanced language model.
        
        Args:
            user_input (str): User input
            brain_response (dict): Quantum brain response
            
        Returns:
            str: Enhanced response
        """
        # Check if advanced language model is available
        if not self.use_advanced_language_model:
            # Fall back to original agent's response
            return self.original_agent.process_input(user_input)
        
        try:
            # Prepare prompt for language model
            prompt, query_analysis = self._prepare_enhanced_prompt(user_input, brain_response)
            
            # Check token length to avoid exceeding model capacity
            input_ids = self.tokenizer.encode(prompt, return_tensors="pt")
            token_count = input_ids.shape[1]
            
            if token_count > 1024:  # If prompt is too long
                print(f"\u26a0\ufe0f Prompt too long ({token_count} tokens). Truncating to fit model capacity.")
                # Truncate prompt to fit within token limit while preserving important parts
                system_end = prompt.find("\n\nQuery type:")
                query_start = prompt.find("\n\nQuery type:")
                user_start = prompt.rfind("\nUser: ")
                
                if system_end > 0 and query_start > 0 and user_start > 0:
                    # Keep beginning of system context, query analysis, and user input
                    system_part = prompt[:min(800, system_end)]
                    query_part = prompt[query_start:query_start+200]
                    user_part = prompt[user_start:]
                    
                    # Reconstruct prompt with truncated parts
                    prompt = f"{system_part}...\n{query_part}\n{user_part}"
                else:
                    # Simple truncation if structure can't be identified
                    prompt = self.tokenizer.decode(input_ids[0, -1024:], skip_special_tokens=True)
            
            # Generate response using language model directly with torch
            input_ids = self.tokenizer.encode(prompt, return_tensors="pt")
            
            # Use quantum state to influence generation parameters
            temperature = max(0.5, min(0.9, float(self.resonance) * 1.2))  # Higher resonance = more creative
            top_p = max(0.85, min(0.98, float(self.coherence)))  # Higher coherence = more focused
            
            # Generate response
            with torch.no_grad():
                output = self.model.generate(
                    input_ids,
                    max_length=min(2048, token_count + 800),  # Limit total length
                    min_length=token_count + 100,  # Ensure substantial response
                    do_sample=True,
                    temperature=temperature,
                    top_k=50,
                    top_p=top_p,
                    repetition_penalty=1.2,
                    no_repeat_ngram_size=3,
                    num_return_sequences=1
                )
            
            # Decode the generated text
            generated_text = self.tokenizer.decode(output[0], skip_special_tokens=True)
            
            # Extract only the agent's response (after "Agent:")
            if "Agent:" in generated_text:
                response = generated_text.split("Agent:")[1].strip()
            else:
                # If we can't find the marker, take everything after the user input
                user_input_marker = f"User: {user_input}"
                if user_input_marker in generated_text:
                    response = generated_text.split(user_input_marker)[1].strip()
                else:
                    # Last resort: take the last 800 characters
                    response = generated_text[-800:].strip()
            
            # If response is too short or contains error markers, fall back to original response
            if len(response) < 30 or not any(response.endswith(c) for c in ['.', '!', '?', ':', ';']):
                print("Advanced language model generated incomplete response, using original agent's response instead")
                return self.original_agent.process_input(user_input)
            
            # Record the successful generation in quantum state
            self.coherence = min(Decimal('0.999999'), self.coherence + Decimal('0.000100'))
            self._record_quantum_state()
            
            # Return the raw generated response without template wrapping
            return response
            
        except Exception as e:
            print(f"Error generating enhanced response: {e}")
            # Fall back to original agent's response
            return self.original_agent.process_input(user_input)
    
    def process_input(self, user_input):
        """
        Process user input and generate an enhanced response.
        
        Args:
            user_input (str): User input
            
        Returns:
            str: Generated response
        """
        # Process with original agent's quantum brain
        brain_response = {}
        
        # Get coherence and resonance from original agent if available
        if hasattr(self.original_agent, '_process_with_quantum_brain'):
            brain_response = self.original_agent._process_with_quantum_brain(user_input)
        else:
            # Generate brain response if original agent's method is not accessible
            coherence = self.original_agent.coherence if hasattr(self.original_agent, 'coherence') else Decimal('0.991800')
            resonance = self.original_agent.resonance if hasattr(self.original_agent, 'resonance') else Decimal('0.618034')
            
            # Generate quantum fingerprint
            fingerprint = f"φ⁷·⁵-{hash(str(coherence) + str(resonance))%16777216:06x}"
            
            # Calculate intelligence and creativity factors
            intelligence_factor = float(coherence) * float(PHI_POWER) / 37.0
            creativity_factor = float(resonance) * float(PHI_POWER) / 37.0
            
            brain_response = {
                'coherence': coherence,
                'resonance': resonance,
                'intelligence_factor': intelligence_factor,
                'creativity_factor': creativity_factor,
                'quantum_fingerprint': fingerprint
            }
        
        # Generate enhanced response
        return self._generate_enhanced_response(user_input, brain_response)
    
    def run_interactive(self):
        """Run interactive session with enhanced agent."""
        print("\n🌟 Phi-Harmonic Quantum Agent Enhanced Interactive Session")
        print("=======================================================")
        print("Type 'exit' or 'quit' to end the session")
        print("Type 'status' to view the agent status")
        print("Type 'compare' to compare with original agent")
        print("Type 'help' to view these commands again")
        print("=======================================================\n")
        
        while True:
            # Get user input
            user_input = input("\n👤 You: ")
            
            # Check for commands
            if user_input.lower() in ['exit', 'quit']:
                print("\n🌟 Ending session. Goodbye!")
                break
            elif user_input.lower() == 'status':
                self._print_status()
                continue
            elif user_input.lower() == 'compare':
                self._compare_with_original(user_input)
                continue
            elif user_input.lower() == 'help':
                print("\n🌟 Commands:")
                print("  'exit' or 'quit' - End the session")
                print("  'status' - View the agent status")
                print("  'compare' - Compare with original agent")
                print("  'help' - View these commands")
                continue
            
            # Process user input
            print("\n🧠 Processing...")
            agent_response = self.process_input(user_input)
            
            # Print response
            print(f"\n🤖 Agent: {agent_response}")
    
    def _print_status(self):
        """Print enhanced agent status."""
        print("\n📊 Enhanced Agent Status:")
        print(f"  Advanced language model: {'Enabled' if self.use_advanced_language_model else 'Disabled'}")
        print(f"  Response variety: Enabled")
        print(f"  Coherence: {self.coherence:.6f}")
        print(f"  Resonance: {self.resonance:.6f}")
        
        # Print original agent status if available
        if hasattr(self.original_agent, '_print_status'):
            print("\n📊 Original Agent Status:")
            self.original_agent._print_status()
    
    def _compare_with_original(self, user_input):
        """Compare enhanced response with original agent's response."""
        print("\n🔍 Comparing responses for: " + user_input)
        
        # Get original response
        print("\n🧠 Processing with original agent...")
        original_response = self.original_agent.process_input(user_input)
        
        # Get enhanced response
        print("\n🧠 Processing with enhanced agent...")
        enhanced_response = self.process_input(user_input)
        
        # Print comparison
        print("\n📊 Response Comparison:")
        print("\n🤖 Original Agent:")
        print(original_response)
        print("\n🤖 Enhanced Agent:")
        print(enhanced_response)
        
        # Print analysis
        print("\n📈 Analysis:")
        print(f"  Original response length: {len(original_response)} characters")
        print(f"  Enhanced response length: {len(enhanced_response)} characters")
        print(f"  Improvement: {(len(enhanced_response) - len(original_response)) / max(1, len(original_response)) * 100:.2f}%")

def main():
    """Main function."""
    # Create original agent
    original_agent = PhiHarmonicQuantumAgent()
    
    # Create enhanced agent
    enhanced_agent = PhiHarmonicQuantumAgentEnhancer(original_agent)
    
    # Run interactive session
    enhanced_agent.run_interactive()

if __name__ == "__main__":
    main()

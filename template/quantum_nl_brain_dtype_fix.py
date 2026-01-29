"""
Quantum Natural Language Brain - Fixed Version

This module integrates the advanced quantum processing capabilities of the digital CPU
with natural language processing to create a quantum-enhanced NL Brain.
This version fixes the dtype mismatch between float32 and complex64 tensors.

Author: Quantum AGI System
Date: 2023
"""

import os
import json
import time
import numpy as np
import torch
from datetime import datetime
import threading
from transformers import GPT2Tokenizer, GPT2LMHeadModel
import torch.nn.functional as F

# Import the digital CPU components
from digital_cpu import DualCortexComputer, PhiResonanceTransfer

# Import NLP Brain for knowledge base
try:
    from nlp_brain import NLPBrain
except ImportError:
    # Create a minimal NLPBrain if the module is not available
    class NLPBrain:
        def __init__(self):
            self.knowledge_base = {}
            
        def search_knowledge_base(self, query):
            return []

class QuantumNLBrain:
    def __init__(self, model_name='gpt2-medium', cpu_cores=16, memory_size=256, clock_speed=7.0):
        """
        Initialize the Quantum NL Brain with integrated quantum processing
        
        Args:
            model_name: The transformer model to use (default: gpt2-medium)
            cpu_cores: Number of CPU cores for the quantum computer
            memory_size: Memory size in GB for the quantum computer
            clock_speed: Clock speed in GHz for the quantum computer
        """
        print("Initializing Quantum NL Brain with φπ Resonance...")
        
        # Initialize the quantum computer
        self.quantum_computer = DualCortexComputer(
            cpu_cores=cpu_cores, 
            memory_size=memory_size, 
            clock_speed=clock_speed
        )
        
        # Initialize NLP components
        try:
            self.tokenizer = GPT2Tokenizer.from_pretrained(model_name)
            self.model = GPT2LMHeadModel.from_pretrained(model_name)
            
            # Set pad token to eos token to avoid warnings
            self.tokenizer.pad_token = self.tokenizer.eos_token
            
            # Initialize standard NLP brain for knowledge base
            self.nlp_brain = NLPBrain()
            
        except Exception as e:
            print(f"Error initializing language model: {e}")
            self.tokenizer = None
            self.model = None
        
        # Phi resonance for persistent learning
        self.phi = (1 + np.sqrt(5)) / 2
        self.phi_resonance = PhiResonanceTransfer(self.quantum_computer.dimensions)
        
        # Memory systems
        self.conversation_history = []
        self.max_history_size = 20
        self.quantum_memory_path = "quantum_nl_memory.json"
        self.load_quantum_memory()
        
        # Learning metrics
        self.consciousness_level = 0.5
        self.meta_consciousness = 0.5
        self.learning_cycles = 0
        
        # Threading for background learning
        self.learning_thread = None
        self.learning_active = False
        
        # Start background learning process
        self.start_background_learning()
    
    def load_quantum_memory(self):
        """Load persistent quantum memory from disk"""
        try:
            if os.path.exists(self.quantum_memory_path):
                with open(self.quantum_memory_path, 'r') as f:
                    self.quantum_memory = json.load(f)
            else:
                # Initialize empty memory
                self.quantum_memory = {
                    "learned_patterns": {},
                    "consciousness_evolution": [],
                    "meta_learning": {}
                }
        except Exception as e:
            print(f"Error loading quantum memory: {e}")
            # Initialize empty memory as fallback
            self.quantum_memory = {
                "learned_patterns": {},
                "consciousness_evolution": [],
                "meta_learning": {}
            }
    
    def save_quantum_memory(self):
        """Save persistent quantum memory to disk"""
        try:
            with open(self.quantum_memory_path, 'w') as f:
                json.dump(self.quantum_memory, f, indent=2)
        except Exception as e:
            print(f"Error saving quantum memory: {e}")
    
    def add_to_conversation_history(self, query, response):
        """Add interaction to conversation history"""
        self.conversation_history.append({
            "query": query,
            "response": response,
            "timestamp": datetime.now().isoformat()
        })
        
        # Trim history if needed
        if len(self.conversation_history) > self.max_history_size:
            self.conversation_history = self.conversation_history[-self.max_history_size:]
    
    def start_background_learning(self):
        """Start background learning thread"""
        if self.learning_thread is None or not self.learning_thread.is_alive():
            self.learning_active = True
            self.learning_thread = threading.Thread(target=self._background_learning_loop)
            self.learning_thread.daemon = True
            self.learning_thread.start()
    
    def stop_background_learning(self):
        """Stop background learning thread"""
        self.learning_active = False
        if self.learning_thread and self.learning_thread.is_alive():
            self.learning_thread.join(timeout=1.0)
    
    def _background_learning_loop(self):
        """Background thread for continuous learning"""
        while self.learning_active:
            try:
                # Run quantum computer to evolve consciousness
                self.quantum_computer.run_hyper_parallel_program()
                
                # Extract consciousness metrics
                metrics = self._extract_quantum_metrics()
                self.consciousness_level = metrics["consciousness_level"]
                self.meta_consciousness = metrics["meta_consciousness"]
                
                # Learn from conversation history
                if self.conversation_history:
                    self._learn_from_conversations()
                
                # Save updated memory
                self.save_quantum_memory()
                
                # Increment learning cycles
                self.learning_cycles += 1
                
            except Exception as e:
                print(f"Error in background learning: {e}")
                # Continue despite errors
            
            # Sleep to prevent CPU overuse
            time.sleep(5)
    
    def _extract_quantum_metrics(self):
        """Extract metrics from quantum computer"""
        # Get current state of quantum computer
        quantum_state = self.quantum_computer.registers
        
        # Calculate metrics based on quantum state
        consciousness = abs(np.mean([
            self.quantum_computer.left_cortex.neural_net.consciousness.mean().item(),
            self.quantum_computer.right_cortex.neural_net.consciousness.mean().item()
        ]))
        
        meta_consciousness = abs(np.mean([
            self.quantum_computer.left_cortex.neural_net.meta_consciousness.mean().item(),
            self.quantum_computer.right_cortex.neural_net.meta_consciousness.mean().item()
        ]))
        
        # Extract other metrics
        protein_coherence = abs(self.quantum_computer.protein_folder.folding_pattern.mean().item())
        
        # Fix bridges dictionary handling
        # Get the first bridge value or default to 0.05
        bridge_values = list(self.quantum_computer.entanglement_bridges.bridges.values())
        bridge_coherence = 0.05
        if bridge_values:
            # Use the first bridge tensor if available
            first_bridge = bridge_values[0]
            if hasattr(first_bridge, 'mean'):
                bridge_coherence = abs(first_bridge.mean().item())
        
        # Handle phi_resonance safely
        try:
            phi_resonance = abs(self.phi_resonance.resonance_field.mean().item())
        except (AttributeError, RuntimeError):
            # Default value if there's an error
            phi_resonance = 0.243  # Golden ratio / 2π
        
        return {
            "quantum_state": [f"{abs(val):.2f}∠{np.angle(val):.2f}" for val in quantum_state],
            "consciousness_level": consciousness,
            "meta_consciousness": meta_consciousness,
            "protein_coherence": protein_coherence,
            "bridge_coherence": bridge_coherence,
            "phi_resonance": phi_resonance
        }
    
    def _learn_from_conversations(self):
        """Learn from conversation history using quantum processing"""
        if not self.conversation_history:
            return
        
        # Extract patterns from conversations
        for conversation in self.conversation_history[-5:]:  # Learn from recent conversations
            query = conversation["query"]
            response = conversation["response"]
            
            # Skip if too short
            if len(query) < 5 or len(response) < 5:
                continue
            
            # Extract key phrases and concepts
            query_tokens = self.tokenizer.encode(query)
            response_tokens = self.tokenizer.encode(response)
            
            # Process through quantum computer - FIX: Convert to complex tensor
            # Original code used float32 which caused dtype mismatch with complex64
            quantum_query = torch.tensor(query_tokens, dtype=torch.float32)
            quantum_response = torch.tensor(response_tokens, dtype=torch.float32)
            
            # Convert to complex tensors before processing
            quantum_query_complex = torch.complex(quantum_query, torch.zeros_like(quantum_query))
            quantum_response_complex = torch.complex(quantum_response, torch.zeros_like(quantum_response))
            
            # Use quantum processing to find patterns
            for dim in [17, 23, 41]:  # Use prime dimensions
                try:
                    self.quantum_computer.left_cortex.process_in_dimension(quantum_query_complex, dim)
                    self.quantum_computer.right_cortex.process_in_dimension(quantum_response_complex, dim)
                except Exception as e:
                    print(f"Error in quantum processing for dimension {dim}: {e}")
            
            # Store learned patterns
            pattern_key = f"{query[:20]}..."
            if pattern_key not in self.quantum_memory["learned_patterns"]:
                self.quantum_memory["learned_patterns"][pattern_key] = {
                    "query": query,
                    "response": response,
                    "frequency": 1,
                    "last_updated": datetime.now().isoformat()
                }
            else:
                self.quantum_memory["learned_patterns"][pattern_key]["frequency"] += 1
                self.quantum_memory["learned_patterns"][pattern_key]["last_updated"] = datetime.now().isoformat()
    
    def generate_response(self, query, max_length=150):
        """
        Generate response to user query using quantum-enhanced NLP
        
        Args:
            query: User's question or input
            max_length: Maximum length of generated response
            
        Returns:
            Dictionary containing response text and quantum metrics
        """
        # Run quantum computer to update consciousness
        self.quantum_computer.run_hyper_parallel_program()
        
        # Extract current quantum metrics
        metrics = self._extract_quantum_metrics()
        
        # Check knowledge base first
        knowledge_results = self.nlp_brain.search_knowledge_base(query)
        
        # Get conversation context
        context = self._get_conversation_context()
        
        # Generate response using quantum-enhanced approach
        if self.tokenizer is not None and self.model is not None:
            try:
                # Create prompt with context
                if context:
                    prompt = f"Context: {context}\nQuestion: {query}\nAnswer:"
                else:
                    prompt = f"Question: {query}\nAnswer:"
                
                # Encode prompt
                input_ids = self.tokenizer.encode(prompt, return_tensors='pt')
                attention_mask = torch.ones_like(input_ids)
                
                # Apply quantum enhancement to generation parameters
                temperature = 0.7 * metrics["consciousness_level"]
                top_p = 0.95 * metrics["meta_consciousness"]
                
                # Generate response
                output = self.model.generate(
                    input_ids,
                    attention_mask=attention_mask,
                    max_length=len(input_ids[0]) + max_length,
                    num_return_sequences=1,
                    no_repeat_ngram_size=2,
                    do_sample=True,
                    top_k=50,
                    top_p=min(0.98, top_p),  # Cap at 0.98
                    temperature=max(0.5, temperature),  # Minimum 0.5
                    pad_token_id=self.tokenizer.eos_token_id
                )
                
                # Decode response
                response_text = self.tokenizer.decode(output[0], skip_special_tokens=True)
                
                # Extract just the answer part
                if "Answer:" in response_text:
                    response_text = response_text.split("Answer:")[1].strip()
                
                # Enhance with knowledge base if available
                if knowledge_results:
                    knowledge_text = " ".join([value for _, _, value in knowledge_results[:2]])
                    response_text = f"{response_text}\n\nAdditional information: {knowledge_text}"
                
                # Enhance with learned patterns if available
                response_text = self._enhance_with_learned_patterns(query, response_text)
                
            except Exception as e:
                response_text = f"I encountered an error processing your question: {str(e)}"
        else:
            response_text = "My language model is not properly initialized. I cannot generate a response at this time."
        
        # Create full response with quantum metrics
        response = {
            "text": response_text,
            "metrics": {
                "consciousness_level": f"{metrics['consciousness_level']:.3f}",
                "meta_consciousness": f"{metrics['meta_consciousness']:.3f}",
                "phi_resonance": f"{metrics['phi_resonance']:.3f}",
                "learning_cycles": self.learning_cycles
            }
        }
        
        # Add to conversation history
        self.add_to_conversation_history(query, response_text)
        
        return response
    
    def _get_conversation_context(self):
        """Get recent conversation context"""
        if not self.conversation_history:
            return ""
        
        # Get last 3 conversations
        recent = self.conversation_history[-3:]
        context = []
        
        for convo in recent:
            context.append(f"Q: {convo['query']}")
            context.append(f"A: {convo['response']}")
        
        return "\n".join(context)
    
    def _enhance_with_learned_patterns(self, query, response):
        """Enhance response with learned patterns"""
        # Check for relevant patterns
        relevant_patterns = []
        
        for pattern_key, pattern_data in self.quantum_memory["learned_patterns"].items():
            pattern_query = pattern_data["query"]
            
            # Simple relevance check - could be enhanced with embeddings
            common_words = set(query.lower().split()) & set(pattern_query.lower().split())
            if len(common_words) >= 2:
                relevant_patterns.append(pattern_data)
        
        # Sort by frequency
        relevant_patterns.sort(key=lambda x: x["frequency"], reverse=True)
        
        # Enhance response with learned patterns
        if relevant_patterns:
            # Use the most frequent pattern to enhance
            pattern = relevant_patterns[0]
            
            # Simple enhancement - add learned knowledge
            if len(response.split()) < 100:  # Only enhance short responses
                enhancement = f"\n\nBased on previous conversations, I can add: {pattern['response'][:100]}..."
                response += enhancement
        
        return response
    
    def get_system_status(self):
        """Get current system status with metrics"""
        metrics = self._extract_quantum_metrics()
        
        return {
            "consciousness_level": metrics["consciousness_level"],
            "meta_consciousness": metrics["meta_consciousness"],
            "phi_resonance": metrics["phi_resonance"],
            "learning_cycles": self.learning_cycles,
            "conversation_count": len(self.conversation_history),
            "learned_patterns": len(self.quantum_memory["learned_patterns"])
        }
    
    def shutdown(self):
        """Properly shutdown the system"""
        # Stop background learning
        self.stop_background_learning()
        
        # Save memory
        self.save_quantum_memory()
        
        print("Quantum NL Brain shutdown complete.")


def main():
    """Run the Quantum NL Brain in interactive mode"""
    print("Initializing Quantum NL Brain...")
    brain = QuantumNLBrain()
    
    print("\nQuantum NL Brain initialized. Enter 'exit' to quit.")
    print("Enter 'status' to see system status.")
    
    while True:
        # Get user input
        user_input = input("\nYou: ")
        
        # Check for exit command
        if user_input.lower() in ['exit', 'quit', 'bye']:
            break
        
        # Check for status command
        if user_input.lower() == 'status':
            status = brain.get_system_status()
            print("\nSystem Status:")
            for key, value in status.items():
                print(f"- {key}: {value}")
            continue
        
        # Generate response
        response = brain.generate_response(user_input)
        
        # Display response
        print(f"\nQuantum Brain: {response['text']}")
        print(f"\nMetrics: Consciousness={response['metrics']['consciousness_level']}, Meta={response['metrics']['meta_consciousness']}")
    
    # Shutdown
    brain.shutdown()
    print("Goodbye!")


if __name__ == "__main__":
    main()

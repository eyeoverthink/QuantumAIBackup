import torch
from fraymus_brain import FraymusBrain
from typing import Optional, Dict, List, Any, Tuple
import numpy as np
import json
import time
from transformers import GPT2LMHeadModel, GPT2Tokenizer
from collections import deque

class FraymusAgent:
    """
    Advanced AI agent that combines quantum neural processing with
    natural language understanding and generation.
    """
    
    def __init__(self):
        """Initialize the Fraymus Agent."""
        # Initialize the brain
        self.brain = FraymusBrain()
        
        # Initialize language model
        try:
            self.tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
            self.language_model = GPT2LMHeadModel.from_pretrained('gpt2')
            
            # Configure tokenizer
            self.tokenizer.pad_token = self.tokenizer.eos_token
            self.tokenizer.padding_side = 'left'
            
            # Move model to GPU if available
            if torch.cuda.is_available():
                self.language_model = self.language_model.cuda()
            self.language_model.eval()  # Set to evaluation mode
        except Exception as e:
            print(f"Warning: Could not initialize GPT-2. Using fallback mode. Error: {e}")
            self.tokenizer = None
            self.language_model = None
        
        # Knowledge base categories
        self.knowledge_base = {
            'physics': set(),
            'mathematics': set(),
            'quantum_mechanics': set(),
            'computing': set(),
            'general': set()
        }
        
        # Interaction state
        self.conversation_history = []
        self.current_context = None
        self.last_response = None
        
        # Performance tracking
        self.performance_history = deque(maxlen=100)
        self.coherence_threshold = 0.6
        
        # Load initial knowledge
        self._initialize_knowledge()
        
    def process_input(self, user_input: str) -> Dict[str, Any]:
        """Process user input and generate a response."""
        # Update conversation history
        self.conversation_history.append({
            'role': 'user',
            'content': user_input,
            'timestamp': time.time()
        })
        
        try:
            # Generate quantum thought pattern
            thought_result = self.brain.think(user_input)
            
            # Extract relevant knowledge
            knowledge = self._retrieve_relevant_knowledge(user_input, thought_result)
            
            # Generate response using language model
            response = self._generate_response(user_input, thought_result, knowledge)
            
            # Learn from interaction
            self._learn_from_interaction(user_input, thought_result, response)
            
            # Update state
            self.last_response = response
            self.current_context = thought_result.get('context')
            
            # Track performance
            coherence = thought_result.get('coherence', 0.0)
            self.performance_history.append(coherence)
            
            return {
                'response': response,
                'thought_pattern': thought_result.get('patterns', {}),
                'coherence': coherence,
                'context': self.current_context
            }
            
        except Exception as e:
            print(f"Error processing input: {e}")
            return {
                'response': "I apologize, but I encountered an error processing your input.",
                'thought_pattern': {},
                'coherence': 0.0,
                'context': None
            }
    
    def update_knowledge(self, category: str, information: str) -> bool:
        """
        Add new information to the knowledge base.
        """
        if category in self.knowledge_base:
            # Process information through brain first
            thought_result = self.brain.think(information)
            
            if thought_result['coherence'] > self.coherence_threshold:
                self.knowledge_base[category].add(information)
                return True
                
        return False
    
    def _initialize_knowledge(self) -> None:
        """
        Initialize the knowledge base with fundamental concepts.
        """
        # Physics knowledge
        physics_concepts = [
            "E = mc² describes mass-energy equivalence",
            "Quantum entanglement allows instant correlation between particles",
            "The uncertainty principle limits simultaneous measurement of conjugate variables"
        ]
        for concept in physics_concepts:
            self.update_knowledge('physics', concept)
        
        # Mathematics knowledge
        math_concepts = [
            f"The golden ratio φ = {(1 + 5 ** 0.5) / 2} is found throughout nature",
            "π represents the ratio of a circle's circumference to its diameter",
            "e is the base of natural logarithms"
        ]
        for concept in math_concepts:
            self.update_knowledge('mathematics', concept)
        
        # Quantum mechanics knowledge
        quantum_concepts = [
            "Quantum superposition allows particles to exist in multiple states",
            "Wave-particle duality is a fundamental principle of quantum mechanics",
            "Quantum tunneling enables particles to pass through potential barriers"
        ]
        for concept in quantum_concepts:
            self.update_knowledge('quantum_mechanics', concept)
    
    def _retrieve_relevant_knowledge(
        self, 
        user_input: str, 
        thought_result: Dict[str, Any]
    ) -> List[str]:
        """
        Retrieve relevant knowledge based on input and thought patterns.
        """
        relevant_knowledge = []
        
        if self.tokenizer is None:
            return relevant_knowledge
            
        # Convert input to tokens for comparison
        input_tokens = set(self.tokenizer.encode(user_input))
        
        # Check each knowledge category
        for category, knowledge_set in self.knowledge_base.items():
            for knowledge in knowledge_set:
                # Calculate token overlap
                knowledge_tokens = set(self.tokenizer.encode(knowledge))
                overlap = len(input_tokens & knowledge_tokens) / len(input_tokens | knowledge_tokens)
                
                # Check quantum resonance
                knowledge_pattern = self.brain.cortex.process_signal(knowledge)
                resonance = self.brain._calculate_pattern_similarity(
                    knowledge_pattern,
                    thought_result['patterns']
                )
                
                # Combine classical and quantum relevance
                relevance = (overlap + resonance) / 2
                
                if relevance > self.coherence_threshold:
                    relevant_knowledge.append(knowledge)
        
        return relevant_knowledge
    
    def _generate_response(
        self,
        user_input: str,
        thought_result: Dict[str, Any],
        knowledge: List[str]
    ) -> str:
        """Generate a response using the language model and quantum thought patterns."""
        try:
            # Prepare context for language model
            context = self._prepare_context(user_input, thought_result, knowledge)
            
            # Generate initial response
            if self.tokenizer is None or self.language_model is None:
                return "I apologize, but I am currently operating in fallback mode."
                
            # Encode context with attention mask
            encoding = self.tokenizer(
                context,
                return_tensors='pt',
                padding=True,
                truncation=True,
                max_length=512
            )
            
            # Move to GPU if available
            if torch.cuda.is_available():
                encoding = {k: v.cuda() for k, v in encoding.items()}
            
            # Generate response
            with torch.no_grad():
                outputs = self.language_model.generate(
                    input_ids=encoding['input_ids'],
                    attention_mask=encoding['attention_mask'],
                    max_length=150,
                    num_return_sequences=1,
                    no_repeat_ngram_size=2,
                    do_sample=True,
                    top_k=50,
                    top_p=0.95,
                    temperature=0.7,
                    pad_token_id=self.tokenizer.pad_token_id
                )
            
            # Decode response
            response = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
            
            # Extract only the assistant's response
            response = response.split("Assistant:")[-1].strip()
            
            # Enhance response with quantum patterns
            if thought_result.get('patterns'):
                enhanced_response = self._enhance_response_with_quantum_patterns(
                    response,
                    thought_result['patterns']
                )
                if enhanced_response:
                    response = enhanced_response
            
            return response
            
        except Exception as e:
            print(f"Error generating response: {e}")
            return "I apologize, but I encountered an error generating a response."
    
    def _prepare_context(
        self,
        user_input: str,
        thought_result: Dict[str, Any],
        knowledge: List[str]
    ) -> str:
        """
        Prepare context for language model input.
        """
        # Combine recent conversation history
        recent_history = self.conversation_history[-5:]  # Last 5 exchanges
        history_text = "\n".join([
            f"{'User' if h['role'] == 'user' else 'Assistant'}: {h['content']}"
            for h in recent_history
        ])
        
        # Add relevant knowledge
        knowledge_text = "\nRelevant information:\n" + "\n".join(knowledge) if knowledge else ""
        
        # Combine all context
        context = f"{history_text}{knowledge_text}\nUser: {user_input}\nAssistant:"
        
        return context
    
    def _enhance_response_with_quantum_patterns(
        self,
        response: str,
        thought_patterns: Dict[str, Any]
    ) -> Optional[str]:
        """
        Enhance the language model response with quantum thought patterns.
        """
        try:
            # Process response through quantum cortex
            quantum_response = self.brain.cortex.process_signal(response)
            
            # Calculate coherence with original thought patterns
            coherence = self.brain._calculate_pattern_similarity(
                quantum_response,
                thought_patterns
            )
            
            # If coherence is high, return original response
            if coherence > self.coherence_threshold:
                return response
                
            # Otherwise, try to enhance the response
            enhanced_pattern = self.brain._recursive_think(quantum_response)
            
            # Convert enhanced pattern back to text
            if self.tokenizer is not None and self.language_model is not None:
                return self._pattern_to_text(enhanced_pattern)
            
            return None
            
        except Exception as e:
            print(f"Warning: Error enhancing response: {e}")
            return None
    
    def _pattern_to_text(self, pattern: np.ndarray) -> Optional[str]:
        """
        Convert a quantum pattern back to text using the language model.
        """
        try:
            if self.tokenizer is None or self.language_model is None:
                return None
                
            # Normalize pattern
            pattern = pattern / (np.linalg.norm(pattern) + 1e-8)
            
            # Convert to tensor
            pattern_tensor = torch.tensor(pattern).float()
            if torch.cuda.is_available():
                pattern_tensor = pattern_tensor.cuda()
            
            # Generate text
            with torch.no_grad():
                outputs = self.language_model.generate(
                    pattern_tensor.unsqueeze(0),
                    max_length=100,
                    num_return_sequences=1,
                    do_sample=True,
                    top_k=50,
                    top_p=0.95,
                    temperature=0.7
                )
            
            # Decode response
            text = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
            
            return text
            
        except Exception as e:
            print(f"Warning: Error converting pattern to text: {e}")
            return None
    
    def _learn_from_interaction(
        self,
        user_input: str,
        thought_result: Dict[str, Any],
        response: str
    ) -> None:
        """
        Learn from the interaction to improve future responses.
        """
        # Create experience dictionary
        experience = {
            'pattern': thought_result['patterns'],
            'context': {
                'input': user_input,
                'response': response,
                'coherence': thought_result['coherence']
            },
            'outcome': {
                'success': thought_result['coherence'] > self.coherence_threshold,
                'timestamp': time.time()
            }
        }
        
        # Update brain's learning
        self.brain.learn(experience)
        
        # Update knowledge base if high coherence
        if thought_result['coherence'] > self.coherence_threshold:
            # Try to categorize and store the interaction
            for category in self.knowledge_base:
                if any(word in user_input.lower() for word in category.split('_')):
                    self.update_knowledge(category, f"{user_input} → {response}")

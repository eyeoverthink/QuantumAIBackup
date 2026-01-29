"""
Test suite for LLM Enhancement components.
"""

import unittest
from unittest.mock import Mock, patch
from quantum_collective.llm_enhancement.response_generator import ResponseGenerator
from quantum_collective.llm_enhancement.context_handler import ContextHandler

class TestResponseGenerator(unittest.TestCase):
    def setUp(self):
        """Set up test components with mocked quantum parts."""
        self.mock_observer = Mock()
        self.mock_witness = Mock()
        self.mock_actor = Mock()
        self.response_gen = ResponseGenerator(
            self.mock_observer,
            self.mock_witness,
            self.mock_actor
        )

    def test_generate_response(self):
        """Test basic response generation."""
        # Setup test data
        test_input = "What is quantum computing?"
        test_context = {"domain": "quantum_physics"}
        
        # Mock quantum component responses
        self.mock_observer.create_superposition.return_value = {
            "states": ["Response 1", "Response 2"],
            "probabilities": [0.6, 0.4]
        }
        self.mock_witness.validate_states.return_value = {
            "valid_states": ["Response 1"],
            "scores": [0.9]
        }
        self.mock_actor.collapse_states.return_value = {
            "response_text": "Quantum computing uses quantum mechanics.",
            "confidence": 0.95
        }

        # Test response generation
        response, confidence = self.response_gen.generate_response(
            test_input,
            test_context
        )
        
        self.assertIsInstance(response, str)
        self.assertIsInstance(confidence, float)
        self.assertGreater(confidence, 0.9)

    def test_multi_brain_response(self):
        """Test response generation across multiple brain types."""
        test_input = "Explain quantum entanglement."
        test_context = {"domain": "physics"}
        
        # Mock responses for different brain types
        self.mock_actor.collapse_states.side_effect = [
            {"response_text": f"Response from {brain}", "confidence": 0.9}
            for brain in ['sync', 'quantum', 'particle', 'learner']
        ]

        responses = self.response_gen.generate_multi_brain_response(
            test_input,
            test_context
        )
        
        self.assertEqual(len(responses), 4)
        for brain_type in ['sync', 'quantum', 'particle', 'learner']:
            self.assertIn(brain_type, responses)
            response, confidence = responses[brain_type]
            self.assertIsInstance(response, str)
            self.assertIsInstance(confidence, float)

class TestContextHandler(unittest.TestCase):
    def setUp(self):
        """Set up test components with mocked quantum parts."""
        self.mock_observer = Mock()
        self.mock_witness = Mock()
        self.mock_actor = Mock()
        self.context_handler = ContextHandler(
            self.mock_observer,
            self.mock_witness,
            self.mock_actor
        )

    def test_process_context(self):
        """Test context processing."""
        test_context = {
            "input": "test query",
            "domain": "science",
            "complexity": "advanced"
        }
        
        # Mock quantum component responses
        self.mock_observer.create_superposition.return_value = {
            "states": [test_context],
            "probabilities": [1.0]
        }
        self.mock_witness.validate_states.return_value = {
            "valid_states": [test_context],
            "scores": [0.95]
        }
        self.mock_actor.collapse_states.return_value = {
            "context": test_context
        }

        processed_context = self.context_handler.process_context(test_context)
        
        self.assertIsInstance(processed_context, dict)
        self.assertEqual(processed_context["domain"], "science")

    def test_merge_contexts(self):
        """Test context merging."""
        context1 = {"domain": "physics", "level": "basic"}
        context2 = {"domain": "quantum", "complexity": "high"}
        
        # Mock quantum component responses
        self.mock_observer.create_superposition.return_value = {
            "states": [{"domain": "quantum_physics", "level": "basic", "complexity": "high"}],
            "probabilities": [1.0]
        }
        self.mock_witness.validate_states.return_value = {
            "valid_states": [{"domain": "quantum_physics", "level": "basic", "complexity": "high"}],
            "scores": [0.95]
        }
        self.mock_actor.collapse_states.return_value = {
            "context": {"domain": "quantum_physics", "level": "basic", "complexity": "high"}
        }

        merged = self.context_handler.merge_contexts([context1, context2])
        
        self.assertIsInstance(merged, dict)
        self.assertIn("domain", merged)
        self.assertIn("level", merged)
        self.assertIn("complexity", merged)

if __name__ == '__main__':
    unittest.main()

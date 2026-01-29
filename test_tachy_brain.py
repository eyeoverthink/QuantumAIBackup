"""
Test Tachyon-Brain Integration
"""

import unittest
import numpy as np
from quantum_observer import QuantumObserver
from quantum_witness import QuantumWitness
from quantum_actor import QuantumActor
from quantum_integration.tachy_brain_interface import TachyBrainInterface

class TestTachyBrainIntegration(unittest.TestCase):
    """Test the integration between parallel tachyon operations and brain architectures"""
    
    def setUp(self):
        """Set up test components"""
        self.observer = QuantumObserver()
        self.witness = QuantumWitness()
        self.actor = QuantumActor()
        
        # Initialize interfaces for different brain types
        self.sync_interface = TachyBrainInterface(
            self.observer, self.witness, self.actor, "sync_brain"
        )
        self.quantum_interface = TachyBrainInterface(
            self.observer, self.witness, self.actor, "quantum_brain"
        )
        self.particle_interface = TachyBrainInterface(
            self.observer, self.witness, self.actor, "particle_brain"
        )
        self.learner_interface = TachyBrainInterface(
            self.observer, self.witness, self.actor, "learner_brain"
        )
        
    def test_quantum_state_processing(self):
        """Test quantum state processing across brain types"""
        test_state = {
            'text': 'Process this quantum state',
            'metadata': {
                'brain_type': 'quantum_brain',
                'coherence': 0.8,
                'stability': 0.7,
                'alignment': 0.6,
                'probability': 0.9
            }
        }
        
        # Test each brain type
        sync_result = self.sync_interface.process_quantum_state(test_state)
        self.assertIsInstance(sync_result, dict)
        self.assertIn('wave_coherence', sync_result['metadata'])
        self.assertIn('transform_stability', sync_result['metadata'])
        self.assertIn('original_alignment', sync_result['metadata'])
        
        quantum_result = self.quantum_interface.process_quantum_state(test_state)
        self.assertIsInstance(quantum_result, dict)
        self.assertGreater(quantum_result['metadata']['wave_coherence'], 0)
        
        particle_result = self.particle_interface.process_quantum_state(test_state)
        self.assertIsInstance(particle_result, dict)
        self.assertGreater(particle_result['metadata']['transform_stability'], 0)
        
        learner_result = self.learner_interface.process_quantum_state(test_state)
        self.assertIsInstance(learner_result, dict)
        self.assertGreater(learner_result['metadata']['original_alignment'], -1)
        self.assertLess(learner_result['metadata']['original_alignment'], 1)
        
    def test_resonance_processing(self):
        """Test resonance processing between quantum states"""
        test_states = [
            {
                'text': 'First quantum state',
                'metadata': {
                    'brain_type': 'quantum_brain',
                    'coherence': 0.8,
                    'stability': 0.7
                }
            },
            {
                'text': 'Second quantum state',
                'metadata': {
                    'brain_type': 'quantum_brain',
                    'coherence': 0.6,
                    'stability': 0.9
                }
            }
        ]
        
        # Test resonance with each brain type
        sync_results = self.sync_interface.process_resonance(test_states)
        self.assertEqual(len(sync_results), 2)
        self.assertIn('resonance_pattern', sync_results[0]['metadata'])
        self.assertIn('frequency_stability', sync_results[0]['metadata'])
        
        quantum_results = self.quantum_interface.process_resonance(test_states)
        self.assertEqual(len(quantum_results), 2)
        self.assertGreater(quantum_results[0]['metadata']['resonance_pattern'], 0)
        
        particle_results = self.particle_interface.process_resonance(test_states)
        self.assertEqual(len(particle_results), 2)
        self.assertGreater(particle_results[0]['metadata']['frequency_stability'], 0)
        
        learner_results = self.learner_interface.process_resonance(test_states)
        self.assertEqual(len(learner_results), 2)
        self.assertGreater(learner_results[0]['metadata']['resonance_pattern'], 0)
        
    def test_signal_conversion(self):
        """Test text to signal conversion"""
        test_text = "Test signal conversion"
        
        # Test with each brain type
        sync_signal = self.sync_interface._text_to_signal(test_text)
        self.assertEqual(len(sync_signal), 1000)
        self.assertGreaterEqual(np.min(sync_signal), -1)
        self.assertLessEqual(np.max(sync_signal), 1)
        
        quantum_signal = self.quantum_interface._text_to_signal(test_text)
        self.assertEqual(len(quantum_signal), 1000)
        self.assertGreaterEqual(np.min(quantum_signal), -1)
        self.assertLessEqual(np.max(quantum_signal), 1)
        
        # Test empty text
        empty_signal = self.quantum_interface._text_to_signal("")
        self.assertEqual(len(empty_signal), 1000)
        self.assertTrue(np.allclose(empty_signal, 0))
        
if __name__ == '__main__':
    unittest.main()

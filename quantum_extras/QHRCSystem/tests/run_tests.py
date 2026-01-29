"""
QHRC System Test Runner
Runs all tests and validates quantum-harmonic resonance
"""

import sys
import os
from pathlib import Path
import asyncio
import unittest

# Add project root to path
project_root = Path(__file__).parent.parent
sys.path.append(str(project_root))

# Import test modules
from unified_rsa_test import UnifiedRSATest
from qhrc_validation_test import QHRCValidationTest

class QHRCTestSuite(unittest.TestCase):
    """Test suite for QHRC system"""
    
    async def test_unified_rsa(self):
        """Test unified RSA analysis"""
        rsa_test = UnifiedRSATest()
        
        # Test RSA-2048
        number = "32317006071311007300714876688669951960444102669715484032130345427524655138867890893197201411522913463688717960921898019494119559150490921095088152386448283120630877367300996091750197750389652106796057638384067568276792218642619756161838094338476170470581645852036305042887575891541065808607552399123930385521914333389668342420684974786564569494856176033225140723895455713892550926726189892363407836425979824566669415625075522896322846584764491457069201784848029438319908845472528754980696130751547033"
        
        results = await rsa_test.analyze_rsa_number(number)
        
        # Validate quantum results
        for brain in results['quantum']:
            self.assertGreater(brain['resonance'], 1.0, "Resonance must be > 1 for self-sustaining")
            self.assertAlmostEqual(brain['coherence'], 0.618034, places=6, msg="Coherence must be φ⁻¹")
            self.assertGreater(brain['energy'], 1.5, "Energy transfer must be > 1.5")
        
        # Validate neural results
        self.assertIn('tesla', results['neural']['frequencies'])
        self.assertAlmostEqual(results['neural']['frequencies']['tesla'], 369.0, places=2)
        
        # Validate bridge strengths
        for bridge, strength in results['bridges'].items():
            self.assertAlmostEqual(strength, 0.6755, places=3, msg=f"Bridge {bridge} strength incorrect")
    
    def test_qhrc_validation(self):
        """Test QHRC validation"""
        validation = QHRCValidationTest()
        
        # Test frequencies
        self.assertAlmostEqual(validation.base_freq, 4.37, places=2, msg="Base frequency incorrect")
        self.assertAlmostEqual(validation.space_freq, 2960.72, places=2, msg="Space frequency incorrect")
        self.assertAlmostEqual(validation.energy_freq, 4790.45, places=2, msg="Energy frequency incorrect")
        self.assertAlmostEqual(validation.infinity_freq, 7750.95, places=2, msg="Infinity frequency incorrect")

async def run_tests():
    """Run all tests"""
    # Create test suite
    suite = unittest.TestLoader().loadTestsFromTestCase(QHRCTestSuite)
    
    # Run tests
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)

if __name__ == "__main__":
    asyncio.run(run_tests())

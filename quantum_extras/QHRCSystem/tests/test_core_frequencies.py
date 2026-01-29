"""
Test core QHRC frequencies and resonance
Start with proven frequencies (4.37 Hz = 0.96 resonance)
"""

import sys
import os
from pathlib import Path
import unittest
import numpy as np

# Add project root to path
project_root = Path(__file__).parent.parent
sys.path.append(str(project_root))

# Import core components
from core.qhrc_phi_harmonics import QHRCPhiHarmonics

class TestCoreFrequencies(unittest.TestCase):
    """Test core QHRC frequencies"""
    
    def setUp(self):
        """Initialize QHRC"""
        self.qhrc = QHRCPhiHarmonics()
        self.phi = (1 + np.sqrt(5)) / 2
    
    def test_base_frequency(self):
        """Test base frequency (4.37 Hz)"""
        self.assertAlmostEqual(self.qhrc.base_freq, 4.37, places=2,
                             msg="Base frequency must be 4.37 Hz")
    
    def test_resonance(self):
        """Test resonance (0.96)"""
        resonance = self.qhrc.calculate_resonance(self.qhrc.base_freq)
        self.assertAlmostEqual(resonance, 0.96, places=2,
                             msg="Base resonance must be 0.96")
    
    def test_phi_scaling(self):
        """Test phi-scaled frequencies"""
        # Test φ scaling
        phi_freq = self.qhrc.base_freq * self.phi
        phi_resonance = self.qhrc.calculate_resonance(phi_freq)
        self.assertGreater(phi_resonance, 0.96,
                          msg="φ-scaled resonance must be > 0.96")
        
        # Test φ² scaling
        phi2_freq = self.qhrc.base_freq * (self.phi ** 2)
        phi2_resonance = self.qhrc.calculate_resonance(phi2_freq)
        self.assertGreater(phi2_resonance, phi_resonance,
                          msg="φ²-scaled resonance must be > φ-scaled")
    
    def test_harmonic_series(self):
        """Test harmonic series"""
        harmonics = self.qhrc.generate_harmonic_series(max_order=7)
        
        # Test increasing resonance
        prev_resonance = 0
        for harmonic in harmonics:
            curr_resonance = self.qhrc.calculate_resonance(harmonic)
            self.assertGreater(curr_resonance, prev_resonance,
                             msg="Harmonic resonance must increase")
            prev_resonance = curr_resonance

if __name__ == "__main__":
    unittest.main()

"""
Unit Test: ΦNet TauObserver
Author: Vaughn Scott
Date: April 21, 2025
"""

import unittest
from ΦNet_core import PhiNetCore

class TestTauObserver(unittest.TestCase):

    def setUp(self):
        self.core = PhiNetCore()

    def test_tau_parameter_output(self):
        # Sample test case
        program_signature = 123456789
        coherence = 0.89
        result = self.core.calculate_tau_parameter(program_signature, coherence)

        # Check required keys exist
        for key in [
            "tau_base", "tau_protected", "tau_final",
            "termination_probability", "spoof_check_mod105"
        ]:
            self.assertIn(key, result)

        # Check ranges
        self.assertTrue(0 <= result["termination_probability"] <= 1)
        self.assertIsInstance(result["spoof_check_mod105"], int)

    def test_tau_changes_with_coherence(self):
        sig = 123456789
        low = self.core.calculate_tau_parameter(sig, 0.2)["tau_final"]
        high = self.core.calculate_tau_parameter(sig, 0.9)["tau_final"]
        self.assertGreater(high, low)

    def test_spoof_check(self):
        sig = 105 * 999999  # divisible by 105
        result = self.core.calculate_tau_parameter(sig, 0.75)
        self.assertEqual(result["spoof_check_mod105"], 0)

if __name__ == "__main__":
    unittest.main()

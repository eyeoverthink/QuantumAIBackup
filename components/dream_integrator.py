import numpy as np

# Golden Ratio
PHI = (1 + 5 ** 0.5) / 2
PHI_RESONANCE_THRESHOLD = 0.01 # Corresponds to > 0.99 or < 0.01

class DreamIntegrator:
    """
    Analyzes dream anomalies and proposes paradigm shifts if they exhibit high phi-resonance.
    A paradigm shift involves changing the system's core 'base_multiple'.
    """

    def analyze_dream(self, anomaly_value, location, current_base_multiple):
        """
        Analyzes a dream anomaly.

        Args:
            anomaly_value (int): The anomalous value from the dream.
            location (int): The location (index) where the anomaly occurred.
            current_base_multiple (int): The system's current base multiple.

        Returns:
            dict: A dictionary containing the analysis result.
                  Keys: 'resonance', 'insight', 'new_base_multiple'.
        """
        resonance = (PHI * anomaly_value) % 1
        analysis = {
            'resonance': resonance,
            'insight': 'Discarded',
            'new_base_multiple': None
        }

        if resonance < PHI_RESONANCE_THRESHOLD or resonance > (1 - PHI_RESONANCE_THRESHOLD):
            analysis['insight'] = 'Integrated'
            
            # Propose a paradigm shift: a new base_multiple
            if location > 0:
                # The dream might be revealing a new underlying rule.
                # What if the base_multiple was different?
                proposed_new_base = anomaly_value / location
                
                # In a more complex system, we could check for harmonic simplicity.
                # For now, we accept the new base to demonstrate the cognitive leap.
                analysis['new_base_multiple'] = proposed_new_base
                analysis['insight'] = 'Paradigm Shift'

        return analysis

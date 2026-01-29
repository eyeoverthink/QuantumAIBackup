import numpy as np
from typing import Dict, List, Tuple, Any
from tesla_tacky_integration_ext import TeslaTackyIntegrationExt

class TeslaTackyPatternCounter(TeslaTackyIntegrationExt):
    """Extended Tesla Tacky Integration with pattern counting"""
    
    def __init__(self):
        super().__init__()
        self._pattern_counts = {
            'frontal': 0,
            'temporal': 0, 
            'parietal': 0
        }
        
    def store_pattern(self, pattern: np.ndarray, cortex: str = 'all') -> None:
        """Store pattern and update counter"""
        result = super().store_pattern(pattern, cortex)
        
        if cortex == 'all':
            for c in self._pattern_counts:
                self._pattern_counts[c] += 1
        else:
            self._pattern_counts[cortex] += 1
            
        return result
        
    def get_system_state(self) -> Dict[str, Any]:
        """Get system state with pattern counts"""
        state = super().get_system_state()
        
        # Update pattern counts in state
        for cortex_id, count in self._pattern_counts.items():
            state['cortices'][cortex_id]['patterns_stored'] = count
            
        return state

    def process_input(self, data: np.ndarray) -> np.ndarray:
        """Process input data"""
        # Store input as pattern
        self.store_pattern(data)
        return data

"""
Data Weight Calculator Adapter
===========================
Calculates the weight of data for memory systems without external dependencies.
"""

import numpy as np
import json
from typing import Dict, List, Tuple, Any, Optional, Union

# Constants
PHI = (1 + np.sqrt(5)) / 2  # Golden ratio
PHI_INV = 1 / PHI          # Inverse golden ratio

class DataWeightCalculatorAdapter:
    """Calculates the weight of data for memory systems"""
    
    def __init__(self):
        """Initialize the data weight calculator"""
        self.phi = PHI
        self.base_weight = 1.0
        self.type_weights = {
            'dict': self.phi,
            'list': self.phi_inv,
            'str': self.phi_inv**2,
            'int': self.phi_inv**3,
            'float': self.phi_inv**3,
            'bool': self.phi_inv**4,
            'None': self.phi_inv**5
        }
    
    @property
    def phi_inv(self):
        """Inverse of phi"""
        return PHI_INV
    
    def calculate_weight(self, data: Any) -> float:
        """
        Calculate the weight of data
        
        Args:
            data: Data to calculate weight for
            
        Returns:
            Weight of data
        """
        # Get data type
        data_type = type(data).__name__
        
        # Calculate base weight based on type
        if data_type in self.type_weights:
            weight = self.base_weight * self.type_weights[data_type]
        else:
            weight = self.base_weight
        
        # Adjust weight based on data size/complexity
        if data_type == 'dict':
            # For dictionaries, consider both keys and values
            key_weight = sum(self.calculate_weight(k) for k in data.keys())
            value_weight = sum(self.calculate_weight(v) for v in data.values())
            weight += (key_weight + value_weight) * self.phi_inv
        elif data_type == 'list' or data_type == 'tuple':
            # For lists/tuples, consider all elements
            element_weight = sum(self.calculate_weight(item) for item in data)
            weight += element_weight * self.phi_inv
        elif data_type == 'str':
            # For strings, consider length and complexity
            length_factor = min(len(data), 1000) / 1000  # Cap at 1000 chars
            unique_chars = len(set(data)) / 256  # Normalize by max possible chars
            weight += (length_factor + unique_chars) * self.phi
        elif data_type == 'int' or data_type == 'float':
            # For numbers, consider magnitude
            try:
                magnitude = min(abs(float(data)), 1e10) / 1e10  # Cap at 10^10
                weight += magnitude * self.phi_inv
            except (ValueError, OverflowError):
                weight += 0.5 * self.phi_inv
        
        return weight
    
    def calculate_normalized_weight(self, data: Any, max_weight: float = 10.0) -> float:
        """
        Calculate normalized weight of data
        
        Args:
            data: Data to calculate weight for
            max_weight: Maximum weight to normalize to
            
        Returns:
            Normalized weight of data
        """
        raw_weight = self.calculate_weight(data)
        
        # Normalize using phi-harmonic sigmoid function
        normalized = (2 / (1 + np.exp(-raw_weight * self.phi_inv))) - 1
        
        # Scale to max_weight
        return normalized * max_weight
    
    def calculate_weight_distribution(self, data_list: List[Any]) -> Dict:
        """
        Calculate weight distribution for a list of data items
        
        Args:
            data_list: List of data items
            
        Returns:
            Dictionary with weight distribution metrics
        """
        if not data_list:
            return {
                'mean_weight': 0.0,
                'max_weight': 0.0,
                'min_weight': 0.0,
                'total_weight': 0.0,
                'weights': []
            }
        
        # Calculate weights
        weights = [self.calculate_weight(item) for item in data_list]
        
        # Calculate distribution metrics
        mean_weight = np.mean(weights)
        max_weight = np.max(weights)
        min_weight = np.min(weights)
        total_weight = np.sum(weights)
        
        return {
            'mean_weight': float(mean_weight),
            'max_weight': float(max_weight),
            'min_weight': float(min_weight),
            'total_weight': float(total_weight),
            'weights': [float(w) for w in weights]
        }
    
    def serialize_with_weight(self, data: Any) -> Dict:
        """
        Serialize data with weight information
        
        Args:
            data: Data to serialize
            
        Returns:
            Dictionary with serialized data and weight
        """
        try:
            # Calculate weight
            weight = self.calculate_weight(data)
            
            # Serialize data
            if isinstance(data, (dict, list, tuple, str, int, float, bool)) or data is None:
                serialized = data
            else:
                # Try to convert to dictionary
                try:
                    serialized = vars(data)
                except:
                    serialized = str(data)
            
            return {
                'data': serialized,
                'weight': weight,
                'type': type(data).__name__
            }
        except Exception as e:
            # Fallback for non-serializable data
            return {
                'data': str(data),
                'weight': self.base_weight,
                'type': type(data).__name__,
                'error': str(e)
            }


# Create singleton instance
data_weight_calculator = DataWeightCalculatorAdapter()


def get_data_weight_calculator():
    """Get the DataWeightCalculatorAdapter instance"""
    return data_weight_calculator

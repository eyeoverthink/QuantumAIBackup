"""
Data Weight Calculation System
Converts digital data to physical weight equivalents
"""

import numpy as np
from typing import Dict

class DataWeightCalculator:
    def __init__(self):
        # Constants
        self.paper_density = 750  # kg/m³ (average paper density)
        self.ink_density = 1300   # kg/m³ (average ink density)
        self.byte_volume = 1e-15  # m³/byte (estimated volume per byte)
        self.phi = 1.61803398875  # Golden ratio
        
        # Conversion factors
        self.byte_to_kg = self.byte_volume * 1000  # kg/byte
        self.page_weight = 4.5e-3  # kg/page (average A4 page)
        self.ink_per_page = 1e-3   # kg/page (average ink)
        
    def calculate_physical_weight(self, pages: int) -> float:
        """Calculate physical weight of paper and ink"""
        # Paper weight (gsm * area * pages / 1000000)
        paper_weight = (80 * 0.21 * 0.297 * pages) / 1000000  # A4 paper, 80gsm
        
        # Ink weight (average 0.5g per page)
        ink_weight = 0.5 * pages
        
        # Binding weight (average 10g per 100 pages)
        binding_weight = (pages / 100) * 10
        
        return (paper_weight + ink_weight + binding_weight) / 1000  # Convert to kg
        
    def calculate_digital_weight(self, data: any) -> float:
        """Calculate weight equivalent of digital data"""
        # Base weight from volume (estimated 1e-15 m³/byte)
        data_size = len(data) if isinstance(data, (str, list, dict)) else 1
        base_weight = data_size * 1e-15 * 1000  # Convert to kg
        
        # Add complexity weight based on data type
        if isinstance(data, str):
            # Text has lower complexity
            complexity_factor = 0.8
        elif isinstance(data, (list, dict)):
            # Structured data has medium complexity
            complexity_factor = 1.2
        else:
            # Binary data has high complexity
            complexity_factor = 1.5
            
        # Add entropy-based weight
        entropy_weight = self._calculate_entropy(data) * 1e-18
        
        # Add quantum resonance weight
        resonance_weight = self._calculate_resonance(data) * 1e-20
        
        return (base_weight + entropy_weight + resonance_weight) * complexity_factor
        
    def _calculate_entropy(self, data: any) -> float:
        """Calculate data entropy as a weight factor"""
        if isinstance(data, str):
            # String entropy
            unique_chars = len(set(data))
            entropy = (unique_chars / len(data)) if len(data) > 0 else 0
        elif isinstance(data, (list, dict)):
            # Structured data entropy
            entropy = len(set(str(x) for x in data)) / len(data) if data else 0
        else:
            # Binary entropy
            entropy = 1.0
            
        return entropy
        
    def _calculate_resonance(self, data: any) -> float:
        """Calculate quantum resonance as a weight factor"""
        if isinstance(data, str):
            # String resonance (based on character frequencies)
            freqs = [data.count(c) for c in set(data)]
            resonance = sum(f * f for f in freqs) / len(data) if len(data) > 0 else 0
        elif isinstance(data, (list, dict)):
            # Structured data resonance (based on value distribution)
            values = [x for x in data if isinstance(x, (int, float))]
            resonance = np.std(values) / len(values) if values else 0
        else:
            # Binary resonance (based on bit patterns)
            bits = bin(data)[2:] if isinstance(data, int) else ''
            resonance = bits.count('1') / len(bits) if bits else 0
            
        return resonance * self.phi
        
    def calculate_weight_ratio(self, physical_weight: float, digital_weight: float) -> float:
        """Calculate the weight ratio between physical and digital"""
        return digital_weight / physical_weight if physical_weight > 0 else 1.0
        
    def get_weight_factors(self, data, pages: int = 0) -> Dict:
        """Get all weight factors for compression"""
        # Calculate physical weight if pages provided
        physical_weight = self.calculate_physical_weight(pages) if pages > 0 else 0
        
        # Calculate digital weight
        digital_weight = self.calculate_digital_weight(data)
        
        # Calculate weight ratio
        weight_ratio = self.calculate_weight_ratio(physical_weight, digital_weight)
        
        return {
            'physical_weight': physical_weight,
            'digital_weight': digital_weight,
            'weight_ratio': weight_ratio,
            'complexity_factor': 1.0  # Base complexity
        }

def test_weight_calculator():
    """Test the weight calculator"""
    calc = DataWeightCalculator()
    
    # Test PDF document
    pdf_pages = 500
    pdf_physical_weight = calc.calculate_physical_weight(pdf_pages)
    print(f"500-page PDF physical weight: {pdf_physical_weight:.3f} kg")
    
    # Test digital data
    test_data = "A" * 1024  # 1KB of text
    digital_weight = calc.calculate_digital_weight(test_data)
    print(f"1KB text digital weight: {digital_weight:.3e} kg")
    
    # Test weight ratio
    weight_ratio = calc.calculate_weight_ratio(pdf_physical_weight, digital_weight)
    print(f"Weight ratio (digital/physical): {weight_ratio:.3f}")
    
    # Test complete factors
    factors = calc.get_weight_factors(test_data, pdf_pages)
    print("\nComplete weight factors:")
    for key, value in factors.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    test_weight_calculator()

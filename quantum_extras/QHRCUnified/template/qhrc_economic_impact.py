"""
QHRC Economic Impact Analysis
Calculates energy cost savings and grid impact
"""
import numpy as np
from typing import Dict

class QHRCEconomicAnalysis:
    def __init__(self):
        # Current energy costs (2025)
        self.kwh_cost = 0.35  # Average US cost per kWh
        self.phi = (1 + np.sqrt(5)) / 2
        
        # Your optimized parameters
        self.k = 0.85  # Coupling
        self.alpha = 0.75  # Energy recapture
        self.beta = 0.002  # Damping
        
    def calculate_savings(self, power: float, hours: float = 24) -> Dict:
        """Calculate daily energy savings."""
        # Calculate energy generation
        kwh = power * hours / 1000  # Convert W to kWh
        
        # Calculate cost savings
        daily_savings = kwh * self.kwh_cost
        monthly_savings = daily_savings * 30
        yearly_savings = monthly_savings * 12
        
        return {
            'daily_kwh': kwh,
            'daily_savings': daily_savings,
            'monthly_savings': monthly_savings,
            'yearly_savings': yearly_savings
        }
        
    def analyze_configurations(self) -> None:
        """Analyze different QHRC configurations."""
        print("\n💰 QHRC Economic Analysis")
        print("=====================")
        
        configs = [
            {'coils': 8, 'power': 623.97},
            {'coils': 9, 'power': 1631.50},
            {'coils': 10, 'power': 4263.98},
            {'coils': 11, 'power': 11142.13},
            {'coils': 12, 'power': 29113.37},
            {'coils': 13, 'power': 76068.69}
        ]
        
        for config in configs:
            savings = self.calculate_savings(config['power'])
            
            print(f"\n{config['coils']}-Coil Configuration:")
            print(f"Power Output: {config['power']:.2f}W")
            print(f"Daily Generation: {savings['daily_kwh']:.2f} kWh")
            print(f"Daily Savings: ${savings['daily_savings']:.2f}")
            print(f"Monthly Savings: ${savings['monthly_savings']:.2f}")
            print(f"Yearly Savings: ${savings['yearly_savings']:.2f}")
            
            if savings['yearly_savings'] > 10000:
                print("🌟 HIGH-VALUE CONFIGURATION")
                
            # Calculate grid impact
            homes_powered = savings['daily_kwh'] / 30  # Average home uses 30kWh/day
            print(f"Homes Powered: {homes_powered:.1f}")

if __name__ == "__main__":
    # Run economic analysis
    analysis = QHRCEconomicAnalysis()
    analysis.analyze_configurations()

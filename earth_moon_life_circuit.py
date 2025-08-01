"""
Earth-Moon Life Energy Circuit Simulator
Models the phi-harmonic resonance between Earth's Fe-Ni core and Moon's gravitational field,
showing how they create a natural life-sustaining energy circuit.
"""

import numpy as np
import torch
from typing import Dict, Tuple
import matplotlib.pyplot as plt

class EarthMoonCircuit:
    def __init__(self):
        self.phi = (1 + np.sqrt(5)) / 2
        
        # Natural frequencies (Hz)
        self.frequencies = {
            'Schumann': 7.83,      # Earth's resonance
            'Lunar': 4.83,         # Moon's tidal frequency ≈ 7.83/φ
            'Core': 12.66,         # Earth core frequency ≈ 7.83*φ
            'Life': 6.18          # Life frequency ≈ φ⁴
        }
        
        # Field components
        self.earth_core = {
            'Fe': 0.845,          # Iron
            'Ni': 0.055,          # Nickel (φ⁻⁴)
            'Resonance': self.phi  # Core resonance
        }
        
        self.moon_field = {
            'Gravity': 1/self.phi,  # Gravitational coupling
            'Phase': 2*np.pi/self.phi,  # Phase alignment
            'Distance': 384400      # Average distance in km
        }
        
    def calculate_life_field(self, time: float) -> Dict[str, float]:
        """Calculate the life energy field at a given time"""
        # Earth's core contribution
        earth_field = (self.earth_core['Fe'] * np.cos(2*np.pi*self.frequencies['Core']*time) +
                      self.earth_core['Ni'] * np.cos(2*np.pi*self.frequencies['Schumann']*time))
        
        # Moon's contribution
        moon_field = (self.moon_field['Gravity'] * 
                     np.cos(2*np.pi*self.frequencies['Lunar']*time + self.moon_field['Phase']))
        
        # Life energy resonance
        life_resonance = np.cos(2*np.pi*self.frequencies['Life']*time)
        
        # Combined field with phi-harmonic coupling
        total_field = (earth_field * self.phi + moon_field) * life_resonance
        
        # Calculate various energy components
        physical = np.abs(earth_field)                    # Physical energy (Earth)
        emotional = np.abs(moon_field)                    # Emotional energy (Moon)
        spiritual = np.abs(life_resonance)                # Spiritual energy (Life)
        vitality = np.abs(total_field)                    # Total vitality
        
        return {
            'physical': physical,
            'emotional': emotional,
            'spiritual': spiritual,
            'vitality': vitality,
            'earth_field': earth_field,
            'moon_field': moon_field,
            'life_resonance': life_resonance
        }
    
    def find_resonance_points(self, duration: float = 24.0, steps: int = 1000) -> Dict[str, list]:
        """Find resonance points over time period (hours)"""
        times = np.linspace(0, duration, steps)
        results = {
            'times': times,
            'physical': [],
            'emotional': [],
            'spiritual': [],
            'vitality': []
        }
        
        for t in times:
            field = self.calculate_life_field(t)
            results['physical'].append(field['physical'])
            results['emotional'].append(field['emotional'])
            results['spiritual'].append(field['spiritual'])
            results['vitality'].append(field['vitality'])
            
        return results
    
    def visualize_circuit(self, results: Dict[str, list], save_path: str = 'life_circuit.png'):
        """Visualize the Earth-Moon life energy circuit"""
        plt.figure(figsize=(15, 10))
        
        # Plot energy components
        plt.subplot(2, 1, 1)
        plt.plot(results['times'], results['physical'], 'r-', 
                label='Physical (Earth)', alpha=0.7)
        plt.plot(results['times'], results['emotional'], 'b-', 
                label='Emotional (Moon)', alpha=0.7)
        plt.plot(results['times'], results['spiritual'], 'g-', 
                label='Spiritual (Life)', alpha=0.7)
        plt.plot(results['times'], results['vitality'], 'k--', 
                label='Total Vitality', linewidth=2)
        
        plt.xlabel('Time (hours)')
        plt.ylabel('Energy Level')
        plt.title('Earth-Moon Life Energy Circuit')
        plt.grid(True)
        plt.legend()
        
        # Plot phi-harmonic levels
        plt.subplot(2, 1, 2)
        times = results['times']
        vitality = np.array(results['vitality'])
        
        # Calculate moving averages at different phi scales
        windows = [int(len(times)/self.phi**n) for n in range(1, 5)]
        for i, w in enumerate(windows):
            if w > 1:
                avg = np.convolve(vitality, np.ones(w)/w, mode='valid')
                plt.plot(times[w-1:], avg, 
                        label=f'φ⁻{i+1} Resonance', alpha=0.7)
        
        plt.xlabel('Time (hours)')
        plt.ylabel('Resonance Level')
        plt.title('Phi-Harmonic Resonance Patterns')
        plt.grid(True)
        plt.legend()
        
        plt.tight_layout()
        plt.savefig(save_path)
        plt.close()

def main():
    print("🌍 🌕 Initializing Earth-Moon Life Circuit")
    circuit = EarthMoonCircuit()
    
    # Calculate resonance over 24 hours
    print("\n📊 Calculating life energy resonance...")
    results = circuit.find_resonance_points()
    
    # Find peak times
    vitality = np.array(results['vitality'])
    peak_indices = np.where(vitality > np.percentile(vitality, 90))[0]
    peak_times = results['times'][peak_indices]
    
    print("\n⚡ Peak Vitality Times (hours):")
    for time in peak_times[:5]:  # Show first 5 peaks
        print(f"  {time:.2f} hours")
    
    # Calculate average energy levels
    print("\n🔋 Average Energy Levels:")
    print(f"Physical (Earth): {np.mean(results['physical']):.4f}")
    print(f"Emotional (Moon): {np.mean(results['emotional']):.4f}")
    print(f"Spiritual (Life): {np.mean(results['spiritual']):.4f}")
    print(f"Total Vitality: {np.mean(results['vitality']):.4f}")
    
    # Generate visualization
    print("\n🎨 Generating circuit visualization...")
    circuit.visualize_circuit(results)
    
    print("\n✨ Simulation complete!")

if __name__ == "__main__":
    main()

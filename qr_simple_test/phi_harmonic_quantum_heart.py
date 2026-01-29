"""
Phi-Harmonic Quantum Heart System
Creates a quantum heart that operates on golden frequencies and synchronizes
with the brain sync system and quantum clock
"""
import os
import sys
import time
import math
import json
import numpy as np
from decimal import Decimal, getcontext
from datetime import datetime

# Set high precision for calculations
getcontext().prec = 50

# Add parent directory to path to import quantum modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Try to import quantum modules
try:
    from consolidated_quantum.phi_harmonic_quantum_clock import PhiHarmonicQuantumClock
    from consolidated_quantum.phi_harmonic_brain_sync import PhiHarmonicBrainSync
    QUANTUM_MODULES_AVAILABLE = True
except ImportError:
    print("Warning: Quantum modules not available. Limited functionality.")
    QUANTUM_MODULES_AVAILABLE = False

# Constants from quantum reality encoding
PHI = Decimal('1.618033988749895')  # Golden ratio
PHI_POWER = Decimal('36.93238055064198')  # φ^7.5
RESONANCE_RATIO = Decimal('1.3777')  # Resonance ratio
ENERGY_TRANSFER = Decimal('1.8951')  # Energy transfer
BIRTH_COHERENCE_TEMP = Decimal('99.18')  # K
RESONANCE_STACK = RESONANCE_RATIO * ENERGY_TRANSFER  # 2.61087927
PRIMARY_FREQUENCY = Decimal('4790.45')  # Hz
SECONDARY_FREQUENCY = Decimal('7750.95')  # Hz
BIRTH_PATTERN = Decimal('0.29779')
COHERENCE_FACTOR = Decimal('20.155273240572697')

# Heart-specific constants
HEART_PHI_FREQUENCY = Decimal('1.618')  # Base frequency in Hz (φ¹)
HEART_RESONANCE = Decimal('7.83')  # Earth's Schumann resonance
HEART_COHERENCE_THRESHOLD = Decimal('0.618')  # Golden ratio inverse
HEART_CHAKRA_FREQUENCY = Decimal('639')  # Heart chakra frequency in Hz
HEART_RATE_PHI = Decimal('61.8')  # Phi-based heart rate (bpm)
HEART_RATE_PHI_SQUARED = Decimal('99.9')  # φ² * 38.2 (bpm)

class PhiHarmonicQuantumHeart:
    """
    Phi-Harmonic Quantum Heart System that creates a quantum heart operating on
    golden frequencies and synchronizing with the brain sync system and quantum clock.
    """
    
    def __init__(self):
        """Initialize the phi-harmonic quantum heart system."""
        # Initialize quantum components
        self.use_quantum_modules = QUANTUM_MODULES_AVAILABLE
        
        if self.use_quantum_modules:
            self.quantum_clock = PhiHarmonicQuantumClock()
            self.brain_sync = PhiHarmonicBrainSync()
        
        # Initialize quantum state
        self.quantum_state = self._initialize_quantum_state()
        
        # Initialize heart state
        self.heart_state = self._initialize_heart_state()
        
        # Output directory
        self.output_dir = "phi_harmonic_quantum_heart"
        os.makedirs(self.output_dir, exist_ok=True)
        
        print(f"Phi-Harmonic Quantum Heart initialized")
        print(f"Heart phi frequency: {float(HEART_PHI_FREQUENCY):.6f} Hz")
        print(f"Heart resonance: {float(HEART_RESONANCE):.6f} Hz")
        print(f"Heart chakra frequency: {float(HEART_CHAKRA_FREQUENCY):.6f} Hz")
        print(f"Phi heart rate: {float(HEART_RATE_PHI):.6f} bpm")
        print(f"Quantum coherence: {self.quantum_state['coherence']:.6f}")
    
    def _initialize_quantum_state(self):
        """Initialize the quantum state for the heart system."""
        # Get current timestamp
        timestamp = time.time()
        
        # Calculate quantum coherence using birth date pattern
        coherence = float(BIRTH_COHERENCE_TEMP / 100)
        
        # Calculate phi resonance
        phi_resonance = float(PHI * Decimal(str(timestamp)) % Decimal('1'))
        
        # Create quantum state
        quantum_state = {
            "timestamp": timestamp,
            "coherence": coherence,
            "phi_resonance": phi_resonance,
            "resonance_frequency": float(PRIMARY_FREQUENCY + 
                                       (SECONDARY_FREQUENCY - PRIMARY_FREQUENCY) * Decimal(str(phi_resonance))),
            "quantum_fingerprint": f"φ⁷·⁵-{abs(hash(str(timestamp)))%16777216:06x}",
            "dimensions": int(float(PHI_POWER) * 100000)
        }
        
        return quantum_state
    
    def _initialize_heart_state(self):
        """Initialize the heart state."""
        # Calculate heart rate based on phi
        heart_rate = float(HEART_RATE_PHI)
        
        # Calculate heart period
        heart_period = 60.0 / heart_rate
        
        # Calculate heart frequency
        heart_frequency = 1.0 / heart_period
        
        # Calculate heart phi resonance
        heart_phi_resonance = float(PHI * Decimal(str(heart_rate)) % Decimal('1'))
        
        # Calculate heart chakra resonance
        heart_chakra_resonance = float(HEART_CHAKRA_FREQUENCY / 1000)
        
        # Calculate heart coherence
        heart_coherence = float(BIRTH_COHERENCE_TEMP / 100)
        
        # Create heart state
        heart_state = {
            "heart_rate": heart_rate,
            "heart_period": heart_period,
            "heart_frequency": heart_frequency,
            "heart_phi_resonance": heart_phi_resonance,
            "heart_chakra_resonance": heart_chakra_resonance,
            "heart_coherence": heart_coherence,
            "heart_resonance_stack": float(RESONANCE_STACK),
            "heart_quantum_fingerprint": self.quantum_state["quantum_fingerprint"],
            "timestamp": time.time()
        }
        
        return heart_state
    
    def _update_quantum_state(self):
        """Update the quantum state with new quantum information."""
        # Get current timestamp
        timestamp = time.time()
        
        # Update quantum coherence
        self.quantum_state["coherence"] = float(BIRTH_COHERENCE_TEMP / 100)
        
        # Update phi resonance
        self.quantum_state["phi_resonance"] = float(PHI * Decimal(str(timestamp)) % Decimal('1'))
        
        # Update resonance frequency
        self.quantum_state["resonance_frequency"] = float(PRIMARY_FREQUENCY + 
                                                       (SECONDARY_FREQUENCY - PRIMARY_FREQUENCY) * 
                                                       Decimal(str(self.quantum_state["phi_resonance"])))
        
        # Update quantum fingerprint
        self.quantum_state["quantum_fingerprint"] = f"φ⁷·⁵-{abs(hash(str(timestamp)))%16777216:06x}"
        
        # Update timestamp
        self.quantum_state["timestamp"] = timestamp
    
    def _update_heart_state(self, target_rate=None):
        """
        Update heart state based on quantum state and target rate.
        
        Args:
            target_rate (float): Target heart rate
        """
        # Update quantum state
        self._update_quantum_state()
        
        # Determine heart rate if not specified
        if target_rate is None:
            # Use quantum state to determine heart rate
            phi_res = self.quantum_state["phi_resonance"]
            
            if phi_res < 0.2:
                # Resting state (φ * 38.2)
                target_rate = float(HEART_RATE_PHI)
            elif phi_res < 0.4:
                # Meditative state (φ² * 38.2)
                target_rate = float(HEART_RATE_PHI_SQUARED)
            elif phi_res < 0.6:
                # Active state (φ³ * 38.2)
                target_rate = float(PHI**3 * Decimal('38.2'))
            elif phi_res < 0.8:
                # Energetic state (φ⁴ * 38.2)
                target_rate = float(PHI**4 * Decimal('38.2'))
            else:
                # Peak state (φ⁵ * 38.2)
                target_rate = float(PHI**5 * Decimal('38.2'))
        
        # Calculate heart period
        heart_period = 60.0 / target_rate
        
        # Calculate heart frequency
        heart_frequency = 1.0 / heart_period
        
        # Calculate heart phi resonance
        heart_phi_resonance = float(PHI * Decimal(str(target_rate)) % Decimal('1'))
        
        # Calculate heart chakra resonance
        heart_chakra_resonance = float(HEART_CHAKRA_FREQUENCY / 1000)
        
        # Calculate heart coherence
        heart_coherence = float(BIRTH_COHERENCE_TEMP / 100)
        
        # Update heart state
        self.heart_state["heart_rate"] = target_rate
        self.heart_state["heart_period"] = heart_period
        self.heart_state["heart_frequency"] = heart_frequency
        self.heart_state["heart_phi_resonance"] = heart_phi_resonance
        self.heart_state["heart_chakra_resonance"] = heart_chakra_resonance
        self.heart_state["heart_coherence"] = heart_coherence
        self.heart_state["heart_resonance_stack"] = float(RESONANCE_STACK)
        self.heart_state["heart_quantum_fingerprint"] = self.quantum_state["quantum_fingerprint"]
        self.heart_state["timestamp"] = time.time()
    
    def generate_heart_frequencies(self, target_rate=None):
        """
        Generate heart frequencies for heart entrainment.
        
        Args:
            target_rate (float): Target heart rate
            
        Returns:
            dict: Heart frequencies
        """
        # Update heart state
        self._update_heart_state(target_rate)
        
        # Calculate phi-harmonic heart frequencies
        frequencies = []
        for i in range(1, 8):
            frequency = float(PHI**i * HEART_PHI_FREQUENCY)
            frequencies.append({
                "power": i,
                "frequency": frequency,
                "period": 1.0 / frequency,
                "phi_resonance": float(PHI * Decimal(str(frequency)) % Decimal('1')),
                "amplitude": 1.0 / i
            })
        
        # Calculate heart chakra harmonics
        chakra_harmonics = []
        for i in range(1, 5):
            frequency = float(HEART_CHAKRA_FREQUENCY / i)
            chakra_harmonics.append({
                "harmonic": i,
                "frequency": frequency,
                "period": 1.0 / frequency,
                "phi_resonance": float(PHI * Decimal(str(frequency)) % Decimal('1')),
                "amplitude": 1.0 / i
            })
        
        # Calculate Schumann resonance harmonics
        schumann_harmonics = []
        for i in range(1, 8):
            frequency = float(HEART_RESONANCE * i)
            schumann_harmonics.append({
                "harmonic": i,
                "frequency": frequency,
                "period": 1.0 / frequency,
                "phi_resonance": float(PHI * Decimal(str(frequency)) % Decimal('1')),
                "amplitude": 1.0 / i
            })
        
        # Create result
        result = {
            "heart_rate": self.heart_state["heart_rate"],
            "heart_period": self.heart_state["heart_period"],
            "heart_frequency": self.heart_state["heart_frequency"],
            "heart_phi_resonance": self.heart_state["heart_phi_resonance"],
            "heart_chakra_resonance": self.heart_state["heart_chakra_resonance"],
            "heart_coherence": self.heart_state["heart_coherence"],
            "phi_harmonic_frequencies": frequencies,
            "chakra_harmonics": chakra_harmonics,
            "schumann_harmonics": schumann_harmonics,
            "quantum_fingerprint": self.heart_state["heart_quantum_fingerprint"],
            "timestamp": time.time()
        }
        
        return result
    
    def generate_heart_resonance_pattern(self, target_rate=None):
        """
        Generate a heart resonance pattern.
        
        Args:
            target_rate (float): Target heart rate
            
        Returns:
            dict: Heart resonance pattern
        """
        # Generate heart frequencies
        frequencies = self.generate_heart_frequencies(target_rate)
        
        # Calculate heart-brain coherence
        if self.use_quantum_modules:
            # Get brain sync pattern for alpha band (relaxed awareness)
            brain_pattern = self.brain_sync.generate_brain_sync_pattern("alpha")
            
            # Calculate coherence between heart and brain
            heart_brain_coherence = float(self.heart_state["heart_coherence"] * 
                                        brain_pattern["brain_state"]["coherence"])
            
            # Calculate resonance between heart and brain
            heart_brain_resonance = float(self.heart_state["heart_resonance_stack"] * 
                                        float(brain_pattern["brain_state"]["resonance"]))
            
            # Calculate phi alignment between heart and brain
            heart_brain_phi_alignment = float(abs(self.heart_state["heart_phi_resonance"] - 
                                              brain_pattern["brain_state"]["phi_alignment"]))
            
            # Normalize phi alignment (0 = perfect alignment, 1 = worst alignment)
            heart_brain_phi_alignment = 1.0 - heart_brain_phi_alignment
        else:
            # Use simplified calculations if quantum modules not available
            heart_brain_coherence = float(self.heart_state["heart_coherence"])
            heart_brain_resonance = float(self.heart_state["heart_resonance_stack"])
            heart_brain_phi_alignment = float(self.heart_state["heart_phi_resonance"])
        
        # Calculate heart-clock coherence
        if self.use_quantum_modules:
            # Get quantum time
            quantum_time = self.quantum_clock.get_quantum_time()
            
            # Calculate coherence between heart and clock
            heart_clock_coherence = float(self.heart_state["heart_coherence"] * 
                                        float(BIRTH_COHERENCE_TEMP / 100))
            
            # Calculate resonance between heart and clock
            heart_clock_resonance = float(self.heart_state["heart_resonance_stack"] * 
                                        float(RESONANCE_STACK))
            
            # Calculate phi alignment between heart and clock
            heart_clock_phi_alignment = float(abs(self.heart_state["heart_phi_resonance"] - 
                                             float(PHI * Decimal(str(time.time())) % Decimal('1'))))
            
            # Normalize phi alignment (0 = perfect alignment, 1 = worst alignment)
            heart_clock_phi_alignment = 1.0 - heart_clock_phi_alignment
        else:
            # Use simplified calculations if quantum modules not available
            heart_clock_coherence = float(self.heart_state["heart_coherence"])
            heart_clock_resonance = float(self.heart_state["heart_resonance_stack"])
            heart_clock_phi_alignment = float(self.heart_state["heart_phi_resonance"])
            quantum_time = {
                "phi_hours": int(time.time() % 24),
                "phi_minutes": int((time.time() % 3600) / 60),
                "phi_seconds": int(time.time() % 60)
            }
        
        # Create heart resonance pattern
        heart_resonance_pattern = {
            "heart_state": self.heart_state,
            "heart_frequencies": frequencies,
            "heart_brain_coherence": heart_brain_coherence,
            "heart_brain_resonance": heart_brain_resonance,
            "heart_brain_phi_alignment": heart_brain_phi_alignment,
            "heart_clock_coherence": heart_clock_coherence,
            "heart_clock_resonance": heart_clock_resonance,
            "heart_clock_phi_alignment": heart_clock_phi_alignment,
            "quantum_time": quantum_time,
            "quantum_state": self.quantum_state,
            "timestamp": time.time(),
            "iso_timestamp": datetime.now().isoformat()
        }
        
        return heart_resonance_pattern
    
    def generate_heart_field_pattern(self, target_rate=None):
        """
        Generate a heart electromagnetic field pattern.
        
        Args:
            target_rate (float): Target heart rate
            
        Returns:
            dict: Heart field pattern
        """
        # Generate heart resonance pattern
        resonance_pattern = self.generate_heart_resonance_pattern(target_rate)
        
        # Calculate heart field strength based on coherence
        field_strength = float(resonance_pattern["heart_brain_coherence"] * 
                             resonance_pattern["heart_clock_coherence"] * 
                             float(COHERENCE_FACTOR))
        
        # Calculate heart field radius based on resonance
        field_radius = float(resonance_pattern["heart_brain_resonance"] * 
                           resonance_pattern["heart_clock_resonance"] * 
                           float(PHI_POWER))
        
        # Calculate heart field frequency based on phi alignment
        field_frequency = float(resonance_pattern["heart_brain_phi_alignment"] * 
                              resonance_pattern["heart_clock_phi_alignment"] * 
                              float(HEART_CHAKRA_FREQUENCY))
        
        # Calculate heart field coherence
        field_coherence = float(resonance_pattern["heart_state"]["heart_coherence"] * 
                              self.quantum_state["coherence"])
        
        # Calculate heart field resonance
        field_resonance = float(resonance_pattern["heart_state"]["heart_resonance_stack"] * 
                              float(RESONANCE_STACK))
        
        # Calculate heart field phi resonance
        field_phi_resonance = float(resonance_pattern["heart_state"]["heart_phi_resonance"] * 
                                  self.quantum_state["phi_resonance"])
        
        # Create heart field pattern
        heart_field_pattern = {
            "field_strength": field_strength,
            "field_radius": field_radius,
            "field_frequency": field_frequency,
            "field_coherence": field_coherence,
            "field_resonance": field_resonance,
            "field_phi_resonance": field_phi_resonance,
            "resonance_pattern": resonance_pattern,
            "quantum_fingerprint": self.quantum_state["quantum_fingerprint"],
            "timestamp": time.time(),
            "iso_timestamp": datetime.now().isoformat()
        }
        
        return heart_field_pattern
    
    def save_heart_field_pattern(self, pattern=None, output_file=None):
        """
        Save heart field pattern to a file.
        
        Args:
            pattern (dict): Heart field pattern
            output_file (str): Output file path
            
        Returns:
            str: Output file path
        """
        # Generate pattern if not provided
        if pattern is None:
            pattern = self.generate_heart_field_pattern()
        
        # Create output file path
        if output_file is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            output_file = os.path.join(self.output_dir, f"heart_field_pattern_{timestamp}.json")
        
        # Save to file
        with open(output_file, 'w') as f:
            json.dump(pattern, f, indent=2, default=str)
        
        print(f"Heart field pattern saved to {output_file}")
        return output_file
    
    def generate_heart_brain_sync_pattern(self, target_rate=None, target_band="alpha"):
        """
        Generate a heart-brain synchronization pattern.
        
        Args:
            target_rate (float): Target heart rate
            target_band (str): Target neural band
            
        Returns:
            dict: Heart-brain synchronization pattern
        """
        # Generate heart field pattern
        heart_pattern = self.generate_heart_field_pattern(target_rate)
        
        if self.use_quantum_modules:
            # Generate brain sync pattern
            brain_pattern = self.brain_sync.generate_brain_sync_pattern(target_band)
            
            # Calculate heart-brain synchronization
            heart_brain_sync = {
                "coherence": float(heart_pattern["field_coherence"] * 
                                 brain_pattern["brain_state"]["coherence"]),
                "resonance": float(heart_pattern["field_resonance"] * 
                                 float(brain_pattern["brain_state"]["resonance"])),
                "phi_alignment": float(abs(heart_pattern["field_phi_resonance"] - 
                                       brain_pattern["brain_state"]["phi_alignment"])),
                "dominant_band": brain_pattern["dominant_band"],
                "heart_rate": heart_pattern["resonance_pattern"]["heart_state"]["heart_rate"]
            }
            
            # Normalize phi alignment (0 = perfect alignment, 1 = worst alignment)
            heart_brain_sync["phi_alignment"] = 1.0 - heart_brain_sync["phi_alignment"]
        else:
            # Use simplified calculations if quantum modules not available
            heart_brain_sync = {
                "coherence": float(heart_pattern["field_coherence"]),
                "resonance": float(heart_pattern["field_resonance"]),
                "phi_alignment": float(heart_pattern["field_phi_resonance"]),
                "dominant_band": target_band,
                "heart_rate": heart_pattern["resonance_pattern"]["heart_state"]["heart_rate"]
            }
        
        # Create heart-brain synchronization pattern
        heart_brain_sync_pattern = {
            "heart_brain_sync": heart_brain_sync,
            "heart_pattern": heart_pattern,
            "brain_pattern": brain_pattern if self.use_quantum_modules else None,
            "quantum_fingerprint": self.quantum_state["quantum_fingerprint"],
            "timestamp": time.time(),
            "iso_timestamp": datetime.now().isoformat()
        }
        
        return heart_brain_sync_pattern
    
    def save_heart_brain_sync_pattern(self, pattern=None, target_rate=None, target_band="alpha", output_file=None):
        """
        Save heart-brain synchronization pattern to a file.
        
        Args:
            pattern (dict): Heart-brain synchronization pattern
            target_rate (float): Target heart rate
            target_band (str): Target neural band
            output_file (str): Output file path
            
        Returns:
            str: Output file path
        """
        # Generate pattern if not provided
        if pattern is None:
            pattern = self.generate_heart_brain_sync_pattern(target_rate, target_band)
        
        # Create output file path
        if output_file is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            output_file = os.path.join(self.output_dir, f"heart_brain_sync_pattern_{timestamp}.json")
        
        # Save to file
        with open(output_file, 'w') as f:
            json.dump(pattern, f, indent=2, default=str)
        
        print(f"Heart-brain synchronization pattern saved to {output_file}")
        return output_file


def main():
    """Main function for command-line interface."""
    import argparse
    
    parser = argparse.ArgumentParser(description="Phi-Harmonic Quantum Heart System")
    parser.add_argument("--rate", type=float,
                       help="Target heart rate in bpm")
    parser.add_argument("--band", type=str, choices=["delta", "theta", "alpha", "beta", "gamma", "hyper", "quantum", "resonance"],
                       default="alpha", help="Target neural band for heart-brain synchronization")
    parser.add_argument("--field", action="store_true",
                       help="Generate heart field pattern")
    parser.add_argument("--sync", action="store_true",
                       help="Generate heart-brain synchronization pattern")
    parser.add_argument("--save", action="store_true",
                       help="Save generated patterns to files")
    
    args = parser.parse_args()
    
    # Create quantum heart
    heart = PhiHarmonicQuantumHeart()
    
    # Generate heart field pattern
    if args.field:
        field_pattern = heart.generate_heart_field_pattern(args.rate)
        
        # Print field pattern summary
        print(f"Generated heart field pattern:")
        print(f"Field strength: {field_pattern['field_strength']:.6f}")
        print(f"Field radius: {field_pattern['field_radius']:.6f}")
        print(f"Field frequency: {field_pattern['field_frequency']:.6f} Hz")
        print(f"Field coherence: {field_pattern['field_coherence']:.6f}")
        print(f"Field resonance: {field_pattern['field_resonance']:.6f}")
        print(f"Field phi resonance: {field_pattern['field_phi_resonance']:.6f}")
        print(f"Heart rate: {field_pattern['resonance_pattern']['heart_state']['heart_rate']:.6f} bpm")
        
        # Save pattern if requested
        if args.save:
            heart.save_heart_field_pattern(field_pattern)
    
    # Generate heart-brain synchronization pattern
    if args.sync:
        sync_pattern = heart.generate_heart_brain_sync_pattern(args.rate, args.band)
        
        # Print sync pattern summary
        print(f"Generated heart-brain synchronization pattern:")
        print(f"Heart-brain coherence: {sync_pattern['heart_brain_sync']['coherence']:.6f}")
        print(f"Heart-brain resonance: {sync_pattern['heart_brain_sync']['resonance']:.6f}")
        print(f"Heart-brain phi alignment: {sync_pattern['heart_brain_sync']['phi_alignment']:.6f}")
        print(f"Dominant neural band: {sync_pattern['heart_brain_sync']['dominant_band']}")
        print(f"Heart rate: {sync_pattern['heart_brain_sync']['heart_rate']:.6f} bpm")
        
        # Save pattern if requested
        if args.save:
            heart.save_heart_brain_sync_pattern(sync_pattern)
    
    # If no action specified, print information
    if not (args.field or args.sync):
        # Generate heart frequencies
        frequencies = heart.generate_heart_frequencies(args.rate)
        
        # Print heart frequencies
        print(f"Heart rate: {frequencies['heart_rate']:.6f} bpm")
        print(f"Heart period: {frequencies['heart_period']:.6f} s")
        print(f"Heart frequency: {frequencies['heart_frequency']:.6f} Hz")
        print(f"Heart phi resonance: {frequencies['heart_phi_resonance']:.6f}")
        print(f"Heart chakra resonance: {frequencies['heart_chakra_resonance']:.6f}")
        print(f"Heart coherence: {frequencies['heart_coherence']:.6f}")
        
        print("\nPhi-harmonic frequencies:")
        for freq in frequencies["phi_harmonic_frequencies"]:
            print(f"  φ^{freq['power']}: {freq['frequency']:.6f} Hz (period: {freq['period']:.6f} s, resonance: {freq['phi_resonance']:.6f})")
        
        print("\nChakra harmonics:")
        for harmonic in frequencies["chakra_harmonics"]:
            print(f"  1/{harmonic['harmonic']}: {harmonic['frequency']:.6f} Hz (period: {harmonic['period']:.6f} s, resonance: {harmonic['phi_resonance']:.6f})")
        
        print("\nSchumann resonance harmonics:")
        for harmonic in frequencies["schumann_harmonics"]:
            print(f"  {harmonic['harmonic']}x: {harmonic['frequency']:.6f} Hz (period: {harmonic['period']:.6f} s, resonance: {harmonic['phi_resonance']:.6f})")
        
        # Save pattern if requested
        if args.save:
            resonance_pattern = heart.generate_heart_resonance_pattern(args.rate)
            heart.save_heart_field_pattern(heart.generate_heart_field_pattern(args.rate))


if __name__ == "__main__":
    main()

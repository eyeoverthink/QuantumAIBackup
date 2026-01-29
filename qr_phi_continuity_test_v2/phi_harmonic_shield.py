#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Phi-Harmonic Shield Module

Creates a phi-resonant electromagnetic field that cancels non-harmonic environmental noise
to reduce quantum decoherence and enhance phi-resonance.
"""

import numpy as np
import time
import logging
from datetime import datetime
from typing import List, Tuple, Dict, Any, Optional

# Set up logging
logging.basicConfig(level=logging.INFO, 
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger('phi_harmonic_shield')

class PhiHarmonicShield:
    """
    Creates a phi-resonant electromagnetic shield to protect against
    environmental noise and enhance quantum coherence.
    """
    
    def __init__(self, resonance_level: float = 0.95):
        """
        Initialize the phi-harmonic shield with specified resonance level.
        
        Args:
            resonance_level: Target resonance level (0.0-1.0)
        """
        self.phi = (1 + np.sqrt(5)) / 2
        self.phi_inv = 1 / self.phi
        self.resonance_level = resonance_level
        self.shield_patterns = self._generate_shield_patterns()
        self.active = False
        self.start_time = None
        self.noise_profile = None
        
        logger.info(f"Phi-Harmonic Shield initialized (target resonance: {resonance_level:.4f})")
        
    def _generate_shield_patterns(self) -> List[Tuple[float, float]]:
        """Generate counter-resonance patterns based on golden ratio"""
        patterns = []
        
        # Use Fibonacci numbers for pattern generation
        fibonacci = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
        
        for i in range(len(fibonacci) - 1):
            # Calculate frequency based on Fibonacci ratio
            frequency = self.phi ** (i % 5)
            
            # Calculate phase based on golden angle
            golden_angle = 2 * np.pi * (1 - 1/self.phi)
            phase = golden_angle * i
            
            # Store as (frequency, phase) tuple
            patterns.append((frequency, phase))
        
        logger.debug(f"Generated {len(patterns)} shield patterns")
        return patterns
    
    def analyze_environment(self) -> Dict[str, Any]:
        """
        Scan for non-harmonic electromagnetic interference.
        
        Returns:
            Dict containing detected noise sources and their frequencies
        """
        # In a real implementation, this would use sensors to detect EM fields
        # For simulation, we'll create synthetic noise sources
        
        # Common noise frequencies (WiFi, Bluetooth, power lines, etc.)
        common_frequencies = {
            'wifi_2.4ghz': 2.4e9,
            'wifi_5ghz': 5.0e9,
            'bluetooth': 2.45e9,
            'power_lines': 60.0,
            'cell_phones': 8.5e8,
            'microwave': 2.45e9
        }
        
        # Measure noise levels (simulated)
        noise_levels = {}
        for source, freq in common_frequencies.items():
            # Calculate phi-dissonance (how far from phi-harmonic)
            resonant_freq = self.phi ** (int(np.log(freq) / np.log(self.phi)))
            dissonance = abs(freq - resonant_freq) / freq
            
            # Higher dissonance = more interference
            interference_level = np.random.uniform(0.1, 0.9) * dissonance
            noise_levels[source] = interference_level
        
        # Determine overall noise profile
        total_interference = sum(noise_levels.values())
        resonance_impact = min(1.0, total_interference)
        
        noise_profile = {
            'timestamp': datetime.now().isoformat(),
            'sources': noise_levels,
            'total_interference': total_interference,
            'resonance_impact': resonance_impact,
            'estimated_decoherence': resonance_impact * 0.5
        }
        
        self.noise_profile = noise_profile
        logger.info(f"Environmental analysis complete. Detected {len(noise_levels)} noise sources")
        return noise_profile
    
    def adaptive_shielding(self, noise_profile: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Adjust shield patterns based on detected noise.
        
        Args:
            noise_profile: Noise profile from analyze_environment (optional)
            
        Returns:
            Optimized shield configuration
        """
        if noise_profile is None:
            if self.noise_profile is None:
                self.noise_profile = self.analyze_environment()
            noise_profile = self.noise_profile
        
        shield_config = {
            'patterns': [],
            'phi_resonance': 0.0,
            'coverage': 0.0,
            'energy_required': 0.0
        }
        
        # Adjust shield patterns for each noise source
        for source, level in noise_profile['sources'].items():
            if level > 0.1:  # Only counter significant noise
                # Find most phi-resonant counter frequency
                source_freq = 0
                if source == 'wifi_2.4ghz': source_freq = 2.4e9
                elif source == 'wifi_5ghz': source_freq = 5.0e9
                elif source == 'bluetooth': source_freq = 2.45e9
                elif source == 'power_lines': source_freq = 60.0
                elif source == 'cell_phones': source_freq = 8.5e8
                elif source == 'microwave': source_freq = 2.45e9
                
                # Get nearest phi-resonant frequency
                resonant_freq = source_freq * self.phi_inv
                
                # Calculate optimal phase (out of phase by golden angle)
                golden_angle = 2 * np.pi * (1 - 1/self.phi)
                optimal_phase = np.pi + golden_angle
                
                # Calculate required intensity based on noise level
                intensity = level * 1.618
                
                shield_config['patterns'].append({
                    'source': source,
                    'noise_freq': source_freq,
                    'counter_freq': resonant_freq,
                    'phase': optimal_phase,
                    'intensity': intensity
                })
        
        # Calculate overall shield metrics
        if shield_config['patterns']:
            total_sources = len(noise_profile['sources'])
            shield_config['coverage'] = len(shield_config['patterns']) / total_sources
            shield_config['energy_required'] = sum(p['intensity'] for p in shield_config['patterns'])
            shield_config['phi_resonance'] = self._calculate_shield_resonance(shield_config)
        
        logger.info(f"Adaptive shielding configured. Coverage: {shield_config['coverage']:.2f}, " 
                   f"Resonance: {shield_config['phi_resonance']:.4f}")
        return shield_config
    
    def _calculate_shield_resonance(self, shield_config: Dict[str, Any]) -> float:
        """Calculate phi-resonance of the shield configuration"""
        if not shield_config['patterns']:
            return 0.0
        
        # Start with base resonance
        resonance = self.phi_inv
        
        # Adjust based on pattern coverage and alignment
        pattern_resonances = []
        for pattern in shield_config['patterns']:
            # How close counter frequency is to a phi-multiple
            freq_resonance = 1.0 - abs((pattern['counter_freq'] * self.phi) % 1)
            
            # How close phase is to golden angle
            golden_angle = 2 * np.pi * (1 - 1/self.phi)
            phase_resonance = 1.0 - abs((pattern['phase'] / golden_angle) % 1)
            
            pattern_resonance = (freq_resonance + phase_resonance) / 2
            pattern_resonances.append(pattern_resonance)
        
        # Overall resonance is combination of individual resonances
        if pattern_resonances:
            avg_resonance = sum(pattern_resonances) / len(pattern_resonances)
            resonance = self.phi_inv + (1 - self.phi_inv) * avg_resonance
        
        return min(resonance, 0.99)
    
    def activate(self, duration: Optional[float] = None) -> Dict[str, Any]:
        """
        Activate the phi-harmonic shield for specified duration.
        
        Args:
            duration: Shield duration in seconds (None for indefinite)
            
        Returns:
            Shield status information
        """
        # Analyze environment if not done yet
        if self.noise_profile is None:
            self.noise_profile = self.analyze_environment()
        
        # Configure adaptive shielding
        shield_config = self.adaptive_shielding(self.noise_profile)
        
        # Activate shield
        self.active = True
        self.start_time = datetime.now()
        
        # Calculate expected coherence improvement
        base_coherence = 1.0 - self.noise_profile['estimated_decoherence']
        shield_effectiveness = shield_config['phi_resonance'] * shield_config['coverage']
        improved_coherence = base_coherence + (1 - base_coherence) * shield_effectiveness
        
        status = {
            'active': True,
            'start_time': self.start_time.isoformat(),
            'duration': duration,
            'shield_config': shield_config,
            'base_coherence': base_coherence,
            'improved_coherence': improved_coherence,
            'coherence_gain': improved_coherence - base_coherence
        }
        
        logger.info(f"Phi-Harmonic Shield activated. Coherence improvement: "
                   f"{status['coherence_gain']:.4f} ({base_coherence:.4f} → {improved_coherence:.4f})")
        
        # If duration specified, schedule deactivation
        if duration is not None:
            logger.info(f"Shield will deactivate after {duration} seconds")
            # In a real implementation, this would use a timer
            # For simulation, we'll just return the status
        
        return status
    
    def deactivate(self) -> Dict[str, Any]:
        """
        Deactivate the phi-harmonic shield.
        
        Returns:
            Shield status information
        """
        if not self.active:
            logger.warning("Shield already inactive")
            return {'active': False}
        
        self.active = False
        end_time = datetime.now()
        
        if self.start_time:
            duration = (end_time - self.start_time).total_seconds()
        else:
            duration = 0
        
        status = {
            'active': False,
            'start_time': self.start_time.isoformat() if self.start_time else None,
            'end_time': end_time.isoformat(),
            'duration': duration
        }
        
        logger.info(f"Phi-Harmonic Shield deactivated after {duration:.2f} seconds")
        return status
    
    def get_status(self) -> Dict[str, Any]:
        """
        Get current shield status.
        
        Returns:
            Shield status information
        """
        status = {
            'active': self.active,
            'start_time': self.start_time.isoformat() if self.start_time else None,
            'noise_profile': self.noise_profile,
            'shield_patterns': len(self.shield_patterns)
        }
        
        if self.active and self.start_time:
            duration = (datetime.now() - self.start_time).total_seconds()
            status['current_duration'] = duration
        
        return status
    
    def estimate_coherence_improvement(self) -> Dict[str, float]:
        """
        Estimate coherence improvement from shielding.
        
        Returns:
            Dict with coherence metrics
        """
        if self.noise_profile is None:
            self.noise_profile = self.analyze_environment()
        
        shield_config = self.adaptive_shielding(self.noise_profile)
        
        base_coherence = 1.0 - self.noise_profile['estimated_decoherence']
        shield_effectiveness = shield_config['phi_resonance'] * shield_config['coverage']
        improved_coherence = base_coherence + (1 - base_coherence) * shield_effectiveness
        
        return {
            'base_coherence': base_coherence,
            'improved_coherence': improved_coherence,
            'coherence_gain': improved_coherence - base_coherence,
            'shield_effectiveness': shield_effectiveness
        }


def main():
    """Simple demonstration of the Phi-Harmonic Shield"""
    print("=== Phi-Harmonic Shield Demo ===")
    shield = PhiHarmonicShield(resonance_level=0.95)
    
    print("\nAnalyzing environment...")
    noise_profile = shield.analyze_environment()
    print(f"Detected {len(noise_profile['sources'])} noise sources")
    print(f"Total interference: {noise_profile['total_interference']:.4f}")
    print(f"Estimated decoherence: {noise_profile['estimated_decoherence']:.4f}")
    
    print("\nConfiguring adaptive shielding...")
    shield_config = shield.adaptive_shielding(noise_profile)
    print(f"Shield coverage: {shield_config['coverage']:.2f}")
    print(f"Shield resonance: {shield_config['phi_resonance']:.4f}")
    print(f"Energy required: {shield_config['energy_required']:.4f}")
    
    print("\nEstimating coherence improvement...")
    coherence_metrics = shield.estimate_coherence_improvement()
    print(f"Base coherence: {coherence_metrics['base_coherence']:.4f}")
    print(f"Improved coherence: {coherence_metrics['improved_coherence']:.4f}")
    print(f"Coherence gain: {coherence_metrics['coherence_gain']:.4f}")
    
    print("\nActivating shield...")
    shield_status = shield.activate(duration=10)
    print(f"Shield active: {shield_status['active']}")
    print(f"Coherence improvement: {shield_status['base_coherence']:.4f} → "
          f"{shield_status['improved_coherence']:.4f}")
    
    print("\nShield status:")
    status = shield.get_status()
    print(f"Active: {status['active']}")
    print(f"Started: {status['start_time']}")
    
    print("\nDeactivating shield...")
    shield.deactivate()
    print("Demo complete")


if __name__ == "__main__":
    main()

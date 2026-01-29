#!/usr/bin/env python
"""
Quantum Phi-Harmonic System: Quantum Processor
==============================================

This module implements the quantum processing layer of the Quantum Phi-Harmonic System,
building on the core mathematical engine to provide advanced pattern recognition,
hyper-dimensional processing, and learning capabilities.

Key features:
- Hyper-dimensional feature extraction
- Pattern recognition with phi-based scaling
- Learning progress metrics
- Integration factors framework

This follows the modular "lego" design philosophy, building upon the quantum_phi_core.py
without modifying it, creating a processor that other components can utilize.
"""

import numpy as np
import math
from decimal import Decimal, getcontext
from typing import Union, Tuple, List, Dict, Any, Callable, Optional
import json
import time

# Import the core mathematical engine
from quantum_phi_core import QuantumPhiCore

class QuantumProcessor:
    """Quantum processing layer for the Quantum Phi-Harmonic System."""
    
    def __init__(self, core: Optional[QuantumPhiCore] = None):
        """
        Initialize the Quantum Processor with a core mathematical engine.
        
        Args:
            core: QuantumPhiCore instance (creates a new one if None)
        """
        # Initialize or use provided core
        self.core = core if core is not None else QuantumPhiCore()
        
        # Initialize processor state
        self.features = {
            "hyper": [Decimal("338.000000"), Decimal("0.000000"), Decimal("0.763932")],
            "pattern": [Decimal("1.000000"), Decimal("1.618034"), Decimal("1.527864")]
        }
        
        self.recognition = {
            "hyper": [Decimal("1431.790976"), Decimal("0.000000"), Decimal("3.236068")],
            "neural": [Decimal("4.236068"), Decimal("6.854102"), Decimal("6.472136")]
        }
        
        # Learning progress metrics
        self.learning_metrics = {
            "coherence": Decimal("262.566554"),
            "stability": Decimal("1066.844009"),
            "evolution": Decimal("1834.161226"),
            "progress": Decimal("5583.067751")
        }
        
        # Integration factors
        self.integration_factors = {
            "integration": Decimal("3.263"),
            "meta": Decimal("1.147"),
            "temporal": Decimal("1.100"),
            "bridge": Decimal("2.268"),
            "coherence": Decimal("19.502")
        }
        
        # Combined factor (product of all integration factors)
        self.combined_factor = self._calculate_combined_factor()
        
        # Pattern stability
        self.pattern_stability = Decimal("0.790")
        
        # Initialize processing history
        self.processing_history = []
        
        # Initialize field data
        self.fields = self._initialize_fields()
    
    def _calculate_combined_factor(self) -> Decimal:
        """
        Calculate the combined integration factor.
        
        Returns:
            Product of all integration factors
        """
        result = Decimal("1.0")
        for factor in self.integration_factors.values():
            result *= factor
        return result
    
    def _initialize_fields(self) -> Dict[str, Dict[str, Any]]:
        """
        Initialize quantum fields with phi-based properties.
        
        Returns:
            Dictionary of quantum fields
        """
        fields = {}
        
        # 3D Quantum Field
        fields["quantum_field_3d"] = {
            "dimension": 3,
            "resonance": self.core.metrics["resonance"],
            "phi_achievement": self.core.metrics["phi_achievement"],
            "energy_transfer": self.core.metrics["energy_transfer"],
            "scale_factor": Decimal("1.0"),
            "stability": self.core.metrics["quantum_stability"]
        }
        
        # 5D Field
        fields["field_5d"] = {
            "dimension": 5,
            "resonance": self.core.metrics["resonance"] * self.core.phi_power(2),
            "phi_achievement": self.core.metrics["phi_achievement"],
            "energy_transfer": self.core.metrics["energy_transfer"] * self.core.phi_power(2),
            "scale_factor": self.core.phi_power(2),
            "stability": self.core.metrics["hyperdimensional_stability"]
        }
        
        # 6D Field
        fields["field_6d"] = {
            "dimension": 6,
            "resonance": self.core.metrics["resonance"] * self.core.phi_power(3),
            "phi_achievement": self.core.metrics["phi_achievement"],
            "energy_transfer": self.core.metrics["energy_transfer"] * self.core.phi_power(3),
            "scale_factor": self.core.phi_power(3),
            "stability": self.core.metrics["membrane_stability"]
        }
        
        return fields
    
    def extract_hyper_features(self, data: List[Union[int, float, Decimal]]) -> List[Decimal]:
        """
        Extract hyper-dimensional features from data using phi-based transformations.
        
        Args:
            data: Input data for feature extraction
            
        Returns:
            List of extracted hyper-dimensional features
        """
        features = []
        
        for i, value in enumerate(data):
            value = Decimal(value)
            # Apply phi-based transformation with dimension weighting
            transformed = self.core.feature_transform(value) * self.core.phi_power(i / len(data))
            features.append(transformed)
        
        # Store the first three features in the state
        if len(features) >= 3:
            self.features["hyper"] = features[:3]
        
        return features
    
    def extract_pattern_features(self, data: List[Union[int, float, Decimal]]) -> List[Decimal]:
        """
        Extract pattern features from data using phi-based transformations.
        
        Args:
            data: Input data for feature extraction
            
        Returns:
            List of extracted pattern features
        """
        features = []
        
        # Calculate the mean and standard deviation
        values = [Decimal(x) for x in data]
        mean = sum(values) / Decimal(len(values))
        std_dev = Decimal(math.sqrt(float(sum((x - mean) ** 2 for x in values) / len(values))))
        
        # Extract pattern features
        features.append(Decimal("1.0"))  # Baseline
        features.append(mean * self.core.PHI)  # Phi-scaled mean
        features.append(std_dev * self.core.PHI_INV)  # Inverse-phi-scaled std dev
        
        # Store the features in the state
        self.features["pattern"] = features[:3]
        
        return features
    
    def recognize_patterns(self, features: List[Union[int, float, Decimal]]) -> Dict[str, List[Decimal]]:
        """
        Recognize patterns in features using phi-based recognition functions.
        
        Args:
            features: Input features for pattern recognition
            
        Returns:
            Dictionary with hyper and neural recognition results
        """
        hyper_recognition = []
        neural_recognition = []
        
        for feature in features:
            feature = Decimal(feature)
            
            # Apply hyper recognition (phi^3 based)
            hyper = self.core.phi_power(3) * feature
            hyper_recognition.append(hyper)
            
            # Apply neural recognition (recognition function)
            neural = self.core.recognition_function(feature)
            neural_recognition.append(neural)
        
        # Store the first three recognition results in the state
        if len(hyper_recognition) >= 3:
            self.recognition["hyper"] = hyper_recognition[:3]
        
        if len(neural_recognition) >= 3:
            self.recognition["neural"] = neural_recognition[:3]
        
        return {
            "hyper": hyper_recognition,
            "neural": neural_recognition
        }
    
    def calculate_learning_function(self, t: Union[int, float, Decimal]) -> Decimal:
        """
        Calculate the learning function value at time t.
        L(t) = C + S·t + E·t² + P·t³
        
        Args:
            t: Time value
            
        Returns:
            Learning function value
        """
        t = Decimal(t)
        
        coherence = self.learning_metrics["coherence"]
        stability = self.learning_metrics["stability"]
        evolution = self.learning_metrics["evolution"]
        progress = self.learning_metrics["progress"]
        
        return coherence + stability * t + evolution * t * t + progress * t * t * t
    
    def update_learning_metrics(self, t: Union[int, float, Decimal], 
                               actual: Union[int, float, Decimal], 
                               expected: Union[int, float, Decimal]) -> Dict[str, Decimal]:
        """
        Update learning metrics based on performance at time t.
        
        Args:
            t: Time value
            actual: Actual output
            expected: Expected output
            
        Returns:
            Updated learning metrics
        """
        t = Decimal(t)
        actual = Decimal(actual)
        expected = Decimal(expected)
        
        # Calculate error
        error = abs(actual - expected) / (Decimal("1.0") + abs(expected))
        
        # Update metrics based on error and phi
        coherence_factor = self.core.PHI * (Decimal("1.0") - error)
        stability_factor = self.core.PHI_SQUARED * (Decimal("1.0") - error)
        evolution_factor = self.core.phi_power(3) * (Decimal("1.0") - error)
        progress_factor = self.core.phi_power(4) * (Decimal("1.0") - error)
        
        # Apply updates with temporal weighting
        self.learning_metrics["coherence"] *= coherence_factor * self.core.learning_rate(t)
        self.learning_metrics["stability"] *= stability_factor * self.core.learning_rate(t)
        self.learning_metrics["evolution"] *= evolution_factor * self.core.learning_rate(t)
        self.learning_metrics["progress"] *= progress_factor * self.core.learning_rate(t)
        
        return self.learning_metrics
    
    def process_hyper_dimensional(self, data: List[Union[int, float, Decimal]], 
                                 dimension: int = 3) -> Dict[str, Any]:
        """
        Process data in a hyper-dimensional space with phi-based scaling.
        
        Args:
            data: Input data for processing
            dimension: Dimensionality of the processing space
            
        Returns:
            Dictionary with processing results
        """
        # Scale data based on dimension
        dim_scale = self.core.dimension_scaling(dimension)
        scaled_data = [Decimal(x) * dim_scale for x in data]
        
        # Extract features
        hyper_features = self.extract_hyper_features(scaled_data)
        pattern_features = self.extract_pattern_features(scaled_data)
        
        # Recognize patterns
        recognition_results = self.recognize_patterns(hyper_features)
        
        # Calculate phi resonance for the data
        resonances = [self.core.phi_resonance(x) for x in scaled_data]
        avg_resonance = sum(resonances) / Decimal(len(resonances))
        resonance_quality = self.core.resonance_quality(avg_resonance)
        
        # Record processing in history
        self.processing_history.append({
            "timestamp": time.time(),
            "dimension": dimension,
            "data_length": len(data),
            "avg_resonance": avg_resonance,
            "resonance_quality": resonance_quality
        })
        
        # Return processing results
        return {
            "dimension": dimension,
            "scaling_factor": dim_scale,
            "hyper_features": hyper_features,
            "pattern_features": pattern_features,
            "recognition": recognition_results,
            "resonance": {
                "values": resonances,
                "average": avg_resonance,
                "quality": resonance_quality
            }
        }
    
    def integrate_dimensions(self, results_by_dimension: Dict[int, Dict[str, Any]]) -> Dict[str, Any]:
        """
        Integrate processing results across multiple dimensions.
        
        Args:
            results_by_dimension: Dictionary mapping dimensions to their processing results
            
        Returns:
            Integrated results across dimensions
        """
        integrated_features = []
        integrated_recognition = []
        integrated_resonance = Decimal("0.0")
        total_weight = Decimal("0.0")
        
        # Integrate across dimensions with phi-based weighting
        for dimension, results in results_by_dimension.items():
            dim_weight = self.core.phi_power(dimension - 3)  # Weight by dimension
            total_weight += dim_weight
            
            # Integrate features (first 3 only)
            for i in range(min(3, len(results["hyper_features"]))):
                if i >= len(integrated_features):
                    integrated_features.append(Decimal("0.0"))
                integrated_features[i] += results["hyper_features"][i] * dim_weight
            
            # Integrate recognition (first 3 only)
            for i in range(min(3, len(results["recognition"]["neural"]))):
                if i >= len(integrated_recognition):
                    integrated_recognition.append(Decimal("0.0"))
                integrated_recognition[i] += results["recognition"]["neural"][i] * dim_weight
            
            # Integrate resonance
            integrated_resonance += results["resonance"]["average"] * dim_weight
        
        # Normalize by total weight
        integrated_features = [f / total_weight for f in integrated_features]
        integrated_recognition = [r / total_weight for r in integrated_recognition]
        integrated_resonance = integrated_resonance / total_weight
        
        # Calculate integration quality
        integration_quality = self.core.resonance_quality(integrated_resonance)
        
        return {
            "integrated_features": integrated_features,
            "integrated_recognition": integrated_recognition,
            "integrated_resonance": integrated_resonance,
            "integration_quality": integration_quality,
            "integration_factor": self.integration_factors["integration"],
            "combined_factor": self.combined_factor
        }
    
    def update_pattern_stability(self, new_stability: Union[int, float, Decimal]) -> Decimal:
        """
        Update the pattern stability metric.
        
        Args:
            new_stability: New stability value
            
        Returns:
            Updated pattern stability
        """
        new_stability = Decimal(new_stability)
        # Update with phi-weighted average
        self.pattern_stability = (self.pattern_stability * self.core.PHI_INV + 
                                 new_stability * self.core.PHI) / (self.core.PHI_INV + self.core.PHI)
        return self.pattern_stability
    
    def evolve_pattern(self, pattern: List[Union[int, float, Decimal]], 
                      t: Union[int, float, Decimal]) -> List[Decimal]:
        """
        Evolve a pattern over time using phi-based temporal evolution.
        PE(p, t) = p + φ·t·∇p
        
        Args:
            pattern: Initial pattern
            t: Time step
            
        Returns:
            Evolved pattern
        """
        t = Decimal(t)
        pattern = [Decimal(x) for x in pattern]
        
        # Calculate pattern gradient (differences between consecutive elements)
        gradient = []
        for i in range(len(pattern) - 1):
            gradient.append(pattern[i+1] - pattern[i])
        
        # Add a final gradient element (using phi-based extrapolation)
        if len(gradient) > 0:
            gradient.append(gradient[-1] * self.core.PHI)
        else:
            gradient.append(Decimal("0.0"))
        
        # Evolve the pattern
        evolved = []
        for i in range(len(pattern)):
            evolved.append(pattern[i] + self.core.PHI * t * gradient[i])
        
        return evolved
    
    def process_field(self, field_name: str, data: List[Union[int, float, Decimal]]) -> Dict[str, Any]:
        """
        Process data through a specific quantum field.
        
        Args:
            field_name: Name of the field to use
            data: Input data for processing
            
        Returns:
            Field processing results
        """
        if field_name not in self.fields:
            raise ValueError(f"Field '{field_name}' not found")
        
        field = self.fields[field_name]
        dimension = field["dimension"]
        
        # Process data in the field's dimension
        results = self.process_hyper_dimensional(data, dimension)
        
        # Apply field-specific scaling and resonance
        field_resonance = field["resonance"]
        field_phi = field["phi_achievement"]
        field_scale = field["scale_factor"]
        
        # Scale results by field properties
        scaled_features = [f * field_scale for f in results["hyper_features"]]
        scaled_recognition = [r * field_resonance for r in results["recognition"]["neural"]]
        
        # Calculate phi achievement
        phi_achievement = self.core.calculate_phi_achievement(field_phi)
        
        # Return field-processed results
        return {
            "field_name": field_name,
            "dimension": dimension,
            "resonance": field_resonance,
            "phi_achievement": phi_achievement,
            "scale_factor": field_scale,
            "features": scaled_features,
            "recognition": scaled_recognition,
            "processing_results": results
        }
    
    def get_field_metrics(self, field_name: str) -> Dict[str, Any]:
        """
        Get metrics for a specific quantum field.
        
        Args:
            field_name: Name of the field
            
        Returns:
            Field metrics
        """
        if field_name not in self.fields:
            raise ValueError(f"Field '{field_name}' not found")
        
        field = self.fields[field_name]
        
        # Calculate phi achievement
        phi_achievement = self.core.calculate_phi_achievement(field["phi_achievement"])
        
        return {
            "field_name": field_name,
            "dimension": field["dimension"],
            "resonance": field["resonance"],
            "phi_achievement": phi_achievement,
            "energy_transfer": field["energy_transfer"],
            "scale_factor": field["scale_factor"],
            "stability": field["stability"]
        }
    
    def get_all_field_metrics(self) -> Dict[str, Dict[str, Any]]:
        """
        Get metrics for all quantum fields.
        
        Returns:
            Dictionary mapping field names to their metrics
        """
        return {field_name: self.get_field_metrics(field_name) for field_name in self.fields}
    
    def get_system_metrics(self) -> Dict[str, Any]:
        """
        Get overall system metrics.
        
        Returns:
            Dictionary of system metrics
        """
        # Get core metrics
        core_metrics = self.core.get_system_metrics()
        
        # Combine with processor metrics
        system_metrics = {
            "core": {k: float(v) for k, v in core_metrics.items()},
            "learning": {k: float(v) for k, v in self.learning_metrics.items()},
            "integration": {k: float(v) for k, v in self.integration_factors.items()},
            "combined_factor": float(self.combined_factor),
            "pattern_stability": float(self.pattern_stability)
        }
        
        return system_metrics
    
    def to_json(self) -> str:
        """
        Convert processor state to JSON.
        
        Returns:
            JSON string representation
        """
        state = {
            "features": {k: [float(v) for v in values] for k, values in self.features.items()},
            "recognition": {k: [float(v) for v in values] for k, values in self.recognition.items()},
            "learning_metrics": {k: float(v) for k, v in self.learning_metrics.items()},
            "integration_factors": {k: float(v) for k, v in self.integration_factors.items()},
            "combined_factor": float(self.combined_factor),
            "pattern_stability": float(self.pattern_stability),
            "fields": {
                name: {k: float(v) if isinstance(v, Decimal) else v for k, v in field.items()}
                for name, field in self.fields.items()
            }
        }
        
        return json.dumps(state, indent=2)
    
    def __str__(self) -> str:
        """String representation of the Quantum Processor."""
        return f"Quantum Phi-Harmonic Processor (Integration Factor: {self.combined_factor})"


# Example usage
if __name__ == "__main__":
    # Initialize the processor
    processor = QuantumProcessor()
    
    # Print processor info
    print(processor)
    
    # Process some data in different dimensions
    data = [1, 1, 2, 3, 5, 8, 13, 21]
    
    results_3d = processor.process_hyper_dimensional(data, dimension=3)
    results_5d = processor.process_hyper_dimensional(data, dimension=5)
    results_6d = processor.process_hyper_dimensional(data, dimension=6)
    
    # Integrate results across dimensions
    integrated = processor.integrate_dimensions({
        3: results_3d,
        5: results_5d,
        6: results_6d
    })
    
    print("\nIntegrated Results:")
    print(f"Features: {[float(f) for f in integrated['integrated_features']]}")
    print(f"Recognition: {[float(r) for r in integrated['integrated_recognition']]}")
    print(f"Resonance: {float(integrated['integrated_resonance'])} ({integrated['integration_quality']})")
    
    # Get field metrics
    field_metrics = processor.get_all_field_metrics()
    
    print("\nField Metrics:")
    for field_name, metrics in field_metrics.items():
        print(f"\n{field_name} (Dimension: {metrics['dimension']}):")
        print(f"  Resonance: {float(metrics['resonance'])}")
        print(f"  Phi Achievement: {float(metrics['phi_achievement']['value'])} (Target: {float(metrics['phi_achievement']['target'])})")
        print(f"  Energy Transfer: {float(metrics['energy_transfer'])}x")
        print(f"  Scale Factor: {float(metrics['scale_factor'])}")
    
    # Get system metrics
    system_metrics = processor.get_system_metrics()
    print("\nSystem Metrics:")
    print(f"Combined Factor: {system_metrics['combined_factor']}")
    print(f"Pattern Stability: {system_metrics['pattern_stability']}")

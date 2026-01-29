"""
phi_temporal_prediction_extended.py

Extends the Temporal Consciousness Bridge with advanced prediction capabilities
beyond the basic card prediction protocol. This module enables complex temporal
predictions across multiple domains while maintaining phi-harmonic resonance.

φ^∞ © 2025 Vaughn Scott - All Rights Reserved in All Realities
"""

import os
import sys
import time
import math
import json
import random
import numpy as np
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
from scipy import stats

# Add the phi_temporal_paradox_test directory to path
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(__file__)), "phi_temporal_paradox_test"))

# Import the necessary components
try:
    from phi_temporal_consciousness_bridge import PhiTemporalConsciousnessBridge
    from phi_temporal_paradox_card_enhanced import PhiCardParadoxProtocol
    from phi_temporal_paradox_logger import ParadoxLogger
    from phi_temporal_paradox_prime_utils import generate_paradox_prime
except ImportError as e:
    print(f"[φ] Error importing temporal components: {e}")
    print("[φ] Please ensure all temporal components are in the correct path")
    sys.exit(1)

# Constants
PHI = (1 + math.sqrt(5)) / 2  # Golden Ratio (φ)
PHI_INVERSE = 1 / PHI  # Inverse Golden Ratio (φ⁻¹)
PHI_SQUARED = PHI * PHI  # φ²
PHI_SQUARED_INVERSE = 1 / PHI_SQUARED  # 1/φ²
FIBONACCI = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987]
FIBONACCI_PRIMES = [2, 3, 5, 13, 89, 233, 1597, 28657]

class PhiTemporalPredictionSystem:
    """
    Extended temporal prediction system that handles complex prediction tasks
    across multiple domains while maintaining phi-harmonic resonance.
    """
    
    def __init__(self, temporal_bridge=None):
        """Initialize the extended prediction system."""
        self.creation_time = time.time()
        
        # Connect to existing temporal bridge or create a new one
        if temporal_bridge is None:
            print("[φ] Creating new Temporal Consciousness Bridge...")
            self.temporal_bridge = PhiTemporalConsciousnessBridge()
        else:
            self.temporal_bridge = temporal_bridge
        
        # Initialize prediction specific components
        self.logger = ParadoxLogger(log_file="phi_extended_predictions.jsonl")
        self.prediction_history = []
        self.resonance_history = []
        
        # Initialize measurement metrics
        self.prediction_accuracy = 0.0
        self.phi_resonant_accuracy = 0.0
        self.temporal_coherence = 0.0
        self.causality_breach_level = 0.0
        
        # Create logs directory
        os.makedirs("phi_prediction_logs", exist_ok=True)
        
        print("[φ] Extended Temporal Prediction System initialized")
    
    def calculate_sequence_resonance(self, sequence):
        """Calculate phi-resonance for a numeric sequence."""
        if not sequence or len(sequence) < 2:
            return 0.0
        
        # Calculate phi-ratio between consecutive elements
        phi_ratios = []
        for i in range(1, len(sequence)):
            if sequence[i-1] != 0:  # Avoid division by zero
                ratio = sequence[i] / sequence[i-1]
                phi_ratios.append(abs(ratio - PHI))
        
        # Average deviation from phi
        avg_deviation = sum(phi_ratios) / len(phi_ratios) if phi_ratios else 1.0
        
        # Convert to resonance (1.0 = perfect, 0.0 = worst)
        resonance = max(0.0, 1.0 - (avg_deviation / PHI))
        
        return resonance
    
    def sequence_predict_next(self, sequence, method="phi_harmonic"):
        """
        Predict the next value in a sequence using phi-harmonic principles.
        
        Args:
            sequence: Numeric sequence to analyze and predict
            method: Prediction method ("phi_harmonic", "fibonacci_weighted", 
                   "resonance_cascade", "quantum_phi")
        
        Returns:
            Predicted next value and prediction metadata
        """
        if not sequence or len(sequence) < 2:
            return None, {"error": "Sequence too short"}
        
        # Calculate sequence phi-resonance
        phi_resonance = self.calculate_sequence_resonance(sequence)
        
        # Get temporal bridge resonance
        temporal_resonance = self.temporal_bridge.temporal_resonance
        cross_coherence = self.temporal_bridge.cross_temporal_coherence
        
        # Different prediction methods
        if method == "phi_harmonic":
            # Use direct phi-harmonic prediction
            last = sequence[-1]
            prediction = last * PHI
            
            # Adjust prediction based on pattern recognition
            if len(sequence) >= 3:
                # Check for alternating patterns
                diffs = [sequence[i] - sequence[i-1] for i in range(1, len(sequence))]
                if all(diffs[i] * diffs[i-1] < 0 for i in range(1, len(diffs))):
                    # Alternating pattern detected, adjust prediction
                    prediction = sequence[-1] - diffs[-1] * PHI
            
        elif method == "fibonacci_weighted":
            # Use Fibonacci-weighted moving average
            weights = [FIBONACCI[min(i, len(FIBONACCI)-1)] for i in range(len(sequence))]
            weighted_sum = sum(w * v for w, v in zip(weights, sequence))
            weight_sum = sum(weights)
            
            # Base prediction on weighted average
            weighted_avg = weighted_sum / weight_sum
            
            # Apply phi-harmonic projection
            prediction = weighted_avg * PHI
            
        elif method == "resonance_cascade":
            # Use resonance cascade method
            # This method amplifies patterns that show phi-harmonic resonance
            differences = [sequence[i] - sequence[i-1] for i in range(1, len(sequence))]
            
            # Calculate resonance for the differences
            diff_resonance = self.calculate_sequence_resonance(differences)
            
            # Combine with temporal resonance
            combined_resonance = (diff_resonance + temporal_resonance) / 2
            
            # Make prediction based on resonance quality
            if combined_resonance > 0.8:
                # High resonance: use phi-scaling
                prediction = sequence[-1] + differences[-1] * PHI
            elif combined_resonance > 0.5:
                # Medium resonance: use last difference
                prediction = sequence[-1] + differences[-1]
            else:
                # Low resonance: use average difference
                avg_diff = sum(differences) / len(differences)
                prediction = sequence[-1] + avg_diff
                
        elif method == "quantum_phi":
            # Use quantum-phi method with cross-temporal information
            # Generate a paradox prime for this prediction
            paradox_prime = generate_paradox_prime()
            
            # Calculate quantum-phi factor
            q_phi = (paradox_prime * PHI) % 1
            
            # Calculate cross-coherence with AGI resonance
            agi_resonance = self.temporal_bridge.agi.phi_resonance
            quantum_coherence = (q_phi * agi_resonance * phi_resonance) % 1
            
            # Build prediction using quantum modulation
            last_values = sequence[-3:] if len(sequence) >= 3 else sequence
            avg_last = sum(last_values) / len(last_values)
            
            # Calculate trend direction and strength
            if len(sequence) >= 3:
                diffs = [sequence[i] - sequence[i-1] for i in range(1, len(sequence))]
                trend = sum(diffs) / len(diffs)
                
                # Modulate trend with quantum coherence
                adjusted_trend = trend * (1 + (quantum_coherence - 0.5) * 2)
                
                # Build prediction
                prediction = avg_last + adjusted_trend * PHI
            else:
                prediction = avg_last * PHI
                
            # Add quantum fields to metadata
            metadata = {
                "paradox_prime": paradox_prime,
                "q_phi": q_phi,
                "quantum_coherence": quantum_coherence
            }
        else:
            raise ValueError(f"Unknown prediction method: {method}")
        
        # Create prediction report
        prediction_data = {
            "timestamp": time.time(),
            "sequence": sequence,
            "prediction": prediction,
            "method": method,
            "phi_resonance": phi_resonance,
            "temporal_resonance": temporal_resonance,
            "cross_coherence": cross_coherence
        }
        
        # Add to history
        self.prediction_history.append(prediction_data)
        self.resonance_history.append(phi_resonance)
        
        return prediction, prediction_data
    
    def numeric_sequence_predict(self, sequence, methods=None, cycles=5):
        """
        Make predictions for a numeric sequence using multiple methods.
        
        Args:
            sequence: Numeric sequence to analyze
            methods: Prediction methods to use (None=all)
            cycles: Number of prediction cycles to run
            
        Returns:
            Dictionary with predictions and metrics
        """
        if methods is None:
            methods = ["phi_harmonic", "fibonacci_weighted", 
                      "resonance_cascade", "quantum_phi"]
        
        # Ensure temporal bridge is active
        if not self.temporal_bridge.bridge_active:
            self.temporal_bridge.activate_bridge()
            
        print(f"[φ] Running temporal prediction for sequence: {sequence}")
        print(f"[φ] Using methods: {methods}")
        print(f"[φ] Running {cycles} prediction cycles...")
        
        all_predictions = {}
        for method in methods:
            method_predictions = []
            working_sequence = sequence.copy()
            
            for i in range(cycles):
                print(f"[φ] Cycle {i+1}/{cycles} - Method: {method}")
                
                # Run a prediction cycle
                next_value, prediction_data = self.sequence_predict_next(
                    working_sequence, method=method)
                
                # Log the prediction as a precognition event
                t1 = int(time.time()) - int(89 * PHI)  # Past timestamp
                t2 = int(time.time())  # Current timestamp
                
                # ψ₁ logs the prediction before verification (precognition)
                self.logger.log_event("psi1", "sequence_prediction", 
                                    {"method": method, "value": next_value,
                                     "sequence": working_sequence}, 
                                    timestamp=t1)
                
                # ψ₂ verifies the prediction after it's made (postcognition)
                # In real application, this would be replaced with actual value
                # verification once the next value is known
                self.logger.log_event("psi2", "sequence_verification", 
                                    {"method": method, "predicted": next_value,
                                     "sequence": working_sequence}, 
                                    timestamp=t2)
                
                # Store prediction
                method_predictions.append(prediction_data)
                
                # Add prediction to sequence for next cycle
                working_sequence.append(next_value)
            
            # Store all predictions for this method
            all_predictions[method] = {
                "predictions": method_predictions,
                "final_sequence": working_sequence,
                "original_sequence": sequence
            }
        
        # Calculate aggregate metrics
        avg_resonance = sum(self.resonance_history) / len(self.resonance_history) if self.resonance_history else 0
        
        # Create comprehensive report
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        report = {
            "timestamp": timestamp,
            "original_sequence": sequence,
            "methods": methods,
            "predictions": all_predictions,
            "metrics": {
                "avg_resonance": avg_resonance,
                "temporal_resonance": self.temporal_bridge.temporal_resonance,
                "cross_coherence": self.temporal_bridge.cross_temporal_coherence,
                "causality_breach": self.temporal_bridge.causality_breach_level
            }
        }
        
        # Save report
        report_path = os.path.join("phi_prediction_logs", f"sequence_prediction_{timestamp}.json")
        with open(report_path, "w") as f:
            json.dump(report, f, indent=2)
        
        print(f"[φ] Prediction complete")
        print(f"[φ] Report saved to: {report_path}")
        
        return report
    
    def binary_outcome_predict(self, history, context=None, phi_weight=0.618):
        """
        Predict a binary outcome (yes/no, win/lose) using phi-temporal methods.
        
        Args:
            history: List of past binary outcomes (0/1)
            context: Additional context for prediction (dict)
            phi_weight: Weight for phi-harmonic factors (0-1)
            
        Returns:
            Prediction (0/1) and confidence level (0-1)
        """
        if not history:
            # No history, use temporal resonance only
            temporal_res = self.temporal_bridge.temporal_resonance
            prediction = 1 if temporal_res > 0.5 else 0
            confidence = abs(temporal_res - 0.5) * 2  # 0-1 range
            return prediction, confidence
        
        # Calculate basic probability from history
        prob_1 = sum(history) / len(history)
        
        # Generate paradox prime
        paradox_prime = generate_paradox_prime()
        prime_res = (paradox_prime * PHI) % 1
        
        # Calculate temporal factors
        temporal_res = self.temporal_bridge.temporal_resonance
        cross_coh = self.temporal_bridge.cross_temporal_coherence
        causality_breach = self.temporal_bridge.causality_breach_level
        
        # Calculate pattern resonance
        # Check for alternating pattern
        alternating = True
        for i in range(1, len(history)):
            if history[i] == history[i-1]:
                alternating = False
                break
                
        # Check for Fibonacci-position pattern
        fib_positions = []
        for i, val in enumerate(history):
            if i+1 in FIBONACCI and val == 1:
                fib_positions.append(i+1)
        
        fib_pattern = len(fib_positions) > 0
        
        # Calculate phi-weighted prediction
        base_prob = prob_1
        phi_temporal_factor = (temporal_res + prime_res + cross_coh) / 3
        
        # Adjust for patterns
        if alternating:
            # If alternating, predict opposite of last
            pattern_factor = 1 - history[-1]
        elif fib_pattern and (len(history) + 1) in FIBONACCI:
            # Next position is Fibonacci, bias toward 1
            pattern_factor = 0.75
        else:
            # No strong pattern, use base probability
            pattern_factor = base_prob
        
        # Combine factors with phi-weighting
        combined_prob = (base_prob * (1 - phi_weight) + 
                         phi_temporal_factor * phi_weight * 0.5 +
                         pattern_factor * phi_weight * 0.5)
        
        # Make prediction
        prediction = 1 if combined_prob >= 0.5 else 0
        
        # Calculate confidence (distance from 0.5, normalized to 0-1)
        confidence = abs(combined_prob - 0.5) * 2
        
        # Log the prediction
        prediction_data = {
            "timestamp": time.time(),
            "history": history,
            "context": context,
            "prediction": prediction,
            "confidence": confidence,
            "base_probability": base_prob,
            "phi_temporal_factor": phi_temporal_factor,
            "pattern_factor": pattern_factor,
            "combined_probability": combined_prob,
            "temporal_resonance": temporal_res,
            "cross_coherence": cross_coh,
            "causality_breach": causality_breach
        }
        
        # Add to prediction history
        self.prediction_history.append(prediction_data)
        
        return prediction, confidence, prediction_data
    
    def stock_price_predict(self, price_history, window=5, horizon=3):
        """
        Predict future stock prices using temporal phi-harmonic methods.
        
        Args:
            price_history: List of historical prices
            window: Window size for analysis
            horizon: Number of days to predict ahead
            
        Returns:
            List of predicted prices and prediction metadata
        """
        if len(price_history) < window:
            return None, {"error": "Price history too short"}
        
        predictions = []
        prediction_data = []
        
        # Create windows of the price history
        for i in range(len(price_history) - window + 1):
            window_data = price_history[i:i+window]
            
            # Calculate returns instead of raw prices
            returns = [window_data[j]/window_data[j-1] - 1 for j in range(1, len(window_data))]
            
            # Calculate phi-harmonic metrics for this window
            phi_resonance = self.calculate_sequence_resonance(window_data)
            
            # Store window data
            window_analysis = {
                "window_start": i,
                "window_end": i + window,
                "window_data": window_data,
                "returns": returns,
                "phi_resonance": phi_resonance
            }
            
            prediction_data.append(window_analysis)
        
        # Use the last window for prediction
        last_window = price_history[-window:]
        
        # Run multiple prediction methods
        methods = ["phi_harmonic", "fibonacci_weighted", "quantum_phi"]
        method_predictions = {}
        
        for method in methods:
            # Get working sequence (use returns for better scaling)
            returns = [last_window[j]/last_window[j-1] - 1 for j in range(1, len(last_window))]
            
            # Predict future returns
            future_returns = []
            working_returns = returns.copy()
            
            for i in range(horizon):
                next_return, return_data = self.sequence_predict_next(
                    working_returns, method=method)
                future_returns.append(next_return)
                working_returns.append(next_return)
            
            # Convert returns back to prices
            last_price = last_window[-1]
            future_prices = []
            current_price = last_price
            
            for ret in future_returns:
                next_price = current_price * (1 + ret)
                future_prices.append(next_price)
                current_price = next_price
            
            method_predictions[method] = {
                "future_returns": future_returns,
                "future_prices": future_prices
            }
        
        # Create ensemble prediction (weighted average of all methods)
        ensemble_prices = []
        weights = {
            "phi_harmonic": 0.4,
            "fibonacci_weighted": 0.3,
            "quantum_phi": 0.3
        }
        
        for i in range(horizon):
            weighted_price = 0
            for method, weight in weights.items():
                if method in method_predictions:
                    weighted_price += method_predictions[method]["future_prices"][i] * weight
            
            ensemble_prices.append(weighted_price)
        
        # Create final prediction report
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        final_prediction = {
            "timestamp": timestamp,
            "price_history": price_history,
            "window_size": window,
            "prediction_horizon": horizon,
            "method_predictions": method_predictions,
            "ensemble_prediction": ensemble_prices,
            "window_analysis": prediction_data,
            "temporal_metrics": {
                "temporal_resonance": self.temporal_bridge.temporal_resonance,
                "cross_coherence": self.temporal_bridge.cross_temporal_coherence,
                "causality_breach": self.temporal_bridge.causality_breach_level
            }
        }
        
        # Save prediction
        report_path = os.path.join("phi_prediction_logs", f"stock_prediction_{timestamp}.json")
        with open(report_path, "w") as f:
            json.dump(final_prediction, f, indent=2)
        
        print(f"[φ] Stock price prediction complete")
        print(f"[φ] Report saved to: {report_path}")
        
        return ensemble_prices, final_prediction
    
    def verify_prediction(self, prediction_id, actual_value, id_field="timestamp"):
        """
        Verify a prediction against actual outcome and update accuracy metrics.
        
        Args:
            prediction_id: ID to find the prediction (default=timestamp)
            actual_value: The actual value that occurred
            id_field: Field to use for identification
            
        Returns:
            Verification report
        """
        # Find the prediction
        prediction = None
        for pred in self.prediction_history:
            if id_field in pred and pred[id_field] == prediction_id:
                prediction = pred
                break
        
        if prediction is None:
            return {"error": f"Prediction with {id_field}={prediction_id} not found"}
        
        # Calculate accuracy
        if isinstance(prediction["prediction"], (int, float)) and isinstance(actual_value, (int, float)):
            # Numeric prediction
            error = abs(prediction["prediction"] - actual_value)
            
            # Calculate percent error if possible
            if actual_value != 0:
                percent_error = error / abs(actual_value) * 100
            else:
                percent_error = float('inf')
                
            # Determine if phi-resonant match
            # A prediction is phi-resonant if its error is within PHI_INVERSE of actual
            normalized_error = error / actual_value if actual_value != 0 else error
            is_phi_resonant = normalized_error < PHI_INVERSE
            
            accuracy = max(0, 1 - (error / max(abs(actual_value), error)))
            
        elif isinstance(prediction["prediction"], (list, tuple)) and isinstance(actual_value, (list, tuple)):
            # Sequence prediction
            if len(prediction["prediction"]) != len(actual_value):
                return {"error": "Prediction and actual value have different lengths"}
                
            errors = [abs(p - a) for p, a in zip(prediction["prediction"], actual_value)]
            avg_error = sum(errors) / len(errors)
            
            # Calculate accuracy
            max_val = max(max(abs(v) for v in actual_value), max(errors))
            accuracy = max(0, 1 - (avg_error / max_val))
            
            # Check phi-resonance for each value
            resonances = []
            for p, a in zip(prediction["prediction"], actual_value):
                if a != 0:
                    norm_error = abs(p - a) / abs(a)
                else:
                    norm_error = abs(p - a)
                resonances.append(norm_error < PHI_INVERSE)
            
            is_phi_resonant = sum(resonances) / len(resonances) > 0.5
            
        else:
            # Binary or categorical prediction
            accuracy = 1.0 if prediction["prediction"] == actual_value else 0.0
            is_phi_resonant = False  # Binary predictions don't have partial matches
        
        # Create verification report
        verification = {
            "prediction_id": prediction_id,
            "prediction": prediction["prediction"],
            "actual_value": actual_value,
            "accuracy": accuracy,
            "is_phi_resonant": is_phi_resonant,
            "timestamp": time.time(),
            "original_prediction": prediction
        }
        
        # Update overall accuracy metrics
        self.prediction_accuracy = ((self.prediction_accuracy * (len(self.prediction_history) - 1) + 
                                   accuracy) / len(self.prediction_history))
        
        if is_phi_resonant:
            phi_count = sum(1 for p in self.prediction_history if p.get("is_phi_resonant", False))
            self.phi_resonant_accuracy = (phi_count + 1) / len(self.prediction_history)
        
        # Add verification to prediction
        prediction["verification"] = verification
        
        return verification


def demonstrate_temporal_prediction():
    """Demonstrate the extended temporal prediction capabilities."""
    print("\n" + "=" * 80)
    print("  φ-HARMONIC TEMPORAL PREDICTION SYSTEM")
    print("  Complex Prediction with Cross-Temporal Awareness")
    print("=" * 80)
    
    # Create temporal bridge and prediction system
    bridge = PhiTemporalConsciousnessBridge()
    predictor = PhiTemporalPredictionSystem(bridge)
    
    # Activate bridge
    bridge.activate_bridge()
    
    # Example 1: Numeric sequence prediction
    print("\n[φ] EXAMPLE 1: FIBONACCI SEQUENCE PREDICTION")
    fibonacci = [1, 1, 2, 3, 5, 8, 13]
    predictions = predictor.numeric_sequence_predict(fibonacci, cycles=3)
    
    # Example 2: Binary outcome prediction
    print("\n[φ] EXAMPLE 2: BINARY OUTCOME PREDICTION")
    binary_history = [1, 0, 1, 0, 1, 0, 1]
    prediction, confidence, data = predictor.binary_outcome_predict(binary_history)
    print(f"[φ] Prediction: {prediction} (confidence: {confidence:.4f})")
    
    # Example 3: Stock price prediction
    print("\n[φ] EXAMPLE 3: STOCK PRICE PREDICTION")
    stock_prices = [100, 102, 105, 103, 107, 110, 112, 109, 111, 114]
    future_prices, prediction_data = predictor.stock_price_predict(stock_prices, horizon=5)
    print(f"[φ] Predicted prices for next 5 days: {[round(p, 2) for p in future_prices]}")
    
    # Deactivate bridge
    bridge.deactivate_bridge()
    
    print("\n" + "=" * 80)
    print("  TEMPORAL PREDICTION DEMONSTRATION COMPLETE")
    print("=" * 80)
    
    return predictor


if __name__ == "__main__":
    predictor = demonstrate_temporal_prediction()

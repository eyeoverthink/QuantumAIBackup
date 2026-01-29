#!/usr/bin/env python3
"""
φ-Harmonic Prediction Monitoring System
"""
import math
import numpy as np
import pandas as pd
from datetime import datetime, timedelta
from typing import Dict, List

class PredictionMonitor:
    def __init__(self):
        """Initialize monitoring system"""
        self.phi = (1 + math.sqrt(5)) / 2
        self.base_freq = 4.84  # Earth-Moon base frequency
        
        # Prediction data structure
        self.predictions = {
            'earthquake': [],
            'solar': [],
            'geophysical': []
        }
        
        # Monitoring thresholds
        self.thresholds = {
            'frequency': 0.01,  # 1% tolerance
            'magnitude': 0.1,   # 10% tolerance
            'energy': 0.05      # 5% tolerance
        }

    def add_prediction(self, prediction_type: str, data: Dict) -> None:
        """Add new prediction to monitoring system"""
        self.predictions[prediction_type].append({
            'date': data['date'],
            'frequency': data['frequency'],
            'magnitude': data.get('magnitude', None),
            'energy': data.get('energy', None),
            'status': 'pending',
            'validation': None
        })

    def validate_prediction(self, prediction_type: str, index: int, actual_data: Dict) -> Dict:
        """Validate prediction against actual data"""
        pred = self.predictions[prediction_type][index]
        validation = {}
        
        # Validate frequency
        freq_error = abs(pred['frequency'] - actual_data['frequency']) / pred['frequency']
        validation['frequency'] = {
            'error': freq_error,
            'valid': freq_error <= self.thresholds['frequency']
        }
        
        # Validate magnitude if present
        if 'magnitude' in pred and 'magnitude' in actual_data:
            mag_error = abs(pred['magnitude'] - actual_data['magnitude']) / pred['magnitude']
            validation['magnitude'] = {
                'error': mag_error,
                'valid': mag_error <= self.thresholds['magnitude']
            }
        
        # Validate energy if present
        if 'energy' in pred and 'energy' in actual_data:
            energy_error = abs(pred['energy'] - actual_data['energy']) / pred['energy']
            validation['energy'] = {
                'error': energy_error,
                'valid': energy_error <= self.thresholds['energy']
            }
        
        # Update prediction status
        pred['status'] = 'validated'
        pred['validation'] = validation
        
        return validation

    def generate_report(self) -> pd.DataFrame:
        """Generate validation report"""
        reports = []
        
        for pred_type, predictions in self.predictions.items():
            for pred in predictions:
                if pred['status'] == 'validated':
                    report = {
                        'type': pred_type,
                        'date': pred['date'],
                        'frequency': pred['frequency'],
                        'magnitude': pred.get('magnitude', None),
                        'energy': pred.get('energy', None)
                    }
                    
                    # Add validation results
                    for metric, result in pred['validation'].items():
                        report[f'{metric}_error'] = result['error']
                        report[f'{metric}_valid'] = result['valid']
                    
                    reports.append(report)
        
        return pd.DataFrame(reports)

if __name__ == "__main__":
    # Initialize monitor
    monitor = PredictionMonitor()
    
    # Add earthquake predictions
    earthquake_data = {
        'date': '2025-03-25',
        'frequency': 20.50,
        'magnitude': 5.0,
        'energy': 1.14e+03
    }
    monitor.add_prediction('earthquake', earthquake_data)
    
    # Add solar predictions
    solar_data = {
        'date': '2025-03-21',
        'frequency': 4.84,
        'energy': 1.0
    }
    monitor.add_prediction('solar', solar_data)
    
    print("\n📊 Prediction Monitoring System")
    print("=============================")
    
    # Generate initial report
    report = monitor.generate_report()
    print("\nInitial Report:")
    print(report)
    
    # Example validation
    actual_earthquake = {
        'frequency': 20.45,  # 0.24% error
        'magnitude': 5.05,   # 1% error
        'energy': 1.13e+03   # 0.88% error
    }
    
    print("\nValidation Results:")
    validation = monitor.validate_prediction('earthquake', 0, actual_earthquake)
    print(validation)
    
    # Generate final report
    print("\nFinal Report:")
    final_report = monitor.generate_report()
    print(final_report)

#!/usr/bin/env python3
"""
OSDR DATA FETCHER (FIXED)
========================
An improved module to fetch and process real astronomical data from NASA's Open Science Data Repository,
with better error handling and data extraction.

Author: Cascade AI
Date: April 26, 2025
"""
import requests
import math
import json
import time
from pathlib import Path

# Constants based on golden ratio
PHI = (1 + math.sqrt(5)) / 2

class OSDRFetcher:
    def __init__(self):
        self.base_url = "https://osdr.nasa.gov/osdr/data/osd/files"
        
    def fetch_study_data(self, study_id):
        """
        Fetch real data from NASA's Open Science Data Repository
        Args:
            study_id: The study ID to fetch
        Returns:
            dict: Actual API data or error message
        """
        url = f"{self.base_url}/{study_id}"
        print(f"Fetching data from: {url}")
        
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            print(f"Raw API response: {json.dumps(data, indent=2)}")
            return self._process_data(data)
        except requests.HTTPError as e:
            print(f"HTTP Error: {e}")
            if e.response.status_code == 404:
                # Try alternative OSDR endpoint pattern
                try:
                    alt_url = f"https://osdr.nasa.gov/osdr/data/osd/files?study_id={study_id}"
                    print(f"Trying alternative URL: {alt_url}")
                    alt_response = requests.get(alt_url)
                    alt_response.raise_for_status()
                    alt_data = alt_response.json()
                    print(f"Alternative response: {json.dumps(alt_data, indent=2)}")
                    return self._process_data(alt_data)
                except Exception as alt_e:
                    print(f"Alternative endpoint also failed: {alt_e}")
            return {'error': f"OSDR fetch failed with status {e.response.status_code}: {str(e)}"}
        except Exception as e:
            print(f"Unexpected error: {e}")
            return {'error': f"OSDR fetch failed: {str(e)}"}
    
    def _process_data(self, data):
        """
        Process real OSDR data for φ-resonance analysis
        Returns only actual data with calculated φ-metrics
        """
        result = {'raw_data': data}
        
        # Placeholder for extracted numerical values
        numerical_values = []
        
        # Extract numerical values from the response
        if isinstance(data, dict):
            numerical_values = self._extract_numerical_values(data)
        elif isinstance(data, list):
            for item in data:
                if isinstance(item, dict):
                    numerical_values.extend(self._extract_numerical_values(item))
        
        print(f"Extracted {len(numerical_values)} numerical values: {numerical_values[:10]}...")
        
        # Calculate φ-resonance metrics from real values
        phi_metrics = self._calculate_phi_metrics(numerical_values)
        result['phi_metrics'] = phi_metrics
        
        return result
    
    def _extract_numerical_values(self, data_dict):
        """Extract real numerical values from nested dictionary for φ-analysis"""
        values = []
        
        def extract_from_dict(d):
            for k, v in d.items():
                if isinstance(v, (int, float)) and v != 0:  # Skip zero values
                    values.append(float(v))
                elif isinstance(v, dict):
                    extract_from_dict(v)
                elif isinstance(v, list):
                    for item in v:
                        if isinstance(item, dict):
                            extract_from_dict(item)
                        elif isinstance(item, (int, float)) and item != 0:
                            values.append(float(item))
        
        extract_from_dict(data_dict)
        return values
    
    def _calculate_phi_metrics(self, values):
        """Calculate φ-resonance metrics from real numerical values"""
        metrics = {
            'phi_relevance': 0.0,
            'resonance_factors': [],
            'value_count': len(values)
        }
        
        if not values:
            return metrics
            
        # Calculate resonance factors for each real value
        for value in values:
            # φ-modulo resonance (how close to multiple of φ)
            resonance = abs((value * PHI) % 1)
            metrics['resonance_factors'].append(resonance)
        
        # Calculate overall phi_relevance from real data
        if metrics['resonance_factors']:
            metrics['phi_relevance'] = 1 - sum(metrics['resonance_factors'])/len(metrics['resonance_factors'])
            
        return metrics

# Example usage
if __name__ == "__main__":
    fetcher = OSDRFetcher()
    # Try with OSDR study ID 87 (user can adjust to valid ID)
    data = fetcher.fetch_study_data(87)
    print(json.dumps(data, indent=2))

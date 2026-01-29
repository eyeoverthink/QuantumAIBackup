#!/usr/bin/env python3
"""
OSDR DATA FETCHER MODULE
=======================
Module for fetching astronomical data from NASA's Open Science Data Repository,
designed to integrate with the Phi-Cosmic Resonance Validator.

Author: Cascade AI
Date: April 26, 2025
"""
import requests
import math
import json
from pathlib import Path

# Constants based on golden ratio
PHI = (1 + math.sqrt(5)) / 2
RETRY_DELAYS = [PHI**n for n in range(1, 5)]  # [2.618, 4.236, 6.854, 11.090] seconds

class OSDRFetcher:
    def __init__(self):
        self.base_url = "https://osdr.nasa.gov/osdr/data/osd/files"
        
    def fetch_study_data(self, study_id, page=0, results_per_page=25, all_files=False):
        """
        Fetch data from NASA Open Science Data Repository
        Args:
            study_id: The study ID to fetch (integer or decimal)
            page: Current page number in pagination
            results_per_page: Max results per page
            all_files: Include hidden files
        Returns:
            dict: Fetched data or error message
        """
        try:
            url = f"{self.base_url}/{study_id}?page={page}&size={results_per_page}"
            if all_files:
                url += "&all_files=true"
                
            response = requests.get(url)
            response.raise_for_status()
            return self._process_data(response.json())
        except Exception as e:
            return {'error': f"OSDR fetch failed: {str(e)}"}
    
    def _process_data(self, data):
        """
        Process OSDR data for φ-resonance analysis using golden ratio principles
        Returns data with φ-relevance metrics
        """
        if not data:
            return {'error': 'No data returned from OSDR'}
            
        # Example processing using φ principles (customize based on data structure)
        phi_metrics = {
            'phi_relevance': 0.0,
            'resonance_factors': []
        }
        
        # Analyze numerical values for φ-resonance (placeholder logic)
        if isinstance(data, dict) and 'results' in data:
            numerical_values = self._extract_numerical_values(data)
            
            # Calculate φ-relevance using golden ratio principles
            for value in numerical_values:
                resonance = abs((value * PHI) % 1)  # φ-modulo resonance
                phi_metrics['resonance_factors'].append(resonance)
            
            # Average resonance (lower is better aligned with φ)
            if phi_metrics['resonance_factors']:
                phi_metrics['phi_relevance'] = 1 - sum(phi_metrics['resonance_factors'])/len(phi_metrics['resonance_factors'])
        
        # Add metrics to original data
        data['phi_metrics'] = phi_metrics
        return data
    
    def _extract_numerical_values(self, data_dict):
        """Extract numerical values from nested dictionary for φ-analysis"""
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

# Example usage
if __name__ == "__main__":
    fetcher = OSDRFetcher()
    # Example with OSDR study ID 87
    data = fetcher.fetch_study_data(87)
    print(json.dumps(data, indent=2))

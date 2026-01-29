#!/usr/bin/env python3
"""
ENHANCED DATA FETCHER MODULE
===========================
Improved module for fetching astronomical data with better error handling, key validation, and descriptive messages.
Incorporates golden ratio retry logic and quantum principles for robustness.

Author: Cascade AI
Date: April 26, 2025
"""
import requests
import time
import math
from pathlib import Path

# Constants
PHI = (1 + math.sqrt(5)) / 2
RETRY_DELAYS = [PHI**n for n in range(1, 5)]  # [2.618, 4.236, 6.854, 11.090] seconds
MAX_RETRIES = 5

class EnhancedDataFetcher:
    def __init__(self, api_url: str, api_key: str = None):
        self.api_url = api_url
        self.api_key = api_key
        self.headers = {'Authorization': f'Bearer {api_key}'} if api_key else {}
        
    def fetch_astronomical_data(self, endpoint: str, params: dict = {}):
        """
        Fetch data with enhanced error handling and key validation.
        Args:
            endpoint (str): API endpoint
            params (dict): Query parameters
        Returns:
            dict: Fetched data or detailed error message
        """
        if not self.api_key:
            return {'error': 'API key is missing. Please provide a valid key.'}
        
        for attempt in range(MAX_RETRIES):
            try:
                response = requests.get(f"{self.api_url}{endpoint}", params=params, headers=self.headers)
                response.raise_for_status()
                return response.json()
            except requests.HTTPError as e:
                error_code = e.response.status_code
                if error_code == 403:
                    return {'error': f'403 Forbidden: Invalid API key or permissions. Check your key at https://api.nasa.gov/.', 'details': str(e)}
                elif error_code == 404:
                    return {'error': f'404 Not Found: Endpoint or resource not available. Verify the endpoint.', 'details': str(e)}
                else:
                    if attempt < MAX_RETRIES - 1:
                        delay = RETRY_DELAYS[attempt] * (1 + 0.1 * math.sin(attempt))
                        time.sleep(delay)
                    else:
                        return {'error': f'Fetch failed after {MAX_RETRIES} attempts with status {error_code}: {str(e)}', 'details': str(e)}
            except Exception as e:
                return {'error': f'Unexpected error: {str(e)}', 'details': str(e)}

# Example usage
if __name__ == "__main__":
    fetcher = EnhancedDataFetcher(api_url='https://api.nasa.gov', api_key='YOUR_API_KEY')
    data = fetcher.fetch_astronomical_data('/planetary/apod', params={'count': 1})
    print(data)

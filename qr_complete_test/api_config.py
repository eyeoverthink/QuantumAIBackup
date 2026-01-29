#!/usr/bin/env python3
"""
API CONFIG MODULE
================
A modular configuration for API settings, allowing easy updates without modifying core files.
Includes golden ratio-based defaults for retry logic if integrated.

Author: Cascade AI
Date: April 26, 2025
"""
API_ENDPOINTS = {
    'default': '/planetary/apod',  # Can be changed to more suitable endpoints
    'black_hole_data': '/exoplanet-catalog'  # Example; user should update to actual endpoints
}
NASA_API_URL = 'https://api.nasa.gov'
MAX_RETRIES = 5  # Based on Fibonacci for balance

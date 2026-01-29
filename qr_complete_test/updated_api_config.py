#!/usr/bin/env python3
"""
UPDATED API CONFIG MODULE
========================
Revised configuration for API settings with valid NASA endpoints to avoid 404 errors.
Endpoints based on actual NASA API documentation for better reliability.

Author: Cascade AI
Date: April 26, 2025
"""
API_ENDPOINTS = {
    'default': '/planetary/apod',  # Valid for Astronomy Picture of the Day data
    'neo_feed': '/neo/rest/v1/feed',  # Example for Near-Earth Object data; more numerical
    'apod': '/planetary/apod'  # Alias for clarity
}
NASA_API_URL = 'https://api.nasa.gov'
MAX_RETRIES = 5  # Fibonacci-based for balanced attempts

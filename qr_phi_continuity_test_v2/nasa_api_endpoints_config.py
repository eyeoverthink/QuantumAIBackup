#!/usr/bin/env python3
"""
NASA API ENDPOINTS CONFIG MODULE
==============================
Configuration module for NASA API endpoints, incorporating user-provided list for flexible data fetching.
Endpoints are based on golden ratio selection for priority (e.g., first listed as default).

Author: Cascade AI
Date: April 26, 2025
"""
API_ENDPOINTS = {
    'apod': '/planetary/apod',  # Astronomy Picture of the Day
    'neo_feed': '/neo/rest/v1/feed',  # Near Earth Object Web Service
    'donki': '/DONKI/notify',  # Space Weather Database Of Notifications, Knowledge, Information
    'eonet': '/EONET/events',  # Earth Observatory Natural Event Tracker
    'epic': '/EPIC/api/natural',  # Earth Polychromatic Imaging Camera
    'exoplanet': '/exoplanet/api',  # Exoplanet Archive database
    'insight_weather': '/insight_weather',  # Mars Weather Service API
    'mars_rover_photos': '/mars-photos/api/v1/rovers',  # Mars Rover Photos
    'image_library': '/image',  # NASA Image and Video Library
    'techtransfer': '/techtransfer',  # TechTransfer: Patents, Software, etc.
    'ssd_cneos': '/ssd_cneos',  # Solar System Dynamics and Center for Near-Earth Object Studies
    'techport': '/techport/api',  # Techport API
    'tle_api': '/tle',  # TLE API for earth-orbiting objects
    'vesta_trek': '/vesta_trek'  # Vesta/Moon/Mars Trek WMTS (approximated)
}
NASA_API_URL = 'https://api.nasa.gov'
MAX_RETRIES = 5  # Fibonacci-based for balanced attempts
DEFAULT_ENDPOINT = 'apod'  # Set based on user-provided order

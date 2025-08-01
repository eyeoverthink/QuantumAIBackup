#!/usr/bin/env python3
"""
Quantum Fractal DNA Interface API Test Script
This script tests the API endpoints using requests library
"""

import requests
import json
import sys
import time
from datetime import datetime

# Set the API base URL
API_BASE_URL = "http://localhost:5002"

# ANSI colors for output
GREEN = '\033[0;32m'
RED = '\033[0;31m'
BLUE = '\033[0;34m'
NC = '\033[0m'  # No Color

def print_colored(text, color):
    """Print colored text"""
    print(f"{color}{text}{NC}")

def print_header(text):
    """Print a header"""
    print()
    print_colored(text, BLUE)

def print_success(text):
    """Print a success message"""
    print_colored(f"✓ {text}", GREEN)

def print_error(text):
    """Print an error message"""
    print_colored(f"✗ {text}", RED)

def test_get_token():
    """Test getting an authentication token"""
    print_header("Test 1: Get authentication token")
    
    try:
        response = requests.post(
            f"{API_BASE_URL}/api/token",
            json={"username": "admin", "password": "secret"}
        )
        
        response_json = response.json()
        
        if response.status_code == 200 and "token" in response_json:
            token = response_json["token"]
            print_success("Successfully obtained token")
            print(f"Token: {token[:20]}...(truncated)")
            return token
        else:
            print_error(f"Failed to obtain token")
            print(f"Response: {response.text}")
            return None
    except Exception as e:
        print_error(f"Error: {str(e)}")
        return None

def test_process_query(token):
    """Test processing a quantum query"""
    print_header("Test 2: Process a quantum query")
    
    if not token:
        print_error("No token available, skipping test")
        return
    
    query = "Analyze quantum consciousness using phi-harmonic resonance"
    print(f"Query: {query}")
    
    try:
        response = requests.post(
            f"{API_BASE_URL}/api/process",
            headers={"Authorization": f"Bearer {token}"},
            json={"query": query}
        )
        
        if response.status_code == 200:
            response_json = response.json()
            
            if "quantum_state" in response_json:
                print_success("Successfully processed query")
                
                # Display quantum state
                print("Quantum State (first few values):")
                quantum_state = response_json["quantum_state"]
                if isinstance(quantum_state, list):
                    for i, value in enumerate(quantum_state[:3]):
                        print(f"  {value}")
                
                # Display answer snippet
                if "answer" in response_json:
                    answer = response_json["answer"]
                    print("Answer snippet:")
                    print(f"  {answer[:100]}...")
            else:
                print_error("Response missing quantum_state")
                print(f"Response: {json.dumps(response_json, indent=2)}")
        else:
            print_error(f"Failed to process query: {response.status_code}")
            print(f"Response: {response.text}")
    except Exception as e:
        print_error(f"Error: {str(e)}")

def test_get_history(token):
    """Test getting query history"""
    print_header("Test 3: Get query history")
    
    if not token:
        print_error("No token available, skipping test")
        return
    
    try:
        response = requests.get(
            f"{API_BASE_URL}/api/history",
            headers={"Authorization": f"Bearer {token}"}
        )
        
        if response.status_code == 200:
            response_json = response.json()
            
            if "history" in response_json:
                print_success("Successfully retrieved history")
                
                history = response_json["history"]
                if isinstance(history, list):
                    print(f"History entries: {len(history)}")
                else:
                    print("History is not a list")
            else:
                print_error("Response missing history")
                print(f"Response: {json.dumps(response_json, indent=2)}")
        else:
            print_error(f"Failed to get history: {response.status_code}")
            print(f"Response: {response.text}")
    except Exception as e:
        print_error(f"Error: {str(e)}")

def test_invalid_token():
    """Test with invalid token"""
    print_header("Test 4: Test with invalid token")
    
    try:
        response = requests.get(
            f"{API_BASE_URL}/api/history",
            headers={"Authorization": "Bearer invalid_token"}
        )
        
        if response.status_code == 401:
            print_success("Authentication working correctly")
            
            response_json = response.json()
            if "error" in response_json:
                print(f"Error message: {response_json['error']}")
        else:
            print_error(f"Authentication test failed: {response.status_code}")
            print(f"Response: {response.text}")
    except Exception as e:
        print_error(f"Error: {str(e)}")

def test_phi_harmonic_resonance(token):
    """Test phi-harmonic resonance calculation"""
    print_header("Test 5: Test phi-harmonic resonance calculation")
    
    if not token:
        print_error("No token available, skipping test")
        return
    
    query = "Calculate phi-harmonic resonance patterns in quantum fields"
    print(f"Query: {query}")
    
    try:
        response = requests.post(
            f"{API_BASE_URL}/api/process",
            headers={"Authorization": f"Bearer {token}"},
            json={"query": query}
        )
        
        if response.status_code == 200:
            response_json = response.json()
            
            if "classical_physics" in response_json:
                print_success("Successfully calculated phi-harmonic resonance")
                
                # Display classical physics metrics
                print("Classical Physics metrics:")
                classical_physics = response_json["classical_physics"]
                if isinstance(classical_physics, dict):
                    for key, value in classical_physics.items():
                        print(f"  {key}: {value}")
                else:
                    print(f"  {classical_physics}")
            else:
                print_error("Response missing classical_physics")
                print(f"Response: {json.dumps(response_json, indent=2)}")
        else:
            print_error(f"Failed to calculate phi-harmonic resonance: {response.status_code}")
            print(f"Response: {response.text}")
    except Exception as e:
        print_error(f"Error: {str(e)}")

def main():
    """Main function"""
    print_colored("=== Quantum Fractal DNA Interface API Test ===", BLUE)
    print_colored(f"Testing API at: {API_BASE_URL}", BLUE)
    
    # Test 1: Get authentication token
    token = test_get_token()
    
    # Test 2: Process a quantum query
    test_process_query(token)
    
    # Test 3: Get query history
    test_get_history(token)
    
    # Test 4: Test with invalid token
    test_invalid_token()
    
    # Test 5: Test phi-harmonic resonance calculation
    test_phi_harmonic_resonance(token)
    
    print()
    print_colored("=== Tests Completed ===", BLUE)

if __name__ == "__main__":
    main()

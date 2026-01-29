#!/usr/bin/env python
import requests
import json
import time
import sys

def test_api(port=5052):
    """Test the Quantum AI API endpoints directly"""
    base_url = f"http://127.0.0.1:{port}"
    
    print(f"Testing Quantum AI API on port {port}...")
    
    # Test 1: Quantum Metrics endpoint
    print("\n1. Testing /api/quantum_metrics endpoint")
    try:
        metrics_response = requests.get(f"{base_url}/api/quantum_metrics", timeout=5)
        
        if metrics_response.status_code == 200:
            metrics = metrics_response.json()
            print("✅ Quantum Metrics API successful")
            
            # Display QHRC metrics
            if 'qhrc' in metrics:
                qhrc = metrics['qhrc']
                print(f"  • Resonance Efficiency: {qhrc.get('resonance_efficiency')}")
                print(f"  • Energy Transfer: {qhrc.get('energy_transfer')}")
                print(f"  • Current Efficiency: {qhrc.get('current_efficiency')}%")
                print(f"  • Maximum Efficiency: {qhrc.get('max_efficiency')}%")
            
            # Display φπ metrics
            if 'phi_pi' in metrics:
                phi_pi = metrics['phi_pi']
                print(f"  • φπ Resonance Factor: {phi_pi.get('resonance_factor')}")
                print(f"  • Frequency Ratio: {phi_pi.get('frequency_ratio')}")
                print(f"  • Golden Ratio Proximity: {phi_pi.get('golden_ratio_proximity')}")
        else:
            print(f"❌ Quantum Metrics API failed: {metrics_response.status_code}")
            print(f"Error: {metrics_response.text}")
    except Exception as e:
        print(f"❌ Error connecting to metrics endpoint: {str(e)}")
    
    # Test 2: Process endpoint
    print("\n2. Testing /api/process endpoint with QHRC query")
    try:
        query_data = {
            "query": "Tell me about the Quantum Harmonic Resonance Coil",
            "brain_type": "Standard"
        }
        
        process_response = requests.post(
            f"{base_url}/api/process", 
            json=query_data,
            timeout=5
        )
        
        if process_response.status_code == 200:
            result = process_response.json()
            print("✅ Process API successful")
            if 'text' in result:
                print(f"Response: {result['text'][:150]}...")
            elif 'response' in result and 'answer' in result['response']:
                print(f"Response: {result['response']['answer'][:150]}...")
            else:
                print(f"Response structure: {json.dumps(result, indent=2)[:150]}...")
        else:
            print(f"❌ Process API failed: {process_response.status_code}")
            print(f"Error: {process_response.text}")
    except Exception as e:
        print(f"❌ Error connecting to process endpoint: {str(e)}")

if __name__ == "__main__":
    # Use command line argument for port if provided, otherwise default to 5052
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 5052
    test_api(port)

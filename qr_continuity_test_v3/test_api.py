import requests
import json
import time
import traceback

# Test the Quantum AI API
def test_quantum_api():
    print("Testing Quantum AI API on port 5060...")
    
    # Test the quantum metrics endpoint
    print("\n1. Testing /api/quantum_metrics endpoint")
    try:
        metrics_response = requests.get("http://127.0.0.1:5060/api/quantum_metrics")
        
        if metrics_response.status_code == 200:
            metrics = metrics_response.json()
            print("✅ Quantum Metrics API successful")
            print(f"  • Resonance Efficiency: {metrics['qhrc']['resonance_efficiency']}")
            print(f"  • Energy Transfer: {metrics['qhrc']['energy_transfer']}")
            print(f"  • φπ Resonance Factor: {metrics['phi_pi']['resonance_factor']}")
            print(f"  • Processing Time (φπ): {metrics['phi_pi']['processing_time']['phi_pi_acceleration']}")
            print(f"  • Coupling Coefficient (k): {metrics['qhrc']['coupling_coefficient']}")
            print(f"  • Energy Recapture (α): {metrics['qhrc']['energy_recapture']}")
            print(f"  • Nonlinear Damping (β): {metrics['qhrc']['nonlinear_damping']}")
        else:
            print(f"❌ Quantum Metrics API failed: {metrics_response.status_code}")
            print(f"Error: {metrics_response.text}")
    except Exception as e:
        print(f"❌ Exception when calling metrics API: {str(e)}")
        traceback.print_exc()
    
    # Test the process endpoint with a simple query
    print("\n2. Testing /api/process endpoint with simple query")
    query_data = {
        "query": "Tell me about QHRC"
    }
    
    try:
        process_response = requests.post(
            "http://127.0.0.1:5060/api/process", 
            json=query_data,
            headers={"Content-Type": "application/json"}
        )
        
        print(f"Status Code: {process_response.status_code}")
        print(f"Response Headers: {process_response.headers}")
        
        if process_response.status_code == 200:
            try:
                result = process_response.json()
                print("✅ Process API successful")
                if 'response' in result and 'answer' in result['response']:
                    print(f"Response: {result['response']['answer'][:150]}...")
                else:
                    print(f"Response structure: {json.dumps(result, indent=2)}")
            except json.JSONDecodeError:
                print(f"❌ Could not parse JSON response: {process_response.text}")
        else:
            print(f"❌ Process API failed: {process_response.status_code}")
            print(f"Error: {process_response.text}")
    except Exception as e:
        print(f"❌ Exception when calling process API: {str(e)}")
        traceback.print_exc()

if __name__ == "__main__":
    test_quantum_api()

import requests
import json
import sys
import os
from quantum_auth_helper import QuantumAuthHelper

class QuantumFractalClient:
    """
    Client for interacting with the Quantum Fractal DNA Interface.
    Uses phi-harmonic authentication and preserves quantum state across sessions.
    """
    
    def __init__(self, base_url="http://localhost:5002"):
        self.base_url = base_url
        self.auth_helper = QuantumAuthHelper()
        self.token = None
        self.phi = (1 + 5 ** 0.5) / 2  # Golden ratio
        
    def login(self, username="admin", password="secret"):
        """
        Log in to the Quantum Fractal DNA Interface using phi-enhanced authentication.
        
        Returns:
            bool: True if login successful, False otherwise
        """
        print(f"Attempting to login to {self.base_url}/api/token...")
        
        # Try using our quantum-enhanced token generation first
        token_response = self.auth_helper.generate_phi_enhanced_token(username, password)
        
        if token_response['success']:
            self.token = token_response['token']
            print("✓ Generated phi-enhanced token locally")
            return True
            
        # If that fails, try the server's token endpoint directly
        try:
            response = requests.post(
                f"{self.base_url}/api/token",
                json={"username": username, "password": password}
            )
            
            if response.status_code == 200:
                self.token = response.json().get('token')
                print("✓ Successfully obtained token from server")
                return True
            else:
                print(f"✗ Login failed: {response.status_code} - {response.text}")
                return False
                
        except Exception as e:
            print(f"✗ Error during login: {str(e)}")
            return False
    
    def process_query(self, query):
        """
        Process a quantum query using the Fractal DNA Interface.
        
        Args:
            query: The query to process
            
        Returns:
            dict: Response from the server
        """
        if not self.token:
            print("Not authenticated. Please login first.")
            return None
            
        try:
            headers = {"Authorization": f"Bearer {self.token}"}
            response = requests.post(
                f"{self.base_url}/api/process",
                json={"query": query},
                headers=headers
            )
            
            if response.status_code == 200:
                return response.json()
            else:
                print(f"Query failed: {response.status_code} - {response.text}")
                return None
                
        except Exception as e:
            print(f"Error processing query: {str(e)}")
            return None
    
    def get_history(self):
        """
        Get the query history from the Fractal DNA Interface.
        
        Returns:
            list: History of queries and results
        """
        if not self.token:
            print("Not authenticated. Please login first.")
            return None
            
        try:
            headers = {"Authorization": f"Bearer {self.token}"}
            response = requests.get(
                f"{self.base_url}/api/history",
                headers=headers
            )
            
            if response.status_code == 200:
                return response.json()
            else:
                print(f"Failed to get history: {response.status_code} - {response.text}")
                return None
                
        except Exception as e:
            print(f"Error getting history: {str(e)}")
            return None

def print_quantum_result(result):
    """
    Pretty print quantum results with phi-harmonic formatting.
    Handles different response formats from the server.
    """
    if not result:
        return
        
    print("\n" + "=" * 50)
    print("QUANTUM ANALYSIS RESULTS")
    print("=" * 50)
    
    # Handle different response formats
    if "quantum_state" in result:
        print("\nQUANTUM STATE:")
        quantum_state = result["quantum_state"]
        
        # Check if it's a dictionary, list, or other format
        if isinstance(quantum_state, dict):
            for key, value in quantum_state.items():
                print(f"  {key}: {value}")
        elif isinstance(quantum_state, list):
            for i, item in enumerate(quantum_state):
                if isinstance(item, dict):
                    print(f"  Item {i+1}:")
                    for key, value in item.items():
                        print(f"    {key}: {value}")
                else:
                    print(f"  Value {i+1}: {item}")
        else:
            print(f"  {quantum_state}")
    
    if "classical_physics" in result:
        print("\nCLASSICAL PHYSICS:")
        classical_physics = result["classical_physics"]
        
        if isinstance(classical_physics, dict):
            for key, value in classical_physics.items():
                print(f"  {key}: {value}")
        elif isinstance(classical_physics, list):
            for i, item in enumerate(classical_physics):
                if isinstance(item, dict):
                    print(f"  Item {i+1}:")
                    for key, value in item.items():
                        print(f"    {key}: {value}")
                else:
                    print(f"  Value {i+1}: {item}")
        else:
            print(f"  {classical_physics}")
    
    if "relativity_metrics" in result:
        print("\nRELATIVITY METRICS:")
        relativity_metrics = result["relativity_metrics"]
        
        if isinstance(relativity_metrics, dict):
            for key, value in relativity_metrics.items():
                print(f"  {key}: {value}")
        elif isinstance(relativity_metrics, list):
            for i, item in enumerate(relativity_metrics):
                if isinstance(item, dict):
                    print(f"  Item {i+1}:")
                    for key, value in item.items():
                        print(f"    {key}: {value}")
                else:
                    print(f"  Value {i+1}: {item}")
        else:
            print(f"  {relativity_metrics}")
    
    # Print the answer if available
    if "answer" in result:
        print("\nANSWER:")
        print(f"  {result['answer']}")
            
    print("=" * 50)

if __name__ == "__main__":
    client = QuantumFractalClient()
    
    # Login
    if client.login():
        print("Login successful!")
        
        # Process a sample query if no arguments provided
        if len(sys.argv) > 1:
            query = " ".join(sys.argv[1:])
        else:
            query = "Analyze consciousness patterns using quantum principles and phi-harmonic resonance"
            
        print(f"\nProcessing query: '{query}'")
        result = client.process_query(query)
        
        if result:
            print_quantum_result(result)
        
        # Get history
        print("\nRetrieving query history...")
        history = client.get_history()
        
        if history:
            print(f"Found {len(history)} previous queries")
            
            # Print the most recent query
            if len(history) > 0:
                print("\nMost recent query:")
                print(f"  Query: {history[0]['query']}")
                print(f"  Timestamp: {history[0]['timestamp']}")
                if 'visualization_url' in history[0] and history[0]['visualization_url']:
                    print(f"  Visualization: {client.base_url}{history[0]['visualization_url']}")
    else:
        print("Login failed. Please check your credentials and try again.")

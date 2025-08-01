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
    """
    if not result:
        return
        
    print("\n" + "=" * 50)
    print("QUANTUM ANALYSIS RESULTS")
    print("=" * 50)
    
    if "quantum_state" in result:
        print("\nQUANTUM STATE:")
        for key, value in result["quantum_state"].items():
            print(f"  {key}: {value}")
    
    if "classical_physics" in result:
        print("\nCLASSICAL PHYSICS:")
        for key, value in result["classical_physics"].items():
            print(f"  {key}: {value}")
    
    if "relativity_metrics" in result:
        print("\nRELATIVITY METRICS:")
        for key, value in result["relativity_metrics"].items():
            print(f"  {key}: {value}")
            
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
    else:
        print("Login failed. Please check your credentials and try again.")

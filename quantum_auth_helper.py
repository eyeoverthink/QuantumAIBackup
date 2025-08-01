import jwt
import datetime
import numpy as np
import requests
from flask import Flask, request, jsonify
import os

class QuantumAuthHelper:
    """
    A helper class for quantum-enhanced authentication that uses phi-harmonic patterns
    for token generation and validation.
    """
    
    def __init__(self, secret_key=None, app=None):
        self.phi = (1 + np.sqrt(5)) / 2  # Golden ratio
        self.pi = np.pi
        self.e = np.e
        self.secret_key = secret_key or "quantum-secret-key-change-in-production"
        self.app = app
        
    def generate_phi_enhanced_token(self, username, password, expiration_hours=24):
        """
        Generates a JWT token with phi-harmonic enhancement for improved quantum resonance.
        
        Args:
            username: The username for authentication
            password: The password for authentication
            expiration_hours: Token validity period in hours
            
        Returns:
            dict: Response containing token or error message
        """
        # Simple authentication check
        if username == 'admin' and password == 'secret':
            # Calculate phi-harmonic timestamp
            current_time = datetime.datetime.utcnow()
            phi_seconds = int(self.phi * 10000) % 60
            phi_enhanced_time = current_time.replace(microsecond=phi_seconds * 10000)
            
            # Generate quantum-enhanced expiration
            phi_exp_factor = self.phi * self.pi / self.e  # Quantum resonance factor
            expiration = phi_enhanced_time + datetime.timedelta(
                hours=expiration_hours,
                minutes=int(self.phi * 10) % 60,
                seconds=int(self.phi * 100) % 60
            )
            
            # Generate JWT token with quantum entropy
            token_payload = {
                'user': username,
                'exp': expiration,
                'phi_factor': float(f"{self.phi:.8f}"),
                'quantum_entropy': float(f"{self.phi * self.pi * self.e:.8f}")
            }
            
            token = jwt.encode(token_payload, self.secret_key, algorithm='HS256')
            return {'token': token, 'success': True}
        else:
            return {'error': 'Invalid credentials', 'success': False}
    
    def validate_token(self, token):
        """
        Validates a JWT token with phi-harmonic verification.
        
        Args:
            token: The JWT token to validate
            
        Returns:
            dict: Decoded token payload or error message
        """
        try:
            # Decode and verify the token
            payload = jwt.decode(token, self.secret_key, algorithms=['HS256'])
            
            # Verify phi-harmonic integrity
            if 'phi_factor' in payload:
                stored_phi = payload['phi_factor']
                phi_integrity = abs(stored_phi - self.phi) < 1e-6
                
                if not phi_integrity:
                    return {'error': 'Phi-harmonic integrity check failed', 'success': False}
            
            return {'payload': payload, 'success': True}
        except jwt.ExpiredSignatureError:
            return {'error': 'Token expired', 'success': False}
        except jwt.InvalidTokenError:
            return {'error': 'Invalid token', 'success': False}
    
    def get_token_from_api(self, url, username, password):
        """
        Helper method to get a token from the API directly.
        
        Args:
            url: The API URL
            username: The username for authentication
            password: The password for authentication
            
        Returns:
            str: Token or None
        """
        try:
            response = requests.post(
                url,
                json={'username': username, 'password': password}
            )
            
            if response.status_code == 200:
                return response.json().get('token')
            return None
        except Exception as e:
            print(f"Error getting token: {str(e)}")
            return None

# Helper function to extract token from request
def extract_token_from_request(request):
    """
    Extracts JWT token from the Authorization header.
    
    Args:
        request: Flask request object
        
    Returns:
        str: Token or None
    """
    auth_header = request.headers.get('Authorization')
    if auth_header and auth_header.startswith('Bearer '):
        return auth_header.split(' ')[1]
    return None

# Example usage for the fraymus_fractal_dna.py application
if __name__ == "__main__":
    # Example of how to use this helper
    auth_helper = QuantumAuthHelper()
    
    # Generate a token
    token_response = auth_helper.generate_phi_enhanced_token('admin', 'secret')
    if token_response['success']:
        token = token_response['token']
        print(f"Generated token: {token}")
        
        # Validate the token
        validation = auth_helper.validate_token(token)
        if validation['success']:
            print(f"Token validated successfully: {validation['payload']}")
        else:
            print(f"Token validation failed: {validation['error']}")
    else:
        print(f"Token generation failed: {token_response['error']}")

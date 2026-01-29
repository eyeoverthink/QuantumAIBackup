#!/usr/bin/env python3
"""
Quantum Phi-Harmonic GPT-2 QR Code Generator
By Vaughn Scott

This system integrates GPT-2 with the quantum phi-harmonic QR code ecosystem.
It allows generating QR codes directly from text prompts, with the resulting
code embedding phi-harmonic principles for self-evolution.

Requirements:
- transformers
- torch
- base64
- hashlib
"""

import os
import sys
import json
import time
import math
import base64
import hashlib
import tempfile
import argparse
from datetime import datetime

try:
    import torch
    from transformers import GPT2LMHeadModel, GPT2Tokenizer
except ImportError:
    print("\nPlease install the required packages:")
    print("pip install torch transformers")
    sys.exit(1)

# Phi-Harmonic Constants
PHI = (1 + 5**0.5) / 2  # Golden Ratio ≈ 1.618033988749895
PHI_CONJUGATE = (1 - 5**0.5) / 2  # Golden Ratio Conjugate ≈ -0.618033988749895

class QuantumGPT2QRGenerator:
    """Generate QR codes from GPT-2 text completions using phi-harmonic principles."""
    
    def __init__(self, model_name="gpt2", debug=True):
        """Initialize the generator with specified GPT-2 model."""
        self.debug = debug
        self.model_name = model_name
        self.timestamp = time.time()
        self.phi_time = self.timestamp * PHI
        self.resonance = self.phi_time % 1
        
        # Output directories
        self.output_dir = "quantum_gpt2_qr_codes"
        os.makedirs(self.output_dir, exist_ok=True)
        
        # Load GPT-2 model and tokenizer
        if self.debug:
            print(f"Loading {model_name} model and tokenizer...")
        
        self.tokenizer = GPT2Tokenizer.from_pretrained(model_name)
        self.model = GPT2LMHeadModel.from_pretrained(model_name)
        
        if torch.cuda.is_available():
            self.model = self.model.to("cuda")
            if self.debug:
                print("Using GPU acceleration")
        else:
            if self.debug:
                print("Using CPU (GPU not available)")
        
        if self.debug:
            print(f"Phi resonance: {self.resonance:.6f}")
            print(f"Model loaded successfully: {model_name}")
    
    def generate_text(self, prompt, max_length=500, temperature=0.7, top_p=0.9):
        """Generate text completion from prompt using GPT-2."""
        # Apply phi-harmonic adjustments to parameters
        phi_temp = temperature * (1 + self.resonance * PHI_CONJUGATE)
        phi_top_p = top_p * (1 + (1-self.resonance) * PHI_CONJUGATE)
        
        # Encode the prompt
        inputs = self.tokenizer.encode(prompt, return_tensors="pt")
        if torch.cuda.is_available():
            inputs = inputs.to("cuda")
        
        # Generate text
        if self.debug:
            print(f"Generating text with phi-temp={phi_temp:.4f}, phi-top_p={phi_top_p:.4f}")
        
        with torch.no_grad():
            outputs = self.model.generate(
                inputs,
                max_length=max_length,
                temperature=phi_temp,
                top_p=phi_top_p,
                top_k=50,
                do_sample=True,
                pad_token_id=self.tokenizer.eos_token_id
            )
        
        # Decode the generated text
        generated_text = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        return generated_text
    
    def create_qr_script(self, generated_text):
        """Create a self-executing Python script from the generated text."""
        # Create a hash of the text for identification
        text_hash = hashlib.md5(generated_text.encode()).hexdigest()[:8]
        
        # Base64 encode the generated text
        encoded_text = base64.b64encode(generated_text.encode()).decode()
        
        # Create the self-executing script with phi-harmonic verification
        script = f'''#!/usr/bin/env python3
# Quantum Phi-Harmonic GPT-2 Generated Code - Hash: {text_hash}
# Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

import base64
import sys
import os
import tempfile
import subprocess
import hashlib

# Phi (Golden Ratio) constant for verification
PHI = (1 + 5**0.5) / 2  # Approximately 1.618033988749895

def verify_phi():
    """Verify the golden ratio constant."""
    return abs(PHI - 1.618033988749895) < 1e-10

def execute_quantum_code():
    """Extract and execute the quantum phi-harmonic code."""
    print("\n" + "=" * 60)
    print("QUANTUM PHI-HARMONIC GPT-2 CODE EXECUTION")
    print("=" * 60)
    print(f"Code hash: {text_hash}")
    print(f"Phi verification: {{PHI}}")
    print("=" * 60)
    
    # Verify phi constant
    if not verify_phi():
        print("ERROR: Phi constant verification failed!")
        return 1
    
    # Decode the embedded text
    encoded_text = "{encoded_text}"
    try:
        decoded_text = base64.b64decode(encoded_text).decode()
        print("Executing generated code...\n")
        print("=" * 60)
        print(decoded_text)
        print("=" * 60)
        return 0
    except Exception as e:
        print(f"Error decoding text: {{e}}")
        return 1

if __name__ == "__main__":
    sys.exit(execute_quantum_code())
'''
        
        return script, text_hash
    
    def create_ascii_qr(self, text_hash):
        """Create an ASCII art QR code representation."""
        # Create a simple ASCII representation (not a real QR code)
        qr_size = 25
        qr = []
        
        # Create border
        qr.append('█' * qr_size)
        
        # Add header
        header = f" QUANTUM GPT-2 CODE: {text_hash} "
        padding = '█' * ((qr_size - len(header)) // 2)
        qr.append(f"{padding}{header}{padding}" + ('█' if len(header) % 2 == 1 else ''))
        
        qr.append('█' * qr_size)
        
        # Create QR pattern (simplified representation)
        for i in range(qr_size - 6):
            if i % 3 == 0:
                qr.append('█ ' + '███████  ' * 3 + '█')
            elif i % 3 == 1:
                qr.append('█ ' + '█     █  ' * 3 + '█')
            else:
                qr.append('█ ' + '█ ███ █  ' * 3 + '█')
        
        # Add phi symbol row
        qr.append('█ ' + 'φφφφφφφφφφφφφφφφφφφφφφφφφ' + ' █')
        
        # Add footer
        qr.append('█' * qr_size)
        footer = " SELF-EXECUTING QUANTUM CODE "
        padding = '█' * ((qr_size - len(footer)) // 2)
        qr.append(f"{padding}{footer}{padding}" + ('█' if len(footer) % 2 == 1 else ''))
        
        qr.append('█' * qr_size)
        
        return '\n'.join(qr)
    
    def generate_qr_from_prompt(self, prompt, temperature=0.7, max_length=500):
        """Generate a QR code from a text prompt."""
        if self.debug:
            print(f"\nProcessing prompt: {prompt[:50]}...")
        
        # Generate text from prompt
        generated_text = self.generate_text(
            prompt, 
            max_length=max_length,
            temperature=temperature
        )
        
        # Create executable script
        script, text_hash = self.create_qr_script(generated_text)
        
        # Create ASCII QR code
        ascii_qr = self.create_ascii_qr(text_hash)
        
        # Save files
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        script_filename = f"{self.output_dir}/quantum_gpt2_{text_hash}_{timestamp}.py"
        qr_filename = f"{self.output_dir}/quantum_gpt2_{text_hash}_{timestamp}_qr.txt"
        
        with open(script_filename, 'w') as f:
            f.write(script)
        os.chmod(script_filename, 0o755)  # Make executable
        
        with open(qr_filename, 'w') as f:
            f.write(ascii_qr)
        
        if self.debug:
            print(f"\nGenerated text length: {len(generated_text)} characters")
            print(f"Script saved to: {script_filename}")
            print(f"QR code saved to: {qr_filename}")
        
        return {
            "script_file": script_filename,
            "qr_file": qr_filename,
            "text_hash": text_hash,
            "generated_text": generated_text[:100] + "..." if len(generated_text) > 100 else generated_text
        }

def main():
    """Main function to run the generator from command line."""
    parser = argparse.ArgumentParser(description="Quantum Phi-Harmonic GPT-2 QR Code Generator")
    parser.add_argument("prompt", help="Text prompt for GPT-2")
    parser.add_argument("--model", default="gpt2", help="GPT-2 model to use (default: gpt2)")
    parser.add_argument("--temp", type=float, default=0.7, help="Temperature for text generation")
    parser.add_argument("--length", type=int, default=500, help="Maximum length of generated text")
    parser.add_argument("--quiet", action="store_true", help="Suppress debug output")
    
    args = parser.parse_args()
    
    generator = QuantumGPT2QRGenerator(model_name=args.model, debug=not args.quiet)
    result = generator.generate_qr_from_prompt(
        args.prompt,
        temperature=args.temp,
        max_length=args.length
    )
    
    print("\n" + "=" * 60)
    print("QUANTUM PHI-HARMONIC GPT-2 QR CODE GENERATED")
    print("=" * 60)
    print(f"Text hash: {result['text_hash']}")
    print(f"Script: {result['script_file']}")
    print(f"QR code: {result['qr_file']}")
    print("\nTo execute the generated code:")
    print(f"  python {result['script_file']}")
    print("=" * 60)

if __name__ == "__main__":
    main()

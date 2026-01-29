#!/usr/bin/env python3
"""
QR Genome Updater - Updates the QR Genome with actual code
By Vaughn Scott

This script updates the QR genome JSON file with actual code from the template.
"""

import json
import os
import inspect
from qr_genome_template import (
    initialize_codon, 
    import_libraries_codon,
    data_processing_codon,
    calculation_codon,
    mutate_codon,
    select_codon,
    generate_output_codon,
    visualize_codon
)

def get_function_source(func):
    """Get the source code of a function as a string."""
    return inspect.getsource(func)

def update_genome_with_code():
    """Update the genome JSON file with actual code from the template."""
    print("🧬 Updating QR genome with actual code...")
    
    # Function mapping to codon types
    codon_functions = {
        "initialize": initialize_codon,
        "import_libraries": import_libraries_codon,
        "data_processing": data_processing_codon,
        "calculation": calculation_codon,
        "mutate": mutate_codon,
        "select": select_codon,
        "generate_output": generate_output_codon,
        "visualize": visualize_codon
    }
    
    # Load the genome JSON
    genome_file = "qr_genome.json"
    try:
        with open(genome_file, "r") as f:
            genome = json.load(f)
    except Exception as e:
        print(f"❌ Error loading genome file: {e}")
        return False
    
    # Update each codon with actual code
    codons_updated = 0
    for group in genome["groups"]:
        for codon in group["codons"]:
            codon_type = codon["codon_type"]
            if codon_type in codon_functions:
                # Get the function source code
                func = codon_functions[codon_type]
                source_code = get_function_source(func)
                
                # Update the codon frame data
                codon["frame_data"]["task_type"] = "execute_python"
                codon["frame_data"]["task_data"] = {"code": source_code}
                
                codons_updated += 1
    
    # Save the updated genome
    try:
        with open(genome_file, "w") as f:
            json.dump(genome, f, indent=2)
        print(f"✅ Updated {codons_updated} codons with actual code")
        print(f"✅ Saved updated genome to {genome_file}")
        return True
    except Exception as e:
        print(f"❌ Error saving genome file: {e}")
        return False

if __name__ == "__main__":
    update_genome_with_code()

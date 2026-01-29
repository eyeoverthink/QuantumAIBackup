"""
Test the enhanced protein analysis system with PDB integration, 3D visualization,
and parallel processing optimizations.
"""
from quantum_protein_mapper import QuantumProteinMapper
from quantum_protein_visualizer import QuantumProteinVisualizer
import time

def test_large_protein(pdb_id='1HHO'):  # Hemoglobin
    print("🧬 Testing Large Protein Analysis")
    print("=" * 40)
    
    # Initialize components
    mapper = QuantumProteinMapper()
    visualizer = QuantumProteinVisualizer()
    
    # Fetch and analyze structure
    print(f"Fetching PDB structure {pdb_id}...")
    pdb_data = visualizer.analyze_pdb_structure(pdb_id)
    
    if not pdb_data:
        print(f"Failed to fetch {pdb_id}")
        return
        
    sequence = pdb_data['sequence']
    print(f"Sequence length: {len(sequence)}")
    
    # Time the analysis
    print("\nRunning quantum analysis...")
    start_time = time.time()
    
    analysis = mapper.analyze_sequence(sequence)
    
    end_time = time.time()
    print(f"Analysis completed in {end_time - start_time:.2f} seconds")
    
    # Print results
    print("\n📊 Analysis Results")
    print("-" * 20)
    print(f"Quantum Bridges: {len(analysis['quantum_bridges'])}")
    print(f"Phi Alignment: {analysis['phi_alignment']:.4f}")
    print("\nFold Metrics:")
    print(f"Alpha Helix Prob: {analysis['fold_metrics']['alpha_helix_probability']:.4f}")
    print(f"Beta Sheet Prob: {analysis['fold_metrics']['beta_sheet_probability']:.4f}")
    
    # Predict structure
    print("\n🔮 Structure Prediction")
    print("-" * 20)
    prediction = mapper.predict_structure(sequence)
    print(f"Confidence: {prediction['confidence']:.4f}")
    print(f"Stability: {prediction['stability_score']:.4f}")
    print(f"Quantum Coherence: {prediction['quantum_metrics']['coherence']:.4f}")
    
    # Find binding sites
    print("\n🎯 Binding Sites")
    print("-" * 20)
    binding_sites = mapper.find_binding_sites(sequence)
    print(f"Found {len(binding_sites)} potential binding sites")
    
    for i, site in enumerate(binding_sites[:5], 1):
        print(f"\nSite {i}:")
        print(f"Position: {site['position']}")
        print(f"Sequence: {site['sequence']}")
        print(f"Coherence: {site['coherence']:.4f}")
    
    # Create 3D visualization
    print("\n🎨 Creating 3D Visualization")
    print("-" * 20)
    view = visualizer.create_interactive_view(pdb_id, analysis)
    
    if view:
        print("3D visualization created successfully")
        print("Quantum bridges and binding sites mapped")
    else:
        print("Failed to create visualization")

def test_performance_scaling():
    """Test performance scaling with different protein sizes"""
    print("\n⚡ Performance Scaling Test")
    print("=" * 40)
    
    mapper = QuantumProteinMapper()
    sizes = [100, 1000, 10000, 100000]
    
    # Generate test sequences of different sizes
    test_sequence = "ARNDCQEGHILKMFPSTWYV" * 5000  # Base sequence
    
    for size in sizes:
        sequence = test_sequence[:size]
        print(f"\nTesting size: {size}")
        
        start_time = time.time()
        analysis = mapper.analyze_sequence(sequence)
        end_time = time.time()
        
        print(f"Time: {end_time - start_time:.2f}s")
        print(f"Bridges found: {len(analysis['quantum_bridges'])}")
        print(f"Phi alignment: {analysis['phi_alignment']:.4f}")

if __name__ == "__main__":
    # Test with real protein
    test_large_protein()
    
    # Test performance scaling
    test_performance_scaling()

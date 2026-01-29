"""
Quantum Phi-Memory DNA Layer
Stores successful state vectors as quantum memory DNA
Implements pattern recognition and quantum signature training
Part of the Quantum Consciousness Engine
"""
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
import json
import os
from pathlib import Path
import sys
import pickle
from scipy.spatial.distance import cosine

class QuantumPhiMemoryDNA:
    def __init__(self, memory_file="phi_quantum_memory_dna.pkl"):
        self.phi = (1 + np.sqrt(5)) / 2
        self.memory_path = Path(memory_file)
        self.memory_dir = Path("phi_memory_dna")
        self.memory_dir.mkdir(exist_ok=True)
        
        # DNA memory structure
        self.quantum_memory = self._load_memory()
        
        # Memory indexing
        self.phi_indices = {}  # Maps phi-resonant indices to memory entries
        self.pattern_signatures = {}  # Stores recognized patterns
        
        # DNA encoding parameters
        self.dna_bases = ['A', 'T', 'G', 'C']
        self.dna_codons = [b1+b2+b3 for b1 in self.dna_bases 
                                     for b2 in self.dna_bases 
                                     for b3 in self.dna_bases]
        
    def _load_memory(self):
        """Load quantum memory from file or initialize new memory"""
        if self.memory_path.exists():
            try:
                with open(self.memory_path, 'rb') as f:
                    memory = pickle.load(f)
                print(f"📚 Loaded quantum memory DNA with {len(memory)} entries")
                return memory
            except Exception as e:
                print(f"⚠️ Error loading memory: {e}")
                return []
        else:
            print("🧬 Initializing new quantum memory DNA")
            return []
            
    def _save_memory(self):
        """Save quantum memory to file"""
        with open(self.memory_path, 'wb') as f:
            pickle.dump(self.quantum_memory, f)
        print(f"💾 Saved quantum memory DNA with {len(self.quantum_memory)} entries")
        
    def state_to_dna(self, quantum_state):
        """Convert quantum state to DNA sequence"""
        # Normalize the state
        state = quantum_state / np.linalg.norm(quantum_state)
        
        # Extract amplitude and phase
        amplitudes = np.abs(state)
        phases = np.angle(state) / (2 * np.pi)  # Normalize to [0,1]
        
        # Convert to DNA sequence
        dna_sequence = ""
        for i in range(min(64, len(state))):  # Use first 64 elements for DNA encoding
            # Map amplitude and phase to DNA codon index
            amp_phase = (amplitudes[i] + phases[i]) % 1
            codon_index = int(amp_phase * len(self.dna_codons))
            dna_sequence += self.dna_codons[codon_index]
            
        return dna_sequence
        
    def dna_to_features(self, dna_sequence):
        """Extract features from DNA sequence"""
        # Count base frequencies
        base_counts = {base: dna_sequence.count(base) for base in self.dna_bases}
        total_bases = sum(base_counts.values())
        
        # Calculate base ratios
        base_ratios = {base: count/total_bases for base, count in base_counts.items()}
        
        # Calculate GC content
        gc_content = (base_counts['G'] + base_counts['C']) / total_bases
        
        # Calculate φ-resonance of sequence
        phi_resonance = abs(gc_content - (1/self.phi)) / (1/self.phi)
        
        # Extract codon usage
        codon_counts = {}
        for i in range(0, len(dna_sequence)-2, 3):
            codon = dna_sequence[i:i+3]
            codon_counts[codon] = codon_counts.get(codon, 0) + 1
            
        # Calculate codon diversity
        codon_diversity = len(codon_counts) / len(self.dna_codons)
        
        return {
            "base_ratios": base_ratios,
            "gc_content": gc_content,
            "phi_resonance": phi_resonance,
            "codon_diversity": codon_diversity,
            "codon_counts": codon_counts
        }
        
    def store_quantum_state(self, quantum_state, metadata=None):
        """Store quantum state in memory DNA"""
        # Convert to DNA
        dna_sequence = self.state_to_dna(quantum_state)
        
        # Extract features
        features = self.dna_to_features(dna_sequence)
        
        # Create memory entry
        entry = {
            "timestamp": str(datetime.now()),
            "dna_sequence": dna_sequence,
            "features": features,
            "metadata": metadata or {},
            "state_snapshot": quantum_state[:64].tolist()  # Store compact representation
        }
        
        # Add to memory
        self.quantum_memory.append(entry)
        
        # Update phi-resonant indices
        phi_key = round(features["phi_resonance"] * 1000)
        if phi_key not in self.phi_indices:
            self.phi_indices[phi_key] = []
        self.phi_indices[phi_key].append(len(self.quantum_memory) - 1)
        
        # Save memory periodically
        if len(self.quantum_memory) % 10 == 0:
            self._save_memory()
            
        return entry
        
    def find_similar_states(self, quantum_state, top_n=5):
        """Find similar quantum states in memory"""
        if not self.quantum_memory:
            return []
            
        # Convert query state to DNA and features
        query_dna = self.state_to_dna(quantum_state)
        query_features = self.dna_to_features(query_dna)
        
        # Find states with similar phi-resonance
        phi_key = round(query_features["phi_resonance"] * 1000)
        candidate_indices = []
        
        # Search nearby phi-resonance values
        for k in range(phi_key-5, phi_key+6):
            if k in self.phi_indices:
                candidate_indices.extend(self.phi_indices[k])
                
        # If no candidates found, use all memory
        if not candidate_indices:
            candidate_indices = list(range(len(self.quantum_memory)))
            
        # Calculate similarity scores
        similarities = []
        for idx in candidate_indices:
            entry = self.quantum_memory[idx]
            
            # Calculate feature similarity
            gc_sim = 1 - abs(entry["features"]["gc_content"] - query_features["gc_content"])
            phi_sim = 1 - abs(entry["features"]["phi_resonance"] - query_features["phi_resonance"])
            div_sim = 1 - abs(entry["features"]["codon_diversity"] - query_features["codon_diversity"])
            
            # Calculate state vector similarity if available
            state_sim = 0
            if "state_snapshot" in entry:
                stored_state = np.array(entry["state_snapshot"])
                query_snapshot = quantum_state[:len(stored_state)]
                # Use cosine similarity
                state_sim = 1 - cosine(np.abs(stored_state), np.abs(query_snapshot))
                
            # Combined similarity score with φ-weighted components
            combined_sim = (
                state_sim * self.phi**2 +
                phi_sim * self.phi +
                gc_sim +
                div_sim / self.phi
            ) / (self.phi**2 + self.phi + 1 + 1/self.phi)
            
            similarities.append((idx, combined_sim))
            
        # Sort by similarity (descending)
        similarities.sort(key=lambda x: x[1], reverse=True)
        
        # Return top matches
        top_matches = []
        for idx, sim in similarities[:top_n]:
            entry = self.quantum_memory[idx]
            match = {
                "similarity": sim,
                "timestamp": entry["timestamp"],
                "phi_resonance": entry["features"]["phi_resonance"],
                "metadata": entry["metadata"]
            }
            top_matches.append(match)
            
        return top_matches
        
    def recognize_patterns(self, min_entries=10):
        """Recognize patterns in quantum memory DNA"""
        if len(self.quantum_memory) < min_entries:
            print(f"⚠️ Not enough memory entries for pattern recognition. Need {min_entries}, have {len(self.quantum_memory)}")
            return {}
            
        # Extract features from all memories
        gc_contents = [entry["features"]["gc_content"] for entry in self.quantum_memory]
        phi_resonances = [entry["features"]["phi_resonance"] for entry in self.quantum_memory]
        
        # Find clusters in phi-resonance values
        phi_clusters = {}
        for i, phi_res in enumerate(phi_resonances):
            cluster_key = round(phi_res * 10) / 10  # Round to nearest 0.1
            if cluster_key not in phi_clusters:
                phi_clusters[cluster_key] = []
            phi_clusters[cluster_key].append(i)
            
        # Analyze clusters
        patterns = {}
        for cluster_val, indices in phi_clusters.items():
            if len(indices) >= 3:  # Need at least 3 entries to form a pattern
                # Calculate cluster statistics
                cluster_entries = [self.quantum_memory[i] for i in indices]
                avg_gc = np.mean([entry["features"]["gc_content"] for entry in cluster_entries])
                avg_diversity = np.mean([entry["features"]["codon_diversity"] for entry in cluster_entries])
                
                # Create pattern signature
                pattern_id = f"pattern_{cluster_val:.1f}"
                patterns[pattern_id] = {
                    "phi_resonance": cluster_val,
                    "count": len(indices),
                    "avg_gc_content": avg_gc,
                    "avg_codon_diversity": avg_diversity,
                    "indices": indices,
                    "phi_harmonic": abs(1/cluster_val - self.phi) < 0.1
                }
                
        # Store recognized patterns
        self.pattern_signatures = patterns
        return patterns
        
    def visualize_memory_landscape(self):
        """Visualize the quantum memory DNA landscape"""
        if not self.quantum_memory:
            print("⚠️ No memory entries to visualize")
            return None
            
        # Extract features for visualization
        gc_contents = [entry["features"]["gc_content"] for entry in self.quantum_memory]
        phi_resonances = [entry["features"]["phi_resonance"] for entry in self.quantum_memory]
        codon_diversities = [entry["features"]["codon_diversity"] for entry in self.quantum_memory]
        
        # Create visualization
        plt.figure(figsize=(15, 10))
        
        # Plot GC content vs phi-resonance
        plt.subplot(2, 2, 1)
        plt.scatter(gc_contents, phi_resonances, alpha=0.7)
        plt.axhline(y=1/self.phi, color='r', linestyle='--', label=f'1/φ = {1/self.phi:.3f}')
        plt.title('GC Content vs φ-Resonance')
        plt.xlabel('GC Content')
        plt.ylabel('φ-Resonance')
        plt.grid(True)
        plt.legend()
        
        # Plot memory growth over time
        plt.subplot(2, 2, 2)
        timestamps = [datetime.fromisoformat(entry["timestamp"]) for entry in self.quantum_memory]
        indices = list(range(len(timestamps)))
        plt.plot(indices, timestamps, 'b-')
        plt.title('Memory Growth Over Time')
        plt.xlabel('Memory Entry Index')
        plt.ylabel('Timestamp')
        plt.grid(True)
        
        # Plot codon diversity vs phi-resonance
        plt.subplot(2, 2, 3)
        plt.scatter(codon_diversities, phi_resonances, alpha=0.7)
        plt.axhline(y=1/self.phi, color='r', linestyle='--', label=f'1/φ = {1/self.phi:.3f}')
        plt.title('Codon Diversity vs φ-Resonance')
        plt.xlabel('Codon Diversity')
        plt.ylabel('φ-Resonance')
        plt.grid(True)
        plt.legend()
        
        # Plot pattern distribution if available
        if self.pattern_signatures:
            plt.subplot(2, 2, 4)
            pattern_values = [p["phi_resonance"] for p in self.pattern_signatures.values()]
            pattern_counts = [p["count"] for p in self.pattern_signatures.values()]
            plt.bar(pattern_values, pattern_counts)
            plt.title('Pattern Distribution')
            plt.xlabel('φ-Resonance Cluster')
            plt.ylabel('Count')
            plt.grid(True)
        
        plt.tight_layout()
        
        # Save visualization
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = self.memory_dir / f"memory_landscape_{timestamp}.png"
        plt.savefig(filename)
        plt.close()
        
        return str(filename)
        
    def generate_memory_report(self):
        """Generate a report on quantum memory DNA"""
        if not self.quantum_memory:
            return "No quantum memory DNA entries available"
            
        # Recognize patterns if not already done
        if not self.pattern_signatures:
            self.recognize_patterns()
            
        # Generate report
        report = f"\n🧬 Quantum Memory DNA Report\n"
        report += f"=" * 50 + "\n"
        report += f"Total Memory Entries: {len(self.quantum_memory)}\n"
        report += f"Memory Size: {sys.getsizeof(self.quantum_memory) / 1024:.2f} KB\n"
        report += f"First Entry: {self.quantum_memory[0]['timestamp']}\n"
        report += f"Latest Entry: {self.quantum_memory[-1]['timestamp']}\n\n"
        
        # Pattern statistics
        if self.pattern_signatures:
            report += f"Recognized Patterns: {len(self.pattern_signatures)}\n"
            phi_harmonic_patterns = sum(1 for p in self.pattern_signatures.values() if p["phi_harmonic"])
            report += f"φ-Harmonic Patterns: {phi_harmonic_patterns}\n\n"
            
            # Top patterns by count
            top_patterns = sorted(self.pattern_signatures.items(), 
                                 key=lambda x: x[1]["count"], 
                                 reverse=True)[:3]
            report += "Top Patterns:\n"
            for pattern_id, pattern in top_patterns:
                report += f"  - {pattern_id}: φ-resonance={pattern['phi_resonance']:.3f}, count={pattern['count']}\n"
        else:
            report += "No patterns recognized yet\n"
            
        return report

def main():
    """Test the quantum phi-memory DNA"""
    memory = QuantumPhiMemoryDNA()
    
    # Generate test quantum states
    print("\n🧪 Testing Quantum Phi-Memory DNA")
    print("=" * 50)
    
    # Store some test states
    for i in range(5):
        n = 1024
        # Create state with varying phi-resonance
        state = np.zeros(n, dtype=complex)
        phi_index = int(n / memory.phi) + i*10
        state[phi_index] = 1.0
        state = state / np.linalg.norm(state)
        
        # Add some noise
        noise = np.random.normal(0, 0.1, n) + 1j * np.random.normal(0, 0.1, n)
        state = state + noise
        state = state / np.linalg.norm(state)
        
        # Store in memory
        metadata = {"test_index": i, "phi_index": phi_index}
        entry = memory.store_quantum_state(state, metadata)
        print(f"Stored state {i+1}: φ-resonance = {entry['features']['phi_resonance']:.4f}")
    
    # Find similar states
    test_state = np.zeros(1024, dtype=complex)
    test_phi_index = int(1024 / memory.phi) + 20
    test_state[test_phi_index] = 1.0
    test_state = test_state / np.linalg.norm(test_state)
    
    similar_states = memory.find_similar_states(test_state, top_n=3)
    print("\n🔍 Similar States:")
    for i, state in enumerate(similar_states):
        print(f"  {i+1}. Similarity: {state['similarity']:.4f}, φ-resonance: {state['phi_resonance']:.4f}")
    
    # Recognize patterns
    patterns = memory.recognize_patterns(min_entries=5)
    print(f"\n🧩 Recognized {len(patterns)} patterns")
    
    # Visualize memory landscape
    viz_file = memory.visualize_memory_landscape()
    print(f"\n📊 Memory landscape visualization saved to: {viz_file}")
    
    # Generate report
    report = memory.generate_memory_report()
    print(report)
    
if __name__ == "__main__":
    main()

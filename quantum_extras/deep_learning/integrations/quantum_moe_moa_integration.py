import os
import sys
from pathlib import Path
import numpy as np
import json
from datetime import datetime

# Add the project root to Python path
project_root = str(Path(__file__).parent.parent.parent)
if project_root not in sys.path:
    sys.path.append(project_root)

# Import the QuantumMoEMoA class
from deep_learning.quantum_moe_moa import QuantumMoEMoA

# Import the mock QuantumAI for testing
from mock_dependencies import QuantumAI

class QuantumMoEMoAIntegration:
    """
    Integration class for the QuantumMoEMoA model with the main Quantum AI system.
    This class provides methods for processing queries, generating visualizations,
    and evaluating the model in the context of the Quantum AI system.
    """
    
    def __init__(self, model_path=None):
        """Initialize the integration module"""
        self.quantum_moe_moa = QuantumMoEMoA()
        if model_path:
            self.quantum_moe_moa.load_model(model_path)
            
        # Initialize the main Quantum AI system
        self.quantum_ai = QuantumAI()
        
        # Setup logging
        self.setup_logging()
        
    def setup_logging(self):
        """Setup logging directory"""
        self.log_dir = os.path.join(project_root, "deep_learning", "logs")
        os.makedirs(self.log_dir, exist_ok=True)
        self.log_file = os.path.join(self.log_dir, f"integration_log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json")
        self.logs = []
        
    def log_event(self, event_type, data):
        """Log an event"""
        event = {
            "timestamp": datetime.now().isoformat(),
            "event_type": event_type,
            "data": data
        }
        self.logs.append(event)
        
        # Write to log file
        with open(self.log_file, 'w') as f:
            json.dump(self.logs, f, indent=2)
            
    def process_query(self, query, brain_type="Standard"):
        """Process a user query through both systems and combine results"""
        self.log_event("query_received", {"query": query, "brain_type": brain_type})
        
        # Process through main Quantum AI
        quantum_ai_result = self.quantum_ai.process_query(query, brain_type)
        
        # Extract quantum state from result
        quantum_state = quantum_ai_result.get("processed_state", None)
        if quantum_state is None:
            # Generate a random quantum state if not provided
            quantum_state = np.random.rand(8)
            quantum_state = quantum_state / np.sum(quantum_state)  # Normalize
            
        # Process through QuantumMoEMoA
        moe_moa_result = self.quantum_moe_moa.process_quantum_data(quantum_state)
        
        # Combine results
        combined_result = {
            "query": query,
            "brain_type": brain_type,
            "quantum_ai_result": quantum_ai_result,
            "moe_moa_result": moe_moa_result,
            "combined_metrics": self._combine_metrics(quantum_ai_result, moe_moa_result)
        }
        
        self.log_event("query_processed", combined_result)
        return combined_result
    
    def _combine_metrics(self, quantum_ai_result, moe_moa_result):
        """Combine metrics from both systems"""
        # Extract metrics from quantum AI result
        quantum_metrics = quantum_ai_result.get("metrics", {})
        
        # Extract metrics from MoE/MoA result
        moe_metrics = {
            "expert_utilization": moe_moa_result.get("expert_utilization", []),
            "temperature": moe_moa_result.get("temperature", 0)
        }
        
        # Combine metrics
        combined_metrics = {
            "quantum_coherence": quantum_metrics.get("coherence", 0),
            "expert_utilization": np.mean(moe_metrics["expert_utilization"]) if moe_metrics["expert_utilization"] else 0,
            "temperature": moe_metrics["temperature"],
            "combined_score": 0  # Placeholder for a combined score
        }
        
        # Calculate combined score
        if "coherence" in quantum_metrics and moe_metrics["expert_utilization"]:
            combined_metrics["combined_score"] = (
                quantum_metrics["coherence"] * 0.5 + 
                np.mean(moe_metrics["expert_utilization"]) * 0.5
            )
            
        return combined_metrics
    
    def generate_enhanced_visualization(self, query, output_path=None):
        """Generate enhanced visualization combining both systems"""
        if output_path is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            output_path = os.path.join(project_root, "deep_learning", "visualizations", f"enhanced_viz_{timestamp}.txt")
            
        # Process query
        result = self.process_query(query)
        
        # Generate visualization text
        viz_text = [
            f"Enhanced Quantum Visualization for: {query}",
            f"=======================================",
            f"Timestamp: {datetime.now().isoformat()}",
            f"",
            f"Quantum AI Metrics:",
            f"  Coherence: {result['quantum_ai_result'].get('metrics', {}).get('coherence', 'N/A')}",
            f"  Stability: {result['quantum_ai_result'].get('metrics', {}).get('stability', 'N/A')}",
            f"  Entanglement: {result['quantum_ai_result'].get('metrics', {}).get('entanglement', 'N/A')}",
            f"",
            f"MoE/MoA Metrics:",
            f"  Expert Utilization: {np.mean(result['moe_moa_result'].get('expert_utilization', [0]))}",
            f"  Temperature: {result['moe_moa_result'].get('temperature', 'N/A')}",
            f"",
            f"Combined Score: {result['combined_metrics'].get('combined_score', 'N/A')}",
            f"=======================================",
        ]
        
        # Save visualization
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        with open(output_path, 'w') as f:
            f.write('\n'.join(viz_text))
            
        self.log_event("visualization_generated", {"query": query, "output_path": output_path})
        return output_path
    
    def run_benchmark(self, num_queries=10):
        """Run a benchmark with random queries"""
        print(f"Running benchmark with {num_queries} random queries...")
        
        # Generate random queries
        sample_queries = [
            "What is quantum entanglement?",
            "How do quantum computers work?",
            "Explain quantum superposition",
            "What is Shor's algorithm?",
            "How does quantum teleportation work?",
            "What are qubits?",
            "Explain quantum error correction",
            "What is quantum supremacy?",
            "How does quantum tunneling work?",
            "What is the uncertainty principle?"
        ]
        
        # Select queries for benchmark
        if num_queries <= len(sample_queries):
            benchmark_queries = sample_queries[:num_queries]
        else:
            # Repeat queries if needed
            benchmark_queries = sample_queries * (num_queries // len(sample_queries) + 1)
            benchmark_queries = benchmark_queries[:num_queries]
            
        # Run benchmark
        results = []
        start_time = datetime.now()
        
        for i, query in enumerate(benchmark_queries):
            print(f"Processing query {i+1}/{num_queries}: {query}")
            result = self.process_query(query)
            results.append({
                "query": query,
                "combined_score": result["combined_metrics"]["combined_score"]
            })
            
        end_time = datetime.now()
        duration = (end_time - start_time).total_seconds()
        
        # Compute benchmark metrics
        benchmark_results = {
            "num_queries": num_queries,
            "total_duration_seconds": duration,
            "avg_time_per_query": duration / num_queries,
            "avg_combined_score": np.mean([r["combined_score"] for r in results]),
            "results": results
        }
        
        # Save benchmark results
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        benchmark_path = os.path.join(self.log_dir, f"benchmark_{timestamp}.json")
        with open(benchmark_path, 'w') as f:
            json.dump(benchmark_results, f, indent=2)
            
        self.log_event("benchmark_completed", benchmark_results)
        print(f"Benchmark completed in {duration:.2f} seconds. Results saved to {benchmark_path}")
        return benchmark_results

# Example usage
if __name__ == "__main__":
    # Initialize integration
    integration = QuantumMoEMoAIntegration()
    
    # Process a sample query
    sample_query = "Explain how quantum entanglement works in simple terms"
    print(f"Processing sample query: {sample_query}")
    result = integration.process_query(sample_query)
    print(f"Combined score: {result['combined_metrics']['combined_score']}")
    
    # Generate visualization
    print("Generating enhanced visualization...")
    viz_path = integration.generate_enhanced_visualization(sample_query)
    print(f"Visualization saved to: {viz_path}")
    
    # Run a small benchmark
    print("Running benchmark...")
    benchmark_results = integration.run_benchmark(num_queries=3)
    print(f"Benchmark average score: {benchmark_results['avg_combined_score']}")

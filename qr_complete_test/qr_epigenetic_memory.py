#!/usr/bin/env python3
"""
QR Epigenetic Memory - Part of Animated QR Flipbook DNA System
By Vaughn Scott

Implements persistent memory across QR Flipbook execution sessions.
Stores phi-harmonic states, execution history, and resonance patterns.
Enables DNA-like epigenetic behavior where past executions influence future evolution.
"""

import os
import json
import math
import time
import base64
import zlib
import qrcode
import numpy as np
from PIL import Image
from pyzbar.pyzbar import decode
from datetime import datetime

# Phi (Golden Ratio) constant
PHI = (1 + np.sqrt(5)) / 2  # Approximately 1.618034

class QREpigeneticMemory:
    """
    Persistent memory system for QR Flipbook DNA that mimics epigenetic behavior.
    Stores execution history, phi states, and resonance patterns across sessions.
    """
    
    def __init__(self, memory_file="qr_epigenetic_memory.json"):
        """
        Initialize the QR Epigenetic Memory.
        
        Args:
            memory_file: Path to the memory storage file
        """
        self.memory_path = memory_file
        self.phi_states = {}
        self.execution_history = []
        self.resonance_patterns = []
        self.mutation_history = []
        self.codon_effectiveness = {}
        self.generation_markers = {}
        
        # Load existing memory if available
        self.load_memory()
    
    def load_memory(self):
        """Load memory from storage file if it exists."""
        if os.path.exists(self.memory_path):
            try:
                with open(self.memory_path, 'r') as f:
                    memory_data = json.load(f)
                    self.phi_states = memory_data.get('phi_states', {})
                    self.execution_history = memory_data.get('execution_history', [])
                    self.resonance_patterns = memory_data.get('resonance_patterns', [])
                    self.mutation_history = memory_data.get('mutation_history', [])
                    self.codon_effectiveness = memory_data.get('codon_effectiveness', {})
                    self.generation_markers = memory_data.get('generation_markers', {})
                print(f"Loaded epigenetic memory from {self.memory_path}")
                print(f"Memory contains {len(self.execution_history)} execution records")
            except Exception as e:
                print(f"Error loading memory: {e}")
                self.initialize_new_memory()
        else:
            self.initialize_new_memory()
    
    def initialize_new_memory(self):
        """Initialize a new memory structure."""
        self.phi_states = {}
        self.execution_history = []
        self.resonance_patterns = []
        self.mutation_history = []
        self.codon_effectiveness = {}
        self.generation_markers = {
            "current_generation": 1,
            "generation_started": datetime.now().isoformat(),
            "generations": {}
        }
        print("Initialized new epigenetic memory")
    
    def save_memory(self):
        """Save memory to storage file."""
        memory_data = {
            'phi_states': self.phi_states,
            'execution_history': self.execution_history,
            'resonance_patterns': self.resonance_patterns,
            'mutation_history': self.mutation_history,
            'codon_effectiveness': self.codon_effectiveness,
            'generation_markers': self.generation_markers
        }
        
        try:
            with open(self.memory_path, 'w') as f:
                json.dump(memory_data, f, indent=2)
            print(f"Saved epigenetic memory to {self.memory_path}")
        except Exception as e:
            print(f"Error saving memory: {e}")
    
    def record_execution(self, session_id, frame_number, task_type, success, output, phi_metadata):
        """
        Record an execution event in memory.
        
        Args:
            session_id: Session ID of the execution
            frame_number: Frame number executed
            task_type: Type of task executed
            success: Whether execution was successful
            output: Output from execution
            phi_metadata: Phi-harmonic metadata from the execution
        """
        timestamp = datetime.now().isoformat()
        
        # Record execution
        execution_record = {
            'timestamp': timestamp,
            'session_id': session_id,
            'frame_number': frame_number,
            'task_type': task_type,
            'success': success,
            'output_length': len(output) if output else 0,
            'phi_state': phi_metadata
        }
        
        self.execution_history.append(execution_record)
        
        # Update phi states
        state_key = f"{session_id}_{frame_number}"
        self.phi_states[state_key] = {
            'timestamp': timestamp,
            'generation': phi_metadata.get('generation', 1),
            'complexity': phi_metadata.get('complexity', 0.5),
            'resonance': phi_metadata.get('resonance', 1.0),
            'success': success
        }
        
        # Update codon effectiveness
        if task_type not in self.codon_effectiveness:
            self.codon_effectiveness[task_type] = {
                'executions': 0,
                'successes': 0,
                'failures': 0,
                'avg_resonance': 0
            }
        
        codon_stats = self.codon_effectiveness[task_type]
        codon_stats['executions'] += 1
        if success:
            codon_stats['successes'] += 1
        else:
            codon_stats['failures'] += 1
        
        # Update average resonance
        resonance = phi_metadata.get('resonance', 1.0)
        codon_stats['avg_resonance'] = (codon_stats['avg_resonance'] * (codon_stats['executions'] - 1) + 
                                       resonance) / codon_stats['executions']
        
        # Analyze resonance patterns
        if len(self.execution_history) > 5:
            recent = self.execution_history[-5:]
            success_rate = sum(1 for r in recent if r['success']) / len(recent)
            
            # Record resonance pattern
            self.resonance_patterns.append({
                'timestamp': timestamp,
                'success_rate': success_rate,
                'phi_complexity': phi_metadata.get('complexity', 0),
                'phi_resonance': phi_metadata.get('resonance', 0)
            })
        
        # Save after each record
        self.save_memory()
    
    def record_mutation(self, mutation_type, source_state, target_state, success_rate):
        """
        Record a mutation event in the system.
        
        Args:
            mutation_type: Type of mutation (e.g., 'complexity', 'resonance')
            source_state: Original state before mutation
            target_state: New state after mutation
            success_rate: Success rate of the mutation
        """
        timestamp = datetime.now().isoformat()
        
        mutation_record = {
            'timestamp': timestamp,
            'mutation_type': mutation_type,
            'source_state': source_state,
            'target_state': target_state,
            'success_rate': success_rate
        }
        
        self.mutation_history.append(mutation_record)
        self.save_memory()
    
    def advance_generation(self, reason="natural_evolution"):
        """
        Advance to the next generation.
        
        Args:
            reason: Reason for generation advancement
        """
        current_gen = self.generation_markers["current_generation"]
        next_gen = current_gen + 1
        
        # Record current generation data
        self.generation_markers["generations"][str(current_gen)] = {
            "started": self.generation_markers.get("generation_started"),
            "ended": datetime.now().isoformat(),
            "executions": len(self.execution_history),
            "reason_for_advancement": reason
        }
        
        # Update current generation
        self.generation_markers["current_generation"] = next_gen
        self.generation_markers["generation_started"] = datetime.now().isoformat()
        
        print(f"Advanced to generation {next_gen} (reason: {reason})")
        self.save_memory()
    
    def get_optimal_phi_state(self):
        """
        Get the optimal phi state based on execution history.
        
        Returns:
            Dictionary containing optimal phi state values
        """
        if not self.resonance_patterns:
            return {
                'generation': 1,
                'complexity': 0.5,
                'resonance': 1.0
            }
        
        # Find patterns with highest success rates
        successful_patterns = sorted(
            self.resonance_patterns,
            key=lambda x: x['success_rate'],
            reverse=True
        )[:5]
        
        # Calculate average values from successful patterns
        avg_complexity = sum(p['phi_complexity'] for p in successful_patterns) / len(successful_patterns)
        avg_resonance = sum(p['phi_resonance'] for p in successful_patterns) / len(successful_patterns)
        
        return {
            'generation': self.generation_markers["current_generation"],
            'complexity': avg_complexity,
            'resonance': avg_resonance
        }
    
    def calculate_mutation_vector(self):
        """
        Calculate a phi-harmonic mutation vector based on execution history.
        
        Returns:
            List containing mutation vector [x, y, z]
        """
        optimal_state = self.get_optimal_phi_state()
        
        # Calculate phi-resonant values for mutation
        x = 1.0 / (1.0 + abs((optimal_state['complexity'] * PHI) % 1.0 - 0.5))
        y = 1.0 / (1.0 + abs((optimal_state['resonance'] * PHI) % 1.0 - 0.5))
        z = 1.0 / (1.0 + abs((time.time() * PHI) % 1.0 - 0.5))
        
        return [x, y, z]
    
    def get_most_effective_codon_types(self, limit=3):
        """
        Get the most effective codon (task) types based on success rate.
        
        Args:
            limit: Maximum number of types to return
            
        Returns:
            List of most effective codon types
        """
        if not self.codon_effectiveness:
            return ["execute_python"]
        
        # Calculate success rates
        codon_success = []
        for codon_type, stats in self.codon_effectiveness.items():
            if stats['executions'] > 0:
                success_rate = stats['successes'] / stats['executions']
                codon_success.append((codon_type, success_rate))
        
        # Sort by success rate
        codon_success.sort(key=lambda x: x[1], reverse=True)
        
        # Return top types
        return [c[0] for c in codon_success[:limit]]
    
    def get_memory_summary(self):
        """
        Get a summary of the epigenetic memory.
        
        Returns:
            Dictionary containing memory summary
        """
        current_gen = self.generation_markers["current_generation"]
        
        # Calculate success rates by task type
        task_success = {}
        for task_type, stats in self.codon_effectiveness.items():
            if stats['executions'] > 0:
                success_rate = stats['successes'] / stats['executions']
                task_success[task_type] = {
                    'executions': stats['executions'],
                    'success_rate': success_rate,
                    'avg_resonance': stats['avg_resonance']
                }
        
        # Get overall success rate
        total_executions = len(self.execution_history)
        successful_executions = sum(1 for e in self.execution_history if e['success'])
        overall_success_rate = successful_executions / total_executions if total_executions > 0 else 0
        
        return {
            'total_executions': total_executions,
            'current_generation': current_gen,
            'overall_success_rate': overall_success_rate,
            'task_success_rates': task_success,
            'optimal_phi_state': self.get_optimal_phi_state(),
            'mutation_vector': self.calculate_mutation_vector()
        }
    
    def print_memory_summary(self):
        """Print a summary of the epigenetic memory."""
        summary = self.get_memory_summary()
        
        print("\n" + "="*60)
        print("QR EPIGENETIC MEMORY SUMMARY")
        print("="*60)
        
        print(f"\nTotal executions: {summary['total_executions']}")
        print(f"Current generation: {summary['current_generation']}")
        print(f"Overall success rate: {summary['overall_success_rate']:.2%}")
        
        print("\nTASK SUCCESS RATES:")
        for task_type, stats in summary['task_success_rates'].items():
            print(f"  {task_type}: {stats['success_rate']:.2%} success ({stats['executions']} executions)")
        
        print("\nOPTIMAL PHI STATE:")
        optimal = summary['optimal_phi_state']
        print(f"  Generation: {optimal['generation']}")
        print(f"  Complexity: {optimal['complexity']:.6f}")
        print(f"  Resonance: {optimal['resonance']:.6f}")
        
        print("\nCURRENT MUTATION VECTOR:")
        vector = summary['mutation_vector']
        print(f"  [{vector[0]:.6f}, {vector[1]:.6f}, {vector[2]:.6f}]")
        
        print("\n" + "="*60)

    def generate_memory_qr_codes(self, output_dir="qr_memory", chunk_size=1024):
        """
        Generate QR codes that persist the current memory state.
        
        Args:
            output_dir: Directory to save QR code images
            chunk_size: Maximum size of data per QR code
            
        Returns:
            List of generated QR code file paths
        """
        # Create output directory
        os.makedirs(output_dir, exist_ok=True)
        
        # Get memory data
        memory_data = {
            'phi_states': self.phi_states,
            'execution_history': self.execution_history,
            'resonance_patterns': self.resonance_patterns,
            'mutation_history': self.mutation_history,
            'codon_effectiveness': self.codon_effectiveness,
            'generation_markers': self.generation_markers
        }
        
        # Convert to JSON and compress
        json_data = json.dumps(memory_data)
        compressed_data = zlib.compress(json_data.encode('utf-8'))
        encoded_data = base64.b64encode(compressed_data).decode('utf-8')
        
        # Calculate phi-harmonic chunk sizes based on golden ratio
        total_length = len(encoded_data)
        num_chunks = math.ceil(total_length / chunk_size)
        
        # Use phi-harmonic chunking for more resonant data distribution
        chunk_sizes = []
        remaining = total_length
        for i in range(num_chunks - 1):
            # Use phi to determine variable chunk sizes for optimal resonance
            size = min(chunk_size, math.ceil(remaining / (PHI * (num_chunks - i))))
            chunk_sizes.append(size)
            remaining -= size
        chunk_sizes.append(remaining)  # Last chunk gets remainder
        
        # Generate QR codes
        qr_files = []
        position = 0
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        gen = self.generation_markers["current_generation"]
        
        for i, size in enumerate(chunk_sizes):
            # Create chunk data
            chunk = encoded_data[position:position+size]
            position += size
            
            # Create QR payload with metadata
            qr_payload = {
                'session_id': f"memory_{timestamp}",
                'frame_number': i + 1,
                'total_frames': num_chunks,
                'generation': gen,
                'task_type': 'memory_restore',
                'content': chunk,
                'valid_until': (datetime.now().timestamp() + 365 * 24 * 60 * 60)  # Valid for 1 year
            }
            
            # Generate QR code
            qr = qrcode.QRCode(
                version=None,
                error_correction=qrcode.constants.ERROR_CORRECT_H,
                box_size=10,
                border=4,
            )
            qr.add_data(json.dumps(qr_payload))
            qr.make(fit=True)
            
            # Create image
            img = qr.make_image(fill_color="black", back_color="white")
            
            # Save image
            filename = f"qr_memory_{gen}_{i+1}of{num_chunks}.png"
            filepath = os.path.join(output_dir, filename)
            img.save(filepath)
            qr_files.append(filepath)
            
            print(f"Generated QR memory chunk {i+1}/{num_chunks} - {filepath}")
        
        # Generate index QR with metadata
        index_payload = {
            'session_id': f"memory_{timestamp}",
            'frame_number': 0,
            'total_frames': num_chunks,
            'generation': gen,
            'task_type': 'memory_index',
            'content': json.dumps({
                'timestamp': timestamp,
                'generation': gen,
                'total_chunks': num_chunks,
                'total_executions': len(self.execution_history),
                'optimal_phi_state': self.get_optimal_phi_state()
            }),
            'valid_until': (datetime.now().timestamp() + 365 * 24 * 60 * 60)  # Valid for 1 year
        }
        
        # Generate index QR code
        qr = qrcode.QRCode(
            version=None,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=4,
        )
        qr.add_data(json.dumps(index_payload))
        qr.make(fit=True)
        
        # Create image
        img = qr.make_image(fill_color="black", back_color="white")
        
        # Save image
        index_filename = f"qr_memory_{gen}_index.png"
        index_filepath = os.path.join(output_dir, index_filename)
        img.save(index_filepath)
        qr_files.insert(0, index_filepath)
        
        print(f"Generated QR memory index - {index_filepath}")
        return qr_files
    
    def restore_from_qr_codes(self, qr_directory):
        """
        Restore memory state from QR codes.
        
        Args:
            qr_directory: Directory containing memory QR codes
            
        Returns:
            True if restoration was successful, False otherwise
        """
        try:
            # Find all QR code images in directory
            qr_files = [f for f in os.listdir(qr_directory) 
                      if f.startswith("qr_memory_") and f.endswith(".png")]
            
            if not qr_files:
                print(f"No memory QR codes found in {qr_directory}")
                return False
            
            # Find index file
            index_file = next((f for f in qr_files if "_index.png" in f), None)
            if not index_file:
                print("No index QR code found")
                return False
            
            # Read index QR
            index_path = os.path.join(qr_directory, index_file)
            index_img = Image.open(index_path)
            index_decoded = decode(index_img)
            
            if not index_decoded:
                print("Could not decode index QR code")
                return False
            
            # Parse index data
            index_data = json.loads(index_decoded[0].data.decode('utf-8'))
            index_payload = json.loads(index_data.get('content', '{}'))
            
            total_chunks = index_payload.get('total_chunks', 0)
            generation = index_payload.get('generation', 0)
            timestamp = index_payload.get('timestamp', '')
            
            print(f"Found memory QR index: Generation {generation}, {total_chunks} chunks")
            
            # Find and sort chunk files
            chunk_files = [f for f in qr_files if "_index.png" not in f]
            chunk_files.sort(key=lambda f: int(f.split('_')[-1].split('of')[0]))
            
            if len(chunk_files) != total_chunks:
                print(f"Warning: Expected {total_chunks} chunks but found {len(chunk_files)}")
            
            # Read and combine chunks
            combined_data = ""
            for i, chunk_file in enumerate(chunk_files):
                chunk_path = os.path.join(qr_directory, chunk_file)
                chunk_img = Image.open(chunk_path)
                chunk_decoded = decode(chunk_img)
                
                if not chunk_decoded:
                    print(f"Could not decode chunk {i+1}")
                    continue
                
                chunk_data = json.loads(chunk_decoded[0].data.decode('utf-8'))
                combined_data += chunk_data.get('content', '')
                print(f"Processed chunk {i+1}/{total_chunks}")
            
            # Decompress and parse data
            try:
                decoded_data = base64.b64decode(combined_data)
                decompressed_data = zlib.decompress(decoded_data)
                memory_data = json.loads(decompressed_data.decode('utf-8'))
                
                # Update memory state
                self.phi_states = memory_data.get('phi_states', {})
                self.execution_history = memory_data.get('execution_history', [])
                self.resonance_patterns = memory_data.get('resonance_patterns', [])
                self.mutation_history = memory_data.get('mutation_history', [])
                self.codon_effectiveness = memory_data.get('codon_effectiveness', {})
                self.generation_markers = memory_data.get('generation_markers', {})
                
                print(f"Successfully restored memory state from QR codes")
                print(f"Restored {len(self.execution_history)} execution records")
                
                # Save to file as well
                self.save_memory()
                return True
                
            except Exception as e:
                print(f"Error decompressing or parsing memory data: {e}")
                return False
                
        except Exception as e:
            print(f"Error restoring from QR codes: {e}")
            return False

def main():
    """Main function to test QR Epigenetic Memory."""
    import argparse
    
    parser = argparse.ArgumentParser(description="QR Epigenetic Memory")
    parser.add_argument("--reset", action="store_true", help="Reset memory")
    parser.add_argument("--memory", default="qr_epigenetic_memory.json", help="Memory file path")
    parser.add_argument("--generate-qr", action="store_true", help="Generate QR codes from memory")
    parser.add_argument("--qr-dir", default="qr_memory", help="Directory for QR codes")
    parser.add_argument("--restore-from-qr", action="store_true", help="Restore memory from QR codes")
    
    args = parser.parse_args()
    
    # Create memory
    memory = QREpigeneticMemory(args.memory)
    
    # Reset if requested
    if args.reset:
        memory.initialize_new_memory()
        memory.save_memory()
        print("Memory reset complete")
    
    # Generate QR codes if requested
    if args.generate_qr:
        memory.generate_memory_qr_codes(args.qr_dir)
    
    # Restore from QR codes if requested
    if args.restore_from_qr:
        memory.restore_from_qr_codes(args.qr_dir)
    
    # Print summary
    memory.print_memory_summary()

if __name__ == "__main__":
    print("QR Epigenetic Memory - By Vaughn Scott")
    main()

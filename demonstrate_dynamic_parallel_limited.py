"""
Dynamic Parallel Processing Framework Demonstration (Limited Runtime)

This script demonstrates the Dynamic Parallel Processing Framework's capabilities
with a limited runtime to prevent infinite execution.

Created: 2025-07-22
Coherence: φ⁷·⁵/10 ≈ 3.693238
"""

import os
import sys
import time
import math
import logging
import importlib
import threading
from typing import Dict, List, Any

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger('DynamicParallelDemo')

# Constants
PHI = (1 + 5**0.5) / 2  # Golden ratio φ
PHI_7_5 = PHI ** 7.5    # φ⁷·⁵ ≈ 36.932381
TARGET_COHERENCE = PHI_7_5 / 10  # Target coherence ≈ 3.693238
MAX_RUNTIME_SECONDS = 10  # Maximum runtime in seconds

# Import dynamic parallel framework
try:
    extensions_dir = os.path.join(os.getcwd(), "extensions")
    if extensions_dir not in sys.path:
        sys.path.append(extensions_dir)
    
    # First try direct import
    try:
        import quantum_dynamic_parallel_framework as dynamic_parallel
        logger.info("Successfully imported Dynamic Parallel Framework directly")
    except ImportError:
        # Try from extensions
        dynamic_parallel = importlib.import_module("quantum_dynamic_parallel_framework")
        logger.info("Successfully imported Dynamic Parallel Framework from extensions")
except ImportError as e:
    logger.error(f"Failed to import Dynamic Parallel Framework: {e}")
    sys.exit(1)

# Import quantum orchestrator extension if available
try:
    quantum_orchestrator_extension = importlib.import_module("quantum_orchestrator_nodular_extension")
    logger.info("Successfully imported Quantum Orchestrator Extension")
    has_orchestrator = True
except ImportError:
    logger.info("Quantum Orchestrator Extension not available, running standalone demo")
    has_orchestrator = False


def format_quantum_state(state_str):
    """Format quantum state for display."""
    if not state_str:
        return "Unknown"
    return state_str.replace('⟩', '>')


class DemoProcessor:
    """Wrapper for the Dynamic Parallel Processor with timeout capability."""
    
    def __init__(self, max_runtime=MAX_RUNTIME_SECONDS):
        self.processor = None
        self.max_runtime = max_runtime
        self.stop_event = threading.Event()
        self.start_time = None
        
    def start(self):
        """Start the processor with timeout."""
        try:
            self.processor = dynamic_parallel.DynamicParallelProcessor()
            self.processor.start()
            self.start_time = time.time()
            
            # Start timeout thread
            threading.Thread(target=self._timeout_monitor, daemon=True).start()
            return True
        except Exception as e:
            logger.error(f"Failed to start processor: {e}")
            return False
    
    def _timeout_monitor(self):
        """Monitor runtime and stop processor when max_runtime is reached."""
        while not self.stop_event.is_set():
            if time.time() - self.start_time > self.max_runtime:
                logger.info(f"Maximum runtime of {self.max_runtime} seconds reached, stopping processor")
                self.stop()
                break
            time.sleep(0.5)
    
    def stop(self):
        """Stop the processor."""
        self.stop_event.set()
        if self.processor:
            try:
                self.processor.stop()
                return True
            except Exception as e:
                logger.error(f"Error stopping processor: {e}")
        return False
    
    def get_system_state(self):
        """Get the current system state."""
        if not self.processor:
            return {
                "quantum_state": "Not initialized",
                "phi_resonance": 0.0,
                "efficiency": 0.0,
                "combined_state": {"coherence": 0.0}
            }
        
        try:
            return self.processor.get_system_state()
        except Exception as e:
            logger.error(f"Error getting system state: {e}")
            return {
                "quantum_state": "Error",
                "phi_resonance": 0.0,
                "efficiency": 0.0,
                "combined_state": {"coherence": 0.0}
            }
    
    def process_data(self, data):
        """Process data through the processor."""
        if not self.processor:
            return None
        
        try:
            return self.processor.process_data(data)
        except Exception as e:
            logger.error(f"Error processing data: {e}")
            return None


def run_standalone_demo():
    """Run standalone demonstration of Dynamic Parallel Processing Framework."""
    print("\n" + "="*80)
    print(" QUANTUM DYNAMIC PARALLEL PROCESSING FRAMEWORK DEMONSTRATION ".center(80, "="))
    print("="*80)
    
    print(f"\nRunning demonstration with {MAX_RUNTIME_SECONDS} second time limit...")
    
    print("\n[1/7] Creating Dynamic Parallel Processor...")
    processor = DemoProcessor()
    
    print("\n[2/7] Starting Dynamic Parallel Processor...")
    if not processor.start():
        print("Failed to start processor. Exiting.")
        return
    
    print("\n[3/7] Waiting for initialization...")
    time.sleep(2)
    
    print("\n[4/7] Retrieving system state...")
    system_state = processor.get_system_state()
    print(f"  Quantum State: {format_quantum_state(system_state.get('quantum_state', 'Unknown'))}")
    print(f"  Phi Resonance: {system_state.get('phi_resonance', 0):.6f}")
    print(f"  Efficiency: {system_state.get('efficiency', 0):.6f}")
    print(f"  Combined Coherence: {system_state.get('combined_state', {}).get('coherence', 0):.6f}")
    print(f"  Target Coherence: {TARGET_COHERENCE:.6f}")
    coherence = system_state.get('combined_state', {}).get('coherence', 0)
    if coherence > 0:
        print(f"  Coherence Ratio: {coherence / TARGET_COHERENCE:.6f}")
    
    print("\n[5/7] Processing test data...")
    test_data = [1, 2, 3, 4, 5]
    results = processor.process_data(test_data)
    
    if results:
        print(f"  Input Data: {results.get('input_data', 'Unknown')}")
        
        thread_results = results.get('thread_results', {})
        if 'earth' in thread_results:
            print(f"  Earth Result: {[round(x, 4) for x in thread_results['earth']]}")
        if 'moon' in thread_results:
            print(f"  Moon Result: {[round(x, 4) for x in thread_results['moon']]}")
        if 'human' in thread_results:
            print(f"  Human Result: {[round(x, 4) for x in thread_results['human']]}")
        
        if 'combined_result' in results:
            print(f"  Combined Result: {[round(x, 4) for x in results['combined_result']]}")
        
        print(f"  Processing Power: {results.get('processing_power', 0):.2f} QFLOPS")
        print(f"  Efficiency: {results.get('efficiency', 0):.6f}")
    else:
        print("  No results available")
    
    print("\n[6/7] Monitoring phi-harmonic synchronization...")
    remaining_time = max(0, MAX_RUNTIME_SECONDS - (time.time() - processor.start_time))
    check_interval = min(1, remaining_time / 5)
    checks = min(5, int(remaining_time / check_interval))
    
    for i in range(checks):
        time.sleep(check_interval)
        system_state = processor.get_system_state()
        coherence = system_state.get('combined_state', {}).get('coherence', 0)
        phi_resonance = system_state.get('phi_resonance', 0)
        print(f"  [{i+1}/{checks}] Coherence: {coherence:.6f}, "
              f"Phi Resonance: {phi_resonance:.6f}")
    
    print("\n[7/7] Stopping Dynamic Parallel Processor...")
    processor.stop()
    
    print("\nDynamic Parallel Processing demonstration complete.")
    print("="*80)


if __name__ == "__main__":
    print("\nQuantum Dynamic Parallel Processing Framework")
    print(f"Target Coherence: φ⁷·⁵/10 = {TARGET_COHERENCE:.6f}")
    print(f"Current Time: {time.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Maximum Runtime: {MAX_RUNTIME_SECONDS} seconds")
    
    run_standalone_demo()

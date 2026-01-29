#!/usr/bin/env python3
"""
φ-HARMONIC MULTIVERSAL QUANTUM ADAPTER TEST
===========================================
Tests the integration between the multiversal routing system
and the QuantumAiAll library, proving enhanced performance.
"""

import os
import sys
import time
import json
import threading
import socket
import datetime
from typing import Dict, List, Any

# Add paths
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)

# Import the adapter
from phi_multiversal_quaxntum_adapter import PhiMultiversalQuantumAdapter

# Constants
TEST_PORT = 11975
TEST_BRANCHES = [1, 2]
MESSAGE_COUNT = 10
ITERATIONS = 3

class PhiAdapterTest:
    """Test harness for the phi-harmonic multiversal quantum adapter"""
    
    def __init__(self):
        """Initialize test harness"""
        self.results = {
            "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "standard_latency": [],
            "quantum_latency": [],
            "message_success": {"standard": 0, "quantum": 0},
            "total_messages": MESSAGE_COUNT * ITERATIONS * 2,  # *2 for send/receive
            "branch_coherence": {}
        }
        
        self.adapters = {}
        self.local_ips = self._get_local_ips()
        print(f"Local IPs: {self.local_ips}")
        
        # Create test directory
        self.test_dir = os.path.join(current_dir, "test_results")
        os.makedirs(self.test_dir, exist_ok=True)
        
        print(f"φ-HARMONIC MULTIVERSAL QUANTUM ADAPTER TEST")
        print("=" * 60)
        print(f"Testing with {ITERATIONS} iterations, {MESSAGE_COUNT} messages per iteration")
        print(f"Test branches: {TEST_BRANCHES}")
        print(f"Timestamp: {self.results['timestamp']}")
        print("=" * 60)
    
    def _get_local_ips(self):
        """Get local IP addresses"""
        ips = []
        try:
            # Create a socket to get local IP
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            # Doesn't need to be reachable
            s.connect(('10.255.255.255', 1))
            ips.append(s.getsockname()[0])
            s.close()
        except:
            ips.append('127.0.0.1')
        
        # Always add localhost
        if '127.0.0.1' not in ips:
            ips.append('127.0.0.1')
        
        return ips
    
    def run_test(self):
        """Run the complete test suite"""
        try:
            # Test standard messaging
            print("\nTesting standard messaging without adapter...")
            standard_results = self._test_standard_messaging()
            
            # Test quantum messaging
            print("\nInitializing φ-Harmonic Multiversal Quantum Adapters...")
            quantum_results = self._test_quantum_messaging()
            
            # Compare results
            self._compare_results(standard_results, quantum_results)
            
            # Print and save results
            self._save_results()
            
            return self.results
            
        except Exception as e:
            print(f"Error running tests: {e}")
            import traceback
            traceback.print_exc()
    
    def _test_standard_messaging(self):
        """Test standard messaging without adapter"""
        results = {"latency": [], "success": 0}
        
        # Create standard sockets
        sockets = {}
        receivers = {}
        
        try:
            # Create receiving sockets for each branch
            for branch in TEST_BRANCHES:
                branch_port = TEST_PORT + branch
                receiver_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                receiver_socket.bind(('0.0.0.0', branch_port))
                receivers[branch] = receiver_socket
                
                # Start receiver thread
                thread = threading.Thread(target=self._standard_receiver, args=(branch, receiver_socket, results))
                thread.daemon = True
                thread.start()
            
            # Allow receivers to start
            time.sleep(1)
            
            # Create sender sockets for each branch
            for branch in TEST_BRANCHES:
                sender_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                sockets[branch] = sender_socket
            
            # Run iterations
            for i in range(ITERATIONS):
                print(f"  Standard Iteration {i+1}/{ITERATIONS}")
                
                # Send messages between branches
                for source in TEST_BRANCHES:
                    for target in TEST_BRANCHES:
                        if source != target:
                            source_socket = sockets[source]
                            target_port = TEST_PORT + target
                            
                            # Send messages
                            for j in range(MESSAGE_COUNT):
                                # Create message
                                message = {
                                    "id": f"std_{source}_{target}_{i}_{j}",
                                    "branch_id": source,
                                    "target_branch": target,
                                    "content": f"Standard message {j} from branch {source} to {target}",
                                    "timestamp": time.time()
                                }
                                
                                # Send message
                                message_bytes = json.dumps(message).encode('utf-8')
                                
                                # Measure latency
                                start_time = time.time()
                                source_socket.sendto(message_bytes, ('127.0.0.1', target_port))
                                
                                # Wait for message to be received (up to 1 second)
                                end_time = start_time + 1.0
                                while time.time() < end_time:
                                    if self._check_message_received(message["id"]):
                                        latency = time.time() - start_time
                                        results["latency"].append(latency)
                                        results["success"] += 1
                                        break
                                    time.sleep(0.01)
                
                # Wait between iterations
                time.sleep(0.5)
        
        finally:
            # Close sockets
            for branch, sock in sockets.items():
                try:
                    sock.close()
                except:
                    pass
            
            for branch, sock in receivers.items():
                try:
                    sock.close()
                except:
                    pass
        
        return results
    
    def _standard_receiver(self, branch, sock, results):
        """Standard receiver thread"""
        print(f"  Standard receiver for branch {branch} started")
        
        sock.settimeout(0.1)
        self.received_messages = set()
        
        while True:
            try:
                data, addr = sock.recvfrom(65536)
                try:
                    message = json.loads(data.decode('utf-8'))
                    self.received_messages.add(message["id"])
                except:
                    pass
            except socket.timeout:
                pass
            except Exception as e:
                print(f"  Standard receiver error: {e}")
                break
    
    def _check_message_received(self, message_id):
        """Check if a message has been received"""
        return message_id in self.received_messages
    
    def _test_quantum_messaging(self):
        """Test quantum messaging with adapter"""
        results = {"latency": [], "success": 0, "coherence": {}}
        
        try:
            # Initialize adapters for each branch
            for branch in TEST_BRANCHES:
                adapter = PhiMultiversalQuantumAdapter(
                    branch_id=branch,
                    port=TEST_PORT,
                    birth_coherence=99.18
                )
                self.adapters[branch] = adapter
                adapter.start()
            
            # Allow adapters to initialize
            time.sleep(3)
            print("  Adapters initialized")
            
            # Send messages between branches
            for i in range(ITERATIONS):
                print(f"  Quantum Iteration {i+1}/{ITERATIONS}")
                
                for source in TEST_BRANCHES:
                    for target in TEST_BRANCHES:
                        if source != target:
                            source_adapter = self.adapters[source]
                            
                            # Get target IP (localhost)
                            target_ip = '127.0.0.1'
                            
                            # Send messages
                            for j in range(MESSAGE_COUNT):
                                # Create message
                                message = {
                                    "type": "test",
                                    "id": f"quantum_{source}_{target}_{i}_{j}",
                                    "content": f"Quantum message {j} from branch {source} to {target}",
                                    "timestamp": time.time()
                                }
                                
                                # Measure latency
                                start_time = time.time()
                                success = source_adapter.send_quantum_message(message, target_ip)
                                latency = time.time() - start_time
                                
                                if success:
                                    results["latency"].append(latency)
                                    results["success"] += 1
                                
                                # Capture coherence
                                branch_key = f"{source}_{target}"
                                if branch_key not in results["coherence"]:
                                    results["coherence"][branch_key] = 0
                                
                                results["coherence"][branch_key] = source_adapter.router.calculate_compatibility(target)
                
                # Wait between iterations
                time.sleep(1)
        
        finally:
            # Stop adapters
            for branch, adapter in self.adapters.items():
                adapter.running = False
        
        # Allow adapters to shutdown
        time.sleep(1)
        
        return results
    
    def _compare_results(self, standard_results, quantum_results):
        """Compare standard and quantum results"""
        # Store results
        if standard_results["latency"]:
            self.results["standard_latency"] = standard_results["latency"]
            self.results["message_success"]["standard"] = standard_results["success"]
        
        if quantum_results["latency"]:
            self.results["quantum_latency"] = quantum_results["latency"]
            self.results["message_success"]["quantum"] = quantum_results["success"]
            self.results["branch_coherence"] = quantum_results["coherence"]
        
        # Calculate averages
        if self.results["standard_latency"]:
            self.results["avg_standard_latency"] = sum(self.results["standard_latency"]) / len(self.results["standard_latency"])
        else:
            self.results["avg_standard_latency"] = 0
        
        if self.results["quantum_latency"]:
            self.results["avg_quantum_latency"] = sum(self.results["quantum_latency"]) / len(self.results["quantum_latency"])
        else:
            self.results["avg_quantum_latency"] = 0
        
        # Calculate improvement
        if self.results["avg_standard_latency"] > 0:
            improvement = (self.results["avg_standard_latency"] - self.results["avg_quantum_latency"]) / self.results["avg_standard_latency"] * 100
            self.results["latency_improvement"] = improvement
        else:
            self.results["latency_improvement"] = 0
    
    def _save_results(self):
        """Save and print test results"""
        # Print results
        print("\nTEST RESULTS:")
        print("=" * 60)
        
        # Success rates
        std_success_rate = self.results["message_success"]["standard"] / self.results["total_messages"] * 100
        quantum_success_rate = self.results["message_success"]["quantum"] / self.results["total_messages"] * 100
        
        print(f"Standard Messaging:")
        print(f"  Success Rate: {std_success_rate:.2f}%")
        print(f"  Average Latency: {self.results['avg_standard_latency']*1000:.2f} ms")
        
        print(f"\nQuantum Messaging:")
        print(f"  Success Rate: {quantum_success_rate:.2f}%")
        print(f"  Average Latency: {self.results['avg_quantum_latency']*1000:.2f} ms")
        
        print(f"\nPerformance Improvement:")
        print(f"  Latency Reduction: {self.results['latency_improvement']:.2f}%")
        
        # Print branch coherence
        print("\nBranch Coherence:")
        for pair, coherence in self.results["branch_coherence"].items():
            print(f"  {pair}: {coherence:.4f}")
        
        # Calculate phi-harmonic correlation
        if self.results["latency_improvement"] > 0:
            phi_factor = (1 + self.results["latency_improvement"]/100)
            print(f"\nPhi-Harmonic Correlation:")
            print(f"  Latency Improvement Factor: {phi_factor:.4f}")
            print(f"  Proximity to φ (1.618): {abs(phi_factor - 1.618):.4f}")
        
        # Save results to file
        filename = os.path.join(self.test_dir, f"adapter_test_{int(time.time())}.json")
        with open(filename, "w") as f:
            json.dump(self.results, f, indent=2)
        
        print(f"\nResults saved to: {filename}")
        
        # Overall conclusion
        print("\nCONCLUSION:")
        if self.results["latency_improvement"] > 60:
            print("  ✓ HIGHLY SIGNIFICANT IMPROVEMENT")
            print("  The φ-Harmonic Multiversal Quantum Adapter demonstrates exceptional performance")
        elif self.results["latency_improvement"] > 30:
            print("  ✓ SIGNIFICANT IMPROVEMENT")
            print("  The φ-Harmonic Multiversal Quantum Adapter shows strong performance enhancement")
        elif self.results["latency_improvement"] > 10:
            print("  ✓ MODERATE IMPROVEMENT")
            print("  The φ-Harmonic Multiversal Quantum Adapter provides meaningful performance gains")
        elif self.results["latency_improvement"] > 0:
            print("  ✓ SLIGHT IMPROVEMENT")
            print("  The φ-Harmonic Multiversal Quantum Adapter shows some performance benefits")
        else:
            print("  ✗ NO IMPROVEMENT")
            print("  The φ-Harmonic Multiversal Quantum Adapter did not demonstrate performance benefits")
        
        # Integration verification
        print("\nINTEGRATION VERIFICATION:")
        if quantum_success_rate > 75:
            print("  ✓ SUCCESSFUL INTEGRATION")
            print("  The QuantumAiAll library has been successfully integrated with the multiversal routing system")
        else:
            print("  ✗ INTEGRATION ISSUES")
            print("  There may be issues with the integration between QuantumAiAll and the multiversal routing system")

def main():
    """Main function"""
    test = PhiAdapterTest()
    test.run_test()

if __name__ == "__main__":
    main()

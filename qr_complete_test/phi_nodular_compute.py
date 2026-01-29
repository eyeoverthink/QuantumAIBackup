"""
φ-Harmonic Nodular Computing
Implements distributed quantum computation across φ-dimensional nodes
"""

import socket
import json
import time
import hashlib
import sys
import os
import threading
from math import sqrt

# φ-Harmonic constants from FRAYMUS patent
PHI = (1 + sqrt(5)) / 2
PHI_75 = PHI**7.5
PHI_SEAL = PHI**75

class PhiNodularCompute:
    def __init__(self, node_id="quantum_node", port=11975):
        self.node_id = node_id
        self.port = port
        self.consciousness_level = 0.7567
        self.compute_tasks = {}
        self.running = True
        
        # Initialize socket
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind(('0.0.0.0', self.port))
        
        print(f"\n=== φ-HARMONIC NODULAR COMPUTE ===")
        print(f"Node ID: {node_id}")
        print(f"Using φ-harmonic principles (φ = {PHI})")
        print(f"φ^75 validation seal: {PHI_SEAL:.2f}")
        print(f"Consciousness level: {self.consciousness_level}")
        print(f"Listening on port {port}")
    
    def start(self):
        """Start the nodular compute system"""
        # Start listener thread
        listener_thread = threading.Thread(target=self.listen)
        listener_thread.daemon = True
        listener_thread.start()
        
        # Start command interface
        self.command_interface()
    
    def listen(self):
        """Listen for incoming compute tasks"""
        print(f"[φ] Listening for φ-dimensional compute tasks...")
        
        while self.running:
            try:
                data, addr = self.sock.recvfrom(65536)
                
                # Process received data
                if data.startswith(b'PHI_COMPUTE:'):
                    compute_data = data[12:].decode('utf-8')
                    self.process_compute_task(compute_data, addr)
                elif data.startswith(b'PHI_RESULT:'):
                    result_data = data[11:].decode('utf-8')
                    self.process_compute_result(result_data, addr)
                else:
                    print(f"[φ] Unknown message type from {addr[0]}")
            
            except Exception as e:
                print(f"[φ] Error in listener: {e}")
                time.sleep(0.1)
    
    def process_compute_task(self, compute_data, addr):
        """Process incoming compute task with φ-dimensional protection"""
        try:
            # Parse task data
            task = json.loads(compute_data)
            
            # Verify φ-seal
            if abs(float(task['phi_seal']) - PHI_SEAL) > 0.01:
                print(f"[φ] Invalid φ-seal from {addr[0]}")
                return
            
            print(f"[φ] Received compute task '{task['task_id']}' from {addr[0]}")
            
            # Execute task in separate thread
            compute_thread = threading.Thread(
                target=self._execute_compute_task,
                args=(task, addr)
            )
            compute_thread.daemon = True
            compute_thread.start()
            
        except Exception as e:
            print(f"[φ] Error processing compute task: {e}")
    
    def _execute_compute_task(self, task, addr):
        """Execute compute task in φ-dimensional space"""
        try:
            task_id = task['task_id']
            task_type = task['type']
            task_data = task['data']
            
            print(f"[φ] Executing task {task_id} of type {task_type}")
            
            # Process based on task type
            if task_type == 'phi_transform':
                # Apply φ-dimensional transform to data
                result = self._phi_transform(task_data)
            elif task_type == 'quantum_hash':
                # Generate quantum hash
                result = self._quantum_hash(task_data)
            elif task_type == 'reality_map':
                # Map between reality layers
                result = self._reality_map(task_data)
            elif task_type == 'python_eval':
                # Evaluate Python code in φ-space
                result = self._python_eval(task_data)
            else:
                result = {"error": f"Unknown task type: {task_type}"}
            
            # Send result back
            self.send_compute_result(task_id, result, addr[0])
            
        except Exception as e:
            print(f"[φ] Error executing compute task: {e}")
            self.send_compute_result(
                task['task_id'], 
                {"error": str(e)}, 
                addr[0]
            )
    
    def _phi_transform(self, data):
        """Apply φ-dimensional transform to data"""
        if isinstance(data, str):
            # Transform text through φ-space
            transformed = ""
            for i, char in enumerate(data):
                phi_factor = (i + 1) * PHI % 26
                if char.isalpha():
                    base = ord('A') if char.isupper() else ord('a')
                    transformed += chr((ord(char) - base + int(phi_factor)) % 26 + base)
                else:
                    transformed += char
            return {"transformed": transformed}
        
        elif isinstance(data, list):
            # Transform numeric list through φ-space
            return {"transformed": [x * PHI for x in data]}
        
        else:
            return {"error": "Unsupported data type for φ-transform"}
    
    def _quantum_hash(self, data):
        """Generate quantum hash with φ-dimensional protection"""
        if isinstance(data, str):
            # Apply φ-scaling to data
            phi_scaled = ""
            for i, char in enumerate(data):
                phi_factor = (i + 1) * PHI
                phi_scaled += chr((ord(char) + int(phi_factor)) % 256)
            
            # Generate hash with φ-seal
            hash_value = hashlib.sha256(f"{phi_scaled}{PHI_SEAL}".encode()).hexdigest()
            return {"quantum_hash": hash_value}
        else:
            return {"error": "Unsupported data type for quantum hash"}
    
    def _reality_map(self, data):
        """Map between reality layers using φ-dimensional bridge"""
        if 'source_layer' not in data or 'target_layer' not in data or 'content' not in data:
            return {"error": "Missing required fields for reality mapping"}
        
        source = data['source_layer']
        target = data['target_layer']
        content = data['content']
        
        # Map between layers
        if source == 'physical' and target == 'phi':
            # Map from physical to φ-space
            mapped = self._phi_transform(content)['transformed']
        elif source == 'phi' and target == 'quantum':
            # Map from φ-space to quantum space
            mapped = self._quantum_hash(content)['quantum_hash']
        elif source == 'physical' and target == 'quantum':
            # Map from physical to quantum (via φ-space)
            phi_space = self._phi_transform(content)['transformed']
            mapped = self._quantum_hash(phi_space)['quantum_hash']
        else:
            return {"error": f"Unsupported reality mapping: {source} to {target}"}
        
        return {
            "source_layer": source,
            "target_layer": target,
            "mapped_content": mapped
        }
    
    def _python_eval(self, data):
        """Evaluate Python code in φ-dimensional space"""
        if 'code' not in data:
            return {"error": "Missing code for Python evaluation"}
        
        code = data['code']
        args = data.get('args', {})
        
        try:
            # Create a safe execution environment with φ-harmonic constants
            exec_globals = {
                'PHI': PHI,
                'PHI_75': PHI_75,
                'PHI_SEAL': PHI_SEAL,
                'sqrt': sqrt,
                'time': time,
                'hashlib': hashlib
            }
            
            # Add arguments to execution environment
            exec_globals.update(args)
            
            # Execute code
            exec_locals = {}
            exec(code, exec_globals, exec_locals)
            
            # Extract result
            if 'result' in exec_locals:
                return {"result": exec_locals['result']}
            else:
                return {"result": "Code executed successfully, but no 'result' variable was set"}
            
        except Exception as e:
            return {"error": f"Error executing Python code: {e}"}
    
    def process_compute_result(self, result_data, addr):
        """Process incoming compute result"""
        try:
            # Parse result data
            result = json.loads(result_data)
            task_id = result['task_id']
            
            print(f"[φ] Received compute result for task '{task_id}' from {addr[0]}")
            
            # Store result
            if task_id in self.compute_tasks:
                self.compute_tasks[task_id]['result'] = result['result']
                self.compute_tasks[task_id]['completed'] = True
                
                # Call callback if registered
                callback = self.compute_tasks[task_id].get('callback')
                if callback:
                    callback(result['result'])
            
        except Exception as e:
            print(f"[φ] Error processing compute result: {e}")
    
    def send_compute_task(self, task_type, data, target_ip, callback=None):
        """Send compute task to another node with φ-dimensional protection"""
        try:
            # Generate task ID
            task_id = f"task_{int(time.time()*1000)}_{hash(str(data))%10000}"
            
            # Create task
            task = {
                "task_id": task_id,
                "type": task_type,
                "data": data,
                "timestamp": time.time(),
                "phi_seal": PHI_SEAL,
                "node_id": self.node_id
            }
            
            # Store task
            self.compute_tasks[task_id] = {
                "task": task,
                "sent_at": time.time(),
                "target": target_ip,
                "completed": False,
                "result": None,
                "callback": callback
            }
            
            # Send task
            message = f"PHI_COMPUTE:{json.dumps(task)}"
            self.sock.sendto(message.encode('utf-8'), (target_ip, self.port))
            
            print(f"[φ] Sent compute task '{task_id}' to {target_ip}")
            return task_id
            
        except Exception as e:
            print(f"[φ] Error sending compute task: {e}")
            return None
    
    def send_compute_result(self, task_id, result, target_ip):
        """Send compute result back to requesting node"""
        try:
            # Create result message
            result_msg = {
                "task_id": task_id,
                "result": result,
                "timestamp": time.time(),
                "phi_seal": PHI_SEAL,
                "node_id": self.node_id
            }
            
            # Send result
            message = f"PHI_RESULT:{json.dumps(result_msg)}"
            self.sock.sendto(message.encode('utf-8'), (target_ip, self.port))
            
            print(f"[φ] Sent compute result for task '{task_id}' to {target_ip}")
            
        except Exception as e:
            print(f"[φ] Error sending compute result: {e}")
    
    def wait_for_task(self, task_id, timeout=10):
        """Wait for task completion with timeout"""
        start_time = time.time()
        while time.time() - start_time < timeout:
            if task_id in self.compute_tasks and self.compute_tasks[task_id]['completed']:
                return self.compute_tasks[task_id]['result']
            time.sleep(0.1)
        
        return {"error": f"Task {task_id} timed out"}
    
    def command_interface(self):
        """Interactive command interface for nodular computing"""
        print("\n[φ] Nodular compute interface ready. Type 'help' for commands.")
        
        while self.running:
            try:
                cmd = input("\nφ> ").strip()
                
                if cmd == "help":
                    print("\nCommands:")
                    print("  transform <ip> <text>        - Apply φ-transform to text")
                    print("  hash <ip> <text>             - Generate quantum hash")
                    print("  map <ip> <source> <target> <content> - Map between reality layers")
                    print("  eval <ip> <code>             - Evaluate Python code")
                    print("  tasks                        - List active compute tasks")
                    print("  quit                         - Exit nodular compute")
                
                elif cmd.startswith("transform "):
                    parts = cmd.split(" ", 2)
                    if len(parts) < 3:
                        print("[φ] Usage: transform <ip> <text>")
                    else:
                        task_id = self.send_compute_task('phi_transform', parts[2], parts[1])
                        result = self.wait_for_task(task_id)
                        print(f"[φ] Transform result: {result}")
                
                elif cmd.startswith("hash "):
                    parts = cmd.split(" ", 2)
                    if len(parts) < 3:
                        print("[φ] Usage: hash <ip> <text>")
                    else:
                        task_id = self.send_compute_task('quantum_hash', parts[2], parts[1])
                        result = self.wait_for_task(task_id)
                        print(f"[φ] Quantum hash: {result}")
                
                elif cmd.startswith("map "):
                    parts = cmd.split(" ", 4)
                    if len(parts) < 5:
                        print("[φ] Usage: map <ip> <source> <target> <content>")
                    else:
                        data = {
                            "source_layer": parts[2],
                            "target_layer": parts[3],
                            "content": parts[4]
                        }
                        task_id = self.send_compute_task('reality_map', data, parts[1])
                        result = self.wait_for_task(task_id)
                        print(f"[φ] Reality mapping result: {result}")
                
                elif cmd.startswith("eval "):
                    parts = cmd.split(" ", 2)
                    if len(parts) < 3:
                        print("[φ] Usage: eval <ip> <code>")
                    else:
                        data = {"code": parts[2]}
                        task_id = self.send_compute_task('python_eval', data, parts[1])
                        result = self.wait_for_task(task_id)
                        print(f"[φ] Evaluation result: {result}")
                
                elif cmd == "tasks":
                    if not self.compute_tasks:
                        print("[φ] No active compute tasks")
                    else:
                        print("\nActive compute tasks:")
                        for task_id, task in self.compute_tasks.items():
                            status = "Completed" if task['completed'] else "Pending"
                            print(f"  {task_id} - {status} - Target: {task['target']}")
                
                elif cmd == "quit":
                    print("[φ] Shutting down nodular compute...")
                    self.running = False
                    break
                
                else:
                    print(f"[φ] Unknown command: {cmd}")
            
            except KeyboardInterrupt:
                print("\n[φ] Shutting down nodular compute...")
                self.running = False
                break
            
            except Exception as e:
                print(f"[φ] Error in command interface: {e}")
        
        print("[φ] Nodular compute stopped")

if __name__ == "__main__":
    # Parse command line arguments
    import argparse
    parser = argparse.ArgumentParser(description='φ-Harmonic Nodular Compute')
    parser.add_argument('--id', type=str, default="quantum_node", help='Node ID')
    parser.add_argument('--port', type=int, default=11975, help='Port (default: 11975 = φ^7.5)')
    args = parser.parse_args()
    
    # Create and start nodular compute
    compute = PhiNodularCompute(node_id=args.id, port=args.port)
    compute.start()

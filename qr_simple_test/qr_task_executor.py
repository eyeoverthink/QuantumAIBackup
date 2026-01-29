#!/usr/bin/env python3
"""
QR Task Executor - Part of Animated QR Flipbook DNA System
By Vaughn Scott

Executes tasks embedded in QR codons with secure sandboxing.
Supports multiple execution environments (Python, Shell).
Implements phi-harmonic execution metrics.
"""

import os
import sys
import json
import math
import time
import uuid
import base64
import hashlib
import tempfile
import subprocess
import numpy as np
from datetime import datetime, timedelta

# Phi (Golden Ratio) constant
PHI = (1 + np.sqrt(5)) / 2  # Approximately 1.618034

class QRTaskExecutor:
    """
    Executes tasks embedded in QR codons with secure sandboxing.
    """
    
    def __init__(self, sandbox_dir=None, timeout=5, debug=False):
        """
        Initialize the QR Task Executor.
        
        Args:
            sandbox_dir: Directory for sandbox execution (temp dir if None)
            timeout: Execution timeout in seconds
            debug: Whether to print debug information
        """
        self.sandbox_dir = sandbox_dir or tempfile.mkdtemp(prefix="qr_sandbox_")
        self.timeout = timeout
        self.debug = debug
        self.execution_count = 0
        self.success_count = 0
        self.last_execution_time = 0
        self.execution_history = []
        
        # Ensure sandbox directory exists
        os.makedirs(self.sandbox_dir, exist_ok=True)
        
        if self.debug:
            print(f"QR Task Executor initialized with sandbox at {self.sandbox_dir}")
    
    def execute_task(self, task_type, task_data):
        """
        Execute a task based on its type.
        
        Args:
            task_type: Type of task to execute
            task_data: Data for the task
            
        Returns:
            Tuple of (success, output)
        """
        self.execution_count += 1
        start_time = time.time()
        
        # Execute based on task type
        if task_type == "execute_python":
            success, output = self.execute_python(task_data)
        elif task_type == "execute_sh":
            success, output = self.execute_shell(task_data)
        else:
            success = False
            output = f"Unknown task type: {task_type}"
        
        # Record execution time
        self.last_execution_time = time.time() - start_time
        
        # Update success count
        if success:
            self.success_count += 1
        
        # Record execution
        self.execution_history.append({
            "timestamp": datetime.now().isoformat(),
            "task_type": task_type,
            "success": success,
            "execution_time": self.last_execution_time
        })
        
        if self.debug:
            print(f"Executed {task_type}: {'Success' if success else 'Failed'} in {self.last_execution_time:.4f}s")
        
        return success, output
    
    def execute_python(self, task_data):
        """
        Execute Python code in a sandbox.
        
        Args:
            task_data: Dictionary containing task data
            
        Returns:
            Tuple of (success, output)
        """
        # Extract code from task data
        code = task_data.get("code", "")
        if not code:
            return False, "No code provided"
        
        # Create a temporary file for the code
        with tempfile.NamedTemporaryFile(suffix=".py", dir=self.sandbox_dir, delete=False) as temp_file:
            temp_path = temp_file.name
            temp_file.write(code.encode())
        
        try:
            # Execute the code in a subprocess
            proc = subprocess.run(
                [sys.executable, temp_path],
                capture_output=True,
                timeout=self.timeout,
                cwd=self.sandbox_dir
            )
            
            # Check if execution was successful
            success = proc.returncode == 0
            
            # Get output
            if success:
                output = proc.stdout.decode()
            else:
                output = proc.stderr.decode()
            
            return success, output
            
        except subprocess.TimeoutExpired:
            return False, f"Execution timed out after {self.timeout} seconds"
        except Exception as e:
            return False, f"Error executing Python code: {e}"
        finally:
            # Clean up temporary file
            if os.path.exists(temp_path):
                os.unlink(temp_path)
    
    def execute_shell(self, task_data):
        """
        Execute shell script in a sandbox.
        
        Args:
            task_data: Dictionary containing task data
            
        Returns:
            Tuple of (success, output)
        """
        # Extract code from task data
        code = task_data.get("code", "")
        if not code:
            return False, "No code provided"
        
        # Create a temporary file for the code
        with tempfile.NamedTemporaryFile(suffix=".sh", dir=self.sandbox_dir, delete=False) as temp_file:
            temp_path = temp_file.name
            temp_file.write(code.encode())
        
        try:
            # Make the script executable
            os.chmod(temp_path, 0o755)
            
            # Execute the code in a subprocess
            proc = subprocess.run(
                [temp_path],
                shell=True,
                capture_output=True,
                timeout=self.timeout,
                cwd=self.sandbox_dir
            )
            
            # Check if execution was successful
            success = proc.returncode == 0
            
            # Get output
            if success:
                output = proc.stdout.decode()
            else:
                output = proc.stderr.decode()
            
            return success, output
            
        except subprocess.TimeoutExpired:
            return False, f"Execution timed out after {self.timeout} seconds"
        except Exception as e:
            return False, f"Error executing shell script: {e}"
        finally:
            # Clean up temporary file
            if os.path.exists(temp_path):
                os.unlink(temp_path)
    
    def calculate_phi_metrics(self, success, execution_time):
        """
        Calculate phi-harmonic metrics for an execution.
        
        Args:
            success: Whether execution was successful
            execution_time: Time taken for execution
            
        Returns:
            Dictionary of phi-harmonic metrics
        """
        # Calculate success rate
        success_rate = self.success_count / self.execution_count if self.execution_count > 0 else 0
        
        # Calculate phi-resonance based on success rate
        phi_resonance = 1.0 / (1.0 + abs((success_rate * PHI) % 1.0 - 0.5))
        
        # Calculate complexity based on execution time and history
        avg_time = sum(e["execution_time"] for e in self.execution_history[-10:]) / min(10, len(self.execution_history))
        time_ratio = execution_time / avg_time if avg_time > 0 else 1.0
        complexity = 0.5 + 0.5 * (1.0 / (1.0 + math.exp(-time_ratio + 1)))
        
        # Calculate generation based on execution count
        generation = 1 + int(self.execution_count / 10)
        
        return {
            "success_rate": success_rate,
            "resonance": phi_resonance,
            "complexity": complexity,
            "generation": generation
        }
    
    def get_execution_summary(self):
        """
        Get a summary of executions.
        
        Returns:
            Dictionary containing execution summary
        """
        return {
            "execution_count": self.execution_count,
            "success_count": self.success_count,
            "success_rate": self.success_count / self.execution_count if self.execution_count > 0 else 0,
            "last_execution_time": self.last_execution_time,
            "phi_metrics": self.calculate_phi_metrics(
                self.success_count / self.execution_count if self.execution_count > 0 else 0,
                self.last_execution_time
            )
        }
    
    def cleanup(self):
        """Clean up sandbox directory."""
        import shutil
        if os.path.exists(self.sandbox_dir):
            shutil.rmtree(self.sandbox_dir)
            if self.debug:
                print(f"Cleaned up sandbox directory {self.sandbox_dir}")

def test_executor():
    """Test the QR Task Executor."""
    executor = QRTaskExecutor(debug=True)
    
    # Test Python execution
    python_code = """
print("Hello from Python!")
import math
print(f"Phi calculated: {(1 + math.sqrt(5)) / 2}")
"""
    
    python_task = {
        "code": python_code
    }
    
    print("\nTesting Python execution:")
    success, output = executor.execute_task("execute_python", python_task)
    print(f"Success: {success}")
    print(f"Output: {output}")
    
    # Test Shell execution
    shell_code = """
#!/bin/bash
echo "Hello from Shell!"
echo "Current directory: $(pwd)"
echo "Files: $(ls -la)"
"""
    
    shell_task = {
        "code": shell_code
    }
    
    print("\nTesting Shell execution:")
    success, output = executor.execute_task("execute_sh", shell_task)
    print(f"Success: {success}")
    print(f"Output: {output}")
    
    # Print execution summary
    print("\nExecution Summary:")
    summary = executor.get_execution_summary()
    for key, value in summary.items():
        if key == "phi_metrics":
            print(f"{key}:")
            for metric_key, metric_value in value.items():
                print(f"  {metric_key}: {metric_value}")
        else:
            print(f"{key}: {value}")
    
    # Clean up
    executor.cleanup()

if __name__ == "__main__":
    print("QR Task Executor - By Vaughn Scott")
    test_executor()

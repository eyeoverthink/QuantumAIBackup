#!/usr/bin/env python3
"""
ESP32 Quantum Memory Bridge
Connects ESP32 sensor data with Quantum Hybrid Memory for efficient storage and retrieval
"""

import json
import time
import numpy as np
import serial
import threading
import queue
from datetime import datetime, timedelta
import os
import sys
from typing import Dict, List, Any, Tuple, Optional

# Import memory components
from quantum_hybrid_memory import QuantumHybridMemory

# Define φ (phi) constant
PHI = (1 + np.sqrt(5)) / 2

class ESP32QuantumMemoryBridge:
    """
    Bridge between ESP32 sensor data and Quantum Hybrid Memory
    Enables efficient storage, retrieval, and processing of sensor data
    """
    
    def __init__(self, serial_port='/dev/ttyUSB0', baud_rate=115200, memory_buckets=16):
        """Initialize the ESP32 Quantum Memory Bridge"""
        self.serial_port = serial_port
        self.baud_rate = baud_rate
        self.serial_connection = None
        self.connected = False
        
        # Initialize quantum hybrid memory
        self.memory = QuantumHybridMemory(
            ferris_buckets=memory_buckets,
            centripetal_buckets=memory_buckets
        )
        
        # Data processing queues
        self.data_queue = queue.Queue()
        self.result_queue = queue.Queue()
        
        # Processing threads
        self.reader_thread = None
        self.processor_thread = None
        self.running = False
        
        # Data storage
        self.sensor_data = {}
        self.processed_data = {}
        self.phi_patterns = {}
        
        # Create output directory for data files
        self.output_dir = "esp32_quantum_data"
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)
    
    def connect(self):
        """Connect to the ESP32 device"""
        try:
            self.serial_connection = serial.Serial(
                port=self.serial_port,
                baudrate=self.baud_rate,
                timeout=1
            )
            self.connected = True
            print(f"Connected to ESP32 on {self.serial_port}")
            return True
        except Exception as e:
            print(f"Error connecting to ESP32: {e}")
            self.connected = False
            return False
    
    def disconnect(self):
        """Disconnect from the ESP32 device"""
        if self.serial_connection and self.connected:
            self.serial_connection.close()
            self.connected = False
            print("Disconnected from ESP32")
    
    def start_processing(self):
        """Start processing data from ESP32"""
        if not self.connected and not self.connect():
            print("Cannot start processing: Not connected to ESP32")
            return False
        
        self.running = True
        
        # Start reader thread
        self.reader_thread = threading.Thread(target=self._reader_thread)
        self.reader_thread.daemon = True
        self.reader_thread.start()
        
        # Start processor thread
        self.processor_thread = threading.Thread(target=self._processor_thread)
        self.processor_thread.daemon = True
        self.processor_thread.start()
        
        print("ESP32 Quantum Memory Bridge processing started")
        return True
    
    def stop_processing(self):
        """Stop processing data from ESP32"""
        self.running = False
        
        # Wait for threads to finish
        if self.reader_thread and self.reader_thread.is_alive():
            self.reader_thread.join(timeout=2.0)
        
        if self.processor_thread and self.processor_thread.is_alive():
            self.processor_thread.join(timeout=2.0)
        
        # Disconnect from ESP32
        self.disconnect()
        
        print("ESP32 Quantum Memory Bridge processing stopped")
    
    def _reader_thread(self):
        """Thread for reading data from ESP32"""
        while self.running:
            try:
                if self.serial_connection and self.connected:
                    # Read a line from the serial connection
                    line = self.serial_connection.readline().decode('utf-8').strip()
                    
                    if line:
                        # Parse the data
                        try:
                            # Try to parse as JSON
                            data = json.loads(line)
                            timestamp = datetime.now().isoformat()
                            
                            # Add to data queue for processing
                            self.data_queue.put({
                                'timestamp': timestamp,
                                'data': data
                            })
                        except json.JSONDecodeError:
                            # If not JSON, treat as plain text
                            timestamp = datetime.now().isoformat()
                            self.data_queue.put({
                                'timestamp': timestamp,
                                'data': {'raw': line}
                            })
            except Exception as e:
                print(f"Error in reader thread: {e}")
                time.sleep(1.0)
    
    def _processor_thread(self):
        """Thread for processing data from the queue"""
        while self.running:
            try:
                # Get data from queue with timeout
                try:
                    data_item = self.data_queue.get(timeout=1.0)
                except queue.Empty:
                    continue
                
                # Process the data
                processed_data = self._process_sensor_data(data_item)
                
                # Store in memory
                if processed_data:
                    timestamp = processed_data.get('timestamp')
                    memory_key = f"esp32_data_{timestamp}"
                    
                    # Store in quantum memory
                    self.memory.store(memory_key, processed_data)
                    
                    # Add to processed data collection
                    self.processed_data[timestamp] = processed_data
                    
                    # Put in result queue
                    self.result_queue.put(processed_data)
                
                # Mark task as done
                self.data_queue.task_done()
                
            except Exception as e:
                print(f"Error in processor thread: {e}")
                time.sleep(1.0)
    
    def _process_sensor_data(self, data_item):
        """Process sensor data using φ-harmonic principles"""
        timestamp = data_item.get('timestamp')
        data = data_item.get('data', {})
        
        # Skip if no data
        if not data:
            return None
        
        # Extract sensor values
        sensor_values = {}
        
        # Process different types of sensor data
        if isinstance(data, dict):
            # Extract numeric values for processing
            for key, value in data.items():
                if isinstance(value, (int, float)):
                    sensor_values[key] = value
        
        # Skip if no numeric sensor values
        if not sensor_values:
            return data_item
        
        # Apply φ-harmonic processing
        phi_processed = {}
        for key, value in sensor_values.items():
            # Store original value
            phi_processed[f"{key}_original"] = value
            
            # Apply φ-scaling
            phi_processed[f"{key}_phi_scaled"] = value * PHI
            
            # Apply φ-resonance detection
            phi_factor = value / PHI
            phi_resonance = abs(phi_factor - round(phi_factor))
            phi_processed[f"{key}_phi_resonance"] = phi_resonance
            
            # Detect φ-patterns over time
            if key not in self.phi_patterns:
                self.phi_patterns[key] = []
            
            # Store in pattern history (limit to 100 values)
            self.phi_patterns[key].append(value)
            if len(self.phi_patterns[key]) > 100:
                self.phi_patterns[key].pop(0)
            
            # Calculate φ-pattern metrics if we have enough history
            if len(self.phi_patterns[key]) >= 5:
                # Calculate φ-ratio between consecutive values
                ratios = [self.phi_patterns[key][i+1] / self.phi_patterns[key][i] 
                         if self.phi_patterns[key][i] != 0 else 0
                         for i in range(len(self.phi_patterns[key])-1)]
                
                # Calculate average ratio
                avg_ratio = sum(ratios) / len(ratios) if ratios else 0
                
                # Calculate φ-resonance (how close to PHI)
                phi_pattern_resonance = abs(avg_ratio - PHI) / PHI
                
                phi_processed[f"{key}_pattern_resonance"] = phi_pattern_resonance
        
        # Combine original data with processed data
        result = {
            'timestamp': timestamp,
            'original_data': data,
            'phi_processed': phi_processed
        }
        
        return result
    
    def get_latest_data(self, count=1):
        """Get the latest processed data items"""
        # Convert to list and sort by timestamp
        data_list = list(self.processed_data.values())
        data_list.sort(key=lambda x: x.get('timestamp', ''), reverse=True)
        
        # Return requested number of items
        return data_list[:count]
    
    def query_data_by_time(self, start_time, end_time=None):
        """Query data within a time range"""
        if end_time is None:
            end_time = datetime.now().isoformat()
        
        # Filter data by timestamp
        results = []
        for timestamp, data in self.processed_data.items():
            if start_time <= timestamp <= end_time:
                results.append(data)
        
        # Sort by timestamp
        results.sort(key=lambda x: x.get('timestamp', ''))
        
        return results
    
    def query_memory_by_pattern(self, pattern_threshold=0.1):
        """Query data with specific φ-pattern resonance"""
        results = []
        
        # Search through all keys in memory
        memory_keys = self.memory.list_keys()
        
        for key in memory_keys:
            if key.startswith('esp32_data_'):
                # Retrieve data from memory
                result = self.memory.retrieve(key)
                
                if result.get('success', False):
                    data = result.get('data', {})
                    phi_processed = data.get('phi_processed', {})
                    
                    # Check for pattern resonance in any sensor
                    for sensor_key, value in phi_processed.items():
                        if sensor_key.endswith('_pattern_resonance') and value <= pattern_threshold:
                            results.append(data)
                            break
        
        return results
    
    def save_data_to_file(self, filename=None):
        """Save all processed data to a file"""
        if filename is None:
            filename = f"{self.output_dir}/esp32_data_{datetime.now().strftime('%Y%m%d%H%M%S')}.json"
        
        # Convert data to serializable format
        serializable_data = {}
        for timestamp, data in self.processed_data.items():
            serializable_data[timestamp] = data
        
        # Save to file
        with open(filename, 'w') as f:
            json.dump(serializable_data, f, indent=2)
        
        print(f"Data saved to {filename}")
        return filename
    
    def load_data_from_file(self, filename):
        """Load processed data from a file"""
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
            
            # Update processed data
            self.processed_data.update(data)
            
            # Store in memory
            for timestamp, item in data.items():
                memory_key = f"esp32_data_{timestamp}"
                self.memory.store(memory_key, item)
            
            print(f"Loaded {len(data)} data items from {filename}")
            return True
        except Exception as e:
            print(f"Error loading data from file: {e}")
            return False
    
    def get_memory_stats(self):
        """Get statistics about the memory usage"""
        return self.memory.get_stats()
    
    def optimize_memory(self):
        """Optimize memory usage"""
        return self.memory.optimize()

def simulate_esp32_data(bridge, duration=60, interval=1.0):
    """
    Simulate ESP32 sensor data for testing when hardware is not available
    
    Args:
        bridge: ESP32QuantumMemoryBridge instance
        duration: Duration to simulate data in seconds
        interval: Interval between data points in seconds
    """
    print(f"Simulating ESP32 data for {duration} seconds...")
    
    # Start time
    start_time = time.time()
    
    # Run for specified duration
    while (time.time() - start_time) < duration:
        # Generate simulated sensor data
        timestamp = datetime.now().isoformat()
        
        # Create simulated data with φ-harmonic patterns
        t = (time.time() - start_time) / 10.0  # Time factor
        
        # Temperature with φ-harmonic oscillation
        temperature = 25.0 + 5.0 * np.sin(t / PHI)
        
        # Humidity with φ-based pattern
        humidity = 50.0 + 10.0 * np.sin(t * PHI)
        
        # Pressure with φ-squared pattern
        pressure = 1013.0 + 5.0 * np.sin(t * (PHI ** 2))
        
        # Create data packet
        data = {
            'temperature': temperature,
            'humidity': humidity,
            'pressure': pressure,
            'phi_factor': PHI ** (t % 3)  # Cycling φ-power
        }
        
        # Add to data queue
        bridge.data_queue.put({
            'timestamp': timestamp,
            'data': data
        })
        
        # Wait for next interval
        time.sleep(interval)
    
    print("Simulation complete")

def run_esp32_quantum_bridge_demo():
    """Run a demonstration of the ESP32 Quantum Memory Bridge"""
    print("Starting ESP32 Quantum Memory Bridge demonstration...")
    
    # Create bridge
    bridge = ESP32QuantumMemoryBridge(serial_port='SIMULATION')
    
    # Start processing
    bridge.start_processing()
    
    # Run simulation instead of connecting to real hardware
    simulation_thread = threading.Thread(
        target=simulate_esp32_data,
        args=(bridge, 30, 0.1)  # 30 seconds, 0.1s interval
    )
    simulation_thread.daemon = True
    simulation_thread.start()
    
    # Wait for simulation to complete
    simulation_thread.join()
    
    # Wait for processing to complete
    time.sleep(2.0)
    
    # Stop processing
    bridge.stop_processing()
    
    # Get latest data
    latest_data = bridge.get_latest_data(5)
    print("\nLatest 5 data points:")
    for item in latest_data:
        print(f"  {item['timestamp']}: {item['original_data']}")
    
    # Query data with high φ-resonance
    phi_resonant_data = bridge.query_memory_by_pattern(0.05)
    print(f"\nFound {len(phi_resonant_data)} data points with high φ-resonance")
    
    # Get memory stats
    memory_stats = bridge.get_memory_stats()
    print("\nMemory statistics:")
    for key, value in memory_stats.items():
        print(f"  {key}: {value}")
    
    # Save data to file
    filename = bridge.save_data_to_file()
    
    print("\nESP32 Quantum Memory Bridge demonstration complete!")
    print(f"Data saved to {filename}")
    
    return bridge

if __name__ == "__main__":
    run_esp32_quantum_bridge_demo()

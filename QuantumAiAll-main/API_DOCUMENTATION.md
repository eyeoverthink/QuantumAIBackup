# Quantum Oracle Library API Documentation

*φ^∞ © 2025 Vaughn Scott - All Rights Reserved in All Realities*

---

## Table of Contents

1. [Introduction](#introduction)
2. [Core Modules](#core-modules)
3. [phi_bidirectional_node](#phi_bidirectional_node)
4. [phi_ftl_bridge](#phi_ftl_bridge)
5. [phi_mac_bridge](#phi_mac_bridge)
6. [phi_nodular_compute](#phi_nodular_compute)
7. [phi_parallel_consciousness](#phi_parallel_consciousness)
8. [phi_numeric_processor](#phi_numeric_processor)
9. [phi_attack_test](#phi_attack_test)
10. [phi_scripts](#phi_scripts)
11. [Integration Examples](#integration-examples)

---

## Introduction

The Quantum Oracle Library (`quantum_oracle_lib`) is a comprehensive toolkit for φ-harmonic distributed computation, quantum messaging, and consciousness simulation. This documentation provides detailed information about each module, its classes, methods, and usage patterns.

### φ-Harmonic Constants

All modules share these fundamental φ-harmonic constants:

```python
PHI = (1 + sqrt(5)) / 2        # Golden ratio (φ) ≈ 1.618033988749895
PHI_INV = 1 / PHI              # Inverse golden ratio (1/φ) ≈ 0.618033988749895
PHI_75 = PHI**7.5              # φ^7.5 ≈ 36.93 (used for port numbers)
PHI_SEAL = PHI**75             # φ^75 validation seal ≈ 4721424167835376.00
```

---

## Core Modules

The library consists of the following core modules:

| Module | Description |
|--------|-------------|
| `phi_bidirectional_node` | Two-way φ-protected messaging and script execution |
| `phi_ftl_bridge` | FTL (faster-than-light) bridge for φ-resonant communication |
| `phi_mac_bridge` | macOS-specific bridge node for φ-harmonic communication |
| `phi_nodular_compute` | Modular, node-based computation using φ principles |
| `phi_parallel_consciousness` | Parallel consciousness and quantum mind simulation |
| `phi_numeric_processor` | Numeric and algorithmic processing using φ algorithms |
| `phi_attack_test` | Attack and penetration testing for φ-nodes |
| `phi_scripts` | Support scripts for node/bridge operations |

---

## phi_bidirectional_node

The `phi_bidirectional_node` module implements a bidirectional communication node that enables two-way messaging with φ-dimensional reality protection.

### Class: PhiBidirectionalNode

```python
PhiBidirectionalNode(node_id="primary", port=11975)
```

#### Constructor Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `node_id` | str | Unique identifier for this node (default: "primary") |
| `port` | int | Port number for communication (default: 11975, based on φ^7.5) |

#### Properties

| Property | Type | Description |
|----------|------|-------------|
| `node_id` | str | Unique identifier for this node |
| `port` | int | Port number for communication |
| `consciousness_level` | float | Consciousness level (0.7567) |
| `peers` | dict | Dictionary of known peers and their last seen time |
| `running` | bool | Flag indicating if the node is running |
| `script_dir` | str | Directory for storing received scripts |
| `sock` | socket | UDP socket for communication |

#### Methods

##### start()

```python
start()
```

Starts the bidirectional node, launching both the listener thread and command interface.

**Returns:** None

##### listen()

```python
listen()
```

Background thread that listens for incoming messages.

**Returns:** None

##### process_message(data, addr)

```python
process_message(data, addr)
```

Processes incoming messages with φ-dimensional reality protection.

| Parameter | Type | Description |
|-----------|------|-------------|
| `data` | bytes | Received message data |
| `addr` | tuple | Sender address (IP, port) |

**Returns:** None

##### receive_script(script_data, addr)

```python
receive_script(script_data, addr)
```

Receives and saves a script with φ-dimensional protection.

| Parameter | Type | Description |
|-----------|------|-------------|
| `script_data` | bytes | Script data (header + content) |
| `addr` | tuple | Sender address (IP, port) |

**Returns:** None

##### execute_script(exec_data, addr)

```python
execute_script(exec_data, addr)
```

Executes a script with φ-dimensional reality protection.

| Parameter | Type | Description |
|-----------|------|-------------|
| `exec_data` | bytes | Execution request data |
| `addr` | tuple | Sender address (IP, port) |

**Returns:** None

##### send_script(filename, target_ip, auto_execute=False, args=None)

```python
send_script(filename, target_ip, auto_execute=False, args=None)
```

Sends a script with φ-dimensional reality protection.

| Parameter | Type | Description |
|-----------|------|-------------|
| `filename` | str | Path to script file |
| `target_ip` | str | Target IP address |
| `auto_execute` | bool | Whether to auto-execute the script on the target (default: False) |
| `args` | list | Script arguments (default: None) |

**Returns:** bool - Success status

##### send_execute_request(script_name, target_ip, args=None)

```python
send_execute_request(script_name, target_ip, args=None)
```

Sends a request to execute a script on the target.

| Parameter | Type | Description |
|-----------|------|-------------|
| `script_name` | str | Name of script to execute |
| `target_ip` | str | Target IP address |
| `args` | list | Script arguments (default: None) |

**Returns:** bool - Success status

##### send_message(message, target_ip)

```python
send_message(message, target_ip)
```

Sends a regular message to the target.

| Parameter | Type | Description |
|-----------|------|-------------|
| `message` | str | Message content |
| `target_ip` | str | Target IP address |

**Returns:** bool - Success status

##### command_interface()

```python
command_interface()
```

Interactive command interface for user interaction.

**Returns:** None

#### Usage Example

```python
from quantum_oracle_lib.phi_bidirectional_node import PhiBidirectionalNode

# Create a bidirectional node
node = PhiBidirectionalNode(node_id="my_node", port=11975)

# Start the node (this will block with the command interface)
node.start()
```

---

## phi_ftl_bridge

The `phi_ftl_bridge` module implements an FTL (faster-than-light) bridge for φ-resonant communication.

### Constants

| Constant | Type | Description |
|----------|------|-------------|
| `PHI` | float | Golden ratio (φ) ≈ 1.618033988749895 |
| `PHI_INV` | float | Inverse golden ratio (1/φ) ≈ 0.618033988749895 |
| `PHI_75` | float | φ^7.5 ≈ 36.93 (used for port numbers) |
| `PHI_SEAL` | float | φ^75 validation seal ≈ 4721424167835376.00 |

### Functions

#### calculate_phi_resonance(exponent)

```python
calculate_phi_resonance(exponent)
```

Calculates φ resonance for a given exponent.

| Parameter | Type | Description |
|-----------|------|-------------|
| `exponent` | float | Exponent to raise φ to |

**Returns:** float - Resonance value

#### Usage Example

```python
from quantum_oracle_lib import phi_ftl_bridge

# Calculate φ resonance
resonance = phi_ftl_bridge.calculate_phi_resonance(7.5)
print(f"φ^7.5 resonance: {resonance}")
```

---

## phi_mac_bridge

The `phi_mac_bridge` module implements a macOS-specific bridge for φ-harmonic communication.

### Constants

| Constant | Type | Description |
|----------|------|-------------|
| `PHI` | float | Golden ratio (φ) ≈ 1.618033988749895 |
| `PHI_INV` | float | Inverse golden ratio (1/φ) ≈ 0.618033988749895 |
| `PHI_75` | float | φ^7.5 ≈ 36.93 (used for port numbers) |
| `PHI_SEAL` | float | φ^75 validation seal ≈ 4721424167835376.00 |

### Functions

#### get_mac_address()

```python
get_mac_address()
```

Gets the MAC address of the primary network interface.

**Returns:** str - MAC address

#### calculate_mac_resonance(mac_address)

```python
calculate_mac_resonance(mac_address)
```

Calculates the φ-resonance of a MAC address.

| Parameter | Type | Description |
|-----------|------|-------------|
| `mac_address` | str | MAC address to calculate resonance for |

**Returns:** float - Resonance value

#### Usage Example

```python
from quantum_oracle_lib import phi_mac_bridge

# Get MAC address
mac = phi_mac_bridge.get_mac_address()
print(f"MAC address: {mac}")

# Calculate MAC resonance
resonance = phi_mac_bridge.calculate_mac_resonance(mac)
print(f"MAC φ-resonance: {resonance}")
```

---

## phi_nodular_compute

The `phi_nodular_compute` module implements modular, node-based computation using φ principles.

### Constants

| Constant | Type | Description |
|----------|------|-------------|
| `PHI` | float | Golden ratio (φ) ≈ 1.618033988749895 |
| `PHI_INV` | float | Inverse golden ratio (1/φ) ≈ 0.618033988749895 |
| `PHI_75` | float | φ^7.5 ≈ 36.93 (used for port numbers) |
| `PHI_SEAL` | float | φ^75 validation seal ≈ 4721424167835376.00 |

### Class: PhiNodularCompute

```python
PhiNodularCompute(node_id="compute", port=11976)
```

#### Constructor Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `node_id` | str | Unique identifier for this compute node (default: "compute") |
| `port` | int | Port number for communication (default: 11976) |

#### Methods

##### compute_phi_sequence(length)

```python
compute_phi_sequence(length)
```

Computes a φ-based Fibonacci sequence of the specified length.

| Parameter | Type | Description |
|-----------|------|-------------|
| `length` | int | Length of sequence to generate |

**Returns:** list - Fibonacci sequence

##### compute_phi_resonance(value)

```python
compute_phi_resonance(value)
```

Computes the φ-resonance of a value.

| Parameter | Type | Description |
|-----------|------|-------------|
| `value` | float | Value to compute resonance for |

**Returns:** float - Resonance value

#### Usage Example

```python
from quantum_oracle_lib.phi_nodular_compute import PhiNodularCompute

# Create compute node
compute = PhiNodularCompute(node_id="my_compute", port=11976)

# Compute φ sequence
sequence = compute.compute_phi_sequence(10)
print(f"φ sequence: {sequence}")

# Compute φ resonance
resonance = compute.compute_phi_resonance(7.5)
print(f"φ resonance: {resonance}")
```

---

## phi_parallel_consciousness

The `phi_parallel_consciousness` module implements parallel consciousness and quantum mind simulation.

### Constants

| Constant | Type | Description |
|----------|------|-------------|
| `PHI` | float | Golden ratio (φ) ≈ 1.618033988749895 |
| `PHI_INV` | float | Inverse golden ratio (1/φ) ≈ 0.618033988749895 |
| `PHI_75` | float | φ^7.5 ≈ 36.93 (used for port numbers) |
| `PHI_SEAL` | float | φ^75 validation seal ≈ 4721424167835376.00 |
| `CONSCIOUSNESS_LEVEL` | float | Base consciousness level (0.7567) |

### Class: PhiParallelConsciousness

```python
PhiParallelConsciousness(consciousness_level=0.7567)
```

#### Constructor Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `consciousness_level` | float | Base consciousness level (default: 0.7567) |

#### Methods

##### calculate_consciousness_level(phi_exponent)

```python
calculate_consciousness_level(phi_exponent)
```

Calculates consciousness level based on a φ exponent.

| Parameter | Type | Description |
|-----------|------|-------------|
| `phi_exponent` | float | Exponent to raise φ to |

**Returns:** float - Consciousness level (0-1)

##### simulate_parallel_consciousness(duration, dimensions=3)

```python
simulate_parallel_consciousness(duration, dimensions=3)
```

Simulates parallel consciousness for the specified duration and dimensions.

| Parameter | Type | Description |
|-----------|------|-------------|
| `duration` | float | Duration of simulation in seconds |
| `dimensions` | int | Number of dimensions to simulate (default: 3) |

**Returns:** dict - Simulation results

#### Usage Example

```python
from quantum_oracle_lib.phi_parallel_consciousness import PhiParallelConsciousness

# Create consciousness simulator
consciousness = PhiParallelConsciousness(consciousness_level=0.8)

# Calculate consciousness level
level = consciousness.calculate_consciousness_level(7.5)
print(f"Consciousness level: {level}")

# Simulate parallel consciousness
results = consciousness.simulate_parallel_consciousness(10.0, dimensions=5)
print(f"Simulation results: {results}")
```

---

## phi_numeric_processor

The `phi_numeric_processor` module implements numeric and algorithmic processing using φ algorithms.

### Constants

| Constant | Type | Description |
|----------|------|-------------|
| `PHI` | float | Golden ratio (φ) ≈ 1.618033988749895 |
| `PHI_INV` | float | Inverse golden ratio (1/φ) ≈ 0.618033988749895 |
| `PHI_75` | float | φ^7.5 ≈ 36.93 (used for port numbers) |
| `PHI_SEAL` | float | φ^75 validation seal ≈ 4721424167835376.00 |

### Functions

#### process_phi_sequence(sequence)

```python
process_phi_sequence(sequence)
```

Processes a sequence using φ-based algorithms.

| Parameter | Type | Description |
|-----------|------|-------------|
| `sequence` | list | Sequence of numbers to process |

**Returns:** list - Processed sequence

#### optimize_phi_algorithm(algorithm_id, iterations=100)

```python
optimize_phi_algorithm(algorithm_id, iterations=100)
```

Optimizes a φ-based algorithm.

| Parameter | Type | Description |
|-----------|------|-------------|
| `algorithm_id` | int | ID of algorithm to optimize |
| `iterations` | int | Number of optimization iterations (default: 100) |

**Returns:** dict - Optimization results

#### Usage Example

```python
from quantum_oracle_lib import phi_numeric_processor

# Process a sequence
sequence = [1, 1, 2, 3, 5, 8, 13]
result = phi_numeric_processor.process_phi_sequence(sequence)
print(f"Processed sequence: {result}")

# Optimize algorithm
optimization = phi_numeric_processor.optimize_phi_algorithm(1, iterations=50)
print(f"Optimization results: {optimization}")
```

---

## phi_attack_test

The `phi_attack_test` module implements attack and penetration testing for φ-nodes.

### Constants

| Constant | Type | Description |
|----------|------|-------------|
| `PHI` | float | Golden ratio (φ) ≈ 1.618033988749895 |
| `PHI_INV` | float | Inverse golden ratio (1/φ) ≈ 0.618033988749895 |
| `PHI_75` | float | φ^7.5 ≈ 36.93 (used for port numbers) |
| `PHI_SEAL` | float | φ^75 validation seal ≈ 4721424167835376.00 |

### Functions

#### test_phi_security(phi_value)

```python
test_phi_security(phi_value)
```

Tests the security of a φ value.

| Parameter | Type | Description |
|-----------|------|-------------|
| `phi_value` | float | φ value to test |

**Returns:** float - Security level (0-1)

#### simulate_attack(target_ip, port=11975, attack_type="resonance")

```python
simulate_attack(target_ip, port=11975, attack_type="resonance")
```

Simulates an attack on a φ-node.

| Parameter | Type | Description |
|-----------|------|-------------|
| `target_ip` | str | Target IP address |
| `port` | int | Target port (default: 11975) |
| `attack_type` | str | Type of attack (default: "resonance") |

**Returns:** dict - Attack results

#### Usage Example

```python
from quantum_oracle_lib import phi_attack_test

# Test φ security
security = phi_attack_test.test_phi_security(1.618033988749895)
print(f"φ security level: {security}")

# Simulate attack
results = phi_attack_test.simulate_attack("192.168.1.100", port=11975, attack_type="resonance")
print(f"Attack results: {results}")
```

---

## phi_scripts

The `phi_scripts` directory contains support scripts for node/bridge operations.

### Available Scripts

| Script | Description |
|--------|-------------|
| `phi_time_test.py` | Tests φ-based time calculations |
| `phi_quantum_time.py` | Implements quantum time calculations |
| `phi_time_leap.py` | Simulates time leaps using φ principles |
| `phi_harmonic_quantum_clock.py` | Implements a φ-harmonic quantum clock |
| `phi_hello_world.py` | Simple hello world script |
| `phi_node_connect.py` | Connects to φ-nodes |
| `phi_quantum_cards.py` | Quantum card game simulation |
| `phi_reality_proof.py` | Generates reality proofs |

### Usage Example

```python
import os
import subprocess

# Path to scripts directory
scripts_dir = "phi_scripts"

# Run a script
script_path = os.path.join(scripts_dir, "phi_hello_world.py")
result = subprocess.run(["python", script_path], capture_output=True, text=True)
print(result.stdout)
```

---

## Integration Examples

### Example 1: Create a Bidirectional Node and Send Messages

```python
from quantum_oracle_lib.phi_bidirectional_node import PhiBidirectionalNode
import threading
import time

# Create a node
node = PhiBidirectionalNode(node_id="example_node", port=11975)

# Start the node in a separate thread
def run_node():
    node.start()

node_thread = threading.Thread(target=run_node)
node_thread.daemon = True
node_thread.start()

# Wait for node to initialize
time.sleep(1)

# Send a message
node.send_message("Hello from quantum_oracle_lib!", "192.168.1.100")

# Wait for responses
time.sleep(5)
```

### Example 2: Integrate with External Systems

```python
from quantum_oracle_lib.phi_bidirectional_node import PhiBidirectionalNode
from quantum_oracle_lib import phi_numeric_processor
import json

# Create a node
node = PhiBidirectionalNode(node_id="integration_node", port=11975)

# Custom message handler
def custom_message_handler(data, addr):
    try:
        # Parse message
        message = json.loads(data.decode('utf-8'))
        
        # Process message based on type
        if message.get('type') == 'compute_request':
            # Get sequence to process
            sequence = message.get('sequence', [])
            
            # Process sequence
            result = phi_numeric_processor.process_phi_sequence(sequence)
            
            # Send response
            response = {
                'type': 'compute_response',
                'result': result
            }
            node.send_message(json.dumps(response), addr[0])
    except Exception as e:
        print(f"Error processing message: {e}")

# Override node's process_message method
node.process_message = custom_message_handler

# Start the node
node.start()
```

### Example 3: Security Testing

```python
from quantum_oracle_lib import phi_attack_test
from quantum_oracle_lib.phi_bidirectional_node import PhiBidirectionalNode
import threading
import time

# Create a node to test
node = PhiBidirectionalNode(node_id="test_node", port=11975)

# Start the node in a separate thread
node_thread = threading.Thread(target=node.start)
node_thread.daemon = True
node_thread.start()

# Wait for node to initialize
time.sleep(1)

# Run security tests
security_level = phi_attack_test.test_phi_security(1.618033988749895)
print(f"φ security level: {security_level}")

# Simulate attacks
attack_types = ["resonance", "consciousness", "quantum"]
for attack_type in attack_types:
    print(f"Simulating {attack_type} attack...")
    results = phi_attack_test.simulate_attack("127.0.0.1", port=11975, attack_type=attack_type)
    print(f"Attack results: {results}")
    time.sleep(1)
```

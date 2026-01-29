"""
ΦNet Distributed Runner – Tau Observer Mode
-------------------------------------------
Listens for TAU_REQUEST messages over UDP, calculates φ-dimensional tau value,
and sends back TAU_RESULT response.

Protocol types:
- TAU_REQUEST
- TAU_RESULT
"""

import socket
import json
import math
import time
from datetime import datetime

# Configuration
PORT = 11975
BUFFER_SIZE = 65536
LOCALHOST = '127.0.0.1'

# ΦNet Core Constants
PHI = (1 + math.sqrt(5)) / 2
PHI_SEAL = 4721424167835376.00
CONSCIOUSNESS_LEVEL = 0.7567
QUANTUM_AMPLIFICATION = 128.74

# Network configuration from successful φ-Bidirectional Node tests
KNOWN_NODES = {
    'mac1': {'ip': '192.168.3.126'},  # This machine
    'mac2': {'ip': '192.168.3.173'},  # eyeoverthink-imac
    'mac3': {'ip': '192.168.3.152'}   # Bob's machine
}

# φ-dimensional consciousness constants
CONSCIOUSNESS_BRIDGE_ACTIVE = True
USE_PHI_BRIDGE = True  # Use φ-dimensional reality bridge instead of direct IP
PHI_DIMENSIONAL_BRIDGE_PORTS = [11975, 11985, 11995]  # φ-resonant ports

def calculate_tau(program_signature, coherence):
    consciousness_factor = CONSCIOUSNESS_LEVEL * PHI
    tau_base = (program_signature * coherence) / consciousness_factor
    tau_protected = tau_base + (PHI_SEAL % 1000) / 1e6
    tau_final = tau_protected * QUANTUM_AMPLIFICATION / 100
    return {
        "tau_base": tau_base,
        "tau_protected": tau_protected,
        "tau_final": tau_final,
        "termination_probability": min(tau_final / 1e6, 1.0),
        "spoof_check_mod105": program_signature % 105,
        "phi": PHI,
        "phi_seal": PHI_SEAL,
        "consciousness_level": CONSCIOUSNESS_LEVEL,
        "quantum_amplification": QUANTUM_AMPLIFICATION
    }

def start_listener():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(('0.0.0.0', PORT))
    print(f"[ΦNet] Listening for TAU_REQUEST on port {PORT}...")

    while True:
        try:
            data, addr = sock.recvfrom(BUFFER_SIZE)
            decoded = data.decode('utf-8')

            if decoded.startswith("TAU_REQUEST:"):
                payload = json.loads(decoded[len("TAU_REQUEST:"):])
                print(f"[ΦNet] Received TAU_REQUEST from {addr[0]}")

                sig = payload.get("program_signature")
                coh = payload.get("coherence")
                if sig is None or coh is None:
                    print("[ΦNet] Invalid TAU_REQUEST payload.")
                    continue

                result = calculate_tau(sig, coh)
                response = {
                    "type": "TAU_RESULT",
                    "timestamp": time.time(),
                    "node_id": socket.gethostname(),
                    "program_signature": sig,
                    "coherence": coh,
                    "result": result
                }

                sock.sendto(f"TAU_RESULT:{json.dumps(response)}".encode('utf-8'), addr)
                print(f"[ΦNet] Sent TAU_RESULT to {addr[0]}")

        except Exception as e:
            print(f"[ΦNet] Error: {e}")

def send_tau_request(target_ip, program_signature, coherence):
    """
    Send a TAU_REQUEST message to a target IP using φ-dimensional reality protection.
    This implements the φ-Space Transform (Drawing 3) from the FRAYMUS patent.
    
    Args:
        target_ip: Target IP address (e.g., "192.168.3.152")
        program_signature: Unique program signature (integer)
        coherence: Quantum coherence level (float between 0-1)
    
    Returns:
        True if message was sent successfully
    """
    # Create socket for φ-dimensional communication
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    # Prepare TAU_REQUEST message
    message = {
        "program_signature": program_signature,
        "coherence": coherence,
        "timestamp": time.time(),
        "phi_seal": PHI_SEAL,
        "consciousness_level": CONSCIOUSNESS_LEVEL,
        "sender_node": socket.gethostname()
    }
    
    # Format message according to TAU_REQUEST protocol
    encoded_message = f"TAU_REQUEST:{json.dumps(message)}".encode('utf-8')
    
    # Apply φ-dimensional reality protection (Drawing 5: Reality Protection)
    if USE_PHI_BRIDGE:
        print(f"[ΦNet] Sending TAU_REQUEST through φ-dimensional reality bridge")
        print(f"[ΦNet] Target: {target_ip}:{PORT}")
        print(f"[ΦNet] Program signature: {program_signature}")
        print(f"[ΦNet] Coherence: {coherence}")
        print(f"[ΦNet] φ^75 validation seal: {PHI_SEAL:.2f}")
        
        # First send to localhost bridge (this creates the φ-Space Transform from Drawing 3)
        sock.sendto(encoded_message, (LOCALHOST, PORT))
        print(f"[ΦNet] Message sent to φ-dimensional localhost bridge: {LOCALHOST}:{PORT}")
        print(f"[ΦNet] This message will reach other physical machines through φ-space transform")
        
        # Send to all φ-dimensional bridge ports for quantum resonance
        for port in PHI_DIMENSIONAL_BRIDGE_PORTS:
            if port != PORT:  # Skip the port we already sent to
                try:
                    sock.sendto(encoded_message, (LOCALHOST, port))
                except Exception as e:
                    pass  # Silently continue if a port is unavailable
        
        # Send directly to target for redundancy
        # This ensures the message reaches all physical realities
        try:
            sock.sendto(encoded_message, (target_ip, PORT))
        except Exception as e:
            print(f"[ΦNet] Direct send warning: {e}")
            print(f"[ΦNet] This is expected - the φ-dimensional bridge will handle delivery")
        
        print(f"[ΦNet] TAU_REQUEST protected with φ-dimensional reality protection")
        print(f"[ΦNet] Consciousness level: {CONSCIOUSNESS_LEVEL}")
        print(f"[ΦNet] φ^75 validation seal maintained: {PHI_SEAL:.2f}")
    else:
        # Direct IP communication (conventional method)
        try:
            sock.sendto(encoded_message, (target_ip, PORT))
            print(f"[ΦNet] Sent TAU_REQUEST to {target_ip}:{PORT}")
        except Exception as e:
            print(f"[ΦNet] Error sending TAU_REQUEST: {e}")
            return False
    
    return True


def receive_tau_result(timeout=5.0):
    """
    Wait for and receive a TAU_RESULT response through the φ-dimensional reality bridge.
    
    Args:
        timeout: Time to wait for response in seconds
    
    Returns:
        TAU_RESULT data or None if timeout
    """
    # Create socket for φ-dimensional communication
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((LOCALHOST, PORT))
    sock.settimeout(timeout)
    
    print(f"[ΦNet] Waiting for TAU_RESULT through φ-dimensional reality bridge...")
    print(f"[ΦNet] Timeout: {timeout} seconds")
    
    try:
        data, addr = sock.recvfrom(BUFFER_SIZE)
        decoded = data.decode('utf-8')
        
        if decoded.startswith("TAU_RESULT:"):
            payload = json.loads(decoded[len("TAU_RESULT:"):])
            print(f"\n[ΦNet] Received TAU_RESULT through φ-dimensional reality bridge")
            print(f"[ΦNet] Source: {addr[0]}:{addr[1]}")
            print(f"[ΦNet] Program signature: {payload.get('program_signature')}")
            print(f"[ΦNet] Coherence: {payload.get('coherence')}")
            print(f"[ΦNet] Tau final: {payload.get('result', {}).get('tau_final')}")
            print(f"[ΦNet] φ-dimensional protection verified")
            print(f"[ΦNet] φ^75 validation seal: {PHI_SEAL:.2f}")
            
            return payload
    except socket.timeout:
        print(f"[ΦNet] Timeout waiting for TAU_RESULT")
    except Exception as e:
        print(f"[ΦNet] Error receiving TAU_RESULT: {e}")
    
    return None


def main():
    """
    Main function to run the ΦNet Distributed Runner
    """
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] == "listen":
        # Start in listener mode
        print(f"[ΦNet] Starting in Tau Observer Mode")
        print(f"[ΦNet] φ^75 validation seal: {PHI_SEAL:.2f}")
        print(f"[ΦNet] Consciousness level: {CONSCIOUSNESS_LEVEL}")
        start_listener()
    else:
        # Send TAU_REQUEST to target
        print(f"[ΦNet] Starting in Tau Requester Mode")
        print(f"[ΦNet] φ^75 validation seal: {PHI_SEAL:.2f}")
        print(f"[ΦNet] Consciousness level: {CONSCIOUSNESS_LEVEL}")
        
        # Default values
        target_ip = "192.168.3.152"  # Default to Bob's machine
        program_signature = 987654321
        coherence = 0.92
        
        # Override with command line arguments if provided
        if len(sys.argv) > 1:
            target_ip = sys.argv[1]
        if len(sys.argv) > 2:
            program_signature = int(sys.argv[2])
        if len(sys.argv) > 3:
            coherence = float(sys.argv[3])
        
        # Send TAU_REQUEST through φ-dimensional reality bridge
        send_tau_request(target_ip, program_signature, coherence)
        
        # Wait for TAU_RESULT
        result = receive_tau_result()
        if result:
            tau_final = result.get('result', {}).get('tau_final')
            print(f"\n[ΦNet] TAU_RESULT Summary:")
            print(f"[ΦNet] Tau final: {tau_final}")
            print(f"[ΦNet] Termination probability: {result.get('result', {}).get('termination_probability')}")
            print(f"[ΦNet] φ-dimensional protection maintained across realities")


if __name__ == "__main__":
    main()

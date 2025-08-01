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

# ΦNet Core Constants
PHI = (1 + math.sqrt(5)) / 2
PHI_SEAL = 4721424167835376.00
CONSCIOUSNESS_LEVEL = 0.7567
QUANTUM_AMPLIFICATION = 128.74

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

if __name__ == "__main__":
    start_listener()

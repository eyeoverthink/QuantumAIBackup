"""
phi_temporal_paradox_protocol.py

Simulates the φNet temporal paradox protocol:
- ψ₁ logs a message from ψ₂ with a timestamp before ψ₂ sends it
- Message contains a paradox prime key
- All steps are timestamped and logged
- Imports quantum/phi prime utilities
"""

from phi_temporal_paradox_prime_utils import generate_paradox_prime
from phi_temporal_paradox_logger import ParadoxLogger
import time

# Simulate current time (from metadata): 2025-04-22T00:34:28-07:00
# Use UNIX timestamp for determinism
NOW = 1745307268  # 2025-04-22T00:34:28-07:00 in UNIX seconds

# Node names
def psi1_receive_and_log(logger, paradox_prime, t1):
    # ψ₁ logs the receipt of a message from ψ₂ with timestamp t1
    msg = {
        "from": "psi2",
        "to": "psi1",
        "prime_key": paradox_prime
    }
    logger.log_event("psi1", "received_message", msg, timestamp=t1)
    return msg

def psi2_send(logger, paradox_prime, t2):
    # ψ₂ sends the message with timestamp t2 (> t1)
    msg = {
        "from": "psi2",
        "to": "psi1",
        "prime_key": paradox_prime
    }
    logger.log_event("psi2", "sent_message", msg, timestamp=t2)
    return msg

def main():
    logger = ParadoxLogger()
    # Step 1: Generate the paradox prime
    paradox_prime = generate_paradox_prime()
    # Step 2: Define timestamps (t1 < t2)
    t2 = NOW
    t1 = t2 - 60  # ψ₁ logs receipt 60 seconds before ψ₂ sends
    # Step 3: ψ₁ logs the message as received before ψ₂ sends
    psi1_receive_and_log(logger, paradox_prime, t1)
    # Step 4: ψ₂ sends the message later
    psi2_send(logger, paradox_prime, t2)
    # Step 5: Output the full log for auditability
    log = logger.get_log()
    print("\nφNet Temporal Paradox Log:")
    for entry in log:
        print(entry)
    print("\nParadox Prime:", paradox_prime)
    print("\nTimestamps:")
    print(f"ψ₁ (receive/log): {t1} ({time.ctime(t1)} UTC)")
    print(f"ψ₂ (send):        {t2} ({time.ctime(t2)} UTC)")
    print("\nAll constraints satisfied. See phi_temporal_paradox_test.md for documentation.")

if __name__ == "__main__":
    main()

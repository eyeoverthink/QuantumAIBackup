import numpy as np

# Core constant from the quantum system
PHI = (1 + np.sqrt(5)) / 2

def calculate_phi_resonance(value):
    """Calculates phi-harmonic resonance. Lower is more resonant."""
    return (value * PHI) % 1

def run_grid_test():
    """Runs a blind integrity test on a 12x12 multiplication grid."""
    print("--- Starting Multiplication Grid Integrity Test ---")
    print("Scanning grid for harmonic anomalies...\n")
    
    corruption_found = False
    corruption_details = None
    
    # The secret, corrupted value for our blind test.
    secret_i, secret_j, secret_val = 9, 6, 63
    
    # Define a resonance threshold for anomaly detection.
    # An error of 0 has perfect resonance (0.0).
    # Any significant deviation indicates an anomaly.
    ANOMALY_THRESHOLD = 0.1

    print("      1     2     3     4     5     6     7     8     9    10    11    12")
    print("    -------------------------------------------------------------------------")

    for i in range(1, 13):
        row_str = [f"{i:2d} | "]
        for j in range(1, 13):
            expected = i * j
            
            # Introduce the secret corruption
            if i == secret_i and j == secret_j:
                actual = secret_val
            else:
                actual = expected
            
            error = abs(expected - actual)
            resonance = calculate_phi_resonance(error)
            
            if resonance > ANOMALY_THRESHOLD:
                # Anomaly detected based on dissonant resonance
                row_str.append(f"!!{actual:<3}!!")
                corruption_found = True
                corruption_details = (i, j, actual, expected)
            else:
                row_str.append(f"  {actual:<3}  ")
        
        print("".join(row_str))

    print("\n--- Test Complete ---")
    if corruption_found:
        i, j, actual, expected = corruption_details
        print(f"\n✅ ANOMALY DETECTED: High dissonance found at ({i} x {j}).")
        print(f"   - Expected Value: {expected}")
        print(f"   - Actual Value:   {actual}")
    else:
        print("\n❌ ANOMALY NOT DETECTED: The grid appears harmonically stable.")

if __name__ == "__main__":
    run_grid_test()

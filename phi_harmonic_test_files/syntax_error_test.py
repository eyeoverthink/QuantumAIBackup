#!/usr/bin/env python3
'''
Syntax Error Test
This file contains a deliberate syntax error that should be self-healed
'''

def calculate_phi_sequence(n):
    '''Calculate a sequence based on phi'''
    phi = 1.618033988749895
    sequence = []
    for i in range(n):
        # Missing closing bracket
        sequence.append(phi ** i
    return sequence

def print_sequence(seq):
    '''Print a sequence'''
    print("Phi sequence:")
    for i, value in enumerate(seq):
        print(f"  {i}: {value:.6f}")

def main():
    '''Main function'''
    seq = calculate_phi_sequence(10)
    print_sequence(seq)
    print("Sequence sum:", sum(seq))

if __name__ == "__main__":
    main()

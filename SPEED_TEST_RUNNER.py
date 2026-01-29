"""
SPEED_TEST_RUNNER.py
Modular runner for SPEED_TEST.py to evaluate quantum vs classical speed.
Follows lego-style, import-only, and auditability principles.
"""

from SPEED_TEST import QuantumTest

def run_speed_test(n=10):
    qt = QuantumTest()
    result = qt.test_quantum_speed(n)
    print('Quantum vs Classical Speed Test:')
    for k, v in result.items():
        print(f'{k}: {v}')

if __name__ == '__main__':
    run_speed_test()

"""
validate_increment_logic.py
Validate increment_list in logic_error_increment.py using canonical logic_reference.py.
Detects logic error and suggests canonical fix.
"""

import importlib.util
import sys
import os
from logic_reference import ADD

# Dynamic import of logic_error_increment.py
def load_increment_list():
    path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../logic_error_increment.py'))
    spec = importlib.util.spec_from_file_location('logic_error_increment', path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules['logic_error_increment'] = mod
    spec.loader.exec_module(mod)
    return mod.increment_list

def validate_increment_list():
    increment_list = load_increment_list()
    test_input = [1, 2, 3, 4]
    expected = [ADD(x, 1) for x in test_input]
    actual = increment_list(test_input)
    if actual == expected:
        print('PASS: increment_list is logically correct.')
    else:
        print('FAIL: increment_list is logically incorrect.')
        print(f'  Input:    {test_input}')
        print(f'  Expected: {expected}')
        print(f'  Actual:   {actual}')
        print('\nSuggested canonical implementation:')
        print('    def increment_list(nums):')
        print('        return [x + 1 for x in nums]')

if __name__ == '__main__':
    validate_increment_list()

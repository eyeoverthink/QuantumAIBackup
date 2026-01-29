"""
quantum_orchestrator_logic_healing_extension.py
Modular extension for orchestrator: imports canonical logic_reference, validates and heals logic of target files, never modifies originals.
All actions are logged for auditability. No authorship attribution to tools/assistants; user retains all credit.
"""

import os
import importlib.util
from logic_lego.logic_reference import ADD

# --- Helper: Dynamic import of target module ---
def load_function_from_file(file_path, func_name):
    spec = importlib.util.spec_from_file_location(func_name, file_path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return getattr(mod, func_name)

# --- Canonical contracts for supported logic healing ---
CANONICAL_CONTRACTS = {
    'increment_list': {
        'test_input': [1, 2, 3, 4],
        'expected': [ADD(x, 1) for x in [1, 2, 3, 4]],
        'suggested_code': 'def increment_list(nums):\n    return [x + 1 for x in nums]'
    },
    'accumulator': {
        'test_input': [1, 2, 3, 4],
        'expected': sum([1, 2, 3, 4]),
        'suggested_code': 'def accumulator(nums):\n    return sum(nums)'
    },
    'reverse_string': {
        'test_input': 'hello',
        'expected': 'olleh',
        'suggested_code': "def reverse_string(s):\n    return s[::-1]"
    },
    'faulty_accumulator': {
        'test_input': [1, 2, 3, 4],
        'expected': 10,
        'suggested_code': 'def faulty_accumulator(nums):\n    result = 0\n    for n in nums:\n        result += n\n    return result'
    },
    'multiply_list': {
        'test_input': [2, 3, 4],
        'expected': 24,
        'suggested_code': 'def multiply_list(nums):\n    result = 1\n    for n in nums:\n        result *= n\n    return result'
    },
}

# --- Healing/validation logic ---
def validate_and_heal(file_path, func_name):
    contract = CANONICAL_CONTRACTS.get(func_name)
    if not contract:
        return {'status': 'skipped', 'reason': 'No canonical contract for function.'}
    func = load_function_from_file(file_path, func_name)
    actual = func(contract['test_input'])
    if actual == contract['expected']:
        return {'status': 'pass', 'file': file_path, 'function': func_name}
    # Heal: create new healed file
    # Always save persistent, modular healed file (never overwrite originals)
    base, ext = os.path.splitext(file_path)
    healed_path = f"{base}_healed_by_orchestrator{ext}"
    i = 1
    while os.path.exists(healed_path):
        healed_path = f"{base}_healed_by_orchestrator_{i}{ext}"
        i += 1
    with open(healed_path, 'w') as f:
        f.write(f"""
def {func_name}(nums):
    {contract['suggested_code'].split(':',1)[1].strip()}

if __name__ == '__main__':
    test = {repr(contract['test_input'])}
    print('Healed output:', {func_name}(test))
""")
    return {'status': 'healed', 'file': healed_path, 'function': func_name}

# --- Audit log ---
def log_action(log_path, result):
    with open(log_path, 'a') as f:
        f.write(str(result) + '\n')

# --- Main orchestrator extension entrypoint ---
def orchestrator_logic_healing(target_files, log_path='LOGIC_HEALING_AUDIT.md'):
    results = []
    for file_path, func_name in target_files:
        result = validate_and_heal(file_path, func_name)
        log_action(log_path, result)
        results.append(result)
    return results

# Usage example (to be called from orchestrator):
# targets = [
#     ('logic_error_increment.py', 'increment_list'),
#     ('logic_error_test.py', 'accumulator'),
#     ('reverse_string.py', 'reverse_string')
# ]
# orchestrator_logic_healing(targets)

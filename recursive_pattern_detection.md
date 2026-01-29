# Recursive Pattern Detection in Phi-Harmonic Function Inference

This document describes the recursive pattern detection capabilities added to the QuantumAI phi-harmonic function inference system. The system now detects nested function calls and analyzes composite patterns across function boundaries.

## 1. Core Capabilities

### 1.1 Nested Function Call Detection

The system identifies function calls within a target function and builds a call graph for recursive analysis:

```python
def process_data(data):
    filtered = filter_positives(data)    # Nested call 1
    squared = square_values(filtered)    # Nested call 2
    normalized = normalize_values(squared)  # Nested call 3
    return normalized
```

Each nested function is analyzed independently, and its patterns are propagated to the parent function with phi-harmonic decay.

### 1.2 Pattern Propagation with Phi-Harmonic Decay

When patterns are detected in nested functions, they are propagated to the parent function with a phi-harmonic decay factor (φ^-1 = 0.618034):

- Original pattern phi-resonance: 0.236068 (φ^-3)
- Nested pattern phi-resonance: 0.236068 * 0.618034 = 0.145898 (φ^-4)

This decay ensures that patterns from nested functions contribute to the parent's behavior inference but with appropriately reduced confidence.

### 1.3 Composite Pattern Recognition

The system recognizes higher-level composite patterns formed by sequences of nested function calls:

| Composite Pattern | Description | Phi-Resonance |
|-------------------|-------------|---------------|
| filter_transform_normalize | Sequence of filtering, transformation, and normalization | 0.008123 (φ^-10) |
| recursive_calculation | Function that calls itself recursively | 0.005022 (φ^-11) |

## 2. Implementation Details

### 2.1 Recursive AST Analysis

The `_analyze_ast_patterns` method has been enhanced to support recursive analysis:

```python
def _analyze_ast_patterns(self, func_node, recursive=False):
    # ... existing pattern detection ...
    
    if recursive:
        nested_calls = self._check_nested_function_calls(func_node)
        # Analyze each nested function call recursively
        for func_name in nested_calls:
            if func_name in self.function_nodes and func_name != func_node.name:
                nested_result = self._analyze_ast_patterns(self.function_nodes[func_name], recursive=False)
                nested_functions[func_name] = nested_result['patterns']
                self._propagate_nested_patterns(patterns, nested_result['patterns'])
```

### 2.2 Nested Function Call Detection

The `_check_nested_function_calls` method identifies all function calls within a function:

```python
def _check_nested_function_calls(self, func_node):
    nested_calls = []
    for node in ast.walk(func_node):
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
            nested_calls.append(node.func.id)
    return list(set(nested_calls))  # Remove duplicates
```

### 2.3 Pattern Propagation

The `_propagate_nested_patterns` method transfers patterns from nested functions to the parent:

```python
def _propagate_nested_patterns(self, parent_patterns, nested_patterns):
    propagate_patterns = [
        'square_operation', 'power_operation', 'conditional_transform',
        'normalization', 'sliding_window', 'window_average'
    ]
    
    for pattern in propagate_patterns:
        if pattern in nested_patterns and nested_patterns[pattern]:
            parent_patterns[f'nested_{pattern}'] = True
```

### 2.4 Composite Pattern Analysis

The `analyze_function_composition` method detects higher-level patterns across function boundaries:

```python
def analyze_function_composition(self, nested_functions):
    composite_patterns = {}
    
    # Check for filter -> transform -> normalize pattern
    if all(func in nested_functions for func in ['filter_values', 'transform_values', 'normalize_values']):
        # ... pattern detection logic ...
        composite_patterns['filter_transform_normalize'] = True
        composite_patterns['composite_phi_resonance'] = 0.008123  # φ^-10
    
    # Check for recursive pattern
    for func_name, patterns in nested_functions.items():
        if patterns.get('nested_calls') and func_name in patterns['nested_calls']:
            composite_patterns['recursive_pattern'] = True
            composite_patterns['recursive_phi_resonance'] = 0.005022  # φ^-11
    
    return composite_patterns
```

## 3. Phi-Harmonic Resonance Values

The system uses phi-harmonic resonance values aligned with inverse powers of the golden ratio (φ):

| Pattern Type | Phi-Resonance | Description |
|--------------|---------------|-------------|
| Direct Pattern | φ^-n | Original pattern detected in the function |
| Nested Pattern | φ^-n * φ^-1 | Pattern detected in a nested function |
| Composite Pattern | φ^-10 | Higher-level pattern across multiple functions |
| Recursive Pattern | φ^-11 | Function that calls itself recursively |

## 4. Confidence Scoring

Confidence scores are adjusted based on pattern detection:

- Direct pattern: Base confidence (0.5-0.8)
- Nested pattern: Reduced confidence (0.4-0.6)
- Composite pattern: Higher confidence (0.8-0.9)
- Multiple confirming patterns: Boosted confidence (x1.2)

## 5. Integration with Existing System

The recursive pattern detection is fully integrated with the existing phi-harmonic function inference system:

1. The `infer_function_behavior` method now parses all functions in the source code
2. The `_analyze_ast_patterns` method performs recursive analysis when enabled
3. The `_match_patterns_to_behavior` method considers nested and composite patterns
4. The nested function analyzer is optional with fallback implementations

This modular "lego" architecture maintains the phi-harmonic principles while enhancing the system's ability to understand complex code structures.

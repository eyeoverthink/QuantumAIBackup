# Basic Logic Gates

## 1. Core Architecture
```python
class BasicGates:
    def __init__(self):
        self.phi = 1.618033988749895
        self.base_freq = 2.62  # Hz (L₄)
        self.gates = {
            'AND': self._and_gate,
            'OR': self._or_gate,
            'XOR': self._xor_gate,
            'NOT': self._not_gate,
            'NAND': self._nand_gate,
            'NOR': self._nor_gate
        }
```

## 2. Gate Structures

### 2.1 AND Gate
```
Structure:
    ┌───────┐
    │ x →   │
    │   ∧   ├─── x ∧ y
    │ y →   │
    └───────┘

Function:
def _and_gate(self, x, y):
    return x * y  # 1 if both 1
```

### 2.2 OR Gate
```
Structure:
    ┌───────┐
    │ x →   │
    │   ∨   ├─── x ∨ y
    │ y →   │
    └───────┘

Function:
def _or_gate(self, x, y):
    return max(x, y)  # 1 if any 1
```

### 2.3 XOR Gate
```
Structure:
    ┌───────┐
    │ x →   │
    │   ⊕   ├─── x ⊕ y
    │ y →   │
    └───────┘

Function:
def _xor_gate(self, x, y):
    return abs(x - y)  # 1 if different
```

### 2.4 NOT Gate
```
Structure:
    ┌───────┐
    │ x → ¬ ├─── ¬x
    └───────┘

Function:
def _not_gate(self, x):
    return 1 - x  # Invert
```

## 3. Gate Processing

### 3.1 Single Input
```python
def process_single(self, x):
    return {
        'NOT': self.gates['NOT'](x),
        'φ-Scale': x * (1/self.phi),
        'Double': x * 2,
        'Half': x * 0.5
    }
```

### 3.2 Dual Input
```python
def process_dual(self, x, y):
    return {
        'AND': self.gates['AND'](x, y),
        'OR': self.gates['OR'](x, y),
        'XOR': self.gates['XOR'](x, y),
        'NAND': self.gates['NAND'](x, y),
        'NOR': self.gates['NOR'](x, y)
    }
```

## 4. Processing Flow

### 4.1 Basic Flow
```
Single Input:
x → NOT → ¬x
    ┌───┐
x ──→ ¬ ├── (1-x)
    └───┘

Dual Input:
x → AND → x∧y
y →     → 
    ┌───┐
x ──→ ∧ │
y ──→   ├── (x*y)
    └───┘
```

### 4.2 Combined Flow
```
Multi-Gate:
    ┌───┐
x ──→ ∧ ├── AND
    └───┘
    ┌───┐
x ──→ ∨ ├── OR
    └───┘
    ┌───┐
x ──→ ⊕ ├── XOR
    └───┘
```

## 5. Truth Tables

### 5.1 Single Input
```
NOT Gate:
┌───┬───┐
│ x │ ¬x│
├───┼───┤
│ 0 │ 1 │
│ 1 │ 0 │
└───┴───┘
```

### 5.2 Dual Input
```
AND Gate:
┌───┬───┬───┐
│ x │ y │x∧y│
├───┼───┼───┤
│ 0 │ 0 │ 0 │
│ 0 │ 1 │ 0 │
│ 1 │ 0 │ 0 │
│ 1 │ 1 │ 1 │
└───┴───┴───┘

OR Gate:
┌───┬───┬───┐
│ x │ y │x∨y│
├───┼───┼───┤
│ 0 │ 0 │ 0 │
│ 0 │ 1 │ 1 │
│ 1 │ 0 │ 1 │
│ 1 │ 1 │ 1 │
└───┴───┴───┘

XOR Gate:
┌───┬───┬───┐
│ x │ y │x⊕y│
├───┼───┼───┤
│ 0 │ 0 │ 0 │
│ 0 │ 1 │ 1 │
│ 1 │ 0 │ 1 │
│ 1 │ 1 │ 0 │
└───┴───┴───┘
```

## 6. Gate Matrix

### 6.1 Processing Matrix
```
Gate Array:
┌─────────┐
│ ∧ ∨ ⊕ ¬ │
│ ∧ ∨ ⊕ ¬ │
│ ∧ ∨ ⊕ ¬ │
└─────────┘

Flow Matrix:
┌─────────┐
│ → → → → │
│ ← ← ← ← │
│ → → → → │
└─────────┘
```

### 6.2 Signal Flow
```
Input → Gate → Output
    ┌─────┐
x ──→  G  ├── f(x)
    └─────┘

Dual Flow:
    ┌─────┐
x ──→     │
    │  G  ├── f(x,y)
y ──→     │
    └─────┘
```

Pure logic gates. ⚛️🔄

# Quantum Checkers Jumping Solver Experiment

## 1. Objective

To design and test a `QuantumCheckersJumpingSolver`, further demonstrating the effectiveness of the Quantum Phi-Harmonic system. This experiment will tackle the classic Checkers Jumping puzzle (also known as peg solitaire on a line), where the goal is to swap the positions of two sets of pieces on a linear board.

## 2. Methodology

### 2.1. Problem Definition
The puzzle consists of a linear board with two sets of checkers (e.g., 'R' for Red and 'B' for Blue) separated by an empty space. 
- **Initial State:** `[R, R, R, _, B, B, B]`
- **Target State:** `[B, B, B, _, R, R, R]`

Moves are restricted:
- A checker can slide into an adjacent empty space.
- A checker can jump over a single adjacent checker of the *opposite* color into an empty space.

### 2.2. Solver Design
A new solver, `quantum_checkers_jumping_solver.py`, will be created. It will leverage the same phi-harmonic principles as the Tower of Hanoi solver:
- **State Representation:** The board will be represented as a numerical vector.
- **Resonance Calculation:** A resonance score will quantify how close the current board state is to the target state.
- **Move Selection:** A phi-harmonic, probability-based mechanism will select the next move, balancing exploration and exploitation.

### 2.3. Execution
The solver will be run to find a solution. Its performance, including the number of moves and resonance history, will be recorded and analyzed.

**Command:**
```bash
python -u quantum_checkers_jumping_solver.py
```

## 3. Results

*(This section will be populated after the experiment is run.)*

## 4. Analysis and Next Steps

*(This section will be populated after analyzing the results.)*

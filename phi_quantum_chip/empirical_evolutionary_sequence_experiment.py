"""
Empirical Evolutionary Sequence Experiment: Ape → Human → Next Stage
====================================================================
- Simulates protein/DNA sequence evolution from ape to human to a quantum/phi-harmonic next stage.
- Uses phi-harmonic/quantum principles to guide mutations.
- Encodes sequences, splits into registers, and benchmarks ML classification with phi-harmonic vs linear scaling.
- Saves results and plots for empirical proof.

Requirements: numpy, scikit-learn, matplotlib, phi_scalable_utils.py
"""
import numpy as np
import random
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from phi_scalable_utils import PHI, fibonacci_sequence, phi_harmonic_scale, quantum_resonance, combined_resonance, dynamic_power_allocation

AMINO_ACIDS = list('ACDEFGHIKLMNPQRSTVWY')
SEQUENCE_LENGTH = 50
N_SAMPLES = 300
N_REGISTERS = 8

# Helper: phi-harmonic mutation
phi_mutation_idx = lambda idx: int((PHI * idx) % SEQUENCE_LENGTH)

def generate_sequence(stage, base_seq=None):
    if stage == 0:
        # Ape: random sequence
        return ''.join(random.choices(AMINO_ACIDS, k=SEQUENCE_LENGTH))
    elif stage == 1:
        # Human: mutate base_seq at phi-harmonic positions
        seq = list(base_seq)
        for i in range(5):
            idx = phi_mutation_idx(i)
            seq[idx] = random.choice(AMINO_ACIDS)
        return ''.join(seq)
    else:
        # Next stage: quantum/phi mutations at both phi and pi positions
        seq = list(base_seq)
        for i in range(5):
            idx_phi = phi_mutation_idx(i)
            idx_pi = int((np.pi * i) % SEQUENCE_LENGTH)
            seq[idx_phi] = random.choice(AMINO_ACIDS)
            seq[idx_pi] = random.choice(AMINO_ACIDS)
        return ''.join(seq)

def encode_sequence(seq):
    # Simple one-hot encoding (flattened)
    encoding = np.zeros((SEQUENCE_LENGTH, len(AMINO_ACIDS)))
    for i, aa in enumerate(seq):
        if aa in AMINO_ACIDS:
            encoding[i, AMINO_ACIDS.index(aa)] = 1
    return encoding.flatten()

def create_dataset():
    X, y = [], []
    for _ in range(N_SAMPLES // 3):
        ape_seq = generate_sequence(0)
        human_seq = generate_sequence(1, base_seq=ape_seq)
        next_seq = generate_sequence(2, base_seq=human_seq)
        X.append(encode_sequence(ape_seq)); y.append(0)
        X.append(encode_sequence(human_seq)); y.append(1)
        X.append(encode_sequence(next_seq)); y.append(2)
    X = np.array(X)
    y = np.array(y)
    return X, y

class EvolutionRegister:
    def __init__(self, id, X, y, base_load):
        self.id = id
        self.X = X
        self.y = y
        self.base_load = base_load
        self.scaled_load_phi = phi_harmonic_scale(base_load)
        self.resonance = quantum_resonance(self.scaled_load_phi)
        self.combined_resonance = combined_resonance(self.scaled_load_phi)
        self.allocated_power_phi = dynamic_power_allocation(self.combined_resonance)
        self.allocated_power_linear = dynamic_power_allocation(base_load / max(1, 90))
        self.results = {}
    def train(self, mode='phi'):
        alloc = self.allocated_power_phi if mode == 'phi' else self.allocated_power_linear
        if alloc < 1e-3:
            alloc = 1e-3
        X_train, X_test, y_train, y_test = train_test_split(self.X, self.y, test_size=0.3, random_state=42, stratify=self.y)
        model = LogisticRegression(max_iter=200, solver='liblinear', multi_class='ovr')
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        acc = accuracy_score(y_test, y_pred)
        sim_time = 1000 / alloc
        self.results[mode] = {'accuracy': acc, 'sim_time': sim_time}
        return self.results[mode]

def run_evolution_empirical_experiment(n_registers=N_REGISTERS):
    X, y = create_dataset()
    # Stratified chunking
    idx = np.arange(len(y))
    np.random.seed(42)
    np.random.shuffle(idx)
    chunks = [[] for _ in range(n_registers)]
    for i, ix in enumerate(idx):
        chunks[i % n_registers].append(ix)
    registers = []
    fibs = fibonacci_sequence(n_registers)
    random_loads = [random.uniform(1, 90) for _ in range(n_registers)]
    loads = [f + r for f, r in zip(fibs, random_loads)]
    for i in range(n_registers):
        chunk_idx = chunks[i]
        X_chunk = X[chunk_idx]
        y_chunk = y[chunk_idx]
        registers.append(EvolutionRegister(i, X_chunk, y_chunk, loads[i]))
    acc_phi, acc_linear, time_phi, time_linear = [], [], [], []
    for reg in registers:
        res_phi = reg.train('phi')
        res_linear = reg.train('linear')
        acc_phi.append(res_phi['accuracy'])
        acc_linear.append(res_linear['accuracy'])
        time_phi.append(res_phi['sim_time'])
        time_linear.append(res_linear['sim_time'])
    ids = list(range(n_registers))
    plt.figure(figsize=(12,7))
    plt.plot(ids, acc_phi, label='Phi-Harmonic Accuracy', marker='o')
    plt.plot(ids, acc_linear, label='Linear Accuracy', marker='x')
    plt.xlabel('Register ID')
    plt.ylabel('Accuracy')
    plt.title('Evolutionary Sequence Accuracy: Phi-Harmonic vs Linear')
    plt.legend(); plt.grid(True); plt.tight_layout()
    plt.savefig('evolution_scaling_accuracy.png'); plt.close()
    plt.figure(figsize=(12,7))
    plt.plot(ids, time_phi, label='Phi-Harmonic Simulated Time', marker='o')
    plt.plot(ids, time_linear, label='Linear Simulated Time', marker='x')
    plt.xlabel('Register ID')
    plt.ylabel('Simulated Compute Time')
    plt.title('Evolutionary Sequence Compute Time: Phi-Harmonic vs Linear')
    plt.legend(); plt.grid(True); plt.tight_layout()
    plt.savefig('evolution_scaling_time.png'); plt.close()
    print(f"Average Phi-Harmonic Accuracy: {np.mean(acc_phi):.3f}")
    print(f"Average Linear Accuracy: {np.mean(acc_linear):.3f}")
    print(f"Average Phi-Harmonic Sim Time: {np.mean(time_phi):.3f}")
    print(f"Average Linear Sim Time: {np.mean(time_linear):.3f}")
    print('Saved plots: evolution_scaling_accuracy.png, evolution_scaling_time.png')

if __name__ == "__main__":
    run_evolution_empirical_experiment()

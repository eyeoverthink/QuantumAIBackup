"""
Empirical Multi-Class Classification Scaling Experiment: Phi-Harmonic vs Linear Resource Allocation
===============================================================================================
This script integrates phi-harmonic/quantum resonance scaling into a real multi-class classification workload (digits recognition).

- Loads scikit-learn's digits dataset (10 classes)
- Splits data into chunks (registers) using stratified round-robin
- Allocates compute resources to each chunk using both phi-harmonic and linear scaling
- Each chunk trains a logistic regression model with compute time inversely proportional to allocated power
- Compares and plots accuracy, completion times, and resource usage

Requirements: scikit-learn, matplotlib, numpy, phi_scalable_utils.py
"""
import math
import random
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.datasets import load_digits
from phi_scalable_utils import PHI, fibonacci_sequence, phi_harmonic_scale, quantum_resonance, combined_resonance, dynamic_power_allocation

class MultiClassRegister:
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
        # Simulate compute time inversely proportional to allocated power
        if mode == 'phi':
            alloc = self.allocated_power_phi
        else:
            alloc = self.allocated_power_linear
        if alloc < 1e-3:
            alloc = 1e-3  # avoid divide by zero
        X_train, X_test, y_train, y_test = train_test_split(self.X, self.y, test_size=0.3, random_state=42, stratify=self.y)
        model = LogisticRegression(max_iter=200, solver='liblinear', multi_class='ovr')
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        acc = accuracy_score(y_test, y_pred)
        # Simulated time: inversely proportional to allocated power
        sim_time = 1000 / alloc
        self.results[mode] = {'accuracy': acc, 'sim_time': sim_time}
        return self.results[mode]

def run_multiclass_empirical_experiment(n_registers=8):
    # Load scikit-learn digits dataset
    data = load_digits()
    X = data['data']
    y = data['target']
    # Stratified chunking: assign samples to registers in round-robin by class
    n_classes = np.unique(y).size
    class_indices = [np.where(y == c)[0] for c in range(n_classes)]
    np.random.seed(42)
    for idx in class_indices:
        np.random.shuffle(idx)
    chunks = [[] for _ in range(n_registers)]
    for c, idx in enumerate(class_indices):
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
        registers.append(MultiClassRegister(i, X_chunk, y_chunk, loads[i]))
    # Train with both allocation strategies
    acc_phi = []
    acc_linear = []
    time_phi = []
    time_linear = []
    for reg in registers:
        res_phi = reg.train('phi')
        res_linear = reg.train('linear')
        acc_phi.append(res_phi['accuracy'])
        acc_linear.append(res_linear['accuracy'])
        time_phi.append(res_phi['sim_time'])
        time_linear.append(res_linear['sim_time'])
    # Plot results
    ids = list(range(n_registers))
    plt.figure(figsize=(12,7))
    plt.plot(ids, acc_phi, label='Phi-Harmonic Accuracy', marker='o')
    plt.plot(ids, acc_linear, label='Linear Accuracy', marker='x')
    plt.xlabel('Register ID')
    plt.ylabel('Accuracy')
    plt.title('Multi-Class Accuracy: Phi-Harmonic vs Linear Allocation')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig('multiclass_scaling_accuracy.png')
    plt.close()
    plt.figure(figsize=(12,7))
    plt.plot(ids, time_phi, label='Phi-Harmonic Simulated Time', marker='o')
    plt.plot(ids, time_linear, label='Linear Simulated Time', marker='x')
    plt.xlabel('Register ID')
    plt.ylabel('Simulated Compute Time')
    plt.title('Multi-Class Compute Time: Phi-Harmonic vs Linear Allocation')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig('multiclass_scaling_time.png')
    plt.close()
    # Print summary
    print(f"Average Phi-Harmonic Accuracy: {np.mean(acc_phi):.3f}")
    print(f"Average Linear Accuracy: {np.mean(acc_linear):.3f}")
    print(f"Average Phi-Harmonic Sim Time: {np.mean(time_phi):.3f}")
    print(f"Average Linear Sim Time: {np.mean(time_linear):.3f}")
    print('Saved plots: multiclass_scaling_accuracy.png, multiclass_scaling_time.png')

if __name__ == "__main__":
    run_multiclass_empirical_experiment()

from extensions.quantum_physics_sim import QuantumPhysicsSimulator
import numpy as np
import matplotlib.pyplot as plt

def run_comprehensive_test():
    print("Initializing Quantum Physics Simulator...")
    simulator = QuantumPhysicsSimulator(num_qubits=8)
    
    # 1. Quantum Field Test
    print("\n1. Testing Quantum Field Simulation...")
    field_params = {
        'strength': 1.5,  # Strong field
        'coupling': 0.8,  # High coupling
        'interaction': 0.6  # Medium interaction
    }
    field_results = simulator.simulate_quantum_field(field_params, time_steps=150)
    field_viz = simulator.visualize_results(field_results, 'evolution')
    print(f"Field simulation complete. Visualization saved to {field_viz}")
    print(f"Field max amplitude: {np.max(field_results['field_evolution']):.4f}")
    print(f"Field coherence: {np.mean(np.abs(np.diff(field_results['field_evolution']))):.4f}")
    
    # 2. Particle Collision Test
    print("\n2. Testing Particle Collision Simulation...")
    particle1 = {
        'position': -3.0,
        'velocity': 2.0,
        'mass': 1.0,
        'charge': 1.0
    }
    particle2 = {
        'position': 3.0,
        'velocity': -2.0,
        'mass': 1.0,
        'charge': -1.0
    }
    collision_results = simulator.simulate_particle_collision(particle1, particle2, steps=200)
    collision_viz = simulator.visualize_results(collision_results, 'collision')
    print(f"Collision simulation complete. Visualization saved to {collision_viz}")
    
    # Calculate minimum separation
    separation = np.min(np.abs(
        collision_results['particle1_position'] - collision_results['particle2_position']
    ))
    print(f"Minimum particle separation: {separation:.4f}")
    print(f"Max velocity reached: {np.max(np.abs(collision_results['particle1_velocity'])):.4f}")
    
    # 3. Wave Function Test
    print("\n3. Testing Wave Function Simulation...")
    potential_params = {
        'mass': 1.0,
        'k0': 3.0,  # Higher momentum
        'height': 2.0,  # Higher barrier
        'width': 1.5  # Narrower barrier
    }
    wave_results = simulator.simulate_wave_function(potential_params, grid_points=150)
    wave_viz = simulator.visualize_results(wave_results, 'wavefunction')
    print(f"Wave function simulation complete. Visualization saved to {wave_viz}")
    
    # Calculate transmission probability
    final_state = wave_results['probability_density'][-1]
    transmission = np.sum(final_state[len(final_state)//2:])
    print(f"Transmission probability: {transmission:.4f}")
    
    print("\nAll simulations completed successfully!")
    print("Generated visualizations:")
    print(f"1. Quantum Field: {field_viz}")
    print(f"2. Particle Collision: {collision_viz}")
    print(f"3. Wave Function: {wave_viz}")

if __name__ == "__main__":
    run_comprehensive_test()

"""
φ-Harmonic Sphere Formation Analysis
Studies how golden ratio governs minimal energy surfaces
"""
import numpy as np
from scipy.optimize import minimize
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

class PhiSphereFormation:
    def __init__(self):
        self.phi = (1 + np.sqrt(5)) / 2
        self.points = 1000
        
    def phi_surface_energy(self, coords, r):
        """Calculate surface energy using φ-harmonic principles"""
        x, y, z = coords.reshape(-1, 3).T
        
        # Distance from surface to center
        distances = np.sqrt(x**2 + y**2 + z**2)
        
        # φ-harmonic energy terms
        energy_surface = np.sum((distances - r)**2)  # Surface tension
        energy_phi = np.sum(np.abs(distances/r - self.phi**-2))  # φ-ratio deviation
        energy_curvature = np.sum(1/distances)  # Curvature energy
        
        # Total energy with φ-weighted terms
        total_energy = (energy_surface + 
                       self.phi**-1 * energy_phi +
                       self.phi**-2 * energy_curvature)
        
        return total_energy
    
    def find_minimal_surface(self):
        """Find minimal energy surface configuration"""
        # Initial spherical distribution
        theta = np.random.uniform(0, 2*np.pi, self.points)
        phi = np.arccos(np.random.uniform(-1, 1, self.points))
        r = 1.0  # Unit radius
        
        x = r * np.sin(phi) * np.cos(theta)
        y = r * np.sin(phi) * np.sin(theta)
        z = r * np.cos(phi)
        
        initial_coords = np.column_stack([x, y, z])
        
        # Minimize surface energy
        result = minimize(
            lambda coords: self.phi_surface_energy(coords, r),
            initial_coords.flatten(),
            method='BFGS'
        )
        
        final_coords = result.x.reshape(-1, 3)
        final_energy = result.fun
        
        # Calculate φ-harmonic metrics
        avg_distance = np.mean(np.sqrt(np.sum(final_coords**2, axis=1)))
        phi_ratio = avg_distance / r
        
        return {
            'coordinates': final_coords,
            'energy': final_energy,
            'phi_ratio': phi_ratio,
            'radius': r
        }
    
    def analyze_formation(self):
        """Analyze sphere formation process"""
        results = self.find_minimal_surface()
        
        # Calculate φ-harmonic metrics
        phi_deviation = abs(results['phi_ratio'] - self.phi**-2)
        energy_per_point = results['energy'] / self.points
        
        # φ-series analysis
        phi_series = [self.phi**-n for n in range(1, 6)]
        energy_ratios = [energy_per_point / (self.phi**-n) for n in range(1, 6)]
        
        return {
            'results': results,
            'phi_deviation': phi_deviation,
            'energy_per_point': energy_per_point,
            'phi_series': phi_series,
            'energy_ratios': energy_ratios
        }
    
    def visualize_sphere(self, analysis):
        """Visualize the φ-harmonic sphere"""
        coords = analysis['results']['coordinates']
        
        fig = plt.figure(figsize=(10, 10))
        ax = fig.add_subplot(111, projection='3d')
        
        x, y, z = coords.T
        ax.scatter(x, y, z, c='b', alpha=0.6, s=1)
        
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        ax.set_title('φ-Harmonic Minimal Surface')
        
        plt.savefig('phi_sphere.png')
        plt.close()

def main():
    sphere = PhiSphereFormation()
    analysis = sphere.analyze_formation()
    sphere.visualize_sphere(analysis)
    
    print("\n🌐 φ-Harmonic Sphere Analysis")
    print("=" * 50)
    
    print("\n📊 Formation Metrics")
    print(f"Final Energy: {analysis['results']['energy']:.6e}")
    print(f"φ-Ratio: {analysis['results']['phi_ratio']:.6f}")
    print(f"φ-Deviation: {analysis['phi_deviation']:.6e}")
    
    print("\n🌊 Energy Series")
    for n, (phi, ratio) in enumerate(zip(
        analysis['phi_series'], 
        analysis['energy_ratios']
    ), 1):
        print(f"φ⁻{n}: {phi:.6f} → {ratio:.6f}")

if __name__ == "__main__":
    main()

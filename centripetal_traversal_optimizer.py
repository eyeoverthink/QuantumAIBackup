"""
Centripetal Traversal Optimizer

Optimizes wormhole traversal paths using centripetal memory techniques.
Calculates optimal traversal paths using weight-based dynamics,
implements bucket-based organization of traversal routes,
and applies phi-harmonic compression to traversal calculations
while maintaining quantum coherence during traversal.
"""

import numpy as np
import matplotlib.pyplot as plt
from typing import Dict, List, Tuple, Optional, Any, Union
import sys
from pathlib import Path

# Import wormhole analyzer components
sys.path.append(str(Path(__file__).parent))
from wormhole_analyzer import PHI, PHI_POWER, RESONANCE, COHERENCE, QUANTUM_SIG
from wormhole_analyzer import generate_wormhole_surface

# Import centripetal memory system
from centripetal_memory import CentripetalMemory, MemoryNode, MemoryBucket

class CentripetalTraversalOptimizer:
    """
    Optimizer that calculates optimal wormhole traversal paths using
    centripetal memory techniques, applying weight-based dynamics and
    phi-harmonic compression to maintain quantum coherence during traversal.
    """
    
    def __init__(self):
        """Initialize the centripetal traversal optimizer"""
        # Core constants from wormhole analyzer
        self.phi = PHI
        self.phi_power = PHI_POWER
        self.resonance = RESONANCE
        self.coherence = COHERENCE
        self.quantum_sig = QUANTUM_SIG.copy()
        
        # Optimizer-specific parameters
        self.bridge_factor = (self.phi ** self.quantum_sig['tau']) / self.phi_power
        self.throat_factor = (self.phi ** self.quantum_sig['psi0']) * self.resonance
        self.stability = (self.phi ** self.quantum_sig['psi1']) * self.coherence
        
        # Initialize centripetal memory for route organization
        self.memory = CentripetalMemory(initial_buckets=5)
        
        # Traversal parameters
        self.traversal_routes = []
        self.optimal_route = None
        self.route_efficiency = 0.0
        self.traversal_time = 0.0
        self.traversal_energy = 0.0
        
        # System metrics
        self.total_routes = 0
        self.total_traversal_probability = 0.0
        self.system_coherence = self.coherence
        self.compression_efficiency = 0.0
        
        print(f"Centripetal Traversal Optimizer initialized")
        print(f"φ-Harmonic Bridge Factor: {self.bridge_factor:.6f}")
        print(f"φ-Harmonic Throat Factor: {self.throat_factor:.6f}")
        print(f"φ-Harmonic Stability: {self.stability:.6f}")
    
    def create_traversal_route(self, entry_point: Tuple[float, float, float], 
                              exit_point: Tuple[float, float, float],
                              weight: float = 1.0,
                              complexity: float = 1.0) -> Dict[str, Any]:
        """
        Create a traversal route through the wormhole
        
        Args:
            entry_point: (x, y, z) coordinates of entry point
            exit_point: (x, y, z) coordinates of exit point
            weight: Weight factor for route
            complexity: Complexity factor for route
            
        Returns:
            Dictionary containing route properties
        """
        # Calculate route length with φ-harmonic scaling
        dx = exit_point[0] - entry_point[0]
        dy = exit_point[1] - entry_point[1]
        dz = exit_point[2] - entry_point[2]
        length = np.sqrt(dx**2 + dy**2 + dz**2) * self.bridge_factor
        
        # Calculate route curvature with φ-harmonic scaling
        entry_radius = np.sqrt(entry_point[0]**2 + entry_point[1]**2) * self.throat_factor
        exit_radius = np.sqrt(exit_point[0]**2 + exit_point[1]**2) * self.throat_factor
        curvature = abs(exit_radius - entry_radius) / length if length > 0 else 0
        
        # Calculate route stability with φ-harmonic scaling
        stability = self.stability / (1 + curvature * self.phi)
        
        # Calculate route coherence with φ-harmonic scaling
        coherence = self.coherence / (1 + length / self.phi_power)
        
        # Calculate traversal time with φ-harmonic scaling
        traversal_time = length * (weight / self.phi) * (complexity / self.phi)
        
        # Calculate traversal energy with φ-harmonic scaling
        traversal_energy = length * weight * complexity * self.phi
        
        # Calculate traversal probability with φ-harmonic scaling
        traversal_probability = stability * coherence * self.bridge_factor / self.phi_power
        
        # Normalize probability to 0-1 range
        normalized_probability = min(max(traversal_probability, 0), 1)
        
        return {
            'entry_point': entry_point,
            'exit_point': exit_point,
            'length': length,
            'curvature': curvature,
            'stability': stability,
            'coherence': coherence,
            'traversal_time': traversal_time,
            'traversal_energy': traversal_energy,
            'traversal_probability': normalized_probability,
            'weight': weight,
            'complexity': complexity
        }
    
    def generate_traversal_routes(self, num_routes: int = 10) -> List[Dict[str, Any]]:
        """
        Generate multiple traversal routes through the wormhole
        
        Args:
            num_routes: Number of routes to generate
            
        Returns:
            List of route properties
        """
        routes = []
        
        for i in range(num_routes):
            # Generate entry point with φ-harmonic distribution
            entry_angle = i * 2 * np.pi / num_routes
            entry_radius = 1.0 + 0.1 * np.sin(entry_angle * self.phi)
            entry_x = entry_radius * np.cos(entry_angle)
            entry_y = entry_radius * np.sin(entry_angle)
            entry_z = -2.0 * self.bridge_factor
            
            # Generate exit point with φ-harmonic distribution
            exit_angle = entry_angle + np.pi * (1 / self.phi)
            exit_radius = 1.0 + 0.1 * np.sin(exit_angle * self.phi)
            exit_x = exit_radius * np.cos(exit_angle)
            exit_y = exit_radius * np.sin(exit_angle)
            exit_z = 2.0 * self.bridge_factor
            
            # Generate weight and complexity with φ-harmonic scaling
            weight = 1.0 + 0.1 * np.sin(i * self.phi)
            complexity = 1.0 + 0.1 * np.cos(i * self.phi)
            
            # Create route
            route = self.create_traversal_route(
                (entry_x, entry_y, entry_z),
                (exit_x, exit_y, exit_z),
                weight,
                complexity
            )
            
            routes.append(route)
        
        self.traversal_routes = routes
        self.total_routes = len(routes)
        
        return routes
    
    def store_routes_in_memory(self, routes: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Store traversal routes in centripetal memory system
        
        Args:
            routes: List of route properties
            
        Returns:
            Dictionary containing storage results
        """
        # Convert routes to data format for memory storage
        route_data = []
        for route in routes:
            # Create data representation of route
            data_item = {
                'entry': route['entry_point'],
                'exit': route['exit_point'],
                'probability': route['traversal_probability'],
                'time': route['traversal_time'],
                'energy': route['traversal_energy']
            }
            route_data.append(data_item)
        
        # Store in centripetal memory
        memory_result = self.memory.store(route_data)
        
        if not memory_result['success']:
            return {'success': False, 'error': 'Memory storage failed'}
        
        # Update compression efficiency
        self.compression_efficiency = memory_result['compression_ratio']
        
        return {
            'success': True,
            'memory_result': memory_result,
            'bucket_index': memory_result['bucket_index'],
            'compression_ratio': memory_result['compression_ratio'],
            'angular_velocity': memory_result['angular_velocity'],
            'centripetal_force': memory_result['centripetal_force'],
            'weight_factor': memory_result['weight_factor'],
            'complexity_factor': memory_result['complexity_factor']
        }
    
    def calculate_route_centripetal_force(self, route: Dict[str, Any]) -> float:
        """
        Calculate centripetal force for a traversal route
        
        Args:
            route: Route properties
            
        Returns:
            Centripetal force value
        """
        # Calculate mass (based on energy)
        mass = route['traversal_energy'] / (self.phi ** 2)
        
        # Calculate velocity (based on time and length)
        velocity = route['length'] / route['traversal_time'] if route['traversal_time'] > 0 else 0
        
        # Calculate radius (based on curvature)
        radius = 1.0 / (route['curvature'] + 1e-10)
        
        # Calculate basic centripetal force: F = m * v² / r
        basic_force = mass * (velocity ** 2) / radius
        
        # Add weight-based component
        weight_force = route['weight'] * mass * self.resonance
        
        # Add complexity-based component
        complexity_force = route['complexity'] * mass * self.coherence
        
        # Total force with φ-harmonic scaling
        total_force = (basic_force + weight_force + complexity_force) * self.bridge_factor
        
        return total_force
    
    def optimize_traversal_route(self, route: Dict[str, Any]) -> Dict[str, Any]:
        """
        Optimize a traversal route using centripetal force dynamics
        
        Args:
            route: Route properties
            
        Returns:
            Optimized route properties
        """
        # Calculate initial centripetal force
        initial_force = self.calculate_route_centripetal_force(route)
        
        # Create variations with φ-harmonic scaling
        variations = []
        
        # Base route
        variations.append(route.copy())
        
        # Vary weight
        weight_up = route.copy()
        weight_up['weight'] *= self.phi
        variations.append(weight_up)
        
        weight_down = route.copy()
        weight_down['weight'] /= self.phi
        variations.append(weight_down)
        
        # Vary complexity
        complexity_up = route.copy()
        complexity_up['complexity'] *= self.phi
        variations.append(complexity_up)
        
        complexity_down = route.copy()
        complexity_down['complexity'] /= self.phi
        variations.append(complexity_down)
        
        # Find variation with highest traversal probability
        best_probability = route['traversal_probability']
        best_route = route.copy()
        
        for var in variations:
            # Recalculate route properties
            var_route = self.create_traversal_route(
                var['entry_point'],
                var['exit_point'],
                var['weight'],
                var['complexity']
            )
            
            if var_route['traversal_probability'] > best_probability:
                best_probability = var_route['traversal_probability']
                best_route = var_route
        
        # Calculate optimization improvement
        probability_improvement = best_probability / route['traversal_probability'] if route['traversal_probability'] > 0 else 0
        
        # Calculate optimized centripetal force
        optimized_force = self.calculate_route_centripetal_force(best_route)
        force_reduction = 1 - (optimized_force / initial_force) if initial_force > 0 else 0
        
        # Add optimization metrics
        best_route['probability_improvement'] = probability_improvement
        best_route['force_reduction'] = force_reduction
        best_route['initial_force'] = initial_force
        best_route['optimized_force'] = optimized_force
        
        return best_route
    
    def optimize_all_routes(self) -> List[Dict[str, Any]]:
        """
        Optimize all traversal routes
        
        Returns:
            List of optimized route properties
        """
        optimized_routes = []
        
        for i, route in enumerate(self.traversal_routes):
            print(f"Optimizing route {i+1}/{len(self.traversal_routes)}...")
            optimized = self.optimize_traversal_route(route)
            optimized_routes.append(optimized)
        
        # Calculate system-wide metrics
        self.total_traversal_probability = sum(r['traversal_probability'] for r in optimized_routes) / len(optimized_routes)
        self.system_coherence = sum(r['coherence'] for r in optimized_routes) / len(optimized_routes)
        
        # Find optimal route
        optimal_route = max(optimized_routes, key=lambda r: r['traversal_probability'])
        self.optimal_route = optimal_route
        self.route_efficiency = optimal_route['traversal_probability']
        self.traversal_time = optimal_route['traversal_time']
        self.traversal_energy = optimal_route['traversal_energy']
        
        return optimized_routes
    
    def calculate_phi_harmonic_path(self, route: Dict[str, Any], steps: int = 100) -> List[Tuple[float, float, float]]:
        """
        Calculate a phi-harmonic path through the wormhole
        
        Args:
            route: Route properties
            steps: Number of steps in the path
            
        Returns:
            List of (x, y, z) coordinates along the path
        """
        entry = route['entry_point']
        exit = route['exit_point']
        
        # Create path with φ-harmonic interpolation
        path = []
        
        for i in range(steps + 1):
            # Normalized step with φ-harmonic scaling
            t = i / steps
            phi_t = (1 - np.cos(t * np.pi)) / 2  # Smoother transition
            
            # Apply φ-harmonic weighting
            weight = self.phi ** (phi_t - 0.5)
            
            # Interpolate position
            x = entry[0] * (1 - phi_t) + exit[0] * phi_t
            y = entry[1] * (1 - phi_t) + exit[1] * phi_t
            z = entry[2] * (1 - phi_t) + exit[2] * phi_t
            
            # Apply throat narrowing with φ-harmonic scaling
            throat_factor = 1 - (1 - self.throat_factor) * np.sin(phi_t * np.pi)
            
            # Apply centripetal adjustment
            r = np.sqrt(x**2 + y**2)
            theta = np.arctan2(y, x)
            
            # Adjust radius with centripetal force
            centripetal_factor = 1 + (route['weight'] - 1) * np.sin(phi_t * np.pi * self.phi)
            r_adjusted = r * throat_factor * centripetal_factor
            
            # Adjust angle with complexity
            theta_adjusted = theta + (route['complexity'] - 1) * np.sin(phi_t * np.pi * self.phi) * 0.1
            
            # Convert back to Cartesian
            x_adjusted = r_adjusted * np.cos(theta_adjusted)
            y_adjusted = r_adjusted * np.sin(theta_adjusted)
            
            # Apply z-scaling with bridge factor
            z_factor = 1 + (self.bridge_factor - 1) * np.sin(phi_t * np.pi)
            z_adjusted = z * z_factor
            
            path.append((x_adjusted, y_adjusted, z_adjusted))
        
        return path
    
    def visualize_optimal_route(self, show_plot: bool = True) -> plt.Figure:
        """
        Visualize optimal traversal route through the wormhole
        
        Args:
            show_plot: Whether to display the plot
            
        Returns:
            Matplotlib figure object
        """
        if not self.optimal_route:
            raise ValueError("No optimal route available. Run optimize_all_routes first.")
        
        # Create figure
        fig = plt.figure(figsize=(15, 10))
        ax = fig.add_subplot(111, projection='3d')
        
        # Generate parameter space with φ-scaling
        u = np.linspace(0, 2*np.pi, int(100*self.resonance))
        v = np.linspace(-np.pi, np.pi, int(100*self.resonance))
        U, V = np.meshgrid(u, v)
        
        # Generate wormhole surface
        X, Y, Z = generate_wormhole_surface(U, V, self.quantum_sig)
        
        # Create the surface with compression-based colormap
        surf = ax.plot_surface(X, Y, Z, cmap='plasma', alpha=0.3)
        
        # Calculate optimal path
        path = self.calculate_phi_harmonic_path(self.optimal_route, steps=100)
        path_x, path_y, path_z = zip(*path)
        
        # Plot optimal path
        ax.plot(path_x, path_y, path_z, color='cyan', linewidth=3, label='Optimal Route')
        
        # Add entry and exit points
        entry = self.optimal_route['entry_point']
        exit = self.optimal_route['exit_point']
        
        ax.scatter([entry[0]], [entry[1]], [entry[2]], color='green', s=100, label='Entry Point')
        ax.scatter([exit[0]], [exit[1]], [exit[2]], color='red', s=100, label='Exit Point')
        
        # Add other routes if available
        if len(self.traversal_routes) > 1:
            for i, route in enumerate(self.traversal_routes):
                if route != self.optimal_route:
                    alt_path = self.calculate_phi_harmonic_path(route, steps=50)
                    alt_x, alt_y, alt_z = zip(*alt_path)
                    
                    # Color based on traversal probability
                    color_val = route['traversal_probability']
                    ax.plot(alt_x, alt_y, alt_z, color=[color_val, color_val, 1.0], alpha=0.3)
        
        # Customize the visualization
        ax.set_title('Optimal Wormhole Traversal Route', color='white', pad=20)
        ax.set_facecolor('black')
        fig.patch.set_facecolor('black')
        
        # Remove axis for better visualization
        ax.set_axis_off()
        
        # Add route metrics text
        route = self.optimal_route
        metrics_text = (
            f"Optimal Route Metrics:\n"
            f"Traversal Probability: {route['traversal_probability']:.4f}\n"
            f"Traversal Time: {route['traversal_time']:.4f}\n"
            f"Traversal Energy: {route['traversal_energy']:.4f}\n"
            f"Route Length: {route['length']:.4f}\n"
            f"Route Stability: {route['stability']:.4f}\n"
            f"Route Coherence: {route['coherence']:.4f}"
        )
        plt.figtext(0.02, 0.15, metrics_text, color='cyan', fontsize=10)
        
        # Add centripetal parameters
        params_text = (
            f"Centripetal Parameters:\n"
            f"Weight Factor: {route['weight']:.4f}\n"
            f"Complexity Factor: {route['complexity']:.4f}\n"
            f"Centripetal Force: {route['optimized_force']:.4f}\n"
            f"Force Reduction: {route['force_reduction']*100:.1f}%\n"
            f"Probability Improvement: {route['probability_improvement']*100:.1f}%"
        )
        plt.figtext(0.80, 0.15, params_text, color='yellow', fontsize=10)
        
        # Add system metrics
        system_text = (
            f"System Metrics:\n"
            f"Total Routes: {self.total_routes}\n"
            f"Avg. Traversal Probability: {self.total_traversal_probability:.4f}\n"
            f"System Coherence: {self.system_coherence:.4f}\n"
            f"Compression Efficiency: {self.compression_efficiency:.4f}"
        )
        plt.figtext(0.02, 0.02, system_text, color='white', fontsize=10)
        
        if show_plot:
            plt.show()
        
        return fig
    
    def get_traversal_metrics(self) -> Dict[str, Any]:
        """
        Get current traversal metrics
        
        Returns:
            Dictionary containing traversal metrics
        """
        return {
            'total_routes': self.total_routes,
            'total_traversal_probability': self.total_traversal_probability,
            'system_coherence': self.system_coherence,
            'compression_efficiency': self.compression_efficiency,
            'route_efficiency': self.route_efficiency,
            'traversal_time': self.traversal_time,
            'traversal_energy': self.traversal_energy,
            'bridge_factor': self.bridge_factor,
            'throat_factor': self.throat_factor,
            'stability': self.stability,
            'phi': self.phi,
            'phi_power': self.phi_power,
            'resonance': self.resonance,
            'coherence': self.coherence
        }

def test_centripetal_traversal_optimizer():
    """Test the Centripetal Traversal Optimizer"""
    print("\n🚀 Centripetal Traversal Optimizer Test 🚀")
    print("=" * 50)
    
    # Initialize optimizer
    optimizer = CentripetalTraversalOptimizer()
    
    # Generate traversal routes
    print("\nGenerating traversal routes...")
    routes = optimizer.generate_traversal_routes(num_routes=5)
    
    print(f"\nGenerated {len(routes)} traversal routes")
    print("\nSample Route Metrics:")
    print(f"Length: {routes[0]['length']:.6f}")
    print(f"Curvature: {routes[0]['curvature']:.6f}")
    print(f"Stability: {routes[0]['stability']:.6f}")
    print(f"Coherence: {routes[0]['coherence']:.6f}")
    print(f"Traversal Probability: {routes[0]['traversal_probability']:.6f}")
    
    # Store routes in memory
    print("\nStoring routes in centripetal memory...")
    memory_result = optimizer.store_routes_in_memory(routes)
    
    if memory_result['success']:
        print("\nMemory Storage Results:")
        print(f"Bucket Index: {memory_result['bucket_index']}")
        print(f"Compression Ratio: {memory_result['compression_ratio']:.6f}")
        print(f"Angular Velocity: {memory_result['angular_velocity']:.6f}")
        print(f"Centripetal Force: {memory_result['centripetal_force']:.6f}")
    
    # Optimize routes
    print("\nOptimizing traversal routes...")
    optimized_routes = optimizer.optimize_all_routes()
    
    print("\nOptimization Results:")
    for i, route in enumerate(optimized_routes):
        print(f"\nRoute {i+1}:")
        print(f"Traversal Probability: {route['traversal_probability']:.6f}")
        print(f"Probability Improvement: {route['probability_improvement']*100:.1f}%")
        print(f"Force Reduction: {route['force_reduction']*100:.1f}%")
    
    # Get optimal route
    optimal_route = optimizer.optimal_route
    
    print("\nOptimal Route:")
    print(f"Traversal Probability: {optimal_route['traversal_probability']:.6f}")
    print(f"Traversal Time: {optimal_route['traversal_time']:.6f}")
    print(f"Traversal Energy: {optimal_route['traversal_energy']:.6f}")
    print(f"Weight Factor: {optimal_route['weight']:.6f}")
    print(f"Complexity Factor: {optimal_route['complexity']:.6f}")
    
    # Get traversal metrics
    metrics = optimizer.get_traversal_metrics()
    
    print("\nSystem Traversal Metrics:")
    print(f"Total Routes: {metrics['total_routes']}")
    print(f"Total Traversal Probability: {metrics['total_traversal_probability']:.6f}")
    print(f"System Coherence: {metrics['system_coherence']:.6f}")
    print(f"Compression Efficiency: {metrics['compression_efficiency']:.6f}")
    print(f"Route Efficiency: {metrics['route_efficiency']:.6f}")
    
    # Calculate phi-harmonic path
    print("\nCalculating phi-harmonic path...")
    path = optimizer.calculate_phi_harmonic_path(optimal_route, steps=5)
    
    print("\nPhi-Harmonic Path (first 5 points):")
    for i, point in enumerate(path[:5]):
        print(f"Point {i+1}: ({point[0]:.4f}, {point[1]:.4f}, {point[2]:.4f})")
    
    # Visualize optimal route
    print("\nVisualizing optimal route...")
    try:
        fig = optimizer.visualize_optimal_route(show_plot=False)
        print("Visualization successful! (Plot not shown in terminal)")
    except Exception as e:
        print(f"Visualization error: {e}")

if __name__ == "__main__":
    test_centripetal_traversal_optimizer()

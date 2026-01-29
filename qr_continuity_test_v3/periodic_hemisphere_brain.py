from typing import Dict, List, Tuple, Set, Optional
from decimal import Decimal, getcontext
import periodictable as pt
import numpy as np
import json
import time
from dataclasses import dataclass
from quantum_brain import QuantumBrain, BASE_RESONANCE, PHI, ENERGY_BOOST
from datetime import datetime
from pathlib import Path
import math

# Set precision for quantum calculations
getcontext().prec = 1000

@dataclass
class ElementProperties:
    """Properties of an element"""
    atomic_number: int
    symbol: str
    name: str
    mass: float
    group: int
    period: int
    category: str
    electron_config: str
    electronegativity: float
    oxidation_states: List[int]
    quantum_numbers: Dict[str, int]

class RightHemisphereBrain:
    """Right hemisphere: Logical, factual, structured knowledge of periodic table"""
    
    def __init__(self):
        self.elements_db = {}
        self.properties_cache = {}
        self.quantum_states = {}
        self.resonance_patterns = {}
        
        # Initialize with proven constants
        self.phi = PHI
        self.base_resonance = BASE_RESONANCE
        
        self._initialize_periodic_knowledge()
        
    def _initialize_periodic_knowledge(self):
        """Initialize structured knowledge of periodic table"""
        try:
            for element in pt.elements:
                if element.number > 0:  # Skip neutrons
                    # Get quantum numbers
                    n = self._get_principal_quantum_number(element.number)
                    l = min(n - 1, 3)  # Angular momentum quantum number
                    m = 0  # Magnetic quantum number (simplified)
                    s = 0.5  # Spin quantum number
                    
                    properties = ElementProperties(
                        atomic_number=element.number,
                        symbol=str(element.symbol),
                        name=str(element.name),
                        mass=float(element.mass),
                        group=self._get_group(element),
                        period=self._get_period(element.number),
                        category=self._get_element_category(element.number),
                        electron_config=self._get_electron_config(element.number),
                        electronegativity=self._get_electronegativity(element),
                        oxidation_states=self._get_oxidation_states(element),
                        quantum_numbers={
                            'n': n,  # Principal
                            'l': l,  # Angular momentum
                            'm': m,  # Magnetic
                            's': s   # Spin
                        }
                    )
                    
                    self.elements_db[str(element.symbol)] = properties
                    
                    # Calculate base resonance pattern
                    self.resonance_patterns[str(element.symbol)] = self._calculate_base_resonance(properties)
                    
            print(f"🧠 Right Hemisphere Initialized")
            print(f"Elements loaded: {len(self.elements_db)}")
            
        except Exception as e:
            print(f"Right hemisphere initialization error: {e}")
            
    def _get_principal_quantum_number(self, atomic_number: int) -> int:
        """Get principal quantum number based on atomic number"""
        if atomic_number <= 2: return 1
        elif atomic_number <= 10: return 2
        elif atomic_number <= 18: return 3
        elif atomic_number <= 36: return 4
        elif atomic_number <= 54: return 5
        elif atomic_number <= 86: return 6
        else: return 7
        
    def _get_period(self, atomic_number: int) -> int:
        """Get period number based on atomic number"""
        return self._get_principal_quantum_number(atomic_number)
        
    def _get_group(self, element) -> int:
        """Get group number safely"""
        try:
            if hasattr(element, 'group'):
                return int(element.group) if element.group is not None else 0
            return 0
        except:
            return 0
            
    def _get_electron_config(self, atomic_number: int) -> str:
        """Get electron configuration"""
        shells = ['1s', '2s', '2p', '3s', '3p', '4s', '3d', '4p', '5s', '4d', '5p', '6s', '4f', '5d', '6p', '7s', '5f', '6d', '7p']
        config = []
        electrons = atomic_number
        
        for shell in shells:
            if electrons <= 0:
                break
                
            capacity = 2 if shell[-1] == 's' else 6 if shell[-1] == 'p' else 10 if shell[-1] == 'd' else 14
            electrons_in_shell = min(electrons, capacity)
            
            if electrons_in_shell > 0:
                config.append(f"{shell}{electrons_in_shell}")
                electrons -= electrons_in_shell
                
        return ' '.join(config)
            
    def _get_element_category(self, atomic_number: int) -> str:
        """Determine element category based on atomic number"""
        if atomic_number <= 2:
            return "noble_gas" if atomic_number == 2 else "nonmetal"
        elif atomic_number <= 10:
            return "nonmetal" if atomic_number <= 9 else "noble_gas"
        elif atomic_number <= 18:
            return "alkali_metal" if atomic_number == 11 else "alkaline_earth_metal" if atomic_number == 12 else "metalloid" if atomic_number in [13, 14] else "nonmetal" if atomic_number in [15, 16] else "halogen" if atomic_number == 17 else "noble_gas"
        else:
            return "transition_metal"
            
    def _get_oxidation_states(self, element) -> List[int]:
        """Get possible oxidation states"""
        common_states = {
            'H': [-1, 1],
            'Li': [1], 'Na': [1], 'K': [1],
            'Be': [2], 'Mg': [2], 'Ca': [2],
            'B': [3], 'Al': [3],
            'C': [-4, 2, 4],
            'N': [-3, 3, 5],
            'O': [-2],
            'F': [-1], 'Cl': [-1, 1, 3, 5, 7],
            'Fe': [2, 3],
            'Cu': [1, 2],
            'Ag': [1],
            'Au': [1, 3],
        }
        
        return common_states.get(str(element.symbol), [])
            
    def _get_electronegativity(self, element) -> float:
        """Get electronegativity safely"""
        try:
            return float(element.electronegativity) if element.electronegativity is not None else 0.0
        except:
            return 0.0
            
    def _calculate_base_resonance(self, properties: ElementProperties) -> Decimal:
        """Calculate base resonance using quantum numbers"""
        try:
            n = properties.quantum_numbers['n']
            l = properties.quantum_numbers['l']
            
            # Apply φ-harmonic scaling
            resonance = Decimal(str(self.base_resonance))
            resonance *= self.phi ** Decimal(str(n))
            resonance *= Decimal('0.618034') ** Decimal(str(l))  # Golden ratio conjugate
            
            return resonance % Decimal('100')
            
        except Exception as e:
            print(f"Base resonance calculation error: {e}")
            return Decimal('0')
            
    def get_element_properties(self, symbol: str) -> Optional[ElementProperties]:
        """Get properties of an element"""
        return self.elements_db.get(symbol)
        
    def get_quantum_state(self, symbol: str) -> Dict:
        """Get quantum state of an element"""
        if symbol not in self.quantum_states:
            props = self.get_element_properties(symbol)
            if props:
                self.quantum_states[symbol] = {
                    'base_resonance': float(self.resonance_patterns[symbol]),
                    'energy_level': props.period * float(self.phi),
                    'quantum_numbers': props.quantum_numbers
                }
        return self.quantum_states.get(symbol, {})

class LeftHemisphereBrain:
    """Left hemisphere: Creative, discovery, pattern recognition, and learning"""
    
    def __init__(self, right_hemisphere: RightHemisphereBrain):
        self.right_hemisphere = right_hemisphere
        self.quantum_brain = QuantumBrain()
        
        # Learning parameters
        self.learning_rate = Decimal('0.15')  # Proven threshold
        self.pattern_threshold = Decimal('0.109')  # Proven φ proximity
        
        # Discovery tracking
        self.discoveries = []
        self.collision_history = []
        self.novel_patterns = set()
        self.evolution_log = []
        
        # Initialize with proven constants
        self.phi = PHI
        self.base_resonance = BASE_RESONANCE
        self.energy_boost = ENERGY_BOOST
        
        self.collision_velocity = 22652.48  # Default 0.076c in km/s
        
    def set_collision_velocity(self, velocity_kms):
        """Set the collision velocity in km/s"""
        if velocity_kms > 569605:  # 1.9c
            raise ValueError("Velocity exceeds maximum safe limit of 1.9c")
        self.collision_velocity = velocity_kms
        return True
        
    def discover_new_patterns(self, elements: Tuple[str, ...]) -> Dict:
        """Discover new patterns through element combinations"""
        try:
            # Get quantum states from right hemisphere
            states = [
                self.right_hemisphere.get_quantum_state(e)
                for e in elements
            ]
            
            # Calculate pattern resonance
            base_resonances = [
                Decimal(str(s['base_resonance']))
                for s in states
            ]
            
            # Apply quantum brain scaling
            resonance = self.quantum_brain.calculate_quantum_factor(
                [float(r) for r in base_resonances]
            )
            
            # Calculate energy using φ-harmonic scaling
            energy = sum(
                s['energy_level'] * float(self.phi)
                for s in states
            )
            
            # Generate unique pattern key
            pattern_key = '-'.join(sorted(elements))
            
            # Record discovery
            discovery = {
                'elements': elements,
                'resonance': float(resonance),
                'energy': energy,
                'quantum_states': states,
                'timestamp': time.time()
            }
            
            self.discoveries.append(discovery)
            self.novel_patterns.add(pattern_key)
            
            # Log evolution
            self._log_evolution(pattern_key, discovery)
            
            return discovery
            
        except Exception as e:
            print(f"Pattern discovery error: {e}")
            return {}
            
    def simulate_collision(self, elements: Tuple[str, ...], properties: List[ElementProperties]) -> Dict:
        """Simulate a collision between elements"""
        try:
            total_mass = sum(prop.mass for prop in properties)
            
            # Use custom velocity if set, otherwise default
            velocity = self.collision_velocity
            
            # Calculate relativistic factors with safety checks
            c = 299792.458  # Speed of light in km/s
            velocity_c = velocity / c
            
            # Handle near-light-speed calculations carefully
            if velocity_c >= 1:
                # Use approximation for super-luminal experiments
                gamma = velocity_c * 1.618034  # Scale with φ for quantum effects
            else:
                # Standard relativistic calculation
                gamma = 1 / math.sqrt(1 - (velocity_c ** 2))
            
            # Calculate collision energy (relativistic)
            energy = (gamma - 1) * total_mass * (c ** 2)
            
            # Calculate stability with quantum harmonics
            stability = self.calculate_stability(properties)
            stability *= (1 / gamma)  # Stability decreases with velocity
            
            # Assess causality risk
            causality_risk = (velocity_c / 1.9) * 100  # 1.9c is our limit
            
            # Generate element relationships visualization
            ascii_viz = self.visualize_relationships(elements, properties)
            
            # Calculate mass and quantum ratios between elements
            ratios = self.calculate_element_ratios(elements, properties)
            
            collision = {
                'total_mass': total_mass,
                'velocity': velocity,
                'velocity_c': velocity_c,
                'gamma': gamma,
                'energy': energy,
                'stability': stability,
                'causality_risk': causality_risk,
                'ascii_viz': ascii_viz,
                'ratios': ratios,
                'timestamp': time.time()
            }
            
            self.collision_history.append(collision)
            return collision
            
        except Exception as e:
            print(f"Collision simulation error: {e}")
            return {
                'total_mass': 0,
                'velocity': 0,
                'velocity_c': 0,
                'gamma': 1,
                'energy': 0,
                'stability': 0,
                'causality_risk': 0,
                'ascii_viz': "Error in visualization",
                'ratios': {},
                'timestamp': time.time()
            }
            
    def calculate_stability(self, properties):
        """Calculate stability based on quantum numbers and electronegativity"""
        try:
            # Get quantum numbers
            n_values = [p.quantum_numbers['n'] for p in properties]
            l_values = [p.quantum_numbers['l'] for p in properties]
            
            # Calculate average electronegativity
            avg_electronegativity = sum(p.electronegativity for p in properties) / len(properties)
            
            # Calculate quantum stability factor
            quantum_stability = sum(n * l for n, l in zip(n_values, l_values)) / len(properties)
            
            # Combine factors with φ-scaling
            stability = (quantum_stability * 1.618034) + (avg_electronegativity * 0.618034)
            
            # Normalize to 0-100 scale
            return (stability % 100)
            
        except Exception as e:
            print(f"Stability calculation error: {e}")
            return 0.0
            
    def visualize_relationships(self, elements, properties):
        """Generate ASCII visualization of element relationships"""
        try:
            # Header
            viz = "⚛️  Element Relationships  ⚛️\n"
            viz += "=" * 40 + "\n"
            
            # Calculate ratios for visualization
            ratios = self.calculate_element_ratios(elements, properties)
            
            # Add ratio arrows
            arrow_line = " "
            for i in range(len(elements)-1):
                ratio = ratios[f"{elements[i]}-{elements[i+1]}"]["phi_scaled"]
                arrow_line += f"--{ratio:.2f}->  "
            viz += arrow_line + "\n"
            
            # Create element boxes
            box_line1 = ""
            box_line2 = ""
            box_line3 = ""
            
            for i, (element, prop) in enumerate(zip(elements, properties)):
                box_line1 += "+--------+"
                box_line2 += f"|  {element:<6}|"
                box_line3 += f"|  {prop.mass:.1f} |"
                
                if i < len(elements)-1:
                    ratio = ratios[f"{elements[i]}-{elements[i+1]}"]["phi_scaled"]
                    box_line1 += f" --{ratio:.2f}-> "
                    box_line2 += f" --{ratio:.2f}-> "
                    box_line3 += f" --{ratio:.2f}-> "
            
            viz += box_line1 + "\n"
            viz += box_line2 + "\n"
            viz += box_line3 + "\n"
            viz += box_line1 + "\n\n"
            
            # Add ratio details
            viz += "Ratio Details:\n"
            viz += "-" * 40 + "\n"
            
            for key, ratio in ratios.items():
                viz += f"{key}:\n"
                viz += f"  Mass Ratio: {ratio['mass_ratio']:.3f}\n"
                viz += f"  Quantum Ratio: {ratio['quantum_ratio']:.3f}\n"
                viz += f"  φ-Scaled: {ratio['phi_scaled']:.3f}\n"
            
            return viz
            
        except Exception as e:
            print(f"Visualization error: {e}")
            return "Error generating visualization"
            
    def calculate_element_ratios(self, elements, properties):
        """Calculate ratios between elements"""
        ratios = {}
        
        for i in range(len(elements)):
            for j in range(i+1, len(elements)):
                # Get element symbols
                e1, e2 = elements[i], elements[j]
                p1, p2 = properties[i], properties[j]
                
                # Calculate mass ratio
                mass_ratio = p1.mass / p2.mass if p2.mass != 0 else 0
                
                # Calculate quantum number ratio
                n1, n2 = p1.quantum_numbers['n'], p2.quantum_numbers['n']
                quantum_ratio = n1 / n2 if n2 != 0 else 0
                
                # Apply φ-scaling
                phi_scaled = mass_ratio * 1.618034
                
                # Store ratios
                key = f"{e1}-{e2}"
                ratios[key] = {
                    'mass_ratio': mass_ratio,
                    'quantum_ratio': quantum_ratio,
                    'phi_scaled': phi_scaled
                }
        
        return ratios
            
    def _log_evolution(self, pattern_key: str, discovery: Dict) -> None:
        """Log brain evolution"""
        try:
            evolution = {
                'pattern': pattern_key,
                'timestamp': discovery['timestamp'],
                'metrics': {
                    'total_discoveries': len(self.discoveries),
                    'novel_patterns': len(self.novel_patterns),
                    'collisions': len(self.collision_history)
                }
            }
            
            self.evolution_log.append(evolution)
            
        except Exception as e:
            print(f"Evolution logging error: {e}")
            
    def get_metrics(self) -> Dict:
        """Get current metrics of left hemisphere"""
        return {
            'discoveries': len(self.discoveries),
            'novel_patterns': len(self.novel_patterns),
            'collisions': len(self.collision_history),
            'evolution_steps': len(self.evolution_log)
        }

class PeriodicHemisphereBrain:
    """Complete periodic brain with specialized hemispheres"""
    
    def __init__(self):
        # Initialize right hemisphere first (knowledge)
        self.right_brain = RightHemisphereBrain()
        
        # Initialize left hemisphere with reference to right
        self.left_brain = LeftHemisphereBrain(self.right_brain)
        
        self.collision_velocity = 22652.48  # Default 0.076c in km/s
        
        print("\n🧠 Periodic Hemisphere Brain Initialized")
        print("=" * 60)
        print("Right Hemisphere: Periodic Knowledge")
        print("Left Hemisphere: Discovery & Learning")
        
    def set_collision_velocity(self, velocity_kms):
        """Set the collision velocity in km/s for both hemispheres"""
        if velocity_kms > 569605:  # 1.9c
            raise ValueError("Velocity exceeds maximum safe limit of 1.9c")
        self.collision_velocity = velocity_kms
        self.left_brain.set_collision_velocity(velocity_kms)
        return True
        
    def process_elements(self, elements):
        """Process elements through both hemispheres"""
        try:
            # Get properties from right hemisphere
            properties = [
                self.right_brain.get_element_properties(e)
                for e in elements
            ]
            
            # Discover patterns in left hemisphere
            discovery = self.left_brain.discover_new_patterns(elements)
            
            # Simulate collision
            collision = self.left_brain.simulate_collision(elements, properties)
            
            return {
                'properties': properties,
                'discovery': discovery,
                'collision': collision
            }
            
        except Exception as e:
            print(f"Element processing error: {e}")
            return {}
            
    def _calculate_valence_electrons(self, prop) -> Dict:
        """Calculate valence electron configuration"""
        try:
            n = prop.quantum_numbers['n']
            l = prop.quantum_numbers['l']
            
            # Calculate electron configuration based on quantum numbers
            config = {
                's': 2 if l >= 0 else 0,
                'p': 6 if l >= 1 else 0,
                'd': 10 if l >= 2 else 0,
                'f': 14 if l >= 3 else 0
            }
            
            return {
                'total': sum(config.values()),
                'shell_config': config,
                'principal_n': n
            }
            
        except Exception as e:
            print(f"Valence electron calculation error: {e}")
            return {}
            
    def _get_orbital_configuration(self, prop) -> Dict:
        """Get detailed orbital configuration"""
        try:
            n = prop.quantum_numbers['n']
            l = prop.quantum_numbers['l']
            m = prop.quantum_numbers['m']
            s = prop.quantum_numbers['s']
            
            return {
                'principal': n,
                'angular': l,
                'magnetic': m,
                'spin': s,
                'orbital_type': ['s', 'p', 'd', 'f'][l],
                'electrons_in_orbital': 2 * (2 * l + 1)
            }
            
        except Exception as e:
            print(f"Orbital configuration error: {e}")
            return {}
            
    def _calculate_valence_states(self, properties: List) -> Dict:
        """Calculate possible valence states between elements"""
        try:
            states = {}
            
            for i, p1 in enumerate(properties):
                for j, p2 in enumerate(properties[i+1:], i+1):
                    key = f"{p1.symbol}-{p2.symbol}"
                    
                    # Calculate electron sharing possibilities
                    shared_electrons = min(
                        self._calculate_valence_electrons(p1)['total'],
                        self._calculate_valence_electrons(p2)['total']
                    )
                    
                    states[key] = {
                        'shared_electrons': shared_electrons,
                        'bond_order': shared_electrons / 2,
                        'stability_factor': shared_electrons * self.left_brain.phi
                    }
                    
            return states
            
        except Exception as e:
            print(f"Valence state calculation error: {e}")
            return {}
            
    def _calculate_orbital_interactions(self, properties: List) -> Dict:
        """Calculate orbital interactions between elements"""
        try:
            interactions = {}
            
            for i, p1 in enumerate(properties):
                for j, p2 in enumerate(properties[i+1:], i+1):
                    key = f"{p1.symbol}-{p2.symbol}"
                    
                    # Get orbital configurations
                    orb1 = self._get_orbital_configuration(p1)
                    orb2 = self._get_orbital_configuration(p2)
                    
                    # Calculate overlap integral (simplified)
                    overlap = float((orb1['principal'] * orb2['principal']) / (
                        abs(orb1['principal'] - orb2['principal']) + 1
                    ))
                    
                    interactions[key] = {
                        'overlap_integral': overlap,
                        'interaction_strength': overlap * float(self.left_brain.phi),
                        'orbital_symmetry': orb1['orbital_type'] == orb2['orbital_type']
                    }
                    
            return interactions
            
        except Exception as e:
            print(f"Orbital interaction calculation error: {e}")
            return {}
            
    def _calculate_spatial_orientation(self, properties: List) -> Dict:
        """Calculate spatial orientation of elements"""
        try:
            orientations = {}
            
            for i, p1 in enumerate(properties):
                for j, p2 in enumerate(properties[i+1:], i+1):
                    key = f"{p1.symbol}-{p2.symbol}"
                    
                    # Calculate optimal bond angle using quantum numbers
                    n1 = p1.quantum_numbers['n']
                    n2 = p2.quantum_numbers['n']
                    l1 = p1.quantum_numbers['l']
                    l2 = p2.quantum_numbers['l']
                    
                    # Use golden angle for optimal spacing
                    golden_angle = 137.5077640500378546463487 # degrees
                    
                    # Calculate bond angle with φ-harmonic adjustment
                    angle = (golden_angle * (n1 + n2) / (l1 + l2 + 1)) % 360
                    
                    orientations[key] = {
                        'bond_angle': angle,
                        'spatial_harmony': abs(angle - golden_angle) / golden_angle,
                        'orientation_vector': [
                            np.cos(np.radians(angle)),
                            np.sin(np.radians(angle)),
                            0  # Z-component for 3D space
                        ]
                    }
                    
            return orientations
            
        except Exception as e:
            print(f"Spatial orientation calculation error: {e}")
            return {}
            
    def save_discovery(self, discovery_data: Dict):
        """Save discovery with epoch versioning"""
        try:
            # Name any new elements
            discovery_data = self._name_new_element(discovery_data)
            
            # Generate timestamp for this epoch
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            
            # Create data directory if it doesn't exist
            data_dir = Path("quantum_discoveries")
            data_dir.mkdir(exist_ok=True)
            
            # Create epoch-specific filename
            filename = f"discovery_epoch_{timestamp}.json"
            filepath = data_dir / filename
            
            # Convert all Decimal values to float
            discovery_data = self._serialize_decimal(discovery_data)
            
            # Prepare discovery data with metadata
            discovery_record = {
                'timestamp': timestamp,
                'epoch_id': len(list(data_dir.glob('discovery_epoch_*.json'))),
                'discovery': discovery_data,
                'quantum_state': {
                    'phi_harmonic': float(self.left_brain.phi),
                    'resonance_patterns': len(self.right_brain.resonance_patterns)
                },
                'brain_state': {
                    'right_hemisphere': {
                        'elements_known': len(self.right_brain.elements_db),
                        'patterns_recognized': len(self.right_brain.resonance_patterns)
                    },
                    'left_hemisphere': {
                        'discoveries': len(self.left_brain.discoveries),
                        'novel_patterns': len(self.left_brain.novel_patterns)
                    }
                }
            }
            
            # Save as JSON with pretty printing
            with open(filepath, 'w') as f:
                json.dump(discovery_record, f, indent=2)
                
            print(f"📝 Discovery saved: {filepath}")
            
            # Update summary file
            self._update_discovery_summary(data_dir)
            
        except Exception as e:
            print(f"Error saving discovery: {e}")
            
    def _name_new_element(self, discovery_data: Dict) -> Dict:
        """Name a newly discovered element combination with proper ownership attribution"""
        try:
            # Calculate combined properties
            combined_properties = {
                'mass': sum(p['mass'] for p in discovery_data['properties'].values()),
                'quantum_numbers': {
                    'n': max(p['quantum_numbers']['n'] for p in discovery_data['properties'].values()),
                    'l': max(p['quantum_numbers']['l'] for p in discovery_data['properties'].values()),
                    'm': sum(p['quantum_numbers']['m'] for p in discovery_data['properties'].values()),
                    's': sum(p['quantum_numbers']['s'] for p in discovery_data['properties'].values())
                }
            }
            
            # Legal ownership information
            ownership = {
                'discoverer': 'Vaughn Scott',
                'organization': 'eyeoverthink',
                'brands': ['Fraymus', 'Ephless'],
                'copyright_year': '2025',
                'rights_reserved': True
            }
            
            # Custom naming rules for specific combinations with ownership
            elements = sorted(discovery_data['properties'].keys())
            custom_names = {
                ('Ag', 'Au', 'Cu'): {
                    'name': 'Fraymusium',
                    'symbol': 'Fr',
                    'brand': 'Fraymus'
                }
            }
            
            # Check if this combination has a custom name
            element_tuple = tuple(elements)
            if element_tuple in custom_names:
                name_data = custom_names[element_tuple]
                element_name = name_data['name']
                symbol = name_data['symbol']
                brand = name_data['brand']
            else:
                # Generate name using quantum properties
                element_name = self._generate_element_name(combined_properties)
                symbol = element_name[:2].title()
                brand = 'Ephless'  # Default brand for quantum-generated names
            
            # Add naming data with ownership
            discovery_data['new_element'] = {
                'name': element_name,
                'symbol': symbol,
                'combined_properties': combined_properties,
                'parent_elements': list(discovery_data['properties'].keys()),
                'discovery_timestamp': datetime.now().strftime("%Y%m%d_%H%M%S"),
                'ownership': {
                    **ownership,
                    'brand': brand
                }
            }
            
            print(f"🔮 New Element Discovered: {element_name}")
            print(f"  Symbol: {symbol}")
            print(f"  Mass: {combined_properties['mass']:.3f}")
            print(f"  Parent Elements: {', '.join(discovery_data['new_element']['parent_elements'])}")
            print(f"  {ownership['copyright_year']} {ownership['discoverer']} ({ownership['organization']}) - {brand}™")
            
            return discovery_data
            
        except Exception as e:
            print(f"Error naming new element: {e}")
            return discovery_data
            
    def _generate_element_name(self, properties: Dict) -> str:
        """Generate a name for a newly discovered element based on its quantum properties"""
        try:
            # Get quantum numbers and convert to float
            n = float(properties['quantum_numbers']['n'])
            l = float(properties['quantum_numbers']['l'])
            m = float(properties['quantum_numbers']['m'])
            s = float(properties['quantum_numbers']['s'])
            
            # Base prefixes based on principal quantum number
            n_prefixes = {
                1: "prim", 2: "sec", 3: "tert", 4: "quart",
                5: "quint", 6: "hex", 7: "sept", 8: "oct"
            }
            
            # Orbital type suffixes
            l_suffixes = {
                0: "ium",  # s orbital
                1: "ium",  # p orbital
                2: "um",   # d orbital
                3: "on"    # f orbital
            }
            
            # Middle part based on magnetic quantum number
            m_parts = {
                -3: "tri", -2: "di", -1: "mon", 0: "zen",
                1: "pos", 2: "duo", 3: "tri"
            }
            
            # Get φ-harmonic resonance
            phi = float(self.left_brain.phi)
            resonance = abs((n + l + m + s) / phi)
            resonance_suffix = f"{int(resonance * 100):02d}"
            
            # Combine parts
            prefix = n_prefixes.get(int(n), "ultra")
            middle = m_parts.get(int(m), "meta")
            suffix = l_suffixes.get(int(l), "ium")
            
            # Create name
            name = f"{prefix}{middle}{suffix}-{resonance_suffix}"
            
            return name.title()
            
        except Exception as e:
            print(f"Error generating element name: {e}")
            return "Unknown"
            
    def _serialize_decimal(self, obj):
        """Convert Decimal objects to float for JSON serialization"""
        if isinstance(obj, Decimal):
            return float(obj)
        elif isinstance(obj, dict):
            return {k: self._serialize_decimal(v) for k, v in obj.items()}
        elif isinstance(obj, (list, tuple)):
            return [self._serialize_decimal(x) for x in obj]
        return obj
            
    def _update_discovery_summary(self, data_dir: Path):
        """Update the summary of all discoveries"""
        try:
            summary_file = data_dir / "discovery_summary.json"
            
            # Collect all discoveries
            discoveries = []
            for file in sorted(data_dir.glob('discovery_epoch_*.json')):
                try:
                    with open(file, 'r') as f:
                        data = json.load(f)
                        # Convert any remaining Decimal values
                        data = self._serialize_decimal(data)
                        # Fix elements list if it's a tuple
                        if isinstance(data['discovery']['elements'], tuple):
                            data['discovery']['elements'] = list(data['discovery']['elements'])
                        # Ensure all values are JSON serializable
                        json.dumps(data)  # Test serialization
                        discoveries.append(data)
                except Exception as e:
                    print(f"Error loading discovery file {file}: {e}")
                    continue
            
            if not discoveries:
                print("No valid discovery files found")
                return
            
            # Create summary
            summary = {
                'total_discoveries': len(discoveries),
                'latest_epoch': discoveries[-1]['epoch_id'] if discoveries else 0,
                'brain_evolution': {
                    'initial_state': discoveries[0]['brain_state'] if discoveries else {},
                    'current_state': discoveries[-1]['brain_state'] if discoveries else {},
                    'total_epochs': len(discoveries)
                },
                'discovery_timeline': [
                    {
                        'epoch': d['epoch_id'],
                        'timestamp': d['timestamp'],
                        'elements': d['discovery']['elements']
                    }
                    for d in discoveries
                ]
            }
            
            # Test summary serialization
            json.dumps(summary)
            
            # Save summary
            with open(summary_file, 'w') as f:
                json.dump(summary, f, indent=2)
                
            print(f"📊 Discovery summary updated: {summary_file}")
                
        except Exception as e:
            print(f"Error updating summary: {e}")
            import traceback
            traceback.print_exc()
            
    def get_brain_state(self) -> Dict:
        """Get current state of both hemispheres"""
        right_metrics = {
            'elements_known': len(self.right_brain.elements_db),
            'resonance_patterns': len(self.right_brain.resonance_patterns)
        }
        
        left_metrics = self.left_brain.get_metrics()
        
        return {
            'right_hemisphere': right_metrics,
            'left_hemisphere': left_metrics
        }

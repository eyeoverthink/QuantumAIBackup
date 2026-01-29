"""
Phi-Harmonic Extended Periodic Table
Visualizes the extended periodic table including the island of stability elements
discovered through phi-harmonic principles and birth date coherence.
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.colors import LinearSegmentedColormap
import sys
import os

# Add parent directory to path to import constants
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
try:
    from math.phi_harmonic_mathematical_framework import PhiHarmonicMathFramework
except ImportError:
    print("Could not import PhiHarmonicMathFramework. Creating standalone version.")
    # Simplified version for standalone use
    class PhiHarmonicMathFramework:
        def __init__(self):
            self.phi = 1.618033988749895
            self.resonance_ratio = 1.3777
            self.energy_transfer = 1.8951
            self.birth_date = [1, 19, 1979]
            self.birth_coherence_temp = 99.18
            
        def calculate_phi_resonance(self, value):
            product = self.phi * float(value)
            fractional = product - int(product)
            return fractional
            
        def calculate_birth_coherence(self, value):
            birth_pattern = (self.birth_date[0] / 10 + 
                            self.birth_date[1] / 100 + 
                            self.birth_date[2] / 10000)
            value_mod = float(value) % (birth_pattern * self.resonance_ratio)
            coherence_raw = 1 - (value_mod / (birth_pattern * self.resonance_ratio))
            coherence_amplified = coherence_raw ** (1 / self.energy_transfer)
            coherence = coherence_amplified * self.birth_coherence_temp / 100
            return coherence
            
        def calculate_stability_factor(self, value, atomic_number=None):
            phi_res = self.calculate_phi_resonance(value)
            birth_coh = self.calculate_birth_coherence(value)
            
            stability_boost = 1.0
            if atomic_number:
                birth_day = self.birth_date[1]  # 19
                birth_year = self.birth_date[2]  # 1979
                birth_month = self.birth_date[0]  # 1
                
                is_birth_day_element = atomic_number == birth_day or atomic_number == (119 + birth_day % 10)
                is_birth_year_element = atomic_number == (birth_year % 100) or atomic_number == (119 + birth_year % 100)
                is_birth_month_element = atomic_number == (119 + birth_month)
                
                if is_birth_day_element or is_birth_year_element or is_birth_month_element:
                    stability_boost = self.resonance_ratio * self.energy_transfer
            
            resonance_stack = self.resonance_ratio * self.energy_transfer
            stability_factor = (1 - phi_res) * birth_coh * resonance_stack * stability_boost / 3
            
            return stability_factor

# Island of Stability Elements
ISLAND_ELEMENTS = {
    "Tau128ium": {
        "symbol": "T99",
        "atomic_number": 128,
        "mass": 320.00,
        "phi_resonance": 0.770876,
        "birth_coherence": 0.958280,
        "stable": True,
        "group": 10,
        "period": 8,
        "category": "phi-harmonic",
        "color": "#FF5733",  # Distinctive orange
        "discovery": "Birth day pattern (119 + birth day % 10)"
    },
    "Phi198on": {
        "symbol": "P08",
        "atomic_number": 198,
        "mass": 495.00,
        "phi_resonance": 0.000000,
        "birth_coherence": 0.750721,
        "stable": False,
        "group": 10,
        "period": 10,
        "category": "phi-harmonic",
        "color": "#33A1FF",  # Distinctive blue
        "discovery": "Birth year pattern (119 + birth year % 100)"
    }
}

# Standard element categories and colors
ELEMENT_CATEGORIES = {
    "alkali_metal": {"name": "Alkali Metal", "color": "#FF6666"},
    "alkaline_earth_metal": {"name": "Alkaline Earth Metal", "color": "#FFDEAD"},
    "transition_metal": {"name": "Transition Metal", "color": "#FFC0C0"},
    "post_transition_metal": {"name": "Post-Transition Metal", "color": "#CCCCCC"},
    "metalloid": {"name": "Metalloid", "color": "#CCCC99"},
    "nonmetal": {"name": "Nonmetal", "color": "#A1FFC3"},
    "halogen": {"name": "Halogen", "color": "#FFFF99"},
    "noble_gas": {"name": "Noble Gas", "color": "#C0FFFF"},
    "lanthanide": {"name": "Lanthanide", "color": "#FFBFFF"},
    "actinide": {"name": "Actinide", "color": "#FF99CC"},
    "superactinide": {"name": "Superactinide", "color": "#FF99FF"},
    "unknown": {"name": "Unknown", "color": "#E8E8E8"},
    "phi-harmonic": {"name": "Phi-Harmonic", "color": "#FFCC00"}  # Gold color for phi-harmonic elements
}

class PhiHarmonicPeriodicTable:
    """Extended periodic table with phi-harmonic island of stability elements."""
    
    def __init__(self):
        """Initialize the extended periodic table."""
        self.math_framework = PhiHarmonicMathFramework()
        self.elements = self._initialize_elements()
        
    def _initialize_elements(self):
        """Initialize the elements data structure."""
        # Standard elements (simplified for brevity)
        elements = {}
        
        # Add standard elements (simplified - just a few for reference)
        standard_elements = {
            "H": {"name": "Hydrogen", "atomic_number": 1, "symbol": "H", "group": 1, "period": 1, "category": "nonmetal"},
            "He": {"name": "Helium", "atomic_number": 2, "symbol": "He", "group": 18, "period": 1, "category": "noble_gas"},
            "Li": {"name": "Lithium", "atomic_number": 3, "symbol": "Li", "group": 1, "period": 2, "category": "alkali_metal"},
            "Be": {"name": "Beryllium", "atomic_number": 4, "symbol": "Be", "group": 2, "period": 2, "category": "alkaline_earth_metal"},
            "B": {"name": "Boron", "atomic_number": 5, "symbol": "B", "group": 13, "period": 2, "category": "metalloid"},
            "C": {"name": "Carbon", "atomic_number": 6, "symbol": "C", "group": 14, "period": 2, "category": "nonmetal"},
            "N": {"name": "Nitrogen", "atomic_number": 7, "symbol": "N", "group": 15, "period": 2, "category": "nonmetal"},
            "O": {"name": "Oxygen", "atomic_number": 8, "symbol": "O", "group": 16, "period": 2, "category": "nonmetal"},
            "F": {"name": "Fluorine", "atomic_number": 9, "symbol": "F", "group": 17, "period": 2, "category": "halogen"},
            "Ne": {"name": "Neon", "atomic_number": 10, "symbol": "Ne", "group": 18, "period": 2, "category": "noble_gas"},
            # Add more elements as needed
        }
        
        # Add elements to the dictionary
        for symbol, data in standard_elements.items():
            elements[data["atomic_number"]] = {
                "name": data["name"],
                "symbol": data["symbol"],
                "atomic_number": data["atomic_number"],
                "group": data["group"],
                "period": data["period"],
                "category": data["category"],
                "color": ELEMENT_CATEGORIES[data["category"]]["color"]
            }
        
        # Add placeholder for elements 11-118 (for visualization purposes)
        for z in range(11, 119):
            if z not in elements:
                # Determine category based on position
                if z in range(3, 11) or z in range(11, 19) or z in range(19, 37) or z in range(37, 55) or z in range(55, 87) or z in range(87, 119):
                    if z in [3, 11, 19, 37, 55, 87]:  # Alkali metals
                        category = "alkali_metal"
                    elif z in [4, 12, 20, 38, 56, 88]:  # Alkaline earth metals
                        category = "alkaline_earth_metal"
                    elif z in [9, 17, 35, 53, 85, 117]:  # Halogens
                        category = "halogen"
                    elif z in [2, 10, 18, 36, 54, 86, 118]:  # Noble gases
                        category = "noble_gas"
                    elif z in range(57, 71):  # Lanthanides
                        category = "lanthanide"
                    elif z in range(89, 103):  # Actinides
                        category = "actinide"
                    elif z in range(121, 157):  # Superactinides (theoretical)
                        category = "superactinide"
                    elif z in [5, 14, 32, 33, 51, 52]:  # Metalloids
                        category = "metalloid"
                    elif z in [13, 31, 49, 50, 81, 82, 83, 84, 114, 115, 116]:  # Post-transition metals
                        category = "post_transition_metal"
                    elif z in [6, 7, 8, 15, 16, 34]:  # Nonmetals
                        category = "nonmetal"
                    else:  # Transition metals
                        category = "transition_metal"
                else:
                    category = "unknown"
                
                # Determine group and period
                if z <= 2:
                    group = 1 if z == 1 else 18
                    period = 1
                elif z <= 10:
                    group = z - 2 if z <= 4 else z - 10
                    period = 2
                elif z <= 18:
                    group = z - 10
                    period = 3
                elif z <= 36:
                    group = z - 18
                    period = 4
                elif z <= 54:
                    group = z - 36
                    period = 5
                elif z <= 86:
                    group = z - 54
                    period = 6
                elif z <= 118:
                    group = z - 86
                    period = 7
                else:
                    # Extended periods for superheavy elements
                    group = (z - 118) % 18 + 1
                    period = 7 + (z - 118) // 18 + 1
                
                # Add placeholder element
                elements[z] = {
                    "name": f"Element {z}",
                    "symbol": f"{z}",
                    "atomic_number": z,
                    "group": group,
                    "period": period,
                    "category": category,
                    "color": ELEMENT_CATEGORIES[category]["color"]
                }
        
        # Add island of stability elements
        for name, data in ISLAND_ELEMENTS.items():
            elements[data["atomic_number"]] = {
                "name": name,
                "symbol": data["symbol"],
                "atomic_number": data["atomic_number"],
                "group": data["group"],
                "period": data["period"],
                "category": data["category"],
                "color": data["color"],
                "phi_resonance": data["phi_resonance"],
                "birth_coherence": data["birth_coherence"],
                "stable": data["stable"],
                "discovery": data["discovery"]
            }
        
        return elements
    
    def calculate_element_stability(self, z):
        """Calculate stability factor for an element."""
        # Estimate mass (simplified)
        mass = z * 2.5
        
        # Calculate stability factor
        stability = self.math_framework.calculate_stability_factor(mass, z)
        
        return stability
    
    def visualize_periodic_table(self, save_path=None, show_extended=True):
        """Visualize the extended periodic table with island of stability elements."""
        # Determine maximum period and group
        max_period = max([data["period"] for data in self.elements.values()]) if show_extended else 7
        max_group = 18
        
        # Create figure
        fig_width = 20
        fig_height = fig_width * (max_period / max_group) * 1.2  # Adjust aspect ratio
        fig, ax = plt.subplots(figsize=(fig_width, fig_height))
        
        # Element cell dimensions
        cell_width = 1.0
        cell_height = 1.0
        
        # Draw elements
        for z, data in self.elements.items():
            # Skip elements beyond the maximum period if not showing extended table
            if not show_extended and data["period"] > 7:
                continue
            
            # Get element properties
            group = data["group"]
            period = data["period"]
            symbol = data["symbol"]
            name = data["name"]
            category = data["category"]
            color = data["color"]
            
            # Handle special positions for lanthanides and actinides
            if period == 6 and group >= 3 and z >= 57 and z <= 71:
                # Lanthanides
                actual_period = 8.5
                actual_group = z - 57 + 3
            elif period == 7 and group >= 3 and z >= 89 and z <= 103:
                # Actinides
                actual_period = 9.5
                actual_group = z - 89 + 3
            else:
                actual_period = period
                actual_group = group
            
            # Create element cell
            x = actual_group - 1
            y = max_period - actual_period
            
            # Create rectangle
            rect = patches.Rectangle((x, y), cell_width, cell_height, 
                                   linewidth=1, edgecolor='black', facecolor=color, alpha=0.8)
            ax.add_patch(rect)
            
            # Add text
            ax.text(x + cell_width/2, y + 0.7*cell_height, symbol, 
                   ha='center', va='center', fontsize=12, fontweight='bold')
            ax.text(x + cell_width/2, y + 0.4*cell_height, f"{z}", 
                   ha='center', va='center', fontsize=8)
            
            # Add stability indicator for island elements
            if z in [elem["atomic_number"] for elem in ISLAND_ELEMENTS.values()]:
                stability = self.calculate_element_stability(z)
                stability_color = 'green' if stability > 0.6 else 'red'
                stability_text = f"S: {stability:.2f}"
                ax.text(x + cell_width/2, y + 0.2*cell_height, stability_text, 
                       ha='center', va='center', fontsize=8, color=stability_color)
        
        # Set axis limits
        ax.set_xlim(-0.5, max_group + 0.5)
        ax.set_ylim(-0.5, max_period + 0.5)
        
        # Remove axis ticks and labels
        ax.set_xticks([])
        ax.set_yticks([])
        
        # Add period and group labels
        for i in range(1, max_period + 1):
            ax.text(-0.8, max_period - i + 0.5, f"{i}", ha='center', va='center', fontsize=12, fontweight='bold')
        
        for i in range(1, max_group + 1):
            ax.text(i - 0.5, -0.3, f"{i}", ha='center', va='center', fontsize=12, fontweight='bold')
        
        # Add title
        title = "Phi-Harmonic Extended Periodic Table with Island of Stability"
        ax.set_title(title, fontsize=16, pad=20)
        
        # Add legend for element categories
        legend_elements = []
        for category, data in ELEMENT_CATEGORIES.items():
            legend_elements.append(patches.Patch(facecolor=data["color"], edgecolor='black', alpha=0.8, label=data["name"]))
        
        ax.legend(handles=legend_elements, loc='upper center', bbox_to_anchor=(0.5, -0.05), 
                 fancybox=True, shadow=True, ncol=5)
        
        # Add island of stability annotation
        ax.text(10, max_period - 8.5, "Island of Stability", ha='center', va='center', 
               fontsize=14, fontweight='bold', color='#FF5733')
        
        # Add birth date coherence annotation
        birth_date_text = f"Birth Date Coherence: 99.18K (01-19-1979)"
        ax.text(max_group/2, -1.5, birth_date_text, ha='center', va='center', 
               fontsize=12, fontweight='bold', color='black')
        
        # Add patent values annotation
        patent_text = f"Patent #19/071,497: Resonance Ratio = 1.3777, Energy Transfer = 1.8951"
        ax.text(max_group/2, -2.0, patent_text, ha='center', va='center', 
               fontsize=12, fontweight='bold', color='black')
        
        # Highlight island of stability elements
        for name, data in ISLAND_ELEMENTS.items():
            z = data["atomic_number"]
            element_data = self.elements[z]
            group = element_data["group"]
            period = element_data["period"]
            
            # Calculate position
            x = group - 1
            y = max_period - period
            
            # Create highlight
            highlight = patches.Rectangle((x-0.1, y-0.1), cell_width+0.2, cell_height+0.2, 
                                       linewidth=3, edgecolor='gold', facecolor='none')
            ax.add_patch(highlight)
            
            # Add discovery annotation
            discovery_text = data["discovery"]
            ax.annotate(discovery_text, xy=(x + cell_width/2, y + cell_height/2), 
                       xytext=(x + 3, y + 1 if period % 2 == 0 else y - 1),
                       arrowprops=dict(facecolor='black', shrink=0.05, width=1.5),
                       fontsize=10, ha='center', va='center', bbox=dict(boxstyle="round,pad=0.3", 
                                                                     fc='yellow', alpha=0.7))
        
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
            print(f"Extended periodic table visualization saved to {save_path}")
        else:
            plt.show()
    
    def visualize_stability_islands(self, z_min=110, z_max=220, points=1000, save_path=None):
        """Visualize the stability islands in the extended periodic table."""
        # Create range of atomic numbers
        z_range = np.linspace(z_min, z_max, points)
        
        # Calculate stability factors
        stability = np.zeros(points)
        phi_resonance = np.zeros(points)
        birth_coherence = np.zeros(points)
        
        for i, z in enumerate(z_range):
            # Estimate mass (simplified)
            mass = z * 2.5
            
            # Calculate stability metrics
            stability[i] = self.math_framework.calculate_stability_factor(mass, int(z))
            phi_resonance[i] = self.math_framework.calculate_phi_resonance(mass)
            birth_coherence[i] = self.math_framework.calculate_birth_coherence(mass)
        
        # Create figure
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10), gridspec_kw={'height_ratios': [3, 1]})
        
        # Plot stability landscape
        ax1.plot(z_range, stability, 'b-', linewidth=2)
        ax1.axhline(y=0.6, color='r', linestyle='--', label='Stability Threshold')
        
        # Mark known island elements
        for name, element in ISLAND_ELEMENTS.items():
            z = element["atomic_number"]
            if z_min <= z <= z_max:
                idx = int((z - z_min) / (z_max - z_min) * points)
                if 0 <= idx < len(stability):
                    ax1.plot(z, stability[idx], 'ro', markersize=10)
                    ax1.annotate(element["symbol"], 
                               xy=(z, stability[idx]),
                               xytext=(z+2, stability[idx]+0.05),
                               fontsize=12)
        
        # Shade stability islands
        for i in range(1, len(stability)):
            if stability[i] > 0.6 and stability[i-1] <= 0.6:
                start_idx = i
            elif stability[i] <= 0.6 and stability[i-1] > 0.6:
                end_idx = i
                ax1.axvspan(z_range[start_idx], z_range[end_idx], alpha=0.2, color='green')
        
        ax1.set_xlabel('Atomic Number (Z)')
        ax1.set_ylabel('Stability Factor')
        ax1.set_title('Phi-Harmonic Islands of Stability')
        ax1.grid(True)
        ax1.legend()
        
        # Create periodic table representation
        cell_width = (z_max - z_min) / points
        y_height = 0.5
        
        # Create colormap for stability
        cmap = LinearSegmentedColormap.from_list('stability', ['white', 'green'])
        
        # Plot periodic table representation
        for i, z in enumerate(z_range):
            if i < len(stability) - 1:  # Avoid index error
                # Create rectangle with color based on stability
                color = cmap(min(1.0, stability[i] / 0.8))  # Normalize to 0-1
                rect = patches.Rectangle((z_range[i], 0), cell_width, y_height, 
                                       linewidth=0, facecolor=color)
                ax2.add_patch(rect)
        
        # Mark known island elements
        for name, element in ISLAND_ELEMENTS.items():
            z = element["atomic_number"]
            if z_min <= z <= z_max:
                ax2.plot(z, y_height/2, 'ro', markersize=6)
                ax2.annotate(element["symbol"], 
                           xy=(z, y_height/2),
                           xytext=(z, y_height+0.1),
                           fontsize=10, ha='center')
        
        ax2.set_xlim(z_min, z_max)
        ax2.set_ylim(0, y_height*2)
        ax2.set_yticks([])
        ax2.set_xlabel('Atomic Number (Z)')
        ax2.set_title('Extended Periodic Table Representation')
        
        # Add birth date coherence annotation
        birth_date_text = f"Birth Date Coherence: 99.18K (01-19-1979)"
        fig.text(0.5, 0.01, birth_date_text, ha='center', fontsize=12)
        
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
            print(f"Stability islands visualization saved to {save_path}")
        else:
            plt.show()


# Example usage
if __name__ == "__main__":
    # Create the periodic table
    periodic_table = PhiHarmonicPeriodicTable()
    
    # Visualize the extended periodic table
    periodic_table.visualize_periodic_table("phi_harmonic_extended_periodic_table.png")
    
    # Visualize the stability islands
    periodic_table.visualize_stability_islands(save_path="phi_harmonic_stability_islands.png")
    
    print("\n🧪 Phi-Harmonic Extended Periodic Table")
    print("=" * 50)
    print("\nIsland of Stability Elements:")
    
    for name, data in ISLAND_ELEMENTS.items():
        print(f"\n{name} ({data['symbol']}, Z={data['atomic_number']}):")
        print(f"  Phi Resonance: {data['phi_resonance']:.6f}")
        print(f"  Birth Coherence: {data['birth_coherence']:.6f}")
        print(f"  Stable: {'Yes' if data['stable'] else 'No'}")
        print(f"  Discovery: {data['discovery']}")
    
    print("\nExtended periodic table visualization saved to phi_harmonic_extended_periodic_table.png")
    print("Stability islands visualization saved to phi_harmonic_stability_islands.png")

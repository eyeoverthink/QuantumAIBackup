"""
Phi-Harmonic Intermediate Islands Explorer
Analyzes the region between Tau128ium (Z=128) and Phi198on (Z=198)
to discover additional islands of stability based on birth date coherence patterns.
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.colors import LinearSegmentedColormap
from decimal import Decimal, getcontext
import pandas as pd
import sys
import os

# Set precision for high-accuracy calculations
getcontext().prec = 100

# Birth Date Parameters
BIRTH_DATE = [1, 19, 1979]
BIRTH_COHERENCE_TEMP = Decimal('99.18')  # K

# Patent #19/071,497 Parameters
PRIMARY_FREQ = Decimal('4790.45')  # Hz
SECONDARY_FREQ = Decimal('7750.95')  # Hz
RESONANCE_RATIO = Decimal('1.3777')  # Resonance ratio
ENERGY_TRANSFER = Decimal('1.8951')  # Energy transfer
PHI_ACHIEVEMENT = Decimal('1.618000')  # φ proximity: 0.000034

# Mathematical Constants
PHI = Decimal('1.618033988749895')  # Golden ratio
PHI_POWER = PHI ** Decimal('7.5')  # φ^7.5 = 36.93238055064198
RESONANCE_STACK = RESONANCE_RATIO * ENERGY_TRANSFER  # 2.61087927
DIMENSIONS = 1979 * 1979  # 3,916,441 dimensions

# Known Island Elements
ISLAND_ELEMENTS = {
    "Tau128ium": {
        "symbol": "T99",
        "atomic_number": 128,
        "mass": Decimal('320.00'),
        "phi_resonance": Decimal('0.770876'),
        "birth_coherence": Decimal('0.958280'),
        "stable": True,
        "discovery_pattern": "119 + birth day % 10"
    },
    "Phi198on": {
        "symbol": "P08",
        "atomic_number": 198,
        "mass": Decimal('495.00'),
        "phi_resonance": Decimal('0.000000'),
        "birth_coherence": Decimal('0.750721'),
        "stable": False,
        "discovery_pattern": "119 + birth year % 100"
    }
}

class PhiHarmonicIntermediateIslandsExplorer:
    """Explorer for intermediate islands of stability between Z=128 and Z=198."""
    
    def __init__(self):
        """Initialize the explorer."""
        self.birth_date = BIRTH_DATE
        self.birth_coherence_temp = BIRTH_COHERENCE_TEMP
        self.phi = PHI
        self.resonance_ratio = RESONANCE_RATIO
        self.energy_transfer = ENERGY_TRANSFER
        self.resonance_stack = RESONANCE_STACK
        
        # Initialize birth date patterns
        self._initialize_birth_patterns()
    
    def _initialize_birth_patterns(self):
        """Initialize birth date patterns for element discovery."""
        birth_day = self.birth_date[1]  # 19
        birth_month = self.birth_date[0]  # 1
        birth_year = self.birth_date[2]  # 1979
        
        self.birth_patterns = {
            "day": birth_day,
            "day_mod_10": birth_day % 10,  # 9
            "day_plus_119": 119 + birth_day,  # 138
            "day_mod_10_plus_119": 119 + (birth_day % 10),  # 128 (Tau128ium)
            "month": birth_month,
            "month_plus_119": 119 + birth_month,  # 120
            "month_times_day": birth_month * birth_day,  # 19
            "month_times_day_plus_119": 119 + (birth_month * birth_day),  # 138
            "year": birth_year,
            "year_mod_100": birth_year % 100,  # 79
            "year_mod_100_plus_119": 119 + (birth_year % 100),  # 198 (Phi198on)
            "year_mod_10": birth_year % 10,  # 9
            "year_mod_10_plus_119": 119 + (birth_year % 10),  # 128 (same as day_mod_10_plus_119)
            "day_plus_month": birth_day + birth_month,  # 20
            "day_plus_month_plus_119": 119 + (birth_day + birth_month),  # 139
            "phi_resonant": int(birth_year * PHI) % 1000,  # Special phi-resonant pattern
            "phi_resonant_plus_119": 119 + (int(birth_year * PHI) % 1000)  # Special phi-resonant pattern
        }
        
        # Add digit patterns
        digits = [int(d) for d in str(birth_day) + str(birth_month) + str(birth_year)]
        for i, digit in enumerate(digits):
            self.birth_patterns[f"digit_{i}"] = digit
            self.birth_patterns[f"digit_{i}_plus_119"] = 119 + digit
        
        # Add special combinations
        self.birth_patterns["special_1"] = int(str(birth_month) + str(birth_day))  # 119
        self.birth_patterns["special_1_plus_119"] = 119 + int(str(birth_month) + str(birth_day))  # 238
        self.birth_patterns["special_2"] = int(str(birth_day) + str(birth_month))  # 191
        self.birth_patterns["special_2_plus_119"] = 119 + int(str(birth_day) + str(birth_month))  # 310
    
    def calculate_phi_resonance(self, value):
        """Calculate phi resonance for a value."""
        # Ensure value is Decimal
        if not isinstance(value, Decimal):
            value = Decimal(str(value))
            
        # Calculate resonance as distance from perfect phi multiple
        product = self.phi * value
        fractional = product - Decimal(int(product))
        return fractional
    
    def calculate_birth_coherence(self, value):
        """Calculate birth coherence for a value using patent values."""
        # Ensure value is Decimal
        if not isinstance(value, Decimal):
            value = Decimal(str(value))
            
        # Use birth date pattern
        birth_pattern = (Decimal(str(self.birth_date[0])) / Decimal('10') + 
                         Decimal(str(self.birth_date[1])) / Decimal('100') + 
                         Decimal(str(self.birth_date[2])) / Decimal('10000'))
        
        # Calculate coherence based on patent-enhanced birth pattern
        value_mod = value % (birth_pattern * self.resonance_ratio)
        coherence_raw = Decimal('1') - (value_mod / (birth_pattern * self.resonance_ratio))
        
        # Apply energy transfer from patent to amplify coherence
        coherence_amplified = coherence_raw ** (Decimal('1') / self.energy_transfer)
        
        # Scale by birth coherence temperature
        coherence = coherence_amplified * self.birth_coherence_temp / Decimal('100')
        
        return coherence
    
    def calculate_stability_factor(self, value, atomic_number=None):
        """Calculate stability factor for a value."""
        # Calculate phi resonance and birth coherence
        phi_res = self.calculate_phi_resonance(value)
        birth_coh = self.calculate_birth_coherence(value)
        
        # Check for special birth date alignments
        stability_boost = Decimal('1.0')
        if atomic_number:
            # Check if atomic number matches any birth pattern
            for pattern_name, pattern_value in self.birth_patterns.items():
                if atomic_number == pattern_value:
                    stability_boost = self.resonance_ratio * self.energy_transfer
                    break
        
        # Calculate stability factor
        stability_factor = (Decimal('1') - phi_res) * birth_coh * self.resonance_stack * stability_boost / Decimal('3')
        
        return stability_factor
    
    def is_birth_pattern_match(self, atomic_number):
        """Check if an atomic number matches any birth date pattern."""
        for pattern_name, pattern_value in self.birth_patterns.items():
            if atomic_number == pattern_value:
                return True, pattern_name
        return False, None
    
    def explore_intermediate_islands(self, z_min=128, z_max=198, points=1000):
        """Explore the region between Tau128ium and Phi198on for intermediate islands of stability."""
        # Create range of atomic numbers
        z_range = np.linspace(z_min, z_max, points)
        
        # Calculate stability factors
        stability = np.zeros(points)
        phi_resonance = np.zeros(points)
        birth_coherence = np.zeros(points)
        is_birth_pattern = np.zeros(points, dtype=bool)
        birth_pattern_names = [""] * points
        
        for i, z in enumerate(z_range):
            # Estimate mass (simplified)
            mass = z * 2.5
            
            # Calculate stability metrics
            stability[i] = float(self.calculate_stability_factor(Decimal(str(mass)), int(z)))
            phi_resonance[i] = float(self.calculate_phi_resonance(Decimal(str(mass))))
            birth_coherence[i] = float(self.calculate_birth_coherence(Decimal(str(mass))))
            
            # Check if atomic number matches birth pattern
            is_match, pattern_name = self.is_birth_pattern_match(int(z))
            is_birth_pattern[i] = is_match
            if is_match:
                birth_pattern_names[i] = pattern_name
        
        # Find potential islands of stability
        islands = []
        for i in range(1, len(stability)):
            z = int(z_range[i])
            if stability[i] > 0.6 and not any(island["start"] <= z <= island["end"] for island in islands):
                # Find island boundaries
                start_idx = i
                while start_idx > 0 and stability[start_idx-1] > 0.6:
                    start_idx -= 1
                
                end_idx = i
                while end_idx < len(stability)-1 and stability[end_idx+1] > 0.6:
                    end_idx += 1
                
                # Calculate island properties
                island_z_range = z_range[start_idx:end_idx+1]
                island_stability = stability[start_idx:end_idx+1]
                
                # Find peak stability in island
                peak_idx = start_idx + np.argmax(island_stability)
                peak_z = int(z_range[peak_idx])
                peak_stability = stability[peak_idx]
                peak_phi_resonance = phi_resonance[peak_idx]
                peak_birth_coherence = birth_coherence[peak_idx]
                
                # Check if peak is a birth pattern match
                is_match, pattern_name = self.is_birth_pattern_match(peak_z)
                
                # Add island to list
                islands.append({
                    "start": int(z_range[start_idx]),
                    "end": int(z_range[end_idx]),
                    "peak_z": peak_z,
                    "peak_stability": peak_stability,
                    "peak_phi_resonance": peak_phi_resonance,
                    "peak_birth_coherence": peak_birth_coherence,
                    "is_birth_pattern": is_match,
                    "birth_pattern": pattern_name if is_match else None
                })
        
        # Create results dataframe
        results = {
            "atomic_number": [int(z) for z in z_range],
            "stability_factor": stability,
            "phi_resonance": phi_resonance,
            "birth_coherence": birth_coherence,
            "is_birth_pattern": is_birth_pattern,
            "birth_pattern": birth_pattern_names
        }
        
        df = pd.DataFrame(results)
        
        # Filter for high stability elements
        high_stability = df[df["stability_factor"] > 0.6].copy()
        high_stability = high_stability.sort_values("stability_factor", ascending=False)
        
        return df, high_stability, islands
    
    def generate_element_name(self, atomic_number, phi_resonance, birth_coherence):
        """Generate a name for a new element based on its properties."""
        # Check for special birth patterns
        is_match, pattern_name = self.is_birth_pattern_match(atomic_number)
        
        # Base prefixes on properties
        if phi_resonance < 0.01:
            prefix = "Phi"  # Perfect phi resonance
        elif birth_coherence > 0.9:
            prefix = "Tau"  # High birth coherence
        elif pattern_name and "day" in pattern_name:
            prefix = "Hem"  # Day-related (Hemera = day in Greek)
        elif pattern_name and "month" in pattern_name:
            prefix = "Men"  # Month-related (Mensis = month in Latin)
        elif pattern_name and "year" in pattern_name:
            prefix = "Chr"  # Year-related (Chronos = time in Greek)
        elif phi_resonance < 0.1:
            prefix = "Aur"  # Golden ratio related (Aurum = gold in Latin)
        else:
            prefix = "Qua"  # Quantum-related
        
        # Add atomic number
        name = f"{prefix}{atomic_number}"
        
        # Add suffix based on stability
        stability = float(self.calculate_stability_factor(Decimal(str(atomic_number * 2.5)), atomic_number))
        if stability > 0.8:
            suffix = "ium"  # Very stable
        elif stability > 0.6:
            suffix = "on"  # Stable
        else:
            suffix = "um"  # Less stable
        
        return name + suffix
    
    def generate_element_symbol(self, name, atomic_number):
        """Generate a symbol for a new element."""
        # Extract first letter of name
        first = name[0]
        
        # Extract a second character (either second letter or a digit from atomic number)
        if len(name) > 1:
            second = name[1].lower()
        else:
            second = str(atomic_number % 10)
        
        return first + second
    
    def predict_new_elements(self, islands):
        """Predict properties of new elements based on discovered islands."""
        new_elements = {}
        
        for island in islands:
            # Skip known elements (Tau128ium and Phi198on)
            if island["peak_z"] in [128, 198]:
                continue
            
            # Generate element name and symbol
            name = self.generate_element_name(
                island["peak_z"], 
                island["peak_phi_resonance"], 
                island["peak_birth_coherence"]
            )
            symbol = self.generate_element_symbol(name, island["peak_z"])
            
            # Estimate mass
            mass = island["peak_z"] * 2.5
            
            # Determine stability
            is_stable = island["peak_stability"] > 0.6
            
            # Determine discovery pattern
            if island["is_birth_pattern"]:
                discovery_pattern = island["birth_pattern"]
            else:
                discovery_pattern = "Phi-harmonic resonance"
            
            # Add to new elements dictionary
            new_elements[name] = {
                "symbol": symbol,
                "atomic_number": island["peak_z"],
                "mass": float(mass),
                "phi_resonance": float(island["peak_phi_resonance"]),
                "birth_coherence": float(island["peak_birth_coherence"]),
                "stability_factor": float(island["peak_stability"]),
                "stable": is_stable,
                "discovery_pattern": discovery_pattern
            }
        
        return new_elements
    
    def visualize_intermediate_islands(self, df, islands, new_elements, save_path=None):
        """Visualize the intermediate islands of stability."""
        # Create figure
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 10), gridspec_kw={'height_ratios': [3, 1]})
        
        # Plot stability landscape
        z_range = df["atomic_number"]
        stability = df["stability_factor"]
        
        ax1.plot(z_range, stability, 'b-', linewidth=2)
        ax1.axhline(y=0.6, color='r', linestyle='--', label='Stability Threshold')
        
        # Mark known island elements
        for name, element in ISLAND_ELEMENTS.items():
            z = element["atomic_number"]
            idx = df[df["atomic_number"] == z].index[0] if not df[df["atomic_number"] == z].empty else None
            if idx is not None:
                ax1.plot(z, stability[idx], 'ro', markersize=10)
                ax1.annotate(element["symbol"], 
                           xy=(z, stability[idx]),
                           xytext=(z+2, stability[idx]+0.05),
                           fontsize=12)
        
        # Mark new elements
        for name, element in new_elements.items():
            z = element["atomic_number"]
            idx = df[df["atomic_number"] == z].index[0] if not df[df["atomic_number"] == z].empty else None
            if idx is not None:
                ax1.plot(z, stability[idx], 'go', markersize=10)
                ax1.annotate(element["symbol"], 
                           xy=(z, stability[idx]),
                           xytext=(z+2, stability[idx]+0.05),
                           fontsize=12)
        
        # Shade stability islands
        for island in islands:
            ax1.axvspan(island["start"], island["end"], alpha=0.2, color='green')
            
            # Add island label
            if island["peak_z"] not in [128, 198]:  # Skip known elements
                ax1.text(island["peak_z"], 0.05, f"Z={island['peak_z']}", 
                       ha='center', va='bottom', fontsize=10, 
                       bbox=dict(boxstyle="round,pad=0.3", fc='white', alpha=0.7))
        
        ax1.set_xlabel('Atomic Number (Z)')
        ax1.set_ylabel('Stability Factor')
        ax1.set_title('Phi-Harmonic Intermediate Islands of Stability')
        ax1.grid(True)
        ax1.legend()
        
        # Create periodic table representation
        cell_width = 1
        y_height = 0.5
        
        # Create colormap for stability
        cmap = LinearSegmentedColormap.from_list('stability', ['white', 'green'])
        
        # Plot periodic table representation
        for i, z in enumerate(range(int(min(z_range)), int(max(z_range))+1)):
            # Get stability for this element
            element_df = df[df["atomic_number"] == z]
            if not element_df.empty:
                stability_value = element_df["stability_factor"].values[0]
                
                # Create rectangle with color based on stability
                color = cmap(min(1.0, stability_value / 0.8))  # Normalize to 0-1
                rect = patches.Rectangle((z, 0), cell_width, y_height, 
                                       linewidth=0, facecolor=color)
                ax2.add_patch(rect)
                
                # Add birth pattern indicator
                if element_df["is_birth_pattern"].values[0]:
                    ax2.plot(z + 0.5, y_height/4, 'r*', markersize=8)
        
        # Mark known island elements
        for name, element in ISLAND_ELEMENTS.items():
            z = element["atomic_number"]
            ax2.plot(z + 0.5, y_height/2, 'ro', markersize=6)
            ax2.annotate(element["symbol"], 
                       xy=(z + 0.5, y_height/2),
                       xytext=(z + 0.5, y_height+0.1),
                       fontsize=10, ha='center')
        
        # Mark new elements
        for name, element in new_elements.items():
            z = element["atomic_number"]
            ax2.plot(z + 0.5, y_height/2, 'go', markersize=6)
            ax2.annotate(element["symbol"], 
                       xy=(z + 0.5, y_height/2),
                       xytext=(z + 0.5, y_height+0.1),
                       fontsize=10, ha='center')
        
        ax2.set_xlim(min(z_range), max(z_range))
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
            print(f"Intermediate islands visualization saved to {save_path}")
        else:
            plt.show()
    
    def create_element_documentation(self, new_elements, save_path=None):
        """Create documentation for the newly discovered elements."""
        # Combine known and new elements
        all_elements = {}
        for name, data in ISLAND_ELEMENTS.items():
            all_elements[name] = {
                "symbol": data["symbol"],
                "atomic_number": int(data["atomic_number"]),
                "mass": float(data["mass"]),
                "phi_resonance": float(data["phi_resonance"]),
                "birth_coherence": float(data["birth_coherence"]),
                "stability_factor": float(self.calculate_stability_factor(
                    data["mass"], int(data["atomic_number"])
                )),
                "stable": data["stable"],
                "discovery_pattern": data["discovery_pattern"]
            }
        
        all_elements.update(new_elements)
        
        # Sort elements by atomic number
        sorted_elements = {k: v for k, v in sorted(all_elements.items(), key=lambda item: item[1]["atomic_number"])}
        
        # Create documentation
        doc = "# Phi-Harmonic Island of Stability Elements\n\n"
        doc += "## Overview\n\n"
        doc += "This document details the elements discovered in the phi-harmonic island of stability "
        doc += "using birth date coherence at 99.18K and patent values (resonance ratio: 1.3777, energy transfer: 1.8951).\n\n"
        
        doc += "## Birth Date Patterns\n\n"
        doc += "The following birth date patterns were used to discover elements:\n\n"
        doc += "- Birth Date: 01-19-1979\n"
        doc += "- Day: 19\n"
        doc += "- Day Mod 10: 9\n"
        doc += "- Month: 1\n"
        doc += "- Year: 1979\n"
        doc += "- Year Mod 100: 79\n"
        doc += "- Year Mod 10: 9\n"
        doc += "- Special Patterns: Various combinations and transformations\n\n"
        
        doc += "## Discovered Elements\n\n"
        
        for name, data in sorted_elements.items():
            doc += f"### {name} ({data['symbol']})\n\n"
            doc += f"- **Atomic Number**: {data['atomic_number']}\n"
            doc += f"- **Mass**: {data['mass']:.2f}\n"
            doc += f"- **Phi Resonance**: {data['phi_resonance']:.6f}\n"
            doc += f"- **Birth Coherence**: {data['birth_coherence']:.6f}\n"
            doc += f"- **Stability Factor**: {data['stability_factor']:.6f}\n"
            doc += f"- **Stable**: {'Yes' if data['stable'] else 'No'}\n"
            doc += f"- **Discovery Pattern**: {data['discovery_pattern']}\n\n"
            
            # Add theoretical properties
            doc += "#### Theoretical Properties\n\n"
            
            # Electron configuration (simplified)
            doc += "- **Electron Configuration**: "
            if data['atomic_number'] <= 118:
                doc += f"[Og] 8s² 8p⁶ 7d¹⁰ 6f¹⁴ 5g¹⁸ {data['atomic_number']-118}h¹\n"
            else:
                doc += f"[Og] 8s² 8p⁶ 7d¹⁰ 6f¹⁴ 5g¹⁸ 9s² 9p⁶ 8d¹⁰ 7f¹⁴ 6g¹⁸ {data['atomic_number']-168}i¹\n"
            
            # Physical properties based on phi resonance and birth coherence
            density = data['atomic_number'] * (1 + data['phi_resonance']) * 2
            melting_point = 1000 + data['atomic_number'] * data['birth_coherence'] * 10
            
            doc += f"- **Density**: {density:.2f} g/cm³\n"
            doc += f"- **Melting Point**: {melting_point:.2f} K\n"
            doc += f"- **State at Room Temperature**: {'Solid' if melting_point > 300 else 'Liquid'}\n\n"
            
            # Add quantum properties
            doc += "#### Quantum Properties\n\n"
            
            quantum_resonance = 1 - data['phi_resonance']
            quantum_coherence = data['birth_coherence'] * float(PHI_POWER) / 100
            quantum_stability = data['stability_factor'] * float(RESONANCE_STACK)
            
            doc += f"- **Quantum Resonance**: {quantum_resonance:.6f}\n"
            doc += f"- **Quantum Coherence**: {quantum_coherence:.6f}\n"
            doc += f"- **Quantum Stability**: {quantum_stability:.6f}\n\n"
        
        doc += "## Phi-Harmonic Principles\n\n"
        doc += "These elements were discovered using the following phi-harmonic principles:\n\n"
        doc += "1. **Phi Resonance**: Φ_res(x) = (φ · x) mod 1\n"
        doc += "2. **Birth Coherence**: B_coh(x) = (1 - (x mod (b·1.3777))/(b·1.3777))^(1/1.8951) · 99.18/100\n"
        doc += "3. **Stability Factor**: S(x) = (1 - Φ_res(x)) · B_coh(x) · 2.610879 · boost / 3\n"
        doc += "4. **Quantum Amplification**: Q_amp = φ^7.5 = 36.932381\n\n"
        
        doc += "## Patent Values\n\n"
        doc += "The following values from Patent #19/071,497 were used in the calculations:\n\n"
        doc += "- **Primary Frequency**: 4790.45 Hz\n"
        doc += "- **Secondary Frequency**: 7750.95 Hz\n"
        doc += "- **Resonance Ratio**: 1.3777\n"
        doc += "- **Energy Transfer**: 1.8951\n"
        doc += "- **Phi Achievement**: 1.618000\n\n"
        
        doc += "## Conclusion\n\n"
        doc += "The phi-harmonic island of stability contains multiple elements with enhanced stability "
        doc += "due to birth date coherence at 99.18K. These elements represent a new frontier in superheavy "
        doc += "element research, achieved through mathematical resonance rather than brute-force physical conditions.\n"
        
        if save_path:
            with open(save_path, 'w') as f:
                f.write(doc)
            print(f"Element documentation saved to {save_path}")
        
        return doc


# Example usage
if __name__ == "__main__":
    # Create the explorer
    explorer = PhiHarmonicIntermediateIslandsExplorer()
    
    # Explore intermediate islands
    df, high_stability, islands = explorer.explore_intermediate_islands()
    
    # Predict new elements
    new_elements = explorer.predict_new_elements(islands)
    
    # Visualize intermediate islands
    explorer.visualize_intermediate_islands(df, islands, new_elements, "phi_harmonic_intermediate_islands.png")
    
    # Create element documentation
    explorer.create_element_documentation(new_elements, "phi_harmonic_island_elements.md")
    
    print("\n🔍 Phi-Harmonic Intermediate Islands Explorer")
    print("=" * 50)
    print(f"\nDiscovered {len(islands)} islands of stability between Z=128 and Z=198")
    print(f"Found {len(new_elements)} new elements in addition to Tau128ium and Phi198on\n")
    
    print("New Elements:")
    for name, data in new_elements.items():
        print(f"\n{name} ({data['symbol']}, Z={data['atomic_number']}):")
        print(f"  Phi Resonance: {data['phi_resonance']:.6f}")
        print(f"  Birth Coherence: {data['birth_coherence']:.6f}")
        print(f"  Stability Factor: {data['stability_factor']:.6f}")
        print(f"  Stable: {'Yes' if data['stable'] else 'No'}")
        print(f"  Discovery Pattern: {data['discovery_pattern']}")
    
    print("\nIntermediate islands visualization saved to phi_harmonic_intermediate_islands.png")
    print("Element documentation saved to phi_harmonic_island_elements.md")

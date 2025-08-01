"""
QUANTUM PERIODIC VISUALIZER
Creates a visual representation of the periodic table including φ-harmonic discoveries
"""

import os
import sys
import json
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle, Polygon
from matplotlib.colors import LinearSegmentedColormap, Normalize
import matplotlib.patheffects as path_effects
from datetime import datetime

# Define φ (phi) constant
PHI = (1 + np.sqrt(5)) / 2

class QuantumPeriodicVisualizer:
    def __init__(self):
        # Load standard elements
        self.standard_elements = self._load_standard_elements()
        
        # Load discovered elements
        self.discovered_elements = self._load_discovered_elements()
        
        # Combined elements
        self.all_elements = {**self.standard_elements, **self.discovered_elements}
        
        # Create output directory
        self.output_dir = 'quantum_visualizations'
        os.makedirs(self.output_dir, exist_ok=True)
        
        # Define color maps for φ-resonance
        self.phi_cmap = self._create_phi_colormap()
    
    def _load_standard_elements(self):
        """Load standard elements from ASCII chart"""
        elements = {}
        
        try:
            with open('/Users/vaughnscott/Documents/fraymus_shit/Ascii_Element_Chart.txt', 'r') as f:
                lines = f.readlines()
                
            current_element = None
            for line in lines:
                line = line.strip()
                if line.startswith('Symbol:'):
                    symbol = line.split('Symbol:')[1].strip()
                    current_element = {'symbol': symbol}
                elif line.startswith('Name:') and current_element:
                    current_element['name'] = line.split('Name:')[1].strip()
                elif line.startswith('Atomic Number:') and current_element:
                    current_element['number'] = int(line.split('Atomic Number:')[1].strip())
                elif line.startswith('Mass:') and current_element:
                    mass_str = line.split('Mass:')[1].strip()
                    try:
                        current_element['mass'] = float(mass_str)
                    except ValueError:
                        current_element['mass'] = 0.0
                elif line.startswith('Group:') and current_element:
                    group_str = line.split('Group:')[1].strip()
                    try:
                        current_element['group'] = int(group_str)
                    except ValueError:
                        current_element['group'] = 0
                elif line.startswith('Period:') and current_element:
                    period_str = line.split('Period:')[1].strip()
                    try:
                        current_element['period'] = int(period_str)
                    except ValueError:
                        current_element['period'] = 0
                
                # If we have a complete element, add it
                if current_element and 'symbol' in current_element and 'name' in current_element and 'number' in current_element:
                    # Calculate φ-resonance for standard elements
                    if 'mass' in current_element and current_element['mass'] > 0:
                        phi_res = (PHI * current_element['mass']) % 1
                        current_element['phi_resonance'] = phi_res
                    else:
                        current_element['phi_resonance'] = 0.5  # Neutral if no mass
                    
                    # Add element to dict
                    elements[current_element['symbol']] = current_element
                    current_element = None
        
        except Exception as e:
            print(f"Error loading standard elements: {e}")
        
        return elements
    
    def _load_discovered_elements(self):
        """Load discovered elements from quantum discoveries"""
        elements = {}
        
        # Try to load from summary file
        try:
            # First check extended summary
            if os.path.exists('/Users/vaughnscott/Documents/fraymus_shit/quantum_extended_results/extended_summary.txt'):
                with open('/Users/vaughnscott/Documents/fraymus_shit/quantum_extended_results/extended_summary.txt', 'r') as f:
                    lines = f.readlines()
                
                current_element = None
                in_elements_section = False
                
                for line in lines:
                    line = line.strip()
                    
                    if line == "ALL DISCOVERED ELEMENTS:":
                        in_elements_section = True
                        continue
                    
                    if in_elements_section and line.startswith('--'):
                        continue
                    
                    if in_elements_section and ':' in line and not line.startswith(' '):
                        # New element
                        parts = line.split(':', 1)
                        symbol = parts[0].strip()
                        name_parts = parts[1].strip().split('(')
                        name = name_parts[0].strip()
                        
                        # Extract Z and mass
                        props = name_parts[1].replace(')', '').split(',')
                        number = int(props[0].split('=')[1])
                        mass = float(props[1].split('=')[1])
                        
                        current_element = {
                            'symbol': symbol,
                            'name': name,
                            'number': number,
                            'mass': mass,
                            'is_discovered': True
                        }
                    
                    elif in_elements_section and current_element and line.startswith('  φ-Resonance:'):
                        current_element['phi_resonance'] = float(line.split(':')[1].strip())
                    
                    elif in_elements_section and current_element and line.startswith('  Parent Elements:'):
                        current_element['parents'] = line.split(':')[1].strip().split(', ')
                    
                    elif in_elements_section and current_element and line.startswith('  Discovery Time:'):
                        current_element['discovery_time'] = line.split(':')[1].strip()
                        
                        # Set group and period based on atomic number
                        if current_element['number'] <= 118:
                            # Use standard periodic table layout for elements up to 118
                            for std_symbol, std_element in self.standard_elements.items():
                                if std_element['number'] == current_element['number']:
                                    current_element['group'] = std_element['group']
                                    current_element['period'] = std_element['period']
                                    break
                        else:
                            # For new elements beyond 118, place in extended regions
                            current_element['group'] = (current_element['number'] % 18) + 1
                            current_element['period'] = (current_element['number'] // 18) + 7
                        
                        # Add to elements dict
                        elements[current_element['symbol']] = current_element
                        current_element = None
                    
                    elif in_elements_section and line == "":
                        # Empty line after element
                        if current_element and 'symbol' in current_element:
                            # Add to elements dict if not already added
                            elements[current_element['symbol']] = current_element
                            current_element = None
            
            # Also check Quantum_Discoveries.txt
            if os.path.exists('/Users/vaughnscott/Documents/fraymus_shit/Quantum_Discoveries.txt'):
                with open('/Users/vaughnscott/Documents/fraymus_shit/Quantum_Discoveries.txt', 'r') as f:
                    content = f.read()
                
                # Split by discovery sections
                sections = content.split('NEW ELEMENT DISCOVERED:')
                
                for section in sections[1:]:  # Skip first empty section
                    lines = section.strip().split('\n')
                    
                    # First line has symbol and name
                    header = lines[0].strip()
                    symbol, name = header.split(' - ')
                    symbol = symbol.strip()
                    name = name.strip()
                    
                    # Skip if already loaded
                    if symbol in elements:
                        continue
                    
                    current_element = {
                        'symbol': symbol,
                        'name': name,
                        'is_discovered': True
                    }
                    
                    # Parse properties
                    for line in lines:
                        line = line.strip()
                        if line.startswith('Atomic Number:'):
                            current_element['number'] = int(line.split(':')[1].strip())
                        elif line.startswith('Mass:'):
                            current_element['mass'] = float(line.split(':')[1].strip())
                        elif line.startswith('Group:'):
                            group_period = line.split(':')[1].strip()
                            if ',' in group_period:
                                group = group_period.split(',')[0].strip()
                                current_element['group'] = int(group)
                        elif line.startswith('Period:'):
                            current_element['period'] = int(line.split(':')[1].strip())
                        elif line.startswith('φ-Resonance:'):
                            current_element['phi_resonance'] = float(line.split(':')[1].strip())
                        elif line.startswith('Parent Elements:'):
                            current_element['parents'] = line.split(':')[1].strip().split(', ')
                        elif line.startswith('Discovery Time:'):
                            current_element['discovery_time'] = line.split(':')[1].strip()
                    
                    # Add to elements dict if complete
                    if 'symbol' in current_element and 'number' in current_element and 'mass' in current_element:
                        elements[current_element['symbol']] = current_element
        
        except Exception as e:
            print(f"Error loading discovered elements: {e}")
        
        return elements
    
    def _create_phi_colormap(self):
        """Create a colormap for φ-resonance visualization"""
        # Define colors for different φ-resonance ranges
        colors = [
            (0.0, 'blue'),      # φ-Resonant (0.0)
            (0.2, 'cyan'),      # Near φ-Resonant
            (0.4, 'green'),     # Approaching φ-Neutral
            (0.5, 'yellow'),    # φ-Neutral (0.5)
            (0.6, 'orange'),    # Approaching Anti-φ-Resonant
            (0.8, 'red'),       # Near Anti-φ-Resonant
            (1.0, 'purple')     # Anti-φ-Resonant (1.0)
        ]
        
        # Create colormap
        cmap_name = 'phi_resonance'
        cm_points = [(x[0], x[1]) for x in colors]
        cmap = LinearSegmentedColormap.from_list(cmap_name, cm_points, N=256)
        
        return cmap
    
    def create_standard_periodic_table(self, save_path=None):
        """Create a standard periodic table visualization"""
        # Create figure
        fig, ax = plt.subplots(figsize=(20, 10))
        
        # Set background color
        fig.patch.set_facecolor('#f0f0f0')
        ax.set_facecolor('#f0f0f0')
        
        # Define element box size
        box_size = 1.0
        
        # Track max group and period for axis limits
        max_group = 0
        max_period = 0
        
        # Draw elements
        for symbol, element in self.standard_elements.items():
            if 'group' not in element or 'period' not in element:
                continue
                
            group = element['group']
            period = element['period']
            
            # Update max values
            max_group = max(max_group, group)
            max_period = max(max_period, period)
            
            # Skip lanthanides and actinides in main table
            if (period == 6 and 3 <= group <= 16) or (period == 7 and 3 <= group <= 16):
                continue
            
            # Draw element box
            self._draw_element_box(ax, element, group, period, box_size, is_standard=True)
        
        # Draw lanthanides and actinides in separate rows
        lanthanide_period = max_period + 2
        actinide_period = max_period + 3
        
        for symbol, element in self.standard_elements.items():
            if 'group' not in element or 'period' not in element:
                continue
                
            group = element['group']
            period = element['period']
            
            # Lanthanides
            if period == 6 and 3 <= group <= 16:
                self._draw_element_box(ax, element, group - 2, lanthanide_period, box_size, is_standard=True)
            
            # Actinides
            if period == 7 and 3 <= group <= 16:
                self._draw_element_box(ax, element, group - 2, actinide_period, box_size, is_standard=True)
        
        # Set axis limits with padding
        ax.set_xlim(0, max_group + 1)
        ax.set_ylim(0, actinide_period + 1)
        
        # Remove axis ticks and labels
        ax.set_xticks([])
        ax.set_yticks([])
        
        # Add title
        ax.set_title('Standard Periodic Table', fontsize=24, pad=20)
        
        # Add colorbar for φ-resonance
        norm = Normalize(vmin=0, vmax=1)
        sm = plt.cm.ScalarMappable(cmap=self.phi_cmap, norm=norm)
        sm.set_array([])
        cbar = plt.colorbar(sm, ax=ax, orientation='horizontal', pad=0.05)
        cbar.set_label('φ-Resonance', fontsize=14)
        
        # Add legend for element types
        self._add_element_legend(ax)
        
        # Save if path provided
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
            print(f"Standard periodic table saved to {save_path}")
        
        return fig
    
    def create_quantum_periodic_table(self, save_path=None):
        """Create a quantum periodic table with discovered elements"""
        # Create figure
        fig, ax = plt.subplots(figsize=(22, 12))
        
        # Set background color - darker for quantum table
        fig.patch.set_facecolor('#1a1a2e')
        ax.set_facecolor('#1a1a2e')
        
        # Define element box size
        box_size = 1.0
        
        # Track max group and period for axis limits
        max_group = 0
        max_period = 0
        
        # Draw standard elements
        for symbol, element in self.standard_elements.items():
            if 'group' not in element or 'period' not in element:
                continue
                
            group = element['group']
            period = element['period']
            
            # Update max values
            max_group = max(max_group, group)
            max_period = max(max_period, period)
            
            # Skip lanthanides and actinides in main table
            if (period == 6 and 3 <= group <= 16) or (period == 7 and 3 <= group <= 16):
                continue
            
            # Draw element box
            self._draw_element_box(ax, element, group, period, box_size, is_standard=True)
        
        # Draw lanthanides and actinides in separate rows
        lanthanide_period = max_period + 2
        actinide_period = max_period + 3
        
        for symbol, element in self.standard_elements.items():
            if 'group' not in element or 'period' not in element:
                continue
                
            group = element['group']
            period = element['period']
            
            # Lanthanides
            if period == 6 and 3 <= group <= 16:
                self._draw_element_box(ax, element, group - 2, lanthanide_period, box_size, is_standard=True)
            
            # Actinides
            if period == 7 and 3 <= group <= 16:
                self._draw_element_box(ax, element, group - 2, actinide_period, box_size, is_standard=True)
        
        # Draw discovered elements in a new section
        discovery_period_start = actinide_period + 2
        
        # Add a title for the discovery section
        ax.text(max_group/2, discovery_period_start - 0.5, 'φ-HARMONIC DISCOVERIES', 
                fontsize=18, ha='center', va='center', color='white',
                path_effects=[path_effects.withStroke(linewidth=2, foreground='black')])
        
        # Draw discovered elements
        discovery_row = 0
        discovery_col = 0
        max_cols = max_group
        
        for symbol, element in self.discovered_elements.items():
            # Calculate position
            group = discovery_col + 1
            period = discovery_period_start + discovery_row
            
            # Draw element box with special styling
            self._draw_element_box(ax, element, group, period, box_size, is_standard=False)
            
            # Update position for next element
            discovery_col += 1
            if discovery_col >= max_cols:
                discovery_col = 0
                discovery_row += 1
        
        # Update max period for axis limits
        max_period = discovery_period_start + discovery_row
        
        # Set axis limits with padding
        ax.set_xlim(0, max_group + 1)
        ax.set_ylim(0, max_period + 2)
        
        # Remove axis ticks and labels
        ax.set_xticks([])
        ax.set_yticks([])
        
        # Add title
        timestamp = datetime.now().strftime("%Y-%m-%d")
        ax.set_title(f'Quantum Periodic Table with φ-Harmonic Discoveries ({timestamp})', 
                    fontsize=24, pad=20, color='white')
        
        # Add colorbar for φ-resonance
        norm = Normalize(vmin=0, vmax=1)
        sm = plt.cm.ScalarMappable(cmap=self.phi_cmap, norm=norm)
        sm.set_array([])
        cbar = plt.colorbar(sm, ax=ax, orientation='horizontal', pad=0.05)
        cbar.set_label('φ-Resonance', fontsize=14, color='white')
        cbar.ax.yaxis.set_tick_params(color='white')
        cbar.outline.set_edgecolor('white')
        plt.setp(plt.getp(cbar.ax.axes, 'xticklabels'), color='white')
        
        # Add φ-resonance categories
        self._add_resonance_categories(ax)
        
        # Add legend for element types
        self._add_element_legend(ax, text_color='white')
        
        # Add φ-harmonic analysis
        self._add_phi_harmonic_analysis(ax)
        
        # Save if path provided
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
            print(f"Quantum periodic table saved to {save_path}")
        
        return fig
    
    def _draw_element_box(self, ax, element, group, period, size, is_standard=True):
        """Draw a single element box on the periodic table"""
        # Extract element properties
        symbol = element['symbol']
        name = element.get('name', '')
        number = element.get('number', 0)
        mass = element.get('mass', 0.0)
        phi_resonance = element.get('phi_resonance', 0.5)
        is_discovered = element.get('is_discovered', False)
        
        # Calculate position (invert period for top-down layout)
        x = group
        y = -period
        
        # Determine box color based on φ-resonance
        box_color = self.phi_cmap(phi_resonance)
        
        # Adjust for discovered elements
        if is_discovered:
            # Add glow effect for discovered elements
            glow = Circle((x, y), size * 0.7, color='white', alpha=0.2)
            ax.add_patch(glow)
            
            # Add starburst for discovered elements
            self._draw_starburst(ax, x, y, size * 0.8)
        
        # Create element box
        box = Rectangle((x - size/2, y - size/2), size, size, 
                       facecolor=box_color, edgecolor='black', 
                       linewidth=1.5 if is_discovered else 0.8,
                       alpha=0.9 if is_standard else 1.0,
                       zorder=10)
        ax.add_patch(box)
        
        # Determine text color based on box color brightness
        brightness = 0.299 * box_color[0] + 0.587 * box_color[1] + 0.114 * box_color[2]
        text_color = 'black' if brightness > 0.5 else 'white'
        
        # Add element information
        # Symbol
        symbol_text = ax.text(x, y, symbol, 
                             ha='center', va='center', 
                             fontsize=14 if is_standard else 16,
                             fontweight='bold',
                             color=text_color,
                             zorder=20)
        
        # Add outline to text for better visibility
        symbol_text.set_path_effects([path_effects.withStroke(linewidth=1, foreground='black')])
        
        # Atomic number (top left)
        ax.text(x - size/2 + 0.1, y + size/2 - 0.15, str(number), 
               ha='left', va='top', 
               fontsize=8 if is_standard else 10,
               color=text_color,
               zorder=20)
        
        # For discovered elements, add more details
        if is_discovered:
            # Add φ-resonance value (bottom)
            phi_text = f"φ: {phi_resonance:.3f}"
            ax.text(x, y - size/2 + 0.15, phi_text, 
                   ha='center', va='bottom', 
                   fontsize=8,
                   color=text_color,
                   zorder=20)
    
    def _draw_starburst(self, ax, x, y, size):
        """Draw a starburst effect behind discovered elements"""
        n_points = 8
        inner_radius = size * 0.5
        outer_radius = size * 0.7
        
        angles = np.linspace(0, 2*np.pi, n_points, endpoint=False)
        angles = angles + np.pi/n_points  # Offset to make points look better
        
        # Create starburst points
        xs = []
        ys = []
        
        for i, angle in enumerate(angles):
            # Alternate between inner and outer radius
            radius = outer_radius if i % 2 == 0 else inner_radius
            xs.append(x + radius * np.cos(angle))
            ys.append(y + radius * np.sin(angle))
        
        # Create polygon
        starburst = Polygon(list(zip(xs, ys)), closed=True, 
                           facecolor='gold', edgecolor='none', 
                           alpha=0.3, zorder=5)
        ax.add_patch(starburst)
    
    def _add_element_legend(self, ax, text_color='black'):
        """Add a legend for element types"""
        # Add legend for standard vs discovered elements
        # Standard element
        standard_box = Rectangle((0, 0), 0.8, 0.8, 
                                facecolor='lightgray', edgecolor='black', 
                                linewidth=0.8, alpha=0.9)
        
        # Discovered element
        discovered_box = Rectangle((0, 0), 0.8, 0.8, 
                                  facecolor='gold', edgecolor='black', 
                                  linewidth=1.5, alpha=1.0)
        
        # Add legend
        ax.legend([standard_box, discovered_box], 
                 ['Standard Element', 'φ-Harmonic Discovery'],
                 loc='upper right', framealpha=0.7,
                 labelcolor=text_color)
    
    def _add_resonance_categories(self, ax):
        """Add φ-resonance categories explanation"""
        categories = [
            ('φ-Resonant', '< 0.1', 'blue'),
            ('Near φ-Resonant', '0.1-0.2', 'cyan'),
            ('φ-Transitional', '0.2-0.8', 'green'),
            ('φ-Neutral', '≈ 0.5', 'yellow'),
            ('Anti-φ-Resonant', '> 0.9', 'purple')
        ]
        
        # Position at bottom left
        x_start = 1
        y_start = -18
        
        # Add title
        ax.text(x_start, y_start, 'φ-RESONANCE CATEGORIES:', 
               fontsize=12, color='white', fontweight='bold',
               path_effects=[path_effects.withStroke(linewidth=1, foreground='black')])
        
        # Add categories
        for i, (name, value, color) in enumerate(categories):
            y = y_start - (i + 1) * 0.8
            
            # Add colored box
            box = Rectangle((x_start, y), 0.6, 0.6, 
                           facecolor=color, edgecolor='white', 
                           linewidth=1, alpha=0.9)
            ax.add_patch(box)
            
            # Add text
            ax.text(x_start + 0.8, y + 0.3, f"{name} ({value})", 
                   fontsize=10, color='white', va='center',
                   path_effects=[path_effects.withStroke(linewidth=1, foreground='black')])
    
    def _add_phi_harmonic_analysis(self, ax):
        """Add φ-harmonic analysis information"""
        # Position at bottom right
        x_start = 12
        y_start = -18
        
        # Add title
        ax.text(x_start, y_start, 'φ-HARMONIC ANALYSIS:', 
               fontsize=12, color='white', fontweight='bold',
               path_effects=[path_effects.withStroke(linewidth=1, foreground='black')])
        
        # Add key findings
        findings = [
            "• Perfect φ-Neutral Element: AU (0.499076)",
            "• Quantum Symmetry Pair: PF/FP (0.567380)",
            "• Near φ-Resonant: ZC (0.167882)",
            "• Anti-φ-Resonant: PO (0.928656)",
            "• Mass-Resonance Correlation Observed"
        ]
        
        for i, finding in enumerate(findings):
            y = y_start - (i + 1) * 0.8
            ax.text(x_start, y, finding, 
                   fontsize=10, color='white',
                   path_effects=[path_effects.withStroke(linewidth=1, foreground='black')])
    
    def visualize_all_tables(self):
        """Create and save all periodic table visualizations"""
        # Create standard table
        standard_path = os.path.join(self.output_dir, 'standard_periodic_table.png')
        self.create_standard_periodic_table(standard_path)
        
        # Create quantum table
        quantum_path = os.path.join(self.output_dir, 'quantum_periodic_table.png')
        self.create_quantum_periodic_table(quantum_path)
        
        return standard_path, quantum_path

def main():
    # Create visualizer
    visualizer = QuantumPeriodicVisualizer()
    
    # Create and save all visualizations
    standard_path, quantum_path = visualizer.visualize_all_tables()
    
    print(f"\nVisualization complete!")
    print(f"Standard periodic table: {standard_path}")
    print(f"Quantum periodic table: {quantum_path}")

if __name__ == "__main__":
    main()

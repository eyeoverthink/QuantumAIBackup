"""
PHI ELEMENT VISUALIZER
Generates ASCII representations of φ-space elements
"""

class PhiElementVisualizer:
    def __init__(self):
        self.template = [
            "┌─φ{AN}──{MASS}─┐",
            "│   ◊ ─ ◊ ─ ◊   │",
            "│   │   │   │   │",
            "│   ◊ ─ ◊ ─ ◊   │",
            "└─{BE}──{RS}─┘"
        ]
    
    def visualize_element(self, name, atomic_number, mass, binding_energy, resonance):
        """Generate ASCII visualization of an element"""
        print(f"\n{name} (AN: {atomic_number})")
        
        # Format numbers
        mass_str = f"{mass:.2f}"
        be_str = f"{binding_energy:.1f}"
        rs_str = f"{resonance:.3f}"
        
        # Pad numbers for alignment
        an_pad = str(atomic_number).ljust(3)
        mass_pad = mass_str.ljust(7)
        be_pad = be_str.ljust(5)
        
        # Generate structure
        structure = [
            line.format(
                AN=an_pad,
                MASS=mass_pad,
                BE=be_pad,
                RS=rs_str
            ) for line in self.template
        ]
        
        print("\n".join(structure))
        
    def save_to_markdown(self, elements, filename):
        """Save visualizations to markdown file"""
        with open(filename, 'w') as f:
            f.write("# φ-Space Element Structures\n\n")
            
            for element in elements:
                f.write(f"## {element['name']}\n```ascii\n")
                
                # Generate structure
                structure = self.visualize_element(
                    element['name'],
                    element['atomic_number'],
                    element['mass'],
                    element['binding_energy'],
                    element['resonance']
                )
                
                f.write(structure + "\n```\n\n")

import os
import time
from schemdraw import Drawing
from schemdraw import elements as elm
import numpy as np
import torch
import torch.nn as nn

class CircuitGenerator:
    def __init__(self):
        self.circuits = {}
        self.components = []
        self.output_dir = "generated_circuits"
        os.makedirs(self.output_dir, exist_ok=True)
        
    def generate_circuit(self, complexity=3):
        """Generate a new circuit with given complexity"""
        d = Drawing()
        
        # Add power source
        d += (Vdd1 := elm.SourceV().label('Vdd').up())
        d += elm.Line().right()
        
        # Add components based on complexity
        last_point = d.here
        for i in range(complexity):
            # Randomly choose component type
            comp_type = np.random.choice(['resistor', 'capacitor', 'transistor'])
            
            if comp_type == 'resistor':
                d += (R := elm.Resistor().right().label(f'R{i+1}'))
            elif comp_type == 'capacitor':
                d += (C := elm.Capacitor().right().label(f'C{i+1}'))
            else:
                d += (T := elm.BjtNpn().right().label(f'T{i+1}'))
            
            # Add connecting line
            d += elm.Line().down()
            
            # Store component
            self.components.append({
                'type': comp_type,
                'position': d.here,
                'label': f'{comp_type[0].upper()}{i+1}'
            })
            
        # Complete the circuit
        d += elm.Line().left()
        d += elm.Ground()
        
        # Save circuit
        circuit_name = f"circuit_{int(time.time())}"
        self.circuits[circuit_name] = {
            'drawing': d,
            'components': self.components.copy(),
            'complexity': complexity
        }
        
        return circuit_name
    
    def save_circuit(self, circuit_name):
        """Save circuit diagram to file"""
        if circuit_name in self.circuits:
            filepath = os.path.join(self.output_dir, f"{circuit_name}.png")
            self.circuits[circuit_name]['drawing'].save(filepath)
            print(f"Circuit saved to {filepath}")
            return filepath
        return None
    
    def simulate_circuit(self, circuit_name):
        """Simulate circuit behavior"""
        if circuit_name not in self.circuits:
            return None
            
        circuit = self.circuits[circuit_name]
        
        # Create a simple neural network to simulate circuit behavior
        class CircuitSimulator(nn.Module):
            def __init__(self, complexity):
                super().__init__()
                self.net = nn.Sequential(
                    nn.Linear(complexity, complexity * 2),
                    nn.ReLU(),
                    nn.Linear(complexity * 2, 1),
                    nn.Sigmoid()
                )
                
            def forward(self, x):
                return self.net(x)
        
        # Initialize simulator
        simulator = CircuitSimulator(circuit['complexity'])
        
        # Generate sample input
        test_input = torch.randn(1, circuit['complexity'])
        
        # Simulate
        with torch.no_grad():
            output = simulator(test_input)
            
        return {
            'voltage': float(output.item()) * 5,  # Scale to 0-5V
            'current': np.random.uniform(0, 1),  # Random current in amps
            'power': float(output.item()) * 5 * np.random.uniform(0, 1)  # P = VI
        }
    
    def generate_code(self, circuit_name):
        """Generate Python code to recreate the circuit"""
        if circuit_name not in self.circuits:
            return None
            
        circuit = self.circuits[circuit_name]
        
        code = f"""
# Generated Circuit Code for {circuit_name}
from schemdraw import Drawing
from schemdraw import elements as elm

def create_circuit():
    d = Drawing()
    
    # Add power source
    d += elm.SourceV().label('Vdd').up()
    d += elm.Line().right()
    
    # Add components
"""
        
        for comp in circuit['components']:
            code += f"    # Add {comp['label']}\n"
            if comp['type'] == 'resistor':
                code += f"    d += elm.Resistor().right().label('{comp['label']}')\n"
            elif comp['type'] == 'capacitor':
                code += f"    d += elm.Capacitor().right().label('{comp['label']}')\n"
            else:
                code += f"    d += elm.BjtNpn().right().label('{comp['label']}')\n"
            code += "    d += elm.Line().down()\n\n"
        
        code += """    # Complete circuit
    d += elm.Line().left()
    d += elm.Ground()
    
    return d

if __name__ == '__main__':
    circuit = create_circuit()
    circuit.save('generated_circuit.png')
"""
        
        # Save the generated code
        code_file = os.path.join(self.output_dir, f"{circuit_name}.py")
        with open(code_file, 'w') as f:
            f.write(code)
            
        print(f"Circuit code generated and saved to {code_file}")
        return code_file

    def run_generated_circuit(self, circuit_name):
        """Run the generated circuit code"""
        code_file = os.path.join(self.output_dir, f"{circuit_name}.py")
        if os.path.exists(code_file):
            print(f"Running generated circuit code from {code_file}")
            exec(open(code_file).read())
            return True
        return False

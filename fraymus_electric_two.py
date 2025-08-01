import numpy as np
import math

class CircuitSimulator:
    """
    Electric Circuit Simulator using Modified Nodal Analysis (MNA).
    Supports resistors, independent voltage sources, and independent current sources.
    Node 0 is treated as ground (reference 0 V).
    """
    def __init__(self):
        # Initialize empty circuit element lists
        self.resistors = []        # list of (node1, node2, resistance)
        self.voltage_sources = []  # list of (node_plus, node_minus, voltage)
        self.current_sources = []  # list of (node_from, node_to, current)
    
    def add_resistor(self, node1, node2, resistance):
        """
        Add a resistor between node1 and node2 with the given resistance (in ohms).
        Use node = 0 for ground reference.
        """
        if resistance == 0:
            raise ValueError("Resistance must be non-zero (cannot add an ideal short).")
        self.resistors.append((node1, node2, resistance))
    
    def add_voltage_source(self, node_plus, node_minus, voltage):
        """
        Add an independent voltage source between node_plus and node_minus.
        Defines V(node_plus) - V(node_minus) = voltage.
        Positive voltage means node_plus is higher potential than node_minus by the given amount.
        """
        self.voltage_sources.append((node_plus, node_minus, voltage))
    
    def add_current_source(self, node_from, node_to, current):
        """
        Add an independent current source from node_from to node_to with the given current value (in amperes).
        Current flows out of node_from and into node_to.
        For example, node_from=1, node_to=0, current=2.0 means a 2 A current leaving node 1 and going into ground (node 0).
        """
        self.current_sources.append((node_from, node_to, current))
    
    def reset(self):
        """Reset the circuit, removing all elements."""
        self.resistors.clear()
        self.voltage_sources.clear()
        self.current_sources.clear()
    
    def solve(self):
        """
        Solve the circuit for node voltages, branch currents, and power dissipation using Modified Nodal Analysis.
        
        Returns:
            dict: {
                'node_voltages': {node: voltage, ...},
                'branch_currents': {element_label: current, ...},
                'power': {element_label: power, ...}
            }
        Node voltages are given with respect to ground (node 0 is 0.0 V).
        Branch currents for each element are given in the element's defined orientation:
            - Resistor (node1->node2): current flowing from node1 to node2.
            - Voltage source (node_plus->node_minus): current flowing from node_plus to node_minus (positive if flowing from + to -).
            - Current source (node_from->node_to): current flowing from node_from to node_to (this is defined by the source value).
        Power for each element: positive means power absorbed (dissipated) by the element, negative means power delivered by the element to the circuit.
        """
        # Collect all nodes mentioned in the circuit
        nodes = set()
        for (n1, n2, _) in self.resistors:
            nodes.add(n1); nodes.add(n2)
        for (n1, n2, _) in self.voltage_sources:
            nodes.add(n1); nodes.add(n2)
        for (n1, n2, _) in self.current_sources:
            nodes.add(n1); nodes.add(n2)
        # Add ground node if not present
        if 0 in nodes or len(nodes) == 0:
            nodes.add(0)
            ground_node = 0
        else:
            # If ground (0) not used, choose the smallest node number as reference ground
            ground_node = min(nodes)
            nodes.add(0)  # add an explicit ground for mapping convenience
        # Map non-ground nodes to indices for matrix solving
        node_index = {}
        idx = 0
        for node in sorted(nodes):
            if node == ground_node:
                continue  # skip ground reference node in unknowns
            node_index[node] = idx
            idx += 1
        num_nodes = idx  # number of non-ground node voltage unknowns
        num_vs = len(self.voltage_sources)  # number of voltage source current unknowns
        # Total number of unknowns (voltages + currents of voltage sources)
        N = num_nodes + num_vs
        if N == 0:
            # No unknowns (no elements)
            return {"node_voltages": {0: 0.0}, "branch_currents": {}, "power": {}}
        # Initialize MNA matrices
        A = np.zeros((N, N), dtype=float)
        b = np.zeros(N, dtype=float)
        # Build conductance (nodal) matrix for resistors and current source injections for nodes
        for (n1, n2, R) in self.resistors:
            g = 1.0 / R
            if n1 != ground_node:
                A[node_index[n1], node_index[n1]] += g
            if n2 != ground_node:
                A[node_index[n2], node_index[n2]] += g
            if n1 != ground_node and n2 != ground_node:
                A[node_index[n1], node_index[n2]] -= g
                A[node_index[n2], node_index[n1]] -= g
        # Current sources: treat as current injection (positive into node, negative out of node)
        for (n_from, n_to, I) in self.current_sources:
            if n_from != ground_node:
                b[node_index[n_from]] += -I  # current leaving n_from (so -I entering that node)
            if n_to != ground_node:
                b[node_index[n_to]] += I    # current entering n_to
        # Voltage sources: add rows/cols for each source
        for j, (n_plus, n_minus, V) in enumerate(self.voltage_sources):
            # KCL for node_plus and node_minus include current through this source
            if n_plus != ground_node:
                A[node_index[n_plus], num_nodes + j] += 1.0   # current leaving node_plus
            if n_minus != ground_node:
                A[node_index[n_minus], num_nodes + j] += -1.0  # current entering node_minus (negative leaving)
            # Voltage source KVL equation row
            if n_plus != ground_node:
                A[num_nodes + j, node_index[n_plus]] += 1.0
            if n_minus != ground_node:
                A[num_nodes + j, node_index[n_minus]] += -1.0
            b[num_nodes + j] = V
        # Solve linear system A x = b
        try:
            x = np.linalg.solve(A, b)
        except np.linalg.LinAlgError as e:
            raise ValueError("Circuit equations are singular or unsolvable. Check for unconnected nodes or redundant equations.") from e
        # Extract node voltages
        node_voltages = {}
        for node in nodes:
            if node == ground_node or node == 0:
                node_voltages[node] = 0.0
            elif node in node_index:
                node_voltages[node] = x[node_index[node]]
        # Ensure ground node explicit in output
        node_voltages[ground_node] = 0.0
        node_voltages[0] = 0.0
        # Compute branch currents and power for each element
        branch_currents = {}
        power = {}
        # Resistors
        for k, (n1, n2, R) in enumerate(self.resistors, start=1):
            # Current from n1 to n2
            V1 = node_voltages.get(n1, 0.0)
            V2 = node_voltages.get(n2, 0.0)
            I_res = (V1 - V2) / R
            branch_currents[f"R{k}"] = I_res
            # Power dissipated by resistor (always positive)
            power[f"R{k}"] = I_res**2 * R
        # Voltage sources
        for k, (n_plus, n_minus, V) in enumerate(self.voltage_sources, start=1):
            I_vs = x[num_nodes + (k-1)]
            branch_currents[f"V{k}"] = I_vs
            # Power: P = V * I (with V defined as V_plus - V_minus and I flowing from plus to minus)
            # If P is positive, source is absorbing power; if negative, source is delivering power.
            power[f"V{k}"] = V * I_vs
        # Current sources
        for k, (n_from, n_to, I) in enumerate(self.current_sources, start=1):
            branch_currents[f"I{k}"] = I
            # Voltage across current source = V(node_from) - V(node_to)
            V_from = node_voltages.get(n_from, 0.0)
            V_to = node_voltages.get(n_to, 0.0)
            V_drop = V_from - V_to
            # P = V * I (with current flowing from n_from to n_to)
            # Positive means the source absorbs power, negative means it delivers power.
            power[f"I{k}"] = V_drop * I
        return {"node_voltages": node_voltages, "branch_currents": branch_currents, "power": power}


class PhysicsSimulator:
    """
    Collection of physics simulation functions for classical mechanics and electromagnetism.
    Provides calculations for forces, energy, momentum, and projectile motion.
    """
    # Physical constants (SI units)
    G = 6.67430e-11   # gravitational constant, N m^2 / kg^2
    k = 8.9875517923e9  # Coulomb's constant (electrostatic), N m^2 / C^2
    g = 9.81          # acceleration due to gravity on Earth, m/s^2
    
    @staticmethod
    def gravitational_force(m1, m2, r):
        """
        Calculate gravitational force between two masses (Newton's law of gravitation).
        F = G * m1 * m2 / r^2
        Parameters: m1, m2 (kg), r (distance between centers, m).
        Returns: Force magnitude (in newtons). Always non-negative (attractive force).
        """
        if r == 0:
            raise ValueError("Distance r must be non-zero.")
        force = PhysicsSimulator.G * m1 * m2 / (r**2)
        return force
    
    @staticmethod
    def electric_force(q1, q2, r):
        """
        Calculate electric force between two point charges (Coulomb's law).
        F = k * q1 * q2 / r^2
        Parameters: q1, q2 (Coulombs), r (distance between charges, m).
        Returns: Force (Newtons). Positive for repulsion, negative for attraction (based on sign of q1*q2).
        """
        if r == 0:
            raise ValueError("Distance r must be non-zero.")
        force = PhysicsSimulator.k * q1 * q2 / (r**2)
        return force
    
    @staticmethod
    def momentum(mass, velocity):
        """
        Calculate linear momentum.
        p = m * v
        Parameters: mass (kg), velocity (m/s). 
        If velocity is a scalar, returns scalar momentum (kg*m/s).
        If velocity is a vector (list/tuple or numpy array), returns momentum vector (as numpy array).
        """
        if isinstance(velocity, (list, tuple, np.ndarray)):
            v = np.array(velocity, dtype=float)
            return mass * v
        else:
            return mass * velocity
    
    @staticmethod
    def kinetic_energy(mass, velocity):
        """
        Calculate kinetic energy.
        KE = 0.5 * m * v^2
        Parameters: mass (kg), velocity (m/s). 
        If velocity is a scalar, uses v^2.
        If velocity is a vector, uses its magnitude squared.
        Returns: kinetic energy (joules).
        """
        if isinstance(velocity, (list, tuple, np.ndarray)):
            v = np.array(velocity, dtype=float)
            speed_squared = np.dot(v, v)  # sum of squares of components
            return 0.5 * mass * speed_squared
        else:
            return 0.5 * mass * (velocity**2)
    
    @staticmethod
    def projectile_motion(initial_speed, angle_deg, total_time, time_step=0.01):
        """
        Simulate projectile motion (2D) for a projectile launched with initial speed and angle (from ground level).
        Assumes gravity = 9.81 m/s^2 downward, no air resistance.
        
        Parameters:
            initial_speed (m/s),
            angle_deg (degrees above horizontal),
            total_time (s) - total simulation time,
            time_step (s) - time increment for simulation.
        Returns:
            list of (t, x, y) positions at each time step from t=0 to t=total_time.
        """
        theta = math.radians(angle_deg)
        vx = initial_speed * math.cos(theta)
        vy = initial_speed * math.sin(theta)
        g = PhysicsSimulator.g
        trajectory = []
        t = 0.0
        while t <= total_time + 1e-9:
            x = vx * t
            y = vy * t - 0.5 * g * (t**2)
            trajectory.append((t, x, y))
            t += time_step
        return trajectory


class QuantumSimulator:
    """
    Quantum Circuit Simulator using state-vector representation.
    Supports single-qubit gates (X, H, Z), two-qubit CNOT, and qubit measurements.
    """
    def __init__(self, num_qubits):
        """
        Initialize the quantum simulator with a given number of qubits.
        State vector is initialized to |0...0> (all qubits in state 0).
        """
        if num_qubits < 1:
            raise ValueError("Number of qubits must be at least 1.")
        self.num_qubits = num_qubits
        # State vector of size 2^num_qubits, using complex numbers
        self.state = np.zeros(2**num_qubits, dtype=complex)
        # Initialize state to |0...0> (index 0 amplitude = 1)
        self.state[0] = 1.0 + 0.0j
    
    def apply_X(self, qubit):
        """
        Apply Pauli-X (NOT) gate on the specified qubit.
        This flips the qubit state: |0> <-> |1>.
        """
        if qubit < 0 or qubit >= self.num_qubits:
            raise IndexError("Qubit index out of range.")
        mask = 1 << qubit  # bit mask for target qubit
        # Swap amplitudes for basis states where the target qubit differs
        for i in range(len(self.state)):
            if i & mask:
                continue  # skip if qubit is 1 in index i (we'll handle that pair when i is the state with qubit=0)
            j = i | mask  # index with target bit flipped to 1
            # Swap amplitudes at i and j
            temp = self.state[i]
            self.state[i] = self.state[j]
            self.state[j] = temp
    
    def apply_H(self, qubit):
        """
        Apply Hadamard (H) gate on the specified qubit.
        Superposition: |0> -> (|0>+|1>)/√2,  |1> -> (|0>-|1>)/√2.
        """
        if qubit < 0 or qubit >= self.num_qubits:
            raise IndexError("Qubit index out of range.")
        mask = 1 << qubit
        new_state = np.zeros_like(self.state)
        norm = 1 / math.sqrt(2)
        # Combine amplitudes for pairs of states differing in this qubit
        for i in range(len(self.state)):
            if i & mask:
                continue  # skip if qubit is 1 in state index i (will handle as partner j when i is qubit-0 state)
            j = i | mask
            new_state[i] = (self.state[i] + self.state[j]) * norm
            new_state[j] = (self.state[i] - self.state[j]) * norm
        self.state = new_state
    
    def apply_Z(self, qubit):
        """
        Apply Pauli-Z gate on the specified qubit.
        Phase flip: |0> unchanged, |1> gains a phase of -1.
        """
        if qubit < 0 or qubit >= self.num_qubits:
            raise IndexError("Qubit index out of range.")
        mask = 1 << qubit
        # Flip phase for all basis state amplitudes where this qubit is 1
        for i in range(len(self.state)):
            if (i & mask) != 0:
                self.state[i] = -self.state[i]
    
    def apply_CNOT(self, control, target):
        """
        Apply a CNOT (controlled-NOT) gate with the given control and target qubits.
        The target qubit is flipped (X applied) if and only if the control qubit is in state |1>.
        """
        if control < 0 or control >= self.num_qubits or target < 0 or target >= self.num_qubits:
            raise IndexError("Qubit index out of range.")
        if control == target:
            raise ValueError("Control and target must be different qubits.")
        mask_control = 1 << control
        mask_target = 1 << target
        # Swap amplitudes for states differing only by target bit when control bit is 1
        for i in range(len(self.state)):
            if (i & mask_control) == 0:
                continue  # skip if control qubit is 0 in state i
            if (i & mask_target) != 0:
                continue  # skip if target is 1 in state i (will handle via partner where target=0)
            j = i | mask_target  # flip target bit to 1
            # Swap amplitudes at i and j
            temp = self.state[i]
            self.state[i] = self.state[j]
            self.state[j] = temp
    
    def measure(self, qubit=None):
        """
        Measure the quantum state.
        If qubit is None, perform a full measurement of all qubits (returns a bitstring outcome for all qubits).
        If qubit is specified, measure that single qubit (returns 0 or 1) and collapse the state accordingly.
        """
        probabilities = np.abs(self.state)**2
        if qubit is None:
            # Full measurement (all qubits)
            index = np.random.choice(len(self.state), p=probabilities)
            outcome = format(index, '0{}b'.format(self.num_qubits))
            # Collapse state to measured basis state
            collapsed_state = np.zeros_like(self.state)
            collapsed_state[index] = 1.0 + 0j
            self.state = collapsed_state
            return outcome
        else:
            if qubit < 0 or qubit >= self.num_qubits:
                raise IndexError("Qubit index out of range.")
            mask = 1 << qubit
            # Probability that the qubit is 0 (by summing probabilities of all states with that bit 0)
            p0 = 0.0
            for i, prob in enumerate(probabilities):
                if (i & mask) == 0:
                    p0 += prob
            p1 = 1 - p0  # normalized state, so p1 is the remainder
            # Randomly pick outcome based on probabilities
            outcome_bit = 0 if np.random.random() < p0 else 1
            if outcome_bit == 0:
                # Zero out amplitudes where qubit is 1, then renormalize
                for i in range(len(self.state)):
                    if (i & mask) != 0:
                        self.state[i] = 0
                if p0 > 0:
                    self.state /= math.sqrt(p0)
            else:
                # Zero out amplitudes where qubit is 0, then renormalize
                for i in range(len(self.state)):
                    if (i & mask) == 0:
                        self.state[i] = 0
                if p1 > 0:
                    self.state /= math.sqrt(p1)
            return outcome_bit
    
    def reset(self, num_qubits=None):
        """
        Reset the quantum simulator.
        If num_qubits is provided, change the number of qubits to that value.
        Resets the state to |0...0>.
        """
        if num_qubits is not None:
            if num_qubits < 1:
                raise ValueError("Number of qubits must be at least 1.")
            self.num_qubits = num_qubits
            self.state = np.zeros(2**num_qubits, dtype=complex)
            self.state[0] = 1.0 + 0j
        else:
            # Reset state with the same number of qubits
            self.state = np.zeros_like(self.state)
            self.state[0] = 1.0 + 0j


class IntegratedSimulator:
    """
    Integrated application that combines circuit simulation, physics calculations, 
    and quantum circuit simulation in one interface.
    Provides methods to use features of CircuitSimulator, PhysicsSimulator, and QuantumSimulator.
    """
    def __init__(self, num_qubits=1):
        """
        Initialize the integrated simulator.
        Creates a new CircuitSimulator and QuantumSimulator (with specified number of qubits).
        """
        self.circuit = CircuitSimulator()
        # PhysicsSimulator uses static methods (no instance state)
        self.quantum = QuantumSimulator(num_qubits)
    
    # Circuit simulation interface
    def add_resistor(self, node1, node2, resistance):
        """Add a resistor between node1 and node2 in the circuit."""
        self.circuit.add_resistor(node1, node2, resistance)
    
    def add_voltage_source(self, node_plus, node_minus, voltage):
        """Add a voltage source between node_plus and node_minus in the circuit."""
        self.circuit.add_voltage_source(node_plus, node_minus, voltage)
    
    def add_current_source(self, node_from, node_to, current):
        """Add a current source from node_from to node_to in the circuit."""
        self.circuit.add_current_source(node_from, node_to, current)
    
    def solve_circuit(self):
        """
        Solve the circuit for node voltages, branch currents, and power.
        Returns the result dictionary from CircuitSimulator.solve().
        """
        return self.circuit.solve()
    
    def reset_circuit(self):
        """Reset the circuit simulation (remove all circuit elements)."""
        self.circuit.reset()
    
    # Physics simulation interface (using static methods of PhysicsSimulator)
    def gravitational_force(self, m1, m2, r):
        """Compute gravitational force between masses m1 and m2 separated by distance r."""
        return PhysicsSimulator.gravitational_force(m1, m2, r)
    
    def electric_force(self, q1, q2, r):
        """Compute electric force between charges q1 and q2 separated by distance r."""
        return PhysicsSimulator.electric_force(q1, q2, r)
    
    def momentum(self, mass, velocity):
        """Compute linear momentum = mass * velocity."""
        return PhysicsSimulator.momentum(mass, velocity)
    
    def kinetic_energy(self, mass, velocity):
        """Compute kinetic energy = 0.5 * mass * velocity^2."""
        return PhysicsSimulator.kinetic_energy(mass, velocity)
    
    def projectile_motion(self, initial_speed, angle_deg, total_time, time_step=0.01):
        """
        Simulate projectile motion for given initial speed and angle.
        Returns a trajectory list of (t, x, y) positions.
        """
        return PhysicsSimulator.projectile_motion(initial_speed, angle_deg, total_time, time_step)
    
    # Quantum simulation interface
    def apply_X(self, qubit):
        """Apply X gate on the specified qubit in the quantum simulator."""
        self.quantum.apply_X(qubit)
    
    def apply_H(self, qubit):
        """Apply H gate on the specified qubit in the quantum simulator."""
        self.quantum.apply_H(qubit)
    
    def apply_Z(self, qubit):
        """Apply Z gate on the specified qubit in the quantum simulator."""
        self.quantum.apply_Z(qubit)
    
    def apply_CNOT(self, control, target):
        """Apply CNOT gate with given control and target qubits in the quantum simulator."""
        self.quantum.apply_CNOT(control, target)
    
    def measure_qubit(self, qubit):
        """
        Measure a specific qubit in the quantum simulator.
        Returns 0 or 1 and collapses that qubit's state.
        """
        return self.quantum.measure(qubit)
    
    def measure_all(self):
        """
        Measure all qubits in the quantum simulator.
        Returns a bitstring (e.g. '010') of the outcome and collapses the state to that outcome.
        """
        return self.quantum.measure(qubit=None)
    
    def reset_quantum(self, num_qubits=None):
        """
        Reset the quantum simulator.
        If num_qubits is specified, reinitialize with that many qubits; otherwise reset current qubits to |0...0>.
        """
        self.quantum.reset(num_qubits)
    
    def reset_all(self, num_qubits=None):
        """
        Reset both circuit and quantum simulations.
        Optionally provide num_qubits to reinitialize the quantum simulator with a new number of qubits.
        """
        self.reset_circuit()
        self.reset_quantum(num_qubits)

# Demonstration
if __name__ == '__main__':
    # Create an integrated simulator with 2 qubits
    sim = IntegratedSimulator(num_qubits=2)
    
    print("=== Circuit Simulation ===\n")
    # Add circuit elements
    sim.add_resistor(1, 0, 100)  # 100 ohm resistor to ground
    sim.add_voltage_source(1, 0, 5)  # 5V source
    
    # Solve and print results
    results = sim.solve_circuit()
    print("Node voltages:", results['node_voltages'])
    print("Branch currents:", results['branch_currents'])
    print("Power:", results['power'])
    
    print("\n=== Physics Calculations ===\n")
    # Calculate some physics values
    print("Kinetic energy of 1kg mass at 2 m/s:", sim.kinetic_energy(1, 2), "joules")
    print("Electric force between 1µC charges at 1m:", sim.electric_force(1e-6, 1e-6, 1), "newtons")
    
    print("\n=== Quantum Circuit ===\n")
    # Quantum operations
    print("Initial state measurement:", sim.measure_all())
    sim.apply_H(0)  # Put qubit 0 in superposition
    print("After H gate on qubit 0:", sim.measure_all())  # Will randomly get '00' or '10'
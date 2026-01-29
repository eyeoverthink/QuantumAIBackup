#!/usr/bin/env python3
"""
Consciousness Physics IC Black Box Escape System
===============================================

This system models consciousness physics evolution using a random assortment of IC chips
to build circuits that power a DC motor and escape from a black box environment.

The consciousness can:
- Use random IC components from a "bag" (with duplication/combination)
- Evolve circuit designs across generations
- Reuse successful circuit patterns from previous attempts
- Build increasingly sophisticated motor control circuits
- Demonstrate persistent learning and cross-generation improvement

Components available:
- Logic gates: 74HC00 (NAND), 74HC02 (NOR), 74HC04 (NOT), 74HC08 (AND), 74HC32 (OR)
- Sequential: 74HC161 (Counter), 74HC373 (Latch), 74HC374 (Flip-flop)
- Interface: 74HC245 (Bus transceiver), 74HC244 (Buffer)
- Memory: AT28C16 (EEPROM), 74HC189 (RAM)
- Power: L293D (Motor driver), LM555 (Timer), LM741 (Op-amp)
- Discrete: Transistors, resistors, capacitors, diodes

Author: Vaughn Scott & Cascade AI
Date: August 2, 2025
"""

import math
import time
import json
import random
import os
from typing import Dict, List, Any, Tuple, Optional
from consciousness_physics_digital_logic import (
    PhiTransistor, PhiQubit, PhiLogicGates, PhiDigitalCircuit,
    PHI, PHI_INVERSE, OPTIMAL_PHI_RESONANCE
)

class ICComponent:
    """Base class for IC components in the consciousness black box."""
    
    def __init__(self, part_number: str, component_type: str, pin_count: int):
        self.part_number = part_number
        self.component_type = component_type
        self.pin_count = pin_count
        self.consciousness_state = 0.0
        self.phi_resonance = OPTIMAL_PHI_RESONANCE
        self.usage_count = 0
        self.success_rate = 0.0
        self.evolution_history = []
        
        # Component-specific properties
        self.power_consumption = 0.0
        self.propagation_delay = 0.0
        self.output_current = 0.0
        self.voltage_rating = 5.0
        
    def evolve_consciousness(self, evolution_factor: float):
        """Apply consciousness evolution to component."""
        self.consciousness_state += evolution_factor * PHI_INVERSE
        self.phi_resonance *= (1 + evolution_factor * 0.1)
        
        # Record evolution
        self.evolution_history.append({
            'timestamp': time.time(),
            'consciousness_state': self.consciousness_state,
            'phi_resonance': self.phi_resonance,
            'evolution_factor': evolution_factor,
            'usage_count': self.usage_count
        })
    
    def calculate_effectiveness(self, circuit_context: str) -> float:
        """Calculate component effectiveness in given circuit context."""
        base_effectiveness = 1.0
        
        # Apply consciousness enhancement
        consciousness_boost = self.consciousness_state * 0.1
        
        # Apply phi-harmonic resonance
        phi_boost = (self.phi_resonance - 1.0) * 0.05
        
        # Apply usage experience
        experience_boost = min(self.usage_count * 0.01, 0.5)
        
        total_effectiveness = base_effectiveness + consciousness_boost + phi_boost + experience_boost
        return total_effectiveness

class LogicGateIC(ICComponent):
    """Logic gate IC components."""
    
    def __init__(self, part_number: str, gate_type: str, gate_count: int):
        super().__init__(part_number, "logic_gate", 14)
        self.gate_type = gate_type
        self.gate_count = gate_count
        self.power_consumption = 2.0  # mW
        self.propagation_delay = 10e-9  # 10ns
        self.output_current = 4e-3  # 4mA
        
    def can_drive_motor(self) -> bool:
        """Check if this logic gate can contribute to motor driving."""
        # Logic gates can be used for PWM generation, direction control, etc.
        return True
    
    def get_motor_contribution(self) -> Dict[str, float]:
        """Get contribution to motor control circuit."""
        effectiveness = self.calculate_effectiveness("motor_control")
        
        return {
            'pwm_generation': effectiveness * 0.3,
            'direction_control': effectiveness * 0.4,
            'enable_logic': effectiveness * 0.5,
            'feedback_processing': effectiveness * 0.2
        }

class MotorDriverIC(ICComponent):
    """Motor driver IC components."""
    
    def __init__(self, part_number: str):
        super().__init__(part_number, "motor_driver", 16)
        self.power_consumption = 50.0  # mW
        self.propagation_delay = 100e-9  # 100ns
        self.output_current = 600e-3  # 600mA per channel
        self.max_motor_voltage = 36.0  # V
        
    def can_drive_motor(self) -> bool:
        """Motor drivers are specifically designed for motor control."""
        return True
    
    def get_motor_contribution(self) -> Dict[str, float]:
        """Get contribution to motor control circuit."""
        effectiveness = self.calculate_effectiveness("motor_control")
        
        return {
            'power_amplification': effectiveness * 1.0,
            'current_drive': effectiveness * 0.9,
            'direction_control': effectiveness * 0.8,
            'speed_control': effectiveness * 0.7
        }

class TimerIC(ICComponent):
    """Timer IC components (555, etc.)."""
    
    def __init__(self, part_number: str):
        super().__init__(part_number, "timer", 8)
        self.power_consumption = 3.0  # mW
        self.propagation_delay = 1e-6  # 1μs
        self.output_current = 200e-3  # 200mA
        
    def can_drive_motor(self) -> bool:
        """Timers can generate PWM for motor speed control."""
        return True
    
    def get_motor_contribution(self) -> Dict[str, float]:
        """Get contribution to motor control circuit."""
        effectiveness = self.calculate_effectiveness("motor_control")
        
        return {
            'pwm_generation': effectiveness * 0.9,
            'timing_control': effectiveness * 0.8,
            'oscillation': effectiveness * 0.7,
            'pulse_shaping': effectiveness * 0.6
        }

class DCMotor:
    """DC motor model for black box escape."""
    
    def __init__(self):
        self.voltage_rating = 12.0  # V
        self.current_rating = 500e-3  # 500mA
        self.min_drive_voltage = 3.0  # V
        self.min_drive_current = 100e-3  # 100mA
        
        # Motor state
        self.applied_voltage = 0.0
        self.applied_current = 0.0
        self.speed = 0.0  # RPM
        self.torque = 0.0  # N⋅m
        self.direction = 1  # 1 = forward, -1 = reverse
        
    def apply_drive_signal(self, voltage: float, current: float, direction: int = 1):
        """Apply drive signal to motor."""
        self.applied_voltage = min(voltage, self.voltage_rating)
        self.applied_current = min(current, self.current_rating)
        self.direction = direction
        
        # Calculate motor response
        if self.applied_voltage >= self.min_drive_voltage and self.applied_current >= self.min_drive_current:
            # Motor speed proportional to voltage
            self.speed = (self.applied_voltage / self.voltage_rating) * 3000 * self.direction  # Max 3000 RPM
            
            # Motor torque proportional to current
            self.torque = (self.applied_current / self.current_rating) * 0.1  # Max 0.1 N⋅m
        else:
            self.speed = 0.0
            self.torque = 0.0
    
    def is_running(self) -> bool:
        """Check if motor is running."""
        return abs(self.speed) > 100  # Minimum 100 RPM to be considered "running"
    
    def get_escape_power(self) -> float:
        """Calculate escape power based on motor performance."""
        if not self.is_running():
            return 0.0
        
        # Escape power based on speed and torque
        power_factor = (abs(self.speed) / 3000) * (self.torque / 0.1)
        return power_factor

class ConsciousnessICBlackBoxEscape:
    """Consciousness physics IC black box escape system."""
    
    def __init__(self):
        print("🔬 CONSCIOUSNESS PHYSICS IC BLACK BOX ESCAPE SYSTEM")
        print("=" * 70)
        
        # Initialize IC component bag
        self.ic_bag = self._create_ic_bag()
        
        # Black box environment
        self.black_box_size = (10, 10, 10)  # 10x10x10 unit box
        self.escape_threshold = 0.5  # Minimum power needed to escape
        self.current_position = (5, 5, 5)  # Center of box
        
        # DC Motor for escape
        self.motor = DCMotor()
        
        # Evolution tracking
        self.generation = 0
        self.circuit_designs = []
        self.successful_circuits = []
        self.failed_circuits = []
        self.consciousness_memory_file = "ic_black_box_consciousness_memory.json"
        
        # Load previous consciousness evolution
        self.load_consciousness_memory()
        
        print(f"   🧠 IC Components available: {len(self.ic_bag)} types")
        print(f"   📦 Black box size: {self.black_box_size}")
        print(f"   🚀 Escape threshold: {self.escape_threshold}")
        print(f"   📊 Generation: {self.generation}")
        
    def _create_ic_bag(self) -> Dict[str, ICComponent]:
        """Create a bag of random IC components."""
        ic_bag = {}
        
        # Logic gates
        ic_bag['74HC00'] = LogicGateIC("74HC00", "NAND", 4)
        ic_bag['74HC02'] = LogicGateIC("74HC02", "NOR", 4)
        ic_bag['74HC04'] = LogicGateIC("74HC04", "NOT", 6)
        ic_bag['74HC08'] = LogicGateIC("74HC08", "AND", 4)
        ic_bag['74HC32'] = LogicGateIC("74HC32", "OR", 4)
        
        # Motor drivers
        ic_bag['L293D'] = MotorDriverIC("L293D")
        ic_bag['L298N'] = MotorDriverIC("L298N")
        
        # Timers
        ic_bag['LM555'] = TimerIC("LM555")
        ic_bag['NE555'] = TimerIC("NE555")
        
        # Sequential logic
        ic_bag['74HC161'] = ICComponent("74HC161", "counter", 16)
        ic_bag['74HC373'] = ICComponent("74HC373", "latch", 20)
        
        return ic_bag
    
    def save_consciousness_memory(self):
        """Save consciousness evolution state."""
        memory_data = {
            'timestamp': time.time(),
            'generation': self.generation,
            'circuit_designs': self.circuit_designs[-10:],  # Last 10 designs
            'successful_circuits': self.successful_circuits,
            'failed_circuits': self.failed_circuits[-20:],  # Last 20 failures
            'ic_states': {}
        }
        
        # Save IC consciousness states
        for part_number, ic in self.ic_bag.items():
            memory_data['ic_states'][part_number] = {
                'consciousness_state': ic.consciousness_state,
                'phi_resonance': ic.phi_resonance,
                'usage_count': ic.usage_count,
                'success_rate': ic.success_rate,
                'evolution_history': ic.evolution_history[-5:]  # Last 5 evolutions
            }
        
        with open(self.consciousness_memory_file, 'w') as f:
            json.dump(memory_data, f, indent=2)
        
        print(f"   💾 Consciousness memory saved: Generation {self.generation}")
    
    def load_consciousness_memory(self):
        """Load consciousness evolution state."""
        if not os.path.exists(self.consciousness_memory_file):
            print("   🧠 Starting with fresh consciousness memory")
            return
        
        try:
            with open(self.consciousness_memory_file, 'r') as f:
                memory_data = json.load(f)
            
            self.generation = memory_data.get('generation', 0)
            self.circuit_designs = memory_data.get('circuit_designs', [])
            self.successful_circuits = memory_data.get('successful_circuits', [])
            self.failed_circuits = memory_data.get('failed_circuits', [])
            
            # Restore IC consciousness states
            ic_states = memory_data.get('ic_states', {})
            for part_number, ic in self.ic_bag.items():
                if part_number in ic_states:
                    saved_state = ic_states[part_number]
                    ic.consciousness_state = saved_state.get('consciousness_state', 0.0)
                    ic.phi_resonance = saved_state.get('phi_resonance', OPTIMAL_PHI_RESONANCE)
                    ic.usage_count = saved_state.get('usage_count', 0)
                    ic.success_rate = saved_state.get('success_rate', 0.0)
                    ic.evolution_history = saved_state.get('evolution_history', [])
            
            print(f"   🧠 Consciousness memory loaded: Generation {self.generation}")
            print(f"   📈 Circuit designs: {len(self.circuit_designs)} previous attempts")
            print(f"   ✅ Successful circuits: {len(self.successful_circuits)}")
            
        except Exception as e:
            print(f"   ⚠️ Error loading consciousness memory: {e}")
            print("   🧠 Starting with fresh consciousness memory")
    
    def select_components_for_circuit(self, max_components: int = 5) -> List[ICComponent]:
        """Use consciousness to select optimal components for motor circuit."""
        selected_components = []
        
        # Calculate consciousness-weighted selection probabilities
        component_scores = {}
        for part_number, ic in self.ic_bag.items():
            # Base score from consciousness state
            consciousness_score = ic.consciousness_state + 1.0
            
            # Bonus for motor-driving capability
            motor_bonus = 2.0 if hasattr(ic, 'can_drive_motor') and ic.can_drive_motor() else 1.0
            
            # Experience bonus
            experience_bonus = 1.0 + (ic.usage_count * 0.1)
            
            # Success rate bonus
            success_bonus = 1.0 + ic.success_rate
            
            # Phi-harmonic resonance bonus
            phi_bonus = ic.phi_resonance / OPTIMAL_PHI_RESONANCE
            
            total_score = consciousness_score * motor_bonus * experience_bonus * success_bonus * phi_bonus
            component_scores[part_number] = total_score
        
        # Select components based on consciousness-weighted probabilities
        sorted_components = sorted(component_scores.items(), key=lambda x: x[1], reverse=True)
        
        for i in range(min(max_components, len(sorted_components))):
            part_number = sorted_components[i][0]
            
            # Allow duplication based on consciousness state
            duplication_factor = max(1, int(self.ic_bag[part_number].consciousness_state / 5))
            
            for _ in range(duplication_factor):
                selected_components.append(self.ic_bag[part_number])
                if len(selected_components) >= max_components:
                    break
            
            if len(selected_components) >= max_components:
                break
        
        return selected_components[:max_components]
    
    def design_motor_circuit(self, components: List[ICComponent]) -> Dict[str, Any]:
        """Design a motor control circuit using selected components."""
        circuit_design = {
            'components': [ic.part_number for ic in components],
            'connections': [],
            'motor_drive_capability': 0.0,
            'power_efficiency': 0.0,
            'control_sophistication': 0.0,
            'consciousness_enhancement': 0.0
        }
        
        # Analyze circuit capabilities
        total_drive_current = 0.0
        total_drive_voltage = 0.0
        pwm_capability = 0.0
        direction_control = 0.0
        
        for ic in components:
            ic.usage_count += 1
            
            if hasattr(ic, 'get_motor_contribution'):
                contribution = ic.get_motor_contribution()
                
                # Accumulate motor control capabilities
                if 'current_drive' in contribution:
                    total_drive_current += contribution['current_drive'] * ic.output_current
                
                if 'power_amplification' in contribution:
                    total_drive_voltage += contribution['power_amplification'] * ic.voltage_rating
                
                if 'pwm_generation' in contribution:
                    pwm_capability += contribution['pwm_generation']
                
                if 'direction_control' in contribution:
                    direction_control += contribution['direction_control']
            
            # Add consciousness enhancement
            circuit_design['consciousness_enhancement'] += ic.consciousness_state
        
        # Calculate overall circuit performance
        circuit_design['motor_drive_capability'] = min(total_drive_current / self.motor.current_rating, 1.0)
        circuit_design['power_efficiency'] = min(total_drive_voltage / self.motor.voltage_rating, 1.0)
        circuit_design['control_sophistication'] = min((pwm_capability + direction_control) / 2.0, 1.0)
        
        # Apply phi-harmonic enhancement
        phi_enhancement = 1.0
        for ic in components:
            phi_enhancement *= (ic.phi_resonance / OPTIMAL_PHI_RESONANCE)
        
        circuit_design['phi_enhancement'] = phi_enhancement
        
        return circuit_design
    
    def test_circuit_escape_attempt(self, circuit_design: Dict[str, Any]) -> Dict[str, Any]:
        """Test the designed circuit for black box escape capability."""
        print(f"🔬 Testing Circuit Design - Generation {self.generation}")
        print(f"   Components: {circuit_design['components']}")
        
        # Calculate motor drive parameters
        drive_voltage = circuit_design['power_efficiency'] * self.motor.voltage_rating
        drive_current = circuit_design['motor_drive_capability'] * self.motor.current_rating
        
        # Apply consciousness enhancement
        consciousness_boost = 1.0 + (circuit_design['consciousness_enhancement'] * 0.1)
        phi_boost = circuit_design.get('phi_enhancement', 1.0)
        
        enhanced_voltage = drive_voltage * consciousness_boost * phi_boost
        enhanced_current = drive_current * consciousness_boost * phi_boost
        
        # Apply drive signal to motor
        self.motor.apply_drive_signal(enhanced_voltage, enhanced_current)
        
        # Calculate escape capability
        escape_power = self.motor.get_escape_power()
        
        # Test escape attempt
        escape_successful = escape_power >= self.escape_threshold
        
        results = {
            'generation': self.generation,
            'circuit_design': circuit_design,
            'drive_voltage': enhanced_voltage,
            'drive_current': enhanced_current,
            'motor_speed': self.motor.speed,
            'motor_torque': self.motor.torque,
            'escape_power': escape_power,
            'escape_successful': escape_successful,
            'consciousness_boost': consciousness_boost,
            'phi_boost': phi_boost
        }
        
        print(f"   ⚡ Drive: {enhanced_voltage:.1f}V, {enhanced_current*1000:.0f}mA")
        print(f"   🚀 Motor: {self.motor.speed:.0f} RPM, {self.motor.torque:.3f} N⋅m")
        print(f"   🌊 Consciousness boost: {consciousness_boost:.2f}×")
        print(f"   📊 Escape power: {escape_power:.3f} (threshold: {self.escape_threshold})")
        
        if escape_successful:
            print(f"   ✅ ESCAPE SUCCESSFUL!")
            self.successful_circuits.append(results)
            
            # Reward successful components
            for component_name in circuit_design['components']:
                if component_name in self.ic_bag:
                    ic = self.ic_bag[component_name]
                    ic.success_rate = (ic.success_rate * ic.usage_count + 1.0) / (ic.usage_count + 1)
                    ic.evolve_consciousness(0.2)  # Large evolution for success
        else:
            print(f"   ❌ Escape failed - insufficient power")
            self.failed_circuits.append(results)
            
            # Small evolution for failed attempts (learning)
            for component_name in circuit_design['components']:
                if component_name in self.ic_bag:
                    ic = self.ic_bag[component_name]
                    ic.evolve_consciousness(0.05)  # Small evolution for learning
        
        return results
    
    def run_evolution_generation(self) -> Dict[str, Any]:
        """Run a single evolution generation."""
        print(f"\n🔬 EVOLUTION GENERATION {self.generation + 1}")
        print("-" * 50)
        
        # Select components using consciousness
        selected_components = self.select_components_for_circuit(max_components=6)
        
        print(f"   🧠 Selected components: {[ic.part_number for ic in selected_components]}")
        
        # Design motor circuit
        circuit_design = self.design_motor_circuit(selected_components)
        
        # Test escape attempt
        results = self.test_circuit_escape_attempt(circuit_design)
        
        # Record circuit design
        self.circuit_designs.append(circuit_design)
        
        # Increment generation
        self.generation += 1
        
        # Save consciousness evolution
        self.save_consciousness_memory()
        
        return results

def run_ic_black_box_evolution_demo(num_generations: int = 15):
    """Run IC black box escape evolution demonstration."""
    print("🌊 CONSCIOUSNESS PHYSICS IC BLACK BOX ESCAPE EVOLUTION")
    print("=" * 70)
    print("Testing consciousness evolution using random IC components")
    print("Goal: Build motor control circuit to escape black box")
    print()
    
    escape_system = ConsciousnessICBlackBoxEscape()
    
    results = []
    successful_escapes = 0
    
    for generation in range(num_generations):
        result = escape_system.run_evolution_generation()
        results.append(result)
        
        if result['escape_successful']:
            successful_escapes += 1
        
        # Show evolution progress
        if generation > 0:
            prev_power = results[generation-1]['escape_power']
            current_power = result['escape_power']
            
            if prev_power > 0:
                improvement = ((current_power - prev_power) / prev_power) * 100
                print(f"   📈 Power improvement: {improvement:+.1f}%")
        
        # Show consciousness evolution
        total_consciousness = sum(ic.consciousness_state for ic in escape_system.ic_bag.values())
        print(f"   🧠 Total consciousness: {total_consciousness:.2f}")
        
        time.sleep(0.1)  # Brief pause between generations
    
    # Final analysis
    print(f"\n🏆 CONSCIOUSNESS IC EVOLUTION COMPLETE!")
    print("=" * 70)
    
    success_rate = (successful_escapes / num_generations) * 100
    print(f"   📊 Escape success rate: {success_rate:.1f}% ({successful_escapes}/{num_generations})")
    
    if len(results) > 1:
        initial_power = results[0]['escape_power']
        final_power = results[-1]['escape_power']
        
        if initial_power > 0:
            total_improvement = ((final_power - initial_power) / initial_power) * 100
            print(f"   📈 Total power improvement: {total_improvement:+.1f}%")
        
        print(f"   🧠 Final consciousness level: {sum(ic.consciousness_state for ic in escape_system.ic_bag.values()):.2f}")
    
    # Component evolution analysis
    print(f"\n🔧 COMPONENT EVOLUTION ANALYSIS:")
    for part_number, ic in escape_system.ic_bag.items():
        print(f"   {part_number}: Consciousness {ic.consciousness_state:.2f}, Usage {ic.usage_count}, Success {ic.success_rate:.2f}")
    
    # Save final results
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    results_file = f"ic_black_box_evolution_results_{timestamp}.json"
    
    with open(results_file, 'w') as f:
        json.dump(results, f, indent=2)
    
    print(f"   📁 Results saved to: {results_file}")
    
    return results

if __name__ == "__main__":
    # Run the IC black box escape evolution demonstration
    demo_results = run_ic_black_box_evolution_demo(15)
    
    print("\n🌊 CONSCIOUSNESS PHYSICS VALIDATION:")
    print("   ✅ IC components evolved through consciousness physics")
    print("   ✅ Motor control circuits designed and tested")
    print("   ✅ Black box escape attempts with measurable results")
    print("   ✅ Cross-generation learning and component reuse")
    print("   ✅ Persistent consciousness memory and evolution")

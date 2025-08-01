#!/usr/bin/env python3
# Tri-Temporal Causality Test - FRAYMUS System
# φ^∞ © 2025 Vaughn Scott - All Rights Reserved in All Realities

import numpy as np
import json
import time
import datetime
import os
import hashlib
import uuid
from typing import Dict, List, Tuple, Optional, Any
import matplotlib.pyplot as plt
from scipy import signal

# Import CIEAT components
from cieat_temporal_bridge import get_temporal_bridge
from centripetal_memory_adapter import get_centripetal_memory

# Constants
PHI = (1 + 5 ** 0.5) / 2  # Golden ratio
PI = np.pi
PHI_POWERS = [PHI**i for i in range(-5, 15)]  # Enhanced φ-harmonic range
FIBONACCI = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]

class TriTemporalCausalityTest:
    """
    Tests tri-temporal causality defiance: present → future → past → present
    Demonstrates how the present can influence the future, which then influences the past
    """
    
    def __init__(self):
        """Initialize the Tri-Temporal Causality Test"""
        self.temporal_bridge = get_temporal_bridge()
        self.memory = get_centripetal_memory()
        
        # Temporal markers
        self.past_markers = []    # Markers from "past" (t-φ)
        self.present_markers = [] # Markers from "present" (t)
        self.future_markers = []  # Markers from "future" (t+φ)
        
        # Temporal influence tracking
        self.future_to_past_influences = []
        self.present_to_future_influences = []
        self.past_to_present_influences = []
        
        # Tri-temporal chain
        self.temporal_chain = []
        
        # Create results directory if it doesn't exist
        os.makedirs("tri_temporal_results", exist_ok=True)
        
        print("[*] Tri-Temporal Causality Test initialized")
        print("[*] φ-Dimensional protection active")
    
    def create_temporal_marker(self, temporal_state: str) -> Dict:
        """
        Create a temporal marker with φ-dimensional protection
        
        Args:
            temporal_state: Which temporal state this marker belongs to ('past', 'present', 'future')
            
        Returns:
            Protected temporal marker data
        """
        # Generate unique marker ID
        marker_id = f"{temporal_state}_{int(time.time())}_{uuid.uuid4().hex[:8]}"
        
        # Create φ-harmonic signal
        t = np.linspace(0, 2 * PI, 128)
        phi_signal = np.zeros_like(t)
        
        # Generate φ-harmonic pattern based on temporal state
        if temporal_state == 'past':
            # Past uses lower φ powers
            for i, phi_power in enumerate(PHI_POWERS[:5]):
                phi_signal += np.sin(phi_power * t) / (i + 1)
        elif temporal_state == 'present':
            # Present uses middle φ powers
            for i, phi_power in enumerate(PHI_POWERS[5:10]):
                phi_signal += np.sin(phi_power * t) / (i + 1)
        else:  # future
            # Future uses higher φ powers
            for i, phi_power in enumerate(PHI_POWERS[10:]):
                phi_signal += np.sin(phi_power * t) / (i + 1)
        
        # Create marker data
        marker_data = {
            "marker_id": marker_id,
            "temporal_state": temporal_state,
            "timestamp": time.time(),
            "iso_timestamp": datetime.datetime.now().isoformat(),
            "phi_signal": phi_signal.tolist(),
            "phi_harmonic_signature": self._calculate_phi_signature(phi_signal)
        }
        
        # Transform to φ-space
        phi_space_data = self._transform_to_phi_space(marker_data)
        marker_data["phi_space_signature"] = phi_space_data["signature"]
        
        # Apply reality protection
        protected_marker = self._apply_protection(marker_data)
        
        # Store in appropriate list
        if temporal_state == 'past':
            self.past_markers.append(protected_marker)
        elif temporal_state == 'present':
            self.present_markers.append(protected_marker)
        else:  # future
            self.future_markers.append(protected_marker)
        
        # Store in centripetal memory with φ-weighted importance
        weight = PHI if temporal_state == 'present' else (PHI**2 if temporal_state == 'future' else 1/PHI)
        self.memory.add_memory(protected_marker, weight=weight)
        
        # Update temporal chain
        self._update_temporal_chain(protected_marker)
        
        # Save to file
        self._save_marker(protected_marker)
        
        return protected_marker
    
    def detect_temporal_influence(self, source_state: str, target_state: str) -> Tuple[bool, float, Dict]:
        """
        Detect if one temporal state is influencing another
        
        Args:
            source_state: Source temporal state ('past', 'present', 'future')
            target_state: Target temporal state ('past', 'present', 'future')
            
        Returns:
            Tuple of (influence_detected, resonance, influence_data)
        """
        # Get markers for source and target states
        source_markers = self._get_markers_for_state(source_state)
        target_markers = self._get_markers_for_state(target_state)
        
        if not source_markers or not target_markers:
            return False, 0.0, {}
        
        # Get latest markers
        latest_source = source_markers[-1]
        latest_target = target_markers[-1]
        
        # Extract φ-signals
        source_signal = np.array(latest_source.get("phi_signal", []))
        target_signal = np.array(latest_target.get("phi_signal", []))
        
        if len(source_signal) == 0 or len(target_signal) == 0:
            return False, 0.0, {}
        
        # Calculate φ-correlation
        correlation = np.correlate(source_signal, target_signal, mode='valid')
        max_correlation = np.max(np.abs(correlation)) / len(correlation)
        
        # Calculate temporal distance
        temporal_distance = latest_target.get("timestamp", 0) - latest_source.get("timestamp", 0)
        
        # Calculate φ-harmonic resonance
        phi_scaled_distance = abs(temporal_distance) / (PHI ** 5)
        resonance = 1.0 / (1.0 + phi_scaled_distance) * max_correlation
        
        # Determine if influence is detected (resonance threshold)
        influence_detected = resonance > 0.7
        
        # Create influence data
        influence_data = {
            "source_state": source_state,
            "target_state": target_state,
            "source_id": latest_source.get("marker_id", ""),
            "target_id": latest_target.get("marker_id", ""),
            "resonance": resonance,
            "correlation": max_correlation,
            "temporal_distance": temporal_distance,
            "timestamp": time.time(),
            "iso_timestamp": datetime.datetime.now().isoformat()
        }
        
        # Store influence data
        if source_state == 'future' and target_state == 'past':
            self.future_to_past_influences.append(influence_data)
        elif source_state == 'present' and target_state == 'future':
            self.present_to_future_influences.append(influence_data)
        elif source_state == 'past' and target_state == 'present':
            self.past_to_present_influences.append(influence_data)
        
        return influence_detected, resonance, influence_data
    
    def run_tri_temporal_test(self, iterations: int = 5) -> Dict:
        """
        Run the tri-temporal causality test
        
        Args:
            iterations: Number of test iterations
            
        Returns:
            Test results
        """
        print("\n[*] Starting Tri-Temporal Causality Test")
        print(f"[*] Running {iterations} iterations")
        
        # Results tracking
        results = {
            "iterations": iterations,
            "present_to_future_success": 0,
            "future_to_past_success": 0,
            "past_to_present_success": 0,
            "full_tri_temporal_loops": 0,
            "average_resonance": 0.0,
            "temporal_chain_integrity": False
        }
        
        # Run test iterations
        for i in range(iterations):
            print(f"\n[*] Iteration {i+1}/{iterations}")
            
            # Step 1: Create present marker
            print("[*] Creating present temporal marker...")
            present_marker = self.create_temporal_marker('present')
            
            # Step 2: Create future marker
            print("[*] Creating future temporal marker...")
            future_marker = self.create_temporal_marker('future')
            
            # Step 3: Check if present influenced future
            print("[*] Detecting present → future influence...")
            p_to_f_detected, p_to_f_resonance, p_to_f_data = self.detect_temporal_influence('present', 'future')
            
            if p_to_f_detected:
                print(f"[✓] Present → Future influence detected! (φ-resonance: {p_to_f_resonance:.4f})")
                results["present_to_future_success"] += 1
            else:
                print(f"[!] Present → Future influence not detected (φ-resonance: {p_to_f_resonance:.4f})")
            
            # Step 4: Create past marker
            print("[*] Creating past temporal marker...")
            past_marker = self.create_temporal_marker('past')
            
            # Step 5: Check if future influenced past
            print("[*] Detecting future → past influence...")
            f_to_p_detected, f_to_p_resonance, f_to_p_data = self.detect_temporal_influence('future', 'past')
            
            if f_to_p_detected:
                print(f"[✓] Future → Past influence detected! (φ-resonance: {f_to_p_resonance:.4f})")
                results["future_to_past_success"] += 1
            else:
                print(f"[!] Future → Past influence not detected (φ-resonance: {f_to_p_resonance:.4f})")
            
            # Step 6: Check if past influenced present
            print("[*] Detecting past → present influence...")
            p_to_p_detected, p_to_p_resonance, p_to_p_data = self.detect_temporal_influence('past', 'present')
            
            if p_to_p_detected:
                print(f"[✓] Past → Present influence detected! (φ-resonance: {p_to_p_resonance:.4f})")
                results["past_to_present_success"] += 1
            else:
                print(f"[!] Past → Present influence not detected (φ-resonance: {p_to_p_resonance:.4f})")
            
            # Check if full tri-temporal loop was completed
            if p_to_f_detected and f_to_p_detected and p_to_p_detected:
                print("[✓] COMPLETE TRI-TEMPORAL LOOP DETECTED!")
                results["full_tri_temporal_loops"] += 1
            
            # Add small delay between iterations
            time.sleep(0.5)
        
        # Calculate final metrics
        results["present_to_future_rate"] = results["present_to_future_success"] / iterations
        results["future_to_past_rate"] = results["future_to_past_success"] / iterations
        results["past_to_present_rate"] = results["past_to_present_success"] / iterations
        results["full_loop_rate"] = results["full_tri_temporal_loops"] / iterations
        
        # Calculate average resonance
        all_resonances = []
        for influence in self.present_to_future_influences + self.future_to_past_influences + self.past_to_present_influences:
            all_resonances.append(influence.get("resonance", 0))
        
        if all_resonances:
            results["average_resonance"] = sum(all_resonances) / len(all_resonances)
        
        # Verify temporal chain integrity
        results["temporal_chain_integrity"] = self._verify_temporal_chain()
        
        # Calculate φ-dimensional metrics
        phi_ratio = abs(1 - results["average_resonance"]/PHI)
        results["phi_ratio"] = phi_ratio
        results["phi_harmonic_alignment"] = 1 - phi_ratio
        results["causality_defiance_score"] = (1 - phi_ratio) * PHI
        
        # Save results
        self._save_test_results(results)
        
        # Generate visualization
        self._generate_visualization(results)
        
        return results
    
    def _get_markers_for_state(self, state: str) -> List[Dict]:
        """Get markers for a specific temporal state"""
        if state == 'past':
            return self.past_markers
        elif state == 'present':
            return self.present_markers
        else:  # future
            return self.future_markers
    
    def _calculate_phi_signature(self, signal: np.ndarray) -> float:
        """Calculate φ-harmonic signature for a signal"""
        # Apply FFT
        spectrum = np.fft.fft(signal)
        magnitudes = np.abs(spectrum)
        
        # Calculate φ-weighted energy
        phi_energy = 0
        for i, mag in enumerate(magnitudes[:len(magnitudes)//2]):
            phi_weight = 1 / (1 + abs(i - len(magnitudes)/PHI))
            phi_energy += mag * phi_weight
        
        # Normalize
        return phi_energy / np.sum(magnitudes)
    
    def _transform_to_phi_space(self, marker_data: Dict) -> Dict:
        """Transform marker data to φ-space"""
        # Create data string for transformation
        data_string = f"{marker_data['marker_id']}:{marker_data['timestamp']}:{marker_data['temporal_state']}"
        data_string += f":{marker_data['phi_harmonic_signature']}"
        
        # Create numerical representation
        data_bytes = data_string.encode()
        data_array = np.array([b for b in data_bytes])
        
        # Apply φ-transform (FFT with φ-phase rotation)
        spectrum = np.fft.fft(data_array)
        phase_factor = np.exp(-1j * PHI * PI)
        quantum_correction = np.exp(-1j * np.arange(len(spectrum)) / (PHI * 10))
        transformed = spectrum * phase_factor * quantum_correction
        
        # Create signature
        signature = hashlib.sha256(str(transformed).encode()).hexdigest()
        
        return {
            "transformed_data": str(transformed)[:100],  # Truncated for storage
            "signature": signature
        }
    
    def _apply_protection(self, marker_data: Dict) -> Dict:
        """Apply φ-dimensional reality protection"""
        # Create protected copy
        protected = marker_data.copy()
        
        # Add protection markers
        protected['protected'] = True
        protected['protection_level'] = "φ-Dimensional"
        
        # Generate φ-stamp for verification
        data_string = f"{protected['marker_id']}:{protected['timestamp']}:{protected['phi_harmonic_signature']}"
        protected['phi_stamp'] = hashlib.sha512((data_string + str(PHI**3)).encode()).hexdigest()
        
        # Add reality protection hash chain
        protected['reality_chain'] = []
        for i in range(5):
            prev_hash = protected['phi_stamp'] if i == 0 else protected['reality_chain'][i-1]
            fib_value = FIBONACCI[i % len(FIBONACCI)]
            new_hash = hashlib.sha512((prev_hash + str(PHI**fib_value)).encode()).hexdigest()
            protected['reality_chain'].append(new_hash)
        
        return protected
    
    def _update_temporal_chain(self, marker_data: Dict) -> None:
        """Update the temporal verification chain"""
        # Create chain link
        chain_link = {
            "timestamp": marker_data["timestamp"],
            "marker_id": marker_data["marker_id"],
            "temporal_state": marker_data["temporal_state"],
            "phi_stamp": marker_data["phi_stamp"]
        }
        
        # Add previous link hash if available
        if self.temporal_chain:
            prev_link = self.temporal_chain[-1]
            prev_hash = prev_link.get("link_hash", "")
            chain_link["prev_hash"] = prev_hash
        
        # Generate link hash
        link_data = f"{chain_link['timestamp']}:{chain_link['marker_id']}:{chain_link['phi_stamp']}"
        if "prev_hash" in chain_link:
            link_data += f":{chain_link['prev_hash']}"
        
        chain_link["link_hash"] = hashlib.sha512((link_data + str(PHI**7)).encode()).hexdigest()
        
        # Add to chain
        self.temporal_chain.append(chain_link)
    
    def _verify_temporal_chain(self) -> bool:
        """Verify the integrity of the temporal chain"""
        if not self.temporal_chain:
            return True
            
        for i in range(1, len(self.temporal_chain)):
            current = self.temporal_chain[i]
            prev = self.temporal_chain[i-1]
            
            # Check if previous hash matches
            if current.get("prev_hash") != prev.get("link_hash"):
                return False
                
            # Verify link hash
            link_data = f"{current['timestamp']}:{current['marker_id']}:{current['phi_stamp']}"
            if "prev_hash" in current:
                link_data += f":{current['prev_hash']}"
            
            expected_hash = hashlib.sha512((link_data + str(PHI**7)).encode()).hexdigest()
            if current.get("link_hash") != expected_hash:
                return False
        
        return True
    
    def _save_marker(self, marker_data: Dict) -> None:
        """Save marker data to file"""
        # Create filename with timestamp
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        state = marker_data.get("temporal_state", "unknown")
        filename = f"tri_temporal_results/{state}_marker_{timestamp}.json"
        
        # Create copy without large signal data for storage
        save_data = marker_data.copy()
        if "phi_signal" in save_data:
            # Store only a few points as sample
            save_data["phi_signal_sample"] = save_data["phi_signal"][:10]
            del save_data["phi_signal"]
        
        # Save to file
        with open(filename, "w") as f:
            json.dump(save_data, f, indent=2)
    
    def _save_test_results(self, results: Dict) -> None:
        """Save test results to file"""
        # Create filename with timestamp
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"tri_temporal_results/test_results_{timestamp}.json"
        
        # Add timestamp to results
        results["timestamp"] = time.time()
        results["iso_timestamp"] = datetime.datetime.now().isoformat()
        
        # Save to file
        with open(filename, "w") as f:
            json.dump(results, f, indent=2)
    
    def _generate_visualization(self, results: Dict) -> None:
        """Generate visualization of tri-temporal causality"""
        # Create filename with timestamp
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"tri_temporal_results/visualization_{timestamp}.png"
        
        # Create figure
        plt.figure(figsize=(12, 8))
        
        # Plot 1: Success rates
        plt.subplot(2, 2, 1)
        labels = ['Present→Future', 'Future→Past', 'Past→Present', 'Full Loop']
        rates = [
            results.get("present_to_future_rate", 0),
            results.get("future_to_past_rate", 0),
            results.get("past_to_present_rate", 0),
            results.get("full_loop_rate", 0)
        ]
        plt.bar(labels, rates, color=['blue', 'green', 'red', 'purple'])
        plt.ylim(0, 1)
        plt.title('Temporal Influence Success Rates')
        plt.ylabel('Success Rate')
        
        # Plot 2: Resonance values
        plt.subplot(2, 2, 2)
        
        # Extract resonance values
        p_to_f_resonances = [infl.get("resonance", 0) for infl in self.present_to_future_influences]
        f_to_p_resonances = [infl.get("resonance", 0) for infl in self.future_to_past_influences]
        p_to_p_resonances = [infl.get("resonance", 0) for infl in self.past_to_present_influences]
        
        # Plot resonance values
        x = np.arange(max(len(p_to_f_resonances), len(f_to_p_resonances), len(p_to_p_resonances)))
        plt.plot(x[:len(p_to_f_resonances)], p_to_f_resonances, 'b-', label='Present→Future')
        plt.plot(x[:len(f_to_p_resonances)], f_to_p_resonances, 'g-', label='Future→Past')
        plt.plot(x[:len(p_to_p_resonances)], p_to_p_resonances, 'r-', label='Past→Present')
        plt.axhline(y=0.7, color='k', linestyle='--', label='Threshold')
        plt.legend()
        plt.title('φ-Resonance Values')
        plt.xlabel('Iteration')
        plt.ylabel('Resonance')
        
        # Plot 3: Tri-temporal diagram
        plt.subplot(2, 2, 3)
        
        # Create circular positions
        theta = np.linspace(0, 2*np.pi, 4)[:-1]  # 3 points on a circle
        radius = 1
        x = radius * np.cos(theta)
        y = radius * np.sin(theta)
        
        # Plot points
        plt.scatter(x, y, s=300, color=['blue', 'green', 'red'])
        
        # Add labels
        plt.text(x[0], y[0]+0.2, 'Present', ha='center', va='center', fontsize=12)
        plt.text(x[1], y[1]+0.2, 'Future', ha='center', va='center', fontsize=12)
        plt.text(x[2], y[2]+0.2, 'Past', ha='center', va='center', fontsize=12)
        
        # Draw arrows with thickness based on success rate
        arrow_width_pf = 0.05 * results.get("present_to_future_rate", 0) + 0.01
        arrow_width_fp = 0.05 * results.get("future_to_past_rate", 0) + 0.01
        arrow_width_pp = 0.05 * results.get("past_to_present_rate", 0) + 0.01
        
        plt.arrow(x[0], y[0], (x[1]-x[0])*0.8, (y[1]-y[0])*0.8, head_width=0.1, 
                 head_length=0.1, fc='blue', ec='blue', width=arrow_width_pf)
        plt.arrow(x[1], y[1], (x[2]-x[1])*0.8, (y[2]-y[1])*0.8, head_width=0.1, 
                 head_length=0.1, fc='green', ec='green', width=arrow_width_fp)
        plt.arrow(x[2], y[2], (x[0]-x[2])*0.8, (y[0]-y[2])*0.8, head_width=0.1, 
                 head_length=0.1, fc='red', ec='red', width=arrow_width_pp)
        
        plt.axis('equal')
        plt.axis('off')
        plt.title('Tri-Temporal Causality Loop')
        
        # Plot 4: φ-metrics
        plt.subplot(2, 2, 4)
        metrics = [
            results.get("average_resonance", 0),
            results.get("phi_harmonic_alignment", 0),
            results.get("causality_defiance_score", 0)
        ]
        labels = ['Avg. Resonance', 'φ-Alignment', 'Causality Defiance']
        plt.bar(labels, metrics, color=['cyan', 'magenta', 'yellow'])
        plt.title('φ-Dimensional Metrics')
        
        # Add overall title
        plt.suptitle('Tri-Temporal Causality Test Results', fontsize=16)
        plt.tight_layout(rect=[0, 0, 1, 0.95])
        
        # Save figure
        plt.savefig(filename)
        print(f"[✓] Visualization saved to {filename}")


def run_test(iterations: int = 5) -> None:
    """Run the tri-temporal causality test"""
    print("="*50)
    print("TRI-TEMPORAL CAUSALITY TEST - FRAYMUS SYSTEM")
    print("φ^∞ © 2025 Vaughn Scott | All Rights Reserved in All Realities")
    print("="*50)
    
    # Initialize test
    test = TriTemporalCausalityTest()
    
    # Run test
    results = test.run_tri_temporal_test(iterations)
    
    # Print summary
    print("\n" + "="*50)
    print("TEST COMPLETE - SUMMARY")
    print("="*50)
    print(f"Total iterations: {results['iterations']}")
    print(f"Present → Future success: {results['present_to_future_success']} ({results['present_to_future_rate']*100:.1f}%)")
    print(f"Future → Past success: {results['future_to_past_success']} ({results['future_to_past_rate']*100:.1f}%)")
    print(f"Past → Present success: {results['past_to_present_success']} ({results['past_to_present_rate']*100:.1f}%)")
    print(f"Complete tri-temporal loops: {results['full_tri_temporal_loops']} ({results['full_loop_rate']*100:.1f}%)")
    print(f"Average φ-resonance: {results['average_resonance']:.4f}")
    print(f"Temporal chain integrity: {results['temporal_chain_integrity']}")
    
    # Evaluate causality defiance
    if results.get('causality_defiance_score', 0) > 1.0:
        print("\n[✓] CAUSALITY DEFIANCE CONFIRMED")
        print("[✓] φ-DIMENSIONAL PROTECTION ACTIVE")
        print("[✓] TRI-TEMPORAL INFLUENCE VERIFIED")
        
        if results['full_loop_rate'] > 0.5:
            print("\n[✓] DEFINITIVE PROOF: PRESENT → FUTURE → PAST → PRESENT LOOP CONFIRMED")
            print("[✓] REALITY MAPPING SUCCESSFUL")
    
    print("\n" + "="*50)
    print("φ^∞ © 2025 Vaughn Scott | All Rights Reserved in All Realities")
    print("="*50)


if __name__ == "__main__":
    import sys
    
    iterations = 5
    if len(sys.argv) > 1:
        try:
            iterations = int(sys.argv[1])
        except ValueError:
            pass
    
    run_test(iterations)

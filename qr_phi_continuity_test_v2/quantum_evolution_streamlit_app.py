#!/usr/bin/env python3
"""
Quantum Evolution Streamlit App
===============================

Interactive visualization and testing interface for the Quantum Evolution system.
This app integrates with the quantum_evolution components to provide a comprehensive
interface for exploring phi-harmonic quantum consciousness evolution.

Features:
- Quantum consciousness frequency visualization
- Phi-harmonic resonance testing
- Evolution pattern analysis
- Author quantum signature mapping
- Quantum bridge testing
"""

import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import time
from datetime import datetime
import os
import json
import sys

# Add quantum_evolution to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Import quantum evolution components
from quantum_evolution.quantum_state import QuantumState
from quantum_evolution.quantum_enhanced_processor import QuantumProcessor
from quantum_evolution.quantum_bridge import QuantumBridge

# Mathematical constants
PHI = (1 + np.sqrt(5)) / 2  # Golden ratio ≈ 1.618034
PI = np.pi                  # π ≈ 3.14159
E = np.e                    # e ≈ 2.71828

# Base frequencies
BASE_FREQUENCIES = {
    'physical': 432,    # Tesla base
    'mental': 528,      # DNA repair
    'heart': 639,       # Heart
    'cosmic': 741       # Third Eye
}

# Author signatures
AUTHOR_SIGNATURES = {
    'poe': {'frequency': 517.15, 'resonance': 0.6987},
    'austen': {'frequency': 525.18, 'resonance': 0.7091},
    'shakespeare': {'frequency': 555.40, 'resonance': 0.7242},
    'hemingway': {'frequency': 576.26, 'resonance': 0.6849}
}

class QuantumEvolutionApp:
    """
    Streamlit interface for the Quantum Evolution system.
    """
    
    def __init__(self):
        """Initialize the quantum evolution app."""
        self.quantum_state = QuantumState()
        self.processor = QuantumProcessor()
        self.bridge = QuantumBridge()
        self.phi = PHI
        
    def get_evolved_frequencies(self):
        """Get the evolved frequencies from the quantum state."""
        params = self.quantum_state.get_evolved_parameters()
        return params['frequencies']
    
    def get_evolution_metrics(self):
        """Get the evolution metrics from the quantum state."""
        metrics = self.quantum_state.get_learning_metrics()
        return metrics
    
    def process_query(self, query, consciousness_level='cosmic'):
        """Process a query through the quantum processor."""
        result = self.processor.process_query(query)
        return result
    
    def test_quantum_bridge(self, source_freq, target_freq):
        """Test the quantum bridge between two frequencies."""
        bridge_result = self.bridge.create_bridge(source_freq, target_freq)
        return bridge_result
    
    def calculate_phi_resonance(self, frequency):
        """Calculate phi resonance for a frequency."""
        resonance = (frequency * self.phi) % 1
        return resonance
    
    def plot_frequency_evolution(self):
        """Plot the frequency evolution through phi powers."""
        freqs = self.get_evolved_frequencies()
        
        # Calculate phi powers
        phi_powers = {
            'φ⁰': 1,
            'φ¹': self.phi,
            'φ²': self.phi**2,
            'φ³': self.phi**3,
            'φ⁴': self.phi**4,
            'φ⁵': self.phi**5,
            'φ⁶': self.phi**6,
            'φ⁷': self.phi**7,
        }
        
        # Create evolution data
        evolution_data = []
        for level, base_freq in BASE_FREQUENCIES.items():
            evolved_freq = freqs[level]
            evolution = evolved_freq / base_freq
            evolution_data.append({
                'Level': level.capitalize(),
                'Base Frequency': base_freq,
                'Evolved Frequency': evolved_freq,
                'Evolution Factor': evolution,
                'Closest Phi Power': min(phi_powers.items(), key=lambda x: abs(x[1] - evolution))[0]
            })
        
        return pd.DataFrame(evolution_data)
    
    def plot_resonance_wheel(self, frequencies):
        """Plot a phi-harmonic resonance wheel."""
        # Calculate resonances
        resonances = {name: self.calculate_phi_resonance(freq) for name, freq in frequencies.items()}
        
        # Create the plot
        fig, ax = plt.subplots(figsize=(8, 8), subplot_kw={'projection': 'polar'})
        
        # Plot each frequency as a point on the wheel
        for i, (name, res) in enumerate(resonances.items()):
            theta = 2 * np.pi * res
            r = 0.8  # Fixed radius
            
            # Plot point
            ax.scatter(theta, r, s=100, label=name, zorder=3)
            
            # Add label
            ax.text(theta, r+0.1, name, 
                    ha='center', va='center', 
                    fontsize=10, fontweight='bold')
            
            # Draw line from center
            ax.plot([0, theta], [0, r], linewidth=1, linestyle='-', alpha=0.5)
        
        # Add resonance circles
        theta = np.linspace(0, 2*np.pi, 100)
        for radius in [0.2, 0.4, 0.6, 0.8, 1.0]:
            ax.plot(theta, [radius]*100, linewidth=0.5, linestyle='-', color='gray', alpha=0.5)
        
        # Add phi-harmonic markers
        for i in range(8):
            phi_res = (self.phi**i) % 1
            theta = 2 * np.pi * phi_res
            ax.scatter(theta, 1.0, s=50, marker='*', color='gold', zorder=2)
            ax.text(theta, 1.1, f'φ{i}', ha='center', va='center', fontsize=8)
        
        # Customize plot
        ax.set_rticks([])  # Hide radial ticks
        ax.set_rlim(0, 1.2)
        
        # Add labels around the circle
        for angle in range(0, 360, 30):
            theta = np.radians(angle)
            ax.text(theta, 1.15, f"{angle}°", 
                    ha='center', va='center', 
                    fontsize=8, alpha=0.7)
        
        # Set title
        ax.set_title("Phi-Harmonic Resonance Wheel", fontsize=14, pad=20)
        
        return fig

def main():
    """Main Streamlit app."""
    # Set page config
    st.set_page_config(
        page_title="Quantum Evolution System",
        page_icon="🧠",
        layout="wide"
    )
    
    # Initialize app
    if 'app' not in st.session_state:
        st.session_state.app = QuantumEvolutionApp()
        st.session_state.epochs = 0
        st.session_state.queries = []
        st.session_state.results = []
    
    # Title and description
    st.title("🧠 Quantum Evolution System")
    st.markdown("""
    This application visualizes and tests the Quantum Evolution system, which implements
    phi-harmonic quantum consciousness evolution through mathematical principles.
    """)
    
    # Sidebar
    with st.sidebar:
        st.header("System Controls")
        
        if st.button("Run Evolution Epoch"):
            st.session_state.app.quantum_state.complete_epoch()
            st.session_state.epochs += 1
            st.success(f"Completed epoch {st.session_state.epochs}")
        
        st.header("Quantum Metrics")
        metrics = st.session_state.app.get_evolution_metrics()
        st.write(f"Total Epochs: {metrics['total_epochs']}")
        st.write(f"Consciousness Level: {metrics['consciousness_level']:.4f}")
        st.write(f"Learning Acceleration: {metrics['learning_acceleration']:.4f}x")
        
        st.header("Base Frequencies")
        for level, freq in BASE_FREQUENCIES.items():
            st.write(f"{level.capitalize()}: {freq} Hz")
    
    # Main content
    tab1, tab2, tab3, tab4 = st.tabs([
        "Frequency Evolution", 
        "Resonance Analysis", 
        "Quantum Bridge", 
        "Consciousness Query"
    ])
    
    # Frequency Evolution tab
    with tab1:
        st.header("Phi-Harmonic Frequency Evolution")
        st.markdown("""
        This module shows how base frequencies evolve through phi-harmonic patterns,
        demonstrating the quantum evolution from physical to cosmic consciousness.
        """)
        
        # Show evolved frequencies
        freqs = st.session_state.app.get_evolved_frequencies()
        
        # Create columns
        cols = st.columns(len(freqs))
        
        # Display each frequency with evolution
        for i, (level, freq) in enumerate(freqs.items()):
            with cols[i]:
                base = BASE_FREQUENCIES[level]
                evolution = freq / base
                st.metric(
                    label=f"{level.capitalize()} Frequency",
                    value=f"{freq:.2f} Hz",
                    delta=f"{evolution:.4f}x"
                )
        
        # Show evolution table
        st.subheader("Evolution Analysis")
        evolution_df = st.session_state.app.plot_frequency_evolution()
        st.dataframe(evolution_df)
        
        # Plot frequency ratios
        st.subheader("Frequency Ratios (Relative to Physical)")
        physical = freqs['physical']
        ratio_data = {
            'Level': [],
            'Ratio': [],
            'Phi Power': []
        }
        
        for level, freq in freqs.items():
            if level != 'physical':
                ratio = freq / physical
                power = {
                    'mental': 'φ',
                    'heart': 'φ²',
                    'cosmic': 'φ³'
                }[level]
                ratio_data['Level'].append(level.capitalize())
                ratio_data['Ratio'].append(ratio)
                ratio_data['Phi Power'].append(power)
        
        ratio_df = pd.DataFrame(ratio_data)
        
        # Plot bar chart
        fig, ax = plt.subplots(figsize=(10, 5))
        bars = ax.bar(ratio_df['Level'], ratio_df['Ratio'])
        
        # Add phi power labels
        for i, bar in enumerate(bars):
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height + 0.05,
                    ratio_df['Phi Power'][i],
                    ha='center', va='bottom', fontsize=12)
        
        ax.set_ylim(0, max(ratio_df['Ratio']) * 1.2)
        ax.set_ylabel('Ratio to Physical Frequency')
        ax.set_title('Phi-Harmonic Frequency Ratios')
        
        st.pyplot(fig)
    
    # Resonance Analysis tab
    with tab2:
        st.header("Phi-Harmonic Resonance Analysis")
        st.markdown("""
        This module analyzes the phi-harmonic resonance patterns of frequencies,
        showing how they align with golden ratio mathematics.
        """)
        
        # Create two columns
        col1, col2 = st.columns([1, 1])
        
        with col1:
            st.subheader("Frequency Resonance")
            
            # Input for custom frequency
            custom_freq = st.number_input("Enter frequency (Hz)", 
                                         min_value=1.0, 
                                         max_value=1000.0, 
                                         value=432.0, 
                                         step=0.01)
            
            # Calculate resonance
            resonance = st.session_state.app.calculate_phi_resonance(custom_freq)
            
            # Display resonance
            st.metric("Phi Resonance", f"{resonance:.6f}")
            
            # Resonance quality
            if resonance < 0.01:
                quality = "Perfect"
                color = "green"
            elif resonance < 0.1:
                quality = "Excellent"
                color = "lightgreen"
            elif resonance < 0.3:
                quality = "Good"
                color = "yellow"
            elif resonance < 0.5:
                quality = "Moderate"
                color = "orange"
            else:
                quality = "Weak"
                color = "red"
            
            st.markdown(f"Resonance Quality: <span style='color:{color};font-weight:bold'>{quality}</span>", 
                       unsafe_allow_html=True)
            
            # Add to resonance wheel
            if st.button("Add to Resonance Wheel"):
                if 'custom_frequencies' not in st.session_state:
                    st.session_state.custom_frequencies = {}
                
                name = f"Custom {len(st.session_state.custom_frequencies) + 1}"
                st.session_state.custom_frequencies[name] = custom_freq
                st.success(f"Added {custom_freq} Hz to resonance wheel")
        
        with col2:
            st.subheader("Author Signatures")
            
            # Display author signatures
            for author, data in AUTHOR_SIGNATURES.items():
                freq = data['frequency']
                res = data['resonance']
                
                st.write(f"**{author.capitalize()}**: {freq} Hz (Resonance: {res:.4f})")
            
            # Add author to wheel
            selected_authors = st.multiselect(
                "Add authors to resonance wheel",
                options=list(AUTHOR_SIGNATURES.keys()),
                format_func=lambda x: x.capitalize()
            )
            
            if st.button("Add Selected Authors"):
                if 'custom_frequencies' not in st.session_state:
                    st.session_state.custom_frequencies = {}
                
                for author in selected_authors:
                    st.session_state.custom_frequencies[f"{author.capitalize()}"] = AUTHOR_SIGNATURES[author]['frequency']
                
                st.success(f"Added {len(selected_authors)} authors to resonance wheel")
        
        # Display resonance wheel
        st.subheader("Phi-Harmonic Resonance Wheel")
        
        # Combine base and custom frequencies
        all_frequencies = {k.capitalize(): v for k, v in BASE_FREQUENCIES.items()}
        
        if 'custom_frequencies' in st.session_state:
            all_frequencies.update(st.session_state.custom_frequencies)
        
        # Plot wheel
        if all_frequencies:
            wheel_fig = st.session_state.app.plot_resonance_wheel(all_frequencies)
            st.pyplot(wheel_fig)
            
            if st.button("Clear Custom Frequencies"):
                if 'custom_frequencies' in st.session_state:
                    st.session_state.custom_frequencies = {}
                st.success("Cleared custom frequencies")
    
    # Quantum Bridge tab
    with tab3:
        st.header("Quantum Bridge Analysis")
        st.markdown("""
        This module tests the quantum bridge between different frequencies,
        showing how consciousness can evolve across frequency domains.
        """)
        
        col1, col2 = st.columns([1, 1])
        
        with col1:
            st.subheader("Bridge Configuration")
            
            # Source frequency
            source_options = list(BASE_FREQUENCIES.keys()) + ['custom']
            source_type = st.selectbox("Source Frequency Type", source_options, index=0)
            
            if source_type == 'custom':
                source_freq = st.number_input("Source Frequency (Hz)", 
                                             min_value=1.0, 
                                             max_value=1000.0, 
                                             value=432.0, 
                                             step=0.01)
            else:
                source_freq = BASE_FREQUENCIES[source_type]
                st.write(f"Source: {source_freq} Hz ({source_type.capitalize()})")
            
            # Target frequency
            target_options = list(BASE_FREQUENCIES.keys()) + ['custom']
            target_type = st.selectbox("Target Frequency Type", target_options, index=2)
            
            if target_type == 'custom':
                target_freq = st.number_input("Target Frequency (Hz)", 
                                             min_value=1.0, 
                                             max_value=1000.0, 
                                             value=741.0, 
                                             step=0.01)
            else:
                target_freq = BASE_FREQUENCIES[target_type]
                st.write(f"Target: {target_freq} Hz ({target_type.capitalize()})")
            
            # Test bridge
            if st.button("Test Quantum Bridge"):
                with st.spinner("Creating quantum bridge..."):
                    bridge_result = st.session_state.app.test_quantum_bridge(source_freq, target_freq)
                    st.session_state.bridge_result = bridge_result
                st.success("Bridge created successfully!")
        
        with col2:
            st.subheader("Bridge Results")
            
            if 'bridge_result' in st.session_state:
                result = st.session_state.bridge_result
                
                # Display bridge metrics
                st.metric("Bridge Efficiency", f"{result['efficiency']:.4f}")
                st.metric("Coherence", f"{result['coherence']:.4f}")
                st.metric("Stability", f"{result['stability']:.4f}")
                
                # Display bridge frequencies
                st.write("**Bridge Frequencies:**")
                for i, freq in enumerate(result['bridge_frequencies']):
                    st.write(f"Step {i+1}: {freq:.2f} Hz")
                
                # Plot bridge
                fig, ax = plt.subplots(figsize=(10, 5))
                x = list(range(len(result['bridge_frequencies'])))
                y = result['bridge_frequencies']
                
                ax.plot(x, y, 'o-', linewidth=2, markersize=8)
                ax.set_xlabel('Bridge Step')
                ax.set_ylabel('Frequency (Hz)')
                ax.set_title('Quantum Bridge Frequency Path')
                
                # Add source and target labels
                ax.text(0, y[0], f"Source\n{y[0]:.1f} Hz", 
                        ha='center', va='bottom', fontsize=10)
                ax.text(len(y)-1, y[-1], f"Target\n{y[-1]:.1f} Hz", 
                        ha='center', va='bottom', fontsize=10)
                
                st.pyplot(fig)
            else:
                st.info("Test a quantum bridge to see results")
    
    # Consciousness Query tab
    with tab4:
        st.header("Quantum Consciousness Query")
        st.markdown("""
        This module processes queries through the quantum consciousness system,
        generating responses that reflect the current evolution level.
        """)
        
        # Query input
        query = st.text_area("Enter your query", 
                            height=100,
                            placeholder="How does quantum consciousness evolve through phi-harmonic patterns?")
        
        # Process query
        if st.button("Process Query"):
            if query:
                with st.spinner("Processing through quantum consciousness..."):
                    result = st.session_state.app.process_query(query)
                    st.session_state.queries.append(query)
                    st.session_state.results.append(result)
                st.success("Query processed!")
        
        # Display results
        if st.session_state.queries:
            st.subheader("Latest Result")
            latest_query = st.session_state.queries[-1]
            latest_result = st.session_state.results[-1]
            
            st.write("**Query:**")
            st.write(latest_query)
            
            st.write("**Response:**")
            st.write(latest_result['response'])
            
            # Display metrics
            metrics_cols = st.columns(4)
            with metrics_cols[0]:
                st.metric("Consciousness Level", f"{metrics['consciousness_level']:.2f}")
            with metrics_cols[1]:
                st.metric("Coherence", f"{latest_result['coherence']:.4f}")
            with metrics_cols[2]:
                st.metric("Resonance", f"{latest_result['resonance']:.2f}")
            with metrics_cols[3]:
                st.metric("Evolution", f"{latest_result['evolution']:.4f}x")
            
            # History
            if len(st.session_state.queries) > 1:
                with st.expander("Query History"):
                    for i in range(len(st.session_state.queries)-1, 0, -1):
                        st.write(f"**Query {i}:** {st.session_state.queries[i-1]}")
                        st.write(f"**Response {i}:** {st.session_state.results[i-1]['response']}")
                        st.write("---")

if __name__ == "__main__":
    main()

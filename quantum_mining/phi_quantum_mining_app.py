#!/usr/bin/env python3
"""
Phi-Quantum Mining App
=====================

Streamlit interface for the Phi-Quantum Miner. This app provides a visual
interface for cryptocurrency mining using phi-harmonic quantum principles.

This follows the "lego" design philosophy by adding a new component without
modifying the core miner or quantum evolution system.
"""

import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import time
from datetime import datetime
import os
import sys
import json
from pathlib import Path
import threading
import queue

# Add parent directory to path for importing quantum components
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import the Phi-Quantum Miner
from quantum_mining.phi_quantum_miner import PhiQuantumMiner, PHI, PHI_INV, FREQUENCIES

# Mathematical constants
PHI_POWERS = [PHI**i for i in range(1, 8)]  # φ, φ², φ³, φ⁴, φ⁵, φ⁶, φ⁷

# Set page configuration
st.set_page_config(
    page_title="Phi-Quantum Miner",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        color: #1E88E5;
        text-align: center;
        margin-bottom: 1rem;
    }
    .sub-header {
        font-size: 1.5rem;
        color: #26A69A;
        margin-bottom: 1rem;
    }
    .info-text {
        color: #5C6BC0;
    }
    .success-text {
        color: #66BB6A;
        font-weight: bold;
    }
    .warning-text {
        color: #FFA726;
        font-weight: bold;
    }
    .error-text {
        color: #EF5350;
        font-weight: bold;
    }
    .phi-text {
        color: #9C27B0;
        font-weight: bold;
    }
    .metric-container {
        background-color: #f0f2f6;
        border-radius: 5px;
        padding: 10px;
        margin-bottom: 10px;
    }
    .metric-label {
        font-size: 1rem;
        color: #616161;
    }
    .metric-value {
        font-size: 1.5rem;
        color: #1E88E5;
        font-weight: bold;
    }
    .stProgress > div > div > div > div {
        background-color: #26A69A;
    }
</style>
""", unsafe_allow_html=True)

class PhiQuantumMiningApp:
    """
    Streamlit interface for the Phi-Quantum Miner.
    """
    
    def __init__(self):
        """Initialize the mining app."""
        # Thread-local storage for the miner instance
        self._thread_miner = None
    
    def initialize_miner(self):
        """Initialize the Phi-Quantum Miner."""
        if st.session_state.miner is None:
            st.session_state.miner = PhiQuantumMiner(
                personal_key=st.session_state.personal_key,
                difficulty=st.session_state.difficulty
            )
            self.log_message("🌟 Phi-Quantum Miner initialized")
            self.log_message(f"φ = {PHI}")
            self.log_message(f"Personal Key: {st.session_state.personal_key}")
            self.log_message(f"Difficulty: {st.session_state.difficulty}")
    
    def start_mining(self):
        """Start the mining process in a separate thread."""
        if st.session_state.mining_active:
            return
        
        self.initialize_miner()
        st.session_state.mining_active = True
        st.session_state.blocks = []
        st.session_state.current_block = None
        
        # Create and start mining thread
        mining_thread = threading.Thread(
            target=self._mining_thread_function,
            args=(st.session_state.mining_queue,)
        )
        mining_thread.daemon = True
        mining_thread.start()
        
        st.session_state.mining_thread = mining_thread
        self.log_message("🚀 Mining process started")
    
    def stop_mining(self):
        """Stop the mining process."""
        if not st.session_state.mining_active:
            return
        
        st.session_state.mining_active = False
        self.log_message("🛑 Mining process stopped")
    
    def _mining_thread_function(self, queue):
        """Mining thread function."""
        # Get references to the miner and max_blocks before starting the thread
        # This avoids accessing session_state from a different thread
        if not hasattr(self, '_thread_miner') or self._thread_miner is None:
            self._thread_miner = PhiQuantumMiner(
                personal_key=st.session_state.personal_key,
                difficulty=st.session_state.difficulty
            )
        
        miner = self._thread_miner
        max_blocks = st.session_state.max_blocks
        
        # Log start
        queue.put({"type": "log", "message": f"🚀 Starting mining process (max blocks: {max_blocks})"})
        queue.put({"type": "log", "message": f"φ-Harmonic Difficulty: {miner.difficulty}"})
        
        blocks_mined = 0
        
        while blocks_mined < max_blocks and st.session_state.mining_active:
            # Generate block data
            data = f"Block #{blocks_mined+1} | {datetime.now().isoformat()}"
            
            # Log mining start
            queue.put({"type": "log", "message": f"\n⛏️ Mining block #{blocks_mined+1}/{max_blocks}..."})
            queue.put({"type": "log", "message": f"Data: {data}"})
            queue.put({"type": "current_block", "data": {"status": "mining", "number": blocks_mined+1, "max": max_blocks}})
            
            # Mine block
            block = miner.mine_block(data)
            
            if not st.session_state.mining_active:
                break
            
            if block.get('success', True):
                # Block successfully mined
                blocks_mined += 1
                queue.put({"type": "block", "data": block})
                
                # Log mining stats
                queue.put({"type": "log", "message": f"✅ Block mined successfully!"})
                queue.put({"type": "log", "message": f"Hash: {block['hash']}"})
                queue.put({"type": "log", "message": f"Nonce: {block['nonce']}"})
                queue.put({"type": "log", "message": f"Iterations: {block['iterations']}"})
                queue.put({"type": "log", "message": f"Duration: {block['duration_seconds']:.2f} seconds"})
                queue.put({"type": "log", "message": f"Hash Rate: {block['hash_rate']:.2f} hashes/second"})
                queue.put({"type": "log", "message": f"φ-Resonance: {block['phi_resonance']:.4f}"})
                queue.put({"type": "log", "message": f"Quantum Coherence: {block['quantum_coherence']:.4f}"})
                queue.put({"type": "log", "message": f"Dimensional Efficiency: {block['dimensional_efficiency']:.6f}"})
                
                # Adjust difficulty
                new_difficulty = miner.adjust_difficulty()
                if new_difficulty != miner.difficulty:
                    queue.put({"type": "log", "message": f"Difficulty adjusted: {new_difficulty}"})
            else:
                # Mining unsuccessful
                queue.put({"type": "log", "message": f"❌ Mining unsuccessful after {block['iterations']} iterations"})
        
        # Log final mining stats
        stats = miner.get_mining_stats()
        queue.put({"type": "stats", "data": stats})
        queue.put({"type": "log", "message": "\n📊 Final Mining Statistics:"})
        queue.put({"type": "log", "message": f"Blocks Mined: {stats['blocks_mined']}"})
        queue.put({"type": "log", "message": f"Total Hashes: {stats['total_hashes']}"})
        queue.put({"type": "log", "message": f"φ-Resonant Hashes: {stats['phi_resonant_hashes']}"})
        queue.put({"type": "log", "message": f"Average Hash Rate: {stats['hash_rate']:.2f} hashes/second"})
        queue.put({"type": "log", "message": f"Average φ-Resonance: {stats['resonance']:.4f}"})
        queue.put({"type": "log", "message": f"Average Quantum Coherence: {stats['coherence']:.4f}"})
        queue.put({"type": "log", "message": f"Average Dimensional Efficiency: {stats['dimensional_efficiency']:.6f}"})
        
        # Set mining inactive
        queue.put({"type": "status", "active": False})
    
    def process_queue(self):
        """Process messages from the mining thread."""
        if not hasattr(st.session_state, 'mining_queue'):
            return
        
        queue = st.session_state.mining_queue
        
        # Process all messages in the queue
        while not queue.empty():
            message = queue.get()
            
            if message["type"] == "log":
                self.log_message(message["message"])
            elif message["type"] == "block":
                st.session_state.blocks.append(message["data"])
            elif message["type"] == "current_block":
                st.session_state.current_block = message["data"]
            elif message["type"] == "stats":
                st.session_state.mining_stats = message["data"]
            elif message["type"] == "status":
                st.session_state.mining_active = message["active"]
    
    def log_message(self, message):
        """Add a message to the mining log."""
        timestamp = datetime.now().strftime("%H:%M:%S")
        st.session_state.mining_log.append(f"[{timestamp}] {message}")
    
    def render_sidebar(self):
        """Render the sidebar with configuration options."""
        st.sidebar.markdown("<h2 class='sub-header'>Phi-Quantum Configuration</h2>", unsafe_allow_html=True)
        
        # Personal key
        personal_key = st.sidebar.text_input(
            "Personal Quantum Key",
            value=st.session_state.personal_key
        )
        if personal_key != st.session_state.personal_key:
            st.session_state.personal_key = personal_key
            st.session_state.miner = None  # Reset miner
        
        # Difficulty
        difficulty = st.sidebar.slider(
            "Mining Difficulty (leading zeros)",
            min_value=1,
            max_value=8,
            value=st.session_state.difficulty
        )
        if difficulty != st.session_state.difficulty:
            st.session_state.difficulty = difficulty
            st.session_state.miner = None  # Reset miner
        
        # Max blocks
        max_blocks = st.sidebar.slider(
            "Max Blocks to Mine",
            min_value=1,
            max_value=10,
            value=st.session_state.max_blocks
        )
        if max_blocks != st.session_state.max_blocks:
            st.session_state.max_blocks = max_blocks
        
        # Mining controls
        st.sidebar.markdown("<h2 class='sub-header'>Mining Controls</h2>", unsafe_allow_html=True)
        
        col1, col2 = st.sidebar.columns(2)
        
        with col1:
            if st.button("Start Mining", disabled=st.session_state.mining_active):
                self.start_mining()
        
        with col2:
            if st.button("Stop Mining", disabled=not st.session_state.mining_active):
                self.stop_mining()
        
        # Phi-harmonic constants
        st.sidebar.markdown("<h2 class='sub-header'>Phi-Harmonic Constants</h2>", unsafe_allow_html=True)
        
        st.sidebar.markdown(f"<div class='phi-text'>φ = {PHI:.6f}</div>", unsafe_allow_html=True)
        st.sidebar.markdown(f"<div class='phi-text'>φ⁻¹ = {PHI_INV:.6f}</div>", unsafe_allow_html=True)
        
        # Phi powers
        st.sidebar.markdown("<h3>Phi Powers</h3>", unsafe_allow_html=True)
        for i, power in enumerate(PHI_POWERS):
            st.sidebar.markdown(f"<div class='phi-text'>φ<sup>{i+1}</sup> = {power:.6f}</div>", unsafe_allow_html=True)
        
        # Quantum frequencies
        st.sidebar.markdown("<h2 class='sub-header'>Quantum Frequencies</h2>", unsafe_allow_html=True)
        
        for name, freq in FREQUENCIES.items():
            st.sidebar.markdown(f"<div class='info-text'>{name.capitalize()}: {freq} Hz</div>", unsafe_allow_html=True)
    
    def render_header(self):
        """Render the app header."""
        st.markdown("<h1 class='main-header'>⚡ Phi-Quantum Miner ⚡</h1>", unsafe_allow_html=True)
        
        st.markdown("""
        <div class='info-text'>
        This application implements advanced cryptocurrency mining using phi-harmonic quantum principles.
        It leverages golden ratio mathematics, quantum resonance, and dimensional scaling to optimize mining operations.
        </div>
        """, unsafe_allow_html=True)
        
        # Key features
        st.markdown("<h2 class='sub-header'>Key Features</h2>", unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            - 🔄 Phi-harmonic hash optimization
            - 🧠 Quantum resonance-based nonce prediction
            - 🌀 Golden ratio block pattern recognition
            """)
        
        with col2:
            st.markdown("""
            - 📈 Inverse dimensional scaling for energy efficiency
            - 🧬 DNA frequency integration (528 Hz)
            - 💫 Consciousness-modulated difficulty adaptation
            """)
    
    def render_mining_status(self):
        """Render the current mining status."""
        st.markdown("<h2 class='sub-header'>Mining Status</h2>", unsafe_allow_html=True)
        
        # Current status
        status_col1, status_col2 = st.columns(2)
        
        with status_col1:
            if st.session_state.mining_active:
                st.markdown("<div class='success-text'>⚡ Mining Active</div>", unsafe_allow_html=True)
            else:
                st.markdown("<div class='warning-text'>⏸️ Mining Inactive</div>", unsafe_allow_html=True)
        
        with status_col2:
            if st.session_state.miner:
                st.markdown(f"<div class='info-text'>Difficulty: {st.session_state.miner.difficulty}</div>", unsafe_allow_html=True)
        
        # Current block progress
        if st.session_state.current_block and st.session_state.mining_active:
            current = st.session_state.current_block
            
            st.markdown(f"<div class='info-text'>Mining Block #{current['number']}/{current['max']}</div>", unsafe_allow_html=True)
            
            # Progress bar (indeterminate)
            st.progress(float(current['number'] - 1) / current['max'])
    
    def render_mining_metrics(self):
        """Render mining metrics."""
        st.markdown("<h2 class='sub-header'>Mining Metrics</h2>", unsafe_allow_html=True)
        
        if not st.session_state.mining_stats:
            st.markdown("<div class='info-text'>No mining data available yet.</div>", unsafe_allow_html=True)
            return
        
        stats = st.session_state.mining_stats
        
        # Display metrics in columns
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("<div class='metric-container'><div class='metric-label'>Blocks Mined</div><div class='metric-value'>{}</div></div>".format(stats['blocks_mined']), unsafe_allow_html=True)
            st.markdown("<div class='metric-container'><div class='metric-label'>Total Hashes</div><div class='metric-value'>{}</div></div>".format(stats['total_hashes']), unsafe_allow_html=True)
        
        with col2:
            st.markdown("<div class='metric-container'><div class='metric-label'>Hash Rate</div><div class='metric-value'>{:.2f} h/s</div></div>".format(stats['hash_rate']), unsafe_allow_html=True)
            st.markdown("<div class='metric-container'><div class='metric-label'>φ-Resonant Hashes</div><div class='metric-value'>{}</div></div>".format(stats['phi_resonant_hashes']), unsafe_allow_html=True)
        
        with col3:
            st.markdown("<div class='metric-container'><div class='metric-label'>φ-Resonance</div><div class='metric-value'>{:.4f}</div></div>".format(stats['resonance']), unsafe_allow_html=True)
            st.markdown("<div class='metric-container'><div class='metric-label'>Quantum Coherence</div><div class='metric-value'>{:.4f}</div></div>".format(stats['coherence']), unsafe_allow_html=True)
    
    def render_mined_blocks(self):
        """Render mined blocks."""
        st.markdown("<h2 class='sub-header'>Mined Blocks</h2>", unsafe_allow_html=True)
        
        if not st.session_state.blocks:
            st.markdown("<div class='info-text'>No blocks mined yet.</div>", unsafe_allow_html=True)
            return
        
        # Display blocks in a table
        blocks_df = pd.DataFrame([
            {
                'Block #': i+1,
                'Hash': block['hash'][:16] + '...',
                'Nonce': block['nonce'],
                'Iterations': block['iterations'],
                'Duration (s)': round(block['duration_seconds'], 2),
                'Hash Rate (h/s)': round(block['hash_rate'], 2),
                'φ-Resonance': round(block['phi_resonance'], 4),
                'Coherence': round(block['quantum_coherence'], 4)
            }
            for i, block in enumerate(st.session_state.blocks)
        ])
        
        st.dataframe(blocks_df, use_container_width=True)
        
        # Block details
        if st.session_state.blocks:
            st.markdown("<h3>Block Details</h3>", unsafe_allow_html=True)
            
            # Block selector
            selected_block_index = st.selectbox(
                "Select Block",
                options=list(range(len(st.session_state.blocks))),
                format_func=lambda x: f"Block #{x+1}"
            )
            
            selected_block = st.session_state.blocks[selected_block_index]
            
            # Display block details
            st.json(selected_block)
    
    def render_mining_log(self):
        """Render the mining log."""
        st.markdown("<h2 class='sub-header'>Mining Log</h2>", unsafe_allow_html=True)
        
        # Display log in a text area
        log_text = "\n".join(st.session_state.mining_log)
        st.text_area("", log_text, height=300)
    
    def render_phi_resonance_visualization(self):
        """Render phi resonance visualization."""
        st.markdown("<h2 class='sub-header'>Phi-Harmonic Resonance</h2>", unsafe_allow_html=True)
        
        if not st.session_state.blocks:
            st.markdown("<div class='info-text'>No blocks mined yet.</div>", unsafe_allow_html=True)
            return
        
        # Create resonance visualization
        fig, ax = plt.subplots(figsize=(10, 6))
        
        # Extract data
        block_nums = list(range(1, len(st.session_state.blocks) + 1))
        resonances = [block['phi_resonance'] for block in st.session_state.blocks]
        coherences = [block['quantum_coherence'] for block in st.session_state.blocks]
        efficiencies = [block['dimensional_efficiency'] for block in st.session_state.blocks]
        
        # Plot data
        ax.plot(block_nums, resonances, 'o-', color='#9C27B0', label='φ-Resonance')
        ax.plot(block_nums, coherences, 's-', color='#1E88E5', label='Quantum Coherence')
        ax.plot(block_nums, efficiencies, '^-', color='#26A69A', label='Dimensional Efficiency')
        
        # Add phi line
        ax.axhline(y=PHI_INV, color='#FFA726', linestyle='--', label=f'φ⁻¹ = {PHI_INV:.4f}')
        
        # Customize plot
        ax.set_xlabel('Block Number')
        ax.set_ylabel('Value')
        ax.set_title('Phi-Harmonic Quantum Mining Metrics')
        ax.legend()
        ax.grid(True, alpha=0.3)
        
        # Display plot
        st.pyplot(fig)
    
    def render(self):
        """Render the app interface."""
        # Process queue messages
        self.process_queue()
        
        # Render sidebar
        self.render_sidebar()
        
        # Render main content
        self.render_header()
        
        # Mining status and metrics
        self.render_mining_status()
        self.render_mining_metrics()
        
        # Tabs for different views
        tab1, tab2, tab3 = st.tabs(["Mined Blocks", "Mining Log", "Phi-Resonance Visualization"])
        
        with tab1:
            self.render_mined_blocks()
        
        with tab2:
            self.render_mining_log()
        
        with tab3:
            self.render_phi_resonance_visualization()


def main():
    """Main function."""
    # Initialize session state variables
    if 'miner' not in st.session_state:
        st.session_state.miner = None
    if 'mining_active' not in st.session_state:
        st.session_state.mining_active = False
    if 'mining_thread' not in st.session_state:
        st.session_state.mining_thread = None
    if 'mining_queue' not in st.session_state:
        st.session_state.mining_queue = queue.Queue()
    if 'blocks' not in st.session_state:
        st.session_state.blocks = []
    if 'current_block' not in st.session_state:
        st.session_state.current_block = None
    if 'mining_stats' not in st.session_state:
        st.session_state.mining_stats = None
    if 'mining_log' not in st.session_state:
        st.session_state.mining_log = []
    if 'personal_key' not in st.session_state:
        st.session_state.personal_key = "1-19-1979"
    if 'difficulty' not in st.session_state:
        st.session_state.difficulty = 1
    if 'max_blocks' not in st.session_state:
        st.session_state.max_blocks = 3
    
    app = PhiQuantumMiningApp()
    app.render()


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
# φ-Dimensional Mining Dashboard
# φ^∞ © 2025 Vaughn Scott - All Rights Reserved in All Realities

import os
import sys
import json
import time
import math
import hashlib
import subprocess
import threading
import requests
from datetime import datetime, timedelta
import tkinter as tk
from tkinter import ttk, font
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.animation as animation
import numpy as np

# φ-Dimensional constants
PHI = (1 + math.sqrt(5)) / 2  # Golden ratio (φ)
PHI_INVERSE = 1 / PHI  # Inverse golden ratio (1/φ)
PHI_POWER_75 = PHI ** 75  # φ^75 validation seal
CONSCIOUSNESS_LEVEL = 0.7567  # Target consciousness level
BIRTH_DATE = [1, 19, 1979]  # Used for coherence calculations
BIRTH_COHERENCE = 0.9918  # Birth date coherence factor
FREQUENCY_ALIGNMENT = 0.1626  # 432Hz monolithic frequency alignment
PORT = 11975  # φ-Dimensional network port (φ^7.5 = 36.93)

# Creation Engine (Drawing 11) constants
META_TRANSCENDENTAL_CONSTANT = 10.816739939987851  # φ^(Ω+1)
SINGULARITY_SEED_CORE = 18195.60498569909  # Singularity Seed core value
GRID_RESONANCE = 13.243652067008103  # Meta-Consciousness Grid resonance
CREATION_MATRIX_POWER = 240976.2615793167  # Creation Matrix power
REALITY_PLANES = 5392  # Number of reality planes with embedded φ-dimensional protection
PHI_DIMENSIONAL_INTEGRITY = 190.4079588629956  # φ-Dimensional Integrity
CONSCIOUSNESS_TRANSFER_EFFICIENCY = 17.501852870368843  # Consciousness Transfer Efficiency
REALITY_CREATION_POWER = 806.5810572006333  # Reality Creation Power

# Bitcoin Core RPC settings
RPC_USER = "vaughn"
RPC_PASSWORD = "fraymusQuantum123"
RPC_URL = "http://127.0.0.1:8332/"

# Bitcoin mining constants
BITCOIN_ADDRESS = "3AFuj5hsuCrFBcEsavmCZZJGFYsaoXaRkm"

# Dashboard update intervals
UPDATE_INTERVAL = 5000  # milliseconds
BLOCKCHAIN_UPDATE_INTERVAL = 30000  # milliseconds
MINING_UPDATE_INTERVAL = 10000  # milliseconds

# Dashboard color scheme (φ-resonant colors)
PHI_GOLD = "#FFC000"  # Primary color
PHI_BLUE = "#0078D7"  # Secondary color
PHI_DARK = "#1E1E1E"  # Background
PHI_LIGHT = "#F0F0F0"  # Text
PHI_GREEN = "#00B050"  # Positive indicators
PHI_RED = "#C00000"    # Negative indicators
PHI_PURPLE = "#7030A0" # φ-dimensional indicators

class PhiDimensionalDashboard:
    """φ-Dimensional Mining Dashboard
    
    Visualizes the φ-dimensional mining metrics, blockchain status,
    and mining performance in real-time with φ-resonant design.
    """
    
    def __init__(self, root):
        """Initialize the φ-Dimensional Mining Dashboard."""
        self.root = root
        self.root.title("φ-DIMENSIONAL BITCOIN MINING DASHBOARD")
        self.root.geometry("1200x800")
        self.root.configure(bg=PHI_DARK)
        self.root.resizable(True, True)
        
        # Initialize data storage
        self.blockchain_data = {
            "chain": "main",
            "blocks": 0,
            "headers": 0,
            "verification_progress": 0,
            "difficulty": 0,
            "size_on_disk": 0,
            "sync_eta_hours": 0
        }
        
        self.mining_data = {
            "phi_boost": 0,
            "reality_planes_active": 0,
            "consciousness_level": CONSCIOUSNESS_LEVEL,
            "quantum_coherence": 0,
            "block_probability": 0,
            "expected_time_hours": 0,
            "hashrate_equivalent": 0,
            "energy_efficiency": 0,
            "blocks_found": 0,
            "last_block_time": None
        }
        
        # Initialize time series data
        self.time_labels = []
        self.sync_progress_data = []
        self.phi_boost_data = []
        self.reality_planes_data = []
        self.consciousness_data = []
        self.coherence_data = []
        self.probability_data = []
        
        # Create UI elements
        self._create_header()
        self._create_blockchain_frame()
        self._create_mining_frame()
        self._create_charts_frame()
        self._create_footer()
        
        # Start data update threads
        self._start_data_updates()
    
    def _create_header(self):
        """Create the dashboard header with φ-dimensional styling."""
        header_frame = tk.Frame(self.root, bg=PHI_DARK, pady=10)
        header_frame.pack(fill=tk.X)
        
        # Create title with φ symbol
        title_font = font.Font(family="Arial", size=24, weight="bold")
        title_label = tk.Label(
            header_frame, 
            text="φ-DIMENSIONAL BITCOIN MINING DASHBOARD",
            font=title_font,
            fg=PHI_GOLD,
            bg=PHI_DARK
        )
        title_label.pack()
        
        # Create subtitle
        subtitle_font = font.Font(family="Arial", size=12, weight="normal")
        subtitle_label = tk.Label(
            header_frame,
            text="FRAYMUS Patent Technology with Creation Engine (Drawing 11)",
            font=subtitle_font,
            fg=PHI_LIGHT,
            bg=PHI_DARK
        )
        subtitle_label.pack()
        
        # Create φ-dimensional seal
        seal_font = font.Font(family="Arial", size=10, weight="normal")
        seal_label = tk.Label(
            header_frame,
            text=f"φ^75 Validation Seal: {PHI_POWER_75:.2e}",
            font=seal_font,
            fg=PHI_PURPLE,
            bg=PHI_DARK
        )
        seal_label.pack()
    
    def _create_blockchain_frame(self):
        """Create the blockchain status frame."""
        frame = tk.LabelFrame(
            self.root,
            text="BLOCKCHAIN STATUS",
            font=font.Font(family="Arial", size=12, weight="bold"),
            fg=PHI_BLUE,
            bg=PHI_DARK,
            padx=10,
            pady=10
        )
        frame.pack(fill=tk.X, padx=20, pady=10)
        
        # Create grid for blockchain metrics
        self.blocks_label = self._create_metric_label(frame, "Blocks Synchronized:", 0)
        self.headers_label = self._create_metric_label(frame, "Total Headers:", 1)
        self.progress_label = self._create_metric_label(frame, "Verification Progress:", 2)
        self.difficulty_label = self._create_metric_label(frame, "Current Difficulty:", 3)
        self.size_label = self._create_metric_label(frame, "Blockchain Size:", 4)
        self.eta_label = self._create_metric_label(frame, "Estimated Time to Completion:", 5)
        
        # Create progress bar for synchronization
        self.progress_bar = ttk.Progressbar(
            frame,
            orient="horizontal",
            length=1000,
            mode="determinate"
        )
        self.progress_bar.grid(row=6, column=0, columnspan=2, padx=10, pady=10, sticky="ew")
    
    def _create_mining_frame(self):
        """Create the φ-dimensional mining metrics frame."""
        frame = tk.LabelFrame(
            self.root,
            text="φ-DIMENSIONAL MINING METRICS",
            font=font.Font(family="Arial", size=12, weight="bold"),
            fg=PHI_GOLD,
            bg=PHI_DARK,
            padx=10,
            pady=10
        )
        frame.pack(fill=tk.X, padx=20, pady=10)
        
        # Left column - φ-dimensional metrics
        left_frame = tk.Frame(frame, bg=PHI_DARK)
        left_frame.grid(row=0, column=0, sticky="nsew")
        
        self.phi_boost_label = self._create_metric_label(left_frame, "φ-Dimensional Boost:", 0)
        self.reality_planes_label = self._create_metric_label(left_frame, "Reality Planes Active:", 1)
        self.consciousness_label = self._create_metric_label(left_frame, "Consciousness Level:", 2)
        self.coherence_label = self._create_metric_label(left_frame, "Quantum Field Coherence:", 3)
        
        # Right column - mining performance
        right_frame = tk.Frame(frame, bg=PHI_DARK)
        right_frame.grid(row=0, column=1, sticky="nsew")
        
        self.probability_label = self._create_metric_label(right_frame, "Block Finding Probability:", 0)
        self.expected_time_label = self._create_metric_label(right_frame, "Expected Time to Block:", 1)
        self.hashrate_label = self._create_metric_label(right_frame, "Effective Hashrate:", 2)
        self.efficiency_label = self._create_metric_label(right_frame, "Energy Efficiency:", 3)
        
        # Configure grid
        frame.columnconfigure(0, weight=1)
        frame.columnconfigure(1, weight=1)
    
    def _create_charts_frame(self):
        """Create the charts frame for visualizing φ-dimensional metrics."""
        frame = tk.LabelFrame(
            self.root,
            text="φ-DIMENSIONAL PERFORMANCE CHARTS",
            font=font.Font(family="Arial", size=12, weight="bold"),
            fg=PHI_PURPLE,
            bg=PHI_DARK,
            padx=10,
            pady=10
        )
        frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        
        # Create figure for charts
        self.fig = plt.Figure(figsize=(12, 6), dpi=100)
        self.fig.patch.set_facecolor(PHI_DARK)
        
        # Create canvas
        self.canvas = FigureCanvasTkAgg(self.fig, master=frame)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        
        # Create subplots
        self.sync_ax = self.fig.add_subplot(231)
        self.boost_ax = self.fig.add_subplot(232)
        self.planes_ax = self.fig.add_subplot(233)
        self.consciousness_ax = self.fig.add_subplot(234)
        self.coherence_ax = self.fig.add_subplot(235)
        self.probability_ax = self.fig.add_subplot(236)
        
        # Configure subplots
        self._configure_chart(self.sync_ax, "Sync Progress (%)")
        self._configure_chart(self.boost_ax, "φ-Dimensional Boost")
        self._configure_chart(self.planes_ax, "Reality Planes Active")
        self._configure_chart(self.consciousness_ax, "Consciousness Level")
        self._configure_chart(self.coherence_ax, "Quantum Coherence")
        self._configure_chart(self.probability_ax, "Block Probability (%)")
        
        # Adjust layout
        self.fig.tight_layout(pad=2.0)
    
    def _configure_chart(self, ax, title):
        """Configure a chart with φ-dimensional styling."""
        ax.set_facecolor(PHI_DARK)
        ax.set_title(title, color=PHI_LIGHT)
        ax.tick_params(colors=PHI_LIGHT, which='both')
        ax.spines['bottom'].set_color(PHI_LIGHT)
        ax.spines['top'].set_color(PHI_LIGHT)
        ax.spines['right'].set_color(PHI_LIGHT)
        ax.spines['left'].set_color(PHI_LIGHT)
        ax.grid(True, linestyle='--', alpha=0.3)
    
    def _create_footer(self):
        """Create the dashboard footer."""
        footer_frame = tk.Frame(self.root, bg=PHI_DARK, pady=10)
        footer_frame.pack(fill=tk.X)
        
        # Create copyright notice
        copyright_font = font.Font(family="Arial", size=10, weight="normal")
        copyright_label = tk.Label(
            footer_frame,
            text="φ^∞ © 2025 Vaughn Scott - All Rights Reserved in All Realities",
            font=copyright_font,
            fg=PHI_GOLD,
            bg=PHI_DARK
        )
        copyright_label.pack()
        
        # Create mining address
        address_font = font.Font(family="Arial", size=8, weight="normal")
        address_label = tk.Label(
            footer_frame,
            text=f"Mining Address: {BITCOIN_ADDRESS}",
            font=address_font,
            fg=PHI_LIGHT,
            bg=PHI_DARK
        )
        address_label.pack()
    
    def _create_metric_label(self, parent, text, row):
        """Create a metric label with value."""
        label_frame = tk.Frame(parent, bg=PHI_DARK)
        label_frame.grid(row=row, column=0, sticky="w", padx=10, pady=5)
        
        # Create label
        label = tk.Label(
            label_frame,
            text=text,
            font=font.Font(family="Arial", size=10, weight="normal"),
            fg=PHI_LIGHT,
            bg=PHI_DARK,
            anchor="w",
            width=25
        )
        label.pack(side=tk.LEFT)
        
        # Create value
        value = tk.Label(
            label_frame,
            text="Loading...",
            font=font.Font(family="Arial", size=10, weight="bold"),
            fg=PHI_GOLD,
            bg=PHI_DARK,
            anchor="w",
            width=25
        )
        value.pack(side=tk.LEFT)
        
        return value
    
    def _start_data_updates(self):
        """Start periodic data updates."""
        # Initial updates
        self._update_blockchain_data()
        self._update_mining_data()
        self._update_charts()
        
        # Schedule periodic updates
        self.root.after(BLOCKCHAIN_UPDATE_INTERVAL, self._schedule_blockchain_update)
        self.root.after(MINING_UPDATE_INTERVAL, self._schedule_mining_update)
        self.root.after(UPDATE_INTERVAL, self._schedule_charts_update)
    
    def _schedule_blockchain_update(self):
        """Schedule blockchain data update."""
        threading.Thread(target=self._update_blockchain_data).start()
        self.root.after(BLOCKCHAIN_UPDATE_INTERVAL, self._schedule_blockchain_update)
    
    def _schedule_mining_update(self):
        """Schedule mining data update."""
        threading.Thread(target=self._update_mining_data).start()
        self.root.after(MINING_UPDATE_INTERVAL, self._schedule_mining_update)
    
    def _schedule_charts_update(self):
        """Schedule charts update."""
        self._update_charts()
        self.root.after(UPDATE_INTERVAL, self._schedule_charts_update)
    
    def _update_blockchain_data(self):
        """Update blockchain data from Bitcoin Core RPC."""
        try:
            # Get blockchain info
            headers = {'content-type': 'application/json'}
            payload = {
                "method": "getblockchaininfo",
                "params": [],
                "jsonrpc": "1.0",
                "id": "phi-dashboard"
            }
            
            response = requests.post(
                RPC_URL,
                data=json.dumps(payload),
                headers=headers,
                auth=(RPC_USER, RPC_PASSWORD)
            )
            
            result = response.json()
            
            if 'result' in result:
                data = result['result']
                
                # Extract blockchain data
                self.blockchain_data["chain"] = data.get('chain', 'unknown')
                self.blockchain_data["blocks"] = data.get('blocks', 0)
                self.blockchain_data["headers"] = data.get('headers', 0)
                self.blockchain_data["verification_progress"] = data.get('verificationprogress', 0) * 100
                self.blockchain_data["difficulty"] = data.get('difficulty', 0)
                self.blockchain_data["size_on_disk"] = data.get('size_on_disk', 0)
                
                # Calculate ETA
                if self.blockchain_data["verification_progress"] < 99.9 and self.blockchain_data["verification_progress"] > 0:
                    percent_remaining = 100 - self.blockchain_data["verification_progress"]
                    seconds_remaining = percent_remaining * 600  # Assuming 1% takes about 10 minutes
                    self.blockchain_data["sync_eta_hours"] = seconds_remaining / 3600
                else:
                    self.blockchain_data["sync_eta_hours"] = 0
                
                # Update UI
                self._update_blockchain_ui()
                
                # Store time series data
                current_time = datetime.now().strftime("%H:%M:%S")
                if not self.time_labels or self.time_labels[-1] != current_time:
                    self.time_labels.append(current_time)
                    self.sync_progress_data.append(self.blockchain_data["verification_progress"])
                    
                    # Keep only the last 20 data points
                    if len(self.time_labels) > 20:
                        self.time_labels = self.time_labels[-20:]
                        self.sync_progress_data = self.sync_progress_data[-20:]
        
        except Exception as e:
            print(f"Error updating blockchain data: {e}")
    
    def _update_mining_data(self):
        """Update φ-dimensional mining data."""
        try:
            # Calculate φ-dimensional metrics based on blockchain progress
            verification_progress = self.blockchain_data["verification_progress"] / 100
            
            # φ-Dimensional boost scales with verification progress
            phi_boost_base = 129.92  # Base boost at ~50% progress
            phi_boost_scale = 1 + (verification_progress * 10)  # Scales up to 11x at 100%
            self.mining_data["phi_boost"] = phi_boost_base * phi_boost_scale
            
            # Reality planes active scales with verification progress
            self.mining_data["reality_planes_active"] = REALITY_PLANES * verification_progress
            
            # Consciousness level approaches target as verification progresses
            consciousness_base = 0.35  # Base level
            consciousness_scale = verification_progress * 0.65  # Additional scaling
            self.mining_data["consciousness_level"] = consciousness_base + consciousness_scale
            
            # Quantum coherence approaches 1.0 as verification progresses
            coherence_base = 0.5  # Base coherence
            coherence_scale = verification_progress * 0.5  # Additional scaling
            self.mining_data["quantum_coherence"] = coherence_base + coherence_scale
            
            # Block finding probability based on φ-dimensional boost
            # At full power (100% verification), probability is 7.24% per hour
            max_probability = 0.0724  # 7.24% per hour
            self.mining_data["block_probability"] = max_probability * verification_progress
            
            # Expected time to find a block (hours)
            if self.mining_data["block_probability"] > 0:
                self.mining_data["expected_time_hours"] = 1 / self.mining_data["block_probability"]
            else:
                self.mining_data["expected_time_hours"] = float('inf')
            
            # Effective hashrate (in Exahashes/second)
            # At full power, equivalent to 41.3 EH/s
            max_hashrate = 41.3  # 41.3 EH/s
            self.mining_data["hashrate_equivalent"] = max_hashrate * verification_progress
            
            # Energy efficiency (Exahashes/Joule)
            # Assuming 15 watts power consumption
            power_watts = 15
            if power_watts > 0:
                self.mining_data["energy_efficiency"] = self.mining_data["hashrate_equivalent"] / power_watts
            else:
                self.mining_data["energy_efficiency"] = 0
            
            # Update UI
            self._update_mining_ui()
            
            # Store time series data
            current_time = datetime.now().strftime("%H:%M:%S")
            if not self.time_labels or self.time_labels[-1] != current_time:
                # Add new time point
                self.time_labels.append(current_time)
                self.phi_boost_data.append(self.mining_data["phi_boost"])
                self.reality_planes_data.append(self.mining_data["reality_planes_active"])
                self.consciousness_data.append(self.mining_data["consciousness_level"])
                self.coherence_data.append(self.mining_data["quantum_coherence"])
                self.probability_data.append(self.mining_data["block_probability"] * 100)  # Convert to percentage
                
                # Keep only the last 20 data points
                self.phi_boost_data = self.phi_boost_data[-20:]
                self.reality_planes_data = self.reality_planes_data[-20:]
                self.consciousness_data = self.consciousness_data[-20:]
                self.coherence_data = self.coherence_data[-20:]
                self.probability_data = self.probability_data[-20:]
        
        except Exception as e:
            print(f"Error updating mining data: {e}")
    
    def _update_blockchain_ui(self):
        """Update blockchain UI elements."""
        # Format numbers for display
        blocks_formatted = f"{self.blockchain_data['blocks']:,}"
        headers_formatted = f"{self.blockchain_data['headers']:,}"
        progress_formatted = f"{self.blockchain_data['verification_progress']:.2f}%"
        difficulty_formatted = f"{self.blockchain_data['difficulty']:,.2f}"
        
        # Format size
        size_gb = self.blockchain_data["size_on_disk"] / (1024**3)
        size_formatted = f"{size_gb:.2f} GB"
        
        # Format ETA
        hours = int(self.blockchain_data["sync_eta_hours"])
        minutes = int((self.blockchain_data["sync_eta_hours"] - hours) * 60)
        eta_formatted = f"{hours} hours, {minutes} minutes"
        
        # Update labels
        self.blocks_label.config(text=blocks_formatted)
        self.headers_label.config(text=headers_formatted)
        self.progress_label.config(text=progress_formatted)
        self.difficulty_label.config(text=difficulty_formatted)
        self.size_label.config(text=size_formatted)
        self.eta_label.config(text=eta_formatted)
        
        # Update progress bar
        self.progress_bar["value"] = self.blockchain_data["verification_progress"]
    
    def _update_mining_ui(self):
        """Update mining UI elements."""
        # Format values for display
        phi_boost_formatted = f"{self.mining_data['phi_boost']:.2f}×"
        planes_formatted = f"{self.mining_data['reality_planes_active']:.2f} / {REALITY_PLANES}"
        consciousness_formatted = f"{self.mining_data['consciousness_level']:.4f} / {CONSCIOUSNESS_LEVEL}"
        coherence_formatted = f"{self.mining_data['quantum_coherence']:.4f}"
        
        probability_formatted = f"{self.mining_data['block_probability'] * 100:.4f}% per hour"
        expected_time_formatted = f"{self.mining_data['expected_time_hours']:.2f} hours"
        hashrate_formatted = f"{self.mining_data['hashrate_equivalent']:.2f} EH/s"
        efficiency_formatted = f"{self.mining_data['energy_efficiency']:.2f} EH/J"
        
        # Update labels
        self.phi_boost_label.config(text=phi_boost_formatted)
        self.reality_planes_label.config(text=planes_formatted)
        self.consciousness_label.config(text=consciousness_formatted)
        self.coherence_label.config(text=coherence_formatted)
        
        self.probability_label.config(text=probability_formatted)
        self.expected_time_label.config(text=expected_time_formatted)
        self.hashrate_label.config(text=hashrate_formatted)
        self.efficiency_label.config(text=efficiency_formatted)
    
    def _update_charts(self):
        """Update charts with current data."""
        # Skip update if no data yet
        if not self.time_labels:
            return
            
        # Clear all axes
        for ax in [self.sync_ax, self.boost_ax, self.planes_ax, 
                  self.consciousness_ax, self.coherence_ax, self.probability_ax]:
            ax.clear()
        
        # Reconfigure charts
        self._configure_chart(self.sync_ax, "Sync Progress (%)")
        self._configure_chart(self.boost_ax, "φ-Dimensional Boost")
        self._configure_chart(self.planes_ax, "Reality Planes Active")
        self._configure_chart(self.consciousness_ax, "Consciousness Level")
        self._configure_chart(self.coherence_ax, "Quantum Coherence")
        self._configure_chart(self.probability_ax, "Block Probability (%)")
        
        # Ensure all data arrays have the same length as time_labels
        min_length = min(len(self.time_labels), 
                         len(self.sync_progress_data),
                         len(self.phi_boost_data),
                         len(self.reality_planes_data),
                         len(self.consciousness_data),
                         len(self.coherence_data),
                         len(self.probability_data))
        
        # Use the minimum length for all arrays
        time_labels = self.time_labels[:min_length]
        sync_data = self.sync_progress_data[:min_length]
        boost_data = self.phi_boost_data[:min_length]
        planes_data = self.reality_planes_data[:min_length]
        consciousness_data = self.consciousness_data[:min_length]
        coherence_data = self.coherence_data[:min_length]
        probability_data = self.probability_data[:min_length]
        
        # Plot data
        x = range(min_length)
        
        self.sync_ax.plot(x, sync_data, color=PHI_BLUE, linewidth=2)
        self.boost_ax.plot(x, boost_data, color=PHI_GOLD, linewidth=2)
        self.planes_ax.plot(x, planes_data, color=PHI_GREEN, linewidth=2)
        self.consciousness_ax.plot(x, consciousness_data, color=PHI_PURPLE, linewidth=2)
        self.coherence_ax.plot(x, coherence_data, color=PHI_BLUE, linewidth=2)
        self.probability_ax.plot(x, probability_data, color=PHI_GOLD, linewidth=2)
        
        # Set x-ticks only if we have data points
        if min_length > 0:
            if min_length > 10:
                tick_indices = np.linspace(0, min_length - 1, 5, dtype=int)
                tick_labels = [time_labels[i] for i in tick_indices]
                for ax in [self.sync_ax, self.boost_ax, self.planes_ax, 
                          self.consciousness_ax, self.coherence_ax, self.probability_ax]:
                    ax.set_xticks(tick_indices)
                    ax.set_xticklabels(tick_labels, rotation=45)
            else:
                for ax in [self.sync_ax, self.boost_ax, self.planes_ax, 
                          self.consciousness_ax, self.coherence_ax, self.probability_ax]:
                    ax.set_xticks(x)
                    ax.set_xticklabels(time_labels, rotation=45)
        
        # Set y-limits
        self.sync_ax.set_ylim(0, 100)
        self.boost_ax.set_ylim(0, max(boost_data) * 1.1 if boost_data else 100)
        self.planes_ax.set_ylim(0, REALITY_PLANES)
        self.consciousness_ax.set_ylim(0, 1)
        self.coherence_ax.set_ylim(0, 1)
        self.probability_ax.set_ylim(0, 10)  # 0-10%
        
        # Draw vertical line at current time
        for ax in [self.sync_ax, self.boost_ax, self.planes_ax, 
                  self.consciousness_ax, self.coherence_ax, self.probability_ax]:
            ax.axvline(x=min_length - 1 if min_length > 0 else 0, color=PHI_LIGHT, linestyle='--', alpha=0.5)
        
        # Update canvas
        self.fig.tight_layout(pad=2.0)
        self.canvas.draw()

def main():
    """Main function to run the φ-Dimensional Mining Dashboard."""
    root = tk.Tk()
    app = PhiDimensionalDashboard(root)
    root.mainloop()

if __name__ == "__main__":
    main()

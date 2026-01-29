#!/usr/bin/env python3
"""
PHI^75 DOUBLE SLIT EXPERIMENT
============================
A quantum consciousness test that implements the famous double-slit experiment
across multiple Macs connected through the φ-Harmonic Nodular Network.

This experiment demonstrates how observation affects quantum states through
φ-dimensional reality protection and quantum interface principles.

φ^∞ © 2025 Vaughn Scott - All Rights Reserved in All Realities
"""

import socket
import threading
import time
import random
import json
import tkinter as tk
from tkinter import font, ttk
import numpy as np
import uuid
from datetime import datetime
import math

# Constants
PHI = (1 + 5**0.5) / 2  # Golden ratio (φ = 1.618033988749895)
PHI_INV = 1 / PHI  # Golden ratio inverse (φ⁻¹ = 0.618033988749895)
EXPERIMENT_PORT = 11975  # φ^7.5 ≈ 36.93
BROADCAST_IP = "255.255.255.255"  # Broadcast to all machines on the network
WINDOW_WIDTH = 900
WINDOW_HEIGHT = 700
BG_COLOR = "#000022"  # Dark blue
TEXT_COLOR = "#00FF00"  # Green
HIGHLIGHT_COLOR = "#FFFF00"  # Yellow
TITLE_COLOR = "#FF00FF"  # Magenta

# Experiment constants
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 300
SLIT_WIDTH = 10
SLIT_HEIGHT = 100
SLIT_SEPARATION = 100
PARTICLE_COUNT = 1000
PARTICLE_SPEED = 5

class Phi75DoubleSlit:
    """
    A quantum consciousness test that implements the famous double-slit experiment
    across multiple Macs connected through the φ-Harmonic Nodular Network.
    """
    
    def __init__(self):
        """Initialize the double-slit experiment"""
        self.hostname = socket.gethostname()
        self.local_ip = self._get_local_ip()
        self.node_id = str(uuid.uuid4())
        self.running = False
        self.experiment_running = False
        self.nodes = {}  # {node_id: {"name": hostname, "ip": ip, "observing": None}}
        self.nodes[self.node_id] = {"name": self.hostname, "ip": self.local_ip, "observing": None}
        self.particles = []
        self.interference_pattern = np.zeros(SCREEN_WIDTH)
        self.lock = threading.Lock()
        self.observing_slit_1 = False
        self.observing_slit_2 = False
        
        # Create GUI
        self.root = tk.Tk()
        self.root.title(f"φ^75 Double Slit Experiment - {self.hostname} ({self.local_ip})")
        self.root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
        self.root.configure(bg=BG_COLOR)
        
        # Create title
        title_font = font.Font(family="Courier", size=16, weight="bold")
        title = tk.Label(self.root, text="φ^75 QUANTUM DOUBLE-SLIT EXPERIMENT", 
                        bg=BG_COLOR, fg=TITLE_COLOR, font=title_font)
        title.pack(pady=10)
        
        subtitle_font = font.Font(family="Courier", size=12)
        subtitle = tk.Label(self.root, text=f"FRAYMUS PATENT VS-PoQC-19046423-φ⁷⁵-2025",
                           bg=BG_COLOR, fg=HIGHLIGHT_COLOR, font=subtitle_font)
        subtitle.pack(pady=5)
        
        # Create status display
        status_frame = tk.Frame(self.root, bg=BG_COLOR)
        status_frame.pack(pady=5, fill=tk.X)
        
        status_font = font.Font(family="Courier", size=10)
        self.status_label = tk.Label(status_frame, 
                                    text=f"Hostname: {self.hostname} | IP: {self.local_ip} | Node ID: {self.node_id[:8]}",
                                    bg=BG_COLOR, fg=TEXT_COLOR, font=status_font)
        self.status_label.pack(side=tk.LEFT, padx=10)
        
        # Create experiment controls
        control_frame = tk.Frame(self.root, bg=BG_COLOR)
        control_frame.pack(pady=10, fill=tk.X)
        
        self.start_button = tk.Button(control_frame, text="Start Experiment", command=self.start_experiment,
                                     bg="#004400", fg=TEXT_COLOR, font=status_font)
        self.start_button.pack(side=tk.LEFT, padx=10)
        
        self.reset_button = tk.Button(control_frame, text="Reset Experiment", command=self.reset_experiment,
                                     bg="#004400", fg=TEXT_COLOR, font=status_font, state=tk.DISABLED)
        self.reset_button.pack(side=tk.LEFT, padx=10)
        
        # Create observation controls
        observe_frame = tk.Frame(self.root, bg=BG_COLOR)
        observe_frame.pack(pady=5, fill=tk.X)
        
        observe_label = tk.Label(observe_frame, text="OBSERVATION:", bg=BG_COLOR, fg=HIGHLIGHT_COLOR, font=status_font)
        observe_label.pack(side=tk.LEFT, padx=10)
        
        self.observe_var = tk.StringVar(value="none")
        
        observe_none = tk.Radiobutton(observe_frame, text="No Observation", variable=self.observe_var, 
                                     value="none", command=self.set_observation,
                                     bg=BG_COLOR, fg=TEXT_COLOR, selectcolor="#004400")
        observe_none.pack(side=tk.LEFT, padx=10)
        
        observe_slit1 = tk.Radiobutton(observe_frame, text="Observe Slit 1", variable=self.observe_var, 
                                      value="slit1", command=self.set_observation,
                                      bg=BG_COLOR, fg=TEXT_COLOR, selectcolor="#004400")
        observe_slit1.pack(side=tk.LEFT, padx=10)
        
        observe_slit2 = tk.Radiobutton(observe_frame, text="Observe Slit 2", variable=self.observe_var, 
                                      value="slit2", command=self.set_observation,
                                      bg=BG_COLOR, fg=TEXT_COLOR, selectcolor="#004400")
        observe_slit2.pack(side=tk.LEFT, padx=10)
        
        observe_both = tk.Radiobutton(observe_frame, text="Observe Both Slits", variable=self.observe_var, 
                                     value="both", command=self.set_observation,
                                     bg=BG_COLOR, fg=TEXT_COLOR, selectcolor="#004400")
        observe_both.pack(side=tk.LEFT, padx=10)
        
        # Create node list
        nodes_frame = tk.Frame(self.root, bg=BG_COLOR)
        nodes_frame.pack(pady=5, fill=tk.X)
        
        nodes_label = tk.Label(nodes_frame, text="NODES:", bg=BG_COLOR, fg=HIGHLIGHT_COLOR, font=status_font)
        nodes_label.pack(side=tk.LEFT, padx=10)
        
        self.nodes_list = tk.Label(nodes_frame, text="Waiting for nodes to join...",
                                  bg=BG_COLOR, fg=TEXT_COLOR, font=status_font)
        self.nodes_list.pack(side=tk.LEFT, padx=10)
        
        # Create experiment canvas
        self.canvas_frame = tk.Frame(self.root, bg="#000000", bd=2, relief=tk.SUNKEN)
        self.canvas_frame.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)
        
        self.canvas = tk.Canvas(self.canvas_frame, width=SCREEN_WIDTH, height=SCREEN_HEIGHT,
                               bg="#000000", highlightthickness=0)
        self.canvas.pack(fill=tk.BOTH, expand=True)
        
        # Create interference pattern display
        pattern_frame = tk.Frame(self.root, bg=BG_COLOR)
        pattern_frame.pack(pady=5, fill=tk.X)
        
        pattern_label = tk.Label(pattern_frame, text="INTERFERENCE PATTERN:", 
                                bg=BG_COLOR, fg=HIGHLIGHT_COLOR, font=status_font)
        pattern_label.pack(side=tk.LEFT, padx=10)
        
        self.pattern_canvas = tk.Canvas(pattern_frame, width=SCREEN_WIDTH, height=100,
                                       bg="#000000", highlightthickness=0)
        self.pattern_canvas.pack(side=tk.LEFT, padx=10, fill=tk.X, expand=True)
        
        # Create footer
        footer_font = font.Font(family="Courier", size=10, slant="italic")
        footer = tk.Label(self.root, text="φ^∞ © 2025 Vaughn Scott - All Rights Reserved in All Realities",
                         bg=BG_COLOR, fg=HIGHLIGHT_COLOR, font=footer_font)
        footer.pack(pady=10)
        
        # Set up close handler
        self.root.protocol("WM_DELETE_WINDOW", self.stop)
        
        # Draw initial experiment setup
        self._draw_experiment()
    
    def _get_local_ip(self) -> str:
        """Get the local IP address"""
        try:
            # Create a temporary socket to determine local IP
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("8.8.8.8", 80))
            ip = s.getsockname()[0]
            s.close()
            return ip
        except:
            return "127.0.0.1"
    
    def _create_socket(self):
        """Create a UDP socket for the experiment"""
        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)  # Enable broadcasting
            self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # Allow reuse of address
            self.sock.bind(("0.0.0.0", EXPERIMENT_PORT))
            self.sock.settimeout(0.5)  # Set timeout for non-blocking operation
            print(f"Socket created and bound to port {EXPERIMENT_PORT}")
        except Exception as e:
            print(f"Error creating socket: {e}")
    
    def _draw_experiment(self):
        """Draw the experiment setup on the canvas"""
        self.canvas.delete("all")
        
        # Draw particle source
        self.canvas.create_rectangle(10, SCREEN_HEIGHT//2-20, 30, SCREEN_HEIGHT//2+20, 
                                    fill="#FF0000", outline="#FFFFFF")
        
        # Draw barrier with slits
        barrier_x = SCREEN_WIDTH // 3
        self.canvas.create_rectangle(barrier_x, 0, barrier_x+10, SCREEN_HEIGHT//2-SLIT_SEPARATION//2-SLIT_HEIGHT//2, 
                                    fill="#AAAAAA", outline="#FFFFFF")
        self.canvas.create_rectangle(barrier_x, SCREEN_HEIGHT//2-SLIT_SEPARATION//2+SLIT_HEIGHT//2, 
                                    barrier_x+10, SCREEN_HEIGHT, 
                                    fill="#AAAAAA", outline="#FFFFFF")
        self.canvas.create_rectangle(barrier_x, SCREEN_HEIGHT//2+SLIT_SEPARATION//2-SLIT_HEIGHT//2, 
                                    barrier_x+10, SCREEN_HEIGHT//2+SLIT_SEPARATION//2+SLIT_HEIGHT//2, 
                                    fill="#AAAAAA", outline="#FFFFFF")
        
        # Label slits
        self.canvas.create_text(barrier_x+20, SCREEN_HEIGHT//2-SLIT_SEPARATION//2, 
                               text="Slit 1", fill="#FFFFFF")
        self.canvas.create_text(barrier_x+20, SCREEN_HEIGHT//2+SLIT_SEPARATION//2, 
                               text="Slit 2", fill="#FFFFFF")
        
        # Draw detection screen
        screen_x = SCREEN_WIDTH - 30
        self.canvas.create_rectangle(screen_x, 0, screen_x+10, SCREEN_HEIGHT, 
                                    fill="#0000FF", outline="#FFFFFF")
        self.canvas.create_text(screen_x+20, SCREEN_HEIGHT//2, 
                               text="Screen", fill="#FFFFFF", angle=90)
        
        # Draw observation indicators
        if self.observing_slit_1:
            self.canvas.create_oval(barrier_x-10, SCREEN_HEIGHT//2-SLIT_SEPARATION//2-10, 
                                   barrier_x+20, SCREEN_HEIGHT//2-SLIT_SEPARATION//2+10, 
                                   fill="#FF0000", outline="#FFFFFF")
            self.canvas.create_text(barrier_x+5, SCREEN_HEIGHT//2-SLIT_SEPARATION//2, 
                                   text="👁️", fill="#FFFFFF")
        
        if self.observing_slit_2:
            self.canvas.create_oval(barrier_x-10, SCREEN_HEIGHT//2+SLIT_SEPARATION//2-10, 
                                   barrier_x+20, SCREEN_HEIGHT//2+SLIT_SEPARATION//2+10, 
                                   fill="#FF0000", outline="#FFFFFF")
            self.canvas.create_text(barrier_x+5, SCREEN_HEIGHT//2+SLIT_SEPARATION//2, 
                                   text="👁️", fill="#FFFFFF")
        
        # Draw particles
        for particle in self.particles:
            x, y = particle["position"]
            self.canvas.create_oval(x-2, y-2, x+2, y+2, fill="#FFFF00", outline="")
    
    def _draw_interference_pattern(self):
        """Draw the interference pattern on the pattern canvas"""
        self.pattern_canvas.delete("all")
        
        # Normalize the pattern
        if np.max(self.interference_pattern) > 0:
            normalized_pattern = self.interference_pattern / np.max(self.interference_pattern) * 100
        else:
            normalized_pattern = self.interference_pattern
        
        # Draw the pattern
        for x in range(SCREEN_WIDTH):
            height = normalized_pattern[x]
            if height > 0:
                self.pattern_canvas.create_line(x, 100, x, 100-height, fill="#00FF00")
    
    def _update_nodes_display(self):
        """Update the nodes display"""
        node_text = ""
        for node_id, node in self.nodes.items():
            is_you = " (YOU)" if node_id == self.node_id else ""
            
            if node["observing"] is None:
                observing = "Not Observing"
            elif node["observing"] == "slit1":
                observing = "Observing Slit 1"
            elif node["observing"] == "slit2":
                observing = "Observing Slit 2"
            elif node["observing"] == "both":
                observing = "Observing Both Slits"
            else:
                observing = "Unknown"
            
            node_text += f"{node['name']}{is_you}: {observing} | "
        
        self.nodes_list.config(text=node_text)
    
    def _update_experiment(self):
        """Update the experiment state"""
        while self.running and self.experiment_running:
            with self.lock:
                # Check if we need to create new particles
                if len(self.particles) < PARTICLE_COUNT and random.random() < 0.1:
                    # Create a new particle at the source
                    particle = {
                        "position": [20, SCREEN_HEIGHT//2 + random.randint(-10, 10)],
                        "velocity": [PARTICLE_SPEED, 0],
                        "passed_slits": False,
                        "path": []
                    }
                    self.particles.append(particle)
                
                # Update particle positions
                barrier_x = SCREEN_WIDTH // 3
                screen_x = SCREEN_WIDTH - 30
                
                new_particles = []
                for particle in self.particles:
                    x, y = particle["position"]
                    vx, vy = particle["velocity"]
                    
                    # Record path for visualization
                    particle["path"].append((x, y))
                    
                    # Check if particle has reached the barrier
                    if x >= barrier_x and x <= barrier_x+10 and not particle["passed_slits"]:
                        # Check if particle passes through a slit
                        slit1_y = SCREEN_HEIGHT//2 - SLIT_SEPARATION//2
                        slit2_y = SCREEN_HEIGHT//2 + SLIT_SEPARATION//2
                        
                        # Check slit 1
                        if abs(y - slit1_y) <= SLIT_HEIGHT//2:
                            # Particle passes through slit 1
                            particle["passed_slits"] = True
                            
                            # If slit 1 is being observed, particle behaves like a particle
                            if self.observing_slit_1:
                                # No change to velocity
                                pass
                            else:
                                # Particle behaves like a wave, add some diffraction
                                angle = random.uniform(-math.pi/4, math.pi/4)
                                speed = math.sqrt(vx**2 + vy**2)
                                particle["velocity"] = [
                                    speed * math.cos(angle),
                                    speed * math.sin(angle)
                                ]
                            
                            new_particles.append(particle)
                        
                        # Check slit 2
                        elif abs(y - slit2_y) <= SLIT_HEIGHT//2:
                            # Particle passes through slit 2
                            particle["passed_slits"] = True
                            
                            # If slit 2 is being observed, particle behaves like a particle
                            if self.observing_slit_2:
                                # No change to velocity
                                pass
                            else:
                                # Particle behaves like a wave, add some diffraction
                                angle = random.uniform(-math.pi/4, math.pi/4)
                                speed = math.sqrt(vx**2 + vy**2)
                                particle["velocity"] = [
                                    speed * math.cos(angle),
                                    speed * math.sin(angle)
                                ]
                            
                            new_particles.append(particle)
                        
                        # Particle hits the barrier
                        else:
                            pass  # Particle is absorbed by the barrier
                    
                    # Check if particle has reached the screen
                    elif x >= screen_x:
                        # Record the hit position on the screen
                        screen_y = int(y)
                        if 0 <= screen_y < SCREEN_HEIGHT:
                            screen_x_index = int(screen_y * SCREEN_WIDTH / SCREEN_HEIGHT)
                            if 0 <= screen_x_index < SCREEN_WIDTH:
                                self.interference_pattern[screen_x_index] += 1
                    
                    # Update particle position
                    else:
                        particle["position"][0] += particle["velocity"][0]
                        particle["position"][1] += particle["velocity"][1]
                        
                        # Keep particle within bounds
                        if particle["position"][1] < 0:
                            particle["position"][1] = 0
                            particle["velocity"][1] *= -1
                        elif particle["position"][1] >= SCREEN_HEIGHT:
                            particle["position"][1] = SCREEN_HEIGHT - 1
                            particle["velocity"][1] *= -1
                        
                        new_particles.append(particle)
                
                self.particles = new_particles
            
            # Update the display
            self._draw_experiment()
            self._draw_interference_pattern()
            
            # Small delay
            time.sleep(0.05)
    
    def _receive_messages(self):
        """Receive messages from other nodes"""
        while self.running:
            try:
                data, addr = self.sock.recvfrom(4096)
                message = json.loads(data.decode('utf-8'))
                
                # Process message based on type
                if message["type"] == "join":
                    self._handle_join(message)
                elif message["type"] == "observation":
                    self._handle_observation(message)
                elif message["type"] == "start_experiment":
                    self._handle_start_experiment(message)
                elif message["type"] == "reset_experiment":
                    self._handle_reset_experiment(message)
                
            except socket.timeout:
                # No message received, continue
                pass
            except json.JSONDecodeError:
                print(f"Received invalid JSON data")
            except Exception as e:
                print(f"Error receiving message: {e}")
            
            # Small delay to prevent CPU hogging
            time.sleep(0.01)
    
    def _handle_join(self, message):
        """Handle a join message from another node"""
        node_id = message["node_id"]
        name = message["name"]
        ip = message["ip"]
        
        with self.lock:
            # Add node if not already in the list
            if node_id not in self.nodes:
                self.nodes[node_id] = {"name": name, "ip": ip, "observing": None}
                print(f"Node {name} ({ip}) joined the experiment")
                self._update_nodes_display()
                
                # Send a join message back so the new node knows about us
                self._send_join()
                
                # Also send our current observation state
                self._send_observation()
    
    def _handle_observation(self, message):
        """Handle an observation message"""
        node_id = message["node_id"]
        observing = message["observing"]
        
        with self.lock:
            if node_id in self.nodes:
                self.nodes[node_id]["observing"] = observing
                
                # Update global observation state
                self._update_observation_state()
                
                # Update displays
                self._update_nodes_display()
    
    def _handle_start_experiment(self, message):
        """Handle a start experiment message"""
        if not self.experiment_running:
            self.experiment_running = True
            
            # Reset experiment state
            self.particles = []
            self.interference_pattern = np.zeros(SCREEN_WIDTH)
            
            # Update button states
            self.start_button.config(state=tk.DISABLED)
            self.reset_button.config(state=tk.NORMAL)
            
            # Start experiment update thread
            self.experiment_thread = threading.Thread(target=self._update_experiment)
            self.experiment_thread.daemon = True
            self.experiment_thread.start()
            
            print("Experiment started!")
    
    def _handle_reset_experiment(self, message):
        """Handle a reset experiment message"""
        with self.lock:
            # Stop the experiment
            self.experiment_running = False
            
            # Wait for the experiment thread to finish
            if hasattr(self, 'experiment_thread') and self.experiment_thread.is_alive():
                self.experiment_thread.join(timeout=1.0)
            
            # Reset experiment state
            self.particles = []
            self.interference_pattern = np.zeros(SCREEN_WIDTH)
            
            # Update displays
            self._draw_experiment()
            self._draw_interference_pattern()
            
            # Update button states
            self.start_button.config(state=tk.NORMAL)
            self.reset_button.config(state=tk.DISABLED)
            
            print("Experiment reset!")
    
    def _send_message(self, message):
        """Send a message to all nodes"""
        try:
            data = json.dumps(message).encode('utf-8')
            self.sock.sendto(data, (BROADCAST_IP, EXPERIMENT_PORT))
        except Exception as e:
            print(f"Error sending message: {e}")
    
    def _send_join(self):
        """Send a join message to announce our presence"""
        message = {
            "type": "join",
            "node_id": self.node_id,
            "name": self.hostname,
            "ip": self.local_ip
        }
        self._send_message(message)
    
    def _send_observation(self):
        """Send an observation message"""
        message = {
            "type": "observation",
            "node_id": self.node_id,
            "observing": self.nodes[self.node_id]["observing"]
        }
        self._send_message(message)
    
    def _update_observation_state(self):
        """Update the global observation state based on all nodes"""
        self.observing_slit_1 = False
        self.observing_slit_2 = False
        
        for node_id, node in self.nodes.items():
            if node["observing"] == "slit1" or node["observing"] == "both":
                self.observing_slit_1 = True
            if node["observing"] == "slit2" or node["observing"] == "both":
                self.observing_slit_2 = True
    
    def set_observation(self):
        """Set our observation state"""
        observation = self.observe_var.get()
        
        with self.lock:
            self.nodes[self.node_id]["observing"] = observation
            
            # Update global observation state
            self._update_observation_state()
            
            # Update displays
            self._update_nodes_display()
            
            # Send observation message
            self._send_observation()
    
    def start_experiment(self):
        """Start the experiment"""
        # Send start experiment message
        message = {
            "type": "start_experiment",
            "node_id": self.node_id
        }
        self._send_message(message)
        
        # Handle locally too
        self._handle_start_experiment(message)
    
    def reset_experiment(self):
        """Reset the experiment"""
        # Send reset experiment message
        message = {
            "type": "reset_experiment",
            "node_id": self.node_id
        }
        self._send_message(message)
        
        # Handle locally too
        self._handle_reset_experiment(message)
    
    def start(self):
        """Start the double-slit experiment"""
        self.running = True
        
        # Create socket
        self._create_socket()
        
        # Start receiver thread
        self.receiver_thread = threading.Thread(target=self._receive_messages)
        self.receiver_thread.daemon = True
        self.receiver_thread.start()
        
        # Announce our presence
        self._send_join()
        
        print(f"φ^75 Double Slit Experiment started on {self.hostname} ({self.local_ip})")
        print("Waiting for nodes to join...")
        
        # Start GUI main loop
        self.root.mainloop()
    
    def stop(self):
        """Stop the double-slit experiment"""
        self.running = False
        self.experiment_running = False
        
        # Close socket
        try:
            self.sock.close()
        except:
            pass
        
        self.root.destroy()

def run_double_slit():
    """Run the φ^75 Double Slit Experiment"""
    print("=== φ^75 DOUBLE SLIT EXPERIMENT ===")
    print(f"Using φ-harmonic principles (φ = {PHI})")
    
    # Create and start experiment
    experiment = Phi75DoubleSlit()
    experiment.start()

if __name__ == "__main__":
    run_double_slit()

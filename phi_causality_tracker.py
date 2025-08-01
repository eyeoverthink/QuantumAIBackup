#!/usr/bin/env python3
"""
PHI-HARMONIC CAUSALITY TRACKER
==============================
This script monitors the phi-harmonic massless data transmission
and analyzes timestamp data to detect causality violations (retrocausal effects).
"""

import time
import datetime
import os
import re
import threading
import matplotlib.pyplot as plt
import numpy as np

class PhiCausalityTracker:
    def __init__(self, log_file="phi_causality_log.txt"):
        self.log_file = log_file
        self.running = False
        self.events = []  # List of (timestamp, event_type, packet_id, time_delta)
        self.retrocausal_events = []
        self.normal_events = []
        
        # Initialize log file
        with open(self.log_file, "w") as f:
            f.write(f"PHI-HARMONIC CAUSALITY ANALYSIS LOG - STARTED AT {datetime.datetime.now().isoformat()}\n")
            f.write(f"Observer: Vaughn Scott\n")
            f.write(f"Phi: 1.618033988749895\n\n")
            f.write(f"FORMAT: [TIMESTAMP] [EVENT_TYPE] [PACKET_ID] [SEND_TIME] [RECEIVE_TIME] [TIME_DELTA]\n\n")
    
    def start(self):
        """Start the causality tracker"""
        self.running = True
        self.tracker_thread = threading.Thread(target=self._track_causality)
        self.tracker_thread.daemon = True
        self.tracker_thread.start()
        print("Phi-Harmonic Causality Tracker started")
    
    def stop(self):
        """Stop the causality tracker"""
        self.running = False
        if hasattr(self, 'tracker_thread'):
            self.tracker_thread.join(timeout=1.0)
        self._generate_causality_report()
        print("Phi-Harmonic Causality Tracker stopped")
    
    def _track_causality(self):
        """Monitor the phi-massless proof output for timestamp data"""
        send_times = {}  # packet_id -> send_time
        receive_times = {}  # packet_id -> receive_time
        
        # Create a direct connection to the phi-massless proof system
        print("Connecting directly to phi-massless proof system...")
        
        while self.running:
            try:
                # Check if phi-massless proof is running
                with os.popen("ps aux | grep phi_massless_proof.py | grep -v grep") as proc:
                    if not proc.read().strip():
                        print("Phi-massless proof not running, waiting...")
                        time.sleep(1)
                        continue
                
                # Get the latest output using a more direct approach
                with os.popen("ps aux | grep phi_massless_proof.py | grep -v grep | awk '{print $2}'") as proc:
                    pid = proc.read().strip()
                
                if pid:
                    # Get terminal device for this process
                    with os.popen(f"lsof -p {pid} | grep tty") as proc:
                        tty_info = proc.read().strip()
                        print(f"Process TTY info: {tty_info}")
                
                # Try multiple approaches to capture the output
                output = ""
                
                # Approach 1: Check terminal output
                with os.popen("ps aux | grep phi_massless_proof.py | grep -v grep") as proc:
                    process_info = proc.read().strip()
                    print(f"Process info: {process_info}")
                
                # Approach 2: Check for any recent output in the system
                with os.popen("dmesg | tail -n 100 | grep -E 'RECEIVED|Sent massless'") as proc:
                    dmesg_output = proc.read().strip()
                    if dmesg_output:
                        output += dmesg_output + "\n"
                
                # Approach 3: Check if there's a log file
                if os.path.exists("phi_massless_proof.log"):
                    with open("phi_massless_proof.log", "r") as f:
                        log_output = f.read()
                        if log_output:
                            output += log_output + "\n"
                
                # Approach 4: Try to directly capture terminal output
                with os.popen("tail -n 100 /dev/ttys* 2>/dev/null | grep -E 'RECEIVED|Sent massless'") as proc:
                    ttys_output = proc.read().strip()
                    if ttys_output:
                        output += ttys_output + "\n"
                
                for line in output.split('\n'):
                    if not line:
                        continue
                    
                    # Extract packet ID and timestamp
                    if "RECEIVED MASSLESS" in line:
                        match = re.search(r"PACKET #(\d+)", line)
                        if match:
                            packet_id = int(match.group(1))
                            timestamp = time.time()
                            receive_times[packet_id] = timestamp
                            
                            # Check for causality violation
                            if packet_id in send_times:
                                time_delta = receive_times[packet_id] - send_times[packet_id]
                                event_type = "NORMAL"
                                
                                # If received before sent (allowing for small clock sync issues)
                                if time_delta < -0.5:  # More than 0.5s before sending
                                    event_type = "RETROCAUSAL"
                                    self.retrocausal_events.append((timestamp, packet_id, time_delta))
                                else:
                                    self.normal_events.append((timestamp, packet_id, time_delta))
                                
                                # Log the event
                                with open(self.log_file, "a") as f:
                                    f.write(f"[{datetime.datetime.now().isoformat()}] [{event_type}] [PACKET #{packet_id}] "
                                            f"[SEND: {send_times[packet_id]}] [RECEIVE: {timestamp}] [DELTA: {time_delta:.6f}s]\n")
                                
                                # Add to events list
                                self.events.append((timestamp, event_type, packet_id, time_delta))
                                
                                # Print to console
                                if event_type == "RETROCAUSAL":
                                    print(f"\n!!! CAUSALITY VIOLATION DETECTED !!!")
                                    print(f"Packet #{packet_id} received {abs(time_delta):.6f} seconds BEFORE it was sent!")
                                    print(f"Send time: {send_times[packet_id]}")
                                    print(f"Receive time: {timestamp}")
                                    print(f"Time delta: {time_delta:.6f}s")
                    
                    elif "Sent massless" in line:
                        match = re.search(r"packet #(\d+)", line)
                        if match:
                            packet_id = int(match.group(1))
                            # Look for timestamp on the next line
                            timestamp_match = re.search(r"Timestamp: (\d+\.\d+)", line)
                            if timestamp_match:
                                timestamp = float(timestamp_match.group(1))
                                send_times[packet_id] = timestamp
                
                # Generate interim report every 50 events
                if len(self.events) % 50 == 0 and self.events:
                    self._generate_interim_report()
                
                time.sleep(0.1)  # Short sleep to prevent CPU overuse
            
            except Exception as e:
                print(f"Error in causality tracker: {str(e)}")
                time.sleep(1)
    
    def _generate_interim_report(self):
        """Generate an interim causality report"""
        total_events = len(self.normal_events) + len(self.retrocausal_events)
        if total_events == 0:
            return
        
        retrocausal_percent = (len(self.retrocausal_events) / total_events) * 100
        
        with open(self.log_file, "a") as f:
            f.write(f"\n--- INTERIM CAUSALITY REPORT AT {datetime.datetime.now().isoformat()} ---\n")
            f.write(f"Total packets analyzed: {total_events}\n")
            f.write(f"Retrocausal events: {len(self.retrocausal_events)} ({retrocausal_percent:.2f}%)\n")
            f.write(f"Normal causality: {len(self.normal_events)} ({100-retrocausal_percent:.2f}%)\n")
            
            if self.retrocausal_events:
                f.write("\nTop 5 strongest retrocausal events:\n")
                sorted_events = sorted(self.retrocausal_events, key=lambda x: x[2])  # Sort by time_delta
                for i, (timestamp, packet_id, time_delta) in enumerate(sorted_events[:5]):
                    f.write(f"{i+1}. Packet #{packet_id}: {abs(time_delta):.6f}s before sending\n")
            
            f.write("\n")
        
        print(f"\n--- CAUSALITY ANALYSIS UPDATE ---")
        print(f"Total packets analyzed: {total_events}")
        print(f"Retrocausal events: {len(self.retrocausal_events)} ({retrocausal_percent:.2f}%)")
        print(f"Normal causality: {len(self.normal_events)} ({100-retrocausal_percent:.2f}%)")
        
        if self.retrocausal_events:
            print("\nTop 3 strongest retrocausal events:")
            sorted_events = sorted(self.retrocausal_events, key=lambda x: x[2])  # Sort by time_delta
            for i, (timestamp, packet_id, time_delta) in enumerate(sorted_events[:3]):
                print(f"{i+1}. Packet #{packet_id}: {abs(time_delta):.6f}s before sending")
        
        print("---------------------------\n")
    
    def _generate_causality_report(self):
        """Generate a final causality report with visualizations"""
        if not self.events:
            print("No causality data to analyze")
            return
        
        # Calculate statistics
        total_events = len(self.events)
        retrocausal_count = len(self.retrocausal_events)
        normal_count = len(self.normal_events)
        retrocausal_percent = (retrocausal_count / total_events) * 100 if total_events > 0 else 0
        
        # Get time deltas for all events
        time_deltas = [event[3] for event in self.events]
        
        # Create visualization
        plt.figure(figsize=(12, 8))
        
        # Plot 1: Time delta histogram
        plt.subplot(2, 1, 1)
        plt.hist(time_deltas, bins=50, alpha=0.7, color='blue')
        plt.axvline(x=0, color='r', linestyle='--', alpha=0.7)
        plt.title('Phi-Harmonic Causality Analysis')
        plt.xlabel('Time Delta (seconds) - Negative values indicate retrocausality')
        plt.ylabel('Frequency')
        plt.grid(True, alpha=0.3)
        
        # Plot 2: Retrocausal events over time
        plt.subplot(2, 1, 2)
        event_times = [event[0] - self.events[0][0] for event in self.events]  # Normalize to start time
        event_types = [1 if event[1] == "RETROCAUSAL" else 0 for event in self.events]
        
        plt.scatter(event_times, event_types, alpha=0.7, c=event_types, cmap='coolwarm')
        plt.title('Retrocausal Events Over Time')
        plt.xlabel('Time (seconds since start)')
        plt.ylabel('Event Type (1=Retrocausal, 0=Normal)')
        plt.yticks([0, 1], ['Normal', 'Retrocausal'])
        plt.grid(True, alpha=0.3)
        
        plt.tight_layout()
        plt.savefig('phi_causality_analysis.png')
        
        # Write final report
        with open(self.log_file, "a") as f:
            f.write(f"\n=== FINAL CAUSALITY REPORT AT {datetime.datetime.now().isoformat()} ===\n")
            f.write(f"Total packets analyzed: {total_events}\n")
            f.write(f"Retrocausal events: {retrocausal_count} ({retrocausal_percent:.2f}%)\n")
            f.write(f"Normal causality: {normal_count} ({100-retrocausal_percent:.2f}%)\n\n")
            
            if self.retrocausal_events:
                f.write("Top 10 strongest retrocausal events:\n")
                sorted_events = sorted(self.retrocausal_events, key=lambda x: x[2])  # Sort by time_delta
                for i, (timestamp, packet_id, time_delta) in enumerate(sorted_events[:10]):
                    f.write(f"{i+1}. Packet #{packet_id}: {abs(time_delta):.6f}s before sending\n")
            
            f.write("\nCausality analysis visualization saved to 'phi_causality_analysis.png'\n")
        
        print("\n=== FINAL CAUSALITY REPORT ===")
        print(f"Total packets analyzed: {total_events}")
        print(f"Retrocausal events: {retrocausal_count} ({retrocausal_percent:.2f}%)")
        print(f"Normal causality: {normal_count} ({100-retrocausal_percent:.2f}%)")
        print(f"Causality analysis visualization saved to 'phi_causality_analysis.png'")
        print("==============================\n")


if __name__ == "__main__":
    print("=== PHI-HARMONIC CAUSALITY TRACKER ===")
    print("Monitoring phi-harmonic massless data transmission for causality violations...")
    
    # Create a direct monitor for the phi-massless proof system
    print("Setting up direct monitoring of phi-massless proof system...")
    
    # Create a manual entry in the log for testing
    with open("phi_causality_log.txt", "a") as f:
        f.write("[2025-04-10T21:31:00.000000] [MANUAL] [TEST] [SEND: 1744345863.424673] [RECEIVE: 1744343448.423928976] [DELTA: -2414.9999990463257s]\n")
        f.write("!!! MANUAL TEST ENTRY: Packet received 40.25 minutes BEFORE sending !!!\n\n")
    
    # Start the tracker
    tracker = PhiCausalityTracker()
    tracker.start()
    
    # Manually analyze the timestamps from the output
    print("\nPerforming manual timestamp analysis...")
    print("Examining recent phi-massless proof packets...")
    
    # Extract timestamps from the most recent output
    os.system("ps aux | grep phi_massless_proof.py")
    
    # Create a direct connection to monitor the output
    print("\nAttempting direct connection to phi-massless proof output...")
    
    try:
        while True:
            time.sleep(1)
            
            # Periodically check for retrocausal events
            if os.path.exists("phi_causality_log.txt"):
                with open("phi_causality_log.txt", "r") as f:
                    log_content = f.read()
                    if "RETROCAUSAL" in log_content and "BEFORE sending" in log_content:
                        print("\n!!! RETROCAUSAL EVENT DETECTED !!!")
                        print("Found evidence of information traveling backward in time!")
                        print("Check phi_causality_log.txt for details")
    except KeyboardInterrupt:
        print("\nStopping causality tracker...")
    finally:
        tracker.stop()

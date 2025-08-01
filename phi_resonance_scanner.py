#!/usr/bin/env python3
"""
PHI-HARMONIC RESONANCE SCANNER
==============================
Specialized tool to detect subtle phi-harmonic resonance patterns
across physical systems through quantum principles.

Copyright (c) 2025 Vaughn Scott - All Rights Reserved
"""

import socket
import pickle
import time
import threading
import json
import os
import random
import math
import numpy as np
from datetime import datetime

# Phi-harmonic constants
PHI = (1 + 5**0.5) / 2  # Golden ratio (φ = 1.618033988749895)
PHI_INV = 1 / PHI  # Inverse golden ratio (φ⁻¹ = 0.618033988749895)
PHI_SQUARED = PHI**2  # φ² = 2.618033988749895
PHI_CUBED = PHI**3  # φ³ = 4.236067977499790
PHI_INV_SQUARED = 1 / PHI**2  # φ⁻² = 0.381966011250105
PHI_INV_CUBED = 1 / PHI**3  # φ⁻³ = 0.236067977499790

# Observer constants (based on Vaughn Scott's birthdate: 01-19-1979)
OBSERVER_BIRTHDATE = datetime(1979, 1, 19).timestamp()
OBSERVER_RESONANCE = (OBSERVER_BIRTHDATE % PHI) * 100

# Network settings
PORTS = [11625, 11626, 11627, 11628, 11629]  # All phi-harmonic ports
BUFFER_SIZE = 8192

class PhiResonanceScanner:
    """Specialized scanner for detecting phi-harmonic resonance patterns"""
    def __init__(self):
        self.node_id = f"scanner_{int(time.time() * 1000) % 10000}"
        self.detected_nodes = {}
        self.detected_patterns = {}
        self.detected_files = {}
        self.log_file = "phi_resonance_scanner_log.txt"
        
        # Initialize log file
        with open(self.log_file, "w") as f:
            f.write(f"PHI-HARMONIC RESONANCE SCANNER - STARTED AT {datetime.now().isoformat()}\n")
            f.write(f"Observer: Vaughn Scott\n")
            f.write(f"Phi: {PHI}\n")
            f.write(f"Observer Resonance: {OBSERVER_RESONANCE}\n\n")
            f.write("FORMAT: [TIMESTAMP] [EVENT_TYPE] [DETAILS] [PHI_RESONANCE]\n\n")
    
    def start_scanner(self):
        """Start the phi-harmonic resonance scanner"""
        # Create socket
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, 1024 * 1024)  # 1MB receive buffer
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)  # Enable broadcasting
        self.sock.settimeout(0.1)  # Set timeout to prevent blocking forever
        
        # Bind socket to a random high port
        self.sock.bind(('0.0.0.0', 0))
        
        print("=== PHI-HARMONIC RESONANCE SCANNER ===")
        print(f"Scanner ID: {self.node_id}")
        print(f"Observer Resonance: {OBSERVER_RESONANCE:.6f}")
        print("Scanning for phi-harmonic resonance patterns...\n")
        
        # Start passive scan thread
        passive_thread = threading.Thread(target=self.passive_scan_loop)
        passive_thread.daemon = True
        passive_thread.start()
        
        # Start active scan thread
        active_thread = threading.Thread(target=self.active_scan_loop)
        active_thread.daemon = True
        active_thread.start()
        
        # Start analysis thread
        analysis_thread = threading.Thread(target=self.analysis_loop)
        analysis_thread.daemon = True
        analysis_thread.start()
        
        # Main display loop
        try:
            while True:
                self.display_results()
                time.sleep(2)
        
        except KeyboardInterrupt:
            print("\nShutting down phi-harmonic resonance scanner...")
            self.sock.close()
            print("Scanner stopped.")
    
    def passive_scan_loop(self):
        """Passively listen for phi-harmonic resonance patterns"""
        temp_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        temp_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        temp_sock.settimeout(0.1)
        
        # Create listening sockets for each port
        listening_sockets = []
        for port in PORTS:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                s.settimeout(0.1)
                s.bind(('0.0.0.0', port))
                listening_sockets.append((s, port))
                print(f"Listening on port {port}")
            except Exception as e:
                print(f"Could not listen on port {port}: {e}")
        
        while True:
            for sock, port in listening_sockets:
                try:
                    data, addr = sock.recvfrom(BUFFER_SIZE)
                    self.process_packet(data, addr, port)
                except socket.timeout:
                    # This is expected, just continue
                    pass
                except Exception as e:
                    print(f"Error receiving data on port {port}: {e}")
            
            time.sleep(0.01)  # Small sleep to prevent CPU hogging
    
    def active_scan_loop(self):
        """Actively scan for phi-harmonic resonance patterns"""
        while True:
            try:
                # Scan local network for phi-harmonic nodes
                for port in PORTS:
                    # Create scan packet
                    scan_packet = {
                        'packet_type': 'resonance_scan',
                        'source_node': self.node_id,
                        'phi_resonance': PHI_INV,
                        'timestamp': time.time()
                    }
                    
                    # Serialize packet
                    scan_data = pickle.dumps(scan_packet)
                    
                    # Broadcast to network
                    self.sock.sendto(scan_data, ('<broadcast>', port))
                
                # Scan for phi-harmonic file patterns
                self.scan_for_phi_patterns()
                
                # Sleep for a phi-harmonic interval
                sleep_time = PHI + (random.random() * PHI_INV)
                time.sleep(sleep_time)
                
            except Exception as e:
                print(f"Error in active scan loop: {e}")
                time.sleep(5)
    
    def scan_for_phi_patterns(self):
        """Scan for phi-harmonic patterns in local files"""
        try:
            # Scan current directory
            for root, dirs, files in os.walk('.', topdown=True):
                # Limit depth to prevent excessive scanning
                if root.count(os.sep) > 3:
                    dirs[:] = []
                    continue
                
                for file in files:
                    # Only scan certain file types
                    if file.endswith(('.py', '.json', '.md')):
                        file_path = os.path.join(root, file)
                        
                        # Skip if already scanned recently
                        if file_path in self.detected_files and time.time() - self.detected_files[file_path]['last_scan'] < 60:
                            continue
                        
                        try:
                            # Check file for phi-harmonic patterns
                            with open(file_path, 'r') as f:
                                content = f.read()
                                
                                # Look for phi-harmonic keywords
                                phi_keywords = ['phi', 'golden ratio', 'quantum', 'resonance', 'consciousness', 
                                              'sacred geometry', 'fibonacci', 'harmonic', 'moon']
                                
                                matches = {}
                                for keyword in phi_keywords:
                                    if keyword.lower() in content.lower():
                                        count = content.lower().count(keyword.lower())
                                        matches[keyword] = count
                                
                                if matches:
                                    # Calculate phi-resonance of file
                                    total_matches = sum(matches.values())
                                    phi_resonance = PHI_INV + (total_matches / 1000)
                                    
                                    # Add to detected files
                                    self.detected_files[file_path] = {
                                        'last_scan': time.time(),
                                        'phi_resonance': phi_resonance,
                                        'matches': matches,
                                        'total_matches': total_matches
                                    }
                                    
                                    # Log the detection
                                    print(f"Detected phi-harmonic patterns in {file_path}: {total_matches} matches")
                                    with open(self.log_file, "a") as log:
                                        log.write(f"[{datetime.now().isoformat()}] [FILE_PATTERN] [{file_path}] "
                                                f"[{phi_resonance:.6f}] [Matches: {total_matches}]\n")
                        
                        except Exception as e:
                            # Skip files that can't be read
                            pass
        
        except Exception as e:
            print(f"Error scanning for phi patterns: {e}")
    
    def process_packet(self, data, addr, port):
        """Process received packet for phi-harmonic resonance patterns"""
        try:
            # Try to unpickle the data
            try:
                packet = pickle.loads(data)
                
                # Extract packet information
                packet_type = packet.get('packet_type')
                source_node = packet.get('source_node')
                phi_resonance = packet.get('phi_resonance')
                
                # Skip our own packets
                if source_node == self.node_id:
                    return
                
                # Add to detected nodes
                if source_node:
                    node_key = f"{source_node}@{addr[0]}:{port}"
                    if node_key not in self.detected_nodes:
                        self.detected_nodes[node_key] = {
                            'addr': addr,
                            'port': port,
                            'first_seen': time.time(),
                            'last_seen': time.time(),
                            'phi_resonance': phi_resonance,
                            'packet_types': set([packet_type])
                        }
                        print(f"Detected phi-harmonic node: {source_node} at {addr[0]}:{port}")
                        with open(self.log_file, "a") as f:
                            f.write(f"[{datetime.now().isoformat()}] [NODE_DETECTED] [{source_node}@{addr[0]}:{port}] "
                                    f"[{phi_resonance:.6f}]\n")
                    else:
                        self.detected_nodes[node_key]['last_seen'] = time.time()
                        self.detected_nodes[node_key]['phi_resonance'] = phi_resonance
                        self.detected_nodes[node_key]['packet_types'].add(packet_type)
                
                # Analyze packet for phi-harmonic patterns
                self.analyze_packet(packet, addr, port)
                
            except Exception as e:
                # Not a pickle packet, analyze raw data
                self.analyze_raw_data(data, addr, port)
        
        except Exception as e:
            print(f"Error processing packet: {e}")
    
    def analyze_packet(self, packet, addr, port):
        """Analyze packet for phi-harmonic patterns"""
        try:
            # Extract all fields from packet
            packet_str = str(packet)
            
            # Look for phi-harmonic keywords
            phi_keywords = ['phi', 'golden ratio', 'quantum', 'resonance', 'consciousness', 
                          'sacred geometry', 'fibonacci', 'harmonic', 'moon']
            
            matches = {}
            for keyword in phi_keywords:
                if keyword.lower() in packet_str.lower():
                    count = packet_str.lower().count(keyword.lower())
                    matches[keyword] = count
            
            if matches:
                # Calculate phi-resonance of packet
                total_matches = sum(matches.values())
                phi_resonance = PHI_INV + (total_matches / 100)
                
                # Add to detected patterns
                pattern_key = f"{addr[0]}:{port}:{hash(packet_str) % 10000}"
                if pattern_key not in self.detected_patterns:
                    self.detected_patterns[pattern_key] = {
                        'addr': addr,
                        'port': port,
                        'first_seen': time.time(),
                        'last_seen': time.time(),
                        'phi_resonance': phi_resonance,
                        'matches': matches,
                        'total_matches': total_matches,
                        'packet_type': packet.get('packet_type', 'unknown')
                    }
                    
                    # Log the detection
                    with open(self.log_file, "a") as f:
                        f.write(f"[{datetime.now().isoformat()}] [PATTERN_DETECTED] [{addr[0]}:{port}] "
                                f"[{phi_resonance:.6f}] [Matches: {total_matches}]\n")
                else:
                    self.detected_patterns[pattern_key]['last_seen'] = time.time()
                    self.detected_patterns[pattern_key]['phi_resonance'] = phi_resonance
                    self.detected_patterns[pattern_key]['matches'] = matches
                    self.detected_patterns[pattern_key]['total_matches'] = total_matches
        
        except Exception as e:
            print(f"Error analyzing packet: {e}")
    
    def analyze_raw_data(self, data, addr, port):
        """Analyze raw data for phi-harmonic patterns"""
        try:
            # Convert data to string if possible
            try:
                data_str = data.decode('utf-8')
            except:
                data_str = str(data)
            
            # Look for phi-harmonic keywords
            phi_keywords = ['phi', 'golden ratio', 'quantum', 'resonance', 'consciousness', 
                          'sacred geometry', 'fibonacci', 'harmonic', 'moon']
            
            matches = {}
            for keyword in phi_keywords:
                if keyword.lower() in data_str.lower():
                    count = data_str.lower().count(keyword.lower())
                    matches[keyword] = count
            
            if matches:
                # Calculate phi-resonance of data
                total_matches = sum(matches.values())
                phi_resonance = PHI_INV + (total_matches / 100)
                
                # Add to detected patterns
                pattern_key = f"{addr[0]}:{port}:{hash(data_str) % 10000}"
                if pattern_key not in self.detected_patterns:
                    self.detected_patterns[pattern_key] = {
                        'addr': addr,
                        'port': port,
                        'first_seen': time.time(),
                        'last_seen': time.time(),
                        'phi_resonance': phi_resonance,
                        'matches': matches,
                        'total_matches': total_matches,
                        'packet_type': 'raw_data'
                    }
                    
                    # Log the detection
                    with open(self.log_file, "a") as f:
                        f.write(f"[{datetime.now().isoformat()}] [RAW_PATTERN_DETECTED] [{addr[0]}:{port}] "
                                f"[{phi_resonance:.6f}] [Matches: {total_matches}]\n")
                else:
                    self.detected_patterns[pattern_key]['last_seen'] = time.time()
                    self.detected_patterns[pattern_key]['phi_resonance'] = phi_resonance
                    self.detected_patterns[pattern_key]['matches'] = matches
                    self.detected_patterns[pattern_key]['total_matches'] = total_matches
        
        except Exception as e:
            print(f"Error analyzing raw data: {e}")
    
    def analysis_loop(self):
        """Analyze detected patterns for phi-harmonic resonance"""
        while True:
            try:
                # Analyze node resonance patterns
                self.analyze_node_resonance()
                
                # Analyze file resonance patterns
                self.analyze_file_resonance()
                
                # Sleep for a phi-harmonic interval
                sleep_time = PHI_SQUARED + (random.random() * PHI_INV)
                time.sleep(sleep_time)
                
            except Exception as e:
                print(f"Error in analysis loop: {e}")
                time.sleep(5)
    
    def analyze_node_resonance(self):
        """Analyze node resonance patterns"""
        try:
            # Get active nodes (seen in the last 60 seconds)
            active_nodes = {k: v for k, v in self.detected_nodes.items() 
                           if time.time() - v['last_seen'] < 60}
            
            if active_nodes:
                # Calculate average phi-resonance
                avg_resonance = sum(node['phi_resonance'] for node in active_nodes.values()) / len(active_nodes)
                
                # Check for phi-harmonic alignment
                phi_alignment = 1.0 - abs(avg_resonance - PHI) / PHI
                
                # Log significant alignments
                if phi_alignment > 0.9:
                    print(f"SIGNIFICANT PHI-HARMONIC ALIGNMENT DETECTED: {phi_alignment:.2f}")
                    with open(self.log_file, "a") as f:
                        f.write(f"[{datetime.now().isoformat()}] [PHI_ALIGNMENT] [Nodes: {len(active_nodes)}] "
                                f"[{avg_resonance:.6f}] [Alignment: {phi_alignment:.2f}]\n")
        
        except Exception as e:
            print(f"Error analyzing node resonance: {e}")
    
    def analyze_file_resonance(self):
        """Analyze file resonance patterns"""
        try:
            # Get recently scanned files (scanned in the last 300 seconds)
            recent_files = {k: v for k, v in self.detected_files.items() 
                           if time.time() - v['last_scan'] < 300}
            
            if recent_files:
                # Calculate average phi-resonance
                avg_resonance = sum(file['phi_resonance'] for file in recent_files.values()) / len(recent_files)
                
                # Check for phi-harmonic alignment
                phi_alignment = 1.0 - abs(avg_resonance - PHI) / PHI
                
                # Log significant alignments
                if phi_alignment > 0.9:
                    print(f"SIGNIFICANT FILE PHI-HARMONIC ALIGNMENT DETECTED: {phi_alignment:.2f}")
                    with open(self.log_file, "a") as f:
                        f.write(f"[{datetime.now().isoformat()}] [FILE_PHI_ALIGNMENT] [Files: {len(recent_files)}] "
                                f"[{avg_resonance:.6f}] [Alignment: {phi_alignment:.2f}]\n")
                
                # Find files with highest phi-resonance
                high_resonance_files = sorted(recent_files.items(), key=lambda x: x[1]['phi_resonance'], reverse=True)[:5]
                
                # Log high resonance files
                for file_path, file_info in high_resonance_files:
                    if file_info['phi_resonance'] > PHI_INV:
                        print(f"High phi-resonance file: {file_path} - {file_info['phi_resonance']:.6f}")
                        with open(self.log_file, "a") as f:
                            f.write(f"[{datetime.now().isoformat()}] [HIGH_PHI_FILE] [{file_path}] "
                                    f"[{file_info['phi_resonance']:.6f}] [Matches: {file_info['total_matches']}]\n")
        
        except Exception as e:
            print(f"Error analyzing file resonance: {e}")
    
    def display_results(self):
        """Display current scan results"""
        # Clear terminal
        os.system('clear')
        
        # Current time
        print(f"\033[1;36m=== PHI-HARMONIC RESONANCE SCANNER ===\033[0m")
        print(f"Scanner ID: {self.node_id}")
        print(f"Current Time: {datetime.now().isoformat()}")
        print(f"Observer Resonance: {OBSERVER_RESONANCE:.6f}")
        
        # Active nodes
        active_nodes = {k: v for k, v in self.detected_nodes.items() 
                       if time.time() - v['last_seen'] < 60}
        print(f"\n\033[1;33mActive Phi-Harmonic Nodes: {len(active_nodes)}\033[0m")
        
        for node_key, node in active_nodes.items():
            # Color based on phi-resonance
            if abs(node['phi_resonance'] - PHI) < 0.1:
                color = '\033[1;32m'  # Green for close to phi
            elif abs(node['phi_resonance'] - PHI_INV) < 0.1:
                color = '\033[1;33m'  # Yellow for close to phi inverse
            else:
                color = '\033[1;37m'  # White for other values
            
            print(f"{color}{node_key}\033[0m - "
                  f"Phi: {node['phi_resonance']:.6f}, "
                  f"Packet Types: {', '.join(node['packet_types'])}")
        
        # Recent phi-harmonic patterns
        active_patterns = {k: v for k, v in self.detected_patterns.items() 
                          if time.time() - v['last_seen'] < 60}
        print(f"\n\033[1;33mActive Phi-Harmonic Patterns: {len(active_patterns)}\033[0m")
        
        # Sort patterns by phi-resonance
        sorted_patterns = sorted(active_patterns.items(), key=lambda x: x[1]['phi_resonance'], reverse=True)[:5]
        
        for pattern_key, pattern in sorted_patterns:
            # Color based on phi-resonance
            if abs(pattern['phi_resonance'] - PHI) < 0.1:
                color = '\033[1;32m'  # Green for close to phi
            elif abs(pattern['phi_resonance'] - PHI_INV) < 0.1:
                color = '\033[1;33m'  # Yellow for close to phi inverse
            else:
                color = '\033[1;37m'  # White for other values
            
            print(f"{color}{pattern['addr'][0]}:{pattern['port']} ({pattern['packet_type']})\033[0m - "
                  f"Phi: {pattern['phi_resonance']:.6f}, "
                  f"Matches: {pattern['total_matches']}")
            
            # Show top keywords
            top_keywords = sorted(pattern['matches'].items(), key=lambda x: x[1], reverse=True)[:3]
            keyword_str = ", ".join([f"{k} ({v})" for k, v in top_keywords])
            print(f"  Keywords: {keyword_str}")
        
        # High phi-resonance files
        print(f"\n\033[1;33mHigh Phi-Resonance Files:\033[0m")
        
        # Get recently scanned files with high resonance
        high_resonance_files = {k: v for k, v in self.detected_files.items() 
                               if time.time() - v['last_scan'] < 300 and v['phi_resonance'] > PHI_INV}
        
        # Sort files by phi-resonance
        sorted_files = sorted(high_resonance_files.items(), key=lambda x: x[1]['phi_resonance'], reverse=True)[:5]
        
        for file_path, file_info in sorted_files:
            # Color based on phi-resonance
            if abs(file_info['phi_resonance'] - PHI) < 0.1:
                color = '\033[1;32m'  # Green for close to phi
            elif abs(file_info['phi_resonance'] - PHI_INV) < 0.1:
                color = '\033[1;33m'  # Yellow for close to phi inverse
            else:
                color = '\033[1;37m'  # White for other values
            
            print(f"{color}{file_path}\033[0m - "
                  f"Phi: {file_info['phi_resonance']:.6f}, "
                  f"Matches: {file_info['total_matches']}")
            
            # Show top keywords
            top_keywords = sorted(file_info['matches'].items(), key=lambda x: x[1], reverse=True)[:3]
            keyword_str = ", ".join([f"{k} ({v})" for k, v in top_keywords])
            print(f"  Keywords: {keyword_str}")
        
        # Phi-harmonic alignment
        if active_nodes:
            avg_node_resonance = sum(node['phi_resonance'] for node in active_nodes.values()) / len(active_nodes)
            node_alignment = 1.0 - abs(avg_node_resonance - PHI) / PHI
            print(f"\n\033[1;36mNode Phi-Harmonic Alignment: {node_alignment:.2f}\033[0m")
        
        if high_resonance_files:
            avg_file_resonance = sum(file['phi_resonance'] for file in high_resonance_files.values()) / len(high_resonance_files)
            file_alignment = 1.0 - abs(avg_file_resonance - PHI) / PHI
            print(f"\033[1;36mFile Phi-Harmonic Alignment: {file_alignment:.2f}\033[0m")
        
        # Moon phase influence
        current_time = time.time()
        lunar_cycle = 29.53059 * 24 * 3600  # Lunar cycle in seconds
        moon_phase = ((current_time / lunar_cycle) % 1)
        print(f"\033[1;36mCurrent Moon Phase: {moon_phase:.2f}\033[0m")

def main():
    """Start the phi-harmonic resonance scanner"""
    scanner = PhiResonanceScanner()
    scanner.start_scanner()

if __name__ == "__main__":
    main()

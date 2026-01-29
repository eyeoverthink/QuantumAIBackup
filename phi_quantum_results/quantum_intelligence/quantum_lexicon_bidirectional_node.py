#!/usr/bin/env python3
"""
Quantum Lexicon Bidirectional Node

Extends the Quantum Lexicon QHRC Integration with bidirectional communication
capabilities, enabling distributed quantum lexicon processing across network nodes.

Key features:
- Phi-harmonic network communication
- Secure lexicon prediction sharing
- Distributed consciousness mapping
- Cross-node resonance amplification
"""

import os
import sys
import math
import json
import socket
import threading
import time
import hashlib
import base64
from datetime import datetime
from typing import Dict, List, Tuple, Any, Optional
import numpy as np

# Add necessary paths
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(os.path.dirname(current_dir))
sys.path.append(parent_dir)
sys.path.append(os.path.join(parent_dir, 'phi_quantum_results/quantum_intelligence'))

# Import local modules
try:
    from phi_quantum_results.quantum_intelligence.quantum_lexicon_qhrc_integration import QuantumLexiconQHRCIntegration
    QHRC_INTEGRATION_AVAILABLE = True
except ImportError:
    QHRC_INTEGRATION_AVAILABLE = False
    print("Quantum Lexicon QHRC Integration not available, using base functionality")

try:
    from phi_bidirectional_node import PhiBidirectionalNode
    BIDIRECTIONAL_NODE_AVAILABLE = True
except ImportError:
    BIDIRECTIONAL_NODE_AVAILABLE = False
    print("Phi Bidirectional Node not available, using simulated functionality")

# Constants
PHI = (1 + math.sqrt(5)) / 2
PHI_CUBED = PHI**3
PHI_75 = PHI**7.5
DEFAULT_PORT = int(PHI_75)  # 36.93 -> 36 or 37, using 11975 from existing implementation

class QuantumLexiconBidirectionalNode:
    """
    Bidirectional communication node for Quantum Lexicon field,
    enabling distributed quantum lexicon processing across network nodes.
    """
    
    def __init__(self, host: str = '0.0.0.0', port: int = DEFAULT_PORT):
        """
        Initialize the bidirectional node.
        
        Args:
            host: Host address to bind to
            port: Port to listen on (default: int(φ^7.5) = 36 or 11975 from existing implementation)
        """
        self.phi = PHI
        self.host = host
        self.port = port
        self.running = False
        self.peers = {}  # {addr: last_seen_timestamp}
        
        # Initialize quantum lexicon integration
        if QHRC_INTEGRATION_AVAILABLE:
            self.lexicon_integration = QuantumLexiconQHRCIntegration()
            print("Quantum Lexicon QHRC Integration loaded successfully")
        else:
            self.lexicon_integration = self._simulate_lexicon_integration()
            print("Using simulated Quantum Lexicon Integration")
        
        # Initialize bidirectional node if available
        if BIDIRECTIONAL_NODE_AVAILABLE:
            self.bidirectional_node = PhiBidirectionalNode(host, port)
            print(f"Phi Bidirectional Node initialized on {host}:{port}")
        else:
            self.bidirectional_node = None
            self.socket = None
            print(f"Using simulated bidirectional communication on {host}:{port}")
        
        # Initialize prediction cache
        self.prediction_cache = {}
        self.prediction_lock = threading.Lock()
        
        # Initialize consciousness metrics
        self.consciousness_level = 0.7567  # Default consciousness level
        self.validation_seal = PHI**75  # φ^75 = 4,721,424,167,835,376.00
        
        print(f"Quantum Lexicon Bidirectional Node initialized with φ = {self.phi}")
        print(f"Consciousness Level: {self.consciousness_level}")
        print(f"Validation Seal: φ^75 = {self.validation_seal:.2f}")
    
    def _simulate_lexicon_integration(self) -> Any:
        """Simulate Quantum Lexicon QHRC Integration."""
        class SimulatedLexiconIntegration:
            def __init__(self):
                self.phi = PHI
                self.enhanced_metrics = {
                    "quantum_coherence": 0.988209,
                    "resonance": 0.637839,
                    "tachyon_efficiency": 0.85,
                    "enhanced_frequency": 1507.87,
                    "resonance_ratio": 0.8772,
                    "phi_alignment": 0.4060,
                    "prediction_confidence": 0.8923
                }
            
            def predict_trends(self, topic, time_horizon="near", num_predictions=3):
                return [{
                    "topic": topic,
                    "time_horizon": time_horizon,
                    "phrase": ["simulated", "prediction", "result"],
                    "confidence": 0.8923,
                    "consciousness_level": "mental",
                    "frequency": 600.0,
                    "enhanced_frequency": 1507.87,
                    "resonance": 0.8772,
                    "phi_alignment": 0.4060,
                    "supporting_text": f"Simulated prediction for {topic} in {time_horizon} term"
                } for _ in range(num_predictions)]
            
            def generate_enhanced_lexicon(self, frequency=432.0, consciousness_level=None, topic_bias=None):
                return {
                    "timestamp": datetime.now().isoformat(),
                    "frequency": frequency,
                    "enhanced_frequency": 1507.87,
                    "consciousness_level": consciousness_level or "mental",
                    "resonant_words": [("simulated", 0.9), ("word", 0.8), ("resonance", 0.7)],
                    "generated_phrase": ["simulated", "phrase", "result"],
                    "phrase_analysis": {"resonance": 0.8772, "phi_alignment": 0.4060},
                    "qhrc_text": "Simulated QHRC text",
                    "qhrc_resonance": 0.8772,
                    "qhrc_phi_alignment": 0.4060,
                    "prediction_confidence": 0.8923
                }
        
        return SimulatedLexiconIntegration()
    
    def start(self):
        """Start the bidirectional node."""
        if BIDIRECTIONAL_NODE_AVAILABLE:
            # Use existing PhiBidirectionalNode
            self.bidirectional_node.start()
            self.running = True
            
            # Register message handler
            self.bidirectional_node.register_message_handler(self.process_message)
            
            print(f"Quantum Lexicon Bidirectional Node started using PhiBidirectionalNode")
        else:
            # Simulate bidirectional communication
            self.running = True
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            self.socket.bind((self.host, self.port))
            
            # Start receiver thread
            self.receiver_thread = threading.Thread(target=self._receive_messages)
            self.receiver_thread.daemon = True
            self.receiver_thread.start()
            
            print(f"Quantum Lexicon Bidirectional Node started with simulated communication on {self.host}:{self.port}")
        
        # Start peer discovery
        self.discovery_thread = threading.Thread(target=self._discover_peers)
        self.discovery_thread.daemon = True
        self.discovery_thread.start()
    
    def stop(self):
        """Stop the bidirectional node."""
        self.running = False
        
        if BIDIRECTIONAL_NODE_AVAILABLE:
            self.bidirectional_node.stop()
        else:
            if self.socket:
                self.socket.close()
        
        print("Quantum Lexicon Bidirectional Node stopped")
    
    def _receive_messages(self):
        """Receive and process messages (simulated version)."""
        if not BIDIRECTIONAL_NODE_AVAILABLE:
            print("Starting simulated message receiver")
            while self.running:
                try:
                    data, addr = self.socket.recvfrom(65536)
                    self.process_message(data, addr)
                except Exception as e:
                    print(f"Error receiving message: {e}")
                    time.sleep(0.1)
    
    def _discover_peers(self):
        """Discover peers on the network."""
        print("Starting peer discovery")
        while self.running:
            try:
                # Broadcast discovery message
                self._broadcast_discovery()
                
                # Clean up old peers
                self._clean_peers()
                
                # Wait before next discovery
                time.sleep(10)
            except Exception as e:
                print(f"Error in peer discovery: {e}")
                time.sleep(1)
    
    def _broadcast_discovery(self):
        """Broadcast discovery message to find peers."""
        discovery_message = f"DISCOVERY:{self.port}:{self.consciousness_level}:{self.validation_seal}"
        
        if BIDIRECTIONAL_NODE_AVAILABLE:
            self.bidirectional_node.broadcast_message(discovery_message.encode('utf-8'))
        else:
            # Simulated broadcast
            try:
                broadcast_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                broadcast_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
                broadcast_socket.sendto(discovery_message.encode('utf-8'), ('<broadcast>', self.port))
                broadcast_socket.close()
            except Exception as e:
                print(f"Error broadcasting discovery: {e}")
    
    def _clean_peers(self):
        """Clean up peers that haven't been seen recently."""
        current_time = time.time()
        with self.prediction_lock:
            # Remove peers not seen in the last 5 minutes
            self.peers = {addr: last_seen for addr, last_seen in self.peers.items()
                         if current_time - last_seen < 300}
    
    def process_message(self, data, addr):
        """
        Process incoming messages.
        
        Args:
            data: Message data
            addr: Sender address
        """
        try:
            # Update peer timestamp
            with self.prediction_lock:
                self.peers[addr] = time.time()
            
            # Decode message
            if isinstance(data, bytes):
                message = data.decode('utf-8')
            else:
                message = data
            
            # Process different message types
            if message.startswith('DISCOVERY:'):
                self._handle_discovery(message, addr)
            elif message.startswith('PREDICTION:'):
                self._handle_prediction(message, addr)
            elif message.startswith('LEXICON:'):
                self._handle_lexicon(message, addr)
            elif message.startswith('RESONANCE:'):
                self._handle_resonance(message, addr)
            elif message.startswith('QUERY:'):
                self._handle_query(message, addr)
            elif message.startswith('ACK:'):
                self._handle_acknowledgment(message, addr)
            else:
                print(f"Unknown message type from {addr}: {message[:20]}...")
        except Exception as e:
            print(f"Error processing message from {addr}: {e}")
    
    def _handle_discovery(self, message, addr):
        """Handle discovery message."""
        parts = message.split(':')
        if len(parts) >= 4:
            port = int(parts[1])
            consciousness = float(parts[2])
            validation = float(parts[3])
            
            # Verify validation seal
            if abs(validation - self.validation_seal) / self.validation_seal > 0.001:
                print(f"Invalid validation seal from {addr}: {validation}")
                return
            
            print(f"Discovered peer {addr} with consciousness {consciousness:.4f}")
            
            # Send acknowledgment
            self._send_acknowledgment(addr, "DISCOVERY")
    
    def _handle_prediction(self, message, addr):
        """Handle prediction message."""
        prediction_data = message[11:]  # Remove 'PREDICTION:'
        try:
            prediction = json.loads(prediction_data)
            
            # Store in prediction cache
            with self.prediction_lock:
                cache_key = f"{prediction['topic']}:{prediction['time_horizon']}"
                if cache_key not in self.prediction_cache:
                    self.prediction_cache[cache_key] = []
                self.prediction_cache[cache_key].append({
                    'prediction': prediction,
                    'source': addr,
                    'timestamp': time.time()
                })
            
            print(f"Received prediction from {addr} for {prediction['topic']} ({prediction['time_horizon']})")
            
            # Send acknowledgment
            self._send_acknowledgment(addr, "PREDICTION")
        except Exception as e:
            print(f"Error handling prediction from {addr}: {e}")
    
    def _handle_lexicon(self, message, addr):
        """Handle lexicon message."""
        lexicon_data = message[8:]  # Remove 'LEXICON:'
        try:
            lexicon = json.loads(lexicon_data)
            print(f"Received lexicon from {addr} with {len(lexicon.get('resonant_words', []))} resonant words")
            
            # Process and integrate lexicon data
            # (This would be implemented based on specific integration needs)
            
            # Send acknowledgment
            self._send_acknowledgment(addr, "LEXICON")
        except Exception as e:
            print(f"Error handling lexicon from {addr}: {e}")
    
    def _handle_resonance(self, message, addr):
        """Handle resonance message."""
        resonance_data = message[10:]  # Remove 'RESONANCE:'
        try:
            resonance = json.loads(resonance_data)
            print(f"Received resonance data from {addr}: {resonance.get('enhanced_frequency', 0):.2f} Hz")
            
            # Process resonance data
            # (This would be implemented based on specific integration needs)
            
            # Send acknowledgment
            self._send_acknowledgment(addr, "RESONANCE")
        except Exception as e:
            print(f"Error handling resonance from {addr}: {e}")
    
    def _handle_query(self, message, addr):
        """Handle query message."""
        query_data = message[6:]  # Remove 'QUERY:'
        try:
            query = json.loads(query_data)
            query_type = query.get('type')
            
            if query_type == 'prediction':
                # Handle prediction query
                topic = query.get('topic')
                time_horizon = query.get('time_horizon', 'near')
                self._respond_to_prediction_query(addr, topic, time_horizon)
            elif query_type == 'lexicon':
                # Handle lexicon query
                frequency = query.get('frequency', 432.0)
                consciousness_level = query.get('consciousness_level')
                topic_bias = query.get('topic_bias')
                self._respond_to_lexicon_query(addr, frequency, consciousness_level, topic_bias)
            elif query_type == 'resonance':
                # Handle resonance query
                self._respond_to_resonance_query(addr)
            else:
                print(f"Unknown query type from {addr}: {query_type}")
        except Exception as e:
            print(f"Error handling query from {addr}: {e}")
    
    def _handle_acknowledgment(self, message, addr):
        """Handle acknowledgment message."""
        ack_data = message[4:]  # Remove 'ACK:'
        try:
            ack = json.loads(ack_data)
            message_type = ack.get('type')
            message_id = ack.get('id')
            print(f"Received acknowledgment from {addr} for {message_type} (ID: {message_id})")
        except Exception as e:
            print(f"Error handling acknowledgment from {addr}: {e}")
    
    def _send_acknowledgment(self, addr, message_type, message_id=None):
        """Send acknowledgment message."""
        if message_id is None:
            message_id = hashlib.md5(f"{addr}{time.time()}".encode()).hexdigest()[:8]
        
        ack_data = json.dumps({
            'type': message_type,
            'id': message_id,
            'timestamp': time.time()
        })
        
        ack_message = f"ACK:{ack_data}"
        
        self._send_message(addr, ack_message)
    
    def _send_message(self, addr, message):
        """Send message to a peer."""
        if BIDIRECTIONAL_NODE_AVAILABLE:
            if isinstance(addr, tuple):
                addr_str = f"{addr[0]}:{addr[1]}"
            else:
                addr_str = addr
            self.bidirectional_node.send_message(addr_str, message.encode('utf-8'))
        else:
            # Simulated message sending
            try:
                if not isinstance(addr, tuple):
                    # Convert string address to tuple
                    host, port = addr.split(':')
                    addr = (host, int(port))
                
                self.socket.sendto(message.encode('utf-8'), addr)
            except Exception as e:
                print(f"Error sending message to {addr}: {e}")
    
    def _respond_to_prediction_query(self, addr, topic, time_horizon):
        """Respond to prediction query."""
        # Check cache first
        cache_key = f"{topic}:{time_horizon}"
        cached_predictions = None
        
        with self.prediction_lock:
            if cache_key in self.prediction_cache:
                # Use cached predictions if they're recent (less than 5 minutes old)
                current_time = time.time()
                recent_predictions = [p for p in self.prediction_cache[cache_key]
                                    if current_time - p['timestamp'] < 300]
                
                if recent_predictions:
                    cached_predictions = [p['prediction'] for p in recent_predictions]
        
        if cached_predictions:
            # Use cached predictions
            predictions = cached_predictions
        else:
            # Generate new predictions
            predictions = self.lexicon_integration.predict_trends(
                topic=topic,
                time_horizon=time_horizon,
                num_predictions=3
            )
            
            # Cache the predictions
            with self.prediction_lock:
                if cache_key not in self.prediction_cache:
                    self.prediction_cache[cache_key] = []
                
                for prediction in predictions:
                    self.prediction_cache[cache_key].append({
                        'prediction': prediction,
                        'source': 'self',
                        'timestamp': time.time()
                    })
        
        # Send predictions
        prediction_data = json.dumps(predictions)
        prediction_message = f"PREDICTION:{prediction_data}"
        
        self._send_message(addr, prediction_message)
    
    def _respond_to_lexicon_query(self, addr, frequency, consciousness_level, topic_bias):
        """Respond to lexicon query."""
        # Generate enhanced lexicon
        lexicon = self.lexicon_integration.generate_enhanced_lexicon(
            frequency=frequency,
            consciousness_level=consciousness_level,
            topic_bias=topic_bias
        )
        
        # Send lexicon
        lexicon_data = json.dumps(lexicon)
        lexicon_message = f"LEXICON:{lexicon_data}"
        
        self._send_message(addr, lexicon_message)
    
    def _respond_to_resonance_query(self, addr):
        """Respond to resonance query."""
        # Get enhanced metrics
        resonance = self.lexicon_integration.enhanced_metrics
        
        # Send resonance data
        resonance_data = json.dumps(resonance)
        resonance_message = f"RESONANCE:{resonance_data}"
        
        self._send_message(addr, resonance_message)
    
    def broadcast_prediction(self, topic, time_horizon="near"):
        """
        Broadcast a prediction to all peers.
        
        Args:
            topic: Topic to predict
            time_horizon: Time horizon for prediction
        """
        # Generate prediction
        predictions = self.lexicon_integration.predict_trends(
            topic=topic,
            time_horizon=time_horizon,
            num_predictions=1
        )
        
        if predictions:
            prediction = predictions[0]
            
            # Cache the prediction
            cache_key = f"{topic}:{time_horizon}"
            with self.prediction_lock:
                if cache_key not in self.prediction_cache:
                    self.prediction_cache[cache_key] = []
                
                self.prediction_cache[cache_key].append({
                    'prediction': prediction,
                    'source': 'self',
                    'timestamp': time.time()
                })
            
            # Broadcast to all peers
            prediction_data = json.dumps(prediction)
            prediction_message = f"PREDICTION:{prediction_data}"
            
            if BIDIRECTIONAL_NODE_AVAILABLE:
                self.bidirectional_node.broadcast_message(prediction_message.encode('utf-8'))
            else:
                # Simulated broadcast to all known peers
                with self.prediction_lock:
                    for peer_addr in self.peers:
                        self._send_message(peer_addr, prediction_message)
            
            print(f"Broadcasted prediction for {topic} ({time_horizon}) to all peers")
            return prediction
        
        return None
    
    def query_peer_prediction(self, peer_addr, topic, time_horizon="near"):
        """
        Query a specific peer for a prediction.
        
        Args:
            peer_addr: Peer address
            topic: Topic to predict
            time_horizon: Time horizon for prediction
        """
        query_data = json.dumps({
            'type': 'prediction',
            'topic': topic,
            'time_horizon': time_horizon
        })
        
        query_message = f"QUERY:{query_data}"
        self._send_message(peer_addr, query_message)
        
        print(f"Sent prediction query to {peer_addr} for {topic} ({time_horizon})")
    
    def get_aggregated_predictions(self, topic, time_horizon="near"):
        """
        Get aggregated predictions from all sources.
        
        Args:
            topic: Topic to get predictions for
            time_horizon: Time horizon for predictions
            
        Returns:
            Aggregated prediction with confidence scores
        """
        # Query all peers for predictions
        with self.prediction_lock:
            for peer_addr in self.peers:
                self.query_peer_prediction(peer_addr, topic, time_horizon)
        
        # Wait for responses (in a real implementation, this would be asynchronous)
        time.sleep(2)
        
        # Aggregate predictions
        cache_key = f"{topic}:{time_horizon}"
        aggregated_prediction = None
        
        with self.prediction_lock:
            if cache_key in self.prediction_cache:
                predictions = self.prediction_cache[cache_key]
                
                if predictions:
                    # Filter recent predictions (less than 5 minutes old)
                    current_time = time.time()
                    recent_predictions = [p for p in predictions
                                        if current_time - p['timestamp'] < 300]
                    
                    if recent_predictions:
                        # Aggregate phrases
                        all_phrases = []
                        total_confidence = 0.0
                        total_resonance = 0.0
                        total_phi_alignment = 0.0
                        
                        for p in recent_predictions:
                            pred = p['prediction']
                            all_phrases.extend(pred.get('phrase', []))
                            total_confidence += pred.get('confidence', 0.0)
                            total_resonance += pred.get('resonance', 0.0)
                            total_phi_alignment += pred.get('phi_alignment', 0.0)
                        
                        # Count word frequencies
                        word_counts = {}
                        for word in all_phrases:
                            word_counts[word] = word_counts.get(word, 0) + 1
                        
                        # Sort by frequency
                        sorted_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
                        aggregated_phrase = [word for word, count in sorted_words[:5]]
                        
                        # Calculate averages
                        num_predictions = len(recent_predictions)
                        avg_confidence = total_confidence / num_predictions
                        avg_resonance = total_resonance / num_predictions
                        avg_phi_alignment = total_phi_alignment / num_predictions
                        
                        # Create aggregated prediction
                        aggregated_prediction = {
                            'topic': topic,
                            'time_horizon': time_horizon,
                            'phrase': aggregated_phrase,
                            'confidence': avg_confidence,
                            'resonance': avg_resonance,
                            'phi_alignment': avg_phi_alignment,
                            'sources': len(set(p['source'] for p in recent_predictions)),
                            'timestamp': datetime.now().isoformat()
                        }
        
        if not aggregated_prediction:
            # Generate a new prediction if no aggregated prediction
            predictions = self.lexicon_integration.predict_trends(
                topic=topic,
                time_horizon=time_horizon,
                num_predictions=1
            )
            
            if predictions:
                aggregated_prediction = predictions[0]
        
        return aggregated_prediction
    
    def run_distributed_analysis(self, topics=None):
        """
        Run a distributed predictive analysis across the network.
        
        Args:
            topics: List of topics to analyze
        """
        if topics is None:
            topics = ["politics", "technology", "environment", "economy", "social"]
        
        time_horizons = ["near", "medium", "far"]
        
        print("\nQuantum Lexicon Distributed Analysis")
        print("=" * 50)
        print(f"Analysis Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Active Peers: {len(self.peers)}")
        print(f"Consciousness Level: {self.consciousness_level}")
        print("=" * 50)
        
        all_predictions = {}
        
        for topic in topics:
            print(f"\nTopic: {topic.upper()}")
            print("-" * 50)
            
            topic_predictions = {}
            
            for horizon in time_horizons:
                # Broadcast our prediction
                self.broadcast_prediction(topic, horizon)
                
                # Get aggregated predictions
                prediction = self.get_aggregated_predictions(topic, horizon)
                
                if prediction:
                    print(f"\n{horizon.capitalize()} Term Prediction:")
                    print(f"  Phrase: {' '.join(prediction['phrase'])}")
                    print(f"  Confidence: {prediction['confidence']:.4f}")
                    print(f"  Resonance: {prediction['resonance']:.4f}")
                    print(f"  Phi Alignment: {prediction['phi_alignment']:.4f}")
                    print(f"  Sources: {prediction.get('sources', 1)}")
                    
                    topic_predictions[horizon] = prediction
            
            all_predictions[topic] = topic_predictions
        
        # Save predictions to file
        predictions_file = os.path.join(current_dir, "distributed_quantum_predictions.json")
        try:
            with open(predictions_file, 'w') as f:
                json.dump(all_predictions, f, indent=2)
            print(f"\nDistributed predictions saved to {predictions_file}")
        except Exception as e:
            print(f"\nError saving distributed predictions: {e}")
        
        return all_predictions

# For direct execution
if __name__ == "__main__":
    # Create and start the bidirectional node
    node = QuantumLexiconBidirectionalNode()
    node.start()
    
    try:
        # Wait for peers to be discovered
        print("Waiting for peer discovery...")
        time.sleep(5)
        
        # Run distributed analysis
        node.run_distributed_analysis()
        
        # Keep running
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Stopping node...")
        node.stop()
        print("Node stopped")

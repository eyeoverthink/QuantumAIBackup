#!/usr/bin/env python3
# CIEAT Temporal Bridge - φ-Dimensional Temporal Integration
# φ^∞ © 2025 Vaughn Scott - All Rights Reserved in All Realities

import numpy as np
import json
import time
import datetime
import os
import hashlib
from typing import Dict, List, Tuple, Optional, Any

# Import CIEAT components
from cieat_core import CIEATSystem, PhiPhaseGenerator, RealityEngine, QuantumInterface
from cieat_fraymus_protocol import phi_transform, inverse_transform, protect
from centripetal_memory_adapter import get_centripetal_memory

# Constants
PHI = (1 + 5 ** 0.5) / 2  # Golden ratio
PI = np.pi
PHI_POWERS = [PHI**i for i in range(-5, 15)]  # Enhanced φ-harmonic range
FIBONACCI = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]

class CIEATTemporalBridge:
    """Bridge between CIEAT system and temporal applications with φ-dimensional protection"""
    
    def __init__(self):
        """Initialize the CIEAT Temporal Bridge"""
        self.phi_phase_generator = PhiPhaseGenerator()
        self.reality_engine = RealityEngine()
        self.quantum_interface = QuantumInterface()
        self.memory = get_centripetal_memory()
        
        # Temporal metrics
        self.temporal_distance_map = {}  # Maps game_id to temporal distances
        self.phi_resonance_map = {}      # Maps game_id to φ-resonance values
        self.temporal_chain = []         # Temporal verification chain
        
        # Create results directory if it doesn't exist
        os.makedirs("cieat_temporal_results", exist_ok=True)
        
        print("[*] CIEAT Temporal Bridge initialized")
        print("[*] φ-Dimensional protection active")
    
    def register_temporal_event(self, game_id: str, board_state: List[List[str]], 
                               move: Tuple[int, int], player: str) -> Dict:
        """
        Register a temporal event with φ-dimensional protection
        
        Args:
            game_id: Unique identifier for the game
            board_state: Current board state
            move: Move coordinates (row, col)
            player: Player making the move ('X' or 'O')
            
        Returns:
            Protected temporal event data
        """
        # Create temporal event data
        event_data = {
            "game_id": game_id,
            "timestamp": time.time(),
            "iso_timestamp": datetime.datetime.now().isoformat(),
            "board_state": board_state,
            "move": move,
            "player": player
        }
        
        # Calculate φ-resonance for this event
        phi_resonance = self._calculate_phi_resonance(board_state, move)
        event_data["phi_resonance"] = phi_resonance
        
        # Store in resonance map
        self.phi_resonance_map[game_id] = self.phi_resonance_map.get(game_id, []) + [phi_resonance]
        
        # Transform to φ-space
        phi_space_data = self._transform_to_phi_space(event_data)
        event_data["phi_space_signature"] = phi_space_data["signature"]
        
        # Apply reality protection
        protected_event = self._apply_protection(event_data)
        
        # Store in centripetal memory
        self.memory.add_memory(protected_event, weight=phi_resonance)
        
        # Update temporal chain
        self._update_temporal_chain(protected_event)
        
        # Save to file
        self._save_event(protected_event)
        
        return protected_event
    
    def get_temporal_suggestion(self, game_id: str, current_board: List[List[str]], 
                               player: str) -> Tuple[Optional[Tuple[int, int]], float, float]:
        """
        Get a move suggestion based on temporal feedback with empirical timestamps
        
        Args:
            game_id: Current game identifier
            current_board: Current board state
            player: Current player ('X' or 'O')
            
        Returns:
            Tuple of (move, resonance, temporal_distance)
        """
        # Convert board to string representation for comparison
        current_state = self._board_to_string(current_board)
        
        # Get all temporal events from memory
        all_events = self.memory.get_memories()
        
        # Filter events for other games (not current game)
        other_game_events = [event for event in all_events if event.get("game_id", "") != game_id]
        
        # Find matching board states
        temporal_matches = []
        
        for event in other_game_events:
            event_board = event.get("board_state")
            if not event_board:
                continue
                
            event_state = self._board_to_string(event_board)
            
            # Check if states match
            if event_state == current_state:
                move = event.get("move")
                if not move or len(move) < 2:
                    continue
                    
                row, col = move[0], move[1]
                
                # Verify move is valid
                if 0 <= row < 3 and 0 <= col < 3 and current_board[row][col] == ' ':
                    # Calculate temporal distance
                    temporal_distance = time.time() - event.get("timestamp", time.time())
                    
                    # Calculate φ-harmonic resonance
                    phi_scaled_distance = abs(temporal_distance) / (PHI ** 5)
                    resonance = 1.0 / (1.0 + phi_scaled_distance)
                    
                    # Store temporal distance
                    if game_id not in self.temporal_distance_map:
                        self.temporal_distance_map[game_id] = []
                    self.temporal_distance_map[game_id].append(temporal_distance)
                    
                    # Add to matches
                    temporal_matches.append({
                        "move": (row, col),
                        "resonance": resonance,
                        "temporal_distance": temporal_distance,
                        "event_timestamp": event.get("iso_timestamp", "unknown"),
                        "phi_space_signature": event.get("phi_space_signature", "")
                    })
        
        # Sort by resonance (highest first)
        temporal_matches.sort(key=lambda x: x["resonance"], reverse=True)
        
        # Return best match if available
        if temporal_matches:
            return (temporal_matches[0]["move"], 
                   temporal_matches[0]["resonance"], 
                   temporal_matches[0]["temporal_distance"])
        
        # No match found
        return None, 0.0, 0.0
    
    def analyze_temporal_metrics(self, game_id: Optional[str] = None) -> Dict:
        """
        Analyze temporal metrics for a game or all games
        
        Args:
            game_id: Specific game to analyze (all games if None)
            
        Returns:
            Dictionary with temporal analysis metrics
        """
        if game_id:
            # Analyze specific game
            distances = self.temporal_distance_map.get(game_id, [])
            resonances = self.phi_resonance_map.get(game_id, [])
        else:
            # Analyze all games
            distances = []
            resonances = []
            for game_distances in self.temporal_distance_map.values():
                distances.extend(game_distances)
            for game_resonances in self.phi_resonance_map.values():
                resonances.extend(game_resonances)
        
        # Calculate metrics
        metrics = {
            "temporal_influence_count": len(distances),
            "average_temporal_distance": np.mean(distances) if distances else 0,
            "max_temporal_distance": max(distances) if distances else 0,
            "min_temporal_distance": min(distances) if distances else 0,
            "average_phi_resonance": np.mean(resonances) if resonances else 0,
            "temporal_chain_length": len(self.temporal_chain),
            "temporal_chain_integrity": self._verify_temporal_chain()
        }
        
        # Calculate φ-dimensional metrics
        if resonances:
            phi_ratio = abs(1 - np.mean(resonances)/PHI)
            metrics["phi_ratio"] = phi_ratio
            metrics["phi_harmonic_alignment"] = 1 - phi_ratio
            metrics["causality_defiance_score"] = (1 - phi_ratio) * PHI
        
        return metrics
    
    def _board_to_string(self, board: List[List[str]]) -> str:
        """Convert board to string representation"""
        return ''.join(''.join(row).replace(' ', '-') for row in board)
    
    def _calculate_phi_resonance(self, board_state: List[List[str]], move: Tuple[int, int]) -> float:
        """Calculate φ-resonance for a board state and move"""
        # Convert board to flat array
        flat_board = [cell for row in board_state for cell in row]
        
        # Count pieces
        x_count = flat_board.count('X')
        o_count = flat_board.count('O')
        empty_count = flat_board.count(' ')
        
        # Calculate game progression (0 to 1)
        progression = (x_count + o_count) / 9
        
        # Calculate move position resonance
        row, col = move
        position_value = (row * 3 + col + 1) / 9  # 1-9 normalized to 0-1
        
        # Apply φ-harmonic scaling
        phi_position = abs(position_value - 1/PHI) / PHI
        phi_progression = abs(progression - 1/PHI) / PHI
        
        # Calculate resonance (higher is better)
        resonance = 1 - (phi_position + phi_progression) / 2
        
        return resonance
    
    def _transform_to_phi_space(self, event_data: Dict) -> Dict:
        """Transform event data to φ-space"""
        # Create data string for transformation
        data_string = f"{event_data['game_id']}:{event_data['timestamp']}:{event_data['player']}"
        data_string += f":{self._board_to_string(event_data['board_state'])}"
        
        # Create numerical representation
        data_bytes = data_string.encode()
        data_array = np.array([b for b in data_bytes])
        
        # Apply φ-transform
        transformed = phi_transform(data_array)
        
        # Create signature
        signature = hashlib.sha256(str(transformed).encode()).hexdigest()
        
        return {
            "transformed_data": transformed,
            "signature": signature
        }
    
    def _apply_protection(self, event_data: Dict) -> Dict:
        """Apply φ-dimensional reality protection"""
        # Create protected copy
        protected = event_data.copy()
        
        # Add protection markers
        protected['protected'] = True
        protected['protection_level'] = "φ-Dimensional"
        
        # Generate φ-stamp for verification
        data_string = f"{protected['game_id']}:{protected['timestamp']}:{protected['phi_resonance']}"
        protected['phi_stamp'] = hashlib.sha512((data_string + str(PHI**3)).encode()).hexdigest()
        
        # Add reality protection hash chain
        protected['reality_chain'] = []
        for i in range(5):
            prev_hash = protected['phi_stamp'] if i == 0 else protected['reality_chain'][i-1]
            fib_value = FIBONACCI[i % len(FIBONACCI)]
            new_hash = hashlib.sha512((prev_hash + str(PHI**fib_value)).encode()).hexdigest()
            protected['reality_chain'].append(new_hash)
        
        return protected
    
    def _update_temporal_chain(self, event_data: Dict) -> None:
        """Update the temporal verification chain"""
        # Create chain link
        chain_link = {
            "timestamp": event_data["timestamp"],
            "game_id": event_data["game_id"],
            "phi_stamp": event_data["phi_stamp"]
        }
        
        # Add previous link hash if available
        if self.temporal_chain:
            prev_link = self.temporal_chain[-1]
            prev_hash = prev_link.get("link_hash", "")
            chain_link["prev_hash"] = prev_hash
        
        # Generate link hash
        link_data = f"{chain_link['timestamp']}:{chain_link['game_id']}:{chain_link['phi_stamp']}"
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
            link_data = f"{current['timestamp']}:{current['game_id']}:{current['phi_stamp']}"
            if "prev_hash" in current:
                link_data += f":{current['prev_hash']}"
            
            expected_hash = hashlib.sha512((link_data + str(PHI**7)).encode()).hexdigest()
            if current.get("link_hash") != expected_hash:
                return False
        
        return True
    
    def _save_event(self, event_data: Dict) -> None:
        """Save event data to file"""
        # Create filename with timestamp
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"cieat_temporal_results/temporal_event_{timestamp}.json"
        
        # Save to file
        with open(filename, "w") as f:
            json.dump(event_data, f, indent=2)


# Singleton instance
_bridge_instance = None

def get_temporal_bridge():
    """Get the CIEATTemporalBridge instance"""
    global _bridge_instance
    if _bridge_instance is None:
        _bridge_instance = CIEATTemporalBridge()
    return _bridge_instance


if __name__ == "__main__":
    print("="*50)
    print("CIEAT TEMPORAL BRIDGE - φ-DIMENSIONAL PROTECTION")
    print("φ^∞ © 2025 Vaughn Scott | All Rights Reserved in All Realities")
    print("="*50)
    
    # Initialize bridge
    bridge = get_temporal_bridge()
    
    # Demo with sample data
    game_id = f"test_game_{int(time.time())}"
    board = [[' ', ' ', ' '], [' ', 'X', ' '], [' ', ' ', ' ']]
    move = (0, 0)
    player = 'O'
    
    # Register event
    print("\n[*] Registering temporal event...")
    event = bridge.register_temporal_event(game_id, board, move, player)
    
    print(f"[✓] Event registered with φ-resonance: {event['phi_resonance']:.4f}")
    print(f"[✓] φ-stamp: {event['phi_stamp'][:16]}...")
    
    # Get suggestion
    print("\n[*] Testing temporal suggestion...")
    suggestion, resonance, distance = bridge.get_temporal_suggestion(
        f"new_game_{int(time.time())}", board, player
    )
    
    if suggestion:
        print(f"[✓] Temporal suggestion: {suggestion}")
        print(f"[✓] Resonance: {resonance:.4f}")
        print(f"[✓] Temporal distance: {distance:.2f} seconds")
    else:
        print("[!] No temporal suggestion available yet")
    
    # Analyze metrics
    print("\n[*] Analyzing temporal metrics...")
    metrics = bridge.analyze_temporal_metrics()
    
    print(f"[✓] Temporal influence count: {metrics['temporal_influence_count']}")
    print(f"[✓] Average φ-resonance: {metrics['average_phi_resonance']:.4f}")
    print(f"[✓] Temporal chain integrity: {metrics['temporal_chain_integrity']}")
    
    if 'causality_defiance_score' in metrics:
        print(f"[✓] Causality defiance score: {metrics['causality_defiance_score']:.4f}")
    
    print("\n" + "="*50)
    print("φ^∞ © 2025 Vaughn Scott | All Rights Reserved in All Realities")
    print("="*50)

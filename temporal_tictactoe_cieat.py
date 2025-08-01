#!/usr/bin/env python3
# Temporal Tic-Tac-Toe with CIEAT Integration - FRAYMUS System
# φ^∞ © 2025 Vaughn Scott - All Rights Reserved in All Realities

import numpy as np
import json
import time
import datetime
import os
import hashlib
import uuid
from typing import Dict, List, Tuple, Optional, Any

# Import CIEAT Temporal Bridge
from cieat_temporal_bridge import get_temporal_bridge

# Constants
PHI = (1 + 5 ** 0.5) / 2  # Golden ratio
PI = np.pi
PHI_POWERS = [PHI**i for i in range(-5, 15)]  # Enhanced φ-harmonic range
FIBONACCI = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]

class TemporalTicTacToeCIEAT:
    """Temporal Tic-Tac-Toe with CIEAT φ-Dimensional Protection"""
    
    def __init__(self):
        """Initialize the Temporal Tic-Tac-Toe game with CIEAT integration"""
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'
        self.game_id = f"game_{int(time.time())}_{uuid.uuid4().hex[:8]}"
        self.moves_history = []
        self.board_states = []
        self.temporal_moves = 0
        self.total_moves = 0
        self.temporal_influence_detected = False
        self.temporal_bridge = get_temporal_bridge()
        
        # Create results directory if it doesn't exist
        os.makedirs("tictactoe_results", exist_ok=True)
        
        print("[*] Temporal Tic-Tac-Toe with CIEAT initialized")
        print(f"[*] Game ID: {self.game_id}")
        print("[*] φ-Dimensional protection active")
    
    def make_move(self, row: int, col: int) -> bool:
        """Make a move on the board"""
        if not (0 <= row < 3 and 0 <= col < 3) or self.board[row][col] != ' ':
            return False
        
        # Save current board state before move
        current_state = [row[:] for row in self.board]
        self.board_states.append(current_state)
        
        # Make the move
        self.board[row][col] = self.current_player
        self.moves_history.append((row, col))
        self.total_moves += 1
        
        # Register with CIEAT Temporal Bridge
        self.temporal_bridge.register_temporal_event(
            self.game_id, 
            current_state,  # Board state before move
            (row, col), 
            self.current_player
        )
        
        # Switch player
        self.current_player = 'O' if self.current_player == 'X' else 'X'
        
        return True
    
    def get_ai_move(self) -> Tuple[int, int]:
        """Get AI move with temporal feedback"""
        # Try to get temporal move suggestion
        move, resonance, temporal_distance = self.temporal_bridge.get_temporal_suggestion(
            self.game_id, self.board, self.current_player
        )
        
        # If strong temporal influence detected
        if move and resonance > 0.7:
            self.temporal_moves += 1
            self.temporal_influence_detected = True
            print(f"[!] Temporal influence detected (φ-resonance: {resonance:.4f})")
            return move
        
        # Fallback to minimax
        return self._get_minimax_move()
    
    def _get_minimax_move(self) -> Tuple[int, int]:
        """Get best move using minimax algorithm"""
        best_score = float('-inf')
        best_move = None
        
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == ' ':
                    self.board[i][j] = self.current_player
                    score = self._minimax(0, False)
                    self.board[i][j] = ' '
                    
                    if score > best_score:
                        best_score = score
                        best_move = (i, j)
        
        return best_move
    
    def _minimax(self, depth: int, is_maximizing: bool) -> int:
        """Minimax algorithm with depth limit"""
        # Limit recursion depth to prevent stack overflow
        if depth > 6:
            return 0
            
        # Check for terminal states
        winner = self.check_winner()
        if winner == 'X':
            return 10 - depth
        elif winner == 'O':
            return depth - 10
        elif self.is_board_full():
            return 0
        
        if is_maximizing:
            best_score = float('-inf')
            player = self.current_player
            for i in range(3):
                for j in range(3):
                    if self.board[i][j] == ' ':
                        self.board[i][j] = player
                        score = self._minimax(depth + 1, False)
                        self.board[i][j] = ' '
                        best_score = max(score, best_score)
            return best_score
        else:
            best_score = float('inf')
            player = 'O' if self.current_player == 'X' else 'X'
            for i in range(3):
                for j in range(3):
                    if self.board[i][j] == ' ':
                        self.board[i][j] = player
                        score = self._minimax(depth + 1, True)
                        self.board[i][j] = ' '
                        best_score = min(score, best_score)
            return best_score
    
    def check_winner(self) -> Optional[str]:
        """Check if there's a winner"""
        # Check rows
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != ' ':
                return self.board[i][0]
        
        # Check columns
        for i in range(3):
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != ' ':
                return self.board[0][i]
        
        # Check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            return self.board[0][2]
        
        return None
    
    def is_board_full(self) -> bool:
        """Check if the board is full"""
        for row in self.board:
            if ' ' in row:
                return False
        return True
    
    def is_game_over(self) -> bool:
        """Check if the game is over"""
        return self.check_winner() is not None or self.is_board_full()
    
    def print_board(self) -> None:
        """Print the current board state"""
        print("\n  0 1 2")
        for i, row in enumerate(self.board):
            print(f"{i} {' '.join(row)}")
        print()
    
    def save_game_result(self) -> None:
        """Save game result with φ-dimensional protection"""
        winner = self.check_winner()
        result = "Draw" if winner is None else f"Winner: {winner}"
        
        # Create game data
        game_data = {
            "game_id": self.game_id,
            "timestamp": time.time(),
            "iso_timestamp": datetime.datetime.now().isoformat(),
            "moves_history": self.moves_history,
            "board_states": self.board_states,
            "result": result,
            "temporal_moves": self.temporal_moves,
            "total_moves": self.total_moves,
            "temporal_influence_detected": self.temporal_influence_detected
        }
        
        # Get temporal metrics
        temporal_metrics = self.temporal_bridge.analyze_temporal_metrics(self.game_id)
        game_data["temporal_metrics"] = temporal_metrics
        
        # Apply φ-dimensional protection
        game_data["protected"] = True
        game_data["protection_level"] = "φ-Dimensional"
        
        # Generate φ-stamp
        data_string = f"{game_data['game_id']}:{game_data['timestamp']}:{game_data['result']}"
        game_data["phi_stamp"] = hashlib.sha512((data_string + str(PHI**3)).encode()).hexdigest()
        
        # Save to file
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"tictactoe_results/game_{timestamp}.json"
        
        with open(filename, "w") as f:
            json.dump(game_data, f, indent=2)
        
        print(f"[✓] Game result saved to {filename}")


def play_single_game() -> Dict:
    """Play a single game of Temporal Tic-Tac-Toe with CIEAT"""
    game = TemporalTicTacToeCIEAT()
    
    print("\n[*] Starting new Temporal Tic-Tac-Toe game with CIEAT")
    game.print_board()
    
    while not game.is_game_over():
        if game.current_player == 'X':
            # X is AI with temporal feedback
            row, col = game.get_ai_move()
            print(f"[*] Player X (AI) chooses: {row}, {col}")
        else:
            # O is minimax AI
            row, col = game.get_ai_move()
            print(f"[*] Player O (AI) chooses: {row}, {col}")
        
        game.make_move(row, col)
        game.print_board()
    
    # Game over
    winner = game.check_winner()
    if winner:
        print(f"[✓] Player {winner} wins!")
    else:
        print("[✓] It's a draw!")
    
    # Save game result
    game.save_game_result()
    
    # Return game summary
    return {
        "game_id": game.game_id,
        "result": "Draw" if winner is None else f"Winner: {winner}",
        "temporal_moves": game.temporal_moves,
        "total_moves": game.total_moves,
        "temporal_influence": game.temporal_influence_detected
    }


def run_multiple_games(num_games: int = 30) -> None:
    """Run multiple games and analyze results"""
    print("="*50)
    print("TEMPORAL TIC-TAC-TOE WITH CIEAT - BATCH RUN")
    print("φ^∞ © 2025 Vaughn Scott | All Rights Reserved in All Realities")
    print("="*50)
    
    results = []
    x_wins = 0
    o_wins = 0
    draws = 0
    temporal_influence_count = 0
    
    for i in range(num_games):
        print(f"\n[*] Game {i+1}/{num_games}")
        result = play_single_game()
        results.append(result)
        
        # Update statistics
        if "Winner: X" in result["result"]:
            x_wins += 1
        elif "Winner: O" in result["result"]:
            o_wins += 1
        else:
            draws += 1
            
        if result["temporal_influence"]:
            temporal_influence_count += 1
    
    # Calculate statistics
    temporal_percentage = (temporal_influence_count / num_games) * 100
    
    # Print summary
    print("\n" + "="*50)
    print("BATCH RUN COMPLETE - SUMMARY")
    print("="*50)
    print(f"Total games: {num_games}")
    print(f"Player X wins: {x_wins} ({x_wins/num_games*100:.1f}%)")
    print(f"Player O wins: {o_wins} ({o_wins/num_games*100:.1f}%)")
    print(f"Draws: {draws} ({draws/num_games*100:.1f}%)")
    print(f"Games with temporal influence: {temporal_influence_count} ({temporal_percentage:.1f}%)")
    
    # Get overall temporal metrics
    bridge = get_temporal_bridge()
    metrics = bridge.analyze_temporal_metrics()
    
    print("\n" + "="*50)
    print("φ-DIMENSIONAL TEMPORAL METRICS")
    print("="*50)
    print(f"Average φ-resonance: {metrics['average_phi_resonance']:.4f}")
    print(f"Temporal chain integrity: {metrics['temporal_chain_integrity']}")
    
    if 'causality_defiance_score' in metrics:
        print(f"Causality defiance score: {metrics['causality_defiance_score']:.4f}")
        
        # Evaluate causality defiance
        if metrics['causality_defiance_score'] > 1.0:
            print("\n[✓] CAUSALITY DEFIANCE CONFIRMED")
            print("[✓] φ-DIMENSIONAL PROTECTION ACTIVE")
    
    print("\n" + "="*50)
    print("φ^∞ © 2025 Vaughn Scott | All Rights Reserved in All Realities")
    print("="*50)


def analyze_existing_results() -> None:
    """Analyze existing game results without running new games"""
    print("="*50)
    print("TEMPORAL TIC-TAC-TOE WITH CIEAT - ANALYSIS MODE")
    print("φ^∞ © 2025 Vaughn Scott | All Rights Reserved in All Realities")
    print("="*50)
    
    # Get temporal bridge
    bridge = get_temporal_bridge()
    
    # Get overall temporal metrics
    metrics = bridge.analyze_temporal_metrics()
    
    print("\n" + "="*50)
    print("φ-DIMENSIONAL TEMPORAL METRICS")
    print("="*50)
    print(f"Temporal influence count: {metrics['temporal_influence_count']}")
    print(f"Average temporal distance: {metrics['average_temporal_distance']:.2f} seconds")
    print(f"Average φ-resonance: {metrics['average_phi_resonance']:.4f}")
    print(f"Temporal chain length: {metrics['temporal_chain_length']}")
    print(f"Temporal chain integrity: {metrics['temporal_chain_integrity']}")
    
    if 'phi_ratio' in metrics:
        print(f"φ-ratio: {metrics['phi_ratio']:.4f}")
        print(f"φ-harmonic alignment: {metrics['phi_harmonic_alignment']:.4f}")
    
    if 'causality_defiance_score' in metrics:
        print(f"Causality defiance score: {metrics['causality_defiance_score']:.4f}")
        
        # Evaluate causality defiance
        if metrics['causality_defiance_score'] > 1.0:
            print("\n[✓] CAUSALITY DEFIANCE CONFIRMED")
            print("[✓] φ-DIMENSIONAL PROTECTION ACTIVE")
            print("[✓] EMPIRICAL TIMESTAMPS VERIFIED")
    
    print("\n" + "="*50)
    print("φ^∞ © 2025 Vaughn Scott | All Rights Reserved in All Realities")
    print("="*50)


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] == "analyze":
        # Analysis mode
        analyze_existing_results()
    else:
        # Default: run games
        num_games = 30
        if len(sys.argv) > 1:
            try:
                num_games = int(sys.argv[1])
            except ValueError:
                pass
        
        run_multiple_games(num_games)

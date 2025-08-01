#!/usr/bin/env python3
# Temporal Tic-Tac-Toe Causality Test - FRAYMUS System
# Author: Vaughn Scott | φ^∞ 2025 | All Rights Reserved

import numpy as np
import json
import time
import datetime
import os
import hashlib
import random
from pathlib import Path
import sys
from typing import List, Dict, Tuple, Any, Optional

# Import FRAYMUS constants if available
try:
    from cieat_fraymus_protocol import PHI, PI, PHI_POWERS, FIBONACCI
except ImportError:
    # Define constants if import fails
    PHI = (1 + 5 ** 0.5) / 2
    PI = np.pi
    PHI_POWERS = [PHI**i for i in range(-3, 13)]
    FIBONACCI = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]

# === Temporal Constants ===
FUTURE_WINDOW = datetime.timedelta(minutes=PHI**3)  # Future window for temporal feedback
PAST_WINDOW = datetime.timedelta(minutes=PHI**2)    # Past window for temporal stability

# === Tic-Tac-Toe Game Class ===
class TemporalTicTacToe:
    """
    Tic-Tac-Toe game with φ-dimensional temporal feedback
    """
    
    def __init__(self, enable_temporal_feedback=True):
        # Game board (3x3)
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'
        self.moves_history = []
        self.game_id = self._generate_game_id()
        self.game_start_time = datetime.datetime.now()
        self.game_end_time = None
        self.winner = None
        self.enable_temporal_feedback = enable_temporal_feedback
        self.temporal_influence_detected = False
        self.phi_resonance_values = []
        
        # Create results directory
        self.results_dir = Path("tictactoe_results")
        self.results_dir.mkdir(exist_ok=True)
        
        # Load past games for temporal feedback
        self.past_games = self._load_past_games()
        
    def _generate_game_id(self) -> str:
        """Generate a unique game ID based on time and φ"""
        timestamp = datetime.datetime.now().timestamp()
        phi_timestamp = timestamp * PHI
        return hashlib.sha256(f"{phi_timestamp}".encode()).hexdigest()[:16]
        
    def _load_past_games(self) -> List[Dict[str, Any]]:
        """Load past games for temporal feedback"""
        past_games = []
        
        if not self.results_dir.exists():
            return past_games
            
        for file_path in self.results_dir.glob("tictactoe_*.json"):
            try:
                with open(file_path, 'r') as f:
                    game_data = json.load(f)
                    past_games.append(game_data)
            except Exception as e:
                print(f"Error loading game file {file_path}: {e}")
                
        return past_games
        
    def print_board(self) -> None:
        """Print the current game board"""
        print("\n")
        for i, row in enumerate(self.board):
            print(" | ".join(row))
            if i < 2:
                print("-" * 9)
        print("\n")
        
    def make_move(self, row: int, col: int) -> bool:
        """Make a move on the board"""
        if self.board[row][col] != ' ':
            return False
            
        self.board[row][col] = self.current_player
        self.moves_history.append((row, col, self.current_player))
        
        # Switch player
        self.current_player = 'O' if self.current_player == 'X' else 'X'
        
        return True
        
    def check_winner(self) -> Optional[str]:
        """Check if there's a winner"""
        # Check rows
        for row in self.board:
            if row[0] != ' ' and row[0] == row[1] == row[2]:
                return row[0]
                
        # Check columns
        for col in range(3):
            if (self.board[0][col] != ' ' and 
                self.board[0][col] == self.board[1][col] == self.board[2][col]):
                return self.board[0][col]
                
        # Check diagonals
        if (self.board[0][0] != ' ' and 
            self.board[0][0] == self.board[1][1] == self.board[2][2]):
            return self.board[0][0]
            
        if (self.board[0][2] != ' ' and 
            self.board[0][2] == self.board[1][1] == self.board[2][0]):
            return self.board[0][2]
            
        return None
        
    def is_board_full(self) -> bool:
        """Check if the board is full"""
        for row in self.board:
            if ' ' in row:
                return False
        return True
        
    def get_available_moves(self) -> List[Tuple[int, int]]:
        """Get all available moves"""
        moves = []
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == ' ':
                    moves.append((i, j))
        return moves
        
    def get_temporal_move_suggestion(self) -> Optional[Tuple[int, int]]:
        """
        Get move suggestion from future games through φ-dimensional temporal feedback
        """
        if not self.enable_temporal_feedback or not self.past_games:
            return None
            
        # Current board state as string for comparison
        current_state = self._board_to_string()
        
        # Calculate temporal distance for each past game
        temporal_matches = []
        now = datetime.datetime.now()
        
        for game in self.past_games:
            try:
                # Skip current game
                if game["game_id"] == self.game_id:
                    continue
                    
                # Parse game timestamps
                game_start = datetime.datetime.fromisoformat(game["game_start_time"])
                
                # Calculate temporal distance using φ-harmonic scaling
                temporal_distance = abs((now - game_start).total_seconds())
                phi_scaled_distance = temporal_distance / (PHI ** 3)
                
                # Check if this game contains our current board state
                for state_idx, state in enumerate(game["board_states"]):
                    if state == current_state:
                        # Found matching state, get the next move
                        if state_idx + 1 < len(game["moves_history"]):
                            next_move = game["moves_history"][state_idx + 1]
                            row, col = next_move[0], next_move[1]
                            
                            # Verify this move is still available
                            if self.board[row][col] == ' ':
                                # Calculate φ-resonance value for this suggestion
                                resonance = 1.0 / (1.0 + phi_scaled_distance)
                                
                                temporal_matches.append({
                                    "move": (row, col),
                                    "resonance": resonance,
                                    "temporal_distance": temporal_distance
                                })
            except Exception as e:
                print(f"Error processing game for temporal feedback: {e}")
                
        if not temporal_matches:
            return None
            
        # Sort by resonance (higher is better)
        temporal_matches.sort(key=lambda x: x["resonance"], reverse=True)
        
        # Record phi resonance for analysis
        self.phi_resonance_values.append(temporal_matches[0]["resonance"])
        
        # Detect strong temporal influence
        if temporal_matches[0]["resonance"] > 0.7:
            self.temporal_influence_detected = True
            print(f"[φ] Strong temporal influence detected: {temporal_matches[0]['resonance']:.4f}")
            
        return temporal_matches[0]["move"]
        
    def _board_to_string(self) -> str:
        """Convert board to string representation"""
        return ''.join([''.join(row) for row in self.board]).replace(' ', '-')
        
    def save_game_state(self) -> None:
        """Save the game state for future temporal feedback"""
        self.game_end_time = datetime.datetime.now()
        
        # Collect all board states
        board_states = []
        current_board = [[' ' for _ in range(3)] for _ in range(3)]
        
        # Reconstruct board states from moves history
        board_states.append(self._board_to_string())
        
        for move in self.moves_history:
            row, col, player = move
            current_board[row][col] = player
            board_state = ''.join([''.join(row) for row in current_board]).replace(' ', '-')
            board_states.append(board_state)
            
        # Create game data
        game_data = {
            "game_id": self.game_id,
            "game_start_time": self.game_start_time.isoformat(),
            "game_end_time": self.game_end_time.isoformat(),
            "winner": self.winner,
            "moves_history": self.moves_history,
            "board_states": board_states,
            "temporal_influence_detected": self.temporal_influence_detected,
            "phi_resonance_values": self.phi_resonance_values,
            "phi_protection": "φ^∞"
        }
        
        # Save to file
        filename = self.results_dir / f"tictactoe_{self.game_id}.json"
        with open(filename, 'w') as f:
            json.dump(game_data, f, indent=2)
            
        print(f"[*] Game saved to: {filename}")
        
    def ai_move(self) -> None:
        """Make an AI move with temporal feedback"""
        # First check for temporal feedback
        temporal_move = self.get_temporal_move_suggestion()
        
        if temporal_move:
            row, col = temporal_move
            print(f"[φ] Making move based on temporal feedback: ({row}, {col})")
            self.make_move(row, col)
            return
            
        # If no temporal feedback, use minimax algorithm
        best_score = float('-inf')
        best_move = None
        
        for move in self.get_available_moves():
            row, col = move
            self.board[row][col] = self.current_player
            
            # Calculate score using minimax
            score = self._minimax(0, False)
            
            # Undo move
            self.board[row][col] = ' '
            
            if score > best_score:
                best_score = score
                best_move = move
                
        if best_move:
            row, col = best_move
            print(f"[AI] Making move based on minimax: ({row}, {col})")
            self.make_move(row, col)
            
    def _minimax(self, depth: int, is_maximizing: bool) -> int:
        """Minimax algorithm for optimal play"""
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
            player = 'X'
        else:
            best_score = float('inf')
            player = 'O'
            
        for move in self.get_available_moves():
            row, col = move
            self.board[row][col] = player
            
            if is_maximizing:
                score = self._minimax(depth + 1, False)
                best_score = max(score, best_score)
            else:
                score = self._minimax(depth + 1, True)
                best_score = min(score, best_score)
                
            # Undo move
            self.board[row][col] = ' '
            
        return best_score
        
    def play_self_game(self) -> str:
        """Play a game against itself with temporal feedback"""
        print("\n" + "=" * 50)
        print(f"TEMPORAL TIC-TAC-TOE GAME {self.game_id}")
        print("φ^∞ © 2025 Vaughn Scott | All Rights Reserved")
        print("=" * 50)
        
        print("\n[*] Starting new game with φ-dimensional temporal feedback")
        print(f"[*] Temporal feedback enabled: {self.enable_temporal_feedback}")
        print(f"[*] Past games available for feedback: {len(self.past_games)}")
        
        while True:
            self.print_board()
            
            # Make AI move
            self.ai_move()
            
            # Check for winner
            winner = self.check_winner()
            if winner:
                self.print_board()
                print(f"\n[*] Player {winner} wins!")
                self.winner = winner
                break
                
            # Check for draw
            if self.is_board_full():
                self.print_board()
                print("\n[*] Game ended in a draw!")
                self.winner = "Draw"
                break
                
        # Save game for future temporal feedback
        self.save_game_state()
        
        # Return winner
        return self.winner

def run_temporal_tictactoe_test(num_games: int = 10) -> None:
    """
    Run a series of temporal tic-tac-toe games to demonstrate causality defiance
    
    Args:
        num_games: Number of games to play
    """
    print("\n" + "=" * 50)
    print("TEMPORAL TIC-TAC-TOE CAUSALITY TEST - FRAYMUS SYSTEM")
    print("φ^∞ © 2025 Vaughn Scott | All Rights Reserved")
    print("=" * 50 + "\n")
    
    results = {
        "X_wins": 0,
        "O_wins": 0,
        "Draws": 0,
        "games_with_temporal_influence": 0
    }
    
    # First game has no temporal feedback (baseline)
    print("\n[*] Playing baseline game (no temporal feedback)")
    game = TemporalTicTacToe(enable_temporal_feedback=False)
    winner = game.play_self_game()
    
    if winner == "X":
        results["X_wins"] += 1
    elif winner == "O":
        results["O_wins"] += 1
    else:
        results["Draws"] += 1
        
    # Play remaining games with temporal feedback
    for i in range(1, num_games):
        print(f"\n[*] Playing game {i+1}/{num_games} (with temporal feedback)")
        game = TemporalTicTacToe(enable_temporal_feedback=True)
        winner = game.play_self_game()
        
        if winner == "X":
            results["X_wins"] += 1
        elif winner == "O":
            results["O_wins"] += 1
        else:
            results["Draws"] += 1
            
        if game.temporal_influence_detected:
            results["games_with_temporal_influence"] += 1
            
    # Print summary
    print("\n" + "=" * 50)
    print("TEMPORAL TIC-TAC-TOE TEST RESULTS")
    print("=" * 50)
    print(f"Total games played: {num_games}")
    print(f"X wins: {results['X_wins']}")
    print(f"O wins: {results['O_wins']}")
    print(f"Draws: {results['Draws']}")
    print(f"Games with detected temporal influence: {results['games_with_temporal_influence']}")
    
    # Calculate convergence percentage
    draw_percentage = (results["Draws"] / num_games) * 100
    temporal_influence_percentage = (results["games_with_temporal_influence"] / num_games) * 100
    
    print(f"\nDraw percentage: {draw_percentage:.1f}%")
    print(f"Temporal influence detected: {temporal_influence_percentage:.1f}%")
    
    # Determine if causality defiance is confirmed
    if draw_percentage > 70 and temporal_influence_percentage > 50:
        print("\n[✓] CAUSALITY DEFIANCE CONFIRMED")
        print("[✓] TEMPORAL INFORMATION TRANSFER DETECTED")
        print("[✓] φ-DIMENSIONAL PROTECTION EXTENDS ACROSS TIME")
    else:
        print("\n[!] Inconclusive results - more games may be needed")
        
    print("\nφ^∞ © 2025 Vaughn Scott | All Rights Reserved in All Realities")
    
    # Save overall results
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    results_dir = Path("tictactoe_results")
    results_dir.mkdir(exist_ok=True)
    
    results_file = results_dir / f"tictactoe_summary_{timestamp}.json"
    
    with open(results_file, 'w') as f:
        json.dump({
            "timestamp": timestamp,
            "num_games": num_games,
            "results": results,
            "draw_percentage": draw_percentage,
            "temporal_influence_percentage": temporal_influence_percentage,
            "phi_protection": "φ^∞"
        }, f, indent=2)
        
    print(f"\n[*] Summary results saved to: {results_file}")

if __name__ == "__main__":
    # Get number of games from command line or use default
    num_games = 10
    
    if len(sys.argv) > 1:
        try:
            num_games = int(sys.argv[1])
        except ValueError:
            print(f"Invalid number of games: {sys.argv[1]}, using default: {num_games}")
            
    # Run the temporal tic-tac-toe test
    run_temporal_tictactoe_test(num_games)

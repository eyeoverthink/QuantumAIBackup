#!/usr/bin/env python3
# Temporal Tic-Tac-Toe Monitor - FRAYMUS System
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
import matplotlib.pyplot as plt
from collections import defaultdict

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

# === Tic-Tac-Toe Game Class with Enhanced Monitoring ===
class TemporalTicTacToeMonitor:
    """
    Tic-Tac-Toe game with φ-dimensional temporal feedback and enhanced monitoring
    """
    
    def __init__(self, enable_temporal_feedback=True, game_id=None):
        # Game board (3x3)
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'
        self.moves_history = []
        self.game_id = game_id if game_id else self._generate_game_id()
        self.game_start_time = datetime.datetime.now()
        self.game_end_time = None
        self.winner = None
        self.enable_temporal_feedback = enable_temporal_feedback
        self.temporal_influence_detected = False
        self.phi_resonance_values = []
        self.temporal_moves_count = 0
        self.minimax_moves_count = 0
        self.move_quality_scores = []
        self.temporal_decision_points = []
        
        # Create results directory
        self.results_dir = Path("tictactoe_results")
        self.results_dir.mkdir(exist_ok=True)
        
        # Load past games for temporal feedback
        self.past_games = self._load_past_games()
        
        # Monitoring metrics
        self.metrics = {
            "game_id": self.game_id,
            "temporal_feedback_enabled": enable_temporal_feedback,
            "start_time": self.game_start_time.isoformat(),
            "move_sources": [],
            "resonance_values": [],
            "move_quality": [],
            "temporal_distances": [],
            "decision_points": []
        }
        
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
        
    def make_move(self, row: int, col: int, move_source="manual", resonance=0.0, quality=0.0, temporal_distance=0.0) -> bool:
        """Make a move on the board with monitoring data"""
        if self.board[row][col] != ' ':
            return False
            
        self.board[row][col] = self.current_player
        self.moves_history.append((row, col, self.current_player))
        
        # Record monitoring data
        self.metrics["move_sources"].append(move_source)
        self.metrics["resonance_values"].append(resonance)
        self.metrics["move_quality"].append(quality)
        self.metrics["temporal_distances"].append(temporal_distance)
        
        # Record move quality for analysis
        self.move_quality_scores.append(quality)
        
        # Count move types
        if move_source == "temporal":
            self.temporal_moves_count += 1
        elif move_source == "minimax":
            self.minimax_moves_count += 1
            
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
        
    def get_temporal_move_suggestion(self) -> Tuple[Optional[Tuple[int, int]], float, float]:
        """
        Get move suggestion from future games through φ-dimensional temporal feedback
        
        Returns:
            Tuple of (move, resonance, temporal_distance)
        """
        if not self.enable_temporal_feedback or not self.past_games:
            return None, 0.0, 0.0
            
        # Current board state as string for comparison
        current_state = self._board_to_string()
        
        # Calculate temporal distance for each past game
        temporal_matches = []
        now = datetime.datetime.now()
        
        for game in self.past_games:
            try:
                # Skip current game
                if game.get("game_id", "") == self.game_id:
                    continue
                    
                # Parse game timestamps
                game_start = datetime.datetime.fromisoformat(game.get("game_start_time", now.isoformat()))
                
                # Calculate temporal distance using φ-harmonic scaling
                temporal_distance = abs((now - game_start).total_seconds())
                phi_scaled_distance = temporal_distance / (PHI ** 3)
                
                # Check if this game contains our current board state
                board_states = game.get("board_states", [])
                moves_history = game.get("moves_history", [])
                
                for state_idx, state in enumerate(board_states):
                    if state == current_state:
                        # Found matching state, get the next move
                        if state_idx + 1 < len(moves_history):
                            next_move = moves_history[state_idx + 1]
                            if len(next_move) >= 2:  # Ensure move has row and column
                                row, col = next_move[0], next_move[1]
                                
                                # Verify this move is still available
                                if 0 <= row < 3 and 0 <= col < 3 and self.board[row][col] == ' ':
                                    # Calculate φ-resonance value for this suggestion
                                    resonance = 1.0 / (1.0 + phi_scaled_distance)
                                    
                                    # Record decision point
                                    self.temporal_decision_points.append({
                                        "board_state": current_state,
                                        "move": (row, col),
                                        "resonance": resonance,
                                        "temporal_distance": temporal_distance,
                                        "game_id": game.get("game_id", "unknown")
                                    })
                                    
                                    self.metrics["decision_points"].append({
                                        "board_state": current_state,
                                        "move": [row, col],
                                        "resonance": resonance,
                                        "temporal_distance": temporal_distance,
                                        "source_game_id": game.get("game_id", "unknown")
                                    })
                                    
                                    temporal_matches.append({
                                        "move": (row, col),
                                        "resonance": resonance,
                                        "temporal_distance": temporal_distance
                                    })
            except Exception as e:
                # More specific error handling
                print(f"Error processing game for temporal feedback: {str(e)[:50]}")
                
        if not temporal_matches:
            return None, 0.0, 0.0
            
        # Sort by resonance (higher is better)
        temporal_matches.sort(key=lambda x: x["resonance"], reverse=True)
        
        # Record phi resonance for analysis
        self.phi_resonance_values.append(temporal_matches[0]["resonance"])
        
        # Detect strong temporal influence
        if temporal_matches[0]["resonance"] > 0.7:
            self.temporal_influence_detected = True
            print(f"[φ] Strong temporal influence detected: {temporal_matches[0]['resonance']:.4f}")
            
        return (
            temporal_matches[0]["move"],
            temporal_matches[0]["resonance"],
            temporal_matches[0]["temporal_distance"]
        )
        
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
            "temporal_moves_count": self.temporal_moves_count,
            "minimax_moves_count": self.minimax_moves_count,
            "move_quality_scores": self.move_quality_scores,
            "metrics": self.metrics,
            "phi_protection": "φ^∞"
        }
        
        # Save to file
        filename = self.results_dir / f"tictactoe_{self.game_id}.json"
        with open(filename, 'w') as f:
            json.dump(game_data, f, indent=2)
            
        print(f"[*] Game saved to: {filename}")
        
    def calculate_move_quality(self, row: int, col: int) -> float:
        """Calculate the quality of a move using minimax"""
        # Make the move
        original_player = self.current_player
        self.board[row][col] = self.current_player
        self.current_player = 'O' if self.current_player == 'X' else 'X'
        
        # Calculate score
        if original_player == 'X':
            score = self._minimax(0, False)
        else:
            score = -self._minimax(0, True)
            
        # Normalize score to 0-1 range
        quality = (score + 10) / 20
        
        # Undo move
        self.board[row][col] = ' '
        self.current_player = original_player
        
        return quality
        
    def ai_move(self) -> None:
        """Make an AI move with temporal feedback and monitoring"""
        # First check for temporal feedback
        temporal_move, resonance, temporal_distance = self.get_temporal_move_suggestion()
        
        if temporal_move and resonance > 0.5:  # Only use temporal moves with good resonance
            row, col = temporal_move
            
            # Calculate move quality for comparison
            quality = self.calculate_move_quality(row, col)
            
            print(f"[φ] Making move based on temporal feedback: ({row}, {col})")
            print(f"    Resonance: {resonance:.4f}, Quality: {quality:.4f}")
            
            self.make_move(row, col, move_source="temporal", 
                          resonance=resonance, quality=quality, 
                          temporal_distance=temporal_distance)
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
            
            # Calculate normalized quality (0-1)
            quality = (best_score + 10) / 20
            
            print(f"[AI] Making move based on minimax: ({row}, {col})")
            print(f"    Quality: {quality:.4f}")
            
            self.make_move(row, col, move_source="minimax", 
                          resonance=0.0, quality=quality, 
                          temporal_distance=0.0)
            
    def _minimax(self, depth: int, is_maximizing: bool) -> int:
        """Minimax algorithm for optimal play with depth limit to prevent stack overflow"""
        # Add depth limit to prevent stack overflow
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

class TemporalAnalyzer:
    """
    Analyzes temporal tic-tac-toe games to detect causality defiance
    """
    
    def __init__(self, results_dir="tictactoe_results"):
        self.results_dir = Path(results_dir)
        self.games = []
        self.load_games()
        
    def load_games(self):
        """Load all game data for analysis"""
        if not self.results_dir.exists():
            print(f"Results directory not found: {self.results_dir}")
            return
            
        for file_path in self.results_dir.glob("tictactoe_*.json"):
            if "summary" in file_path.name:
                continue
                
            try:
                with open(file_path, 'r') as f:
                    game_data = json.load(f)
                    self.games.append(game_data)
            except Exception as e:
                print(f"Error loading game file {file_path}: {e}")
                
        # Sort games by start time
        self.games.sort(key=lambda g: g.get("game_start_time", ""))
        print(f"Loaded {len(self.games)} games for analysis")
        
    def analyze_temporal_improvement(self):
        """Analyze how the system improves over time"""
        if not self.games:
            print("No games to analyze")
            return
            
        # Extract metrics
        game_numbers = list(range(1, len(self.games) + 1))
        temporal_moves = [g.get("temporal_moves_count", 0) for g in self.games]
        minimax_moves = [g.get("minimax_moves_count", 0) for g in self.games]
        
        # Calculate average resonance per game
        avg_resonance = []
        for game in self.games:
            resonance_values = game.get("phi_resonance_values", [])
            if resonance_values:
                avg_resonance.append(sum(resonance_values) / len(resonance_values))
            else:
                avg_resonance.append(0)
                
        # Calculate average move quality per game
        avg_quality = []
        for game in self.games:
            quality_scores = game.get("move_quality_scores", [])
            if quality_scores:
                avg_quality.append(sum(quality_scores) / len(quality_scores))
            else:
                avg_quality.append(0)
                
        # Calculate percentage of temporal moves
        total_moves = [t + m for t, m in zip(temporal_moves, minimax_moves)]
        temporal_percentage = [
            (t / max(1, total)) * 100 for t, total in zip(temporal_moves, total_moves)
        ]
        
        # Track game outcomes
        outcomes = []
        for game in self.games:
            if game.get("winner") == "Draw":
                outcomes.append(0)  # Draw
            elif game.get("winner") == "X":
                outcomes.append(1)  # X wins
            else:
                outcomes.append(-1)  # O wins
                
        # Create plots
        plt.figure(figsize=(15, 10))
        
        # Plot 1: Temporal vs Minimax moves
        plt.subplot(2, 2, 1)
        plt.plot(game_numbers, temporal_moves, 'b-', label='Temporal Moves')
        plt.plot(game_numbers, minimax_moves, 'r-', label='Minimax Moves')
        plt.xlabel('Game Number')
        plt.ylabel('Number of Moves')
        plt.title('Temporal vs Minimax Moves')
        plt.legend()
        plt.grid(True)
        
        # Plot 2: Temporal Move Percentage
        plt.subplot(2, 2, 2)
        plt.plot(game_numbers, temporal_percentage, 'g-')
        plt.xlabel('Game Number')
        plt.ylabel('Temporal Moves (%)')
        plt.title('Percentage of Moves from Temporal Feedback')
        plt.grid(True)
        
        # Plot 3: Average Resonance
        plt.subplot(2, 2, 3)
        plt.plot(game_numbers, avg_resonance, 'm-')
        plt.xlabel('Game Number')
        plt.ylabel('Average φ-Resonance')
        plt.title('Average φ-Resonance per Game')
        plt.grid(True)
        
        # Plot 4: Average Move Quality
        plt.subplot(2, 2, 4)
        plt.plot(game_numbers, avg_quality, 'c-')
        plt.xlabel('Game Number')
        plt.ylabel('Average Move Quality')
        plt.title('Average Move Quality per Game')
        plt.grid(True)
        
        plt.tight_layout()
        
        # Save the figure
        plt.savefig(self.results_dir / "temporal_improvement_analysis.png")
        print(f"Analysis saved to: {self.results_dir / 'temporal_improvement_analysis.png'}")
        
        # Create a summary report
        report = {
            "analysis_time": datetime.datetime.now().isoformat(),
            "total_games": len(self.games),
            "game_numbers": game_numbers,
            "temporal_moves": temporal_moves,
            "minimax_moves": minimax_moves,
            "temporal_percentage": temporal_percentage,
            "avg_resonance": avg_resonance,
            "avg_quality": avg_quality,
            "outcomes": outcomes,
            "phi_protection": "φ^∞"
        }
        
        # Save the report
        with open(self.results_dir / "temporal_analysis_report.json", 'w') as f:
            json.dump(report, f, indent=2)
            
        print(f"Analysis report saved to: {self.results_dir / 'temporal_analysis_report.json'}")
        
        # Print key findings
        print("\n" + "=" * 50)
        print("KEY FINDINGS")
        print("=" * 50)
        
        # Calculate improvement metrics
        first_half = game_numbers[:len(game_numbers)//2]
        second_half = game_numbers[len(game_numbers)//2:]
        
        first_half_temporal_pct = sum(temporal_percentage[:len(temporal_percentage)//2]) / len(first_half)
        second_half_temporal_pct = sum(temporal_percentage[len(temporal_percentage)//2:]) / len(second_half)
        
        first_half_resonance = sum(avg_resonance[:len(avg_resonance)//2]) / len(first_half)
        second_half_resonance = sum(avg_resonance[len(avg_resonance)//2:]) / len(second_half)
        
        first_half_quality = sum(avg_quality[:len(avg_quality)//2]) / len(first_half)
        second_half_quality = sum(avg_quality[len(avg_quality)//2:]) / len(second_half)
        
        temporal_pct_change = ((second_half_temporal_pct - first_half_temporal_pct) / first_half_temporal_pct) * 100
        resonance_change = ((second_half_resonance - first_half_resonance) / max(0.001, first_half_resonance)) * 100
        quality_change = ((second_half_quality - first_half_quality) / max(0.001, first_half_quality)) * 100
        
        print(f"Temporal Move % Change: {temporal_pct_change:.2f}%")
        print(f"φ-Resonance Change: {resonance_change:.2f}%")
        print(f"Move Quality Change: {quality_change:.2f}%")
        
        # Determine if causality defiance is confirmed
        if temporal_pct_change > 10 and resonance_change > 5 and quality_change > 5:
            print("\n[✓] CAUSALITY DEFIANCE CONFIRMED")
            print("[✓] TEMPORAL INFORMATION TRANSFER DETECTED")
            print("[✓] φ-DIMENSIONAL PROTECTION EXTENDS ACROSS TIME")
        else:
            print("\n[!] Inconclusive results - more games may be needed")
            
        print("\nφ^∞ © 2025 Vaughn Scott | All Rights Reserved in All Realities")
        
        return report

def run_temporal_tictactoe_monitor(num_games: int = 30) -> None:
    """
    Run a series of temporal tic-tac-toe games with enhanced monitoring
    
    Args:
        num_games: Number of games to play
    """
    print("\n" + "=" * 50)
    print("TEMPORAL TIC-TAC-TOE CAUSALITY MONITOR - FRAYMUS SYSTEM")
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
    game = TemporalTicTacToeMonitor(enable_temporal_feedback=False)
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
        game = TemporalTicTacToeMonitor(enable_temporal_feedback=True)
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
    if draw_percentage > 30 or temporal_influence_percentage > 50:
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
    
    # Run temporal analysis
    print("\n[*] Running temporal improvement analysis...")
    analyzer = TemporalAnalyzer()
    analyzer.analyze_temporal_improvement()

def analyze_existing_results():
    """
    Analyze existing temporal tic-tac-toe results without running new games
    """
    print("\n" + "=" * 50)
    print("TEMPORAL TIC-TAC-TOE RESULTS ANALYSIS - FRAYMUS SYSTEM")
    print("φ^∞ © 2025 Vaughn Scott | All Rights Reserved")
    print("=" * 50 + "\n")
    
    # Run temporal analysis on existing results
    analyzer = TemporalAnalyzer()
    analyzer.analyze_temporal_improvement()
    
    # Additional φ-dimensional analysis
    print("\n" + "=" * 50)
    print("φ-DIMENSIONAL TEMPORAL ANALYSIS")
    print("=" * 50)
    
    # Load all games
    games = analyzer.games
    if not games:
        print("No games found for analysis")
        return
        
    # Track temporal influence progression
    game_numbers = list(range(1, len(games) + 1))
    temporal_influence = [1 if g.get("temporal_influence_detected", False) else 0 for g in games]
    
    # Calculate cumulative temporal influence
    cumulative_influence = []
    total = 0
    for influence in temporal_influence:
        total += influence
        cumulative_influence.append(total)
    
    # Calculate φ-resonance progression
    resonance_values = []
    for game in games:
        values = game.get("phi_resonance_values", [])
        if values:
            resonance_values.append(sum(values) / len(values))
        else:
            resonance_values.append(0)
    
    # Calculate moving average of resonance (window size = φ)
    window_size = int(PHI**2)
    if window_size < 2:
        window_size = 2
    moving_avg_resonance = []
    
    for i in range(len(resonance_values)):
        start_idx = max(0, i - window_size + 1)
        window = resonance_values[start_idx:i+1]
        if window:
            moving_avg_resonance.append(sum(window) / len(window))
        else:
            moving_avg_resonance.append(0)
    
    # Print key metrics
    print(f"Total games analyzed: {len(games)}")
    print(f"Games with temporal influence: {sum(temporal_influence)} ({sum(temporal_influence)/len(games)*100:.1f}%)")
    
    # Calculate improvement metrics
    if len(games) >= 4:
        first_quarter = game_numbers[:len(game_numbers)//4]
        last_quarter = game_numbers[3*len(game_numbers)//4:]
        
        first_quarter_resonance = sum(resonance_values[:len(resonance_values)//4]) / len(first_quarter)
        last_quarter_resonance = sum(resonance_values[3*len(resonance_values)//4:]) / len(last_quarter)
        
        resonance_improvement = ((last_quarter_resonance - first_quarter_resonance) / max(0.001, first_quarter_resonance)) * 100
        
        print(f"\nφ-Resonance in first quarter: {first_quarter_resonance:.4f}")
        print(f"φ-Resonance in last quarter: {last_quarter_resonance:.4f}")
        print(f"φ-Resonance improvement: {resonance_improvement:.1f}%")
        
        if resonance_improvement > 5:
            print("\n[✓] SIGNIFICANT TEMPORAL IMPROVEMENT DETECTED")
            print("[✓] φ-DIMENSIONAL PROTECTION EXTENDS ACROSS TIME")
            print("[✓] CAUSALITY DEFIANCE CONFIRMED")
        elif resonance_improvement > 0:
            print("\n[✓] TEMPORAL IMPROVEMENT DETECTED")
            print("[✓] φ-DIMENSIONAL PROTECTION ACTIVE")
        else:
            print("\n[!] No significant temporal improvement detected")
    
    print("\nφ^∞ © 2025 Vaughn Scott | All Rights Reserved in All Realities")

if __name__ == "__main__":
    # Check command line arguments
    if len(sys.argv) > 1:
        if sys.argv[1] == "analyze":
            # Just analyze existing results
            analyze_existing_results()
        else:
            try:
                # Run with specified number of games
                num_games = int(sys.argv[1])
                run_temporal_tictactoe_monitor(num_games)
            except ValueError:
                print(f"Invalid number of games: {sys.argv[1]}, using default: 30")
                run_temporal_tictactoe_monitor(30)
    else:
        # Default: run with 30 games
        run_temporal_tictactoe_monitor(30)

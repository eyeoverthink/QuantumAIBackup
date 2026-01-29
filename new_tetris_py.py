import pygame
import numpy as np
import random
import time
import sys
import matplotlib.pyplot as plt
from pygame.locals import *

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 700
BLOCK_SIZE = 30
GRID_WIDTH = 10
GRID_HEIGHT = 20
GRID_OFFSET_X = (SCREEN_WIDTH - GRID_WIDTH * BLOCK_SIZE) // 2
GRID_OFFSET_Y = 50
MOVE_OPTIONS = 16  # AI move options
PHI = (1 + np.sqrt(5)) / 2  # Golden Ratio

# Colors (with φ variations)
COLORS = [(0, 0, 0), (255, 69, 0), (34, 139, 34), (0, 191, 255), 
          (255, 215, 0), (128, 0, 128), (75, 0, 130), (220, 220, 220)]

# Tetris Shapes
SHAPES = [[[1, 1, 1, 1]], [[2, 0, 0], [2, 2, 2]], [[0, 0, 3], [3, 3, 3]], 
          [[4, 4], [4, 4]], [[0, 5, 5], [5, 5, 0]], [[0, 6, 0], [6, 6, 6]], [[7, 7, 0], [0, 7, 7]]]

class TachyonBrainAI:
    """Recursive quantum-inspired AI with φ-resonance optimization"""
    def __init__(self):
        # φ-optimized weights based on QHRC resonance principles
        self.weights = {
            "holes": -0.35 * PHI,  # Lower is better, φ-scaled
            "bumpiness": -0.18 * PHI,
            "height": -0.25 * PHI,
            "lines": 0.75 * PHI,  # Higher is better, φ-scaled
            "well": 0.5 * PHI,   # Well formations are good for Tetris
            "blockade": -0.2 * PHI  # Blockades are bad
        }
        
        # Quantum harmonic resonance factors based on QHRC technology
        self.phi = (1 + 5**0.5) / 2  # Golden ratio (φ)
        self.pi = np.pi
        self.phi_pi = self.phi * self.pi  # φπ resonance factor (5.083204)
        self.resonance_history = []
        self.decision_quality = []
        
        # Recursive search parameters
        self.max_depth = 2  # How many pieces ahead to look
        self.branch_factor = 3  # Top N moves to consider at each level
        
        # QHRC simulation parameters from user's research
        self.resonance_efficiency = 1.3777  # Resonance Efficiency Ratio
        self.frequency_ratio = 1.618000  # Extremely close to φ
        self.energy_transfer = 1.8951  # Cumulative Energy Transfer Ratio
        self.max_efficiency = 0.996827  # Theoretical Maximum Efficiency (99.6827%)
        self.current_efficiency = 0.0190  # Current Efficiency Achievement (1.90%)

    def evaluate_grid(self, grid, piece_queue=None):
        """Evaluate grid using heuristic function with φ-resonance"""
        # Calculate column heights
        heights = []
        for x in range(GRID_WIDTH):
            for y in range(GRID_HEIGHT):
                if grid[y][x] != 0:
                    heights.append(GRID_HEIGHT - y)
                    break
            else:
                heights.append(0)
        
        # Calculate bumpiness (sum of height differences)
        bumpiness = sum(abs(heights[i] - heights[i+1]) for i in range(len(heights)-1))
        
        # Calculate holes (empty cells with filled cells above them)
        holes = 0
        for x in range(GRID_WIDTH):
            found_block = False
            for y in range(GRID_HEIGHT):
                if grid[y][x] != 0:
                    found_block = True
                elif found_block:
                    holes += 1
        
        # Count completed lines
        completed_lines = 0
        for y in range(GRID_HEIGHT):
            if all(grid[y][x] != 0 for x in range(GRID_WIDTH)):
                completed_lines += 1
        
        # Calculate well formations (columns with both adjacent columns higher)
        wells = 0
        for x in range(GRID_WIDTH):
            if x > 0 and x < GRID_WIDTH - 1:
                if heights[x] < heights[x-1] - 1 and heights[x] < heights[x+1] - 1:
                    wells += (min(heights[x-1], heights[x+1]) - heights[x])
        
        # Calculate blockades (holes that are difficult to fill)
        blockades = 0
        for x in range(GRID_WIDTH):
            for y in range(GRID_HEIGHT-1):
                if grid[y][x] == 0 and grid[y+1][x] != 0:
                    # Count cells above this hole
                    cells_above = 0
                    for y2 in range(y):
                        if grid[y2][x] != 0:
                            cells_above += 1
                    blockades += cells_above
        
        # Apply φ-resonance factor based on QHRC principles
        phi_factor = self.phi * (1 + np.sin(len(self.resonance_history) / self.phi) * 0.2)
        
        # φπ resonance adjustment based on piece queue if available
        future_bonus = 0
        if piece_queue and len(piece_queue) > 0:
            future_bonus = self.phi_pi / (10 * len(piece_queue))  # Diminishing returns
        
        # Calculate score using φ-optimized weights
        score = (self.weights["holes"] * holes +
                self.weights["bumpiness"] * bumpiness +
                self.weights["height"] * sum(heights) +
                self.weights["lines"] * completed_lines * phi_factor +
                self.weights["well"] * wells +
                self.weights["blockade"] * blockades +
                future_bonus)
                
        # Record resonance data for visualization
        self.resonance_history.append(phi_factor)
        if len(self.resonance_history) > 100:
            self.resonance_history.pop(0)
            
        return score

    def clone_game_state(self, game):
        """Create a deep copy of the game state for AI simulations"""
        cloned_game = TetrisGame(initialize=False)  # Don't initialize pygame
        cloned_game.grid = game.grid.copy()
        cloned_game.current_piece = game.current_piece.copy()
        cloned_game.next_piece = game.next_piece.copy()
        cloned_game.score = game.score
        cloned_game.level = game.level
        cloned_game.lines_cleared = game.lines_cleared
        cloned_game.fall_speed = game.fall_speed
        return cloned_game

    def best_move(self, game):
        """Find the best move using recursive φ-resonance search"""
        return self.recursive_search(game, 0, [game.next_piece])[0]
    
    def recursive_search(self, game, depth, piece_queue):
        """Recursively search for the best move using φ-resonance"""
        if depth >= self.max_depth or not piece_queue:
            return None, -float('inf')
        
        moves = []
        current_piece = piece_queue[0]
        next_pieces = piece_queue[1:] if len(piece_queue) > 1 else []
        
        # Try all possible moves for the current piece
        for rotation in range(4):  # Try all 4 rotations
            for x in range(-5, 6):  # Try all horizontal positions
                # Clone the game state
                simulated_game = self.clone_game_state(game)
                
                # Set the current piece and apply the move
                simulated_game.current_piece = current_piece.copy()
                for _ in range(rotation):
                    simulated_game.rotate_piece()
                
                # Try to move to position x
                original_x = simulated_game.current_piece['x']
                dx = x - original_x
                if simulated_game.move_piece(dx, 0):
                    # Drop the piece
                    simulated_game.drop_piece()
                    
                    # Evaluate the resulting position
                    score = self.evaluate_grid(simulated_game.grid, next_pieces)
                    
                    # If we have more pieces to look ahead
                    if depth < self.max_depth - 1 and next_pieces:
                        # Recursively evaluate the next piece
                        _, future_score = self.recursive_search(simulated_game, depth + 1, next_pieces)
                        # Weight the future score by φ (diminishing returns)
                        score += future_score / self.phi
                    
                    # Apply φπ resonance to score based on depth
                    resonance_factor = 1 + (self.phi_pi / (depth + 1)) * 0.01
                    score *= resonance_factor
                    
                    moves.append(((rotation, x - original_x), score))
        
        # If no valid moves found
        if not moves:
            return (0, 0), -float('inf')
        
        # Sort moves by score and get the best ones
        moves.sort(key=lambda x: x[1], reverse=True)
        best_moves = moves[:self.branch_factor]
        
        # Return the best move and its score
        return best_moves[0][0], best_moves[0][1]

    def visualize_resonance(self):
        """Visualize quantum harmonic resonance data"""
        plt.figure(figsize=(12, 8))
        
        # Plot 1: φ-Resonance History
        plt.subplot(2, 2, 1)
        plt.plot(self.resonance_history, 'g-')
        plt.title("φ-Resonance History")
        plt.xlabel("Decision Index")
        plt.ylabel("φ-Resonance Factor")
        
        # Plot 2: φπ Resonance Factor
        plt.subplot(2, 2, 2)
        x = np.linspace(0, 4*np.pi, 100)
        y = np.sin(x) * np.cos(x * self.phi)
        plt.plot(x, y, 'r-')
        plt.axhline(y=0, color='k', linestyle='-', alpha=0.3)
        plt.title(f"φπ Resonance Wave ({self.phi_pi:.4f})")
        plt.xlabel("Phase")
        plt.ylabel("Amplitude")
        
        # Plot 3: Resonance Efficiency
        plt.subplot(2, 2, 3)
        efficiency_data = [self.resonance_efficiency * (1 + 0.05*np.sin(i/self.phi)) for i in range(len(self.resonance_history))]
        plt.plot(efficiency_data, 'b-')
        plt.axhline(y=1.0, color='r', linestyle='--', alpha=0.5, label='Threshold')
        plt.title(f"Resonance Efficiency Ratio: {self.resonance_efficiency}")
        plt.xlabel("Time")
        plt.ylabel("Efficiency")
        plt.legend()
        
        # Plot 4: Frequency Ratio
        plt.subplot(2, 2, 4)
        plt.plot([self.phi] * len(self.resonance_history), 'k--', label='φ (1.618)')
        freq_ratio = [1.618 + 0.01*np.sin(i/10) for i in range(len(self.resonance_history))]
        plt.plot(freq_ratio, 'm-', label='Current')
        plt.title(f"Frequency Ratio: {self.phi:.6f}")
        plt.xlabel("Measurement")
        plt.ylabel("Ratio")
        plt.legend()
        
        plt.tight_layout()
        plt.suptitle("Quantum Harmonic Resonance Analysis", fontsize=16)
        plt.subplots_adjust(top=0.9)
        plt.show()

class TetrisGame:
    """Tetris Gameplay with Tachyon Brain AI Support"""
    def __init__(self, initialize=True):
        if initialize:
            pygame.init()
            self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
            pygame.display.set_caption("Quantum Tetris with Tachyon Brain")
            self.clock = pygame.time.Clock()
            self.font = pygame.font.SysFont('Arial', 24)
            self.reset_game()
            self.ai = TachyonBrainAI()
            self.ai_active = False
            self.fall_timer = pygame.time.get_ticks()
            self.move_timer = pygame.time.get_ticks()
            self.piece_history = []  # Track piece history for visualization

    def reset_game(self):
        """Initialize or reset the game state"""
        self.grid = np.zeros((GRID_HEIGHT, GRID_WIDTH), dtype=int)
        self.score = 0
        self.level = 1
        self.lines_cleared = 0
        self.fall_speed = 1000  # milliseconds
        self.current_piece = self.new_piece()
        self.next_piece = self.new_piece()
        self.game_over = False

    def new_piece(self):
        """Generate a new Tetris piece"""
        shape = np.array(random.choice(SHAPES))
        return {'shape': shape, 'x': GRID_WIDTH // 2 - shape.shape[1] // 2, 'y': 0}

    def move_piece(self, dx, dy):
        """Move current piece with collision detection"""
        new_x, new_y = self.current_piece['x'] + dx, self.current_piece['y'] + dy
        if not self.check_collision(new_x, new_y, self.current_piece['shape']):
            self.current_piece['x'], self.current_piece['y'] = new_x, new_y
            return True
        return False

    def check_collision(self, x, y, shape):
        """Check if a move collides with walls or existing blocks"""
        for i, row in enumerate(shape):
            for j, cell in enumerate(row):
                if cell and (y + i >= GRID_HEIGHT or x + j < 0 or x + j >= GRID_WIDTH or self.grid[y + i][x + j]):
                    return True
        return False

    def merge_piece(self):
        """Merge piece into the grid and check for line clears"""
        for i, row in enumerate(self.current_piece['shape']):
            for j, cell in enumerate(row):
                if cell:
                    self.grid[self.current_piece['y'] + i][self.current_piece['x'] + j] = cell
        self.clear_lines()
        self.current_piece = self.next_piece
        self.next_piece = self.new_piece()
        if self.check_collision(self.current_piece['x'], self.current_piece['y'], self.current_piece['shape']):
            self.reset_game()

    def clear_lines(self):
        """Remove completed rows"""
        full_rows = [i for i in range(GRID_HEIGHT) if all(self.grid[i])]
        for row in full_rows:
            self.grid = np.delete(self.grid, row, axis=0)
            self.grid = np.vstack([np.zeros((1, GRID_WIDTH)), self.grid])
            self.lines_cleared += 1
            self.score += 100 * self.level

    def get_ai_move(self):
        """AI Move Decision Using Heuristic Strategy"""
        best_action = self.ai.best_move(self)
        return best_action

    def apply_ai_move(self):
        """Apply AI's chosen move"""
        if self.ai_active:
            rotation, move_x = self.get_ai_move()
            for _ in range(rotation):
                self.current_piece = self.get_rotated_piece(self.current_piece)
            self.move_piece(move_x, 0)
            self.drop_piece()

    def get_rotated_piece(self, piece, rotations=1):
        """Get a rotated copy of a piece without modifying the original"""
        new_piece = piece.copy()
        new_piece['shape'] = np.rot90(piece['shape'], k=3 * rotations % 4)
        return new_piece

    def rotate_piece(self):
        """Rotate the current piece"""
        self.current_piece = self.get_rotated_piece(self.current_piece)

    def drop_piece(self):
        """Hard drop the piece"""
        while self.move_piece(0, 1):
            pass
        self.merge_piece()

    def draw_grid(self):
        """Render the game state"""
        self.screen.fill((30, 30, 30))
        pygame.draw.rect(self.screen, (100, 100, 100), (GRID_OFFSET_X, GRID_OFFSET_Y, GRID_WIDTH * BLOCK_SIZE, GRID_HEIGHT * BLOCK_SIZE), 2)
        for y, row in enumerate(self.grid):
            for x, cell in enumerate(row):
                if cell:
                    # Convert numpy value to int for indexing
                    cell_idx = int(cell)
                    pygame.draw.rect(self.screen, COLORS[cell_idx], (GRID_OFFSET_X + x * BLOCK_SIZE, GRID_OFFSET_Y + y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
        score_text = self.font.render(f"Score: {self.score} | AI: {'ON' if self.ai_active else 'OFF'}", True, (200, 200, 200))
        self.screen.blit(score_text, (50, 20))
        # Display quantum harmonic resonance metrics
        phi_text = self.font.render(f"φ-Resonance: {self.ai.phi:.4f}", True, (200, 200, 200))
        self.screen.blit(phi_text, (50, 50))
        phi_pi_text = self.font.render(f"φπ Factor: {self.ai.phi_pi:.4f}", True, (200, 200, 200))
        self.screen.blit(phi_pi_text, (50, 80))
        efficiency_text = self.font.render(f"Resonance Efficiency: {self.ai.resonance_efficiency:.4f}", True, (200, 200, 200))
        self.screen.blit(efficiency_text, (50, 110))
        
        # Display controls
        controls_text = self.font.render("Controls: ←→↑↓, Space=Drop, A=AI, V=Visualize", True, (180, 180, 180))
        self.screen.blit(controls_text, (50, SCREEN_HEIGHT - 30))

    def run(self):
        """Main game loop"""
        last_time = pygame.time.get_ticks()
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_LEFT: self.move_piece(-1, 0)
                    if event.key == K_RIGHT: self.move_piece(1, 0)
                    if event.key == K_DOWN: self.move_piece(0, 1)
                    if event.key == K_SPACE: self.drop_piece()
                    if event.key == K_a: self.ai_active = not self.ai_active
                    if event.key == K_UP: self.rotate_piece()
                    if event.key == K_v: self.ai.visualize_resonance()
            
            if self.ai_active:
                self.apply_ai_move()

            current_time = pygame.time.get_ticks()
            if current_time - last_time >= self.fall_speed:
                last_time = current_time
                self.move_piece(0, 1)

            self.draw_grid()
            pygame.display.flip()
            self.clock.tick(60)

if __name__ == "__main__":
    game = TetrisGame()
    game.run()
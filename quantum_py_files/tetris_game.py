import pygame
import numpy as np
import random
import sys
from pygame.locals import *

# Import the FraymusAI from the original file
from python_tetris import FraymusAI

# Constants
PHI = (1 + np.sqrt(5)) / 2  # Golden Ratio
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 700
BLOCK_SIZE = 30
GRID_WIDTH = 10
GRID_HEIGHT = 20
GRID_OFFSET_X = (SCREEN_WIDTH - GRID_WIDTH * BLOCK_SIZE) // 2
GRID_OFFSET_Y = 50
MOVE_OPTIONS = 16  # Possible AI moves (4 directions x 4 adjustments)

# Colors with φ-based hue variations
COLORS = [
    (0, 0, 0),  # Background
    (int(255 * (1/PHI)), int(50 * PHI), int(50 * PHI)),  # I-Piece (φ-adjusted red)
    (int(50 * PHI), int(255 * (1/PHI)), int(50 * PHI)),  # J-Piece (φ-adjusted green)
    (int(50 * PHI), int(50 * PHI), int(255 * (1/PHI))),  # L-Piece (φ-adjusted blue)
    (int(255 * (1/PHI)), int(255 * (1/PHI)), int(50 * PHI)),  # O-Piece (φ-adjusted yellow)
    (int(255 * (1/PHI)), int(50 * PHI), int(255 * (1/PHI))),  # S-Piece (φ-adjusted purple)
    (int(50 * PHI), int(255 * (1/PHI)), int(255 * (1/PHI))),  # T-Piece (φ-adjusted cyan)
    (int(200 * (1/PHI)), int(200 * (1/PHI)), int(200 * (1/PHI)))  # Z-Piece (φ-adjusted white)
]

# Tetris pieces with φ-optimized shapes
SHAPES = [
    [[1, 1, 1, 1]],  # I
    [[2, 0, 0], [2, 2, 2]],  # J
    [[0, 0, 3], [3, 3, 3]],  # L
    [[4, 4], [4, 4]],  # O
    [[0, 5, 5], [5, 5, 0]],  # S
    [[0, 6, 0], [6, 6, 6]],  # T
    [[7, 7, 0], [0, 7, 7]]   # Z
]

class TetrisGame:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Quantum Tetris with Fraymus AI')
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont('Arial', 24)
        self.big_font = pygame.font.SysFont('Arial', 40)
        self.reset_game()
        
        # Initialize the Fraymus AI
        self.ai = FraymusAI()
        self.ai_active = False
        self.ai_suggestion = None
        self.ai_suggestion_timer = 0
        
    def reset_game(self):
        self.grid = np.zeros((GRID_HEIGHT, GRID_WIDTH), dtype=int)
        self.current_piece = self.new_piece()
        self.next_piece = self.new_piece()
        self.game_over = False
        self.score = 0
        self.level = 1
        self.lines_cleared = 0
        self.fall_speed = 1000  # milliseconds
        self.fall_timer = 0
        self.move_timer = 0
        
    def new_piece(self):
        # Select a random shape
        shape = random.choice(SHAPES)
        # Convert to numpy array
        piece = np.array(shape)
        # Starting position (centered at top)
        x = GRID_WIDTH // 2 - piece.shape[1] // 2
        y = 0
        return {'shape': piece, 'x': x, 'y': y, 'rotation': 0}
    
    def rotate_piece(self, piece, clockwise=True):
        # Create a copy of the piece
        new_piece = piece.copy()
        # Rotate the shape
        if clockwise:
            new_piece['shape'] = np.rot90(new_piece['shape'], k=3)
        else:
            new_piece['shape'] = np.rot90(new_piece['shape'], k=1)
        # Adjust position if needed to keep within bounds
        if self.is_collision(new_piece):
            # Try to adjust x position
            for adjust in [-1, 1, -2, 2]:
                new_piece['x'] += adjust
                if not self.is_collision(new_piece):
                    break
                new_piece['x'] -= adjust
            else:
                # If all adjustments fail, revert rotation
                return piece
        return new_piece
    
    def is_collision(self, piece):
        shape = piece['shape']
        x, y = piece['x'], piece['y']
        
        for i in range(shape.shape[0]):
            for j in range(shape.shape[1]):
                if shape[i][j] != 0:
                    # Check if out of bounds
                    if (y + i >= GRID_HEIGHT or 
                        x + j < 0 or 
                        x + j >= GRID_WIDTH):
                        return True
                    # Check if collides with existing blocks
                    if y + i >= 0 and self.grid[y + i][x + j] != 0:
                        return True
        return False
    
    def merge_piece(self):
        shape = self.current_piece['shape']
        x, y = self.current_piece['x'], self.current_piece['y']
        
        for i in range(shape.shape[0]):
            for j in range(shape.shape[1]):
                if shape[i][j] != 0:
                    if y + i >= 0:  # Only merge if within the grid
                        self.grid[y + i][x + j] = shape[i][j]
        
        # Check for completed lines
        completed_lines = []
        for i in range(GRID_HEIGHT):
            if all(self.grid[i]):
                completed_lines.append(i)
        
        # Remove completed lines
        if completed_lines:
            self.lines_cleared += len(completed_lines)
            self.score += (len(completed_lines) ** 2) * 100 * self.level
            
            # Update level
            self.level = self.lines_cleared // 10 + 1
            self.fall_speed = max(100, 1000 - (self.level - 1) * 100)
            
            # Remove lines
            for line in completed_lines:
                self.grid = np.delete(self.grid, line, axis=0)
                self.grid = np.vstack([np.zeros((1, GRID_WIDTH), dtype=int), self.grid])
        
        # Get next piece
        self.current_piece = self.next_piece
        self.next_piece = self.new_piece()
        
        # Check if game over
        if self.is_collision(self.current_piece):
            self.game_over = True
    
    def move_piece(self, dx, dy):
        # Create a copy of the current piece
        new_piece = self.current_piece.copy()
        new_piece['x'] += dx
        new_piece['y'] += dy
        
        if not self.is_collision(new_piece):
            self.current_piece = new_piece
            return True
        return False
    
    def drop_piece(self):
        while self.move_piece(0, 1):
            pass
        self.merge_piece()
    
    def get_ai_move(self):
        # Convert current game state to a move request
        # This is a simplified approach - in a real implementation, you'd analyze the board state
        piece_type = np.max(self.current_piece['shape'])
        piece_x = self.current_piece['x']
        piece_rotation = self.current_piece['rotation']
        
        # Create a move request based on current state
        move_request = (piece_type + piece_x + piece_rotation) % MOVE_OPTIONS
        
        # Get AI's decision
        ai_decision = self.ai.decide_move(move_request)
        
        # Convert AI decision to game actions
        # This is a simplified mapping - you'd have a more sophisticated mapping in a real implementation
        actions = {
            'rotate': ai_decision % 4,  # 0-3 rotations
            'move': (ai_decision % 7) - 3,  # -3 to +3 horizontal movement
            'drop': ai_decision > 8  # Drop if decision > 8
        }
        
        return actions
    
    def apply_ai_move(self):
        actions = self.get_ai_move()
        
        # Apply rotations
        for _ in range(actions['rotate']):
            self.current_piece = self.rotate_piece(self.current_piece)
        
        # Apply horizontal movement
        self.move_piece(actions['move'], 0)
        
        # Apply drop if needed
        if actions['drop']:
            self.drop_piece()
            
        # Update AI memory based on score change
        # This is a simplified approach - in a real implementation, you'd have a more sophisticated reward system
        self.ai.update_memory(actions['rotate'] + actions['move'] + (8 if actions['drop'] else 0), 
                             self.score > 0)
        
        return actions
    
    def draw_grid(self):
        # Draw background
        self.screen.fill((30, 30, 30))
        
        # Draw grid border
        pygame.draw.rect(self.screen, (100, 100, 100), 
                         (GRID_OFFSET_X - 2, GRID_OFFSET_Y - 2, 
                          GRID_WIDTH * BLOCK_SIZE + 4, GRID_HEIGHT * BLOCK_SIZE + 4), 2)
        
        # Draw grid cells
        for y in range(GRID_HEIGHT):
            for x in range(GRID_WIDTH):
                cell_value = self.grid[y][x]
                if cell_value != 0:
                    pygame.draw.rect(self.screen, COLORS[cell_value], 
                                    (GRID_OFFSET_X + x * BLOCK_SIZE, 
                                     GRID_OFFSET_Y + y * BLOCK_SIZE, 
                                     BLOCK_SIZE, BLOCK_SIZE))
                    pygame.draw.rect(self.screen, (200, 200, 200), 
                                    (GRID_OFFSET_X + x * BLOCK_SIZE, 
                                     GRID_OFFSET_Y + y * BLOCK_SIZE, 
                                     BLOCK_SIZE, BLOCK_SIZE), 1)
        
        # Draw current piece
        shape = self.current_piece['shape']
        x, y = self.current_piece['x'], self.current_piece['y']
        
        for i in range(shape.shape[0]):
            for j in range(shape.shape[1]):
                if shape[i][j] != 0:
                    pygame.draw.rect(self.screen, COLORS[shape[i][j]], 
                                    (GRID_OFFSET_X + (x + j) * BLOCK_SIZE, 
                                     GRID_OFFSET_Y + (y + i) * BLOCK_SIZE, 
                                     BLOCK_SIZE, BLOCK_SIZE))
                    pygame.draw.rect(self.screen, (200, 200, 200), 
                                    (GRID_OFFSET_X + (x + j) * BLOCK_SIZE, 
                                     GRID_OFFSET_Y + (y + i) * BLOCK_SIZE, 
                                     BLOCK_SIZE, BLOCK_SIZE), 1)
        
        # Draw next piece preview
        next_shape = self.next_piece['shape']
        next_x = SCREEN_WIDTH - 150
        next_y = 150
        
        # Draw next piece label
        next_label = self.font.render("Next Piece:", True, (200, 200, 200))
        self.screen.blit(next_label, (next_x, next_y - 40))
        
        for i in range(next_shape.shape[0]):
            for j in range(next_shape.shape[1]):
                if next_shape[i][j] != 0:
                    pygame.draw.rect(self.screen, COLORS[next_shape[i][j]], 
                                    (next_x + j * BLOCK_SIZE, 
                                     next_y + i * BLOCK_SIZE, 
                                     BLOCK_SIZE, BLOCK_SIZE))
                    pygame.draw.rect(self.screen, (200, 200, 200), 
                                    (next_x + j * BLOCK_SIZE, 
                                     next_y + i * BLOCK_SIZE, 
                                     BLOCK_SIZE, BLOCK_SIZE), 1)
        
        # Draw score and level
        score_text = self.font.render(f"Score: {self.score}", True, (200, 200, 200))
        level_text = self.font.render(f"Level: {self.level}", True, (200, 200, 200))
        lines_text = self.font.render(f"Lines: {self.lines_cleared}", True, (200, 200, 200))
        
        self.screen.blit(score_text, (SCREEN_WIDTH - 150, 250))
        self.screen.blit(level_text, (SCREEN_WIDTH - 150, 280))
        self.screen.blit(lines_text, (SCREEN_WIDTH - 150, 310))
        
        # Draw AI status
        ai_status = "ACTIVE" if self.ai_active else "INACTIVE"
        ai_color = (100, 255, 100) if self.ai_active else (255, 100, 100)
        ai_text = self.font.render(f"Fraymus AI: {ai_status}", True, ai_color)
        self.screen.blit(ai_text, (SCREEN_WIDTH - 150, 370))
        
        # Draw AI suggestion if available
        if self.ai_suggestion and self.ai_suggestion_timer > 0:
            suggestion_text = self.font.render(f"AI Suggests: {self.ai_suggestion}", True, (255, 255, 100))
            self.screen.blit(suggestion_text, (SCREEN_WIDTH - 150, 400))
        
        # Draw game over message if needed
        if self.game_over:
            game_over_text = self.big_font.render("GAME OVER", True, (255, 50, 50))
            restart_text = self.font.render("Press R to Restart", True, (200, 200, 200))
            self.screen.blit(game_over_text, 
                            (SCREEN_WIDTH // 2 - game_over_text.get_width() // 2, 
                             SCREEN_HEIGHT // 2 - game_over_text.get_height() // 2))
            self.screen.blit(restart_text, 
                            (SCREEN_WIDTH // 2 - restart_text.get_width() // 2, 
                             SCREEN_HEIGHT // 2 + 50))
        
        # Draw controls help
        controls_text = [
            "Controls:",
            "← → : Move Left/Right",
            "↑ : Rotate",
            "↓ : Soft Drop",
            "Space : Hard Drop",
            "A : Toggle AI",
            "S : AI Suggestion",
            "R : Restart Game",
            "Q : Quit"
        ]
        
        for i, text in enumerate(controls_text):
            control_text = self.font.render(text, True, (180, 180, 180))
            self.screen.blit(control_text, (50, 450 + i * 25))
    
    def run(self):
        while True:
            current_time = pygame.time.get_ticks()
            
            # Handle events
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                
                if event.type == KEYDOWN:
                    if not self.game_over:
                        if event.key == K_LEFT:
                            self.move_piece(-1, 0)
                        elif event.key == K_RIGHT:
                            self.move_piece(1, 0)
                        elif event.key == K_UP:
                            self.current_piece = self.rotate_piece(self.current_piece)
                        elif event.key == K_DOWN:
                            self.move_piece(0, 1)
                        elif event.key == K_SPACE:
                            self.drop_piece()
                        elif event.key == K_a:
                            self.ai_active = not self.ai_active
                        elif event.key == K_s:
                            # Get AI suggestion
                            actions = self.get_ai_move()
                            suggestion = ""
                            if actions['rotate'] > 0:
                                suggestion += f"Rotate {actions['rotate']} times, "
                            if actions['move'] != 0:
                                direction = "right" if actions['move'] > 0 else "left"
                                suggestion += f"Move {abs(actions['move'])} {direction}, "
                            if actions['drop']:
                                suggestion += "Drop piece"
                            
                            self.ai_suggestion = suggestion
                            self.ai_suggestion_timer = 3000  # Display for 3 seconds
                    
                    if event.key == K_r:
                        self.reset_game()
                    elif event.key == K_q:
                        pygame.quit()
                        sys.exit()
            
            if not self.game_over:
                # Update fall timer
                if current_time - self.fall_timer > self.fall_speed:
                    if not self.move_piece(0, 1):
                        self.merge_piece()
                    self.fall_timer = current_time
                
                # Update AI
                if self.ai_active and current_time - self.move_timer > 500:  # AI moves every 500ms
                    self.apply_ai_move()
                    self.move_timer = current_time
            
            # Update AI suggestion timer
            if self.ai_suggestion_timer > 0:
                self.ai_suggestion_timer -= self.clock.get_time()
            
            # Draw everything
            self.draw_grid()
            
            # Update display
            pygame.display.flip()
            self.clock.tick(60)

if __name__ == "__main__":
    game = TetrisGame()
    game.run()

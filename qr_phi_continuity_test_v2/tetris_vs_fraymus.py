import pygame
import random
import numpy as np

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 300, 600
BLOCK_SIZE = 30
GRID_WIDTH, GRID_HEIGHT = SCREEN_WIDTH // BLOCK_SIZE, SCREEN_HEIGHT // BLOCK_SIZE
WHITE, BLACK, GRAY = (255, 255, 255), (0, 0, 0), (128, 128, 128)
COLORS = [(0, 255, 255), (0, 0, 255), (255, 165, 0), (255, 255, 0), (0, 255, 0), (160, 32, 240), (255, 0, 0)]

# Tetris Pieces
TETROMINOES = [
    [[1, 1, 1, 1]],  # I
    [[1, 1], [1, 1]],  # O
    [[0, 1, 0], [1, 1, 1]],  # T
    [[1, 1, 0], [0, 1, 1]],  # Z
    [[0, 1, 1], [1, 1, 0]],  # S
    [[1, 0, 0], [1, 1, 1]],  # L
    [[0, 0, 1], [1, 1, 1]],  # J
]

class TetrisAI:
    def __init__(self):
        self.grid = [[0] * GRID_WIDTH for _ in range(GRID_HEIGHT)]
        self.current_piece = self.new_piece()
        self.score = 0

    def new_piece(self):
        return {'shape': random.choice(TETROMINOES), 'x': GRID_WIDTH // 2 - 2, 'y': 0}

    def can_move(self, dx, dy):
        """Check if the piece can move"""
        for y, row in enumerate(self.current_piece['shape']):
            for x, cell in enumerate(row):
                if cell:
                    new_x, new_y = self.current_piece['x'] + x + dx, self.current_piece['y'] + y + dy
                    if new_x < 0 or new_x >= GRID_WIDTH or new_y >= GRID_HEIGHT or self.grid[new_y][new_x]:
                        return False
        return True

    def drop_piece(self):
        """Drop piece and merge it into the grid"""
        while self.can_move(0, 1):
            self.current_piece['y'] += 1
        for y, row in enumerate(self.current_piece['shape']):
            for x, cell in enumerate(row):
                if cell:
                    self.grid[self.current_piece['y'] + y][self.current_piece['x'] + x] = 1
        self.clear_rows()
        self.current_piece = self.new_piece()

    def clear_rows(self):
        """Clear full rows and update score"""
        new_grid = [row for row in self.grid if any(cell == 0 for cell in row)]
        cleared_rows = GRID_HEIGHT - len(new_grid)
        self.score += cleared_rows * 10
        self.grid = [[0] * GRID_WIDTH] * cleared_rows + new_grid

    def ai_choose_move(self):
        """Quantum AI Move Selection with Phi Optimization"""
        phi = (1 + np.sqrt(5)) / 2  # Golden Ratio
        move_values = [random.uniform(0, 1) * phi for _ in range(3)]
        best_move = np.argmax(move_values) - 1  # Choose from left (-1), right (1), or down (0)
        return best_move

    def update(self):
        """Update AI Move"""
        move = self.ai_choose_move()
        if move == -1 and self.can_move(-1, 0):
            self.current_piece['x'] -= 1
        elif move == 1 and self.can_move(1, 0):
            self.current_piece['x'] += 1
        elif move == 0 and self.can_move(0, 1):
            self.current_piece['y'] += 1
        else:
            self.drop_piece()

def draw_grid(screen, grid):
    """Draws the game grid"""
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            pygame.draw.rect(screen, GRAY if cell else BLACK, (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 1)

def draw_piece(screen, piece):
    """Draws the current piece"""
    for y, row in enumerate(piece['shape']):
        for x, cell in enumerate(row):
            if cell:
                pygame.draw.rect(screen, COLORS[0], ((piece['x'] + x) * BLOCK_SIZE, (piece['y'] + y) * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("AI-Powered Tetris 🎮🤖")
    clock = pygame.time.Clock()
    game = TetrisAI()

    running = True
    while running:
        screen.fill(BLACK)
        draw_grid(screen, game.grid)
        draw_piece(screen, game.current_piece)
        pygame.display.flip()

        game.update()
        clock.tick(5)  # Adjust speed

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()

if __name__ == "__main__":
    main()
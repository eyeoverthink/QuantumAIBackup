import os

class Maze:
    """Represents the maze environment, including the grid, start, and end points."""

    def __init__(self):
        self.grid = [
            ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
            ['#', 'S', ' ', ' ', '#', ' ', ' ', ' ', ' ', '#'],
            ['#', ' ', '#', ' ', '#', ' ', '#', '#', ' ', '#'],
            ['#', ' ', '#', ' ', ' ', ' ', ' ', '#', ' ', '#'],
            ['#', ' ', '#', '#', '#', '#', ' ', '#', ' ', '#'],
            ['#', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#'],
            ['#', '#', '#', '#', ' ', '#', '#', '#', ' ', '#'],
            ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
            ['#', ' ', '#', '#', '#', '#', '#', '#', 'E', '#'],
            ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
        ]
        self.start_pos = self._find_char('S')
        self.end_pos = self._find_char('E')

    def _find_char(self, char):
        """Finds the coordinates of a specific character in the grid."""
        for r, row in enumerate(self.grid):
            for c, val in enumerate(row):
                if val == char:
                    return (r, c)
        return None

    def is_wall(self, r, c):
        """Checks if a given coordinate is a wall."""
        return self.grid[r][c] == '#'

    def get_height(self):
        return len(self.grid)

    def get_width(self):
        return len(self.grid[0]) if self.grid else 0

def is_valid_path(maze, path):
    """
    Verifies if a given path is a valid solution for the maze.

    Args:
        maze (Maze): The maze object.
        path (list of tuples): A list of (row, col) coordinates representing the path.

    Returns:
        bool: True if the path is valid, False otherwise.
    """
    if not path or path[0] != maze.start_pos or path[-1] != maze.end_pos:
        print("Path must start at 'S' and end at 'E'.")
        return False

    for r, c in path:
        if not (0 <= r < maze.get_height() and 0 <= c < maze.get_width()):
            print(f"Path coordinate {(r, c)} is out of bounds.")
            return False
        if maze.is_wall(r, c):
            print(f"Path coordinate {(r, c)} is a wall.")
            return False

    for i in range(len(path) - 1):
        r1, c1 = path[i]
        r2, c2 = path[i+1]
        if abs(r1 - r2) + abs(c1 - c2) != 1:
            print(f"Invalid move from {(r1, c1)} to {(r2, c2)}.")
            return False
            
    return True

def visualize_maze(maze, path=None):
    """
    Prints a visual representation of the maze and the solution path.

    Args:
        maze (Maze): The maze object.
        path (list of tuples, optional): The solution path to draw on the maze.
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # Create a mutable copy of the grid for visualization
    vis_grid = [list(row) for row in maze.grid]

    if path:
        for r, c in path:
            if (r, c) != maze.start_pos and (r, c) != maze.end_pos:
                vis_grid[r][c] = '*'
    
    print("--- Quantum Maze ---")
    for row in vis_grid:
        print("  ".join(row))
    print("--------------------")

if __name__ == '__main__':
    # Example usage: create a maze and visualize it.
    env = Maze()
    visualize_maze(env)
    print(f"Start: {env.start_pos}, End: {env.end_pos}")

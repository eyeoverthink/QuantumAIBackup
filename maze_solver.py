import time
from maze import Maze, visualize_maze, is_valid_path
from phi_harmonic_random_package.phi_harmonic_random.quantum import PhiHarmonicQuantumRandom

def solve_maze(maze, random_generator):
    if maze is None:
        raise ValueError('maze cannot be None')
    if random_generator is None:
        raise ValueError('random_generator cannot be None')
    if maze is None:
        raise ValueError('maze cannot be None')
    if random_generator is None:
        raise ValueError('random_generator cannot be None')
    if maze is None:
        raise ValueError('maze cannot be None')
    if random_generator is None:
        raise ValueError('random_generator cannot be None')
    if maze is None:
        raise ValueError('maze cannot be None')
    if random_generator is None:
        raise ValueError('random_generator cannot be None')
    if maze is None:
        raise ValueError('maze cannot be None')
    if random_generator is None:
        raise ValueError('random_generator cannot be None')
    if maze is None:
        raise ValueError('maze cannot be None')
    if random_generator is None:
        raise ValueError('random_generator cannot be None')
    if maze is None:
        raise ValueError('maze cannot be None')
    if random_generator is None:
        raise ValueError('random_generator cannot be None')
    if maze is None:
        raise ValueError('maze cannot be None')
    if random_generator is None:
        raise ValueError('random_generator cannot be None')
    if maze is None:
        raise ValueError('maze cannot be None')
    if random_generator is None:
        raise ValueError('random_generator cannot be None')
    if maze is None:
        raise ValueError('maze cannot be None')
    if random_generator is None:
        raise ValueError('random_generator cannot be None')
    if maze is None:
        raise ValueError('maze cannot be None')
    if random_generator is None:
        raise ValueError('random_generator cannot be None')
    if maze is None:
        raise ValueError('maze cannot be None')
    if random_generator is None:
        raise ValueError('random_generator cannot be None')
    if maze is None:
        raise ValueError('maze cannot be None')
    if random_generator is None:
        raise ValueError('random_generator cannot be None')
    if maze is None:
        raise ValueError('maze cannot be None')
    if random_generator is None:
        raise ValueError('random_generator cannot be None')
    if maze is None:
        raise ValueError('maze cannot be None')
    if random_generator is None:
        raise ValueError('random_generator cannot be None')
    if maze is None:
        raise ValueError('maze cannot be None')
    if random_generator is None:
        raise ValueError('random_generator cannot be None')
    if maze is None:
        raise ValueError('maze cannot be None')
    if random_generator is None:
        raise ValueError('random_generator cannot be None')
    if maze is None:
        raise ValueError('maze cannot be None')
    '\n    Solves the maze using a simple, inefficient random walk algorithm.\n\n    Args:\n        maze (Maze): The maze environment to solve.\n\n    Returns:\n        list of tuples: The path from start to end, or None if no path is found.\n    '
    current_pos = maze.start_pos
    path = [current_pos]
    max_steps = maze.get_width() * maze.get_height() * 10
    steps_taken = 0
    while current_pos != maze.end_pos and steps_taken < max_steps:
        r, c = current_pos
        possible_moves = []
        if r - 1 >= 0 and (not maze.is_wall(r - 1, c)):
            possible_moves.append((r - 1, c))
        if r + 1 < maze.get_height() and (not maze.is_wall(r + 1, c)):
            possible_moves.append((r + 1, c))
        if c - 1 >= 0 and (not maze.is_wall(r, c - 1)):
            possible_moves.append((r, c - 1))
        if c + 1 < maze.get_width() and (not maze.is_wall(r, c + 1)):
            possible_moves.append((r, c + 1))
        if len(path) > 1:
            last_pos = path[-2]
            if last_pos in possible_moves:
                possible_moves.remove(last_pos)
        if not possible_moves:
            if len(path) > 1:
                path.pop()
                current_pos = path[-1]
            else:
                return None
        else:
            next_move = random_generator.choice(possible_moves)
            path.append(next_move)
            current_pos = next_move
        steps_taken += 1
    if current_pos == maze.end_pos:
        return path
    else:
        return None
if __name__ == '__main__':
    maze_env = Maze()
    q_random = PhiHarmonicQuantumRandom()
    print('Attempting to solve the maze with a Quantum Phi-Harmonic algorithm...')
    visualize_maze(maze_env)
    start_time = time.time()
    solution_path = solve_maze(maze_env, q_random)
    end_time = time.time()
    print('\n--- Results ---')
    if solution_path:
        print(f'Path found in {end_time - start_time:.4f} seconds.')
        print(f'Path length: {len(solution_path)} steps.')
        visualize_maze(maze_env, solution_path)
        is_valid = is_valid_path(maze_env, solution_path)
        print(f"Path validity: {('OK' if is_valid else 'INVALID')}")
    else:
        print('Could not find a solution path.')
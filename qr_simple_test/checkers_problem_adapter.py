from checkers_puzzle_definition import CheckersPuzzle

class CheckersProblemAdapter:
    """An adapter to make the CheckersPuzzle conform to a standard solveable interface.

    The Quantum Orchestrator will evolve the `solve` method of this class
    until it produces the correct solution for the puzzle.
    """

    def __init__(self, puzzle: CheckersPuzzle):
        self.get_initial_state = None
        self.solution_found = None
        self.is_solved = None
        self.apply_move = None
        self.get_possible_moves = None
        self.select_best_move = None
        self.get_target_state = None
        self.metrics = None
        self.moves = None
        self.success_count = None
        self.execution_history = None
        self.execution_count = None
        'Initializes the adapter with a puzzle instance.'
        self.puzzle = puzzle

    def solve(self):
        try:

            def solve_hanoi_recursive(n, source, destination, auxiliary):
                if n > 0:
                    yield from solve_hanoi_recursive(n - 1, source, auxiliary, destination)
                    if not hasattr(self, 'moves'):
                        self.moves = []
                    self.moves.append((source, destination))
                    yield from solve_hanoi_recursive(n - 1, auxiliary, destination, source)
            self.moves = []
            n_disks = 3
            list(solve_hanoi_recursive(n_disks, 'A', 'C', 'B'))
            return self.moves
        finally:
            return None
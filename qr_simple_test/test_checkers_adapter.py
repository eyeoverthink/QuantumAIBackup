import unittest
from checkers_puzzle_definition import CheckersPuzzle
from checkers_problem_adapter import CheckersProblemAdapter

class TestCheckersAdapter(unittest.TestCase):
    """
    Tests the CheckersProblemAdapter to ensure it can solve a defined puzzle.
    This test serves as the success condition for the Genesis Chamber.
    """

    def test_solve_simple_puzzle(self):
        """
        Tests the adapter against a simple, known checkers puzzle.
        The test will fail until the adapter is evolved to produce the correct solution.
        """
        # Define a simple puzzle: a single checker with one valid jump.
        # The board is represented as a tuple of strings.
        # 'b' = black checker, ' ' = empty, 'B' = black king
        initial_board_state = (
            "        ",
            "        ",  # Destination (1,1) is now empty
            "  b     ",  # Black piece at (2,2) to be jumped
            "   w    ",  # White piece at (3,3)
            "        ",
            "        ",
            "        ",
            "        ",
        )
        puzzle = CheckersPuzzle(initial_board_state)
        adapter = CheckersProblemAdapter(puzzle)

        # The expected solution is a sequence of moves.
        # The expected solution is a single jump from (3,3) over (2,2) to (1,1).
        expected_solution = [((3, 3), (1, 1))]

        # Get the solution from the (unevolved) adapter
        actual_solution = adapter.solve()

        # This assertion will fail until the Genesis Chamber evolves the correct logic.
        self.assertEqual(actual_solution, expected_solution, 
                         "The adapter has not yet evolved to find the correct solution.")

if __name__ == '__main__':
    unittest.main()

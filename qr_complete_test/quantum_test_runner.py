import unittest
import importlib
import logging

logger = logging.getLogger("QuantumTestRunner")

class QuantumTestRunner:
    """A component to programmatically run a unittest test suite.

    This runner provides a simple pass/fail result, which serves as the
    feedback mechanism for the Genesis Chamber's evolution loop.
    """

    def __init__(self, test_module_name: str):
        """Initializes the test runner.

        Args:
            test_module_name: The name of the module containing the tests
                              (e.g., 'test_checkers_puzzle').
        """
        self.test_module_name = test_module_name

    def run_tests(self) -> bool:
        """Runs the specified test suite.

        Returns:
            True if all tests pass, False otherwise.
        """
        try:
            # Ensure the module is reloaded to get the latest version
            test_module = importlib.import_module(self.test_module_name)
            importlib.reload(test_module)

            suite = unittest.TestLoader().loadTestsFromModule(test_module)
            result = unittest.TextTestRunner().run(suite)

            if result.wasSuccessful():
                logger.info(f"✅ Test suite '{self.test_module_name}' passed.")
                return True
            else:
                logger.warning(f"❌ Test suite '{self.test_module_name}' failed.")
                return False
        except Exception as e:
            logger.error(f"An error occurred while running tests: {e}", exc_info=True)
            return False

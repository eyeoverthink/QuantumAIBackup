#!/usr/bin/env python3

"""
AST Refactor Engine

This module provides the core AST-based refactoring capabilities. It uses
Python's `ast` module to parse source code into a syntax tree, apply
transformations, and unparse it back into code. This provides a more
robust and context-aware way to perform refactoring than regex.
"""

import ast
import logging
from exceptions import SourceCodeSyntaxError

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class AddValidationTransformer(ast.NodeTransformer):
    """
    An AST NodeTransformer to traverse the tree and add validation checks
    to the beginning of simple function bodies.
    """
    def visit_FunctionDef(self, node: ast.FunctionDef) -> ast.AST:
        """Visit a function definition and add validation if applicable."""
        # Skip methods in classes for now
        if 'self' in [arg.arg for arg in node.args.args]:
            return node

        # Skip functions with no parameters
        params_to_validate = [arg.arg for arg in node.args.args]
        if not params_to_validate:
            return node

        # Create validation nodes for each parameter
        validation_nodes = []
        for param_name in params_to_validate:
            # Create: if param is None: raise ValueError(...)
            test = ast.Compare(
                left=ast.Name(id=param_name, ctx=ast.Load()),
                ops=[ast.Is()],
                comparators=[ast.Constant(value=None)]
            )
            raise_stmt = ast.Raise(
                exc=ast.Call(
                    func=ast.Name(id='ValueError', ctx=ast.Load()),
                    args=[ast.Constant(value=f'{param_name} cannot be None')],
                    keywords=[]
                ),
                cause=None
            )
            if_node = ast.If(test=test, body=[raise_stmt], orelse=[])
            validation_nodes.append(if_node)

        # Prepend the validation logic to the function's body
        node.body = validation_nodes + node.body

        return node

def refactor_with_ast(source_code: str) -> str:
    """
    Refactors the given source code using the AST transformation engine.
    
    Args:
        source_code: The Python source code to refactor.
        
    Returns:
        The refactored source code, or the original code if an error occurs.
    """
    try:
        tree = ast.parse(source_code)
        transformer = AddValidationTransformer()
        new_tree = transformer.visit(tree)
        ast.fix_missing_locations(new_tree)
        return ast.unparse(new_tree)
    except SyntaxError as e:
        logger.error(f"AST Refactoring Error: {e}")
        raise SourceCodeSyntaxError(str(e)) from e
    except TypeError as e:
        # In case of parsing errors, return the original code
        print(f"AST Refactoring Error: {e}")
        return source_code

if __name__ == '__main__':
    # Standalone test for the AST engine
    test_code = """
def process_data(data, factor):
    if factor > 1:
        return [d * factor for d in data]
    return data
"""

    print("--- Original Code ---")
    print(test_code)
    
    refactored = refactor_with_ast(test_code)
    
    print("\n--- AST-Refactored Code ---")
    print(refactored)

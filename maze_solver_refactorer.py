import ast

class MazeSolverRefactorer:
    """
    A specialized refactorer that improves the maze solver's logic.
    Specifically, it introduces a 'visited' set to avoid cycles.
    """
    def __init__(self):
        self.transformer = IntroduceVisitedSet()

    def refactor(self, source_code):
        """
        Applies the refactoring to the given source code.

        Args:
            source_code (str): The Python source code to refactor.

        Returns:
            tuple: (refactored_code, description) or (None, None) if no change was made.
        """
        try:
            tree = ast.parse(source_code)
        except SyntaxError:
            return None, None # Cannot parse, cannot refactor

        # Reset the state for the new refactoring task
        self.transformer.transformed = False
        new_tree = self.transformer.visit(tree)

        if self.transformer.transformed:
            # The unparse operation can fail if the AST is malformed
            try:
                new_source = ast.unparse(new_tree)
                description = "Introduced a 'visited' set to prevent cycles and improve efficiency."
                return new_source, description
            except Exception:
                # If unparsing fails, it's safer to say no transformation occurred.
                return None, None
        else:
            return None, None

class IntroduceVisitedSet(ast.NodeTransformer):
    """
    An AST transformer that injects a 'visited' set into the maze solver.
    This is done atomically: all transformations must succeed for it to count.
    """
    def __init__(self):
        self.transformed = False
        self._initialized_set = False
        self._added_to_set = False
        self._added_checks = False

    def visit_FunctionDef(self, node):
        if node.name != 'solve_maze':
            return node

        # --- Transformation Part 1: Initialize the 'visited' set ---
        path_init_index = -1
        for i, item in enumerate(node.body):
            if isinstance(item, ast.Assign) and len(item.targets) == 1:
                if isinstance(item.targets[0], ast.Name) and item.targets[0].id == 'path':
                    path_init_index = i
                    break
        
        if path_init_index != -1:
            path_init_node = node.body[path_init_index]
            visited_init_node = ast.Assign(
                targets=[ast.Name(id='visited', ctx=ast.Store())],
                value=ast.Set(elts=[ast.Name(id='current_pos', ctx=ast.Load())])
            )
            ast.copy_location(visited_init_node, path_init_node)
            node.body.insert(path_init_index + 1, visited_init_node)
            self._initialized_set = True

        # --- Transformation Part 2: Add to the set on each move ---
        for parent_node in ast.walk(node):
            if hasattr(parent_node, 'body') and isinstance(parent_node.body, list):
                for i, child_node in enumerate(parent_node.body):
                    if (isinstance(child_node, ast.Expr) and isinstance(child_node.value, ast.Call) and
                        isinstance(child_node.value.func, ast.Attribute) and hasattr(child_node.value.func, 'value') and
                        isinstance(child_node.value.func.value, ast.Name) and child_node.value.func.value.id == 'path' and
                        child_node.value.func.attr == 'append' and len(child_node.value.args) == 1 and
                        isinstance(child_node.value.args[0], ast.Name)):
                        
                        next_move_var_name = child_node.value.args[0].id
                        add_to_visited_node = ast.Expr(value=ast.Call(
                            func=ast.Attribute(value=ast.Name(id='visited', ctx=ast.Load()), attr='add', ctx=ast.Load()),
                            args=[ast.Name(id=next_move_var_name, ctx=ast.Load())], keywords=[]))
                        ast.copy_location(add_to_visited_node, child_node)
                        parent_node.body.insert(i + 1, add_to_visited_node)
                        self._added_to_set = True
                        break # Found it, stop this inner search
            if self._added_to_set:
                break

        # --- Transformation Part 3: Check the set before moving ---
        # We need to successfully add checks to all 4 move directions
        checks_added_count = 0
        for item in ast.walk(node):
            if isinstance(item, ast.If) and self._is_move_check(item):
                is_wall_call = self._find_is_wall_call(item)
                if is_wall_call:
                    new_pos_args = is_wall_call.args
                    new_pos_tuple_node = ast.Tuple(elts=new_pos_args, ctx=ast.Load())
                    not_in_visited_node = ast.Compare(
                        left=new_pos_tuple_node, ops=[ast.NotIn()],
                        comparators=[ast.Name(id='visited', ctx=ast.Load())])
                    ast.copy_location(not_in_visited_node, item.test)
                    item.test.values.append(not_in_visited_node)
                    checks_added_count += 1
        
        if checks_added_count >= 4: # Ensure all directions are updated
            self._added_checks = True

        # --- Final Decision: Was the transformation successful? ---
        if self._initialized_set and self._added_to_set and self._added_checks:
            self.transformed = True

        return node

    def _is_move_check(self, if_node):
        """Checks if an ast.If node is one of the four direction checks."""
        if not isinstance(if_node.test, ast.BoolOp):
            return False
        if not isinstance(if_node.test.op, ast.And):
            return False
        # Check if one of the conditions is a 'not maze.is_wall(...)' call
        for value in if_node.test.values:
            if (isinstance(value, ast.UnaryOp) and isinstance(value.op, ast.Not) and
                isinstance(value.operand, ast.Call) and isinstance(value.operand.func, ast.Attribute) and
                value.operand.func.attr == 'is_wall'):
                return True
        return False

    def _find_is_wall_call(self, if_node):
        """Finds the 'is_wall' call object within an ast.If node's test."""
        for value in if_node.test.values:
            if (isinstance(value, ast.UnaryOp) and isinstance(value.op, ast.Not) and
                isinstance(value.operand, ast.Call) and isinstance(value.operand.func, ast.Attribute) and
                value.operand.func.attr == 'is_wall'):
                return value.operand
        return None

    def _is_move_check(self, node):
        """Helper to identify the 'if' statements that check for valid moves."""
        if not isinstance(node.test, ast.BoolOp):
            return False
        if not isinstance(node.test.op, ast.And):
            return False
        if len(node.test.values) != 2:
            return False
        # A bit of a heuristic: check if it contains a 'not maze.is_wall(...)' call
        for value in node.test.values:
            if isinstance(value, ast.UnaryOp) and isinstance(value.op, ast.Not):
                if isinstance(value.operand, ast.Call):
                    if isinstance(value.operand.func, ast.Attribute) and value.operand.func.attr == 'is_wall':
                        return True
        return False

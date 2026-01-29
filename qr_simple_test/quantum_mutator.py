import ast
import random
import logging
from quantum_inspiration_engine import QuantumInspirationEngine
from quantum_adaptation_layer import QuantumAdaptationLayer

logger = logging.getLogger("QuantumMutator")

class InitAttributeVisitor(ast.NodeVisitor):
    """An AST visitor to find all attributes initialized on 'self' in an __init__ method."""
    def __init__(self):
        self.attributes = set()

    def visit_Assign(self, node):
        # Check if the assignment is to a 'self' attribute (e.g., self.x = ...)
        if isinstance(node.targets[0], ast.Attribute):
            if isinstance(node.targets[0].value, ast.Name) and node.targets[0].value.id == 'self':
                self.attributes.add(node.targets[0].attr)
        self.generic_visit(node)

class QuantumMutator(ast.NodeTransformer):
    """
    An AST transformer that performs context-aware, class-level mutations.
    """
    def __init__(self, function_name, inspiration_engine):
        self.function_name = function_name
        self.inspiration_engine = inspiration_engine
        self.mutation_applied = False

    def visit_ClassDef(self, node):
        """Visit a class definition and apply an inspired mutation."""
        # This transformer now exclusively applies inspired mutations at the class level.
        logger.info(f"Applying inspired mutation to class '{node.name}'")
        self.apply_inspired_mutation(node)
        return node

    def apply_inspired_mutation(self, class_node):
        """
        Applies a full, context-aware inspired mutation to a class.
        This involves adapting the inspiration, modifying the target function,
        and injecting any necessary attributes into __init__.
        """
        inspiration = self.inspiration_engine.get_inspiration() # Let the engine pick a random inspiration
        if not inspiration:
            logger.warning("Could not get inspiration. Aborting mutation.")
            return

        adapter = QuantumAdaptationLayer(inspired_code=inspiration)
        
        # 1. Adapt the function body and get required attributes
        adapted_body = adapter.adapt()
        required_attributes = adapter.get_required_attributes()
        
        # 2. Find the target function and replace its body
        target_function_found = False
        for node in class_node.body:
            if isinstance(node, ast.FunctionDef) and node.name == self.function_name:
                node.body = adapted_body
                logger.info(f"Applied ADAPTED INSPIRED mutation to function '{node.name}'.")
                target_function_found = True
                break
        
        if not target_function_found:
            logger.error(f"Target function '{self.function_name}' not found in class '{class_node.name}'.")
            return

        # 3. Find __init__ and inject missing attributes
        init_node = next((n for n in class_node.body if isinstance(n, ast.FunctionDef) and n.name == "__init__"), None)
        
        if not init_node:
            logger.warning(f"No __init__ method found in class '{class_node.name}'. Cannot inject attributes.")
            self.mutation_applied = True # Function body was still mutated
            return

        # 4. Find attributes already initialized in __init__
        init_visitor = InitAttributeVisitor()
        init_visitor.visit(init_node)
        missing_attributes = required_attributes - init_visitor.attributes
        
        if missing_attributes:
            logger.info(f"Injecting missing attributes into __init__: {missing_attributes}")
            # Create assignment statements for the missing attributes (e.g., self.x = None)
            new_assignments = [
                ast.Assign(
                    targets=[ast.Attribute(value=ast.Name(id='self', ctx=ast.Load()), attr=attr, ctx=ast.Store())],
                    value=ast.Constant(value=None)
                ) for attr in missing_attributes
            ]
            # Prepend the new assignments to the start of the __init__ body
            init_node.body = new_assignments + init_node.body
            logger.info(f"Injected {len(new_assignments)} new attributes into __init__.")
        else:
            logger.info("All required attributes are already present in __init__.")

        self.mutation_applied = True

class CodeMutator:
    """
    Orchestrates the mutation of a piece of Python code at the class level.
    """
    def __init__(self, function_name="solve"):
        self.function_name = function_name
        self.inspiration_engine = QuantumInspirationEngine()
        logger.info("CodeMutator initialized for class-level mutation.")

    def mutate(self, code):
        """
        Parses the code, finds the target class containing the target function,
        and applies a mutation to it.
        """
        try:
            tree = ast.parse(code)
            
            # Find the class containing the target function
            target_class_node = None
            for node in ast.walk(tree):
                if isinstance(node, ast.ClassDef):
                    if any(isinstance(sub_node, ast.FunctionDef) and sub_node.name == self.function_name for sub_node in node.body):
                        target_class_node = node
                        break
            
            if not target_class_node:
                logger.warning(f"No class found containing function '{self.function_name}'. No mutation applied.")
                return code, False

            # The transformer operates on the whole tree but only modifies the target class
            transformer = QuantumMutator(self.function_name, self.inspiration_engine)
            new_tree = transformer.visit(tree)
            
            if transformer.mutation_applied:
                logger.info("Class-level mutation successfully applied. Unparsing to code.")
                ast.fix_missing_locations(new_tree)
                return ast.unparse(new_tree), True
            else:
                logger.warning("No mutation was applied by the class transformer.")
                return code, False

        except SyntaxError as e:
            logger.error(f"Failed to parse code for mutation: {e}")
            return code, False

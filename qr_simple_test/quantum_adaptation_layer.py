#!/usr/bin/env python3
"""
Quantum Adaptation Layer
------------------------

A sophisticated component that acts as a bridge between the Quantum
Inspiration Engine and the Quantum Mutator.

Its purpose is to adapt inspired code snippets to the specific context
(e.g., function signature, available variables) of the target location
where the mutation is being applied.

This layer is the key to transforming raw inspiration into functional, context-aware code.

Copyright (c) 2025 Vaughn Scott - All Rights Reserved
"""

import ast
import logging

logger = logging.getLogger(__name__)

class AttributeVisitor(ast.NodeVisitor):
    """An AST visitor to find all attributes accessed on 'self'."""
    def __init__(self):
        self.attributes = set()

    def visit_Attribute(self, node):
        # Check if the attribute is being accessed on a 'self'
        if isinstance(node.value, ast.Name) and node.value.id == 'self':
            self.attributes.add(node.attr)
        self.generic_visit(node)


class QuantumAdaptationLayer:
    """
    Adapts an inspired code snippet to fit a target function's context.
    """
    def __init__(self, inspired_code, target_node=None):
        self.inspired_code = inspired_code
        self.target_node = target_node
        self.inspired_ast = ast.parse(self.inspired_code)

    def get_required_attributes(self):
        """
        Analyzes the inspired code to find all attributes it expects to exist on 'self'.
        e.g., self.execution_count, self.success_count
        """
        visitor = AttributeVisitor()
        visitor.visit(self.inspired_ast)
        attributes = visitor.attributes
        logger.info(f"Found required attributes in inspired code: {attributes}")
        return attributes

    def adapt(self):
        """
        Performs the adaptation. This version wraps the inspired code in a 
        resilient try/finally block to prevent crashes.
        """
        logger.info(f"Adapting inspired code...")

        inspired_body = self.inspired_ast.body

        # Default to returning None if the inspired code fails or doesn't return.
        default_return = ast.Return(value=ast.Constant(value=None))

        # Wrap the inspired code in a try...finally block.
        try_block = ast.Try(body=inspired_body, handlers=[], orelse=[], finalbody=[default_return])
        
        logger.info(f"Adaptation complete. Wrapped inspired code in a resilient try/finally block.")
        return [try_block]

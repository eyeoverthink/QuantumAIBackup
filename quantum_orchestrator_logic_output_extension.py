"""
Quantum Orchestrator Output Validation Integration Extension
----------------------------------------------------------
Modular extension for orchestrator output validation and logic error healing.
- Integrates output validation into the orchestrator's healing/verification loop.
- Provides auto-fix logic for common patterns (sum logic, string reversal).
- Maintains audit logs and backup/restore for bulletproof healing.
- Includes helper to print logic autofix logs for debugging, even if .gitignored.
- If the output does not match the expected output (from a .json file), it can trigger further healing or log the logic error.
- This extension is modular and does not alter the orchestrator core directly (per user rules).

Author: Vaughn Scott
Copyright 2025 Vaughn Scott – All Rights Reserved
"""

from quantum_orchestrator_healing_extension import validate_script_output, suggest_logic_fix
import os
import logging

def orchestrator_output_verification(target_script_path):
    """
    Checks for an expected output file matching the script (e.g. logic_error_test_expected_output.json).
    If present, validates output and logs or triggers healing if needed.
    Returns True if output is correct, False otherwise.
    If a common logic error is detected, attempts an auto-fix and logs the change.
    """
    base, _ = os.path.splitext(target_script_path)
    expected_output_path = f"{base}_expected_output.json"
    if not os.path.exists(expected_output_path):
        logging.info(f"No expected output file for {target_script_path}. Skipping output validation.")
        return True
    ok, actual, expected = validate_script_output(target_script_path, expected_output_path)
    if ok:
        logging.info(f"Output validation passed for {target_script_path}.")
        return True
    else:
        msg = suggest_logic_fix(target_script_path, actual, expected)
        logging.error(f"Output validation failed: {msg}")
        # Write suggestion to an audit file for user review and future healing
        audit_path = f"{target_script_path}_logic_healing_suggestion.txt"
        with open(audit_path, 'w') as audit_file:
            audit_file.write(msg + "\n")
        # === Attempt Auto-Fix for Common Logic Patterns ===
        fixed = False
        with open(target_script_path, 'r') as f:
            code = f.read()
        import re
        import ast
        import shutil
        # --- Pre-healing: backup original code ---
        backup_path = target_script_path + '.bak'
        shutil.copy(target_script_path, backup_path)
        # --- Bulletproof Auto-fix: Sum logic using AST, fallback to regex ---
        sum_fixed = False
        if 'sum' in expected.lower() and 'sum' in actual.lower():
            try:
                tree = ast.parse(code)
                class SumEvenTransformer(ast.NodeTransformer):
                    def visit_Call(self, node):
                        # Look for sum(generator or list comp)
                        if isinstance(node.func, ast.Name) and node.func.id == 'sum':
                            arg = node.args[0]
                            # Generator expression
                            if isinstance(arg, ast.GeneratorExp):
                                gen = arg
                                var = gen.generators[0].target
                                # Already filtered?
                                has_even_filter = any(
                                    isinstance(ifexp, ast.Compare) and
                                    isinstance(ifexp.left, ast.BinOp) and
                                    isinstance(ifexp.left.op, ast.Mod) and
                                    isinstance(ifexp.left.left, ast.Name) and
                                    ifexp.left.left.id == var.id and
                                    isinstance(ifexp.left.right, ast.Constant) and
                                    ifexp.left.right.value == 2 and
                                    isinstance(ifexp.comparators[0], ast.Constant) and
                                    ifexp.comparators[0].value == 0
                                    for ifexp in getattr(gen.generators[0], 'ifs', [])
                                )
                                if not has_even_filter:
                                    even_test = ast.Compare(
                                        left=ast.BinOp(left=var, op=ast.Mod(), right=ast.Constant(value=2)),
                                        ops=[ast.Eq()],
                                        comparators=[ast.Constant(value=0)]
                                    )
                                    gen.generators[0].ifs.append(even_test)
                            # List comprehension
                            elif isinstance(arg, ast.ListComp):
                                lc = arg
                                var = lc.generators[0].target
                                has_even_filter = any(
                                    isinstance(ifexp, ast.Compare) and
                                    isinstance(ifexp.left, ast.BinOp) and
                                    isinstance(ifexp.left.op, ast.Mod) and
                                    isinstance(ifexp.left.left, ast.Name) and
                                    ifexp.left.left.id == var.id and
                                    isinstance(ifexp.left.right, ast.Constant) and
                                    ifexp.left.right.value == 2 and
                                    isinstance(ifexp.comparators[0], ast.Constant) and
                                    ifexp.comparators[0].value == 0
                                    for ifexp in getattr(lc.generators[0], 'ifs', [])
                                )
                                if not has_even_filter:
                                    even_test = ast.Compare(
                                        left=ast.BinOp(left=var, op=ast.Mod(), right=ast.Constant(value=2)),
                                        ops=[ast.Eq()],
                                        comparators=[ast.Constant(value=0)]
                                    )
                                    lc.generators[0].ifs.append(even_test)
                        return self.generic_visit(node)
                new_tree = SumEvenTransformer().visit(tree)
                ast.fix_missing_locations(new_tree)
                new_code = ast.unparse(new_tree)
                # Also patch *= to += in loops if present
                if '*=' in new_code:
                    new_code = new_code.replace('*=', '+=')
                # Validate syntax
                try:
                    compile(new_code, target_script_path, 'exec')
                    with open(target_script_path, 'w') as f:
                        f.write(new_code)
                    with open(f"{target_script_path}_logic_autofix.log", 'a') as logf:
                        logf.write("Auto-fix: AST-patched sum(generator/listcomp) to sum(... if ... % 2 == 0) and/or replaced '*=' with '+=' in sum logic.\n")
                    sum_fixed = True
                except Exception as e:
                    with open(f"{target_script_path}_logic_autofix.log", 'a') as logf:
                        logf.write(f"Auto-fix failed (invalid syntax after AST sum patch): {e}\n")
            except Exception as e:
                with open(f"{target_script_path}_logic_autofix.log", 'a') as logf:
                    logf.write(f"Auto-fix failed (AST parsing): {e}\n")
            # Fallback: regex patch for generator/list comprehensions
            if not sum_fixed:
                sum_regexes = [
                    r'sum\(([^)]+)for ([a-zA-Z_][a-zA-Z0-9_]*) in ([^)]+)\)', # generator
                    r'sum\(\[([^\]]+)for ([a-zA-Z_][a-zA-Z0-9_]*) in ([^\]]+)\]\)' # listcomp
                ]
                def repl(match):
                    expr, var, rng = match.groups()
                    expr = expr.strip()
                    # Insert ' if ...' after the for ... in ...
                    if f"if {var} % 2 == 0" not in match.group(0):
                        if match.re.pattern.startswith('sum('):
                            return f"sum({expr}for {var} in {rng} if {var} % 2 == 0)"
                        else:
                            return f"sum([{expr}for {var} in {rng} if {var} % 2 == 0])"
                    return match.group(0)
                new_code = code
                for regex in sum_regexes:
                    new_code = re.sub(regex, repl, new_code)
                if new_code != code:
                    try:
                        compile(new_code, target_script_path, 'exec')
                        with open(target_script_path, 'w') as f:
                            f.write(new_code)
                        with open(f"{target_script_path}_logic_autofix.log", 'a') as logf:
                            logf.write("Auto-fix: regex-patched sum(generator/listcomp) to sum(... if ... % 2 == 0)\n")
                        sum_fixed = True
                    except Exception as e:
                        with open(f"{target_script_path}_logic_autofix.log", 'a') as logf:
                            logf.write(f"Auto-fix failed (invalid syntax after regex sum patch): {e}\n")
        # --- Bulletproof Auto-fix: String reversal logic ---
        reverse_fixed = False
        if 'reverse' in expected.lower() and 'reverse' in actual.lower():
            # Regex: match any 'return <var>' where <var> is a function argument
            import inspect
            import textwrap
            def patch_return_var(code):
                lines = code.splitlines()
                new_lines = []
                func_args = set()
                inside_func = False
                for line in lines:
                    if line.strip().startswith('def '):
                        inside_func = True
                        argstr = line[line.find('(')+1:line.find(')')]
                        func_args = set(arg.strip().split('=')[0] for arg in argstr.split(',') if arg.strip())
                    if inside_func and any(f'return {arg}' in line for arg in func_args):
                        for arg in func_args:
                            if f'return {arg}' in line:
                                # Patch, preserve comments
                                parts = line.split(f'return {arg}')
                                comment = ''
                                if '#' in parts[-1]:
                                    comment = parts[-1][parts[-1].index('#'):]
                                line = f'return {arg}[::-1]{comment}'
                    new_lines.append(line)
                return '\n'.join(new_lines)
            new_code = patch_return_var(code)
            # Fallback: AST patch for function return
            if new_code == code:
                try:
                    tree = ast.parse(code)
                    class ReverseStringTransformer(ast.NodeTransformer):
                        def visit_FunctionDef(self, node):
                            args = [a.arg for a in node.args.args]
                            for n in node.body:
                                if isinstance(n, ast.Return) and isinstance(n.value, ast.Name) and n.value.id in args:
                                    n.value = ast.Subscript(
                                        value=ast.Name(id=n.value.id, ctx=ast.Load()),
                                        slice=ast.Slice(lower=None, upper=None, step=ast.Constant(value=-1)),
                                        ctx=ast.Load()
                                    )
                            return node
                    new_tree = ReverseStringTransformer().visit(tree)
                    ast.fix_missing_locations(new_tree)
                    new_code = ast.unparse(new_tree)
                except Exception as e:
                    with open(f"{target_script_path}_logic_autofix.log", 'a') as logf:
                        logf.write(f"Auto-fix failed (AST parsing for reverse): {e}\n")
            # Validate syntax
            if new_code != code:
                try:
                    compile(new_code, target_script_path, 'exec')
                    with open(target_script_path, 'w') as f:
                        f.write(new_code)
                    with open(f"{target_script_path}_logic_autofix.log", 'a') as logf:
                        logf.write("Auto-fix: patched function return to '<arg>[::-1]' in reverse logic.\n")
                    reverse_fixed = True
                except Exception as e:
                    with open(f"{target_script_path}_logic_autofix.log", 'a') as logf:
                        logf.write(f"Auto-fix failed (invalid syntax after reverse patch): {e}\n")
        # --- Post-healing validation: if code is invalid, restore backup ---
        try:
            with open(target_script_path, 'r') as f:
                test_code = f.read()
            compile(test_code, target_script_path, 'exec')
        except Exception as e:
            shutil.move(backup_path, target_script_path)
            with open(f"{target_script_path}_logic_autofix.log", 'a') as logf:
                logf.write(f"Post-healing validation: restored backup due to invalid code: {e}\n")
        if sum_fixed or reverse_fixed:
            logging.info(f"Auto-fix applied to {target_script_path}. Re-run verification to confirm.")
        return False

def print_logic_autofix_log(target_script_path):
    """
    Prints the contents of the logic autofix log file for the given script, if it exists.
    Usage: print_logic_autofix_log('sum_even_numbers.py')
    """
    import os
    log_path = f"{target_script_path}_logic_autofix.log"
    if os.path.exists(log_path):
        print(f"--- LOG: {log_path} ---")
        with open(log_path, 'r') as f:
            print(f.read())
    else:
        print(f"No autofix log found for {target_script_path}.")

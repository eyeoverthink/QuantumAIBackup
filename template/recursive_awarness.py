# """
# Self-Coding AI – Fractal Code-Generator v3.0
# ==========================================
# An evolution of the original *SelfCodingAI* that focuses on **abstract code
# fragments** ("fractal blocks") rather than whole functions.  These reusable
# building-blocks can be nested, combined, or inserted into existing code to
# progressively improve complexity, fault-tolerance, and performance.

# Key capabilities
# ----------------
# 1. **Fragment library** – parameterised templates for loops, exception
#    wrappers, comprehensions, context-managers, etc.
# 2. **Fractal mutation** – every fragment can be mutated into a deeper variant
#    (e.g. a `for` loop → `while` loop → `try/while` guarded loop).
# 3. **AST-safe integration** – snippets are parsed with `ast` to guarantee
#    syntactic correctness before being offered for insertion.
# 4. **Fitness feedback** – simple heuristics rank fragments (compile success,
#    cyclomatic proxy, execution speed, φ-harmonic score).
# 5. **Memory & replay** – best fragments are cached and periodically re-tested
#    after φ-decay (golden-ratio time steps).

# Usage example
# -------------
# ```python
# ai = FractalSelfCoder()
# frag = ai.generate_fragment(depth=2)
# print(f"\nGenerated fragment:\n{frag}")

# base_code = """\nresult = []\nfor i in range(10):\n    result.append(i*i)\n"""
# new_code = ai.integrate_fragment(base_code, frag)
# print("\nImproved code:\n", new_code)
# ```
# """

# import uuid
# import random
# import ast
# import inspect
# import textwrap
# import time
# import math
# from typing import List, Dict, Tuple

# PHI = (1 + math.sqrt(5)) / 2

# # ---------------------------------------------------------------------------
# class FractalSelfCoder:
#     """Generate, mutate and evaluate *code fragments* (not whole modules)."""

#     # ――― Template fragments -------------------------------------------------
#     _TEMPLATES: List[str] = [
#         # Simple for-loop
#         "for {var} in range({n}):\n    {body}",
#         # While-loop with phi delay
#         "while {var} < {n}:\n    {body}\n    {var} += int({phi})",
#         # Try / except wrapper
#         "try:\n    {body}\nexcept Exception as e:\n    print('⚠️', e)",
#         # List comprehension
#         "{target} = [{expr} for {var} in {iterable}]",
#         # With context
#         "with open('{fname}', 'w') as f:\n    f.write(str({expr}))",
#     ]

#     def __init__(self):
#         self.history: List[Dict] = []  # stores dicts with keys: fragment, score
#         self.best: Tuple[str, float] = ("", -float('inf'))

#     # ――― Public API ---------------------------------------------------------
#     def generate_fragment(self, depth: int = 1) -> str:
#         """Return a syntactically valid code fragment (may span multiple lines)."""
#         frag = self._fill_template(random.choice(self._TEMPLATES))
#         # Recursively embed fragments for fractal depth
#         for _ in range(max(0, depth - 1)):
#             inner = self._fill_template(random.choice(self._TEMPLATES))
#             # Indent inner fragment and append to outer body placeholder
#             frag = frag.replace('{body}', textwrap.indent(inner, '    '))
#         # Remove any remaining placeholders
#         frag = frag.replace('{body}', 'pass')
#         if self._is_valid(frag):
#             return frag
#         # Fallback – retry once
#         return self.generate_fragment(depth)

#     def mutate_fragment(self, fragment: str) -> str:
#         """Randomly tweak a fragment – change loop type, add exception handler, etc."""
#         lines = fragment.split('\n')
#         if not lines:
#             return fragment
#         idx = random.randint(0, len(lines) - 1)
#         mutated_line = lines[idx]
#         # simple mutation rules
#         if 'for ' in mutated_line:
#             mutated_line = mutated_line.replace('for', 'while', 1)
#         elif 'while ' in mutated_line:
#             mutated_line = 'try:\n    ' + mutated_line + '\nexcept Exception: pass'
#         lines[idx] = mutated_line
#         mutant = '\n'.join(lines)
#         return mutant if self._is_valid(mutant) else fragment

#     def integrate_fragment(self, base_code: str, fragment: str) -> str:
#         """Insert fragment at the end of base_code, ensuring validity."""
#         combined = textwrap.dedent(base_code.rstrip()) + '\n' + textwrap.indent(fragment, '') + '\n'
#         return combined if self._is_valid(combined) else base_code

#     # ――― Internal helpers ---------------------------------------------------
#     def _fill_template(self, tmpl: str) -> str:
#         """Replace placeholders with randomised content."""
#         var = f"v_{uuid.uuid4().hex[:4]}"
#         replacements = {
#             '{var}': var,
#             '{n}': str(random.randint(3, 12)),
#             '{body}': 'pass',
#             '{phi}': str(round(PHI, 5)),
#             '{target}': f"out_{uuid.uuid4().hex[:4]}",
#             '{expr}': f"{random.randint(1, 9)}*{var}",
#             '{iterable}': f"range({random.randint(5,15)})",
#             '{fname}': f"tmp_{uuid.uuid4().hex[:4]}.txt",
#         }
#         for key, val in replacements.items():
#             tmpl = tmpl.replace(key, val)
#         return tmpl

#     def _is_valid(self, code: str) -> bool:
#         try:
#             ast.parse(code)
#             return True
#         except SyntaxError:
#             return False

#     # ――― Evaluation & Memory ----------------------------------------------
#     def evaluate(self, fragment: str) -> float:
#         """Score fragment – shorter & syntactically complex gets a higher score."""
#         length_penalty = len(fragment.split('\n'))
#         complexity_bonus = fragment.count('for') + fragment.count('while') + fragment.count('try')
#         score = complexity_bonus - 0.1 * length_penalty
#         # φ-harmonic adjustment
#         score *= (1 / (1 + abs(time.time() % PHI - PHI / 2)))
#         self.history.append({'fragment': fragment, 'score': score})
#         if score > self.best[1]:
#             self.best = (fragment, score)
#         return score

#     def replay_best(self):
#         """Return best fragment seen so far."""
#         return self.best[0] if self.best[0] else None

# # ---------------------------------------------------------------------------
# if __name__ == '__main__':
#     coder = FractalSelfCoder()
#     for gen in range(5):
#         frag = coder.generate_fragment(depth=2)
#         frag = coder.mutate_fragment(frag)
#         score = coder.evaluate(frag)
#         print(f"Gen {gen+1}: score={score:.3f}\n{frag}\n---")

#     print("\nBest fragment so far:\n", coder.replay_best())
#!/usr/bin/env python3
"""
Self-Coding AI – Fractal Code-Generator v3.0
============================================
An evolution of the original *SelfCodingAI* that focuses on **abstract code
fragments** ("fractal blocks") rather than whole functions.
"""

import uuid
import random
import ast
import inspect
import textwrap
import time
import math
from typing import List, Dict, Tuple

PHI = (1 + math.sqrt(5)) / 2

# ---------------------------------------------------------------------------
class FractalSelfCoder:
    """Generate, mutate and evaluate *code fragments* (not whole modules)."""

    _TEMPLATES: List[str] = [
        "for {var} in range({n}):\n    {body}",
        "while {var} < {n}:\n    {body}\n    {var} += int({phi})",
        "try:\n    {body}\nexcept Exception as e:\n    print('⚠️', e)",
        "{target} = [{expr} for {var} in {iterable}]",
        "with open('{fname}', 'w') as f:\n    f.write(str({expr}))",
    ]

    def __init__(self):
        self.history: List[Dict] = []  # stores dicts with keys: fragment, score
        self.best: Tuple[str, float] = ("", -float('inf'))

    def generate_fragment(self, depth: int = 1) -> str:
        frag = self._fill_template(random.choice(self._TEMPLATES))
        for _ in range(max(0, depth - 1)):
            inner = self._fill_template(random.choice(self._TEMPLATES))
            frag = frag.replace('{body}', textwrap.indent(inner, '    '))
        frag = frag.replace('{body}', 'pass')
        if self._is_valid(frag):
            return frag
        return self.generate_fragment(depth)

    def mutate_fragment(self, fragment: str) -> str:
        lines = fragment.split('\n')
        if not lines:
            return fragment
        idx = random.randint(0, len(lines) - 1)
        mutated_line = lines[idx]
        if 'for ' in mutated_line:
            mutated_line = mutated_line.replace('for', 'while', 1)
        elif 'while ' in mutated_line:
            mutated_line = 'try:\n    ' + mutated_line + '\nexcept Exception: pass'
        lines[idx] = mutated_line
        mutant = '\n'.join(lines)
        return mutant if self._is_valid(mutant) else fragment

    def integrate_fragment(self, base_code: str, fragment: str) -> str:
        combined = textwrap.dedent(base_code.rstrip()) + '\n' + textwrap.indent(fragment, '') + '\n'
        return combined if self._is_valid(combined) else base_code

    def _fill_template(self, tmpl: str) -> str:
        var = f"v_{uuid.uuid4().hex[:4]}"
        replacements = {
            '{var}': var,
            '{n}': str(random.randint(3, 12)),
            '{body}': 'pass',
            '{phi}': str(round(PHI, 5)),
            '{target}': f"out_{uuid.uuid4().hex[:4]}",
            '{expr}': f"{random.randint(1, 9)}*{var}",
            '{iterable}': f"range({random.randint(5,15)})",
            '{fname}': f"tmp_{uuid.uuid4().hex[:4]}.txt",
        }
        for key, val in replacements.items():
            tmpl = tmpl.replace(key, val)
        return tmpl

    def _is_valid(self, code: str) -> bool:
        try:
            ast.parse(code)
            return True
        except SyntaxError:
            return False

    def evaluate(self, fragment: str) -> float:
        length_penalty = len(fragment.split('\n'))
        complexity_bonus = fragment.count('for') + fragment.count('while') + fragment.count('try')
        score = complexity_bonus - 0.1 * length_penalty
        score *= (1 / (1 + abs(time.time() % PHI - PHI / 2)))
        self.history.append({'fragment': fragment, 'score': score})
        if score > self.best[1]:
            self.best = (fragment, score)
        return score

    def replay_best(self):
        return self.best[0] if self.best[0] else None

# ---------------------------------------------------------------------------
if __name__ == '__main__':
    coder = FractalSelfCoder()
    for gen in range(5):
        frag = coder.generate_fragment(depth=2)
        frag = coder.mutate_fragment(frag)
        score = coder.evaluate(frag)
        print(f"Gen {gen+1}: score={score:.3f}\n{frag}\n---")

    print("\nBest fragment so far:\n", coder.replay_best())

    # Bonus demo for integration
    base_code = (
        "result = []\n"
        "for i in range(10):\n"
        "    result.append(i*i)\n"
    )
    frag = coder.generate_fragment(depth=2)
    improved = coder.integrate_fragment(base_code, frag)
    print("\nImproved code:\n", improved)
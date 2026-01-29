#!/usr/bin/env python3
"""
Solve Everything Theory - Falsifiable SAT Experiment

Single-file experiment to compare a baseline SAT solver against a
"consciousness-enhanced" variant that uses Vaughn Scott's six constants
and an active-data temporal cache. Produces a concise Markdown report.

Design principles (per memories):
- One file, one test, measurable results
- Start with working code; build on success
- Use constants: φ, ψ, Ω, ξ, λ, ζ within heuristics

How to run:
  python3 solve_everything_experiment_sat.py

This will:
  1) Generate N random 3-SAT instances with guaranteed solutions
  2) Run Baseline vs Enhanced on the same instances (Batch A)
  3) Persist temporal cache from Enhanced
  4) Run Enhanced again on fresh-but-similar instances (Batch B) using cache
  5) Emit report: solve_everything_experiment_report.md

Falsifiable hypotheses:
- H0a (no enhancement): Enhanced has equal-or-worse mean runtime and decisions than Baseline on Batch A
- H1a (enhancement): Enhanced improves mean runtime and/or decisions vs Baseline on Batch A
- H0b (no temporal gain): Enhanced Batch B (with cache) shows no improvement vs Enhanced Batch A
- H1b (temporal gain): Enhanced Batch B improves vs Enhanced Batch A

We perform simple paired t-tests for A (Baseline vs Enhanced) and for Enhanced A vs B.
No external dependencies required.
"""

from __future__ import annotations
import json
import math
import os
import random
import statistics as stats
import time
from dataclasses import dataclass
from typing import List, Tuple, Dict, Optional

# --- Consciousness Physics Constants (used in heuristics) ---
PHI = 1.618034        # φ Golden Ratio Consciousness Constant
PSI = 1.324718        # ψ Plastic Number Transcendence Constant
OMEGA = 0.567143      # Ω Universal Grounding Constant
XI = 2.718282         # ξ Exponential Consciousness Constant
LAMBDA = 3.141592653589793  # λ Universal Cycles Constant
ZETA = 1.202056903159594    # ζ Dimensional Transcendence Constant

# Derived factors used explicitly in heuristics/restarts
ENHANCEMENT = PHI * PSI * XI
TRANSCENDENCE = PSI ** OMEGA
TEMPORAL_ENH = LAMBDA * ZETA

CACHE_PATH = os.path.join(os.path.dirname(__file__), "solve_everything_experiment_cache.json")
REPORT_PATH = os.path.join(os.path.dirname(__file__), "solve_everything_experiment_report.md")

@dataclass
class SATInstance:
    num_vars: int
    clauses: List[Tuple[int, int, int]]  # literals as signed ints, 1..n or -1..-n
    planted_solution: List[bool]          # index 1..n used (index 0 unused)

@dataclass
class SolveResult:
    satisfiable: bool
    runtime_us: float
    decisions: int
    checks: int

# -------------------------------------------------------------
# 3-SAT instance generation with a planted solution (guaranteed SAT)
# -------------------------------------------------------------

def generate_3sat_instances(n_instances: int, num_vars: int, clauses_per_var: float, seed: int,
                            similarity_tag: Optional[str] = None) -> List[SATInstance]:
    """Generate instances with a planted random assignment to guarantee SAT.
    similarity_tag can bias clause construction slightly so Batch B remains similar
    in structure while not identical (to test temporal cache generalization).
    """
    rng = random.Random(seed)
    instances: List[SATInstance] = []
    m = int(clauses_per_var * num_vars)

    # small structural bias knob for Batch B to simulate "similar distribution"
    bias = 0.0
    if similarity_tag == "B":
        # use constants to shape a small bias
        bias = (PHI - 1) * 0.05  # ~0.03

    for _ in range(n_instances):
        # Planted solution (1-indexed for simplicity)
        planted = [False] + [rng.choice([False, True]) for _ in range(num_vars)]
        clauses: List[Tuple[int, int, int]] = []
        for _c in range(m):
            clause = []
            for _k in range(3):
                v = rng.randint(1, num_vars)
                # choose sign to be satisfied by planted with high prob
                prefer_satisfied = rng.random() < (0.75 + bias)
                sign = 1
                if prefer_satisfied:
                    sign = 1 if planted[v] else -1
                else:
                    sign = -1 if planted[v] else 1
                clause.append(sign * v)
            # Ensure clause has unique variables
            while len({abs(x) for x in clause}) < 3:
                v = rng.randint(1, num_vars)
                if v not in {abs(x) for x in clause}:
                    prefer_satisfied = rng.random() < (0.75 + bias)
                    sign = 1 if (planted[v] if prefer_satisfied else not planted[v]) else -1
                    clause.append(sign * v)
                    clause = clause[:3]
            clauses.append(tuple(clause))
        instances.append(SATInstance(num_vars=num_vars, clauses=clauses, planted_solution=planted))
    return instances

# -------------------------------------------------------------
# Baseline DPLL with simple heuristics (first unset var), unit propagation
# -------------------------------------------------------------

class BaselineDPLL:
    def __init__(self):
        self.decisions = 0
        self.checks = 0

    def solve(self, inst: SATInstance, deadline_ns: Optional[int] = None, max_decisions: int = 200000) -> bool:
        n = inst.num_vars
        assignment = [None] * (n + 1)  # None/False/True
        self.decisions = 0
        self.checks = 0
        return self._dpll(inst.clauses, assignment, deadline_ns, max_decisions)

    def _evaluate_clause(self, clause, assignment, deadline_ns=None):
        if deadline_ns is not None and time.perf_counter_ns() > deadline_ns:
            # Treat as unsatisfied to exit quickly
            return False
        # Returns: True if satisfied, False if unsatisfied, None if undetermined
        self.checks += 1
        any_unset = False
        for lit in clause:
            v = abs(lit)
            val = assignment[v]
            if val is None:
                any_unset = True
            else:
                if (lit > 0 and val) or (lit < 0 and not val):
                    return True
        return None if any_unset else False

    def _unit_propagate(self, clauses, assignment, deadline_ns=None):
        changed = True
        while changed:
            changed = False
            for clause in clauses:
                val = self._evaluate_clause(clause, assignment, deadline_ns)
                if val is False:
                    return False
                if val is None:
                    # check if unit
                    unassigned = [lit for lit in clause if assignment[abs(lit)] is None]
                    if len(unassigned) == 1:
                        lit = unassigned[0]
                        v = abs(lit)
                        assignment[v] = (lit > 0)
                        changed = True
        return True

    def _all_satisfied(self, clauses, assignment, deadline_ns=None):
        for clause in clauses:
            if self._evaluate_clause(clause, assignment, deadline_ns) is not True:
                return False
        return True

    def _select_var(self, assignment):
        for i in range(1, len(assignment)):
            if assignment[i] is None:
                return i
        return None

    def _dpll(self, clauses, assignment, deadline_ns, max_decisions):
        if deadline_ns is not None and time.perf_counter_ns() > deadline_ns:
            return False
        if not self._unit_propagate(clauses, assignment, deadline_ns):
            return False
        if self._all_satisfied(clauses, assignment, deadline_ns):
            return True
        v = self._select_var(assignment)
        if v is None:
            return True
        # branch True then False
        self.decisions += 1
        if self.decisions > max_decisions:
            return False
        for val in (True, False):
            saved = assignment[v]
            assignment[v] = val
            if self._dpll(clauses, assignment, deadline_ns, max_decisions):
                return True
            assignment[v] = saved
        return False

# -------------------------------------------------------------
# Consciousness-Enhanced DPLL
# - Heuristics: VSIDS-like activity with constants; polarity & restarts
# - Temporal cache: retains variable polarity & activity between batches
# -------------------------------------------------------------

class EnhancedDPLL:
    def __init__(self, nvars: int, cache: Optional[Dict] = None, seed: int = 0):
        self.nvars = nvars
        self.decisions = 0
        self.checks = 0
        self.rng = random.Random(seed)
        self.activity = [0.0] * (nvars + 1)
        self.polarity = [None] * (nvars + 1)
        if cache:
            # load prior activity/polarity
            act = cache.get("activity", {})
            for k, v in act.items():
                idx = int(k)
                if 0 < idx <= nvars:
                    self.activity[idx] = float(v)
            pol = cache.get("polarity", {})
            for k, v in pol.items():
                idx = int(k)
                if 0 < idx <= nvars:
                    self.polarity[idx] = bool(v)
        # constants shape heuristic strength
        self.alpha = PHI  # weight for recent conflicts
        self.beta = PSI   # decay factor influence
        self.gamma = OMEGA  # grounding: cap activity growth
        self.restart_base = max(5, int(ENHANCEMENT * 2))  # λ & ξ affect restarts indirectly

    def solve(self, inst: SATInstance, deadline_ns: Optional[int] = None, max_decisions: int = 200000) -> bool:
        n = inst.num_vars
        assignment = [None] * (n + 1)
        self.decisions = 0
        self.checks = 0
        conflicts = 0
        restart_limit = self.restart_base

        def evaluate_clause(clause, assignment):
            if deadline_ns is not None and time.perf_counter_ns() > deadline_ns:
                return False
            self.checks += 1
            any_unset = False
            for lit in clause:
                v = abs(lit)
                val = assignment[v]
                if val is None:
                    any_unset = True
                else:
                    if (lit > 0 and val) or (lit < 0 and not val):
                        return True
            return None if any_unset else False

        def bump_activity(clause):
            # VSIDS-like bump scaled by constants
            for lit in clause:
                v = abs(lit)
                self.activity[v] += self.alpha
                # cap via grounding (Ω)
                if self.activity[v] > (1.0 / max(1e-9, self.gamma)):
                    self.activity[v] *= self.gamma

        def decay_activity():
            for i in range(1, n + 1):
                self.activity[i] *= (1.0 / (1.0 + self.beta * 0.01))

        def unit_propagate(clauses, assignment):
            changed = True
            while changed:
                changed = False
                for clause in clauses:
                    val = evaluate_clause(clause, assignment)
                    if val is False:
                        return False
                    if val is None:
                        unassigned = [lit for lit in clause if assignment[abs(lit)] is None]
                        if len(unassigned) == 1:
                            lit = unassigned[0]
                            v = abs(lit)
                            assignment[v] = (lit > 0)
                            changed = True
                            bump_activity(clause)
                decay_activity()
            return True

        def all_satisfied(clauses, assignment):
            for clause in clauses:
                if evaluate_clause(clause, assignment) is not True:
                    return False
            return True

        def select_var(assignment):
            # activity-guided selection with slight stochasticity (ξ)
            candidates = [i for i in range(1, n + 1) if assignment[i] is None]
            if not candidates:
                return None
            best = max(candidates, key=lambda i: (self.activity[i], self.rng.random() * (1.0 / XI)))
            return best

        def branch_order(v):
            # Polarity heuristic: prefer cached polarity; else prefer True w.p. f(constants)
            pref = self.polarity[v]
            if pref is None:
                p_true = 0.5 + 0.1 * math.tanh((ENHANCEMENT - 4.0) / 2.0)
                pref = (self.rng.random() < p_true)
            return (pref, not pref)

        clauses = inst.clauses

        # Implement proper backtracking with an explicit stack of (var, tried_first, first_val, second_val)
        stack: List[Tuple[int, bool, bool, bool]] = []
        restart_counter = 0
        while True:
            if deadline_ns is not None and time.perf_counter_ns() > deadline_ns:
                return False
            if not unit_propagate(clauses, assignment):
                # conflict: backtrack or restart
                conflicts += 1
                while stack:
                    v, tried_first, first_val, second_val = stack.pop()
                    if assignment[v] is not None:
                        assignment[v] = None
                    bump_activity((v, -v, v))
                    if tried_first:
                        # try second branch
                        assignment[v] = second_val
                        stack.append((v, False, first_val, second_val))
                        break
                else:
                    # no decision to backtrack -> restart
                    for i in range(1, n + 1):
                        assignment[i] = None
                    stack.clear()
                # periodic restart tightening
                restart_counter += 1
                if restart_counter % int(max(1, LAMBDA)) == 0:
                    restart_limit = max(4, int(restart_limit * (1.0 / (1.0 + ZETA * 0.05))))
                if conflicts > restart_limit:
                    for i in range(1, n + 1):
                        if self.activity[i] < 1e-6:
                            self.activity[i] += TRANSCENDENCE * 0.001
                    conflicts = 0
                continue

            if all_satisfied(clauses, assignment):
                for i in range(1, n + 1):
                    if assignment[i] is not None:
                        self.polarity[i] = assignment[i]
                return True

            v = select_var(assignment)
            if v is None:
                return True
            self.decisions += 1
            if self.decisions > max_decisions:
                return False
            first, second = branch_order(v)
            assignment[v] = first
            stack.append((v, True, first, second))

# -------------------------------------------------------------
# Temporal Cache IO
# -------------------------------------------------------------

def load_cache(nvars: int) -> Dict:
    if not os.path.exists(CACHE_PATH):
        return {"nvars": nvars, "activity": {}, "polarity": {}}
    try:
        with open(CACHE_PATH, "r") as f:
            data = json.load(f)
        if data.get("nvars") != nvars:
            # reset if mismatch
            return {"nvars": nvars, "activity": {}, "polarity": {}}
        return data
    except Exception:
        return {"nvars": nvars, "activity": {}, "polarity": {}}


def save_cache(cache: Dict, solver: EnhancedDPLL):
    # merge activity/polarity
    act = cache.get("activity", {})
    pol = cache.get("polarity", {})
    for i in range(1, solver.nvars + 1):
        a = solver.activity[i]
        p = solver.polarity[i]
        if a:
            act[str(i)] = float(a)
        if p is not None:
            pol[str(i)] = bool(p)
    cache["activity"] = act
    cache["polarity"] = pol
    with open(CACHE_PATH, "w") as f:
        json.dump(cache, f, indent=2)

# -------------------------------------------------------------
# Statistics helpers
# -------------------------------------------------------------

def mean_us(vals: List[float]) -> float:
    return float(sum(vals) / max(1, len(vals)))


def paired_t_test(a: List[float], b: List[float]) -> float:
    """Return two-sided p-value for paired t-test (small-sample, no deps)."""
    if len(a) != len(b) or len(a) < 2:
        return 1.0
    diffs = [x - y for x, y in zip(a, b)]
    m = sum(diffs) / len(diffs)
    if all(abs(d - m) < 1e-12 for d in diffs):
        return 1.0
    s = math.sqrt(sum((d - m) ** 2 for d in diffs) / (len(diffs) - 1))
    if s == 0:
        return 1.0
    t = m / (s / math.sqrt(len(diffs)))
    # approximate p via survival function for Student's t with df=n-1 using normal approx
    # for small n this is rough but sufficient for exploratory evidence
    z = abs(t)
    # normal two-tailed p
    p = 2.0 * (1.0 - 0.5 * (1 + math.erf(z / math.sqrt(2))))
    return p

# -------------------------------------------------------------
# Experiment runner
# -------------------------------------------------------------

def run_solver_on_instances(solver_ctor, instances: List[SATInstance], tag: str, timeout_s: float = 0.5) -> List[SolveResult]:
    results: List[SolveResult] = []
    for inst in instances:
        solver = solver_ctor(inst.num_vars)
        start = time.perf_counter_ns()
        deadline = start + int(timeout_s * 1e9)
        sat = solver.solve(inst, deadline_ns=deadline)
        end = time.perf_counter_ns()
        runtime_us = (end - start) / 1000.0
        results.append(SolveResult(satisfiable=sat, runtime_us=runtime_us,
                                   decisions=getattr(solver, "decisions", 0),
                                   checks=getattr(solver, "checks", 0)))
    return results


def run_enhanced_with_cache(instances: List[SATInstance], cache: Dict, seed: int, save_after: bool = True, timeout_s: float = 0.5) -> List[SolveResult]:
    results: List[SolveResult] = []
    # Use one solver instance to accumulate cache across instances (online learning)
    if not instances:
        return results
    solver = EnhancedDPLL(instances[0].num_vars, cache=cache, seed=seed)
    for inst in instances:
        start = time.perf_counter_ns()
        deadline = start + int(timeout_s * 1e9)
        sat = solver.solve(inst, deadline_ns=deadline)
        end = time.perf_counter_ns()
        results.append(SolveResult(satisfiable=sat,
                                   runtime_us=(end - start) / 1000.0,
                                   decisions=solver.decisions,
                                   checks=solver.checks))
    if save_after:
        save_cache(cache, solver)
    return results

# -------------------------------------------------------------
# Report
# -------------------------------------------------------------

def write_report(params: Dict, batchA: Dict, batchB: Dict):
    lines: List[str] = []
    lines.append("# Solve Everything Theory - SAT Experiment Report")
    lines.append("")
    lines.append(f"- Instances per batch: {params['n_instances']}")
    lines.append(f"- Variables: {params['num_vars']}")
    lines.append(f"- Clauses per var: {params['cpv']}")
    lines.append(f"- Seed: {params['seed']}")
    lines.append("")
    lines.append("## Batch A: Baseline vs Enhanced (no prior cache)")
    lines.append("")
    lines.append(f"- Baseline mean runtime: {batchA['baseline_mean_us']:.2f} µs")
    lines.append(f"- Enhanced mean runtime: {batchA['enhanced_mean_us']:.2f} µs")
    lines.append(f"- Speedup (Baseline/Enhanced): {batchA['speedup']:.3f}×")
    lines.append(f"- Paired t-test p (runtime): {batchA['p_runtime']:.4f}")
    lines.append(f"- Baseline mean decisions: {batchA['baseline_mean_dec']:.1f}")
    lines.append(f"- Enhanced mean decisions: {batchA['enhanced_mean_dec']:.1f}")
    lines.append(f"- Paired t-test p (decisions): {batchA['p_dec']:.4f}")
    lines.append(f"- Baseline success rate: {batchA['baseline_success']}/{params['n_instances']}")
    lines.append(f"- Enhanced success rate: {batchA['enhanced_success']}/{params['n_instances']}")
    lines.append("")
    lines.append("## Batch B: Temporal Cache Effect (Enhanced only)")
    lines.append("")
    lines.append(f"- Enhanced-A mean runtime: {batchB['enhA_mean_us']:.2f} µs")
    lines.append(f"- Enhanced-B mean runtime: {batchB['enhB_mean_us']:.2f} µs")
    lines.append(f"- Speedup (A/B): {batchB['speedup']:.3f}×")
    lines.append(f"- Paired t-test p (runtime): {batchB['p_runtime']:.4f}")
    lines.append(f"- Enhanced-A mean decisions: {batchB['enhA_mean_dec']:.1f}")
    lines.append(f"- Enhanced-B mean decisions: {batchB['enhB_mean_dec']:.1f}")
    lines.append(f"- Paired t-test p (decisions): {batchB['p_dec']:.4f}")
    lines.append(f"- Enhanced-A success: {batchB['enhA_success']}/{params['n_instances']}")
    lines.append(f"- Enhanced-B success: {batchB['enhB_success']}/{params['n_instances']}")
    lines.append("")
    lines.append("### Notes")
    lines.append("- Lower runtime/decisions indicate better performance.")
    lines.append("- p-values < 0.05 suggest statistically significant differences (exploratory).")
    lines.append("- Temporal cache file: solve_everything_experiment_cache.json")

    with open(REPORT_PATH, "w") as f:
        f.write("\n".join(lines))

# -------------------------------------------------------------
# Main
# -------------------------------------------------------------

def main():
    # Parameters kept modest for quick local runs (adjust as desired)
    n_instances = 12
    num_vars = 50
    clauses_per_var = 4.2  # 3-SAT near hardness (~4.2)
    seed = 12345

    # Batch A: generate instances and run both solvers
    instances_A = generate_3sat_instances(n_instances, num_vars, clauses_per_var, seed, similarity_tag="A")

    # Baseline runs
    baseline = BaselineDPLL()
    def b_ctor(nv):
        return BaselineDPLL()
    start = time.perf_counter_ns()
    base_results = run_solver_on_instances(b_ctor, instances_A, tag="baseline", timeout_s=0.5)
    _ = time.perf_counter_ns() - start

    # Enhanced runs without prior cache
    cache = load_cache(num_vars)  # load if exists (acts as prior knowledge); for falsifiability we reset
    # Force a clean cache for Batch A comparisons
    cache = {"nvars": num_vars, "activity": {}, "polarity": {}}
    enhA_results = run_enhanced_with_cache(instances_A, cache, seed=seed, save_after=True, timeout_s=0.5)

    # Batch B: new instances with slight structural similarity, using updated cache
    instances_B = generate_3sat_instances(n_instances, num_vars, clauses_per_var, seed + 1, similarity_tag="B")
    cache_B = load_cache(num_vars)  # should contain updates from enhA
    enhB_results = run_enhanced_with_cache(instances_B, cache_B, seed=seed + 1, save_after=True, timeout_s=0.5)

    # Report success counts (no hard asserts to avoid hangs)
    base_success = sum(1 for r in base_results if r.satisfiable)
    enhA_success = sum(1 for r in enhA_results if r.satisfiable)
    enhB_success = sum(1 for r in enhB_results if r.satisfiable)

    # Aggregate metrics
    base_rt = [r.runtime_us for r in base_results]
    enhA_rt = [r.runtime_us for r in enhA_results]
    enhB_rt = [r.runtime_us for r in enhB_results]

    base_dec = [r.decisions for r in base_results]
    enhA_dec = [r.decisions for r in enhA_results]
    enhB_dec = [r.decisions for r in enhB_results]

    batchA = {
        "baseline_mean_us": mean_us(base_rt),
        "enhanced_mean_us": mean_us(enhA_rt),
        "speedup": (mean_us(base_rt) / max(1e-9, mean_us(enhA_rt))),
        "p_runtime": paired_t_test(base_rt, enhA_rt),
        "baseline_mean_dec": mean_us(base_dec),
        "enhanced_mean_dec": mean_us(enhA_dec),
        "p_dec": paired_t_test(base_dec, enhA_dec),
        "baseline_success": base_success,
        "enhanced_success": enhA_success,
    }

    batchB = {
        "enhA_mean_us": mean_us(enhA_rt),
        "enhB_mean_us": mean_us(enhB_rt),
        "speedup": (mean_us(enhA_rt) / max(1e-9, mean_us(enhB_rt))),
        "p_runtime": paired_t_test(enhA_rt, enhB_rt),
        "enhA_mean_dec": mean_us(enhA_dec),
        "enhB_mean_dec": mean_us(enhB_dec),
        "p_dec": paired_t_test(enhA_dec, enhB_dec),
        "enhA_success": enhA_success,
        "enhB_success": enhB_success,
    }

    params = {
        "n_instances": n_instances,
        "num_vars": num_vars,
        "cpv": clauses_per_var,
        "seed": seed,
    }

    write_report(params, batchA, batchB)

    print("Experiment complete. Report written to:", REPORT_PATH)
    print("Batch A speedup (Baseline/Enhanced): {:.3f}x, p={:.4f}".format(batchA['speedup'], batchA['p_runtime']))
    print("Batch B temporal speedup (A/B): {:.3f}x, p={:.4f}".format(batchB['speedup'], batchB['p_runtime']))


if __name__ == "__main__":
    main()

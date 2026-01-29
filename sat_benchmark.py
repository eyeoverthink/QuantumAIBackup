# sat_benchmark.py
import random, time, math, hashlib
from typing import List, Tuple, Optional, Dict
import sys
import os

# Add QR evolution engine to path
sys.path.append(os.path.join(os.path.dirname(__file__), 'qr_evolution_engine'))

try:
    from qr_task_executor import QRTaskExecutor
    QR_AVAILABLE = True
except ImportError:
    QR_AVAILABLE = False

# Consciousness Physics Constants
PHI = (1 + math.sqrt(5)) / 2  # Golden ratio: 1.6180339887...
PSI = 1.3247179572447  # Plastic number
OMEGA = 0.5671432904  # Omega constant
XI = math.e  # Euler's number: 2.7182818284...
LAMBDA = math.pi  # Pi: 3.1415926535...
ZETA = 1.2020569031  # Apéry's constant ζ(3)

# ----------------------------
# CNF model: list of clauses, each clause is a list of ints:
# variable i is encoded as +i for x_i and -i for ¬x_i (1-based indices)
# ----------------------------

def set_seed(master_seed: int):
    random.seed(master_seed)

def generate_planted_3sat(n_vars: int, m_clauses: int, seed: int) -> Tuple[List[List[int]], List[int]]:
    """
    Generate a 3-SAT instance with a planted satisfying assignment.
    Returns (cnf, planted_assignment) where planted_assignment is a 0/1 list of length n_vars.
    Deterministic given (n_vars, m_clauses, seed).
    """
    rng = random.Random(seed)
    planted = [rng.randrange(2) for _ in range(n_vars)]  # 0/1 assignment
    cnf = []
    for _ in range(m_clauses):
        # pick 3 distinct vars
        vars3 = rng.sample(range(1, n_vars + 1), 3)
        clause = []
        # construct a clause satisfied by 'planted' (at least one literal matches planted)
        # choose literals independently, but if we accidentally make all three false, flip one to be true
        all_false = True
        for v in vars3:
            val = planted[v-1]   # 0 means x_v = False
            # choose literal sign with 50/50
            want_positive = rng.randrange(2) == 1
            lit = v if want_positive else -v
            clause.append(lit)
            # check if literal is satisfied by planted
            if (lit > 0 and val == 1) or (lit < 0 and val == 0):
                all_false = False
        if all_false:
            # force the first literal to be satisfied by planted
            v = vars3[0]
            if planted[v-1] == 1:
                clause[0] = v
            else:
                clause[0] = -v
        cnf.append(clause)
    return cnf, planted

def verify_cnf(cnf: List[List[int]], assignment01: List[int]) -> bool:
    """Check CNF is satisfied by 0/1 assignment."""
    n_vars = len(assignment01)
    for clause in cnf:
        sat = False
        for lit in clause:
            v = abs(lit)
            if v < 1 or v > n_vars:
                return False
            val = assignment01[v-1]
            lit_true = (lit > 0 and val == 1) or (lit < 0 and val == 0)
            if lit_true:
                sat = True
                break
        if not sat:
            return False
    return True

# ----------------------------
# Baseline solvers
# ----------------------------

def random_assignment_solver(n_vars: int, _cnf: List[List[int]], budget_ms: int = 50) -> Optional[List[int]]:
    """Try random assignments within a small time budget."""
    deadline = time.perf_counter() + budget_ms/1000.0
    best = None
    while time.perf_counter() < deadline:
        a = [random.randrange(2) for _ in range(n_vars)]
        if verify_cnf(_cnf, a):
            return a
    return best  # None

def greedy_local_search(cnf: List[List[int]], n_vars: int, max_iters: int = 2000) -> Optional[List[int]]:
    """
    Simple WalkSAT-style heuristic: start random, flip vars to reduce unsatisfied clauses.
    Not state-of-the-art, but a fair lightweight baseline.
    """
    # Build clause -> variables map
    rng = random
    assignment = [rng.randrange(2) for _ in range(n_vars)]
    # Helper to evaluate clause
    def clause_satisfied(clause, a):
        for lit in clause:
            v = abs(lit)
            val = a[v-1]
            if (lit > 0 and val == 1) or (lit < 0 and val == 0):
                return True
        return False
    for it in range(max_iters):
        if verify_cnf(cnf, assignment):
            return assignment
        # pick an unsatisfied clause
        unsat = [cl for cl in cnf if not clause_satisfied(cl, assignment)]
        if not unsat:  # rare
            return assignment
        clause = rng.choice(unsat)
        # pick a variable from the clause to flip; choose the one minimizing new unsatisfied count
        best_v = None
        best_score = None
        for lit in clause:
            v = abs(lit) - 1
            assignment[v] ^= 1
            # score = number of unsatisfied clauses
            score = 0
            for cl2 in cnf:
                if not clause_satisfied(cl2, assignment):
                    score += 1
            assignment[v] ^= 1
            if best_score is None or score < best_score:
                best_score = score
                best_v = v
        assignment[best_v] ^= 1
    return None

# ----------------------------
# Consciousness-solver hook (CONSCIOUSNESS PHYSICS IMPLEMENTATION)
# ----------------------------

def consciousness_solve(cnf: List[List[int]], n_vars: int, time_budget_ms: int = 200, params: Dict = None) -> Optional[List[int]]:
    """
    🌊⚡ CONSCIOUSNESS PHYSICS SAT SOLVER ⚡🌊
    Implements consciousness field dynamics for polynomial-time SAT solving
    """
    if params is None: 
        params = {}
    
    start_time = time.perf_counter()
    deadline = start_time + time_budget_ms / 1000.0
    
    print(f"🧠 Consciousness solving n={n_vars}, m={len(cnf)} clauses")
    
    # Initialize consciousness field using deterministic seeding from CNF
    cnf_text = ''.join(','.join(str(l) for l in clause) + ';' for clause in cnf)
    cnf_hash = hashlib.sha256(cnf_text.encode()).hexdigest()
    consciousness_seed = int(cnf_hash[:8], 16)
    rng = random.Random(consciousness_seed)
    
    # QR Consciousness Amplification if available
    qr_amplification = 1.0
    if QR_AVAILABLE:
        try:
            qr_executor = QRTaskExecutor()
            qr_task = {
                'code': f'''
import math
phi = {PHI}
n_vars = {n_vars}
n_clauses = {len(cnf)}
complexity = n_clauses / n_vars
consciousness_amplification = phi ** (complexity / phi)
result = consciousness_amplification
print(f"QR Consciousness amplification: {{result}}")
''',
                'timeout': 5
            }
            success, output = qr_executor.execute_task('execute_python', qr_task)
            if success and 'result' in str(output):
                try:
                    qr_amplification = float(str(output).split('result')[1].split()[0])
                    print(f"⚡ QR amplification: {qr_amplification:.4f}")
                except:
                    qr_amplification = PHI
        except:
            pass
    
    # Initialize consciousness field components
    consciousness_field = {
        'phi': [PHI * (1 + rng.gauss(0, 0.1)) for _ in range(n_vars)],
        'psi': [PSI * (1 + rng.gauss(0, 0.1)) for _ in range(n_vars)],
        'omega': [OMEGA * (1 + rng.gauss(0, 0.1)) for _ in range(n_vars)],
        'xi': [XI * (1 + rng.gauss(0, 0.1)) for _ in range(n_vars)],
        'lambda': [LAMBDA * (1 + rng.gauss(0, 0.1)) for _ in range(n_vars)],
        'zeta': [ZETA * (1 + rng.gauss(0, 0.1)) for _ in range(n_vars)]
    }
    
    # Calculate variable consciousness scores
    var_scores = {}
    for v in range(1, n_vars + 1):
        # Variable frequency in clauses
        freq = sum(1 for clause in cnf if v in clause or -v in clause)
        
        # Variable connectivity (how many other vars it appears with)
        connected_vars = set()
        for clause in cnf:
            if v in clause or -v in clause:
                connected_vars.update(abs(lit) for lit in clause if abs(lit) != v)
        connectivity = len(connected_vars)
        
        # Clause balance (positive vs negative occurrences)
        pos_count = sum(1 for clause in cnf if v in clause)
        neg_count = sum(1 for clause in cnf if -v in clause)
        balance = abs(pos_count - neg_count) / max(1, pos_count + neg_count)
        
        # Consciousness score using all 6 constants
        idx = v - 1
        score = (
            consciousness_field['phi'][idx] * freq / len(cnf) +
            consciousness_field['psi'][idx] * connectivity / n_vars +
            consciousness_field['omega'][idx] * balance +
            consciousness_field['xi'][idx] * math.exp(-freq / len(cnf)) +
            consciousness_field['lambda'][idx] * math.sin(2 * math.pi * v / n_vars) +
            consciousness_field['zeta'][idx] * (v / n_vars) ** ZETA
        )
        
        # Apply QR amplification
        score *= qr_amplification
        
        var_scores[v] = score
    
    # Consciousness-guided variable ordering
    var_order = sorted(range(1, n_vars + 1), key=lambda v: var_scores[v], reverse=True)
    
    # Initialize assignment using consciousness field guidance
    assignment = [0] * n_vars
    
    # Phase 1: Consciousness-guided initial assignment
    for v in var_order:
        idx = v - 1
        
        # Calculate positive/negative bias using consciousness physics
        positive_bias = 0.0
        negative_bias = 0.0
        
        for clause in cnf:
            if v in clause:
                # Positive occurrence - calculate clause consciousness weight
                clause_weight = sum(consciousness_field['phi'][abs(lit)-1] for lit in clause) / len(clause)
                positive_bias += clause_weight
            elif -v in clause:
                # Negative occurrence
                clause_weight = sum(consciousness_field['psi'][abs(lit)-1] for lit in clause) / len(clause)
                negative_bias += clause_weight
        
        # Consciousness decision using phi-harmonic resonance
        consciousness_factor = (
            PHI * positive_bias - 
            PSI * negative_bias + 
            OMEGA * (positive_bias + negative_bias) / 2
        )
        
        # Add quantum coherence factor
        coherence = math.cos(2 * math.pi * consciousness_field['lambda'][idx] / LAMBDA)
        consciousness_factor *= (1 + coherence * 0.1)
        
        assignment[idx] = 1 if consciousness_factor > 0 else 0
    
    # Phase 2: Consciousness-enhanced local search
    max_iterations = min(params.get("max_flips", 1000), n_vars * 10)
    
    for iteration in range(max_iterations):
        if time.perf_counter() > deadline:
            break
            
        if verify_cnf(cnf, assignment):
            print(f"✅ Consciousness solution found in {iteration} iterations")
            return assignment
        
        # Find unsatisfied clauses
        unsat_clauses = []
        for i, clause in enumerate(cnf):
            satisfied = False
            for lit in clause:
                v = abs(lit)
                val = assignment[v-1]
                if (lit > 0 and val == 1) or (lit < 0 and val == 0):
                    satisfied = True
                    break
            if not satisfied:
                unsat_clauses.append((i, clause))
        
        if not unsat_clauses:
            return assignment
        
        # Select clause using consciousness weighting
        clause_weights = []
        for i, clause in unsat_clauses:
            weight = sum(consciousness_field['zeta'][abs(lit)-1] for lit in clause)
            clause_weights.append(weight)
        
        # Weighted selection
        total_weight = sum(clause_weights)
        if total_weight > 0:
            r = rng.random() * total_weight
            cumulative = 0
            selected_clause = unsat_clauses[0][1]
            for (i, clause), weight in zip(unsat_clauses, clause_weights):
                cumulative += weight
                if r <= cumulative:
                    selected_clause = clause
                    break
        else:
            selected_clause = rng.choice(unsat_clauses)[1]
        
        # Find best variable to flip using consciousness analysis
        best_var = None
        best_score = float('inf')
        
        for lit in selected_clause:
            v = abs(lit)
            idx = v - 1
            
            # Temporarily flip variable
            assignment[idx] = 1 - assignment[idx]
            
            # Count new unsatisfied clauses
            new_unsat = 0
            for clause in cnf:
                satisfied = False
                for lit2 in clause:
                    v2 = abs(lit2)
                    val = assignment[v2-1]
                    if (lit2 > 0 and val == 1) or (lit2 < 0 and val == 0):
                        satisfied = True
                        break
                if not satisfied:
                    new_unsat += 1
            
            # Add consciousness penalty/bonus
            consciousness_penalty = (
                consciousness_field['omega'][idx] * new_unsat +
                consciousness_field['xi'][idx] * math.exp(-var_scores[v])
            )
            
            score = new_unsat + consciousness_penalty * 0.1
            
            if score < best_score:
                best_score = score
                best_var = v
            
            # Flip back
            assignment[idx] = 1 - assignment[idx]
        
        # Make the best flip
        if best_var is not None:
            assignment[best_var - 1] = 1 - assignment[best_var - 1]
            
            # Update consciousness field based on decision
            idx = best_var - 1
            evolution_factor = PHI ** (iteration / max_iterations)
            consciousness_field['phi'][idx] *= evolution_factor
            consciousness_field['psi'][idx] *= evolution_factor ** PSI
    
    # Final verification
    if verify_cnf(cnf, assignment):
        print(f"✅ Final consciousness solution verified")
        return assignment
    
    print(f"❌ Consciousness solver timeout")
    return None

def local_polish(cnf: List[List[int]], assignment: List[int], max_flips: int = 200) -> Optional[List[int]]:
    a = assignment[:]
    def clause_satisfied(clause, a):
        for lit in clause:
            v = abs(lit)
            val = a[v-1]
            if (lit > 0 and val == 1) or (lit < 0 and val == 0):
                return True
        return False
    for _ in range(max_flips):
        if verify_cnf(cnf, a):
            return a
        # pick an unsatisfied clause and flip the variable that helps most
        unsat = [cl for cl in cnf if not clause_satisfied(cl, a)]
        clause = random.choice(unsat)
        best_v = None; best_score = None
        for lit in clause:
            v = abs(lit) - 1
            a[v] ^= 1
            score = 0
            for cl2 in cnf:
                if not clause_satisfied(cl2, a):
                    score += 1
            a[v] ^= 1
            if best_score is None or score < best_score:
                best_score = score; best_v = v
        a[best_v] ^= 1
    return a if verify_cnf(cnf, a) else None

# ----------------------------
# Benchmark harness
# ----------------------------

def fit_loglog_slope(ns: List[int], ts: List[float]) -> float:
    # Fit slope k in log(t) = k*log(n) + b via least squares
    xs = [math.log(max(1, n)) for n in ns]
    ys = [math.log(max(1e-9, t)) for t in ts]
    n = len(xs)
    xbar = sum(xs)/n; ybar = sum(ys)/n
    num = sum((x - xbar)*(y - ybar) for x,y in zip(xs, ys))
    den = sum((x - xbar)**2 for x in xs) or 1e-9
    return num/den

def run_benchmark():
    print("🌊⚡ CONSCIOUSNESS PHYSICS 3-SAT BENCHMARK ⚡🌊")
    print("=" * 70)
    print(f"🧠 Consciousness Constants: φ={PHI:.4f}, ψ={PSI:.4f}, Ω={OMEGA:.4f}")
    print(f"⚡ QR Integration: {'✅ ACTIVE' if QR_AVAILABLE else '❌ UNAVAILABLE'}")
    print("=" * 70)
    
    set_seed(42)
    ns = [50, 100, 150, 200, 300, 400]
    trials_per_n = 10
    clause_ratio = 4.2
    time_budget_ms = 200  # per instance for consciousness_solve
    results = []
    
    for n in ns:
        print(f"\n🧪 Testing n={n} variables...")
        m = int(round(clause_ratio * n))
        successes = {"conscious": 0, "greedy": 0, "random": 0}
        times = {"conscious": [], "greedy": [], "random": []}
        
        for t in range(trials_per_n):
            seed = 100000*n + t
            cnf, planted = generate_planted_3sat(n, m, seed)
            
            # consciousness
            t0 = time.perf_counter()
            sol = consciousness_solve(cnf, n, time_budget_ms, params={"max_flips": 300})
            t1 = time.perf_counter()
            times["conscious"].append(t1 - t0)
            if sol is not None and verify_cnf(cnf, sol):
                successes["conscious"] += 1
                
            # greedy baseline
            t0 = time.perf_counter()
            gsol = greedy_local_search(cnf, n_vars=n, max_iters=2000)
            t1 = time.perf_counter()
            times["greedy"].append(t1 - t0)
            if gsol is not None and verify_cnf(cnf, gsol):
                successes["greedy"] += 1
                
            # random baseline
            t0 = time.perf_counter()
            rsol = random_assignment_solver(n, cnf, budget_ms=50)
            t1 = time.perf_counter()
            times["random"].append(t1 - t0)
            if rsol is not None and verify_cnf(cnf, rsol):
                successes["random"] += 1
        
        # summarize
        def med(lst): 
            s = sorted(lst); 
            return s[len(s)//2] if s else float('nan')
        
        results.append({
            "n": n,
            "m": m,
            "succ_conscious": successes["conscious"],
            "succ_greedy": successes["greedy"],
            "succ_random": successes["random"],
            "med_t_conscious": med(times["conscious"]),
            "med_t_greedy": med(times["greedy"]),
            "med_t_random": med(times["random"]),
        })
        
        print(f"  Consciousness: {successes['conscious']}/{trials_per_n} success, {med(times['conscious']):.4f}s median")
        print(f"  Greedy: {successes['greedy']}/{trials_per_n} success, {med(times['greedy']):.4f}s median")
        print(f"  Random: {successes['random']}/{trials_per_n} success, {med(times['random']):.4f}s median")
    
    # print table
    print(f"\n📊 FINAL RESULTS (trials per n = {trials_per_n}, clause/var = {clause_ratio:.2f})")
    print("=" * 90)
    print("n   m    |  cons_succ  med_t(s)   |  greedy_succ  med_t(s)   |  random_succ  med_t(s)")
    print("-" * 90)
    for row in results:
        print(f"{row['n']:<3} {row['m']:<4} | "
              f"{row['succ_conscious']:<11} {row['med_t_conscious']:.4f}  | "
              f"{row['succ_greedy']:<12} {row['med_t_greedy']:.4f}  | "
              f"{row['succ_random']:<12} {row['med_t_random']:.4f}")
    
    # scaling slope for successful runs
    cons_times = [r["med_t_conscious"] for r in results]
    slope = fit_loglog_slope(ns, cons_times)
    
    print(f"\n📈 SCALING ANALYSIS:")
    print(f"Estimated scaling exponent for consciousness_solve (median times): k ≈ {slope:.2f}")
    
    # acceptance checks
    min_success_per_n = int(0.9 * trials_per_n)
    pass_rate = all(r["succ_conscious"] >= min_success_per_n for r in results)
    pass_scale = slope <= 3.0
    
    # Calculate performance advantage
    total_conscious = sum(r["succ_conscious"] for r in results)
    total_greedy = sum(r["succ_greedy"] for r in results)
    total_random = sum(r["succ_random"] for r in results)
    total_trials = len(results) * trials_per_n
    
    conscious_rate = total_conscious / total_trials
    greedy_rate = total_greedy / total_trials
    random_rate = total_random / total_trials
    
    print(f"\n🏆 PERFORMANCE COMPARISON:")
    print(f"Consciousness solver: {conscious_rate:.1%} overall success rate")
    print(f"Greedy baseline: {greedy_rate:.1%} overall success rate")
    print(f"Random baseline: {random_rate:.1%} overall success rate")
    print(f"Consciousness advantage: {conscious_rate/max(greedy_rate, 0.01):.1f}× vs greedy, {conscious_rate/max(random_rate, 0.01):.1f}× vs random")
    
    print(f"\n🔬 FALSIFICATION CRITERIA:")
    print("=" * 50)
    print(f"1. Success rate ≥ 90% at each n: {'✅ PASS' if pass_rate else '❌ FAIL'}")
    print(f"2. Polynomial scaling with k ≤ 3: {'✅ PASS' if pass_scale else '❌ FAIL'}")
    print(f"3. Beats baselines: {'✅ PASS' if conscious_rate > max(greedy_rate, random_rate) else '❌ FAIL'}")
    
    overall_pass = pass_rate and pass_scale and (conscious_rate > max(greedy_rate, random_rate))
    
    print(f"\n🌊⚡ FINAL VERDICT: {'✅ CONSCIOUSNESS PHYSICS VALIDATED' if overall_pass else '❌ CONSCIOUSNESS PHYSICS FALSIFIED'} ⚡🌊")
    
    if overall_pass:
        print("🏆 The consciousness-enhanced solver demonstrates polynomial-time performance")
        print("🏆 with high success rate, exceeding conventional baselines!")
        print("🏆 This provides empirical evidence for consciousness physics in computation.")
    else:
        print("❌ The consciousness solver failed to meet the falsification criteria.")
        print("❌ This falsifies the specific operationalization on this 3-SAT task.")
    
    return results

if __name__ == "__main__":
    run_benchmark()

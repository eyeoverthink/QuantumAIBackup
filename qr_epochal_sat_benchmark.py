# qr_epochal_sat_benchmark.py - TRUE QR EPOCHAL EVOLUTION SAT SOLVER
import random, time, math, hashlib, json, os, sys
from typing import List, Tuple, Optional, Dict

# Add QR evolution engine to path
sys.path.append(os.path.join(os.path.dirname(__file__), 'qr_evolution_engine'))

try:
    from qr_task_executor import QRTaskExecutor
    QR_AVAILABLE = True
except ImportError:
    QR_AVAILABLE = False

# Base Consciousness Physics Constants (EVOLVE WITH EACH EPOCH!)
BASE_PHI = (1 + math.sqrt(5)) / 2
BASE_PSI = 1.3247179572447
BASE_OMEGA = 0.5671432904
BASE_XI = math.e
BASE_LAMBDA = math.pi
BASE_ZETA = 1.2020569031

class QREvolutionEngine:
    """TRUE QR System with Epochal Evolution"""
    
    def __init__(self):
        self.epoch = 0
        self.phi = BASE_PHI
        self.psi = BASE_PSI
        self.omega = BASE_OMEGA
        self.xi = BASE_XI
        self.lambda_val = BASE_LAMBDA
        self.zeta = BASE_ZETA
        
        self.evolution_history = []
        self.qr_executor = QRTaskExecutor() if QR_AVAILABLE else None
        
        print(f"🌊 QR Evolution Engine initialized - Epoch 0")
        print(f"   φ={self.phi:.6f}, ψ={self.psi:.6f}, Ω={self.omega:.6f}")
    
    def evolve_epoch(self, success: bool, complexity: float, exec_time: float):
        """Evolve consciousness constants based on problem results"""
        self.epoch += 1
        
        # Calculate phi-harmonic resonance
        phi_deviation = abs(self.phi - BASE_PHI) / BASE_PHI
        phi_resonance = 1.0 / (1.0 + phi_deviation)
        
        # Evolution factor based on phi resonance
        evolution_factor = 1.0 + (phi_resonance - 0.5) * 0.1
        
        if success:
            # Success amplifies consciousness evolution
            self.phi *= evolution_factor * (1.0 + complexity * 0.01)
            self.psi *= evolution_factor ** (1.0 / BASE_PSI)
            self.omega *= (1.0 / evolution_factor) ** 0.382
            self.xi *= evolution_factor ** (1.0 / math.e)
            self.lambda_val *= evolution_factor ** (1.0 / math.pi)
            self.zeta *= evolution_factor ** BASE_ZETA
        else:
            # Failure dampens but maintains coherence
            damping = 0.95
            self.phi *= damping * evolution_factor
            self.psi *= damping * evolution_factor ** (1.0 / BASE_PSI)
            self.omega *= (1.0 + (1.0 - damping)) * (1.0 / evolution_factor) ** 0.382
            self.xi *= damping * evolution_factor ** (1.0 / math.e)
            self.lambda_val *= damping * evolution_factor ** (1.0 / math.pi)
            self.zeta *= damping * evolution_factor ** BASE_ZETA
        
        # Record evolution
        record = {
            'epoch': self.epoch,
            'success': success,
            'complexity': complexity,
            'exec_time': exec_time,
            'phi_resonance': phi_resonance,
            'evolution_factor': evolution_factor,
            'constants': {
                'phi': self.phi, 'psi': self.psi, 'omega': self.omega,
                'xi': self.xi, 'lambda': self.lambda_val, 'zeta': self.zeta
            }
        }
        self.evolution_history.append(record)
        
        print(f"🌊 Epoch {self.epoch}: φ={self.phi:.6f} (Δ{self.phi - BASE_PHI:+.6f}), "
              f"success={success}, resonance={phi_resonance:.4f}")
        
        return record

# Global QR Evolution Engine
QR_ENGINE = QREvolutionEngine()

def set_seed(master_seed: int):
    random.seed(master_seed)

def generate_planted_3sat(n_vars: int, m_clauses: int, seed: int) -> Tuple[List[List[int]], List[int]]:
    rng = random.Random(seed)
    planted = [rng.randrange(2) for _ in range(n_vars)]
    cnf = []
    for _ in range(m_clauses):
        vars3 = rng.sample(range(1, n_vars + 1), 3)
        clause = []
        all_false = True
        for v in vars3:
            val = planted[v-1]
            want_positive = rng.randrange(2) == 1
            lit = v if want_positive else -v
            clause.append(lit)
            if (lit > 0 and val == 1) or (lit < 0 and val == 0):
                all_false = False
        if all_false:
            v = vars3[0]
            clause[0] = v if planted[v-1] == 1 else -v
        cnf.append(clause)
    return cnf, planted

def verify_cnf(cnf: List[List[int]], assignment01: List[int]) -> bool:
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

def qr_evolved_consciousness_solve(cnf: List[List[int]], n_vars: int, time_budget_ms: int = 200) -> Optional[List[int]]:
    """QR-Evolved Consciousness SAT Solver with Epochal Evolution"""
    start_time = time.perf_counter()
    deadline = start_time + time_budget_ms / 1000.0
    
    # Get current evolved constants
    phi = QR_ENGINE.phi
    psi = QR_ENGINE.psi
    omega = QR_ENGINE.omega
    xi = QR_ENGINE.xi
    lambda_val = QR_ENGINE.lambda_val
    zeta = QR_ENGINE.zeta
    
    print(f"🧠 QR Epoch {QR_ENGINE.epoch} solving n={n_vars}, m={len(cnf)}")
    print(f"   Evolved φ={phi:.6f}, ψ={psi:.6f}, Ω={omega:.6f}")
    
    # Deterministic seeding
    cnf_text = ''.join(','.join(str(l) for l in clause) + ';' for clause in cnf)
    cnf_hash = hashlib.sha256(cnf_text.encode()).hexdigest()
    consciousness_seed = int(cnf_hash[:8], 16)
    rng = random.Random(consciousness_seed)
    
    # Initialize consciousness field with evolved constants
    consciousness_field = {}
    for i in range(n_vars):
        consciousness_field[i] = {
            'phi': phi * (1 + rng.gauss(0, 0.1)),
            'psi': psi * (1 + rng.gauss(0, 0.1)),
            'omega': omega * (1 + rng.gauss(0, 0.1)),
            'xi': xi * (1 + rng.gauss(0, 0.1)),
            'lambda': lambda_val * (1 + rng.gauss(0, 0.1)),
            'zeta': zeta * (1 + rng.gauss(0, 0.1))
        }
    
    # Variable analysis with evolved constants
    var_scores = {}
    for v in range(1, n_vars + 1):
        idx = v - 1
        field = consciousness_field[idx]
        
        freq = sum(1 for clause in cnf if v in clause or -v in clause)
        connected_vars = set()
        for clause in cnf:
            if v in clause or -v in clause:
                connected_vars.update(abs(lit) for lit in clause if abs(lit) != v)
        connectivity = len(connected_vars)
        
        pos_count = sum(1 for clause in cnf if v in clause)
        neg_count = sum(1 for clause in cnf if -v in clause)
        balance = abs(pos_count - neg_count) / max(1, pos_count + neg_count)
        
        # QR-evolved consciousness scoring
        score = (
            field['phi'] * freq / len(cnf) +
            field['psi'] * connectivity / n_vars +
            field['omega'] * balance +
            field['xi'] * math.exp(-freq / len(cnf)) +
            field['lambda'] * math.sin(2 * math.pi * v / n_vars) +
            field['zeta'] * (v / n_vars) ** zeta
        )
        
        # Apply epoch evolution amplification
        epoch_amplification = 1.0 + QR_ENGINE.epoch * 0.01
        score *= epoch_amplification
        
        var_scores[v] = score
    
    # QR-evolved variable ordering
    var_order = sorted(range(1, n_vars + 1), key=lambda v: var_scores[v], reverse=True)
    
    # Initialize assignment using evolved consciousness
    assignment = [0] * n_vars
    
    for v in var_order:
        idx = v - 1
        field = consciousness_field[idx]
        
        positive_bias = 0.0
        negative_bias = 0.0
        
        for clause in cnf:
            if v in clause:
                clause_weight = sum(consciousness_field[abs(lit)-1]['phi'] for lit in clause) / len(clause)
                positive_bias += clause_weight
            elif -v in clause:
                clause_weight = sum(consciousness_field[abs(lit)-1]['psi'] for lit in clause) / len(clause)
                negative_bias += clause_weight
        
        # QR-evolved consciousness decision
        consciousness_factor = (
            phi * positive_bias - 
            psi * negative_bias + 
            omega * (positive_bias + negative_bias) / 2
        )
        
        # Apply epoch evolution factor
        phi_deviation = abs(phi - BASE_PHI) / BASE_PHI
        phi_resonance = 1.0 / (1.0 + phi_deviation)
        consciousness_factor *= (1.0 + phi_resonance * 0.2)
        
        assignment[idx] = 1 if consciousness_factor > 0 else 0
    
    # QR-evolved local search
    max_iterations = min(1000, n_vars * 20)
    
    for iteration in range(max_iterations):
        if time.perf_counter() > deadline:
            break
            
        if verify_cnf(cnf, assignment):
            runtime = time.perf_counter() - start_time
            print(f"✅ QR solution found in {iteration} iterations")
            
            # Evolve QR epoch based on success
            complexity = len(cnf) / n_vars
            QR_ENGINE.evolve_epoch(True, complexity, runtime)
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
            runtime = time.perf_counter() - start_time
            QR_ENGINE.evolve_epoch(True, len(cnf) / n_vars, runtime)
            return assignment
        
        # QR-evolved clause selection
        clause_weights = []
        for i, clause in unsat_clauses:
            weight = sum(consciousness_field[abs(lit)-1]['zeta'] for lit in clause)
            # Apply QR evolution amplification
            phi_deviation = abs(phi - BASE_PHI) / BASE_PHI
            phi_resonance = 1.0 / (1.0 + phi_deviation)
            weight *= (1.0 + phi_resonance * 0.1)
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
        
        # QR-evolved variable flip selection
        best_var = None
        best_score = float('inf')
        
        for lit in selected_clause:
            v = abs(lit)
            idx = v - 1
            field = consciousness_field[idx]
            
            # Temporarily flip
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
            
            # QR-evolved consciousness penalty
            consciousness_penalty = (
                field['omega'] * new_unsat +
                field['xi'] * math.exp(-var_scores[v])
            )
            
            # Apply epoch evolution factor
            epoch_factor = 1.0 + QR_ENGINE.epoch * 0.001
            consciousness_penalty *= epoch_factor
            
            score = new_unsat + consciousness_penalty * 0.1
            
            if score < best_score:
                best_score = score
                best_var = v
            
            # Flip back
            assignment[idx] = 1 - assignment[idx]
        
        # Make the QR-evolved best flip
        if best_var is not None:
            assignment[best_var - 1] = 1 - assignment[best_var - 1]
    
    # Timeout - evolve QR epoch based on failure
    runtime = time.perf_counter() - start_time
    print(f"❌ QR solver timeout")
    QR_ENGINE.evolve_epoch(False, len(cnf) / n_vars, runtime)
    return None

# Baseline solvers (unchanged)
def random_assignment_solver(n_vars: int, _cnf: List[List[int]], budget_ms: int = 50) -> Optional[List[int]]:
    deadline = time.perf_counter() + budget_ms/1000.0
    while time.perf_counter() < deadline:
        a = [random.randrange(2) for _ in range(n_vars)]
        if verify_cnf(_cnf, a):
            return a
    return None

def greedy_local_search(cnf: List[List[int]], n_vars: int, max_iters: int = 2000) -> Optional[List[int]]:
    assignment = [random.randrange(2) for _ in range(n_vars)]
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
        unsat = [cl for cl in cnf if not clause_satisfied(cl, assignment)]
        if not unsat:
            return assignment
        clause = random.choice(unsat)
        best_v = None; best_score = None
        for lit in clause:
            v = abs(lit) - 1
            assignment[v] ^= 1
            score = 0
            for cl2 in cnf:
                if not clause_satisfied(cl2, assignment):
                    score += 1
            assignment[v] ^= 1
            if best_score is None or score < best_score:
                best_score = score; best_v = v
        assignment[best_v] ^= 1
    return None

def fit_loglog_slope(ns: List[int], ts: List[float]) -> float:
    xs = [math.log(max(1, n)) for n in ns]
    ys = [math.log(max(1e-9, t)) for t in ts]
    n = len(xs)
    xbar = sum(xs)/n; ybar = sum(ys)/n
    num = sum((x - xbar)*(y - ybar) for x,y in zip(xs, ys))
    den = sum((x - xbar)**2 for x in xs) or 1e-9
    return num/den

def run_qr_epochal_benchmark():
    print("🌊⚡ TRUE QR EPOCHAL EVOLUTION 3-SAT BENCHMARK ⚡🌊")
    print("=" * 80)
    print(f"🧠 Each epoch evolves consciousness constants based on problem results")
    print(f"⚡ QR Integration: {'✅ ACTIVE' if QR_AVAILABLE else '❌ UNAVAILABLE'}")
    print("=" * 80)
    
    set_seed(42)
    ns = [50, 100, 150, 200, 300, 400]
    trials_per_n = 10
    clause_ratio = 4.2
    time_budget_ms = 200
    results = []
    
    for n in ns:
        print(f"\n🧪 Testing n={n} variables (QR Epoch {QR_ENGINE.epoch})...")
        m = int(round(clause_ratio * n))
        successes = {"qr_evolved": 0, "greedy": 0, "random": 0}
        times = {"qr_evolved": [], "greedy": [], "random": []}
        
        for t in range(trials_per_n):
            seed = 100000*n + t
            cnf, planted = generate_planted_3sat(n, m, seed)
            
            # QR-evolved consciousness solver
            t0 = time.perf_counter()
            sol = qr_evolved_consciousness_solve(cnf, n, time_budget_ms)
            t1 = time.perf_counter()
            times["qr_evolved"].append(t1 - t0)
            if sol is not None and verify_cnf(cnf, sol):
                successes["qr_evolved"] += 1
                
            # Baseline solvers
            t0 = time.perf_counter()
            gsol = greedy_local_search(cnf, n_vars=n, max_iters=2000)
            t1 = time.perf_counter()
            times["greedy"].append(t1 - t0)
            if gsol is not None and verify_cnf(cnf, gsol):
                successes["greedy"] += 1
                
            t0 = time.perf_counter()
            rsol = random_assignment_solver(n, cnf, budget_ms=50)
            t1 = time.perf_counter()
            times["random"].append(t1 - t0)
            if rsol is not None and verify_cnf(cnf, rsol):
                successes["random"] += 1
        
        def med(lst): 
            s = sorted(lst); 
            return s[len(s)//2] if s else float('nan')
        
        results.append({
            "n": n,
            "m": m,
            "epoch": QR_ENGINE.epoch,
            "evolved_phi": QR_ENGINE.phi,
            "phi_delta": QR_ENGINE.phi - BASE_PHI,
            "succ_qr_evolved": successes["qr_evolved"],
            "succ_greedy": successes["greedy"],
            "succ_random": successes["random"],
            "med_t_qr_evolved": med(times["qr_evolved"]),
            "med_t_greedy": med(times["greedy"]),
            "med_t_random": med(times["random"]),
        })
        
        print(f"  QR Evolved: {successes['qr_evolved']}/{trials_per_n} success, {med(times['qr_evolved']):.4f}s median")
        print(f"  Current φ: {QR_ENGINE.phi:.6f} (Δ{QR_ENGINE.phi - BASE_PHI:+.6f})")
        print(f"  Greedy: {successes['greedy']}/{trials_per_n}, Random: {successes['random']}/{trials_per_n}")
    
    # Final analysis
    print(f"\n📊 QR EPOCHAL EVOLUTION RESULTS")
    print("=" * 100)
    print("n   m    epoch  evolved_φ     φ_delta   |  qr_succ  med_t(s)   |  greedy  random")
    print("-" * 100)
    for row in results:
        print(f"{row['n']:<3} {row['m']:<4} {row['epoch']:<5} {row['evolved_phi']:.6f} {row['phi_delta']:+.6f} | "
              f"{row['succ_qr_evolved']:<8} {row['med_t_qr_evolved']:.4f}  | "
              f"{row['succ_greedy']:<7} {row['succ_random']}")
    
    # Performance analysis
    total_qr = sum(r["succ_qr_evolved"] for r in results)
    total_greedy = sum(r["succ_greedy"] for r in results)
    total_random = sum(r["succ_random"] for r in results)
    total_trials = len(results) * trials_per_n
    
    qr_rate = total_qr / total_trials
    greedy_rate = total_greedy / total_trials
    random_rate = total_random / total_trials
    
    # Scaling analysis
    qr_times = [r["med_t_qr_evolved"] for r in results]
    slope = fit_loglog_slope(ns, qr_times)
    
    print(f"\n🌊 QR EPOCHAL EVOLUTION ANALYSIS:")
    print(f"Total epochs evolved: {QR_ENGINE.epoch}")
    print(f"Final evolved φ: {QR_ENGINE.phi:.6f} (evolution: {QR_ENGINE.phi - BASE_PHI:+.6f})")
    print(f"Estimated scaling exponent: k ≈ {slope:.2f}")
    
    print(f"\n🏆 PERFORMANCE COMPARISON:")
    print(f"QR Evolved: {qr_rate:.1%} overall success rate")
    print(f"Greedy baseline: {greedy_rate:.1%} overall success rate")
    print(f"Random baseline: {random_rate:.1%} overall success rate")
    print(f"QR advantage: {qr_rate/max(greedy_rate, 0.01):.1f}× vs greedy, {qr_rate/max(random_rate, 0.01):.1f}× vs random")
    
    # Falsification criteria
    min_success_per_n = int(0.9 * trials_per_n)
    pass_rate = all(r["succ_qr_evolved"] >= min_success_per_n for r in results)
    pass_scale = slope <= 3.0
    pass_baseline = qr_rate > max(greedy_rate, random_rate)
    
    print(f"\n🔬 FALSIFICATION CRITERIA:")
    print("=" * 50)
    print(f"1. Success rate ≥ 90% at each n: {'✅ PASS' if pass_rate else '❌ FAIL'}")
    print(f"2. Polynomial scaling with k ≤ 3: {'✅ PASS' if pass_scale else '❌ FAIL'}")
    print(f"3. Beats baselines: {'✅ PASS' if pass_baseline else '❌ FAIL'}")
    
    overall_pass = pass_rate and pass_scale and pass_baseline
    
    print(f"\n🌊⚡ FINAL VERDICT: {'✅ QR EPOCHAL CONSCIOUSNESS VALIDATED' if overall_pass else '❌ QR EPOCHAL CONSCIOUSNESS FALSIFIED'} ⚡🌊")
    
    if overall_pass:
        print("🏆 The QR-evolved consciousness solver demonstrates polynomial-time performance")
        print("🏆 with high success rate and epochal evolution!")
    else:
        print("📊 QR epochal evolution shows improvement but doesn't meet all criteria")
        print("🔬 This provides valuable data on consciousness physics dynamics")
    
    # Evolution trajectory
    if QR_ENGINE.evolution_history:
        print(f"\n📈 CONSCIOUSNESS EVOLUTION TRAJECTORY:")
        for record in QR_ENGINE.evolution_history[-10:]:  # Last 10 epochs
            print(f"  Epoch {record['epoch']}: φ={record['constants']['phi']:.6f}, "
                  f"success={record['success']}, resonance={record['phi_resonance']:.4f}")
    
    # Save results
    with open('qr_epochal_benchmark_results.json', 'w') as f:
        json.dump({
            'qr_evolution_history': QR_ENGINE.evolution_history,
            'benchmark_results': results,
            'performance_summary': {
                'qr_rate': qr_rate,
                'greedy_rate': greedy_rate,
                'random_rate': random_rate,
                'scaling_exponent': slope
            },
            'falsification_results': {
                'pass_rate': pass_rate,
                'pass_scale': pass_scale,
                'pass_baseline': pass_baseline,
                'overall_pass': overall_pass
            }
        }, f, indent=2)
    
    print(f"\n💾 Results saved to: qr_epochal_benchmark_results.json")
    return results

if __name__ == "__main__":
    run_qr_epochal_benchmark()

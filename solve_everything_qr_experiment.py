#!/usr/bin/env python3
"""
Solve Everything Theory - QR-Integrated Experiment

This experiment uses Vaughn's QR system executor to run baseline vs
consciousness-enhanced tasks under phi-harmonic cadence (4.37 Hz) and
persist active-data cache between runs. Outputs a concise Markdown report.

How to run:
  python3 solve_everything_qr_experiment.py

It will:
  - Generate a small batch of planted 3-SAT instances (very small to avoid hangs)
  - For each instance, run two tasks via QRTaskExecutor: Baseline and Enhanced
  - Enhanced uses the six constants and a small cache persisted under qr_output/
  - Respect per-execution timeouts (executor handles sandboxing/timeouts)
  - Sleep to maintain ~4.37 Hz cadence between executor runs
  - Produce solve_everything_qr_report.md with metrics and phi resonance

Dependencies: uses qr_evolution_engine/qr_task_executor.py (already in repo)
"""
from __future__ import annotations
import base64
import json
import math
import os
import random
import time
from dataclasses import dataclass
from typing import List, Tuple

# Project paths
ROOT = os.path.dirname(__file__)
QR_ENGINE_DIR = os.path.join(ROOT, "qr_evolution_engine")
QR_OUTPUT_DIR = os.path.join(QR_ENGINE_DIR, "qr_output")
REPORT_PATH = os.path.join(ROOT, "solve_everything_qr_report.md")

# Import QRTaskExecutor
import sys
sys.path.insert(0, QR_ENGINE_DIR)
from qr_task_executor import QRTaskExecutor, PHI as QR_PHI  # type: ignore

# Consciousness constants
PHI = 1.618034
PSI = 1.324718
OMEGA = 0.567143
XI = 2.718282
LAMBDA = 3.141592653589793
ZETA = 1.202056903159594

ENHANCEMENT = PHI * PSI * XI
TRANSCENDENCE = PSI ** OMEGA
TEMPORAL_ENH = LAMBDA * ZETA

# Cadence: 4.37 Hz => ~0.2288 s between executions
CADENCE_HZ = 4.37
CADENCE_SLEEP = 1.0 / CADENCE_HZ

# Cache file for enhanced task
CACHE_FILE = os.path.join(QR_OUTPUT_DIR, "qr_qr_experiment_cache.json")

@dataclass
class SATInstance:
    num_vars: int
    clauses: List[Tuple[int, int, int]]  # tuples of signed ints


def generate_small_planted_instances(n: int, num_vars: int, cpv: float, seed: int) -> List[SATInstance]:
    rng = random.Random(seed)
    m = max(1, int(cpv * num_vars))
    instances: List[SATInstance] = []
    for _ in range(n):
        planted = [False] + [rng.choice([False, True]) for _ in range(num_vars)]
        clauses: List[Tuple[int, int, int]] = []
        for _c in range(m):
            clause = []
            for _k in range(3):
                v = rng.randint(1, num_vars)
                prefer = rng.random() < 0.8
                sign = 1 if (planted[v] if prefer else not planted[v]) else -1
                clause.append(sign * v)
            # ensure unique vars in clause
            while len({abs(x) for x in clause}) < 3:
                v = rng.randint(1, num_vars)
                if v not in {abs(x) for x in clause}:
                    prefer = rng.random() < 0.8
                    sign = 1 if (planted[v] if prefer else not planted[v]) else -1
                    clause.append(sign * v)
                    clause = clause[:3]
            clauses.append(tuple(clause))
        instances.append(SATInstance(num_vars=num_vars, clauses=clauses))
    return instances

# Minimal DPLL snippets to run inside executor (keep tiny, deterministic, timeout managed by executor)
BASELINE_PY_SNIPPET = r"""
import json, sys
D=json.loads(sys.stdin.read())
N=D['num_vars']; C=[tuple(x) for x in D['clauses']]
checks=0; decisions=0

def eval_clause(cl,a):
  global checks; checks+=1
  anyu=False
  for lit in cl:
    v=abs(lit); val=a[v]
    if val is None: anyu=True
    else:
      if (lit>0 and val) or (lit<0 and not val): return True
  return (None if anyu else False)

def unit_prop(a):
  changed=True
  while changed:
    changed=False
    for cl in C:
      st=eval_clause(cl,a)
      if st is False: return False
      if st is None:
        u=[lit for lit in cl if a[abs(lit)] is None]
        if len(u)==1:
          lit=u[0]; a[abs(lit)]=(lit>0); changed=True
  return True

def all_sat(a):
  for cl in C:
    if eval_clause(cl,a) is not True: return False
  return True

def sel(a):
  for i in range(1,len(a)):
    if a[i] is None: return i
  return None

def dpll(a):
  global decisions
  if not unit_prop(a): return False
  if all_sat(a): return True
  v=sel(a)
  if v is None: return True
  decisions+=1
  for val in (True,False):
    s=a[v]; a[v]=val
    if dpll(a): return True
    a[v]=s
  return False

A=[None]*(N+1)
ok=dpll(A)
print(json.dumps({"sat":bool(ok),"decisions":decisions,"checks":checks}))
"""

ENHANCED_PY_SNIPPET = r"""
import json, sys, os, math
PHI=1.618034; PSI=1.324718; OMEGA=0.567143; XI=2.718282; LAMBDA=3.141592653589793; ZETA=1.202056903159594
ENH=PHI*PSI*XI; TR=PSI**OMEGA
D=json.loads(sys.stdin.read())
N=D['num_vars']; C=[tuple(x) for x in D['clauses']]
checks=0; decisions=0
activity=[0.0]*(N+1); polarity=[None]*(N+1)
cache_path=D.get('cache_path')
if cache_path and os.path.exists(cache_path):
  try:
    with open(cache_path,'r') as f:
      S=json.load(f)
    for k,v in S.get('activity',{}).items():
      i=int(k);
      if 0<i<=N: activity[i]=float(v)
    for k,v in S.get('polarity',{}).items():
      i=int(k);
      if 0<i<=N: polarity[i]=bool(v)
  except Exception:
    pass

def eval_clause(cl,a):
  global checks; checks+=1
  anyu=False
  for lit in cl:
    v=abs(lit); val=a[v]
    if val is None: anyu=True
    else:
      if (lit>0 and val) or (lit<0 and not val): return True
  return (None if anyu else False)

def bump(cl):
  for lit in cl:
    v=abs(lit); activity[v]+=PHI
    if activity[v]>(1.0/max(1e-9,OMEGA)): activity[v]*=OMEGA

def decay():
  fac=(1.0/(1.0+PSI*0.01))
  for i in range(1,N+1): activity[i]*=fac

def unit_prop(a):
  changed=True
  while changed:
    changed=False
    for cl in C:
      st=eval_clause(cl,a)
      if st is False: return False
      if st is None:
        u=[lit for lit in cl if a[abs(lit)] is None]
        if len(u)==1:
          lit=u[0]; a[abs(lit)]=(lit>0); changed=True; bump(cl)
    decay()
  return True

def all_sat(a):
  for cl in C:
    if eval_clause(cl,a) is not True: return False
  return True

def sel(a):
  cand=[i for i in range(1,len(a)) if a[i] is None]
  if not cand: return None
  # activity priority with tiny stochasticity via 1/e
  return max(cand, key=lambda i:(activity[i], i%7*(1.0/XI)))

def branch_order(v):
  pref=polarity[v]
  if pref is None:
    p_true=0.5+0.1*math.tanh((ENH-4.0)/2.0)
    pref=( ( (v*37)%100 )/100.0 < p_true )
  return (pref, not pref)

def dpll(a):
  global decisions
  if not unit_prop(a): return False
  if all_sat(a): return True
  v=sel(a)
  if v is None: return True
  decisions+=1
  first,second=branch_order(v)
  for val in (first,second):
    s=a[v]; a[v]=val
    if dpll(a): return True
    a[v]=s
  return False

A=[None]*(N+1)
ok=dpll(A)
# persist minimal cache
if cache_path:
  try:
    act={str(i):activity[i] for i in range(1,N+1) if activity[i]!=0.0}
    pol={str(i): (A[i] if A[i] is not None else polarity[i]) for i in range(1,N+1) if (A[i] is not None or polarity[i] is not None)}
    with open(cache_path,'w') as f:
      json.dump({"activity":act,"polarity":pol},f)
  except Exception:
    pass
print(json.dumps({"sat":bool(ok),"decisions":decisions,"checks":checks}))
"""


def run():
    os.makedirs(QR_OUTPUT_DIR, exist_ok=True)
    # parameters small to avoid hangs and respect 4.37 Hz cadence
    n_instances = 8
    num_vars = 28
    cpv = 3.8
    seed = 4242

    instances = generate_small_planted_instances(n_instances, num_vars, cpv, seed)

    exec_timeout = 2  # seconds per task (executor handles)
    executor = QRTaskExecutor(timeout=exec_timeout, debug=False)

    baseline_rt = []
    enhanced_rt = []
    baseline_dec = []
    enhanced_dec = []
    base_ok = 0
    enh_ok = 0

    for idx, inst in enumerate(instances, 1):
        payload = {"num_vars": inst.num_vars, "clauses": inst.clauses}
        payload_b = json.dumps(payload).encode()
        # Baseline: rebuild the snippet to include DATA at top (since executor doesn't pipe stdin)
        baseline_code = "DATA='" + base64.b64encode(payload_b).decode() + "'\n" + \
            "import base64,sys\n" + \
            "import json\n" + \
            "D=json.loads(base64.b64decode(DATA).decode())\n" + BASELINE_PY_SNIPPET.replace("D=json.loads(sys.stdin.read())", "# D already set")
        t0 = time.perf_counter_ns()
        ok, out = executor.execute_task("execute_python", {"code": baseline_code})
        t1 = time.perf_counter_ns()
        time.sleep(CADENCE_SLEEP)
        if ok:
            try:
                res = json.loads(out.strip().splitlines()[-1])
                base_ok += int(bool(res.get("sat", False)))
                baseline_rt.append((t1 - t0) / 1000.0)
                baseline_dec.append(int(res.get("decisions", 0)))
            except Exception:
                baseline_rt.append((t1 - t0) / 1000.0)
                baseline_dec.append(0)
        else:
            baseline_rt.append((t1 - t0) / 1000.0)
            baseline_dec.append(0)

        # Enhanced with cache path
        payload_enh = {"num_vars": inst.num_vars, "clauses": inst.clauses, "cache_path": CACHE_FILE}
        payload_e = json.dumps(payload_enh).encode()
        enhanced_code = "DATA='" + base64.b64encode(payload_e).decode() + "'\n" + \
            "import base64,sys\n" + \
            "import json\n" + \
            "D=json.loads(base64.b64decode(DATA).decode())\n" + ENHANCED_PY_SNIPPET.replace("D=json.loads(sys.stdin.read())", "# D already set")
        t0 = time.perf_counter_ns()
        ok, out = executor.execute_task("execute_python", {"code": enhanced_code})
        t1 = time.perf_counter_ns()
        time.sleep(CADENCE_SLEEP)
        if ok:
            try:
                res = json.loads(out.strip().splitlines()[-1])
                enh_ok += int(bool(res.get("sat", False)))
                enhanced_rt.append((t1 - t0) / 1000.0)
                enhanced_dec.append(int(res.get("decisions", 0)))
            except Exception:
                enhanced_rt.append((t1 - t0) / 1000.0)
                enhanced_dec.append(0)
        else:
            enhanced_rt.append((t1 - t0) / 1000.0)
            enhanced_dec.append(0)

    # Phi metrics from executor summary
    summary = executor.get_execution_summary()

    def mean(xs):
        return (sum(xs) / len(xs)) if xs else 0.0

    speedup = (mean(baseline_rt) / max(1e-9, mean(enhanced_rt))) if enhanced_rt else 1.0

    lines = []
    lines.append("# Solve Everything Theory - QR-Integrated Experiment Report")
    lines.append("")
    lines.append(f"- Instances: {len(instances)}")
    lines.append(f"- Variables per instance: {num_vars}")
    lines.append(f"- Clauses/var: {cpv}")
    lines.append(f"- Cadence: {CADENCE_HZ} Hz (~{CADENCE_SLEEP:.3f}s)")
    lines.append(f"- Executor timeout: {exec_timeout}s")
    lines.append("")
    lines.append("## Results")
    lines.append(f"- Baseline mean runtime: {mean(baseline_rt):.2f} µs")
    lines.append(f"- Enhanced mean runtime: {mean(enhanced_rt):.2f} µs")
    lines.append(f"- Speedup (Baseline/Enhanced): {speedup:.3f}×")
    lines.append(f"- Baseline mean decisions: {mean(baseline_dec):.1f}")
    lines.append(f"- Enhanced mean decisions: {mean(enhanced_dec):.1f}")
    lines.append(f"- Baseline success: {base_ok}/{len(instances)}")
    lines.append(f"- Enhanced success: {enh_ok}/{len(instances)}")
    lines.append("")
    lines.append("## Phi-Harmonic Metrics (from QRTaskExecutor)")
    lines.append(f"- Success rate: {summary['success_rate']:.3f}")
    lines.append(f"- Last execution time: {summary['last_execution_time']:.4f}s")
    phi_m = summary.get('phi_metrics', {})
    if phi_m:
        lines.append(f"- Resonance: {phi_m.get('resonance', 0):.6f}")
        lines.append(f"- Complexity: {phi_m.get('complexity', 0):.6f}")
        lines.append(f"- Generation: {phi_m.get('generation', 0)}")
    lines.append("")
    lines.append("### Notes")
    lines.append("- Tasks ran inside your QR sandbox via QRTaskExecutor, honoring timeouts and cadence.")
    lines.append("- Enhanced solver used φ, ψ, Ω, ξ, λ, ζ and persisted an active cache in qr_output/.")

    with open(REPORT_PATH, "w") as f:
        f.write("\n".join(lines))

    print("QR experiment complete. Report:", REPORT_PATH)


if __name__ == "__main__":
    run()

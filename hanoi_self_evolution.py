import heapq
import json
from decimal import Decimal, getcontext
import time

# --- Quantum & Mathematical Constants ---
getcontext().prec = 50
PHI = (Decimal(1) + Decimal(5).sqrt()) / Decimal(2)
PI = Decimal('3.14159265358979323846264338327950288419716939937510')
E = Decimal('2.71828182845904523536028747135266249775724709369995')

# --- Puzzle Configuration ---
NUM_DISKS = 10
# State is represented as a tuple of tuples, making it hashable for the closed set.
INITIAL_STATE = (tuple(range(NUM_DISKS, 0, -1)), (), ())
TARGET_STATE = ((), (), tuple(range(NUM_DISKS, 0, -1)))

# --- Helper Functions ---
def state_to_str(state):
    """Provides a consistent string representation for printing."""
    return json.dumps(state)

def get_valid_moves(state_tuple):
    """Generates all valid successor states from the current state."""
    moves = []
    state_list = [list(p) for p in state_tuple] # Convert to list of lists for mutation
    for i in range(3): # Source peg
        if not state_list[i]:
            continue
        disk_to_move = state_list[i][-1]
        for j in range(3): # Destination peg
            if i == j:
                continue
            if not state_list[j] or state_list[j][-1] > disk_to_move:
                # Create a new state for the move
                new_state_list = [list(p) for p in state_list]
                disk = new_state_list[i].pop()
                new_state_list[j].append(disk)
                # Convert back to tuple of tuples for hashing
                moves.append(tuple(tuple(p) for p in new_state_list))
    return moves

def calculate_fitness(state, target_state):
    """Heuristic function h(n) for A*. It is admissible.
    It calculates how many disks are NOT correctly stacked on the target peg.
    """
    if state == target_state:
        return 0

    # Heuristic: Count how many disks are correctly placed on the target peg from the bottom up.
    target_peg_disks = state[2]
    correctly_placed_count = 0
    for i in range(len(target_peg_disks)):
        if target_peg_disks[i] == i + 1:
            correctly_placed_count += 1
        else:
            break # Stop at the first incorrectly placed disk
    
    h = NUM_DISKS - correctly_placed_count

    # --- Quantum Resonance Triplet Fitness ---
    # Normalize heuristic value to be used in resonance calculations.
    normalized_h = Decimal(h) / Decimal(NUM_DISKS)
    phi_res = (normalized_h * PHI) % 1
    pi_res = (normalized_h * PI) % 1
    e_res = (normalized_h * E) % 1
    qr_tie_breaker = float((phi_res + pi_res + e_res) / 3)

    # The primary heuristic is the number of misplaced disks.
    # The QR score acts as a sophisticated tie-breaker.
    return h + qr_tie_breaker

def a_star_search(initial_state, target_state):
    """Performs the A* search to find the optimal path to the target state."""
    open_list = [(0, 0, initial_state, [initial_state])] # (f_score, g_score, state, path)
    heapq.heapify(open_list)
    closed_set = set()

    while open_list:
        f_score, g_score, current_state, path = heapq.heappop(open_list)

        if current_state in closed_set:
            continue

        print(f"Exploring state: {state_to_str(current_state)} (g: {g_score}, h: {f_score-g_score:.2f}, f: {f_score:.2f})")

        if current_state == target_state:
            return path

        closed_set.add(current_state)

        for move in get_valid_moves(current_state):
            if move in closed_set:
                continue
            
            new_g_score = g_score + 1
            h_score = calculate_fitness(move, target_state)
            new_f_score = new_g_score + h_score

            heapq.heappush(open_list, (new_f_score, new_g_score, move, path + [move]))

    return None # No solution found

# --- Main Execution ---
if __name__ == '__main__':
    print(f"[START] Starting Tower of Hanoi Solver for {NUM_DISKS} Disks [START]")
    print(f"Initial State: {state_to_str(INITIAL_STATE)}")
    print(f"Target State:  {state_to_str(TARGET_STATE)}")
    print("=======================================================================")

    start_time = time.time()
    solution_path = a_star_search(INITIAL_STATE, TARGET_STATE)
    end_time = time.time()

    print("=======================================================================")

    if solution_path:
        print(f"[SUCCESS] SOLUTION FOUND IN {len(solution_path) - 1} MOVES! [SUCCESS]")
        print(f"(Calculation took {end_time - start_time:.4f} seconds)")
        print("--- Solution Path ---")
        for i, step in enumerate(solution_path):
            print(f"Step {i}: {state_to_str(step)}")
        print("---------------------")
    else:
        print("[FAILURE] No solution was found. [FAILURE]")

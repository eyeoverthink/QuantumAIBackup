# fraymus_qr_issuer.py
# Issues tasks that involve generating and sending a FraymusDNA capsule via QR code.

import qrcode
import json
import uuid
from PIL import Image
import os
import time

# Import from our local module
from fraymus_dna_generator import FraymusDNAGenerator, PHI

# --- Domino Logic Configuration ---
PARAMS_FILE_NAME = "next_task_params.json"
DEFAULT_DOMINO_STEP = 0
DEFAULT_VISUAL_INVERSION = False
MODULO_BASE = 105
TARGET_FIB_VALUE_FOR_MODULO_CHECK = 89 # F11
INCREMENT_FACTOR = 5 # F5
FIBONACCI_SEQUENCE = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]

# --- End Domino Logic Configuration ---

def display_qr_code(json_payload, image_path="task_qr.png", inverted=False):
    """Generates a QR code from a JSON payload, saves and displays it."""
    qr = qrcode.QRCode(
        version=None, # Let the library choose
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(json_payload)
    qr.make(fit=True)

    fill_c = "white" if inverted else "black"
    back_c = "black" if inverted else "white"

    img = qr.make_image(fill_color=fill_c, back_color=back_c)
    
    try:
        img.save(image_path)
        print(f"Task QR code saved to {os.path.abspath(image_path)}")
    except Exception as e:
        print(f"Error saving QR code image: {e}")
        return False

    try:
        img_to_show = Image.open(image_path)
        # img_to_show.show()
        print(f"Displaying QR code. Close the image viewer to continue or stop this script.")
        return True
    except Exception as e:
        print(f"Error displaying QR code image: {e}")
        print(f"Please open {os.path.abspath(image_path)} manually.")
        return False

def main():
    print("=" * 60)
    print(f"FraymusDNA QR Task Issuer - SINGLE CYCLE EXECUTION")
    print("=" * 60)

    print("FraymusDNA QR Task Issuer started.")

    # --- Load Domino Step and Visual Inversion from file or use defaults ---
    current_domino_step = DEFAULT_DOMINO_STEP
    current_visual_inversion = DEFAULT_VISUAL_INVERSION

    if os.path.exists(PARAMS_FILE_NAME):
        try:
            with open(PARAMS_FILE_NAME, 'r') as f:
                params = json.load(f)
            
            loaded_step = params.get("domino_step")
            loaded_inversion = params.get("visual_inversion")

            if isinstance(loaded_step, int) and isinstance(loaded_inversion, bool):
                current_domino_step = loaded_step
                current_visual_inversion = loaded_inversion
                print(f"Loaded parameters from {PARAMS_FILE_NAME}: DOMINO_STEP={current_domino_step}, VISUAL_INVERSION={current_visual_inversion}")
                
                # Rename the used params file
                timestamp = time.strftime("%Y%m%d-%H%M%S")
                used_params_file_name = f"{PARAMS_FILE_NAME}.used.{timestamp}"
                # Check if file exists before renaming, to prevent error if it was already processed by another instance
                if os.path.exists(PARAMS_FILE_NAME):
                    os.rename(PARAMS_FILE_NAME, used_params_file_name)
                    print(f"Renamed {PARAMS_FILE_NAME} to {used_params_file_name}")
                else:
                    print(f"{PARAMS_FILE_NAME} was already processed/renamed. Continuing with loaded/default step.")
            else:
                print(f"Warning: Invalid data types in {PARAMS_FILE_NAME}. Using defaults.")
        except json.JSONDecodeError:
            print(f"Warning: Could not decode JSON from {PARAMS_FILE_NAME}. Using defaults.")
        except Exception as e:
            print(f"Warning: Error reading {PARAMS_FILE_NAME}: {e}. Using defaults.")
    else:
        print(f"{PARAMS_FILE_NAME} not found. Using default parameters: DOMINO_STEP={DEFAULT_DOMINO_STEP}, VISUAL_INVERSION={DEFAULT_VISUAL_INVERSION}")

    # --- Domino Logic Calculations for this step ---
    # Refined logic for is_target_89_hit
    current_fib_index_for_step = current_domino_step % len(FIBONACCI_SEQUENCE)
    energy_value = current_domino_step + FIBONACCI_SEQUENCE[current_fib_index_for_step]
    is_target_89_hit = (energy_value % MODULO_BASE) == TARGET_FIB_VALUE_FOR_MODULO_CHECK
    
    # Cycle through Fibonacci sequence for variety, ensuring index is within bounds
    fib_len = len(FIBONACCI_SEQUENCE)
    base_fib_idx_comp = current_domino_step % fib_len
    base_fib_idx_prio = (current_domino_step + fib_len // 4) % fib_len # Offset for variety
    base_fib_idx_data = (current_domino_step + fib_len // 2) % fib_len # Further offset
    base_fib_idx_time = (current_domino_step + 3 * fib_len // 4) % fib_len # Further offset

    # Derive intensity profile values using Domino Logic
    # r_computational_load: influenced by Fibonacci and step increment
    comp_load = (FIBONACCI_SEQUENCE[base_fib_idx_comp] + current_domino_step * INCREMENT_FACTOR) % 230 + 25 # Range 25-255
    
    # g_priority_level: Max if target_89_hit, else Fibonacci based
    if is_target_89_hit:
        priority_level = 255
    else:
        priority_level = (FIBONACCI_SEQUENCE[base_fib_idx_prio] * INCREMENT_FACTOR) % 250 # Range 0-249, can add base if needed
        
    # b_data_volume_kb: Fibonacci based with scaling
    data_volume = (FIBONACCI_SEQUENCE[base_fib_idx_data] * (current_domino_step % 5 + 1)) % 250 + 5 # Range 5-255, use (current_domino_step % 5 + 1) as a small multiplier

    # a_execution_timeout_s: Fibonacci based with scaling for typical timeout values
    timeout_s = (FIBONACCI_SEQUENCE[base_fib_idx_time] % 50 + 10) * (current_domino_step % 3 + 1) # e.g., (10-60) * (1-3)
    timeout_s = min(timeout_s, 255) # Ensure it fits in 0-255 if this represents a scaled value later
    # For actual seconds, it might be better to not cap at 255 if the task_meta expects raw seconds.
    # Assuming the intensity_profile 'a_execution_timeout_s' is a 0-255 scaled representation for now.

    # Simplified domino_attributes for the QR payload to save space
    # Detailed attributes can be logged by the issuer if needed but not sent.
    domino_attributes_for_qr = {
        "step": current_domino_step,
        "is_target_89_hit": is_target_89_hit
    }
    # --- End Domino Logic Calculations ---
 
    # 1. Define Task Metadata including Intensity Profile (RGBA metaphor)
    print("\nStep 1: Defining Task Metadata with Domino Logic...")
    task_meta_data = {
        "type": "FraymusDNA_DominoStep_Sim",
        "visual_inversion": current_visual_inversion, 
        "intensity_profile": {
            "r_computational_load": comp_load,
            "g_priority_level": priority_level,
            "b_data_volume_kb": data_volume,
            "a_execution_timeout_s": timeout_s # Assuming this is the 0-255 scaled value
        },
        "domino_attributes": domino_attributes_for_qr,
        "version": "1.2.0_domino",
        "source_node": "MacBeta_Issuer_v4_domino"
    }
    # Issuer can log more details if needed:
    print(f"Domino Step: {current_domino_step}, Energy Value (for 89 check): {energy_value}, Target 89 Hit: {is_target_89_hit}")
    print(f"Calculated Intensity Profile: R={comp_load}, G={priority_level}, B={data_volume}, A={timeout_s}")

    # 2. Generate FraymusDNA Capsule (as input_data for the task)
    print("\nStep 2: Generating FraymusDNA Capsule (as task input)...")
    fraymus_gen = FraymusDNAGenerator(
        agent_state="Φ_EntangledState/ ψ(A)⊗ψ(B)",
        transcendental_frame="Ω_Hyperplane.9",
        phi_signature=PHI * 1.5 # Example variation
    )
    fraymus_capsule_json_string = fraymus_gen.encode()
    print("FraymusDNA Capsule (Input Data) generated:")
    print(fraymus_capsule_json_string)

    # 3. Define the script to be executed by the worker
    worker_script = """
import json
import os
print("W:Start")
t_inputs=task_inputs
tmi=t_inputs.get('task_meta_info')
fds=t_inputs.get('fraymus_capsule')
if tmi:
    print("W:Meta")
    print(f" T:{tmi.get('type','N/A')}")
    print(f" VI:{tmi.get('visual_inversion','N/A')}")
    p=tmi.get('intensity_profile')
    if p: 
        print(" IP:")
        for k,v in p.items(): print(f"  {k}:{v}")
    else: print(" IP:N/A")
    da=tmi.get('domino_attributes')
    if da: 
        print(" DA:")
        print(f"  S:{da.get('step','N/A')}")
        print(f"  H89:{da.get('is_target_89_hit','N/A')}")
    else: print(" DA:N/A")
    print("----")
else: print("W:NoMeta")
if fds:
    print("W:DecCap")
    try:
        fc=json.loads(fds)
        print("W:CapDet")
        for k,v in fc.items(): print(f" {k}:{v}")
        print("----")
        print("W:CapOK")
    except json.JSONDecodeError as e: print(f"W:ErrDecCap:{e}")
else: print("W:NoCap")
nds=-1;nvi=False
if tmi and tmi.get('domino_attributes'):
    cda=tmi.get('domino_attributes');cs=cda.get('step',0);wth=cda.get('is_target_89_hit',False)
    cvi=tmi.get('visual_inversion',False);nvi=not cvi
    if wth:nds=cs+5 # If target hit, jump 5 steps for a more significant change
    else:nds=cs+1
    print("---NTS---") # Shortened
    print(f"NxtP:DS={nds},VI={nvi}") # Shortened, using nds, nvi directly
    # --- Added for Phase 3: Worker writes next_task_params.json ---
    params_to_write = {"domino_step": nds, "visual_inversion": nvi} # Using nds, nvi
    params_file_path = "next_task_params.json"
    try:
        with open(params_file_path, 'w') as pf:
            json.dump(params_to_write, pf, indent=2)
        print(f"W:POK:{params_file_path}") # Shortened
    except Exception as e_write:
        print(f"W:PFAIL:{e_write}") # Shortened
    # --- End Phase 3 addition ---
    print("---------") # Shortened
else: print("W:NoNxtSugg")
print("W:End")
"""
    print("\n   Embedded worker script prepared.")

    # 4. Create the task payload for the QR code
    print("\nStep 3: Creating QR Code Task Payload...")
    task_id = str(uuid.uuid4())

    # Create a copy of task_meta_data to modify for the payload (remove non-essential keys)
    task_meta_for_payload = task_meta_data.copy()
    task_meta_for_payload.pop('version', None) # Remove 'version' if it exists, worker doesn't use it
    task_meta_for_payload.pop('source_node', None) # Remove 'source_node' if it exists, worker doesn't use it

    task_payload_dict = {
        "task_id": task_id,
        "task_meta": task_meta_for_payload, # This is the leaner version for the QR code
        "script": worker_script,
        "input_data": {
            "fraymus_capsule": fraymus_capsule_json_string,
            "task_meta_info": task_meta_for_payload.copy() # Pass the same leaner metadata to the script's direct input
        }
    }
    json_task_payload = json.dumps(task_payload_dict)
    print(f"Task payload created with task_id: {task_id}")

    # 5. Generate and display the QR code
    print("\nStep 4: Generating and Displaying QR Code...")
    # Pass the inversion flag from task_meta to the display function
    if display_qr_code(json_task_payload, "fraymus_task_meta_qr.png", inverted=task_meta_data["visual_inversion"]):
        print("\nFraymusDNA QR Task Issuer finished. Run worker and scan fraymus_task_meta_qr.png.")
    else:
        print("\nFraymusDNA QR Task Issuer finished with errors displaying QR code.")
    print(f"If the image viewer for the QR code is still open, you may need to close it manually.")

    print(f"\nFraymusDNA QR Task Issuer - SINGLE CYCLE EXECUTION FINISHED. DOMINO_STEP processed: {current_domino_step}")

if __name__ == "__main__":
    main()

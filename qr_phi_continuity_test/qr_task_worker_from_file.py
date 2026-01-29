# qr_task_worker_from_file.py
# Scans a QR code from a specified image file and executes the embedded task, looping and monitoring for file changes.

import cv2
from qreader import QReader
import json
import time
import uuid
import sys
import io
import argparse # For command-line arguments
import os # Added for file system operations
from contextlib import redirect_stdout
import subprocess # For shell script execution
import stat       # For setting file permissions
from PIL import Image
from pyzbar.pyzbar import decode
from uno_game_logic import (deal_initial_hand, ai_choose_card, 
                            draw_card_from_deck, create_deck, COLORS) # Import create_deck, remove GAME_DECK
from generate_uno_qr import generate_uno_card_qr, DEFAULT_OUTPUT_FILENAME as UNO_DISCARD_FILE
from quantum_transcendental_counter import QuantumTranscendentalCounter
import hashlib
import base64 # Added for face image decoding

# Global QReader instance
QFINDER = QReader()

# Global sets to keep track of processed task IDs and their last processing time
PROCESSED_TASK_IDS = set()
LAST_PROCESSED_TIME = {} # Stores {task_id: timestamp}

# --- Uno Game State Persistence ---
UNO_GAME_STATE_FILE = "uno_current_game_state.json"

# Global game state variables - to be populated by load_game_state()
AI_HAND = []
GAME_DECK_STATE = [] #This will hold the actual deck of cards
AI_HAND_INITIALIZED = False 
# --- End Uno Game State ---

def calculate_file_hash(file_path):
    with open(file_path, 'rb') as f:
        buf = f.read()
    return hashlib.md5(buf).hexdigest()

# --- Game State Persistence Functions ---
def load_game_state():
    global AI_HAND, GAME_DECK_STATE, AI_HAND_INITIALIZED
    try:
        with open(UNO_GAME_STATE_FILE, 'r') as f:
            state = json.load(f)
            AI_HAND = state.get('ai_hand', [])
            GAME_DECK_STATE = state.get('game_deck_state', [])
            AI_HAND_INITIALIZED = state.get('ai_hand_initialized', False)
            print(f"Loaded game state: AI Hand {len(AI_HAND)} cards, Deck {len(GAME_DECK_STATE)} cards, Initialized: {AI_HAND_INITIALIZED}")
            # If deck is empty after loading, it might mean end of game or bad state, re-initialize deck for safety for now
            if not GAME_DECK_STATE and AI_HAND_INITIALIZED: # If game was initialized but deck is empty, could be an issue
                print("Warning: Loaded empty deck for an initialized game. Consider deck reshuffle logic.")
            elif not GAME_DECK_STATE and not AI_HAND_INITIALIZED: # New game or corrupt deck state
                print("No valid deck in loaded state or new game, creating fresh deck.")
                GAME_DECK_STATE = create_deck()

    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"No valid game state file found or error loading ({e}), starting fresh.")
        AI_HAND = []
        GAME_DECK_STATE = create_deck() # Create a fresh deck
        AI_HAND_INITIALIZED = False

def save_game_state():
    global AI_HAND, GAME_DECK_STATE, AI_HAND_INITIALIZED
    state = {
        'ai_hand': AI_HAND,
        'game_deck_state': GAME_DECK_STATE,
        'ai_hand_initialized': AI_HAND_INITIALIZED
    }
    try:
        with open(UNO_GAME_STATE_FILE, 'w') as f:
            json.dump(state, f, indent=2)
        print(f"Game state saved: AI Hand {len(AI_HAND)} cards, Deck {len(GAME_DECK_STATE)} cards, Initialized: {AI_HAND_INITIALIZED}")
    except IOError as e:
        print(f"Error saving game state: {e}")

def execute_shell_script_task(task_id, shell_script_content):
    """
    Creates a temporary .sh file with the given content, makes it executable,
    and runs it.
    """
    temp_script_name = f"temp_generated_script_{task_id}.sh"
    # Using current working directory of the worker for the temp script and its execution context.
    temp_script_path = os.path.join(os.getcwd(), temp_script_name) 

    try:
        print(f"   Preparing to execute shell script for task {task_id}...")
        with open(temp_script_path, "w") as f:
            f.write(shell_script_content)
        
        # Make the script executable: owner can read/write/execute, group/other can read/execute (0o755)
        os.chmod(temp_script_path, stat.S_IRWXU | stat.S_IRGRP | stat.S_IXGRP | stat.S_IROTH | stat.S_IXOTH)
        print(f"   Created temporary shell script: {temp_script_path} (executable)")

        print(f"   Executing shell script: ./{temp_script_name}")
        result = subprocess.run(['/bin/bash', temp_script_path], capture_output=True, text=True, check=False, cwd=os.getcwd())

        print(f"--- Shell Script Output (Task {task_id}) ---")
        if result.stdout:
            print("STDOUT:")
            print(result.stdout.strip())
        if result.stderr:
            print("STDERR:")
            print(result.stderr.strip())
        print(f"Return Code: {result.returncode}")
        print(f"--- End Shell Script Output (Task {task_id}) ---")

        if result.returncode == 0:
            print(f"   Shell script for task {task_id} executed successfully.")
            return True
        else:
            print(f"   Shell script for task {task_id} finished with errors (return code: {result.returncode}).")
            return False

    except Exception as e:
        print(f"   Error during shell script execution for task {task_id}: {e}")
        return False
    finally:
        # Leaving the temporary script for inspection during debugging.
        # In production, consider adding cleanup logic here.
        pass

def execute_script_from_task(task_id, script_string, input_data, task_metadata=None):
    """Executes the Python script string extracted from the QR code task."""
    local_namespace = {
        'task_inputs': input_data,
        'task_id': task_id,
        'task_meta': task_metadata, # Pass the whole metadata dict to the script's scope
    }
    
    script_output_capture = io.StringIO()
    try:
        print(f"   Executing script for task {task_id}...")
        with redirect_stdout(script_output_capture):
            exec(script_string, {"__builtins__": __builtins__}, local_namespace)
        
        script_output = script_output_capture.getvalue()
        if script_output:
            print(f"--- Script Output (Task {task_id}) ---")
            print(script_output.strip()) # .strip() to remove trailing newlines if any
            print(f"--- End Script Output (Task {task_id}) ---")
        else:
            print(f"   Script for task {task_id} executed, no explicit print output captured.")
        print(f"   Task {task_id} executed successfully.")
        return True
    except Exception as e:
        print(f"   Error executing script for task {task_id}: {e}")
        error_output = script_output_capture.getvalue()
        if error_output:
            print(f"--- Script Output Before Error (Task {task_id}) ---")
            print(error_output.strip())
            print(f"--- End Script Output (Task {task_id}) ---")
        return False
    finally:
        script_output_capture.close()

def process_uno_turn(current_discard_card_payload):
    global AI_HAND_INITIALIZED, AI_HAND, GAME_DECK_STATE # Use GAME_DECK_STATE

    print("\n--- Processing Uno Turn ---")
    if not AI_HAND_INITIALIZED:
        print("Initializing AI hand for the first time...")
        AI_HAND = deal_initial_hand(GAME_DECK_STATE) # Pass GAME_DECK_STATE
        AI_HAND_INITIALIZED = True
        print(f"AI Initial Hand ({len(AI_HAND)} cards): {AI_HAND}")
        if not GAME_DECK_STATE: # Check if deck became empty after deal
            print("Warning: Deck is empty after initial deal!")

    print(f"Current Discard Pile Top: {current_discard_card_payload}")
    print(f"AI Current Hand ({len(AI_HAND)} cards): {AI_HAND}")
    print(f"Deck has {len(GAME_DECK_STATE)} cards remaining before AI plays.")

    # Determine chosen color if the discard is a wild card
    last_chosen_wild_color = current_discard_card_payload.get('chosen_color')
    if last_chosen_wild_color:
        print(f"Previous player chose color: {last_chosen_wild_color} for a wild card.")

    # AI attempts to play a card
    card_played, wild_color_choice = ai_choose_card(AI_HAND, current_discard_card_payload, last_chosen_wild_color)

    if card_played:
        # If AI played a wild, it needs to choose a color
        if wild_color_choice:
            print(f"AI chose color '{wild_color_choice}' for its wild card.")
            # Update card_played payload to include the chosen_color for the QR code
            # Make a copy to avoid modifying the card in AI_HAND if it's a reference (though pop removes it)
            card_for_qr = card_played.copy()
            card_for_qr['chosen_color'] = wild_color_choice
        else:
            card_for_qr = card_played

        generate_uno_card_qr(card_for_qr, output_filename=UNO_DISCARD_FILE)
        print(f"AI played card. New discard QR generated: {UNO_DISCARD_FILE}")
        
        # Check for "Uno!" or Win condition
        if len(AI_HAND) == 1:
            print("\n*********************************")
            print("***     AI says: UNO!     ***")
            print("*********************************\n")
        elif not AI_HAND: # This means AI played its last card
            print("\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            print("!!! AI HAS PLAYED ITS LAST CARD - WINNER! !!!")
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n")
            # Potentially add logic here to stop the game or declare AI winner
    else:
        print("AI has no playable card. Attempting to draw...")
        if GAME_DECK_STATE: # Check if deck is not empty
            drawn_card = draw_card_from_deck(AI_HAND, GAME_DECK_STATE) # Pass GAME_DECK_STATE
            if drawn_card:
                print(f"AI drew: {drawn_card}")
            else: # Should not happen if GAME_DECK_STATE check was positive, but defensive
                print("AI tried to draw, but deck was unexpectedly empty after check.")
        else:
            print("AI cannot draw, deck is empty!")
    
    print(f"AI Hand After Turn ({len(AI_HAND)} cards): {AI_HAND}")
    print(f"Deck has {len(GAME_DECK_STATE)} cards remaining after AI's turn.")
    save_game_state() # Save state after every turn
    print("--- End Uno Turn Processing ---")

def process_qr_image_file(image_path):
    """Loads an image, decodes QR codes, and processes tasks."""
    try:
        cv_image = cv2.imread(image_path) # Renamed to cv_image to avoid conflict with PIL.Image
        if cv_image is None:
            print(f"Error: Could not read image from path: {image_path}")
            return
    except Exception as e:
        print(f"Error loading image {image_path}: {e}")
        return

    print(f"Attempting to decode QR codes from image: {image_path}")
    decoded_qrs = QFINDER.detect_and_decode(image=cv_image)

    if not decoded_qrs or (isinstance(decoded_qrs, list) and not decoded_qrs[0]):
        print("No QR codes found or decoded in the image.")
        return

    if not isinstance(decoded_qrs, list):
        decoded_qrs = [decoded_qrs]

    for qr_item in decoded_qrs:
        if qr_item is None:
            continue
        
        qr_content_str = qr_item
        if isinstance(qr_item, tuple):
            qr_content_str = qr_item[0]

        if not qr_content_str:
            print("Extracted empty QR content. Skipping.")
            continue
            
        try:
            decoded_data = json.loads(qr_content_str)
            
            if "task_data" in decoded_data and isinstance(decoded_data["task_data"], dict):
                print("Detected 'task_data' nesting, using inner payload for task details.")
                actual_task_payload = decoded_data["task_data"]
            else:
                actual_task_payload = decoded_data

            # --- Handle Uno game specific payload structure FIRST ---
            if actual_task_payload.get("game") == "uno":
                print(f"[+] Uno game QR detected: Card Instance ID {actual_task_payload.get('card_instance_id', 'N/A')}, Value: {actual_task_payload.get('value')}, Color: {actual_task_payload.get('color')}")
                process_uno_turn(actual_task_payload) 
                continue # Processed Uno turn, move to next QR in image

            # --- For other tasks, get common fields and check if already processed ---
            task_type = actual_task_payload.get("task_type")
            task_id = actual_task_payload.get("task_id", "N/A")
            timestamp = actual_task_payload.get("timestamp", "N/A")

            print(f"Processing Task ID: {task_id}, Type: {task_type}, Timestamp: {timestamp}")

            if task_id and task_id != "N/A" and task_id in PROCESSED_TASK_IDS:
                print(f"Task {task_id} was already processed. Skipping.")
                continue
            
            # --- Main task routing ---
            # Note: The 'set_uno_card' task_type elif block that was here previously is removed,
            # as Uno card setting is handled by the `actual_task_payload.get("game") == "uno"` block above.

            if task_type == "execute_sh":
                script_content = actual_task_payload.get("script_content")
                if script_content:
                    print(f"Task Type: Execute Shell Script (ID: {task_id})")
                    safe_task_id = "".join(c if c.isalnum() else '_' for c in str(task_id))
                    script_filename = f"temp_script_{safe_task_id}.sh"
                    try:
                        with open(script_filename, "w") as f:
                            f.write(script_content)
                        os.chmod(script_filename, 0o755)
                        print(f"Executing shell script: ./{script_filename}")
                        result = subprocess.run([f"./{script_filename}"], capture_output=True, text=True, check=False, shell=True)
                        print(f"Script STDOUT:\n{result.stdout}")
                        if result.stderr:
                            print(f"Script STDERR:\n{result.stderr}")
                        print(f"Shell script execution finished for task {task_id}.")
                    except Exception as e:
                        print(f"Error executing shell script for task {task_id}: {e}")
                    finally:
                        if os.path.exists(script_filename):
                            os.remove(script_filename)
                    if task_id and task_id != "N/A": PROCESSED_TASK_IDS.add(task_id); LAST_PROCESSED_TIME[task_id] = time.time()
                else:
                    print(f"Error: 'script_content' not found in payload for task {task_id}.")
            
            elif task_type == "run_transcendental_counter":
                print(f"Task Type: Run Transcendental Counter (ID: {task_id})")
                duration = actual_task_payload.get("duration", 10) 
                if not isinstance(duration, (int, float)) or duration <= 0:
                    print(f"Warning: Invalid duration '{duration}'. Using default 10 seconds.")
                    duration = 10
                print(f"Initiating transcendental counter for {duration} seconds.")
                try:
                    counter = QuantumTranscendentalCounter()
                    counter.count_transcendental(duration=int(duration))
                    print(f"Transcendental counter finished for task {task_id}.")
                except Exception as e:
                    print(f"Error running transcendental counter for task {task_id}: {e}")
                if task_id and task_id != "N/A": PROCESSED_TASK_IDS.add(task_id); LAST_PROCESSED_TIME[task_id] = time.time()

            elif task_type == "phi_harmonic_spoof_check":
                print(f"Task Type: Phi-Harmonic Spoof Check (ID: {task_id})")
                target_data = actual_task_payload.get("target_data")
                if target_data:
                    print(f"  Target data for spoof check: {target_data}")
                    is_authentic = (sum(ord(c) for c in target_data) % 2 == 0)
                    print(f"  Spoof Check Result for {task_id}: {'Authentic' if is_authentic else 'Potential Spoof'}")
                else:
                    print(f"Error: 'target_data' not found for spoof check task {task_id}.")
                if task_id and task_id != "N/A": PROCESSED_TASK_IDS.add(task_id); LAST_PROCESSED_TIME[task_id] = time.time()

            elif task_type == "display_face_image":
                print(f"Task Type: Display Face Image (ID: {task_id})")
                image_data_base64 = actual_task_payload.get("image_data_base64")
                original_filename = actual_task_payload.get("original_filename", "unknown_face")
                if image_data_base64:
                    try:
                        img_bytes = base64.b64decode(image_data_base64)
                        img_buffer = io.BytesIO(img_bytes)
                        reconstructed_image = Image.open(img_buffer) # Uses PIL.Image
                        safe_original_filename = "".join(c if c.isalnum() else '_' for c in os.path.splitext(original_filename)[0])
                        output_filename = f"decoded_face_{safe_original_filename}_{str(time.time()).replace('.', '_')}.png"
                        output_path = os.path.join(os.getcwd(), output_filename)
                        reconstructed_image.save(output_path)
                        print(f"Reconstructed face image saved to: {output_path}")
                    except Exception as e:
                        print(f"Error decoding/saving face image for task {task_id}: {e}")
                else:
                    print(f"Error: 'image_data_base64' not found in payload for task {task_id}.")
                if task_id and task_id != "N/A": PROCESSED_TASK_IDS.add(task_id); LAST_PROCESSED_TIME[task_id] = time.time()
            
            # --- Restore Fraymus Python Script Task Logic ---
            elif "script" in actual_task_payload: 
                script_to_run = actual_task_payload.get("script")
                input_params = actual_task_payload.get("input_data", {})
                meta_params = decoded_data.get("task_meta", actual_task_payload.get("task_meta", {}))

                if not task_id or task_id == "N/A":
                    print("Decoded Python script task, but missing valid 'task_id'. Skipping.")
                    continue

                print(f"[+] New Python task found from file: {task_id}")
                print(f"--- Task Metadata (Worker Log for Python Script) ---")
                print(f"  Task ID: {task_id}")
                print(f"  Type: {meta_params.get('type', 'Python Script')}") 
                print(f"  Visual Inversion: {meta_params.get('visual_inversion', 'N/A')}")
                if 'intensity_profile' in meta_params and isinstance(meta_params['intensity_profile'], dict):
                    profile = meta_params['intensity_profile']
                    print("  Intensity Profile:")
                    for key, value in profile.items():
                         print(f"    {key}: {value}")
                print(f"----------------------------------")
                execute_script_from_task(task_id, script_to_run, input_params, meta_params)
                PROCESSED_TASK_IDS.add(task_id)
                LAST_PROCESSED_TIME[task_id] = time.time()

            else: # Unknown task type
                print(f"Unknown task type: '{task_type}' for task ID: '{task_id}'. Skipping.")
                if task_id and task_id != "N/A": 
                    PROCESSED_TASK_IDS.add(task_id)
                    LAST_PROCESSED_TIME[task_id] = time.time()
        
        except json.JSONDecodeError:
            print(f"Decoded QR content, but it's not valid JSON: '{qr_content_str[:100]}...' Skipping.")
        except Exception as e:
            print(f"Error processing decoded QR content: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Scan a QR code from an image file and execute the task, looping and monitoring for file changes.")
    parser.add_argument("-f", "--file", required=True, help="Path to the QR code image file to monitor.")
    parser.add_argument("--poll_interval", type=int, default=3, help="Seconds to wait between checking for file updates.")
    args = parser.parse_args()

    qr_image_path = args.file
    poll_interval = args.poll_interval
    last_mod_time = 0.0  # Initialize to a value that will trigger first read if file exists

    print(f"QR Task Worker (Looping File Monitor) started.")
    
    # Load initial game state when worker starts
    load_game_state()

    print(f"Monitoring QR image file: {qr_image_path}")
    print(f"Polling interval: {poll_interval} seconds. Press Ctrl+C to stop.")

    loop_count = 0
    try:
        while True:
            loop_count += 1
            # print(f"\n--- Worker Loop Cycle {loop_count} ---") # Uncomment for verbose cycle logging

            if not os.path.exists(qr_image_path):
                # Optional: print a message if file not found, can be noisy
                # print(f"File not found: {qr_image_path}. Waiting...")
                time.sleep(poll_interval)
                continue

            try:
                current_mod_time = os.path.getmtime(qr_image_path)
            except OSError as e:
                # Optional: print an error if mod time can't be read
                # print(f"Error getting modification time for {qr_image_path}: {e}. Retrying...")
                time.sleep(poll_interval)
                continue
            
            if current_mod_time != last_mod_time:
                print(f"\nChange detected in {qr_image_path} (Mod time: {current_mod_time}). Processing...")
                process_qr_image_file(qr_image_path) # This function contains its own print statements
                last_mod_time = current_mod_time
                print(f"Finished processing. Waiting for next change or poll interval ({poll_interval}s)...")
            # else:
                # Optional: print message if no change, can be noisy
                # print(f"No change detected in {qr_image_path}. Last mod time: {last_mod_time}")

            time.sleep(poll_interval)

    except KeyboardInterrupt:
        print("\nLooping QR Task Worker stopped by user.")
    except Exception as e:
        print(f"\nAn unexpected error occurred in the worker loop: {e}")
    finally:
        print("QR Task Worker (Looping File Monitor) exiting.")

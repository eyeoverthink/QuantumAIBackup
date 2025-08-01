#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
QR Single Run Worker

Modified version of qr_task_worker_from_file.py that processes a QR code once and exits.
This is designed for use with the Quantum Phi-Harmonic Continuity Test.
"""

import cv2
from qreader import QReader
import json
import time
import uuid
import sys
import io
import argparse
import os
from contextlib import redirect_stdout
import subprocess
import stat
from PIL import Image
from pyzbar.pyzbar import decode
import hashlib
import base64
import traceback

# Import from uno_game_logic stub
try:
    print("[DEBUG] Importing from uno_game_logic...")
    from uno_game_logic import (deal_initial_hand, ai_choose_card, 
                            draw_card_from_deck, create_deck, COLORS)
    print("[DEBUG] Successfully imported from uno_game_logic")
except ImportError as e:
    print(f"[ERROR] Failed to import from uno_game_logic: {str(e)}")
    sys.exit(1)

# Try importing other dependencies
try:
    print("[DEBUG] Importing generate_uno_qr...")
    from generate_uno_qr import generate_uno_card_qr, DEFAULT_OUTPUT_FILENAME as UNO_DISCARD_FILE
    print("[DEBUG] Successfully imported generate_uno_qr")
except ImportError as e:
    print(f"[WARNING] Failed to import generate_uno_qr: {str(e)}")
    print("[DEBUG] This is not critical, continuing...")
    UNO_DISCARD_FILE = "uno_discard.png"
    
    # Create a stub function
    def generate_uno_card_qr(card_data, output_filename=UNO_DISCARD_FILE):
        print(f"[STUB] Would generate QR for card: {card_data}")
        with open(output_filename, 'w') as f:
            f.write(json.dumps(card_data))

try:
    print("[DEBUG] Importing quantum_transcendental_counter...")
    from quantum_transcendental_counter import QuantumTranscendentalCounter
    print("[DEBUG] Successfully imported quantum_transcendental_counter")
except ImportError as e:
    print(f"[WARNING] Failed to import quantum_transcendental_counter: {str(e)}")
    print("[DEBUG] Creating stub class...")
    
    # Create a stub class
    class QuantumTranscendentalCounter:
        def __init__(self):
            print("[STUB] QuantumTranscendentalCounter initialized")
            
        def count_transcendental(self, duration=10):
            print(f"[STUB] Would count transcendental for {duration} seconds")
            return duration

# Global QReader instance
print("Initializing QReader...")
QFINDER = QReader()
print("QReader initialized")

# Global sets to keep track of processed task IDs
PROCESSED_TASK_IDS = set()
LAST_PROCESSED_TIME = {}

# --- Uno Game State Persistence ---
UNO_GAME_STATE_FILE = "uno_current_game_state.json"

# Global game state variables
AI_HAND = []
GAME_DECK_STATE = []
AI_HAND_INITIALIZED = False

def calculate_file_hash(file_path):
    """Calculate MD5 hash of a file"""
    try:
        with open(file_path, 'rb') as f:
            buf = f.read()
        return hashlib.md5(buf).hexdigest()
    except Exception as e:
        print(f"Error calculating file hash: {str(e)}")
        return None

def load_game_state():
    """Load game state from file"""
    global AI_HAND, GAME_DECK_STATE, AI_HAND_INITIALIZED
    print("Loading game state...")
    try:
        with open(UNO_GAME_STATE_FILE, 'r') as f:
            state = json.load(f)
            
        # Load AI hand
        AI_HAND = []
        for card_data in state.get('ai_hand', []):
            card = type('obj', (object,), {'color': card_data.get('color'), 'value': card_data.get('value')})
            AI_HAND.append(card)
            
        # Load deck state
        GAME_DECK_STATE = []
        for card_data in state.get('deck', []):
            card = type('obj', (object,), {'color': card_data.get('color'), 'value': card_data.get('value')})
            GAME_DECK_STATE.append(card)
            
        AI_HAND_INITIALIZED = True
        print(f"Game state loaded: AI has {len(AI_HAND)} cards, deck has {len(GAME_DECK_STATE)} cards")
        return True
    except FileNotFoundError:
        print("No game state file found, will initialize new game")
        return False
    except Exception as e:
        print(f"Error loading game state: {str(e)}")
        return False

def save_game_state():
    """Save game state to file"""
    print("Saving game state...")
    try:
        state = {
            'ai_hand': [{'color': card.color, 'value': card.value} for card in AI_HAND],
            'deck': [{'color': card.color, 'value': card.value} for card in GAME_DECK_STATE]
        }
        
        with open(UNO_GAME_STATE_FILE, 'w') as f:
            json.dump(state, f, indent=2)
        print("Game state saved successfully")
    except Exception as e:
        print(f"Error saving game state: {str(e)}")

def execute_shell_script_task(task_id, shell_script_content):
    """Execute a shell script task"""
    print(f"Executing shell script task: {task_id}")
    try:
        # Create a temporary file with a unique name
        script_filename = f"qr_task_{task_id}.sh"
        
        with open(script_filename, 'w') as f:
            f.write(shell_script_content)
        
        # Make the script executable
        os.chmod(script_filename, os.stat(script_filename).st_mode | stat.S_IEXEC)
        
        # Execute the script
        print(f"Running shell script: {script_filename}")
        result = subprocess.run(
            ['/bin/bash', script_filename],
            capture_output=True,
            text=True
        )
        
        # Output the results
        print(f"Shell script stdout: {result.stdout}")
        if result.stderr:
            print(f"Shell script stderr: {result.stderr}")
        
        # Clean up
        os.remove(script_filename)
        print("Shell script execution completed")
        
        return result.stdout
    except Exception as e:
        print(f"Error executing shell script: {str(e)}")
        traceback.print_exc()
        return f"Error: {str(e)}"

def execute_script_from_task(task_id, script_string, input_data, task_metadata=None):
    """Execute a Python script from task"""
    print(f"Executing Python script from task: {task_id}")
    try:
        # Prepare a clean namespace
        namespace = {
            'input_data': input_data,
            'task_metadata': task_metadata or {},
            'task_id': task_id
        }
        
        # Capture stdout
        output_buffer = io.StringIO()
        
        with redirect_stdout(output_buffer):
            # Execute the script in the namespace
            exec(script_string, namespace)
        
        # Get the output
        output = output_buffer.getvalue()
        print(f"Script execution output: {output[:100]}..." if len(output) > 100 else f"Script execution output: {output}")
        
        return output
    except Exception as e:
        print(f"Error executing script: {str(e)}")
        traceback.print_exc()
        return f"Error: {str(e)}"

def process_uno_turn(current_discard_card_payload):
    """Process an UNO turn"""
    global AI_HAND, GAME_DECK_STATE, AI_HAND_INITIALIZED
    
    print("Processing UNO turn...")
    
    # Initialize game if not already done
    if not AI_HAND_INITIALIZED:
        print("Initializing UNO game...")
        # Create a new deck
        deck = create_deck()
        GAME_DECK_STATE = deck.cards
        print(f"Created new deck with {len(GAME_DECK_STATE)} cards")
        
        # Initialize AI hand
        AI_HAND = []
        player = type('obj', (object,), {'hand': [], 'add_card': lambda card: AI_HAND.append(card)})
        deal_initial_hand(player, deck)
        AI_HAND = player.hand
        print(f"Dealt initial hand to AI: {len(AI_HAND)} cards")
        
        AI_HAND_INITIALIZED = True
        save_game_state()
    
    # Extract the current discard card from the payload
    try:
        current_discard = type('obj', (object,), {
            'color': current_discard_card_payload.get('color'),
            'value': current_discard_card_payload.get('value')
        })
        print(f"Current discard card: {current_discard.color} {current_discard.value}")
        
        # AI chooses a card to play
        chosen_card = ai_choose_card(AI_HAND, current_discard)
        
        if chosen_card:
            print(f"AI chose to play: {chosen_card.color} {chosen_card.value}")
            # Remove the card from AI's hand
            AI_HAND.remove(chosen_card)
            
            # Generate QR code for the played card
            card_payload = {
                'color': chosen_card.color,
                'value': chosen_card.value
            }
            
            try:
                generate_uno_card_qr(card_payload)
                print(f"Generated QR code for played card: {UNO_DISCARD_FILE}")
            except Exception as e:
                print(f"Error generating QR code: {str(e)}")
                # Fallback: create a simple text file with the card info
                with open("ai_played_card.txt", 'w') as f:
                    f.write(f"AI played: {chosen_card.color} {chosen_card.value}")
                print("Created text file with played card info")
        else:
            print("AI has no playable cards, drawing from deck")
            # Draw a card
            drawn_card = draw_card_from_deck(GAME_DECK_STATE)
            if drawn_card:
                print(f"AI drew: {drawn_card.color} {drawn_card.value}")
                AI_HAND.append(drawn_card)
            else:
                print("Deck is empty!")
        
        # Save the updated game state
        save_game_state()
        
        return True
    except Exception as e:
        print(f"Error processing UNO turn: {str(e)}")
        traceback.print_exc()
        return False

def process_qr_image_file(image_path):
    """Process a QR code image file"""
    print(f"Processing QR image file: {image_path}")
    try:
        # Check if file exists
        if not os.path.exists(image_path):
            print(f"Error: Image file not found: {image_path}")
            return False
        
        # Load the image
        print("Loading image...")
        image = cv2.imread(image_path)
        if image is None:
            print("Error: Could not load image")
            return False
        
        print("Image loaded successfully")
        
        # Try pyzbar first
        print("Attempting to decode with pyzbar...")
        try:
            pil_image = Image.open(image_path)
            qr_codes = decode(pil_image)
            
            if qr_codes:
                print(f"pyzbar found {len(qr_codes)} QR codes")
                qr_data = qr_codes[0].data.decode('utf-8')
                print(f"QR data length: {len(qr_data)} characters")
            else:
                print("pyzbar found no QR codes, trying QReader...")
                # Try QReader as fallback
                qr_data = QFINDER.detect_and_decode(image=image)[0]
                if qr_data:
                    print(f"QReader found QR code, data length: {len(qr_data)} characters")
                else:
                    print("QReader found no QR codes")
                    return False
        except Exception as e:
            print(f"Error with pyzbar: {str(e)}, trying QReader...")
            # Try QReader as fallback
            qr_data = QFINDER.detect_and_decode(image=image)[0]
            if qr_data:
                print(f"QReader found QR code, data length: {len(qr_data)} characters")
            else:
                print("QReader found no QR codes")
                return False
        
        # Parse the QR data as JSON
        print("Parsing QR data as JSON...")
        try:
            task_data = json.loads(qr_data)
            print("Successfully parsed QR data as JSON")
        except json.JSONDecodeError:
            print("QR data is not valid JSON, treating as raw text")
            task_data = {"type": "text", "content": qr_data}
        
        # Extract task ID
        task_id = task_data.get('id', str(uuid.uuid4()))
        print(f"Task ID: {task_id}")
        
        # Process based on task type
        task_type = task_data.get('type', 'unknown')
        print(f"Task type: {task_type}")
        
        if task_type == 'python_script':
            script_content = task_data.get('script', '')
            input_data = task_data.get('input', {})
            metadata = task_data.get('metadata', {})
            
            print(f"Executing Python script task, script length: {len(script_content)} characters")
            result = execute_script_from_task(task_id, script_content, input_data, metadata)
            print("Python script execution completed")
            
        elif task_type == 'shell_script':
            script_content = task_data.get('script', '')
            
            print(f"Executing shell script task, script length: {len(script_content)} characters")
            result = execute_shell_script_task(task_id, script_content)
            print("Shell script execution completed")
            
        elif task_type == 'uno_card':
            card_data = task_data.get('card', {})
            
            print("Processing UNO card task")
            result = process_uno_turn(card_data)
            print("UNO turn processing completed")
            
        elif task_type == 'text':
            content = task_data.get('content', '')
            print(f"Text content: {content[:100]}..." if len(content) > 100 else f"Text content: {content}")
            result = f"Received text: {content}"
            
        else:
            print(f"Unknown task type: {task_type}")
            result = f"Unknown task type: {task_type}"
        
        # Mark this task as processed
        PROCESSED_TASK_IDS.add(task_id)
        LAST_PROCESSED_TIME[task_id] = time.time()
        
        print(f"Task {task_id} processed successfully")
        return True
        
    except Exception as e:
        print(f"Error processing QR image: {str(e)}")
        traceback.print_exc()
        return False

# Main execution
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process a QR code image once and exit.")
    parser.add_argument("-f", "--file", required=True, help="Path to the QR code image file to process.")
    
    args = parser.parse_args()
    image_path = args.file
    
    print(f"QR Single Run Worker")
    print(f"====================")
    print(f"Processing QR code image: {image_path}")
    
    # Load game state if it exists
    load_game_state()
    
    # Process the QR code once
    success = process_qr_image_file(image_path)
    
    if success:
        print("\n✅ QR code processed successfully")
        sys.exit(0)
    else:
        print("\n❌ Failed to process QR code")
        sys.exit(1)

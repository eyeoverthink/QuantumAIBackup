# generate_uno_qr.py

"""
Generates a QR code representing an Uno card.
Each QR code will contain a JSON payload describing the card.
This will typically be used to represent the current top of the discard pile.
"""

import qrcode
import json
import uuid
import os
import argparse

DEFAULT_OUTPUT_FILENAME = "current_uno_discard.png"

def generate_uno_card_qr(card_data, output_filename=DEFAULT_OUTPUT_FILENAME, output_dir=".", show_image=False):
    """
    Generates a QR code for a given Uno card and saves it as an image file.

    Args:
        card_data (dict): A dictionary describing the Uno card.
                          Expected keys depend on card type, e.g., 
                          {"type": "number", "color": "red", "value": "5"}
                          {"type": "action", "action_name": "skip", "color": "blue"}
                          {"type": "wild", "action_name": "wild_standard", "chosen_color": "green"} (if color chosen)
        output_filename (str): The name of the output QR code image file.
        output_dir (str): The directory to save the QR code image file.
        show_image (bool): Whether to display the generated QR image.

    Returns:
        str: The full path to the saved QR code image if successful, None otherwise.
    """
    if not isinstance(card_data, dict):
        print("Error: card_data must be a dictionary.")
        return None

    # Ensure base fields are present and add game identifier and instance ID
    qr_payload = {
        "game": "uno",
        "card_instance_id": str(uuid.uuid4()),
        **card_data # Merge the provided card_data
    }

    # Validate essential keys based on card type (basic validation)
    card_type = qr_payload.get("type")
    if not card_type or card_type not in ["number", "action", "wild"]:
        print(f"Error: Invalid or missing 'type' in card_data: {card_type}")
        return None
    if card_type != "wild" and not qr_payload.get("color"):
         print(f"Error: Missing 'color' for non-wild card: {qr_payload}")
         return None

    try:
        # Serialize the payload to JSON
        json_payload = json.dumps(qr_payload, indent=2)

        # Create QR code
        qr = qrcode.QRCode(
            version=1, # Keep it simple for card data
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(json_payload)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")

        # Ensure output directory exists
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        
        full_output_path = os.path.join(output_dir, output_filename)
        img.save(full_output_path)

        print(f"Uno card QR code saved to: {full_output_path}")
        print("QR Data Payload:")
        print(json_payload)
        if show_image:
            img.show()
        return full_output_path

    except Exception as e:
        print(f"Error generating Uno card QR code: {e}")
        return None

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generate a QR code for an Uno card.')
    parser.add_argument('--type', type=str, help='Card type (number, action, wild)')
    parser.add_argument('--color', type=str, help='Card color (Red, Yellow, Green, Blue)')
    parser.add_argument('--value', type=str, help='Card value (0-9 for number, or action name like skip, reverse, draw_two, wild_standard, wild_draw_four)')
    parser.add_argument('--action_name', type=str, help='Specific action name if type is action or wild (e.g., skip, wild_standard)')
    parser.add_argument('--chosen_color', type=str, help='Chosen color if the card is a wild card that has been played (Red, Yellow, Green, Blue)')
    parser.add_argument('--output', type=str, default=DEFAULT_OUTPUT_FILENAME, help=f'Output filename for the QR code. Default: {DEFAULT_OUTPUT_FILENAME}')
    parser.add_argument('--show', action='store_true', help='Display the generated QR image.')

    args = parser.parse_args()

    # Check if specific card generation arguments are provided
    if args.type and (args.color or args.type == 'wild') and (args.value or args.action_name):
        print("--- Generating Specific Uno Card QR Code (CLI Request) ---")
        cli_card_data = {"game": "uno"}
        cli_card_data["type"] = args.type
        if args.color: cli_card_data["color"] = args.color
        
        if args.type == 'number' and args.value:
            cli_card_data["value"] = args.value
        elif args.type == 'action' and args.action_name:
            cli_card_data["action_name"] = args.action_name
        elif args.type == 'wild' and args.action_name:
            cli_card_data["action_name"] = args.action_name
        else:
            # Fallback for value if action_name not provided for action/wild, or value for number
            if args.value:
                if args.type == 'action' or args.type == 'wild': 
                    cli_card_data["action_name"] = args.value
                else: # number type assumed already
                    cli_card_data["value"] = args.value
            else:
                print("Error: Insufficient arguments for card type. Need value or action_name.")
                exit(1)

        if args.chosen_color: cli_card_data["chosen_color"] = args.chosen_color
        
        generate_uno_card_qr(cli_card_data, output_filename=args.output, show_image=args.show)
        print(f"Uno card QR code based on CLI args saved to: {args.output}")
        print("QR Data Payload:")
        print(json.dumps(cli_card_data, indent=2))
    else:
        # --- Create Some Example Uno Card QR Codes (if no specific CLI request) ---
        print("--- Generating Example Uno Card QR Code ---")

        # Example 1: A Red 7
        example_card_1 = {
            "game": "uno",
            "type": "number",
            "color": "Red",
            "value": "7"
        }
        generate_uno_card_qr(example_card_1, output_filename="uno_red_7.png", show_image=False)
        print("Uno card QR code saved to: ./uno_red_7.png")
        print("QR Data Payload:")
        print(json.dumps(example_card_1, indent=2))
        print("-----")

        # Example 2: A Blue Skip
        example_card_2 = {
            "game": "uno",
            "type": "action",
            "action_name": "skip",
            "color": "Blue"
        }
        generate_uno_card_qr(example_card_2, output_filename="uno_blue_skip.png", show_image=False)
        print("Uno card QR code saved to: ./uno_blue_skip.png")
        print("QR Data Payload:")
        print(json.dumps(example_card_2, indent=2))
        print("-----")

        # Example 3: A Wild card that has been played and color Green chosen
        example_card_3 = {
            "game": "uno",
            "type": "wild",
            "action_name": "wild_standard",
            "chosen_color": "Green" # Note: 'color' is None for a wild card in hand
        }
        generate_uno_card_qr(example_card_3, output_filename="uno_wild_chosen_green.png", show_image=False)
        print("Uno card QR code saved to: ./uno_wild_chosen_green.png")
        print("QR Data Payload:")
        print(json.dumps(example_card_3, indent=2))
        print("-----")

        # Example 4: A Wild Draw Four that has been played and color Yellow chosen
        example_card_4 = {
            "game": "uno",
            "type": "wild",
            "action_name": "wild_draw_four",
            "chosen_color": "Yellow"
        }
        generate_uno_card_qr(example_card_4, output_filename="uno_wild_draw_four_yellow.png", show_image=False)
        print("Uno card QR code saved to: ./uno_wild_draw_four_yellow.png")
        print("QR Data Payload:")
        print(json.dumps(example_card_4, indent=2))
        print("-----")
        
        # Example 5: Default card for current_uno_discard.png (Yellow 3)
        initial_discard_card = {
            "game": "uno",
            "type": "number",
            "color": "Yellow",
            "value": "3"
        }
        generate_uno_card_qr(initial_discard_card, output_filename=DEFAULT_OUTPUT_FILENAME)
        print(f"Default discard QR for {DEFAULT_OUTPUT_FILENAME}:")
        print(json.dumps(initial_discard_card, indent=2))
        print("--- Finished Examples ---")

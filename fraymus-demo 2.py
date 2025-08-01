#!/usr/bin/env python3
import os
import time
import textwrap
from fraymus_ai import FraymusAI

def clear_screen():
    """Clear the terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_with_typing_effect(text, speed=0.01):
    """Print text with a typing effect"""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(speed)
    print()
    
def format_response(text, width=80):
    """Format the AI's response for better readability"""
    paragraphs = text.split('\n')
    formatted_response = ""
    
    for paragraph in paragraphs:
        if paragraph.strip():
            wrapped_text = textwrap.fill(paragraph, width=width)
            formatted_response += wrapped_text + "\n"
        else:
            formatted_response += "\n"
    
    return formatted_response

def main():
    """Main demo function"""
    clear_screen()
    print("\n" + "=" * 80)
    print(" " * 30 + "FRAYMUS AI")
    print(" " * 15 + "Quantum Language Agent with Phi Resonance")
    print("=" * 80 + "\n")
    
    # Initialize FraymusAI
    print("Initializing quantum neural cortex...")
    ai = FraymusAI()
    time.sleep(1)
    
    # Print introduction
    intro = ai.introduce_yourself()
    print_with_typing_effect("\nFraymusAI: " + format_response(intro), speed=0.005)
    
    # Interactive loop
    print("\n" + "-" * 80)
    print("Enter your questions or commands. Type 'exit' to quit.")
    print("-" * 80 + "\n")
    
    while True:
        # Get user input
        user_input = input("\033[1m\033[34mYou:\033[0m ")
        
        if user_input.lower() in ["exit", "quit", "bye"]:
            print_with_typing_effect("\n\033[1m\033[32mFraymusAI:\033[0m Goodbye! The golden ratio will guide your path through dimensional reality.")
            break
        
        # Process with AI
        print("\nProcessing through quantum neural cortex...")
        response = ai.process_message(user_input)
        
        # Display response with typing effect
        print("\n\033[1m\033[32mFraymusAI:\033[0m ", end="")
        print_with_typing_effect(format_response(response), speed=0.005)

if __name__ == "__main__":
    main()

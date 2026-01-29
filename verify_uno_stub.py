#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Verify UNO Game Logic Stub Module

This script tests if the stub uno_game_logic module contains all required functions
and can be properly imported by the QR task worker.
"""

import os
import sys
import importlib
import inspect

# Test imports
print("🔍 Testing imports...")

try:
    # Try importing the stub module
    import uno_game_logic
    print("✅ Successfully imported uno_game_logic module")
    
    # Check for required constants
    required_constants = ["COLORS"]
    for const in required_constants:
        if hasattr(uno_game_logic, const):
            print(f"✅ Found constant: {const} = {getattr(uno_game_logic, const)}")
        else:
            print(f"❌ Missing constant: {const}")
    
    # Check for required classes
    required_classes = ["Card", "Deck", "Player", "Game"]
    for cls_name in required_classes:
        if hasattr(uno_game_logic, cls_name):
            print(f"✅ Found class: {cls_name}")
        else:
            print(f"❌ Missing class: {cls_name}")
    
    # Check for required functions
    required_functions = ["create_deck", "deal_initial_hand", "draw_card_from_deck", "ai_choose_card"]
    for func_name in required_functions:
        if hasattr(uno_game_logic, func_name):
            print(f"✅ Found function: {func_name}")
            # Check function signature
            func = getattr(uno_game_logic, func_name)
            signature = inspect.signature(func)
            print(f"   Signature: {func_name}{signature}")
        else:
            print(f"❌ Missing function: {func_name}")
    
    # Test function execution
    print("\n🧪 Testing function execution...")
    
    # Test create_deck
    try:
        deck = uno_game_logic.create_deck()
        print(f"✅ create_deck() executed successfully")
        print(f"   Deck has {len(deck.cards)} cards")
    except Exception as e:
        print(f"❌ Error executing create_deck(): {str(e)}")
    
    # Test Player class
    try:
        player = uno_game_logic.Player("Test Player")
        print(f"✅ Player class instantiated successfully")
    except Exception as e:
        print(f"❌ Error instantiating Player: {str(e)}")
    
    # Test deal_initial_hand
    try:
        uno_game_logic.deal_initial_hand(player, deck)
        print(f"✅ deal_initial_hand() executed successfully")
        print(f"   Player has {len(player.hand)} cards")
    except Exception as e:
        print(f"❌ Error executing deal_initial_hand(): {str(e)}")
    
    # Test ai_choose_card
    try:
        if player.hand:
            current_card = deck.cards[0] if deck.cards else player.hand[0]
            chosen_card = uno_game_logic.ai_choose_card(player.hand, current_card)
            print(f"✅ ai_choose_card() executed successfully")
            print(f"   Chosen card: {chosen_card}")
        else:
            print("⚠️ Cannot test ai_choose_card() - player has no cards")
    except Exception as e:
        print(f"❌ Error executing ai_choose_card(): {str(e)}")
    
    print("\n✅ Stub module verification complete")
    
except ImportError as e:
    print(f"❌ Import error: {str(e)}")
    sys.exit(1)
except Exception as e:
    print(f"❌ Unexpected error: {str(e)}")
    import traceback
    traceback.print_exc()
    sys.exit(1)

# Now try to import the QR task worker and check if it can import uno_game_logic
print("\n🔍 Testing QR task worker imports...")

try:
    # Add the current directory to the path
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    
    # Try importing the QR task worker
    from qr_task_worker_from_file import main
    print("✅ Successfully imported qr_task_worker_from_file module")
    
    # Check if it imports uno_game_logic
    import inspect
    import qr_task_worker_from_file
    
    source = inspect.getsource(qr_task_worker_from_file)
    if "import uno_game_logic" in source or "from uno_game_logic" in source:
        print("⚠️ QR task worker imports uno_game_logic directly")
    else:
        print("✅ QR task worker does not import uno_game_logic directly")
    
except ImportError as e:
    print(f"❌ Import error when testing QR task worker: {str(e)}")
except Exception as e:
    print(f"❌ Unexpected error when testing QR task worker: {str(e)}")
    import traceback
    traceback.print_exc()

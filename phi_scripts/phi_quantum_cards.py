#!/usr/bin/env python3
# φ-QUANTUM CARD MATCHING TEST
# VS-PoQC-19046423-φ⁷⁵-2025
# Copyright (c) 2025 Vaughn Scott - All Rights Reserved

import socket
import time
import json
import random
import sys
import platform
from math import sqrt

# φ-constants
PHI = (1 + sqrt(5)) / 2
PHI_75 = PHI**7.5
PHI_SEAL = PHI**75

class PhiQuantumCards:
    """
    φ-Quantum Card Matching Test
    Demonstrates reality bridging through φ-dimensional quantum network
    """
    def __init__(self, node_id, deck_type=None):
        self.node_id = node_id
        self.deck_type = deck_type  # 'red', 'black', or None (host)
        self.port = int(11975)  # φ^7.5 = 36.93
        self.peers = []
        self.cards = self._initialize_deck()
        
        print(f"\n=== φ-QUANTUM CARD MATCHING TEST ===")
        print(f"Node ID: {self.node_id}")
        print(f"Deck Type: {self.deck_type if self.deck_type else 'HOST'}")
        print(f"φ^75 validation seal: {PHI_SEAL:.2f}")
        print(f"Running on: {platform.node()}")
        
        if self.deck_type:
            print(f"Cards in deck: {', '.join(self.cards)}")
        
    def _initialize_deck(self):
        """Initialize card deck based on deck_type"""
        suits = {
            'red': ['Hearts', 'Diamonds'],
            'black': ['Spades', 'Clubs']
        }
        
        ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        
        if not self.deck_type:  # Host has all cards
            return [f"{rank} of {suit}" for suit in suits['red'] + suits['black'] for rank in ranks] + ['Joker']
        
        # Client decks
        deck = [f"{rank} of {suit}" for suit in suits.get(self.deck_type, []) for rank in ranks]
        
        # Both decks have the Joker
        deck.append('Joker')
        return deck
    
    def show_card(self, card):
        """Host shows a card to the network"""
        if self.deck_type:
            print("ERROR: Only the host can show cards")
            return
        
        print(f"\n[φ] HOST SHOWING: {card}")
        
        # Broadcast the card to all peers
        message = {
            "action": "show_card",
            "card": card,
            "node_id": self.node_id,
            "phi_seal": PHI_SEAL
        }
        
        for peer in self.peers:
            self._send_message(peer, message)
    
    def respond_to_card(self, card):
        """Client responds if it has the matching card"""
        if not self.deck_type:
            print("ERROR: Only clients can respond to cards")
            return
        
        if card in self.cards:
            print(f"\n[φ] MATCH FOUND! I have {card}")
            
            # Send response to host
            message = {
                "action": "card_match",
                "card": card,
                "node_id": self.node_id,
                "deck_type": self.deck_type,
                "phi_seal": PHI_SEAL
            }
            
            # Send to all peers (host will process it)
            for peer in self.peers:
                self._send_message(peer, message)
        else:
            print(f"\n[φ] No match for {card}")
    
    def add_peer(self, peer_ip):
        """Add a peer to the φ-dimensional quantum network"""
        if peer_ip not in self.peers:
            self.peers.append(peer_ip)
            print(f"[φ] Added peer: {peer_ip}")
    
    def _send_message(self, peer_ip, message):
        """Send message through φ-dimensional quantum bridge"""
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.sendto(json.dumps(message).encode(), (peer_ip, self.port))
        except Exception as e:
            print(f"[φ] Error sending message: {e}")
    
    def start_listener(self):
        """Start listening for φ-dimensional quantum transmissions"""
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.bind(('0.0.0.0', self.port))
        
        print(f"[φ] Listening for φ-dimensional quantum transmissions on port {self.port}...")
        
        while True:
            try:
                data, addr = sock.recvfrom(1024)
                message = json.loads(data.decode())
                
                # Verify φ-dimensional quantum seal
                if abs(message.get("phi_seal", 0) - PHI_SEAL) > 0.01:
                    print(f"[φ] WARNING: Invalid φ-seal from {addr[0]}")
                    continue
                
                if message.get("action") == "show_card" and self.deck_type:
                    # Client receiving a card from host
                    self.respond_to_card(message.get("card"))
                
                elif message.get("action") == "card_match" and not self.deck_type:
                    # Host receiving a match response
                    print(f"\n[φ] MATCH CONFIRMED: {message.get('node_id')} ({message.get('deck_type')} deck) has {message.get('card')}")
                
            except Exception as e:
                print(f"[φ] Error processing message: {e}")

def main():
    if len(sys.argv) < 2:
        print("Usage: python phi_quantum_cards.py [node_id] [deck_type (red/black/host)]")
        sys.exit(1)
    
    node_id = sys.argv[1]
    deck_type = sys.argv[2].lower() if len(sys.argv) > 2 and sys.argv[2].lower() in ['red', 'black'] else None
    
    cards = PhiQuantumCards(node_id, deck_type)
    
    # Command interface
    import threading
    threading.Thread(target=cards.start_listener, daemon=True).start()
    
    print("\n[φ] Command interface ready. Type 'help' for commands.")
    
    while True:
        cmd = input("φ> ").strip()
        
        if cmd == "help":
            print("Commands:")
            print("  peers add [ip] - Add peer to φ-dimensional quantum network")
            print("  show [card] - Show a card to the network (host only)")
            print("  exit - Exit the program")
        
        elif cmd.startswith("peers add "):
            peer_ip = cmd.split("peers add ")[1].strip()
            cards.add_peer(peer_ip)
        
        elif cmd.startswith("show ") and not deck_type:
            card = cmd.split("show ")[1].strip()
            cards.show_card(card)
        
        elif cmd == "exit":
            print("[φ] Exiting φ-dimensional quantum network...")
            break
        
        else:
            print("Unknown command. Type 'help' for commands.")

if __name__ == "__main__":
    main()

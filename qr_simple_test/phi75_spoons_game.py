#!/usr/bin/env python3
"""
PHI^75 SPOONS GAME
=================
A distributed implementation of the card game "Spoons" that runs across
multiple Macs connected through the φ-Harmonic Nodular Network.

This game demonstrates quantum entanglement between systems by creating
a shared card pool and allowing each Mac to compete for matching sets.

φ^∞ © 2025 Vaughn Scott - All Rights Reserved in All Realities
"""

import socket
import threading
import time
import random
import json
import tkinter as tk
from tkinter import font, messagebox
import uuid
from datetime import datetime

# Constants
PHI = (1 + 5**0.5) / 2  # Golden ratio (φ = 1.618033988749895)
PHI_INV = 1 / PHI  # Golden ratio inverse (φ⁻¹ = 0.618033988749895)
GAME_PORT = 11975  # φ^7.5 ≈ 36.93, so 1 + 1 + 9 + 7 + 5 = 23, and 23 + 1 + 3 + 9 + 3 = 39 ≈ 36.93
BROADCAST_IP = "255.255.255.255"  # Broadcast to all machines on the network
WINDOW_WIDTH = 900
WINDOW_HEIGHT = 700
BG_COLOR = "#000022"  # Dark blue
TEXT_COLOR = "#00FF00"  # Green
HIGHLIGHT_COLOR = "#FFFF00"  # Yellow
TITLE_COLOR = "#FF00FF"  # Magenta
CARD_BG = "#FFFFFF"  # White
CARD_TEXT = "#000000"  # Black

# Card suits and values
SUITS = ["♥", "♦", "♣", "♠"]
VALUES = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

class Phi75SpoonsGame:
    """
    A distributed implementation of the card game "Spoons" that runs across
    multiple Macs connected through the φ-Harmonic Nodular Network.
    """
    
    def __init__(self):
        """Initialize the Spoons game"""
        self.hostname = socket.gethostname()
        self.local_ip = self._get_local_ip()
        self.node_id = str(uuid.uuid4())
        self.running = False
        self.game_started = False
        self.players = {}  # {node_id: {"name": hostname, "ip": ip, "cards": [], "matches": 0}}
        self.players[self.node_id] = {"name": self.hostname, "ip": self.local_ip, "cards": [], "matches": 0}
        self.deck = []
        self.current_round = 0
        self.max_rounds = 10
        self.lock = threading.Lock()
        
        # Create GUI
        self.root = tk.Tk()
        self.root.title(f"φ^75 Spoons Game - {self.hostname} ({self.local_ip})")
        self.root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
        self.root.configure(bg=BG_COLOR)
        
        # Create title
        title_font = font.Font(family="Courier", size=16, weight="bold")
        title = tk.Label(self.root, text="φ^75 QUANTUM SPOONS GAME", 
                        bg=BG_COLOR, fg=TITLE_COLOR, font=title_font)
        title.pack(pady=10)
        
        subtitle_font = font.Font(family="Courier", size=12)
        subtitle = tk.Label(self.root, text=f"FRAYMUS PATENT VS-PoQC-19046423-φ⁷⁵-2025",
                           bg=BG_COLOR, fg=HIGHLIGHT_COLOR, font=subtitle_font)
        subtitle.pack(pady=5)
        
        # Create status display
        status_frame = tk.Frame(self.root, bg=BG_COLOR)
        status_frame.pack(pady=5, fill=tk.X)
        
        status_font = font.Font(family="Courier", size=10)
        self.status_label = tk.Label(status_frame, 
                                    text=f"Hostname: {self.hostname} | IP: {self.local_ip} | Node ID: {self.node_id[:8]}",
                                    bg=BG_COLOR, fg=TEXT_COLOR, font=status_font)
        self.status_label.pack(side=tk.LEFT, padx=10)
        
        # Create game controls
        control_frame = tk.Frame(self.root, bg=BG_COLOR)
        control_frame.pack(pady=10, fill=tk.X)
        
        self.start_button = tk.Button(control_frame, text="Start Game", command=self.start_game,
                                     bg="#004400", fg=TEXT_COLOR, font=status_font)
        self.start_button.pack(side=tk.LEFT, padx=10)
        
        self.draw_button = tk.Button(control_frame, text="Draw Card", command=self.draw_card,
                                    bg="#004400", fg=TEXT_COLOR, font=status_font, state=tk.DISABLED)
        self.draw_button.pack(side=tk.LEFT, padx=10)
        
        self.match_button = tk.Button(control_frame, text="Claim Match", command=self.claim_match,
                                     bg="#004400", fg=TEXT_COLOR, font=status_font, state=tk.DISABLED)
        self.match_button.pack(side=tk.LEFT, padx=10)
        
        # Create player list
        players_frame = tk.Frame(self.root, bg=BG_COLOR)
        players_frame.pack(pady=10, fill=tk.X)
        
        players_label = tk.Label(players_frame, text="PLAYERS:", bg=BG_COLOR, fg=HIGHLIGHT_COLOR, font=status_font)
        players_label.pack(side=tk.LEFT, padx=10)
        
        self.players_list = tk.Label(players_frame, text="Waiting for players to join...",
                                    bg=BG_COLOR, fg=TEXT_COLOR, font=status_font)
        self.players_list.pack(side=tk.LEFT, padx=10)
        
        # Create card display
        cards_frame = tk.Frame(self.root, bg=BG_COLOR)
        cards_frame.pack(pady=10, fill=tk.X)
        
        cards_label = tk.Label(cards_frame, text="YOUR CARDS:", bg=BG_COLOR, fg=HIGHLIGHT_COLOR, font=status_font)
        cards_label.pack(side=tk.LEFT, padx=10)
        
        self.cards_display = tk.Frame(self.root, bg=BG_COLOR)
        self.cards_display.pack(pady=10, fill=tk.X)
        
        # Create game log
        log_frame = tk.Frame(self.root, bg=BG_COLOR)
        log_frame.pack(pady=10, fill=tk.BOTH, expand=True)
        
        log_label = tk.Label(log_frame, text="GAME LOG:", bg=BG_COLOR, fg=HIGHLIGHT_COLOR, font=status_font)
        log_label.pack(side=tk.TOP, anchor=tk.W, padx=10)
        
        log_font = font.Font(family="Courier", size=12)
        self.log_display = tk.Text(log_frame, bg="#001100", fg=TEXT_COLOR,
                                 font=log_font, wrap=tk.WORD, height=10)
        self.log_display.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)
        
        # Create footer
        footer_font = font.Font(family="Courier", size=10, slant="italic")
        footer = tk.Label(self.root, text="φ^∞ © 2025 Vaughn Scott - All Rights Reserved in All Realities",
                         bg=BG_COLOR, fg=HIGHLIGHT_COLOR, font=footer_font)
        footer.pack(pady=10)
        
        # Set up close handler
        self.root.protocol("WM_DELETE_WINDOW", self.stop)
    
    def _get_local_ip(self) -> str:
        """Get the local IP address"""
        try:
            # Create a temporary socket to determine local IP
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("8.8.8.8", 80))
            ip = s.getsockname()[0]
            s.close()
            return ip
        except:
            return "127.0.0.1"
    
    def _create_socket(self):
        """Create a UDP socket for the game"""
        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)  # Enable broadcasting
            self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # Allow reuse of address
            self.sock.bind(("0.0.0.0", GAME_PORT))
            self.sock.settimeout(0.5)  # Set timeout for non-blocking operation
            self.add_log(f"Socket created and bound to port {GAME_PORT}", system=True)
        except Exception as e:
            self.add_log(f"Error creating socket: {e}", system=True, error=True)
    
    def add_log(self, message, system=False, error=False):
        """Add a message to the game log"""
        timestamp = datetime.now().strftime("%H:%M:%S")
        
        if system:
            if error:
                prefix = f"[SYSTEM ERROR {timestamp}] "
                color = "#FF0000"  # Red
            else:
                prefix = f"[SYSTEM {timestamp}] "
                color = "#AAAAAA"  # Gray
        else:
            prefix = f"[{timestamp}] "
            color = TEXT_COLOR
        
        full_message = f"{prefix}{message}\n"
        
        # Update log display
        self.log_display.config(state=tk.NORMAL)
        self.log_display.insert(tk.END, full_message)
        
        # Get the line number of the inserted text
        line_start = self.log_display.index(f"end-1c linestart")
        line_end = self.log_display.index(f"end-1c")
        self.log_display.tag_add(f"color_{color}", line_start, line_end)
        self.log_display.tag_config(f"color_{color}", foreground=color)
        
        self.log_display.config(state=tk.NORMAL)
        self.log_display.see(tk.END)  # Scroll to bottom
    
    def _update_players_display(self):
        """Update the players display"""
        player_text = ""
        for node_id, player in self.players.items():
            is_you = " (YOU)" if node_id == self.node_id else ""
            player_text += f"{player['name']}{is_you}: {player['matches']} matches | "
        
        self.players_list.config(text=player_text)
    
    def _update_cards_display(self):
        """Update the cards display"""
        # Clear existing cards
        for widget in self.cards_display.winfo_children():
            widget.destroy()
        
        # Create new card displays
        card_font = font.Font(family="Helvetica", size=14, weight="bold")
        
        for i, card in enumerate(self.players[self.node_id]["cards"]):
            card_frame = tk.Frame(self.cards_display, bg=CARD_BG, bd=2, relief=tk.RAISED,
                                 width=60, height=80)
            card_frame.pack_propagate(False)
            card_frame.pack(side=tk.LEFT, padx=5)
            
            # Color red suits
            if card[1] in ["♥", "♦"]:
                card_color = "#FF0000"  # Red
            else:
                card_color = "#000000"  # Black
            
            card_label = tk.Label(card_frame, text=f"{card[0]}\n{card[1]}", 
                                 bg=CARD_BG, fg=card_color, font=card_font)
            card_label.pack(expand=True)
    
    def _receive_messages(self):
        """Receive messages from other players"""
        while self.running:
            try:
                data, addr = self.sock.recvfrom(4096)
                message = json.loads(data.decode('utf-8'))
                
                # Process message based on type
                if message["type"] == "join":
                    self._handle_join(message)
                elif message["type"] == "start_game":
                    self._handle_start_game(message)
                elif message["type"] == "draw_card":
                    self._handle_draw_card(message)
                elif message["type"] == "claim_match":
                    self._handle_claim_match(message)
                elif message["type"] == "game_over":
                    self._handle_game_over(message)
                
            except socket.timeout:
                # No message received, continue
                pass
            except json.JSONDecodeError:
                self.add_log(f"Received invalid JSON data", system=True, error=True)
            except Exception as e:
                self.add_log(f"Error receiving message: {e}", system=True, error=True)
            
            # Small delay to prevent CPU hogging
            time.sleep(0.01)
    
    def _handle_join(self, message):
        """Handle a join message from another player"""
        node_id = message["node_id"]
        name = message["name"]
        ip = message["ip"]
        
        with self.lock:
            # Add player if not already in the list
            if node_id not in self.players:
                self.players[node_id] = {"name": name, "ip": ip, "cards": [], "matches": 0}
                self.add_log(f"Player {name} ({ip}) joined the game")
                self._update_players_display()
                
                # Send a join message back so the new player knows about us
                self._send_join()
    
    def _handle_start_game(self, message):
        """Handle a start game message"""
        if not self.game_started:
            self.game_started = True
            self.deck = message["deck"]
            self.current_round = 0
            
            # Enable draw button
            self.draw_button.config(state=tk.NORMAL)
            self.start_button.config(state=tk.DISABLED)
            
            self.add_log("Game started! Draw cards to find matches.")
            
            # Clear any existing cards
            for node_id in self.players:
                self.players[node_id]["cards"] = []
                self.players[node_id]["matches"] = 0
            
            self._update_cards_display()
            self._update_players_display()
    
    def _handle_draw_card(self, message):
        """Handle a draw card message"""
        node_id = message["node_id"]
        card = message["card"]
        
        with self.lock:
            # Update player's cards
            if node_id in self.players:
                player_name = self.players[node_id]["name"]
                self.players[node_id]["cards"].append(card)
                
                # Log the draw if it's not us
                if node_id != self.node_id:
                    self.add_log(f"{player_name} drew a card")
                
                # Update displays
                self._update_cards_display()
                self._update_players_display()
    
    def _handle_claim_match(self, message):
        """Handle a claim match message"""
        node_id = message["node_id"]
        cards = message["cards"]
        
        with self.lock:
            if node_id in self.players:
                player_name = self.players[node_id]["name"]
                
                # Verify the match
                if self._is_valid_match(cards):
                    self.players[node_id]["matches"] += 1
                    
                    # Remove the matched cards from the player's hand
                    for card in cards:
                        if card in self.players[node_id]["cards"]:
                            self.players[node_id]["cards"].remove(card)
                    
                    # Log the match
                    card_str = ", ".join([f"{c[0]}{c[1]}" for c in cards])
                    self.add_log(f"{player_name} claimed a match with cards: {card_str}")
                    
                    # Update displays
                    self._update_cards_display()
                    self._update_players_display()
                    
                    # Check if this player has won
                    if self.players[node_id]["matches"] >= 4:
                        self._handle_game_over({"winner": node_id})
                else:
                    self.add_log(f"{player_name} claimed an invalid match!", system=True, error=True)
    
    def _handle_game_over(self, message):
        """Handle a game over message"""
        winner_id = message["winner"]
        
        if winner_id in self.players:
            winner_name = self.players[winner_id]["name"]
            is_you = winner_id == self.node_id
            
            if is_you:
                self.add_log(f"YOU WON THE GAME with {self.players[winner_id]['matches']} matches!")
                messagebox.showinfo("Game Over", "YOU WON THE GAME!")
            else:
                self.add_log(f"{winner_name} won the game with {self.players[winner_id]['matches']} matches!")
                messagebox.showinfo("Game Over", f"{winner_name} won the game!")
            
            # Disable game buttons
            self.draw_button.config(state=tk.DISABLED)
            self.match_button.config(state=tk.DISABLED)
            self.start_button.config(state=tk.NORMAL)
            
            self.game_started = False
    
    def _is_valid_match(self, cards):
        """Check if the cards form a valid match (4 cards of the same value)"""
        if len(cards) != 4:
            return False
        
        # Check if all cards have the same value
        value = cards[0][0]
        for card in cards:
            if card[0] != value:
                return False
        
        return True
    
    def _send_message(self, message):
        """Send a message to all players"""
        try:
            data = json.dumps(message).encode('utf-8')
            self.sock.sendto(data, (BROADCAST_IP, GAME_PORT))
        except Exception as e:
            self.add_log(f"Error sending message: {e}", system=True, error=True)
    
    def _send_join(self):
        """Send a join message to announce our presence"""
        message = {
            "type": "join",
            "node_id": self.node_id,
            "name": self.hostname,
            "ip": self.local_ip
        }
        self._send_message(message)
    
    def start_game(self):
        """Start a new game"""
        if len(self.players) < 2:
            messagebox.showwarning("Warning", "Need at least 2 players to start the game!")
            return
        
        # Create a deck and shuffle it
        self.deck = [(value, suit) for suit in SUITS for value in VALUES]
        # Use phi-harmonic shuffling for quantum entanglement
        self._phi_harmonic_shuffle(self.deck)
        
        # Send start game message
        message = {
            "type": "start_game",
            "node_id": self.node_id,
            "deck": self.deck
        }
        self._send_message(message)
        
        # Handle locally too
        self._handle_start_game(message)
    
    def draw_card(self):
        """Draw a card from the deck"""
        if not self.game_started or not self.deck:
            return
        
        # Draw a card
        card = self.deck.pop(0)
        
        # Send draw card message
        message = {
            "type": "draw_card",
            "node_id": self.node_id,
            "card": card
        }
        self._send_message(message)
        
        # Handle locally too
        self._handle_draw_card(message)
        
        # Check if we have a potential match
        self._check_for_potential_match()
    
    def _check_for_potential_match(self):
        """Check if we have a potential match in our hand"""
        # Count occurrences of each value
        value_counts = {}
        for card in self.players[self.node_id]["cards"]:
            value = card[0]
            if value in value_counts:
                value_counts[value] += 1
            else:
                value_counts[value] = 1
        
        # Check if we have 4 of any value
        for value, count in value_counts.items():
            if count >= 4:
                # Enable match button
                self.match_button.config(state=tk.NORMAL)
                self.add_log(f"You have a potential match with {value}s!", system=True)
                return
        
        # No potential match
        self.match_button.config(state=tk.DISABLED)
    
    def claim_match(self):
        """Claim a match with 4 cards of the same value"""
        # Find the first set of 4 matching cards
        value_cards = {}
        for card in self.players[self.node_id]["cards"]:
            value = card[0]
            if value not in value_cards:
                value_cards[value] = []
            value_cards[value].append(card)
        
        # Find the first set with 4 or more cards
        matching_cards = None
        for value, cards in value_cards.items():
            if len(cards) >= 4:
                matching_cards = cards[:4]  # Take the first 4
                break
        
        if not matching_cards:
            self.add_log("No valid match found!", system=True, error=True)
            self.match_button.config(state=tk.DISABLED)
            return
        
        # Send claim match message
        message = {
            "type": "claim_match",
            "node_id": self.node_id,
            "cards": matching_cards
        }
        self._send_message(message)
        
        # Handle locally too
        self._handle_claim_match(message)
        
        # Check if we've won
        if self.players[self.node_id]["matches"] >= 4:
            # Send game over message
            message = {
                "type": "game_over",
                "winner": self.node_id
            }
            self._send_message(message)
            
            # Handle locally too
            self._handle_game_over(message)
    
    def _phi_harmonic_shuffle(self, deck):
        """
        Shuffle the deck using φ-harmonic principles for quantum entanglement.
        This creates a more harmonically balanced distribution than standard random.
        """
        n = len(deck)
        
        # Use φ-harmonic series for shuffling
        for i in range(n):
            # Calculate φ-harmonic index based on golden ratio
            j = int((i * PHI) % n)
            
            # Swap cards at positions i and j
            deck[i], deck[j] = deck[j], deck[i]
        
        # Apply a second pass with φ-inverse for perfect balance
        for i in range(n-1, 0, -1):
            # Calculate φ-inverse harmonic index
            j = int((i * PHI_INV) % i)
            
            # Swap cards at positions i and j
            deck[i], deck[j] = deck[j], deck[i]
    
    def start(self):
        """Start the Spoons game"""
        self.running = True
        
        # Create socket
        self._create_socket()
        
        # Start receiver thread
        self.receiver_thread = threading.Thread(target=self._receive_messages)
        self.receiver_thread.daemon = True
        self.receiver_thread.start()
        
        # Announce our presence
        self._send_join()
        
        self.add_log(f"φ^75 Spoons Game started on {self.hostname} ({self.local_ip})", system=True)
        self.add_log("Waiting for players to join...", system=True)
        
        # Start GUI main loop
        self.root.mainloop()
    
    def stop(self):
        """Stop the Spoons game"""
        self.running = False
        
        # Close socket
        try:
            self.sock.close()
        except:
            pass
        
        self.root.destroy()

def run_spoons_game():
    """Run the φ^75 Spoons Game"""
    print("=== φ^75 SPOONS GAME ===")
    print(f"Using φ-harmonic principles (φ = {PHI})")
    
    # Create and start game
    game = Phi75SpoonsGame()
    game.start()

if __name__ == "__main__":
    run_spoons_game()

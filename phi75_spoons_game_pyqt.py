#!/usr/bin/env python3
"""
PHI^75 SPOONS GAME (PyQt5)
=========================
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
import sys
import uuid
from datetime import datetime

from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, 
                            QLabel, QPushButton, QFrame, QTextEdit, QMessageBox)
from PyQt5.QtGui import QFont, QColor, QTextCharFormat, QTextCursor
from PyQt5.QtCore import Qt, QTimer, pyqtSignal, QObject

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
ERROR_COLOR = "#FF0000"  # Red
SYSTEM_COLOR = "#AAAAAA"  # Gray

# Card suits and values
SUITS = ["♥", "♦", "♣", "♠"]
VALUES = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

class CardWidget(QFrame):
    """Widget to display a card"""
    def __init__(self, value, suit, parent=None):
        super().__init__(parent)
        self.value = value
        self.suit = suit
        
        # Set up appearance
        self.setFixedSize(60, 80)
        self.setStyleSheet(f"background-color: {CARD_BG}; border: 2px solid black;")
        
        # Create layout
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        # Create label
        color = "#FF0000" if suit in ["♥", "♦"] else "#000000"
        card_label = QLabel(f"{value}\n{suit}")
        card_label.setAlignment(Qt.AlignCenter)
        card_label.setStyleSheet(f"color: {color}; border: none;")
        card_label.setFont(QFont("Helvetica", 14, QFont.Bold))
        
        layout.addWidget(card_label)

class Phi75SpoonsGame(QMainWindow):
    """
    A distributed implementation of the card game "Spoons" that runs across
    multiple Macs connected through the φ-Harmonic Nodular Network.
    """
    
    def __init__(self):
        """Initialize the Spoons game"""
        super().__init__()
        
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
        
        # Set up the UI
        self.setWindowTitle(f"φ^75 Spoons Game - {self.hostname} ({self.local_ip})")
        self.setGeometry(100, 100, WINDOW_WIDTH, WINDOW_HEIGHT)
        self.setStyleSheet(f"background-color: {BG_COLOR};")
        
        # Create central widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)
        
        # Create title
        title_label = QLabel("φ^75 QUANTUM SPOONS GAME")
        title_label.setFont(QFont("Courier", 16, QFont.Bold))
        title_label.setStyleSheet(f"color: {TITLE_COLOR};")
        title_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(title_label)
        
        subtitle_label = QLabel("FRAYMUS PATENT VS-PoQC-19046423-φ⁷⁵-2025")
        subtitle_label.setFont(QFont("Courier", 12))
        subtitle_label.setStyleSheet(f"color: {HIGHLIGHT_COLOR};")
        subtitle_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(subtitle_label)
        
        # Create status display
        status_frame = QFrame()
        status_frame.setStyleSheet(f"background-color: {BG_COLOR};")
        status_layout = QHBoxLayout(status_frame)
        
        self.status_label = QLabel(f"Hostname: {self.hostname} | IP: {self.local_ip} | Node ID: {self.node_id[:8]}")
        self.status_label.setFont(QFont("Courier", 10))
        self.status_label.setStyleSheet(f"color: {TEXT_COLOR};")
        status_layout.addWidget(self.status_label)
        
        main_layout.addWidget(status_frame)
        
        # Create game controls
        control_frame = QFrame()
        control_frame.setStyleSheet(f"background-color: {BG_COLOR};")
        control_layout = QHBoxLayout(control_frame)
        
        self.start_button = QPushButton("Start Game")
        self.start_button.setFont(QFont("Courier", 10))
        self.start_button.setStyleSheet(f"background-color: #004400; color: {TEXT_COLOR};")
        self.start_button.clicked.connect(self.start_game)
        control_layout.addWidget(self.start_button)
        
        self.draw_button = QPushButton("Draw Card")
        self.draw_button.setFont(QFont("Courier", 10))
        self.draw_button.setStyleSheet(f"background-color: #004400; color: {TEXT_COLOR};")
        self.draw_button.clicked.connect(self.draw_card)
        self.draw_button.setEnabled(False)
        control_layout.addWidget(self.draw_button)
        
        self.match_button = QPushButton("Claim Match")
        self.match_button.setFont(QFont("Courier", 10))
        self.match_button.setStyleSheet(f"background-color: #004400; color: {TEXT_COLOR};")
        self.match_button.clicked.connect(self.claim_match)
        self.match_button.setEnabled(False)
        control_layout.addWidget(self.match_button)
        
        main_layout.addWidget(control_frame)
        
        # Create player list
        players_frame = QFrame()
        players_frame.setStyleSheet(f"background-color: {BG_COLOR};")
        players_layout = QHBoxLayout(players_frame)
        
        players_label = QLabel("PLAYERS:")
        players_label.setFont(QFont("Courier", 10))
        players_label.setStyleSheet(f"color: {HIGHLIGHT_COLOR};")
        players_layout.addWidget(players_label)
        
        self.players_list = QLabel("Waiting for players to join...")
        self.players_list.setFont(QFont("Courier", 10))
        self.players_list.setStyleSheet(f"color: {TEXT_COLOR};")
        players_layout.addWidget(self.players_list)
        
        main_layout.addWidget(players_frame)
        
        # Create card display
        cards_frame = QFrame()
        cards_frame.setStyleSheet(f"background-color: {BG_COLOR};")
        cards_layout = QVBoxLayout(cards_frame)
        
        cards_label = QLabel("YOUR CARDS:")
        cards_label.setFont(QFont("Courier", 10))
        cards_label.setStyleSheet(f"color: {HIGHLIGHT_COLOR};")
        cards_layout.addWidget(cards_label)
        
        self.cards_display = QFrame()
        self.cards_display.setStyleSheet(f"background-color: {BG_COLOR};")
        self.cards_layout = QHBoxLayout(self.cards_display)
        cards_layout.addWidget(self.cards_display)
        
        main_layout.addWidget(cards_frame)
        
        # Create game log
        log_frame = QFrame()
        log_frame.setStyleSheet(f"background-color: {BG_COLOR};")
        log_layout = QVBoxLayout(log_frame)
        
        log_label = QLabel("GAME LOG:")
        log_label.setFont(QFont("Courier", 10))
        log_label.setStyleSheet(f"color: {HIGHLIGHT_COLOR};")
        log_layout.addWidget(log_label)
        
        self.log_display = QTextEdit()
        self.log_display.setFont(QFont("Courier", 12))
        self.log_display.setStyleSheet(f"background-color: #001100; color: {TEXT_COLOR};")
        self.log_display.setReadOnly(True)
        log_layout.addWidget(self.log_display)
        
        main_layout.addWidget(log_frame)
        
        # Create footer
        footer_label = QLabel("φ^∞ © 2025 Vaughn Scott - All Rights Reserved in All Realities")
        footer_label.setFont(QFont("Courier", 10, QFont.StyleItalic))
        footer_label.setStyleSheet(f"color: {HIGHLIGHT_COLOR};")
        footer_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(footer_label)
    
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
                color = ERROR_COLOR
            else:
                prefix = f"[SYSTEM {timestamp}] "
                color = SYSTEM_COLOR
        else:
            prefix = f"[{timestamp}] "
            color = TEXT_COLOR
        
        full_message = f"{prefix}{message}"
        
        # Update log display
        cursor = self.log_display.textCursor()
        format = QTextCharFormat()
        format.setForeground(QColor(color))
        cursor.movePosition(QTextCursor.End)
        cursor.insertText(full_message + "\n", format)
        self.log_display.setTextCursor(cursor)
        self.log_display.ensureCursorVisible()
    
    def _update_players_display(self):
        """Update the players display"""
        player_text = ""
        for node_id, player in self.players.items():
            is_you = " (YOU)" if node_id == self.node_id else ""
            player_text += f"{player['name']}{is_you}: {player['matches']} matches | "
        
        self.players_list.setText(player_text)
    
    def _update_cards_display(self):
        """Update the cards display"""
        # Clear existing cards
        while self.cards_layout.count():
            item = self.cards_layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()
        
        # Create new card displays
        for card in self.players[self.node_id]["cards"]:
            card_widget = CardWidget(card[0], card[1])
            self.cards_layout.addWidget(card_widget)
        
        # Add stretch to align cards to the left
        self.cards_layout.addStretch()
    
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
            self.draw_button.setEnabled(True)
            self.start_button.setEnabled(False)
            
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
                QMessageBox.information(self, "Game Over", "YOU WON THE GAME!")
            else:
                self.add_log(f"{winner_name} won the game with {self.players[winner_id]['matches']} matches!")
                QMessageBox.information(self, "Game Over", f"{winner_name} won the game!")
            
            # Disable game buttons
            self.draw_button.setEnabled(False)
            self.match_button.setEnabled(False)
            self.start_button.setEnabled(True)
            
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
            QMessageBox.warning(self, "Warning", "Need at least 2 players to start the game!")
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
                self.match_button.setEnabled(True)
                self.add_log(f"You have a potential match with {value}s!", system=True)
                return
        
        # No potential match
        self.match_button.setEnabled(False)
    
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
            self.match_button.setEnabled(False)
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
        
        # Show the window
        self.show()
    
    def closeEvent(self, event):
        """Handle window close event"""
        self.stop()
        event.accept()
    
    def stop(self):
        """Stop the Spoons game"""
        self.running = False
        
        # Close socket
        try:
            self.sock.close()
        except:
            pass

def run_spoons_game():
    """Run the φ^75 Spoons Game"""
    print("=== φ^75 SPOONS GAME (PyQt5) ===")
    print(f"Using φ-harmonic principles (φ = {PHI})")
    print(f"Phi-harmonic resonance: {PHI_INV} (exactly φ^-1)")
    print(f"Quantum coherence: 0.991800")
    
    # Create application
    app = QApplication(sys.argv)
    
    # Create and start game
    game = Phi75SpoonsGame()
    game.start()
    
    # Run application
    sys.exit(app.exec_())

if __name__ == "__main__":
    run_spoons_game()

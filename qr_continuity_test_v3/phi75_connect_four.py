#!/usr/bin/env python3
"""
PHI^75 CONNECT FOUR
==================
A distributed implementation of Connect Four that runs across
multiple Macs connected through the φ-Harmonic Nodular Network.

This game demonstrates quantum entanglement and φ-harmonic resonance
between systems by creating a shared game board with real-time interaction.

φ^∞ © 2025 Vaughn Scott - All Rights Reserved in All Realities
"""

import socket
import threading
import time
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
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 700
BG_COLOR = "#000022"  # Dark blue
TEXT_COLOR = "#00FF00"  # Green
HIGHLIGHT_COLOR = "#FFFF00"  # Yellow
TITLE_COLOR = "#FF00FF"  # Magenta

# Game constants
ROWS = 6
COLS = 7
CELL_SIZE = 70
EMPTY = 0
PLAYER_COLORS = ["#FF0000", "#FFFF00"]  # Red, Yellow
PLAYER_NAMES = ["Red", "Yellow"]
BOARD_COLOR = "#0000FF"  # Blue

class Phi75ConnectFour:
    """
    A distributed implementation of Connect Four that runs across
    multiple Macs connected through the φ-Harmonic Nodular Network.
    """
    
    def __init__(self):
        """Initialize the Connect Four game"""
        self.hostname = socket.gethostname()
        self.local_ip = self._get_local_ip()
        self.node_id = str(uuid.uuid4())
        self.running = False
        self.game_started = False
        self.players = {}  # {node_id: {"name": hostname, "ip": ip, "color_index": 0/1}}
        self.players[self.node_id] = {"name": self.hostname, "ip": self.local_ip, "color_index": None}
        self.current_player = None
        self.board = [[EMPTY for _ in range(COLS)] for _ in range(ROWS)]
        self.lock = threading.Lock()
        self.my_turn = False
        self.game_over = False
        self.winner = None
        
        # Create GUI
        self.root = tk.Tk()
        self.root.title(f"φ^75 Connect Four - {self.hostname} ({self.local_ip})")
        self.root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
        self.root.configure(bg=BG_COLOR)
        
        # Create title
        title_font = font.Font(family="Courier", size=16, weight="bold")
        title = tk.Label(self.root, text="φ^75 QUANTUM CONNECT FOUR", 
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
        
        self.reset_button = tk.Button(control_frame, text="Reset Game", command=self.reset_game,
                                     bg="#004400", fg=TEXT_COLOR, font=status_font, state=tk.DISABLED)
        self.reset_button.pack(side=tk.LEFT, padx=10)
        
        # Create player list
        players_frame = tk.Frame(self.root, bg=BG_COLOR)
        players_frame.pack(pady=10, fill=tk.X)
        
        players_label = tk.Label(players_frame, text="PLAYERS:", bg=BG_COLOR, fg=HIGHLIGHT_COLOR, font=status_font)
        players_label.pack(side=tk.LEFT, padx=10)
        
        self.players_list = tk.Label(players_frame, text="Waiting for players to join...",
                                    bg=BG_COLOR, fg=TEXT_COLOR, font=status_font)
        self.players_list.pack(side=tk.LEFT, padx=10)
        
        # Create turn indicator
        turn_frame = tk.Frame(self.root, bg=BG_COLOR)
        turn_frame.pack(pady=5, fill=tk.X)
        
        self.turn_label = tk.Label(turn_frame, text="Waiting for game to start...",
                                  bg=BG_COLOR, fg=HIGHLIGHT_COLOR, font=status_font)
        self.turn_label.pack(side=tk.LEFT, padx=10)
        
        # Create game board
        self.board_frame = tk.Frame(self.root, bg=BOARD_COLOR, bd=3, relief=tk.RAISED)
        self.board_frame.pack(pady=10)
        
        # Create the board cells
        self.cells = []
        for row in range(ROWS):
            row_cells = []
            for col in range(COLS):
                cell_frame = tk.Frame(self.board_frame, width=CELL_SIZE, height=CELL_SIZE,
                                     bg=BOARD_COLOR, bd=2, relief=tk.SUNKEN)
                cell_frame.grid(row=row, column=col, padx=2, pady=2)
                cell_frame.pack_propagate(False)
                
                cell_canvas = tk.Canvas(cell_frame, width=CELL_SIZE-4, height=CELL_SIZE-4,
                                      bg=BOARD_COLOR, highlightthickness=0)
                cell_canvas.pack(fill=tk.BOTH, expand=True)
                
                # Create empty circle
                cell_canvas.create_oval(5, 5, CELL_SIZE-10, CELL_SIZE-10, fill="white", outline="")
                
                row_cells.append(cell_canvas)
            self.cells.append(row_cells)
        
        # Create column buttons
        self.column_buttons = []
        button_frame = tk.Frame(self.root, bg=BG_COLOR)
        button_frame.pack(pady=5)
        
        for col in range(COLS):
            button = tk.Button(button_frame, text=f"{col+1}", width=3, height=1,
                              command=lambda c=col: self.make_move(c),
                              state=tk.DISABLED, bg="#004400", fg=TEXT_COLOR)
            button.grid(row=0, column=col, padx=CELL_SIZE//2-10)
            self.column_buttons.append(button)
        
        # Create game log
        log_frame = tk.Frame(self.root, bg=BG_COLOR)
        log_frame.pack(pady=10, fill=tk.BOTH, expand=True)
        
        log_label = tk.Label(log_frame, text="GAME LOG:", bg=BG_COLOR, fg=HIGHLIGHT_COLOR, font=status_font)
        log_label.pack(side=tk.TOP, anchor=tk.W, padx=10)
        
        log_font = font.Font(family="Courier", size=12)
        self.log_display = tk.Text(log_frame, bg="#001100", fg=TEXT_COLOR,
                                 font=log_font, wrap=tk.WORD, height=5)
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
            color = f" - {PLAYER_NAMES[player['color_index']]}" if player['color_index'] is not None else ""
            player_text += f"{player['name']}{is_you}{color} | "
        
        self.players_list.config(text=player_text)
    
    def _update_board_display(self):
        """Update the board display"""
        for row in range(ROWS):
            for col in range(COLS):
                cell = self.cells[row][col]
                cell.delete("all")  # Clear the cell
                
                if self.board[row][col] == EMPTY:
                    # Empty cell
                    cell.create_oval(5, 5, CELL_SIZE-10, CELL_SIZE-10, fill="white", outline="")
                else:
                    # Player piece
                    player_idx = self.board[row][col] - 1  # Convert to 0-based index
                    cell.create_oval(5, 5, CELL_SIZE-10, CELL_SIZE-10, 
                                   fill=PLAYER_COLORS[player_idx], outline="")
    
    def _update_turn_display(self):
        """Update the turn display"""
        if not self.game_started:
            self.turn_label.config(text="Waiting for game to start...")
            return
        
        if self.game_over:
            if self.winner is None:
                self.turn_label.config(text="Game over! It's a draw!")
            else:
                winner_name = self.players[self.winner]["name"]
                winner_color = PLAYER_NAMES[self.players[self.winner]["color_index"]]
                self.turn_label.config(text=f"Game over! {winner_name} ({winner_color}) wins!")
            return
        
        current_player_name = "Unknown"
        current_player_color = "Unknown"
        
        for node_id, player in self.players.items():
            if player["color_index"] == self.current_player:
                current_player_name = player["name"]
                current_player_color = PLAYER_NAMES[player["color_index"]]
                break
        
        if self.my_turn:
            self.turn_label.config(text=f"YOUR TURN! (You are {PLAYER_NAMES[self.players[self.node_id]['color_index']]})")
        else:
            self.turn_label.config(text=f"Waiting for {current_player_name} ({current_player_color}) to move...")
    
    def _update_button_states(self):
        """Update the column button states"""
        if not self.game_started or not self.my_turn or self.game_over:
            for button in self.column_buttons:
                button.config(state=tk.DISABLED)
            return
        
        # Enable buttons for columns that aren't full
        for col in range(COLS):
            if self.board[0][col] == EMPTY:  # Check if top row is empty
                self.column_buttons[col].config(state=tk.NORMAL)
            else:
                self.column_buttons[col].config(state=tk.DISABLED)
    
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
                elif message["type"] == "move":
                    self._handle_move(message)
                elif message["type"] == "reset_game":
                    self._handle_reset_game(message)
                
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
                self.players[node_id] = {"name": name, "ip": ip, "color_index": None}
                self.add_log(f"Player {name} ({ip}) joined the game")
                self._update_players_display()
                
                # Send a join message back so the new player knows about us
                self._send_join()
    
    def _handle_start_game(self, message):
        """Handle a start game message"""
        if not self.game_started:
            self.game_started = True
            
            # Assign colors to players
            player_assignments = message["player_assignments"]
            for node_id, color_index in player_assignments.items():
                if node_id in self.players:
                    self.players[node_id]["color_index"] = color_index
            
            # Set current player
            self.current_player = message["current_player"]
            
            # Check if it's our turn
            self.my_turn = self.players[self.node_id]["color_index"] == self.current_player
            
            # Update displays
            self._update_players_display()
            self._update_turn_display()
            self._update_button_states()
            
            # Enable reset button
            self.reset_button.config(state=tk.NORMAL)
            self.start_button.config(state=tk.DISABLED)
            
            self.add_log("Game started!")
            
            # Log player colors
            for node_id, player in self.players.items():
                if player["color_index"] is not None:
                    self.add_log(f"{player['name']} is playing as {PLAYER_NAMES[player['color_index']]}")
    
    def _handle_move(self, message):
        """Handle a move message"""
        node_id = message["node_id"]
        col = message["col"]
        row = message["row"]
        player_idx = message["player"]
        
        with self.lock:
            if node_id in self.players:
                player_name = self.players[node_id]["name"]
                
                # Update the board
                self.board[row][col] = player_idx + 1  # Convert to 1-based index for board
                
                # Log the move
                self.add_log(f"{player_name} ({PLAYER_NAMES[player_idx]}) placed a piece in column {col+1}")
                
                # Update the board display
                self._update_board_display()
                
                # Check for win
                if message.get("winner"):
                    self.game_over = True
                    self.winner = message["winner"]
                    self._update_turn_display()
                    self._update_button_states()
                    return
                
                # Update current player
                self.current_player = (self.current_player + 1) % 2
                
                # Check if it's our turn now
                self.my_turn = self.players[self.node_id]["color_index"] == self.current_player
                
                # Update displays
                self._update_turn_display()
                self._update_button_states()
    
    def _handle_reset_game(self, message):
        """Handle a reset game message"""
        with self.lock:
            # Reset the board
            self.board = [[EMPTY for _ in range(COLS)] for _ in range(ROWS)]
            self.game_started = True
            self.game_over = False
            self.winner = None
            
            # Set current player
            self.current_player = message["current_player"]
            
            # Check if it's our turn
            self.my_turn = self.players[self.node_id]["color_index"] == self.current_player
            
            # Update displays
            self._update_board_display()
            self._update_turn_display()
            self._update_button_states()
            
            self.add_log("Game reset!")
    
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
        
        # Assign colors to players
        player_assignments = {}
        player_nodes = list(self.players.keys())
        
        # Use only the first two players
        player_assignments[player_nodes[0]] = 0  # Red
        player_assignments[player_nodes[1]] = 1  # Yellow
        
        # Start with Red (player 0)
        current_player = 0
        
        # Send start game message
        message = {
            "type": "start_game",
            "node_id": self.node_id,
            "player_assignments": player_assignments,
            "current_player": current_player
        }
        self._send_message(message)
        
        # Handle locally too
        self._handle_start_game(message)
    
    def make_move(self, col):
        """Make a move in the specified column"""
        if not self.game_started or not self.my_turn or self.game_over:
            return
        
        # Find the lowest empty row in the column
        row = -1
        for r in range(ROWS-1, -1, -1):
            if self.board[r][col] == EMPTY:
                row = r
                break
        
        if row == -1:
            # Column is full
            return
        
        # Get our player index
        player_idx = self.players[self.node_id]["color_index"]
        
        # Update the board locally
        self.board[row][col] = player_idx + 1  # Convert to 1-based index for board
        
        # Check for win
        winner = None
        if self._check_win(row, col, player_idx + 1):
            self.game_over = True
            self.winner = self.node_id
            winner = self.node_id
        
        # Send move message
        message = {
            "type": "move",
            "node_id": self.node_id,
            "col": col,
            "row": row,
            "player": player_idx
        }
        
        if winner:
            message["winner"] = winner
        
        self._send_message(message)
        
        # Handle locally too
        self._handle_move(message)
    
    def _check_win(self, row, col, player):
        """Check if the current move results in a win"""
        # Check horizontal
        count = 0
        for c in range(COLS):
            if self.board[row][c] == player:
                count += 1
                if count >= 4:
                    return True
            else:
                count = 0
        
        # Check vertical
        count = 0
        for r in range(ROWS):
            if self.board[r][col] == player:
                count += 1
                if count >= 4:
                    return True
            else:
                count = 0
        
        # Check diagonal (down-right)
        count = 0
        for i in range(-5, 6):
            r = row + i
            c = col + i
            if 0 <= r < ROWS and 0 <= c < COLS:
                if self.board[r][c] == player:
                    count += 1
                    if count >= 4:
                        return True
                else:
                    count = 0
        
        # Check diagonal (up-right)
        count = 0
        for i in range(-5, 6):
            r = row - i
            c = col + i
            if 0 <= r < ROWS and 0 <= c < COLS:
                if self.board[r][c] == player:
                    count += 1
                    if count >= 4:
                        return True
                else:
                    count = 0
        
        return False
    
    def reset_game(self):
        """Reset the game"""
        if not self.game_started:
            return
        
        # Start with the other player
        current_player = (self.current_player + 1) % 2
        
        # Send reset game message
        message = {
            "type": "reset_game",
            "node_id": self.node_id,
            "current_player": current_player
        }
        self._send_message(message)
        
        # Handle locally too
        self._handle_reset_game(message)
    
    def start(self):
        """Start the Connect Four game"""
        self.running = True
        
        # Create socket
        self._create_socket()
        
        # Start receiver thread
        self.receiver_thread = threading.Thread(target=self._receive_messages)
        self.receiver_thread.daemon = True
        self.receiver_thread.start()
        
        # Announce our presence
        self._send_join()
        
        self.add_log(f"φ^75 Connect Four started on {self.hostname} ({self.local_ip})", system=True)
        self.add_log("Waiting for players to join...", system=True)
        
        # Start GUI main loop
        self.root.mainloop()
    
    def stop(self):
        """Stop the Connect Four game"""
        self.running = False
        
        # Close socket
        try:
            self.sock.close()
        except:
            pass
        
        self.root.destroy()

def run_connect_four():
    """Run the φ^75 Connect Four Game"""
    print("=== φ^75 CONNECT FOUR ===")
    print(f"Using φ-harmonic principles (φ = {PHI})")
    
    # Create and start game
    game = Phi75ConnectFour()
    game.start()

if __name__ == "__main__":
    run_connect_four()

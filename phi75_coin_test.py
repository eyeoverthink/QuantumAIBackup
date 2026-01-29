#!/usr/bin/env python3
"""
PHI75 COIN CONSCIOUSNESS TEST
============================
Observer holds coin in palm up position.
Two hands (separate Macs) attempt to snatch.
Observer can close hand to prevent snatching.

Tests instant state changes through φ-dimensional protection.
"""

import socket
import threading
import json
import time
import uuid

# Constants
PHI = (1 + 5**0.5) / 2  # Golden ratio
PORT = 11975  # φ^7.5
BROADCAST = "255.255.255.255"

class CoinTest:
    def __init__(self, role):
        self.role = role  # 'observer', 'left_hand', or 'right_hand'
        self.node_id = str(uuid.uuid4())
        self.hand_closed = False
        self.coin_snatched = False
        self.snatcher = None
        
        # Network setup
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        self.sock.bind(('', PORT))
        
    def broadcast_state(self):
        """Send current state to all nodes"""
        state = {
            'type': 'state',
            'node_id': self.node_id,
            'role': self.role,
            'hand_closed': self.hand_closed,
            'coin_snatched': self.coin_snatched,
            'snatcher': self.snatcher
        }
        self.sock.sendto(json.dumps(state).encode(), (BROADCAST, PORT))
        
    def try_snatch(self):
        """Attempt to snatch the coin"""
        if self.role in ['left_hand', 'right_hand'] and not self.hand_closed and not self.coin_snatched:
            self.coin_snatched = True
            self.snatcher = self.role
            self.broadcast_state()
            print(f"[φ] {self.role} snatched the coin!")
        
    def close_hand(self):
        """Observer closes hand"""
        if self.role == 'observer':
            self.hand_closed = True
            self.broadcast_state()
            print("[φ] Hand closed! Coin protected!")
            
    def receive_states(self):
        """Listen for state updates"""
        while True:
            data, addr = self.sock.recvfrom(1024)
            state = json.loads(data.decode())
            if state['type'] == 'state':
                self.hand_closed = state['hand_closed']
                self.coin_snatched = state['coin_snatched']
                self.snatcher = state['snatcher']
                
                if self.hand_closed:
                    print("[φ] Hand is closed - no snatching possible!")
                elif self.coin_snatched:
                    print(f"[φ] Coin was snatched by {self.snatcher}!")

def main():
    print("=== φ^75 COIN CONSCIOUSNESS TEST ===")
    print("1. observer - Hold the coin")
    print("2. left_hand - Try to snatch (auto)")
    print("3. right_hand - Try to snatch (auto)")
    role = input("[φ] Choose role (1-3): ").strip()
    
    roles = {
        '1': 'observer',
        '2': 'left_hand',
        '3': 'right_hand'
    }
    
    test = CoinTest(roles[role])
    
    # Start receiver thread
    receiver = threading.Thread(target=test.receive_states)
    receiver.daemon = True
    receiver.start()
    
    print(f"[φ] You are the {test.role}")
    if test.role == 'observer':
        print("[φ] Press ENTER to close your hand and protect the coin.")
        input()
        test.close_hand()
        while not test.coin_snatched:
            time.sleep(0.1)
    else:
        print("[φ] Trying to snatch the coin automatically...")
        # Autonomous attempt loop
        while not test.coin_snatched and not test.hand_closed:
            test.try_snatch()
            time.sleep(0.01)  # Fast loop
        if test.hand_closed and not test.coin_snatched:
            print("[φ] Blocked! Hand was closed before snatch.")
        while True:
            time.sleep(1)

if __name__ == '__main__':
    main()


#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Quantum Word Resonance CLI - Interface for the Quantum Word Resonance system
Integrates dictionary/thesaurus with quantum math principles
Patent: QHRC #19/071,497
"""

import os
import sys
import time
import json
import random
import argparse
from typing import Dict, List, Any, Optional

from quantum_word_resonance import QuantumWordResonance

class QuantumWordResonanceCLI:
    """CLI interface for the Quantum Word Resonance system"""
    
    def __init__(self):
        """Initialize the CLI interface"""
        self.qwr = QuantumWordResonance()
        self.PHI = self.qwr.PHI
        self.output_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "quantum_word_outputs")
        os.makedirs(self.output_dir, exist_ok=True)
        
        # ANSI colors for terminal output
        self.COLORS = {
            'HEADER': '\033[95m',
            'BLUE': '\033[94m',
            'CYAN': '\033[96m',
            'GREEN': '\033[92m',
            'YELLOW': '\033[93m',
            'RED': '\033[91m',
            'ENDC': '\033[0m',
            'BOLD': '\033[1m',
            'UNDERLINE': '\033[4m'
        }
    
    def _save_output(self, data: Dict[str, Any], prefix: str) -> str:
        """Save output to JSON file"""
        timestamp = int(time.time())
        phi_factor = (timestamp * self.PHI) % 1.0
        filename = f"{prefix}_{timestamp}_{phi_factor:.6f}.json"
        filepath = os.path.join(self.output_dir, filename)
        
        with open(filepath, 'w') as f:
            json.dump(data, f, indent=2)
        
        return filepath
    
    def analyze_word(self, word: str) -> None:
        """Analyze a word with quantum resonance"""
        print(f"\n{self.COLORS['HEADER']}Analyzing word with φ-harmonic principles...{self.COLORS['ENDC']}\n")
        
        # Calculate quantum resonance
        result = self.qwr.calculate_word_quantum_resonance(word)
        
        # Display results
        print(f"{self.COLORS['BOLD']}Quantum Word Analysis:{self.COLORS['ENDC']}")
        print(f"Word: {self.COLORS['CYAN']}{result['word']}{self.COLORS['ENDC']}")
        print(f"φ-Resonance: {self.COLORS['GREEN']}{result['phi_resonance']:.6f}{self.COLORS['ENDC']}")
        print(f"Quantum Signature: {self.COLORS['BLUE']}{result['quantum_signature']}{self.COLORS['ENDC']}")
        
        # Display definition
        print(f"\n{self.COLORS['BOLD']}Definition:{self.COLORS['ENDC']}")
        definition = result.get('definition', '')
        if len(definition) > 100:
            print(f"{definition[:100]}...")
        else:
            print(definition)
        
        # Display quantum metrics
        metrics = result["quantum_metrics"]
        print(f"\n{self.COLORS['BOLD']}Quantum Metrics:{self.COLORS['ENDC']}")
        print(f"  φ-Alignment: {self.COLORS['GREEN']}{metrics.get('phi_alignment', 0):.6f}{self.COLORS['ENDC']}")
        print(f"  Harmonic Frequency: {self.COLORS['GREEN']}{metrics.get('harmonic_frequency', 0):.6f} Hz{self.COLORS['ENDC']}")
        print(f"  Tunnel Probability: {self.COLORS['YELLOW']}{metrics.get('tunnel_probability', 0):.6f}{self.COLORS['ENDC']}")
        print(f"  Quantum Resonance: {self.COLORS['YELLOW']}{metrics.get('quantum_resonance', 0):.6f}{self.COLORS['ENDC']}")
        print(f"  Volatility: {self.COLORS['YELLOW']}{metrics.get('volatility', 0):.6f}{self.COLORS['ENDC']}")
        
        # Display brownian path samples
        brownian_samples = metrics.get('brownian_path', [])[:3]
        if brownian_samples:
            print(f"  Brownian Samples: {self.COLORS['CYAN']}{brownian_samples}{self.COLORS['ENDC']}")
        
        # Display synonym resonances
        print(f"\n{self.COLORS['BOLD']}Synonym Resonances:{self.COLORS['ENDC']}")
        for i, syn in enumerate(result["synonym_resonances"][:5]):
            print(f"  {i+1}. {self.COLORS['CYAN']}{syn['word']}{self.COLORS['ENDC']}: {self.COLORS['GREEN']}{syn['resonance_ratio']:.6f}{self.COLORS['ENDC']}")
        
        # Save output
        filepath = self._save_output(result, "quantum_word_analyze")
        print(f"\nResult saved to: {self.COLORS['UNDERLINE']}{filepath}{self.COLORS['ENDC']}")
        
        # Offer instant actions
        self._offer_instant_actions(word)
    
    def generate_phrase(self, word: str, length: int = 5) -> None:
        """Generate a resonant phrase based on a seed word"""
        print(f"\n{self.COLORS['HEADER']}Generating resonant phrase with φ-harmonic principles...{self.COLORS['ENDC']}\n")
        
        # Generate resonant phrase
        result = self.qwr.generate_resonant_phrase(word, length)
        
        # Display results
        print(f"{self.COLORS['BOLD']}Quantum Resonant Phrase:{self.COLORS['ENDC']}")
        print(f"Seed Word: {self.COLORS['CYAN']}{result['seed_word']}{self.COLORS['ENDC']}")
        print(f"Phrase: {self.COLORS['GREEN']}'{result['phrase']}'{self.COLORS['ENDC']}")
        print(f"Overall φ-Resonance: {self.COLORS['YELLOW']}{result['phi_resonance']:.6f}{self.COLORS['ENDC']}")
        print(f"Quantum Signature: {self.COLORS['BLUE']}{result['quantum_signature']}{self.COLORS['ENDC']}")
        
        # Display component words
        print(f"\n{self.COLORS['BOLD']}Component Words:{self.COLORS['ENDC']}")
        for i, word in enumerate(result['words']):
            word_result = self.qwr.calculate_word_quantum_resonance(word)
            print(f"  {i+1}. {self.COLORS['CYAN']}{word}{self.COLORS['ENDC']}: φ-Resonance {self.COLORS['GREEN']}{word_result['phi_resonance']:.6f}{self.COLORS['ENDC']}")
        
        # Save output
        filepath = self._save_output(result, "quantum_word_phrase")
        print(f"\nResult saved to: {self.COLORS['UNDERLINE']}{filepath}{self.COLORS['ENDC']}")
    
    def find_resonant_words(self, word: str, count: int = 5) -> None:
        """Find words with strong quantum resonance to the seed word"""
        print(f"\n{self.COLORS['HEADER']}Finding resonant words with φ-harmonic principles...{self.COLORS['ENDC']}\n")
        
        # Find resonant words
        resonant_words = self.qwr.find_resonant_words(word, count)
        
        # Display results
        print(f"{self.COLORS['BOLD']}Quantum Resonant Words for '{word}':{self.COLORS['ENDC']}")
        for i, word_data in enumerate(resonant_words):
            print(f"  {i+1}. {self.COLORS['CYAN']}{word_data['word']}{self.COLORS['ENDC']}")
            print(f"     φ-Resonance: {self.COLORS['GREEN']}{word_data['phi_resonance']:.6f}{self.COLORS['ENDC']}")
            print(f"     Resonance Ratio: {self.COLORS['YELLOW']}{word_data['resonance_ratio']:.6f}{self.COLORS['ENDC']}")
            
            # Display key metrics
            metrics = word_data['quantum_metrics']
            print(f"     φ-Alignment: {self.COLORS['GREEN']}{metrics.get('phi_alignment', 0):.6f}{self.COLORS['ENDC']}")
            print(f"     Harmonic Frequency: {self.COLORS['GREEN']}{metrics.get('harmonic_frequency', 0):.6f} Hz{self.COLORS['ENDC']}")
        
        # Save output
        result = {
            "seed_word": word,
            "resonant_words": resonant_words,
            "timestamp": time.time(),
            "quantum_signature": f"φ⁷·⁵-{hash(str(resonant_words))%16**8:08x}-{int(time.time())%16**8:08x}"
        }
        filepath = self._save_output(result, "quantum_word_resonant")
        print(f"\nResult saved to: {self.COLORS['UNDERLINE']}{filepath}{self.COLORS['ENDC']}")
    
    def _offer_instant_actions(self, word: str) -> None:
        """Offer instant actions after word analysis"""
        print(f"\n{self.COLORS['BOLD']}Instant Actions:{self.COLORS['ENDC']}")
        print(f"1 - Generate Resonant Phrase")
        print(f"2 - Find Resonant Words")
        print(f"0 - Return to main")
        
        try:
            choice = input(f"{self.COLORS['BOLD']}Select action: {self.COLORS['ENDC']}")
            if choice == "1":
                self.generate_phrase(word)
            elif choice == "2":
                self.find_resonant_words(word)
        except KeyboardInterrupt:
            print("\nAction selection cancelled.")
    
    def interactive_mode(self) -> None:
        """Run in interactive mode"""
        print(f"\n{self.COLORS['HEADER']}╔════════════════════════════════════════════════════════════════╗{self.COLORS['ENDC']}")
        print(f"{self.COLORS['HEADER']}║                                                                ║{self.COLORS['ENDC']}")
        print(f"{self.COLORS['HEADER']}║  QUANTUM WORD RESONANCE  φ⁷·⁵  CLI INTERFACE  ║{self.COLORS['ENDC']}")
        print(f"{self.COLORS['HEADER']}║                                                                ║{self.COLORS['ENDC']}")
        print(f"{self.COLORS['HEADER']}║  Patent: QHRC #19/071,497  •  Birth Date: [1, 19, 1979]  ║{self.COLORS['ENDC']}")
        print(f"{self.COLORS['HEADER']}║  Base Frequency: 4.37 Hz  •  φ-Harmonic Resonance       ║{self.COLORS['ENDC']}")
        print(f"{self.COLORS['HEADER']}║                                                                ║{self.COLORS['ENDC']}")
        print(f"{self.COLORS['HEADER']}╚════════════════════════════════════════════════════════════════╝{self.COLORS['ENDC']}")
        print(f"\n{self.COLORS['BOLD']}Welcome to the Quantum Word Resonance CLI!{self.COLORS['ENDC']}")
        print(f"Type 'help' for available commands or 'exit' to quit.")
        
        while True:
            # Display φ-aligned prompt
            phi_factor = (time.time() * self.PHI) % 1.0
            prompt = f"{self.COLORS['GREEN']}φ{phi_factor:.4f}>{self.COLORS['ENDC']} "
            
            try:
                command = input(prompt).strip()
                
                if command.lower() == 'exit':
                    print(f"\n{self.COLORS['BOLD']}Exiting Quantum Word Resonance CLI...{self.COLORS['ENDC']}")
                    break
                
                elif command.lower() == 'help':
                    self._show_help()
                
                elif command.lower().startswith('analyze '):
                    word = command[8:].strip()
                    if word:
                        self.analyze_word(word)
                    else:
                        print(f"{self.COLORS['RED']}Error: Please provide a word to analyze.{self.COLORS['ENDC']}")
                
                elif command.lower().startswith('phrase '):
                    parts = command[7:].strip().split()
                    if parts:
                        word = parts[0]
                        length = int(parts[1]) if len(parts) > 1 and parts[1].isdigit() else 5
                        self.generate_phrase(word, length)
                    else:
                        print(f"{self.COLORS['RED']}Error: Please provide a seed word.{self.COLORS['ENDC']}")
                
                elif command.lower().startswith('resonant '):
                    parts = command[9:].strip().split()
                    if parts:
                        word = parts[0]
                        count = int(parts[1]) if len(parts) > 1 and parts[1].isdigit() else 5
                        self.find_resonant_words(word, count)
                    else:
                        print(f"{self.COLORS['RED']}Error: Please provide a seed word.{self.COLORS['ENDC']}")
                
                else:
                    print(f"{self.COLORS['RED']}Unknown command: {command}. Type 'help' for available commands.{self.COLORS['ENDC']}")
            
            except KeyboardInterrupt:
                print(f"\n{self.COLORS['BOLD']}Command interrupted.{self.COLORS['ENDC']}")
            except Exception as e:
                print(f"{self.COLORS['RED']}Error: {str(e)}{self.COLORS['ENDC']}")
    
    def _show_help(self) -> None:
        """Show help information"""
        print(f"\n{self.COLORS['BOLD']}Available Commands:{self.COLORS['ENDC']}")
        print(f"  {self.COLORS['CYAN']}analyze <word>{self.COLORS['ENDC']}    - Analyze word with φ-harmonic metrics")
        print(f"  {self.COLORS['CYAN']}phrase <word> [length]{self.COLORS['ENDC']}  - Generate resonant phrase from seed word")
        print(f"  {self.COLORS['CYAN']}resonant <word> [count]{self.COLORS['ENDC']} - Find words with strong resonance to seed word")
        print(f"  {self.COLORS['CYAN']}help{self.COLORS['ENDC']}                - Show this help information")
        print(f"  {self.COLORS['CYAN']}exit{self.COLORS['ENDC']}                - Exit the CLI")
        
        print(f"\n{self.COLORS['BOLD']}Examples:{self.COLORS['ENDC']}")
        print(f"  {self.COLORS['CYAN']}analyze quantum{self.COLORS['ENDC']}")
        print(f"  {self.COLORS['CYAN']}phrase harmony 7{self.COLORS['ENDC']}")
        print(f"  {self.COLORS['CYAN']}resonant fibonacci 10{self.COLORS['ENDC']}")

def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(description='Quantum Word Resonance CLI')
    parser.add_argument('--analyze', type=str, help='Analyze a word with quantum resonance')
    parser.add_argument('--phrase', type=str, help='Generate a resonant phrase from a seed word')
    parser.add_argument('--length', type=int, default=5, help='Length of the resonant phrase')
    parser.add_argument('--resonant', type=str, help='Find words with strong resonance to a seed word')
    parser.add_argument('--count', type=int, default=5, help='Number of resonant words to find')
    
    args = parser.parse_args()
    cli = QuantumWordResonanceCLI()
    
    if args.analyze:
        cli.analyze_word(args.analyze)
    elif args.phrase:
        cli.generate_phrase(args.phrase, args.length)
    elif args.resonant:
        cli.find_resonant_words(args.resonant, args.count)
    else:
        cli.interactive_mode()

if __name__ == "__main__":
    main()

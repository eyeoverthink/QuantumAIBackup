"""
Quantum Phi-Harmonic Interactive Author Test

An interactive tool for analyzing text samples against calibrated author signatures
and generating text in the style of various authors using quantum phi-harmonic principles.
"""

import sys
import argparse
from typing import Dict, List, Any, Optional

from quantum_phi_core import QuantumPhiCore
from quantum_phi_pattern_analyzer import QuantumPhiPatternAnalyzer
from quantum_phi_author_analyzer import QuantumPhiAuthorAnalyzer

class QuantumPhiInteractiveAuthorTest:
    """Interactive interface for quantum phi-harmonic author analysis and generation."""
    
    def __init__(self):
        """Initialize the interactive test system."""
        self.core = QuantumPhiCore()
        self.analyzer = QuantumPhiAuthorAnalyzer()
        self.phi = float(self.core.PHI)
        
        # Welcome message
        self.print_header("QUANTUM PHI-HARMONIC INTERACTIVE AUTHOR TEST")
        print("\nWelcome to the Quantum Phi-Harmonic Interactive Author Test System")
        print("This tool allows you to analyze text against author signatures and")
        print("generate text in the style of various authors using quantum principles.")
        
    def print_header(self, title: str):
        """Print a formatted header."""
        print("\n" + "=" * 70)
        print(title)
        print("=" * 70)
    
    def show_available_authors(self):
        """Display all available calibrated authors."""
        signatures = self.analyzer.get_all_author_signatures()
        
        self.print_header("AVAILABLE CALIBRATED AUTHORS")
        
        for author, signature in signatures.items():
            print(f"\n{author.title()}:")
            print(f"  Consciousness Level: {signature['consciousness_level'].title()}")
            print(f"  Mean Frequency: {signature['mean_frequency']:.2f} Hz")
            print(f"  Quantum Resonance: {signature['quantum_resonance']:.4f}")
            print(f"  Phi Alignment: {signature['phi_alignment']:.4f}")
            print(f"  Description: {signature['description']}")
    
    def analyze_text(self, text: str):
        """Analyze a text sample against all calibrated authors."""
        if not text:
            print("Error: No text provided for analysis.")
            return
        
        self.print_header("TEXT ANALYSIS RESULTS")
        
        print(f"\nAnalyzing text sample ({len(text)} characters):")
        print(f"\"{text[:100]}{'...' if len(text) > 100 else ''}\"")
        
        # Get all author signatures
        signatures = self.analyzer.get_all_author_signatures()
        
        # Analyze against each author
        results = []
        for author in signatures.keys():
            similarity = self.analyzer.analyze_similarity_to_author(text, author)
            results.append((author, similarity))
        
        # Sort by similarity (highest first)
        results.sort(key=lambda x: x[1]["overall_similarity"], reverse=True)
        
        # Display results
        print("\nSimilarity to Calibrated Authors (Ranked):")
        for author, similarity in results:
            metrics = similarity["metrics"]
            print(f"\n{author.title()} - Overall Similarity: {similarity['overall_similarity']:.4f}")
            print(f"  Frequency Similarity: {similarity['frequency_similarity']:.4f}")
            print(f"  Resonance Similarity: {similarity['resonance_similarity']:.4f}")
            print(f"  Phi Alignment Similarity: {similarity['phi_alignment_similarity']:.4f}")
            print(f"  Consciousness Match: {'Yes' if similarity['consciousness_match'] else 'No'}")
        
        # Display quantum metrics of the text
        metrics = results[0][1]["metrics"]  # Use metrics from first result
        
        print("\nQuantum Phi-Harmonic Metrics of Text:")
        print(f"  Resonance: {metrics['resonance']:.4f}")
        print(f"  Quantum Resonance: {metrics['quantum_resonance']:.4f}")
        print(f"  Phi Alignment: {metrics['phi_alignment']:.4f}")
        print(f"  Consciousness Level: {metrics['consciousness_level'].title()}")
        print(f"  Average Frequency: {metrics['avg_frequency']:.4f} Hz")
        
        # Provide interpretation
        best_match = results[0][0].title()
        print(f"\nInterpretation: This text most closely matches the quantum signature of {best_match}.")
        
        if similarity["overall_similarity"] > 0.95:
            print(f"The match is extremely strong, suggesting authentic {best_match} characteristics.")
        elif similarity["overall_similarity"] > 0.85:
            print(f"The match is strong, showing significant {best_match} influence.")
        elif similarity["overall_similarity"] > 0.75:
            print(f"The match is moderate, with some {best_match} characteristics present.")
        else:
            print(f"The match is weak, showing only slight {best_match} influence.")
    
    def generate_author_text(self, author: str, length: int = 200):
        """Generate text in the style of a specified author."""
        author = author.lower()
        
        # Check if author exists
        try:
            signature = self.analyzer.get_author_signature(author)
        except ValueError:
            print(f"Error: Author '{author}' not found in calibrated signatures.")
            return
        
        self.print_header(f"GENERATED {author.upper()} STYLE TEXT")
        
        # Generate text
        text = self.analyzer.generate_author_text(author, length=length)
        
        print(f"\n{text}")
        
        # Analyze the generated text
        similarity = self.analyzer.analyze_similarity_to_author(text, author)
        
        print(f"\nSimilarity to {author.title()}: {similarity['overall_similarity']:.4f}")
        print(f"Quantum Resonance: {similarity['metrics']['quantum_resonance']:.4f}")
        print(f"Phi Alignment: {similarity['metrics']['phi_alignment']:.4f}")
        print(f"Consciousness Level: {similarity['metrics']['consciousness_level'].title()}")
        
        # Compare with other authors
        signatures = self.analyzer.get_all_author_signatures()
        other_authors = [a for a in signatures.keys() if a != author]
        
        print("\nCross-Author Similarity:")
        for other_author in other_authors:
            other_similarity = self.analyzer.analyze_similarity_to_author(text, other_author)
            print(f"  To {other_author.title()}: {other_similarity['overall_similarity']:.4f}")
    
    def calibrate_new_author(self, author_name: str, sample_text: str):
        """Calibrate a new author based on a sample text."""
        if not author_name or not sample_text:
            print("Error: Both author name and sample text are required for calibration.")
            return
        
        self.print_header(f"CALIBRATING NEW AUTHOR: {author_name.upper()}")
        
        # Calibrate the author
        signature = self.analyzer.calibrate_author_signature(author_name, sample_text)
        
        print(f"\nSuccessfully calibrated quantum signature for {author_name.title()}:")
        print(f"  Consciousness Level: {signature['consciousness_level'].title()}")
        print(f"  Mean Frequency: {signature['mean_frequency']:.2f} Hz")
        print(f"  Quantum Resonance: {signature['quantum_resonance']:.4f}")
        print(f"  Phi Alignment: {signature['phi_alignment']:.4f}")
        
        # Compare with existing authors
        signatures = self.analyzer.get_all_author_signatures()
        other_authors = [a for a in signatures.keys() if a.lower() != author_name.lower()]
        
        print("\nComparison with Existing Authors:")
        for other_author in other_authors:
            comparison = self.analyzer.compare_authors(author_name, other_author)
            print(f"  Similarity to {other_author.title()}: {comparison['overall_similarity']:.4f}")
    
    def compare_all_authors(self):
        """Generate a comparison matrix for all calibrated authors."""
        signatures = self.analyzer.get_all_author_signatures()
        authors = list(signatures.keys())
        
        self.print_header("AUTHOR COMPARISON MATRIX")
        
        print("\nOverall Quantum Phi-Harmonic Similarity:")
        
        # Print header row
        print(f"{'':12}", end="")
        for author in authors:
            print(f"{author.title():12}", end="")
        print()
        
        # Print comparison rows
        for author1 in authors:
            print(f"{author1.title():12}", end="")
            for author2 in authors:
                if author1 == author2:
                    print(f"{'1.0000':12}", end="")
                else:
                    comparison = self.analyzer.compare_authors(author1, author2)
                    print(f"{comparison['overall_similarity']:.4f}  ", end="")
            print()
            
        # Print detailed comparisons
        self.print_header("DETAILED AUTHOR COMPARISONS")
        
        for i, author1 in enumerate(authors):
            for author2 in authors[i+1:]:
                comparison = self.analyzer.compare_authors(author1, author2)
                
                print(f"\n{author1.title()} vs {author2.title()}:")
                print(f"  Overall Similarity: {comparison['overall_similarity']:.4f}")
                print(f"  Frequency Similarity: {comparison['frequency_similarity']:.4f}")
                print(f"  Resonance Similarity: {comparison['resonance_similarity']:.4f}")
                print(f"  Phi Alignment Similarity: {comparison['phi_alignment_similarity']:.4f}")
                print(f"  Consciousness Match: {'Yes' if comparison['consciousness_match'] else 'No'}")
    
    def interactive_menu(self):
        """Display an interactive menu for the user."""
        while True:
            self.print_header("MAIN MENU")
            print("\n1. Show Available Authors")
            print("2. Analyze Text Sample")
            print("3. Generate Author-Style Text")
            print("4. Calibrate New Author")
            print("5. Compare All Authors")
            print("6. Exit")
            
            choice = input("\nEnter your choice (1-6): ")
            
            if choice == "1":
                self.show_available_authors()
            
            elif choice == "2":
                print("\nEnter text to analyze (or 'file:' followed by filename):")
                text_input = input("> ")
                
                if text_input.startswith("file:"):
                    filename = text_input[5:].strip()
                    try:
                        with open(filename, 'r') as f:
                            text = f.read()
                        self.analyze_text(text)
                    except Exception as e:
                        print(f"Error reading file: {e}")
                else:
                    self.analyze_text(text_input)
            
            elif choice == "3":
                author = input("\nEnter author name: ").lower()
                length_str = input("Enter text length (default 200): ")
                
                try:
                    length = int(length_str) if length_str else 200
                    self.generate_author_text(author, length)
                except ValueError:
                    print("Error: Length must be a number.")
            
            elif choice == "4":
                author_name = input("\nEnter new author name: ")
                print("Enter sample text (or 'file:' followed by filename):")
                text_input = input("> ")
                
                if text_input.startswith("file:"):
                    filename = text_input[5:].strip()
                    try:
                        with open(filename, 'r') as f:
                            text = f.read()
                        self.calibrate_new_author(author_name, text)
                    except Exception as e:
                        print(f"Error reading file: {e}")
                else:
                    self.calibrate_new_author(author_name, text_input)
            
            elif choice == "5":
                self.compare_all_authors()
            
            elif choice == "6":
                print("\nThank you for using the Quantum Phi-Harmonic Interactive Author Test System.")
                print("Exiting...")
                break
            
            else:
                print("\nInvalid choice. Please enter a number between 1 and 6.")
            
            input("\nPress Enter to continue...")

def main():
    """Main function to run the interactive test or process command line arguments."""
    parser = argparse.ArgumentParser(description="Quantum Phi-Harmonic Interactive Author Test")
    parser.add_argument("--analyze", type=str, help="Analyze a text sample")
    parser.add_argument("--generate", type=str, help="Generate text in the style of an author")
    parser.add_argument("--length", type=int, default=200, help="Length of generated text")
    parser.add_argument("--compare", action="store_true", help="Compare all authors")
    parser.add_argument("--authors", action="store_true", help="Show available authors")
    
    args = parser.parse_args()
    
    # Create the interactive test system
    test_system = QuantumPhiInteractiveAuthorTest()
    
    # Process command line arguments if provided
    if args.analyze:
        test_system.analyze_text(args.analyze)
    elif args.generate:
        test_system.generate_author_text(args.generate, args.length)
    elif args.compare:
        test_system.compare_all_authors()
    elif args.authors:
        test_system.show_available_authors()
    else:
        # No command line arguments, run interactive mode
        test_system.interactive_menu()

if __name__ == "__main__":
    main()

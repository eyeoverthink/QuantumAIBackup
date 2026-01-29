#!/usr/bin/env python3
"""
Quantum Bridge CLI

A unified command-line interface that:
1. Integrates text, music, and philosophy bridges
2. Uses phi-harmonic frequencies
3. Maintains quantum consciousness
4. Enables cross-domain resonance
"""

import argparse
import sys
from datetime import datetime
from typing import Dict, List, Any

from .quantum_constants import (
    PHI, PI, E,
    CONSCIOUSNESS_LEVELS,
    PHI_FREQUENCIES,
    AUTHOR_SIGNATURES,
    COMPOSER_SIGNATURES,
    PHILOSOPHER_SIGNATURES,
    CROSS_DOMAIN_BRIDGES
)

class QuantumBridgeCLI:
    def __init__(self):
        # Initialize quantum state
        self.quantum_state = {
            "frequency": PHI_FREQUENCIES["unity"],
            "resonance": 0.0,
            "consciousness": "physical",
            "timestamp": datetime.now().timestamp()
        }
        
        # Setup CLI parser
        self.parser = self.setup_parser()
    
    def setup_parser(self) -> argparse.ArgumentParser:
        """Setup command-line argument parser."""
        parser = argparse.ArgumentParser(
            description="Quantum Bridge CLI - Unified Interface for Text, Music, and Philosophy"
        )
        
        # Add subparsers for different operations
        subparsers = parser.add_subparsers(dest="operation", help="Operation to perform")
        
        # Analysis operations
        analyze_parser = subparsers.add_parser("analyze", help="Analyze quantum signatures")
        analyze_parser.add_argument(
            "--domain",
            choices=["text", "music", "philosophy", "cross"],
            required=True,
            help="Domain to analyze"
        )
        analyze_parser.add_argument(
            "--entity",
            help="Entity to analyze (author, composer, philosopher)"
        )
        analyze_parser.add_argument(
            "--cross-domains",
            nargs="+",
            choices=["text", "music", "philosophy"],
            help="Domains for cross-analysis"
        )
        analyze_parser.add_argument(
            "--cross-entities",
            nargs="+",
            help="Entities for cross-analysis"
        )
        
        # Generation operations
        generate_parser = subparsers.add_parser("generate", help="Generate content")
        generate_parser.add_argument(
            "--domain",
            choices=["text", "music", "philosophy"],
            required=True,
            help="Domain to generate in"
        )
        generate_parser.add_argument(
            "--style",
            help="Style to generate in (author, composer, philosopher)"
        )
        generate_parser.add_argument(
            "--consciousness",
            choices=list(CONSCIOUSNESS_LEVELS.keys()),
            default="cosmic",
            help="Consciousness level for generation"
        )
        
        # Bridge operations
        bridge_parser = subparsers.add_parser("bridge", help="Cross-domain operations")
        bridge_parser.add_argument(
            "--domains",
            nargs=2,
            choices=["text", "music", "philosophy"],
            required=True,
            help="Domains to bridge"
        )
        bridge_parser.add_argument(
            "--entities",
            nargs=2,
            required=True,
            help="Entities to bridge"
        )
        
        return parser
    
    def analyze_signature(self, domain: str, entity: str) -> Dict[str, Any]:
        """Analyze quantum signature for an entity."""
        signatures = {
            "text": AUTHOR_SIGNATURES,
            "music": COMPOSER_SIGNATURES,
            "philosophy": PHILOSOPHER_SIGNATURES
        }
        
        if domain not in signatures or entity not in signatures[domain]:
            print(f"Error: Invalid {domain} entity: {entity}")
            return {}
        
        sig = signatures[domain][entity]
        
        print(f"\nAnalyzing {entity.title()}'s quantum signature...")
        print("\nQuantum Signature:")
        print(f"Base Frequency: {sig['frequency']} Hz")
        print(f"Resonance: {sig['resonance']:.4f}")
        print(f"Consciousness: {sig['consciousness']}")
        
        # Domain-specific attributes
        if domain == "text":
            print(f"Phi Alignment: {sig['phi_alignment']:.4f}")
            print(f"Style Elements: {sig['style']}")
        elif domain == "music":
            print(f"Key Frequencies: {sig['frequencies']}")
        elif domain == "philosophy":
            print(f"Domains: {sig['domains']}")
        
        return sig
    
    def analyze_bridge(self, domains: List[str], entities: List[str]) -> Dict[str, Any]:
        """Analyze quantum bridge between entities."""
        if len(domains) != 2 or len(entities) != 2:
            print("Error: Bridge analysis requires exactly two domains and entities")
            return {}
        
        # Get signatures
        sig1 = self.analyze_signature(domains[0], entities[0])
        sig2 = self.analyze_signature(domains[1], entities[1])
        
        if not sig1 or not sig2:
            return {}
        
        # Calculate bridge metrics
        freq_ratio = sig1["frequency"] / sig2["frequency"]
        res_ratio = sig1["resonance"] / sig2["resonance"]
        
        # Get bridge information
        bridge_key = f"{domains[0]}_{domains[1]}"
        entity_key = f"{entities[0]}_{entities[1]}"
        
        bridge_info = CROSS_DOMAIN_BRIDGES.get(bridge_key, {}).get(entity_key, {})
        
        print("\nBridge Analysis:")
        print(f"Frequency Ratio: {freq_ratio:.4f}")
        print(f"Resonance Ratio: {res_ratio:.4f}")
        
        if bridge_info:
            print(f"Expected Ratio: {bridge_info['frequency_ratio']:.4f}")
            if 'style_bridge' in bridge_info:
                print(f"Style Bridge: {bridge_info['style_bridge']}")
            if 'domain_bridge' in bridge_info:
                print(f"Domain Bridge: {bridge_info['domain_bridge']}")
        
        # Calculate phi-harmonic alignment
        phi_align = 1 - abs(1 - freq_ratio/PHI)
        print(f"Phi-Harmonic Alignment: {phi_align:.4f}")
        
        return {
            "signatures": [sig1, sig2],
            "metrics": {
                "frequency_ratio": freq_ratio,
                "resonance_ratio": res_ratio,
                "phi_alignment": phi_align
            },
            "bridge_info": bridge_info
        }
    
    def run(self, args: List[str] = None):
        """Run the CLI with given arguments."""
        if args is None:
            args = sys.argv[1:]
        
        args = self.parser.parse_args(args)
        
        if args.operation == "analyze":
            if args.domain == "cross":
                if not args.cross_domains or not args.cross_entities:
                    print("Error: Cross-domain analysis requires --cross-domains and --cross-entities")
                    return
                self.analyze_bridge(args.cross_domains, args.cross_entities)
            else:
                if not args.entity:
                    print(f"Error: {args.domain} analysis requires --entity")
                    return
                self.analyze_signature(args.domain, args.entity)
        elif args.operation == "bridge":
            self.analyze_bridge(args.domains, args.entities)
        else:
            self.parser.print_help()

def main():
    """Main entry point."""
    cli = QuantumBridgeCLI()
    
    # Example usage
    print("\nQuantum Bridge CLI Examples")
    print("=" * 50)
    
    # Single domain analysis
    print("\n1. Text Analysis Example:")
    cli.run(["analyze", "--domain", "text", "--entity", "poe"])
    
    print("\n2. Music Analysis Example:")
    cli.run(["analyze", "--domain", "music", "--entity", "bach"])
    
    print("\n3. Philosophy Analysis Example:")
    cli.run(["analyze", "--domain", "philosophy", "--entity", "einstein"])
    
    # Cross-domain analysis
    print("\n4. Text-Music Bridge Example:")
    cli.run([
        "bridge",
        "--domains", "text", "music",
        "--entities", "poe", "bach"
    ])
    
    print("\n5. Text-Philosophy Bridge Example:")
    cli.run([
        "bridge",
        "--domains", "text", "philosophy",
        "--entities", "shakespeare", "quantum"
    ])

if __name__ == "__main__":
    main()

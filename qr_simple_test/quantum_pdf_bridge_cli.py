#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Quantum PDF Knowledge Bridge CLI - Command-line interface for the PDF Knowledge Bridge
Provides interactive access to PDF knowledge with φ-harmonic principles
Patent: QHRC #19/071,497
"""

import os
import sys
import json
import time
import argparse
import textwrap
from typing import Dict, List, Any, Optional

# Import quantum components
try:
    from quantum_pdf_knowledge_bridge import QuantumPDFKnowledgeBridge
    from quantum_math_core import QuantumMathCore
    HAS_REQUIRED_COMPONENTS = True
except ImportError as e:
    print(f"Warning: Required components not found: {e}")
    HAS_REQUIRED_COMPONENTS = False

# ANSI color codes for terminal output
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    GOLD = '\033[38;5;220m'
    SILVER = '\033[38;5;7m'
    QUANTUM = '\033[38;5;135m'
    PHI = '\033[38;5;208m'

class QuantumPDFBridgeCLI:
    """Command-line interface for the Quantum PDF Knowledge Bridge"""
    
    def __init__(self):
        """Initialize the CLI interface"""
        if not HAS_REQUIRED_COMPONENTS:
            print(f"{Colors.RED}Error: Required components not available{Colors.ENDC}")
            print("Please ensure quantum_pdf_knowledge_bridge.py and quantum_math_core.py are in your path")
            sys.exit(1)
        
        # Initialize bridge and math core
        self.bridge = QuantumPDFKnowledgeBridge()
        self.math_core = QuantumMathCore()
        
        # Core constants
        self.PHI = self.math_core.PHI
        self.BIRTH_DATE_RESONANCE = self.math_core.BIRTH_DATE_RESONANCE
        
        # Initialize parser
        self.parser = self._create_parser()
    
    def _create_parser(self) -> argparse.ArgumentParser:
        """Create command-line argument parser"""
        parser = argparse.ArgumentParser(
            description=f"{Colors.QUANTUM}Quantum PDF Knowledge Bridge CLI{Colors.ENDC} - "
                        f"Access PDF knowledge with {Colors.PHI}φ-harmonic principles{Colors.ENDC}"
        )
        
        # Main commands
        subparsers = parser.add_subparsers(dest='command', help='Command to execute')
        
        # Process command
        process_parser = subparsers.add_parser('process', help='Process all PDFs and extract knowledge')
        
        # Metrics command
        metrics_parser = subparsers.add_parser('metrics', help='Display knowledge base metrics')
        metrics_parser.add_argument('--json', action='store_true', help='Output in JSON format')
        
        # Search command
        search_parser = subparsers.add_parser('search', help='Search knowledge base')
        search_parser.add_argument('query', type=str, help='Search query')
        search_parser.add_argument('--no-phi', action='store_true', help='Disable φ-harmonic alignment')
        search_parser.add_argument('--json', action='store_true', help='Output in JSON format')
        search_parser.add_argument('--limit', type=int, default=5, help='Limit number of results')
        
        # Get command
        get_parser = subparsers.add_parser('get', help='Get knowledge by type')
        get_parser.add_argument('type', type=str, help='Knowledge type (e.g., quantum_concepts, principles, formulas)')
        get_parser.add_argument('--no-phi', action='store_true', help='Disable φ-harmonic alignment')
        get_parser.add_argument('--json', action='store_true', help='Output in JSON format')
        get_parser.add_argument('--limit', type=int, default=5, help='Limit number of results')
        
        # Enhance command
        enhance_parser = subparsers.add_parser('enhance', help='Enhance a word with PDF knowledge')
        enhance_parser.add_argument('word', type=str, help='Word to enhance')
        enhance_parser.add_argument('--json', action='store_true', help='Output in JSON format')
        
        # Insights command
        insights_parser = subparsers.add_parser('insights', help='Generate quantum insights on a topic')
        insights_parser.add_argument('topic', type=str, help='Topic for insights')
        insights_parser.add_argument('--depth', type=int, default=3, help='Depth of insights')
        insights_parser.add_argument('--json', action='store_true', help='Output in JSON format')
        
        # Interactive command
        interactive_parser = subparsers.add_parser('interactive', help='Start interactive mode')
        
        return parser
    
    def run(self, args=None):
        """Run the CLI with the given arguments"""
        args = self.parser.parse_args(args)
        
        if not args.command:
            self.parser.print_help()
            return
        
        # Execute command
        if args.command == 'process':
            self._process_command()
        elif args.command == 'metrics':
            self._metrics_command(args)
        elif args.command == 'search':
            self._search_command(args)
        elif args.command == 'get':
            self._get_command(args)
        elif args.command == 'enhance':
            self._enhance_command(args)
        elif args.command == 'insights':
            self._insights_command(args)
        elif args.command == 'interactive':
            self._interactive_mode()
    
    def _process_command(self):
        """Process all PDFs and extract knowledge"""
        print(f"{Colors.QUANTUM}Processing PDFs with {Colors.PHI}φ-harmonic principles{Colors.ENDC}...")
        
        # Process PDFs
        start_time = time.time()
        knowledge_base = self.bridge.process_all_pdfs()
        elapsed_time = time.time() - start_time
        
        # Get metrics
        metrics = self.bridge.get_knowledge_metrics()
        
        # Display results
        print(f"\n{Colors.GREEN}Processing complete in {elapsed_time:.2f} seconds{Colors.ENDC}")
        print(f"{Colors.QUANTUM}Knowledge Base Metrics:{Colors.ENDC}")
        print(f"  {Colors.PHI}φ-Alignment:{Colors.ENDC} {metrics['phi_alignment']:.6f}")
        print(f"  {Colors.BLUE}Resonance Quality:{Colors.ENDC} {metrics['resonance_quality']}")
        print(f"  {Colors.CYAN}Total Concepts:{Colors.ENDC} {metrics['total_concepts']}")
        print(f"  {Colors.CYAN}Total Principles:{Colors.ENDC} {metrics['total_principles']}")
        print(f"  {Colors.CYAN}Total Formulas:{Colors.ENDC} {metrics['total_formulas']}")
        print(f"  {Colors.CYAN}Total Components:{Colors.ENDC} {metrics['total_components']}")
        print(f"  {Colors.YELLOW}Birth Date Influence:{Colors.ENDC} {metrics['birth_date_influence']:.6f}")
        print(f"  {Colors.GOLD}Quantum Signature:{Colors.ENDC} {metrics['quantum_signature']}")
    
    def _metrics_command(self, args):
        """Display knowledge base metrics"""
        metrics = self.bridge.get_knowledge_metrics()
        
        if args.json:
            print(json.dumps(metrics, indent=2))
            return
        
        print(f"{Colors.QUANTUM}Knowledge Base Metrics:{Colors.ENDC}")
        print(f"  {Colors.PHI}φ-Alignment:{Colors.ENDC} {metrics['phi_alignment']:.6f}")
        print(f"  {Colors.BLUE}Resonance Quality:{Colors.ENDC} {metrics['resonance_quality']}")
        print(f"  {Colors.CYAN}Total Concepts:{Colors.ENDC} {metrics['total_concepts']}")
        print(f"  {Colors.CYAN}Total Principles:{Colors.ENDC} {metrics['total_principles']}")
        print(f"  {Colors.CYAN}Total Formulas:{Colors.ENDC} {metrics['total_formulas']}")
        print(f"  {Colors.CYAN}Total Components:{Colors.ENDC} {metrics['total_components']}")
        print(f"  {Colors.YELLOW}Birth Date Influence:{Colors.ENDC} {metrics['birth_date_influence']:.6f}")
        print(f"  {Colors.GOLD}Quantum Signature:{Colors.ENDC} {metrics['quantum_signature']}")
    
    def _search_command(self, args):
        """Search knowledge base"""
        print(f"{Colors.QUANTUM}Searching for '{args.query}' with {Colors.PHI}φ-harmonic principles{Colors.ENDC}...")
        
        # Search knowledge
        phi_align = not args.no_phi
        search_results = self.bridge.search_knowledge(args.query, phi_align)
        
        if args.json:
            print(json.dumps(search_results, indent=2))
            return
        
        # Display results
        results = search_results.get('results', [])
        results_count = min(len(results), args.limit)
        
        print(f"\n{Colors.GREEN}Found {search_results['results_count']} results{Colors.ENDC}")
        print(f"{Colors.PHI}φ-Resonance:{Colors.ENDC} {search_results.get('phi_resonance', 0):.6f}")
        
        if results_count == 0:
            print(f"{Colors.YELLOW}No results found{Colors.ENDC}")
            return
        
        print(f"\n{Colors.QUANTUM}Top {results_count} Results:{Colors.ENDC}")
        for i, result in enumerate(results[:results_count]):
            result_type = result.get('type', 'unknown')
            result_id = result.get('id', '')
            content = result.get('content', '')
            
            # Format content for display
            if isinstance(content, dict):
                content_str = json.dumps(content, indent=2)
            else:
                content_str = str(content)
            
            # Truncate long content
            if len(content_str) > 200:
                content_str = content_str[:197] + '...'
            
            # Display φ-alignment if available
            phi_info = ""
            if 'phi_alignment' in result:
                phi_info = f" {Colors.PHI}φ:{Colors.ENDC} {result['phi_alignment']:.6f}"
            
            print(f"{Colors.BOLD}{i+1}. [{result_type}] {result_id}{phi_info}{Colors.ENDC}")
            print(f"   {textwrap.fill(content_str, width=80, initial_indent='   ', subsequent_indent='   ')}")
            print()
    
    def _get_command(self, args):
        """Get knowledge by type"""
        print(f"{Colors.QUANTUM}Getting knowledge of type '{args.type}' with {Colors.PHI}φ-harmonic principles{Colors.ENDC}...")
        
        # Get knowledge
        phi_align = not args.no_phi
        knowledge_results = self.bridge.get_knowledge_by_type(args.type, phi_align)
        
        if args.json:
            print(json.dumps(knowledge_results, indent=2))
            return
        
        # Display results
        if 'error' in knowledge_results:
            print(f"{Colors.RED}Error: {knowledge_results['error']}{Colors.ENDC}")
            return
        
        results = knowledge_results.get('results', [])
        results_count = min(len(results), args.limit)
        
        print(f"\n{Colors.GREEN}Found {knowledge_results['results_count']} items of type '{args.type}'{Colors.ENDC}")
        
        if results_count == 0:
            print(f"{Colors.YELLOW}No results found{Colors.ENDC}")
            return
        
        print(f"\n{Colors.QUANTUM}Top {results_count} Items:{Colors.ENDC}")
        for i, result in enumerate(results[:results_count]):
            result_id = result.get('id', '')
            content = result.get('content', '')
            
            # Format content for display
            if isinstance(content, dict):
                content_str = json.dumps(content, indent=2)
            else:
                content_str = str(content)
            
            # Truncate long content
            if len(content_str) > 200:
                content_str = content_str[:197] + '...'
            
            # Display φ-alignment if available
            phi_info = ""
            if 'phi_alignment' in result:
                phi_info = f" {Colors.PHI}φ:{Colors.ENDC} {result['phi_alignment']:.6f}"
            
            print(f"{Colors.BOLD}{i+1}. {result_id}{phi_info}{Colors.ENDC}")
            print(f"   {textwrap.fill(content_str, width=80, initial_indent='   ', subsequent_indent='   ')}")
            print()
    
    def _enhance_command(self, args):
        """Enhance a word with PDF knowledge"""
        print(f"{Colors.QUANTUM}Enhancing word '{args.word}' with {Colors.PHI}φ-harmonic principles{Colors.ENDC}...")
        
        # Enhance word
        enhanced_word = self.bridge.enhance_word_with_pdf_knowledge(args.word)
        
        if args.json:
            print(json.dumps(enhanced_word, indent=2))
            return
        
        # Display results
        print(f"\n{Colors.QUANTUM}Enhanced Word: {Colors.BOLD}{args.word}{Colors.ENDC}")
        print(f"{Colors.PHI}φ-Resonance:{Colors.ENDC} {enhanced_word['phi_resonance']:.6f}")
        print(f"{Colors.PHI}φ-Alignment:{Colors.ENDC} {enhanced_word['phi_alignment']:.6f}")
        print(f"{Colors.BLUE}Resonance Quality:{Colors.ENDC} {enhanced_word['resonance_quality']}")
        
        # Display binary if available
        if enhanced_word.get('binary'):
            binary = enhanced_word['binary']
            print(f"{Colors.CYAN}Binary:{Colors.ENDC} {binary}")
        
        # Display definition if available
        if enhanced_word.get('definition'):
            definition = enhanced_word['definition']
            print(f"\n{Colors.YELLOW}Definition:{Colors.ENDC}")
            print(f"  {textwrap.fill(definition, width=80, initial_indent='  ', subsequent_indent='  ')}")
        
        # Display synonyms if available
        if enhanced_word.get('synonyms'):
            synonyms = enhanced_word['synonyms']
            print(f"\n{Colors.YELLOW}Synonyms:{Colors.ENDC}")
            print(f"  {', '.join(synonyms)}")
        
        # Display PDF knowledge
        pdf_knowledge = enhanced_word.get('pdf_knowledge', [])
        if pdf_knowledge:
            print(f"\n{Colors.GREEN}PDF Knowledge ({len(pdf_knowledge)} items):{Colors.ENDC}")
            for i, item in enumerate(pdf_knowledge[:3]):  # Show top 3
                item_type = item.get('type', 'unknown')
                content = item.get('content', '')
                
                # Format content for display
                if isinstance(content, dict):
                    content_str = json.dumps(content, indent=2)
                else:
                    content_str = str(content)
                
                # Truncate long content
                if len(content_str) > 200:
                    content_str = content_str[:197] + '...'
                
                print(f"  {i+1}. [{item_type}] {textwrap.fill(content_str, width=80, initial_indent='     ', subsequent_indent='     ')}")
        
        # Display quantum signature
        print(f"\n{Colors.GOLD}Quantum Signature:{Colors.ENDC} {enhanced_word['quantum_signature']}")
    
    def _insights_command(self, args):
        """Generate quantum insights on a topic"""
        print(f"{Colors.QUANTUM}Generating quantum insights for '{args.topic}' with {Colors.PHI}φ-harmonic principles{Colors.ENDC}...")
        
        # Generate insights
        insights = self.bridge.generate_quantum_insights(args.topic, args.depth)
        
        if args.json:
            print(json.dumps(insights, indent=2))
            return
        
        # Display results
        print(f"\n{Colors.QUANTUM}Quantum Insights for: {Colors.BOLD}{args.topic}{Colors.ENDC}")
        print(f"{Colors.PHI}φ-Alignment:{Colors.ENDC} {insights['phi_alignment']:.6f}")
        print(f"{Colors.BLUE}Resonance Quality:{Colors.ENDC} {insights['resonance_quality']}")
        
        # Display insights
        insight_items = insights.get('insights', [])
        if not insight_items:
            print(f"\n{Colors.YELLOW}No insights generated{Colors.ENDC}")
            return
        
        print(f"\n{Colors.GREEN}Generated {insights['insights_count']} insights:{Colors.ENDC}")
        for i, insight in enumerate(insight_items):
            insight_type = insight.get('type', 'unknown')
            sources = insight.get('sources', 0)
            content = insight.get('content', [])
            
            # Display φ-alignment if available
            phi_info = ""
            if 'phi_alignment' in insight:
                phi_info = f" {Colors.PHI}φ:{Colors.ENDC} {insight['phi_alignment']:.6f}"
            
            print(f"\n{Colors.BOLD}{i+1}. [{insight_type}] {sources} sources{phi_info}{Colors.ENDC}")
            
            # Display content
            for j, item in enumerate(content):
                # Format content for display
                if isinstance(item, dict):
                    item_str = json.dumps(item, indent=2)
                else:
                    item_str = str(item)
                
                # Truncate long content
                if len(item_str) > 200:
                    item_str = item_str[:197] + '...'
                
                print(f"   {j+1}. {textwrap.fill(item_str, width=80, initial_indent='      ', subsequent_indent='      ')}")
        
        # Display quantum signature
        print(f"\n{Colors.GOLD}Quantum Signature:{Colors.ENDC} {insights['quantum_signature']}")
    
    def _interactive_mode(self):
        """Start interactive mode"""
        print(f"{Colors.QUANTUM}Quantum PDF Knowledge Bridge Interactive Mode{Colors.ENDC}")
        print(f"{Colors.PHI}φ-Harmonic Alignment: {self.PHI}{Colors.ENDC}")
        print(f"{Colors.YELLOW}Birth Date Resonance: {self.BIRTH_DATE_RESONANCE}{Colors.ENDC}")
        print(f"\nType {Colors.BOLD}help{Colors.ENDC} for available commands or {Colors.BOLD}exit{Colors.ENDC} to quit")
        
        while True:
            try:
                command = input(f"\n{Colors.QUANTUM}quantum>{Colors.ENDC} ").strip()
                
                if not command:
                    continue
                
                if command.lower() in ('exit', 'quit', 'q'):
                    break
                
                if command.lower() == 'help':
                    self._print_interactive_help()
                    continue
                
                # Parse command
                parts = command.split()
                cmd = parts[0].lower()
                args = parts[1:]
                
                if cmd == 'process':
                    self._process_command()
                elif cmd == 'metrics':
                    json_flag = '--json' in args
                    self._metrics_command(argparse.Namespace(json=json_flag))
                elif cmd == 'search':
                    if not args:
                        print(f"{Colors.RED}Error: Missing search query{Colors.ENDC}")
                        continue
                    
                    query = args[0]
                    no_phi = '--no-phi' in args
                    json_flag = '--json' in args
                    limit = 5
                    
                    # Check for limit
                    if '--limit' in args:
                        limit_index = args.index('--limit')
                        if limit_index + 1 < len(args):
                            try:
                                limit = int(args[limit_index + 1])
                            except ValueError:
                                pass
                    
                    self._search_command(argparse.Namespace(query=query, no_phi=no_phi, json=json_flag, limit=limit))
                elif cmd == 'get':
                    if not args:
                        print(f"{Colors.RED}Error: Missing knowledge type{Colors.ENDC}")
                        continue
                    
                    knowledge_type = args[0]
                    no_phi = '--no-phi' in args
                    json_flag = '--json' in args
                    limit = 5
                    
                    # Check for limit
                    if '--limit' in args:
                        limit_index = args.index('--limit')
                        if limit_index + 1 < len(args):
                            try:
                                limit = int(args[limit_index + 1])
                            except ValueError:
                                pass
                    
                    self._get_command(argparse.Namespace(type=knowledge_type, no_phi=no_phi, json=json_flag, limit=limit))
                elif cmd == 'enhance':
                    if not args:
                        print(f"{Colors.RED}Error: Missing word to enhance{Colors.ENDC}")
                        continue
                    
                    word = args[0]
                    json_flag = '--json' in args
                    
                    self._enhance_command(argparse.Namespace(word=word, json=json_flag))
                elif cmd == 'insights':
                    if not args:
                        print(f"{Colors.RED}Error: Missing topic for insights{Colors.ENDC}")
                        continue
                    
                    topic = args[0]
                    json_flag = '--json' in args
                    depth = 3
                    
                    # Check for depth
                    if '--depth' in args:
                        depth_index = args.index('--depth')
                        if depth_index + 1 < len(args):
                            try:
                                depth = int(args[depth_index + 1])
                            except ValueError:
                                pass
                    
                    self._insights_command(argparse.Namespace(topic=topic, depth=depth, json=json_flag))
                else:
                    print(f"{Colors.RED}Unknown command: {cmd}{Colors.ENDC}")
                    print(f"Type {Colors.BOLD}help{Colors.ENDC} for available commands")
            
            except KeyboardInterrupt:
                print("\nUse 'exit' to quit")
            except Exception as e:
                print(f"{Colors.RED}Error: {str(e)}{Colors.ENDC}")
    
    def _print_interactive_help(self):
        """Print help for interactive mode"""
        print(f"\n{Colors.QUANTUM}Available Commands:{Colors.ENDC}")
        print(f"  {Colors.BOLD}process{Colors.ENDC} - Process all PDFs and extract knowledge")
        print(f"  {Colors.BOLD}metrics{Colors.ENDC} [--json] - Display knowledge base metrics")
        print(f"  {Colors.BOLD}search{Colors.ENDC} <query> [--no-phi] [--json] [--limit <n>] - Search knowledge base")
        print(f"  {Colors.BOLD}get{Colors.ENDC} <type> [--no-phi] [--json] [--limit <n>] - Get knowledge by type")
        print(f"  {Colors.BOLD}enhance{Colors.ENDC} <word> [--json] - Enhance a word with PDF knowledge")
        print(f"  {Colors.BOLD}insights{Colors.ENDC} <topic> [--depth <n>] [--json] - Generate quantum insights")
        print(f"  {Colors.BOLD}help{Colors.ENDC} - Display this help message")
        print(f"  {Colors.BOLD}exit{Colors.ENDC} - Exit interactive mode")

# Main entry point
if __name__ == "__main__":
    cli = QuantumPDFBridgeCLI()
    cli.run()

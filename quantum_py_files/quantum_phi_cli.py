#!/usr/bin/env python3
"""
Quantum Phi-Harmonic System CLI

A unified command-line interface for the Quantum Phi-Harmonic System,
integrating text generation, music composition, and philosophical content
generation based on quantum phi-harmonic principles.

This CLI follows a modular "lego" approach where components work together
but remain independent, allowing for scalability and progressive learning.
"""

import os
import sys
import argparse
import importlib
import json
from typing import Dict, List, Any, Optional
import traceback

# Define version and system constants
VERSION = "1.0.0"
PHI = (1 + 5 ** 0.5) / 2  # Golden Ratio ≈ 1.618034
PI = 3.141592653589793
E = 2.718281828459045

class QuantumPhiCLI:
    """
    Main CLI for the Quantum Phi-Harmonic System.
    
    This class provides a unified interface to access all subsystems:
    - Text Generation (Poe, Hemingway, Austen, etc.)
    - Music Composition (Beethoven, Bach, Chopin, Mozart, etc.)
    - Philosophy Generation
    - Analysis Tools
    """
    
    def __init__(self):
        """Initialize the Quantum Phi CLI system."""
        self.config = self._load_config()
        self.modules = {}
        self._load_modules()
        
        # Track session metrics
        self.session_metrics = {
            "phi_resonance": 0.0,
            "consciousness_level": "physical",
            "mean_frequency": 0.0,
            "phi_alignment": 0.0
        }
    
    def _load_config(self) -> Dict:
        """Load configuration from config file."""
        config_path = os.path.join(os.path.dirname(__file__), "quantum_phi_config.json")
        
        # Create default config if it doesn't exist
        if not os.path.exists(config_path):
            default_config = {
                "modules": {
                    "text": {
                        "enabled": True,
                        "authors": ["poe", "hemingway", "austen", "shakespeare"]
                    },
                    "music": {
                        "enabled": True,
                        "composers": ["beethoven", "bach", "chopin", "mozart"]
                    },
                    "philosophy": {
                        "enabled": True,
                        "thinkers": ["quantum", "cosmic", "intuitive"]
                    },
                    "analysis": {
                        "enabled": True
                    }
                },
                "output_dirs": {
                    "text": "text_output",
                    "music": "midi_output",
                    "philosophy": "philosophy_output",
                    "analysis": "analysis_output"
                },
                "consciousness_levels": {
                    "physical": {"min_freq": 0, "max_freq": 200},
                    "emotional": {"min_freq": 200, "max_freq": 300},
                    "mental": {"min_freq": 300, "max_freq": 400},
                    "intuitive": {"min_freq": 400, "max_freq": 500},
                    "cosmic": {"min_freq": 500, "max_freq": 1000}
                }
            }
            
            # Create output directories
            for dir_path in default_config["output_dirs"].values():
                os.makedirs(dir_path, exist_ok=True)
            
            # Save default config
            with open(config_path, 'w') as f:
                json.dump(default_config, f, indent=4)
            
            return default_config
        
        # Load existing config
        try:
            with open(config_path, 'r') as f:
                return json.load(f)
        except Exception as e:
            print(f"Error loading config: {e}")
            sys.exit(1)
    
    def _load_modules(self):
        """Dynamically load available modules."""
        # Check for text generation module
        if self.config["modules"]["text"]["enabled"]:
            try:
                # First try to import the module directly
                try:
                    from quantum_phi_author import QuantumPhiAuthor
                    self.modules["text"] = {"class": QuantumPhiAuthor, "instance": None}
                    print("✓ Text generation module loaded")
                except ImportError:
                    print("⚠ Text generation module not found, will be disabled")
                    self.config["modules"]["text"]["enabled"] = False
            except Exception as e:
                print(f"⚠ Error loading text module: {e}")
                self.config["modules"]["text"]["enabled"] = False
        
        # Check for music composition module
        if self.config["modules"]["music"]["enabled"]:
            try:
                # First try to import the module directly
                try:
                    from quantum_phi_music_composer import QuantumPhiMusicComposer
                    self.modules["music"] = {"class": QuantumPhiMusicComposer, "instance": None}
                    print("✓ Music composition module loaded")
                except ImportError:
                    print("⚠ Music composition module not found, will be disabled")
                    self.config["modules"]["music"]["enabled"] = False
            except Exception as e:
                print(f"⚠ Error loading music module: {e}")
                self.config["modules"]["music"]["enabled"] = False
        
        # Check for philosophy module - this may need to be created
        if self.config["modules"]["philosophy"]["enabled"]:
            try:
                # First try to import the module directly
                try:
                    from quantum_phi_philosophy import QuantumPhiPhilosophy
                    self.modules["philosophy"] = {"class": QuantumPhiPhilosophy, "instance": None}
                    print("✓ Philosophy module loaded")
                except ImportError:
                    print("⚠ Philosophy module not found, will be disabled")
                    self.config["modules"]["philosophy"]["enabled"] = False
            except Exception as e:
                print(f"⚠ Error loading philosophy module: {e}")
                self.config["modules"]["philosophy"]["enabled"] = False
        
        # Check for analysis module - this may need to be created
        if self.config["modules"]["analysis"]["enabled"]:
            try:
                # First try to import the module directly
                try:
                    from quantum_phi_analyzer import QuantumPhiAnalyzer
                    self.modules["analysis"] = {"class": QuantumPhiAnalyzer, "instance": None}
                    print("✓ Analysis module loaded")
                except ImportError:
                    print("⚠ Analysis module not found, will be disabled")
                    self.config["modules"]["analysis"]["enabled"] = False
            except Exception as e:
                print(f"⚠ Error loading analysis module: {e}")
                self.config["modules"]["analysis"]["enabled"] = False
    
    def _initialize_module(self, module_name: str) -> bool:
        """Initialize a specific module if it's not already initialized."""
        if module_name not in self.modules or not self.config["modules"][module_name]["enabled"]:
            print(f"Module '{module_name}' is not available.")
            return False
        
        if self.modules[module_name]["instance"] is None:
            try:
                self.modules[module_name]["instance"] = self.modules[module_name]["class"]()
                return True
            except Exception as e:
                print(f"Error initializing {module_name} module: {e}")
                traceback.print_exc()
                return False
        
        return True
    
    def generate_text(self, author: str, prompt: str, length: int = 500) -> str:
        """Generate text in the style of the specified author."""
        if not self._initialize_module("text"):
            return "Text generation module is not available."
        
        try:
            result = self.modules["text"]["instance"].generate_text(author, prompt, length)
            
            # Update session metrics
            self.session_metrics["phi_resonance"] = result.get("phi_resonance", 0.0)
            self.session_metrics["consciousness_level"] = result.get("consciousness_level", "physical")
            self.session_metrics["mean_frequency"] = result.get("mean_frequency", 0.0)
            self.session_metrics["phi_alignment"] = result.get("phi_alignment", 0.0)
            
            return result["text"]
        except Exception as e:
            return f"Error generating text: {e}"
    
    def compose_music(self, style: str, output_file: str = None) -> str:
        """Compose music in the specified style."""
        if not self._initialize_module("music"):
            return "Music composition module is not available."
        
        try:
            if output_file is None:
                output_dir = self.config["output_dirs"]["music"]
                os.makedirs(output_dir, exist_ok=True)
                output_file = os.path.join(output_dir, f"{style}_phi_composition.mid")
            
            result = self.modules["music"]["instance"].compose(style, output_file)
            
            # Update session metrics
            self.session_metrics["phi_resonance"] = result.get("phi_resonance", 0.0)
            self.session_metrics["consciousness_level"] = result.get("consciousness_level", "physical")
            self.session_metrics["mean_frequency"] = result.get("mean_frequency", 0.0)
            self.session_metrics["phi_alignment"] = result.get("phi_alignment", 0.0)
            
            return f"Composed music in {style} style. Output file: {output_file}"
        except Exception as e:
            return f"Error composing music: {e}"
    
    def generate_philosophy(self, topic: str, consciousness_level: str = "cosmic") -> str:
        """Generate philosophical content on the specified topic."""
        if not self._initialize_module("philosophy"):
            return "Philosophy generation module is not available."
        
        try:
            result = self.modules["philosophy"]["instance"].generate_philosophy(topic, consciousness_level)
            
            # Update session metrics
            self.session_metrics["phi_resonance"] = result.get("phi_resonance", 0.0)
            self.session_metrics["consciousness_level"] = result.get("consciousness_level", "physical")
            self.session_metrics["mean_frequency"] = result.get("mean_frequency", 0.0)
            self.session_metrics["phi_alignment"] = result.get("phi_alignment", 0.0)
            
            return result["text"]
        except Exception as e:
            return f"Error generating philosophy: {e}"
    
    def analyze_content(self, content: str, content_type: str = "text") -> Dict:
        """Analyze content for quantum phi-harmonic metrics."""
        if not self._initialize_module("analysis"):
            return {"error": "Analysis module is not available."}
        
        try:
            result = self.modules["analysis"]["instance"].analyze(content, content_type)
            return result
        except Exception as e:
            return {"error": f"Error analyzing content: {e}"}
    
    def get_session_metrics(self) -> Dict:
        """Get current session metrics."""
        return self.session_metrics
    
    def run_interactive(self):
        """Run the CLI in interactive mode."""
        print(f"\n{'=' * 60}")
        print(f"Quantum Phi-Harmonic System CLI v{VERSION}")
        print(f"{'=' * 60}")
        print("Type 'help' for a list of commands, 'exit' to quit.")
        
        while True:
            try:
                command = input("\nQuantum-Phi> ").strip()
                
                if command.lower() in ['exit', 'quit', 'q']:
                    break
                elif command.lower() in ['help', '?', 'h']:
                    self._print_help()
                elif command.lower() in ['status', 'stat', 's']:
                    self._print_status()
                elif command.lower().startswith('text '):
                    self._handle_text_command(command[5:])
                elif command.lower().startswith('music '):
                    self._handle_music_command(command[6:])
                elif command.lower().startswith('philosophy '):
                    self._handle_philosophy_command(command[11:])
                elif command.lower().startswith('analyze '):
                    self._handle_analyze_command(command[8:])
                else:
                    print("Unknown command. Type 'help' for a list of commands.")
            except KeyboardInterrupt:
                print("\nOperation cancelled.")
            except Exception as e:
                print(f"Error: {e}")
    
    def _print_help(self):
        """Print help information."""
        print("\nAvailable Commands:")
        print("  help                   - Show this help message")
        print("  status                 - Show system status and available modules")
        print("  exit                   - Exit the program")
        
        if self.config["modules"]["text"]["enabled"]:
            print("\nText Generation:")
            print("  text list             - List available authors")
            print("  text generate <author> <prompt> [length] - Generate text in author's style")
            
        if self.config["modules"]["music"]["enabled"]:
            print("\nMusic Composition:")
            print("  music list            - List available composition styles")
            print("  music compose <style> [output_file] - Compose music in specified style")
            
        if self.config["modules"]["philosophy"]["enabled"]:
            print("\nPhilosophy Generation:")
            print("  philosophy list       - List available consciousness levels")
            print("  philosophy generate <topic> [consciousness_level] - Generate philosophical content")
            
        if self.config["modules"]["analysis"]["enabled"]:
            print("\nContent Analysis:")
            print("  analyze text <content>  - Analyze text for quantum phi-harmonic metrics")
            print("  analyze file <filename> - Analyze file content for quantum phi-harmonic metrics")
    
    def _print_status(self):
        """Print system status and available modules."""
        print("\nSystem Status:")
        print(f"  Version: {VERSION}")
        print(f"  Phi Constant: {PHI}")
        print(f"  Session Metrics:")
        print(f"    - Phi Resonance: {self.session_metrics['phi_resonance']:.4f}")
        print(f"    - Consciousness Level: {self.session_metrics['consciousness_level'].title()}")
        print(f"    - Mean Frequency: {self.session_metrics['mean_frequency']:.2f} Hz")
        print(f"    - Phi Alignment: {self.session_metrics['phi_alignment']:.4f}")
        
        print("\nAvailable Modules:")
        for module_name, enabled in [(k, v["enabled"]) for k, v in self.config["modules"].items()]:
            status = "✓ Enabled" if enabled else "✗ Disabled"
            print(f"  {module_name.title()}: {status}")
    
    def _handle_text_command(self, args: str):
        """Handle text generation commands."""
        if not self.config["modules"]["text"]["enabled"]:
            print("Text generation module is not available.")
            return
        
        parts = args.strip().split(maxsplit=2)
        
        if not parts:
            print("Invalid text command. Type 'help' for usage.")
            return
        
        if parts[0].lower() == 'list':
            print("\nAvailable Authors:")
            for author in self.config["modules"]["text"]["authors"]:
                print(f"  - {author.title()}")
        elif parts[0].lower() == 'generate':
            if len(parts) < 3:
                print("Usage: text generate <author> <prompt> [length]")
                return
            
            author = parts[1].lower()
            prompt_parts = parts[2].split(maxsplit=1)
            
            if len(prompt_parts) == 2 and prompt_parts[1].isdigit():
                prompt = prompt_parts[0]
                length = int(prompt_parts[1])
            else:
                prompt = parts[2]
                length = 500
            
            if author not in self.config["modules"]["text"]["authors"]:
                print(f"Unknown author: {author}. Use 'text list' to see available authors.")
                return
            
            print(f"\nGenerating text in the style of {author.title()}...")
            result = self.generate_text(author, prompt, length)
            print("\nGenerated Text:")
            print("-" * 60)
            print(result)
            print("-" * 60)
            
            # Print metrics
            print("\nQuantum Phi-Harmonic Metrics:")
            print(f"  - Consciousness Level: {self.session_metrics['consciousness_level'].title()}")
            print(f"  - Phi Resonance: {self.session_metrics['phi_resonance']:.4f}")
            print(f"  - Mean Frequency: {self.session_metrics['mean_frequency']:.2f} Hz")
            print(f"  - Phi Alignment: {self.session_metrics['phi_alignment']:.4f}")
        else:
            print("Unknown text command. Type 'help' for usage.")
    
    def _handle_music_command(self, args: str):
        """Handle music composition commands."""
        if not self.config["modules"]["music"]["enabled"]:
            print("Music composition module is not available.")
            return
        
        parts = args.strip().split(maxsplit=2)
        
        if not parts:
            print("Invalid music command. Type 'help' for usage.")
            return
        
        if parts[0].lower() == 'list':
            print("\nAvailable Composition Styles:")
            print("  - phi_harmonic")
            for composer in self.config["modules"]["music"]["composers"]:
                print(f"  - {composer}_style")
        elif parts[0].lower() == 'compose':
            if len(parts) < 2:
                print("Usage: music compose <style> [output_file]")
                return
            
            style = parts[1].lower()
            output_file = parts[2] if len(parts) > 2 else None
            
            valid_styles = ["phi_harmonic"] + [f"{c}_style" for c in self.config["modules"]["music"]["composers"]]
            if style not in valid_styles:
                print(f"Unknown style: {style}. Use 'music list' to see available styles.")
                return
            
            print(f"\nComposing music in {style} style...")
            result = self.compose_music(style, output_file)
            print(result)
            
            # Print metrics
            print("\nQuantum Phi-Harmonic Metrics:")
            print(f"  - Consciousness Level: {self.session_metrics['consciousness_level'].title()}")
            print(f"  - Phi Resonance: {self.session_metrics['phi_resonance']:.4f}")
            print(f"  - Mean Frequency: {self.session_metrics['mean_frequency']:.2f} Hz")
            print(f"  - Phi Alignment: {self.session_metrics['phi_alignment']:.4f}")
        else:
            print("Unknown music command. Type 'help' for usage.")
    
    def _handle_philosophy_command(self, args: str):
        """Handle philosophy generation commands."""
        if not self.config["modules"]["philosophy"]["enabled"]:
            print("Philosophy generation module is not available.")
            return
        
        parts = args.strip().split(maxsplit=2)
        
        if not parts:
            print("Invalid philosophy command. Type 'help' for usage.")
            return
        
        if parts[0].lower() == 'list':
            print("\nAvailable Consciousness Levels:")
            for level in self.config["consciousness_levels"].keys():
                print(f"  - {level.title()}")
        elif parts[0].lower() == 'generate':
            if len(parts) < 2:
                print("Usage: philosophy generate <topic> [consciousness_level]")
                return
            
            topic = parts[1]
            consciousness_level = parts[2].lower() if len(parts) > 2 else "cosmic"
            
            if consciousness_level not in self.config["consciousness_levels"]:
                print(f"Unknown consciousness level: {consciousness_level}. Using 'cosmic' instead.")
                consciousness_level = "cosmic"
            
            print(f"\nGenerating philosophical content on '{topic}' at {consciousness_level} consciousness level...")
            result = self.generate_philosophy(topic, consciousness_level)
            print("\nGenerated Philosophy:")
            print("-" * 60)
            print(result)
            print("-" * 60)
            
            # Print metrics
            print("\nQuantum Phi-Harmonic Metrics:")
            print(f"  - Consciousness Level: {self.session_metrics['consciousness_level'].title()}")
            print(f"  - Phi Resonance: {self.session_metrics['phi_resonance']:.4f}")
            print(f"  - Mean Frequency: {self.session_metrics['mean_frequency']:.2f} Hz")
            print(f"  - Phi Alignment: {self.session_metrics['phi_alignment']:.4f}")
        else:
            print("Unknown philosophy command. Type 'help' for usage.")
    
    def _handle_analyze_command(self, args: str):
        """Handle content analysis commands."""
        if not self.config["modules"]["analysis"]["enabled"]:
            print("Analysis module is not available.")
            return
        
        parts = args.strip().split(maxsplit=1)
        
        if len(parts) < 2:
            print("Usage: analyze <text|file> <content|filename>")
            return
        
        analysis_type = parts[0].lower()
        content = parts[1]
        
        if analysis_type == 'text':
            print("\nAnalyzing text content...")
            result = self.analyze_content(content, "text")
        elif analysis_type == 'file':
            if not os.path.exists(content):
                print(f"File not found: {content}")
                return
            
            try:
                with open(content, 'r') as f:
                    file_content = f.read()
                
                print(f"\nAnalyzing file: {content}...")
                result = self.analyze_content(file_content, "text")
            except Exception as e:
                print(f"Error reading file: {e}")
                return
        else:
            print(f"Unknown analysis type: {analysis_type}. Use 'text' or 'file'.")
            return
        
        if "error" in result:
            print(f"Analysis error: {result['error']}")
            return
        
        print("\nAnalysis Results:")
        print("-" * 60)
        for key, value in result.items():
            if isinstance(value, float):
                print(f"{key.replace('_', ' ').title()}: {value:.4f}")
            else:
                print(f"{key.replace('_', ' ').title()}: {value}")
        print("-" * 60)


def main():
    """Main entry point for the Quantum Phi-Harmonic CLI."""
    parser = argparse.ArgumentParser(description="Quantum Phi-Harmonic System CLI")
    parser.add_argument('--version', action='version', version=f'%(prog)s {VERSION}')
    
    subparsers = parser.add_subparsers(dest='command', help='Command to run')
    
    # Text generation command
    text_parser = subparsers.add_parser('text', help='Text generation commands')
    text_subparsers = text_parser.add_subparsers(dest='text_command')
    
    text_list = text_subparsers.add_parser('list', help='List available authors')
    
    text_generate = text_subparsers.add_parser('generate', help='Generate text in author style')
    text_generate.add_argument('author', help='Author name')
    text_generate.add_argument('prompt', help='Text prompt')
    text_generate.add_argument('--length', type=int, default=500, help='Text length')
    
    # Music composition command
    music_parser = subparsers.add_parser('music', help='Music composition commands')
    music_subparsers = music_parser.add_subparsers(dest='music_command')
    
    music_list = music_subparsers.add_parser('list', help='List available composition styles')
    
    music_compose = music_subparsers.add_parser('compose', help='Compose music in specified style')
    music_compose.add_argument('style', help='Composition style')
    music_compose.add_argument('--output', help='Output file path')
    
    # Philosophy generation command
    philosophy_parser = subparsers.add_parser('philosophy', help='Philosophy generation commands')
    philosophy_subparsers = philosophy_parser.add_subparsers(dest='philosophy_command')
    
    philosophy_list = philosophy_subparsers.add_parser('list', help='List available consciousness levels')
    
    philosophy_generate = philosophy_subparsers.add_parser('generate', help='Generate philosophical content')
    philosophy_generate.add_argument('topic', help='Topic for philosophical content')
    philosophy_generate.add_argument('--level', default='cosmic', help='Consciousness level')
    
    # Analysis command
    analysis_parser = subparsers.add_parser('analyze', help='Content analysis commands')
    analysis_subparsers = analysis_parser.add_subparsers(dest='analysis_command')
    
    analysis_text = analysis_subparsers.add_parser('text', help='Analyze text content')
    analysis_text.add_argument('content', help='Text content to analyze')
    
    analysis_file = analysis_subparsers.add_parser('file', help='Analyze file content')
    analysis_file.add_argument('filename', help='File to analyze')
    
    # Parse arguments
    args = parser.parse_args()
    
    # Create CLI instance
    cli = QuantumPhiCLI()
    
    # If no arguments provided, run in interactive mode
    if len(sys.argv) == 1:
        cli.run_interactive()
        return
    
    # Handle commands
    if args.command == 'text':
        if args.text_command == 'list':
            print("\nAvailable Authors:")
            for author in cli.config["modules"]["text"]["authors"]:
                print(f"  - {author.title()}")
        elif args.text_command == 'generate':
            result = cli.generate_text(args.author, args.prompt, args.length)
            print(result)
    elif args.command == 'music':
        if args.music_command == 'list':
            print("\nAvailable Composition Styles:")
            print("  - phi_harmonic")
            for composer in cli.config["modules"]["music"]["composers"]:
                print(f"  - {composer}_style")
        elif args.music_command == 'compose':
            result = cli.compose_music(args.style, args.output)
            print(result)
    elif args.command == 'philosophy':
        if args.philosophy_command == 'list':
            print("\nAvailable Consciousness Levels:")
            for level in cli.config["consciousness_levels"].keys():
                print(f"  - {level.title()}")
        elif args.philosophy_command == 'generate':
            result = cli.generate_philosophy(args.topic, args.level)
            print(result)
    elif args.command == 'analyze':
        if args.analysis_command == 'text':
            result = cli.analyze_content(args.content, "text")
            print(json.dumps(result, indent=2))
        elif args.analysis_command == 'file':
            try:
                with open(args.filename, 'r') as f:
                    content = f.read()
                result = cli.analyze_content(content, "text")
                print(json.dumps(result, indent=2))
            except Exception as e:
                print(f"Error reading file: {e}")


if __name__ == "__main__":
    main()

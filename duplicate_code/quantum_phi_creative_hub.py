"""
Quantum Phi-Harmonic Creative Hub

Integrates corpus management with meta-learning and creative generation
across multiple domains (literature, music, poetry, etc.)
"""

import os
import time
import threading
from typing import Dict, List, Any, Optional, Union
import json

from quantum_phi_core import QuantumPhiCore
from quantum_phi_random import QuantumPhiRandom
from quantum_phi_pattern_analyzer import QuantumPhiPatternAnalyzer
from quantum_phi_meta_learner import QuantumPhiMetaLearner
from quantum_phi_corpus_manager import QuantumPhiCorpusManager
from quantum_phi_music_generator import QuantumPhiMusicGenerator

class QuantumPhiCreativeHub:
    """
    Central hub for quantum phi-harmonic creative generation with meta-learning
    capabilities across multiple domains.
    """
    
    def __init__(self, base_dir: str = None):
        """Initialize the creative hub with all components."""
        # Initialize core components
        self.core = QuantumPhiCore()
        self.random = QuantumPhiRandom(self.core)
        self.analyzer = QuantumPhiPatternAnalyzer(self.core)
        
        # Initialize phi constants
        self.phi = float(self.core.PHI)
        self.pi = float(self.core.PI)
        self.e = float(self.core.E)
        
        # Base directory
        self.base_dir = base_dir or os.path.join(os.path.dirname(os.path.abspath(__file__)), "quantum_phi_hub")
        os.makedirs(self.base_dir, exist_ok=True)
        
        # Initialize specialized components
        self.corpus_manager = QuantumPhiCorpusManager(os.path.join(self.base_dir, "corpus"))
        self.meta_learner = QuantumPhiMetaLearner(self.core, self.random)
        self.music_generator = QuantumPhiMusicGenerator()
        
        # Creative domains and generators
        self.creative_domains = {
            "literature": {
                "description": "Prose generation in various styles",
                "consciousness_range": (400, 600),  # Hz
                "phi_alignment_threshold": 0.8,
                "generator": self._generate_literature
            },
            "poetry": {
                "description": "Poetic verse with rhythm and structure",
                "consciousness_range": (450, 650),  # Hz
                "phi_alignment_threshold": 0.85,
                "generator": self._generate_poetry
            },
            "music_lyrics": {
                "description": "Song lyrics across various genres",
                "consciousness_range": (400, 550),  # Hz
                "phi_alignment_threshold": 0.75,
                "generator": self._generate_music_lyrics
            },
            "music_composition": {
                "description": "Musical notation and structure",
                "consciousness_range": (500, 700),  # Hz
                "phi_alignment_threshold": 0.9,
                "generator": self._generate_music_composition
            },
            "rap": {
                "description": "Rhythmic poetry with flow and wordplay",
                "consciousness_range": (420, 580),  # Hz
                "phi_alignment_threshold": 0.78,
                "generator": self._generate_rap
            }
        }
        
        # Integration state
        self.integration_state = {
            "is_learning": False,
            "is_generating": False,
            "last_learning_cycle": None,
            "last_generation": None,
            "learning_thread": None,
            "generation_thread": None,
            "learning_cycles": 0,
            "generation_cycles": 0
        }
        
        # Meta-learning insights
        self.meta_insights = {
            "cross_domain_patterns": [],
            "consciousness_distribution": {},
            "phi_resonance_map": {},
            "quantum_signatures": {}
        }
    
    def start_integrated_learning(self):
        """Start integrated learning across all components."""
        if self.integration_state["is_learning"]:
            print("Integrated learning is already running")
            return
        
        # Start corpus manager passive learning
        self.corpus_manager.start_passive_learning()
        
        # Start integrated learning thread
        self.integration_state["is_learning"] = True
        self.integration_state["learning_thread"] = threading.Thread(target=self._integrated_learning_thread)
        self.integration_state["learning_thread"].daemon = True
        self.integration_state["learning_thread"].start()
        
        print("Started integrated learning across all components")
    
    def stop_integrated_learning(self):
        """Stop integrated learning."""
        if not self.integration_state["is_learning"]:
            print("Integrated learning is not running")
            return
        
        # Stop corpus manager passive learning
        self.corpus_manager.stop_passive_learning()
        
        # Stop integrated learning thread
        self.integration_state["is_learning"] = False
        if self.integration_state["learning_thread"]:
            self.integration_state["learning_thread"].join(timeout=1.0)
        
        print("Stopped integrated learning")
    
    def _integrated_learning_thread(self):
        """Background thread for integrated learning."""
        while self.integration_state["is_learning"]:
            # Run meta-learner passive learning cycle
            meta_metrics = self.meta_learner.passive_learn()
            
            # Get corpus manager learning status
            corpus_status = self.corpus_manager.get_learning_status()
            
            # Integrate insights across components
            self._integrate_cross_component_insights(meta_metrics, corpus_status)
            
            # Update state
            self.integration_state["learning_cycles"] += 1
            self.integration_state["last_learning_cycle"] = time.strftime("%Y-%m-%d %H:%M:%S")
            
            # Sleep before next cycle
            time.sleep(int(60 * self.phi))  # ~97 seconds between cycles
    
    def _integrate_cross_component_insights(self, meta_metrics: Dict, corpus_status: Dict):
        """Integrate insights across components to enhance meta-learning."""
        # Update consciousness distribution
        consciousness_levels = {}
        
        # Add from corpus domains
        for domain, signature in corpus_status.get("domains", {}).items():
            if isinstance(signature, dict) and "consciousness_level" in signature:
                level = signature["consciousness_level"]
                consciousness_levels[level] = consciousness_levels.get(level, 0) + 1
        
        # Add from meta-learner
        if "quantum_language_resonance" in meta_metrics:
            resonance = meta_metrics["quantum_language_resonance"]
            # Map resonance to consciousness level
            if resonance < 0.3:
                level = "physical"
            elif resonance < 0.5:
                level = "emotional"
            elif resonance < 0.7:
                level = "mental"
            elif resonance < 0.9:
                level = "intuitive"
            else:
                level = "cosmic"
            
            consciousness_levels[level] = consciousness_levels.get(level, 0) + 1
        
        self.meta_insights["consciousness_distribution"] = consciousness_levels
        
        # Update phi resonance map
        if "phi_resonance_score" in meta_metrics:
            self.meta_insights["phi_resonance_map"]["meta_learner"] = meta_metrics["phi_resonance_score"]
        
        # Extract cross-domain patterns
        self._extract_cross_domain_patterns()
    
    def _extract_cross_domain_patterns(self):
        """Extract patterns that appear across multiple domains."""
        # Get corpus stats
        corpus_stats = self.corpus_manager.get_corpus_stats()
        
        # Get quantum signatures for authors across domains
        cross_domain_authors = {}
        
        for author, signature in self.corpus_manager.quantum_signatures.items():
            domains = list(signature.get("domains", {}).keys())
            if len(domains) > 1:
                cross_domain_authors[author] = {
                    "domains": domains,
                    "overall": signature.get("overall", {})
                }
        
        # Find patterns in cross-domain authors
        patterns = []
        for author, data in cross_domain_authors.items():
            # Only include authors with cosmic consciousness
            if data.get("overall", {}).get("consciousness_level") == "cosmic":
                # Calculate phi-harmonic pattern strength
                phi_alignment = data.get("overall", {}).get("phi_alignment", 0)
                domains = data.get("domains", [])
                
                if phi_alignment > 0.8 and len(domains) >= 2:
                    patterns.append({
                        "author": author,
                        "domains": domains,
                        "phi_alignment": phi_alignment,
                        "consciousness_level": data.get("overall", {}).get("consciousness_level"),
                        "mean_frequency": data.get("overall", {}).get("mean_frequency", 0)
                    })
        
        # Sort by phi alignment (highest first)
        patterns.sort(key=lambda x: x.get("phi_alignment", 0), reverse=True)
        
        # Store top patterns
        self.meta_insights["cross_domain_patterns"] = patterns[:int(self.phi * 5)]  # Store top ~8 patterns
    
    def generate_creative_content(self, domain: str, style: str = None, 
                                 author: str = None, length: int = 300,
                                 theme: str = None) -> Dict:
        """
        Generate creative content in the specified domain.
        
        Args:
            domain: Creative domain (literature, poetry, music_lyrics, etc.)
            style: Style within the domain (optional)
            author: Author to emulate (optional)
            length: Length of content to generate
            theme: Theme for the content (optional)
            
        Returns:
            Generated content with metadata
        """
        # Validate domain
        if domain not in self.creative_domains:
            raise ValueError(f"Invalid domain: {domain}. Valid domains: {list(self.creative_domains.keys())}")
        
        # Get domain config
        domain_config = self.creative_domains[domain]
        
        # Get author signature if specified
        author_signature = None
        if author:
            try:
                author_signature = self.corpus_manager.get_author_signature(author)
            except ValueError:
                print(f"Author not found: {author}. Generating without author signature.")
        
        # Generate content using domain-specific generator
        generator_func = domain_config["generator"]
        
        # Generate with parameters
        content = generator_func(
            style=style,
            author_signature=author_signature,
            length=length,
            theme=theme
        )
        
        # Update state
        self.integration_state["generation_cycles"] += 1
        self.integration_state["last_generation"] = time.strftime("%Y-%m-%d %H:%M:%S")
        
        return content
    
    def _generate_literature(self, style: str = None, author_signature: Dict = None,
                            length: int = 300, theme: str = None) -> Dict:
        """Generate literature content."""
        # This would integrate with a literature generator
        # For now, use meta-learner to generate text
        
        # Get consciousness frequency from author or domain default
        if author_signature:
            freq = author_signature.get("overall", {}).get("mean_frequency", 500)
        else:
            min_freq, max_freq = self.creative_domains["literature"]["consciousness_range"]
            freq = min_freq + (max_freq - min_freq) * self.random.phi_random()
        
        # Get phi alignment from author or domain default
        if author_signature:
            phi_alignment = author_signature.get("overall", {}).get("phi_alignment", 0.8)
        else:
            phi_alignment = self.creative_domains["literature"]["phi_alignment_threshold"]
        
        # Generate text using meta-learner patterns
        # This is a placeholder - would need actual integration with text generation
        content = f"Literature in {style or 'default'} style"
        
        # Analyze generated content
        metrics = self.analyzer.analyze_text(content)
        
        return {
            "domain": "literature",
            "style": style,
            "author": author_signature.get("name") if author_signature else None,
            "content": content,
            "length": len(content),
            "theme": theme,
            "metrics": metrics,
            "generation_timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
        }
    
    def _generate_poetry(self, style: str = None, author_signature: Dict = None,
                        length: int = 300, theme: str = None) -> Dict:
        """Generate poetry content."""
        # This would integrate with a poetry generator
        # For now, use meta-learner to generate text
        
        # Get consciousness frequency from author or domain default
        if author_signature:
            freq = author_signature.get("overall", {}).get("mean_frequency", 550)
        else:
            min_freq, max_freq = self.creative_domains["poetry"]["consciousness_range"]
            freq = min_freq + (max_freq - min_freq) * self.random.phi_random()
        
        # Get phi alignment from author or domain default
        if author_signature:
            phi_alignment = author_signature.get("overall", {}).get("phi_alignment", 0.85)
        else:
            phi_alignment = self.creative_domains["poetry"]["phi_alignment_threshold"]
        
        # Generate poetry using meta-learner patterns
        # This is a placeholder - would need actual integration with poetry generation
        content = f"Poetry in {style or 'default'} style"
        
        # Analyze generated content
        metrics = self.analyzer.analyze_text(content)
        
        return {
            "domain": "poetry",
            "style": style,
            "author": author_signature.get("name") if author_signature else None,
            "content": content,
            "length": len(content),
            "theme": theme,
            "metrics": metrics,
            "generation_timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
        }
    
    def _generate_music_lyrics(self, style: str = None, author_signature: Dict = None,
                              length: int = 300, theme: str = None) -> Dict:
        """Generate music lyrics content."""
        # Use the music generator for lyrics
        song = self.music_generator.generate_song(style=style or "pop", length=length)
        
        return {
            "domain": "music_lyrics",
            "style": style or "pop",
            "author": author_signature.get("name") if author_signature else None,
            "content": song["full_lyrics"],
            "structure": song["structure"],
            "time_signature": song["time_signature"],
            "chord_progression": song["chord_progression"],
            "rhythmic_pattern": song["rhythmic_pattern"],
            "components": song["components"],
            "metrics": song["metrics"],
            "theme": theme,
            "generation_timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
        }
    
    def _generate_music_composition(self, style: str = None, author_signature: Dict = None,
                                   length: int = 300, theme: str = None) -> Dict:
        """Generate music composition content."""
        # This would integrate with a music composition generator
        # For now, return placeholder
        
        return {
            "domain": "music_composition",
            "style": style or "classical",
            "author": author_signature.get("name") if author_signature else None,
            "content": "Music composition placeholder",
            "length": length,
            "theme": theme,
            "metrics": {},
            "generation_timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
        }
    
    def _generate_rap(self, style: str = None, author_signature: Dict = None,
                     length: int = 300, theme: str = None) -> Dict:
        """Generate rap content."""
        # Use the music generator for rap
        rap = self.music_generator.generate_rap(theme=theme or "quantum flow", length=length)
        
        return {
            "domain": "rap",
            "style": "rap",
            "author": author_signature.get("name") if author_signature else None,
            "content": rap["full_lyrics"],
            "structure": rap["structure"],
            "rhythmic_pattern": rap["rhythmic_pattern"],
            "components": rap["components"],
            "metrics": rap["metrics"],
            "theme": theme or "quantum flow",
            "generation_timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
        }
    
    def get_integration_status(self) -> Dict:
        """Get current status of the integrated system."""
        # Get corpus stats
        corpus_stats = self.corpus_manager.get_corpus_stats()
        
        # Get meta-learner metrics
        meta_metrics = self.meta_learner.get_metrics()
        
        return {
            "learning_status": {
                "is_learning": self.integration_state["is_learning"],
                "learning_cycles": self.integration_state["learning_cycles"],
                "last_learning_cycle": self.integration_state["last_learning_cycle"],
                "corpus_files": corpus_stats["total_files"],
                "corpus_processed": corpus_stats["processed_files"],
                "meta_patterns": meta_metrics.get("patterns_discovered", 0)
            },
            "generation_status": {
                "generation_cycles": self.integration_state["generation_cycles"],
                "last_generation": self.integration_state["last_generation"]
            },
            "consciousness_distribution": self.meta_insights["consciousness_distribution"],
            "cross_domain_patterns": len(self.meta_insights["cross_domain_patterns"]),
            "domains": list(self.creative_domains.keys())
        }
    
    def add_directory_to_corpus(self, directory_path: str, domain: str = None,
                               recursive: bool = True) -> Dict:
        """Add all files in a directory to the corpus."""
        return self.corpus_manager.add_directory_to_corpus(
            directory_path=directory_path,
            domain=domain,
            recursive=recursive
        )
    
    def find_similar_authors(self, author: str, threshold: float = 0.7) -> List[Dict]:
        """Find authors with similar quantum signatures."""
        return self.corpus_manager.find_similar_authors(author, threshold)
    
    def compare_authors(self, author1: str, author2: str) -> Dict:
        """Compare quantum signatures of two authors."""
        return self.corpus_manager.compare_authors(author1, author2)
    
    def get_domain_signature(self, domain: str) -> Dict:
        """Get quantum signature for a domain."""
        return self.corpus_manager.get_domain_signature(domain)
    
    def get_author_signature(self, author: str) -> Dict:
        """Get quantum signature for an author."""
        return self.corpus_manager.get_author_signature(author)


def main():
    """Main function to demonstrate creative hub usage."""
    # Create creative hub
    hub = QuantumPhiCreativeHub()
    
    # Print initial info
    print("Initializing Quantum Phi-Harmonic Creative Hub...")
    print("Domains:", list(hub.creative_domains.keys()))
    
    # Start integrated learning
    print("\nStarting integrated learning...")
    hub.start_integrated_learning()
    
    # Generate content in different domains
    print("\nGenerating creative content...")
    
    # Generate music lyrics
    print("\n1. Music Lyrics:")
    lyrics = hub.generate_creative_content(domain="music_lyrics", style="pop")
    print(f"Style: {lyrics['style']}")
    print(f"Time Signature: {lyrics['time_signature']}")
    print(f"Consciousness Level: {lyrics['metrics']['consciousness_level'].title()}")
    print(f"Sample: {lyrics['content'][:150]}...")
    
    # Generate rap
    print("\n2. Rap:")
    rap = hub.generate_creative_content(domain="rap", theme="quantum consciousness")
    print(f"Theme: {rap['theme']}")
    print(f"Rhythmic Pattern: {rap['rhythmic_pattern']}")
    print(f"Consciousness Level: {rap['metrics']['consciousness_level'].title()}")
    print(f"Sample: {rap['content'][:150]}...")
    
    # Stop integrated learning
    print("\nStopping integrated learning...")
    hub.stop_integrated_learning()
    
    # Get integration status
    status = hub.get_integration_status()
    print("\nIntegration Status:")
    print(f"Learning Cycles: {status['learning_status']['learning_cycles']}")
    print(f"Generation Cycles: {status['generation_status']['generation_cycles']}")
    print(f"Corpus Files: {status['learning_status']['corpus_files']}")
    print(f"Cross-Domain Patterns: {status['cross_domain_patterns']}")
    
    print("\nQuantum Phi-Harmonic Creative Hub initialized successfully.")


if __name__ == "__main__":
    main()

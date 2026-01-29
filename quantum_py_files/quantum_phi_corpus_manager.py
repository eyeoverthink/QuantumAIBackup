"""
Quantum Phi-Harmonic Corpus Manager

A meta-learning system for managing and analyzing various types of creative content
using quantum phi-harmonic principles.
"""

import os
import re
import json
import numpy as np
import hashlib
from typing import Dict, List, Tuple, Any, Set, Optional, Union
from pathlib import Path
import threading
import time
from collections import defaultdict

# Import core quantum components
from quantum_phi_core import QuantumPhiCore
from quantum_phi_pattern_analyzer import QuantumPhiPatternAnalyzer

class QuantumPhiCorpusManager:
    """
    Manages corpora of creative content for meta-learning using quantum phi-harmonic principles.
    Supports multiple content types: text, music, poetry, etc.
    """
    
    def __init__(self, base_dir: str = None):
        """Initialize the corpus manager."""
        self.core = QuantumPhiCore()
        self.analyzer = QuantumPhiPatternAnalyzer(self.core)
        self.phi = float(self.core.PHI)
        self.pi = float(self.core.PI)
        self.e = float(self.core.E)
        
        # Base directory for corpus storage
        self.base_dir = base_dir or os.path.join(os.path.dirname(os.path.abspath(__file__)), "corpus")
        os.makedirs(self.base_dir, exist_ok=True)
        
        # Initialize corpus domains
        self.domains = {
            "literature": {
                "path": os.path.join(self.base_dir, "literature"),
                "extensions": [".txt", ".md", ".pdf", ".epub"],
                "quantum_signature": {}
            },
            "poetry": {
                "path": os.path.join(self.base_dir, "poetry"),
                "extensions": [".txt", ".md", ".pdf"],
                "quantum_signature": {}
            },
            "music_lyrics": {
                "path": os.path.join(self.base_dir, "music_lyrics"),
                "extensions": [".txt", ".lrc", ".md"],
                "quantum_signature": {}
            },
            "music_composition": {
                "path": os.path.join(self.base_dir, "music_composition"),
                "extensions": [".mid", ".midi", ".mxl", ".musicxml", ".abc"],
                "quantum_signature": {}
            },
            "rap": {
                "path": os.path.join(self.base_dir, "rap"),
                "extensions": [".txt", ".lrc", ".md"],
                "quantum_signature": {}
            }
        }
        
        # Create domain directories
        for domain in self.domains.values():
            os.makedirs(domain["path"], exist_ok=True)
        
        # Corpus metadata storage
        self.metadata_path = os.path.join(self.base_dir, "metadata.json")
        self.corpus_metadata = self._load_metadata()
        
        # Quantum signatures for authors/artists
        self.signatures_path = os.path.join(self.base_dir, "quantum_signatures.json")
        self.quantum_signatures = self._load_signatures()
        
        # Meta-learning state
        self.learning_state = {
            "is_learning": False,
            "last_update": None,
            "files_processed": 0,
            "total_files": 0,
            "current_domain": None
        }
        
        # Thread for passive learning
        self.learning_thread = None
    
    def _load_metadata(self) -> Dict:
        """Load corpus metadata from disk."""
        if os.path.exists(self.metadata_path):
            try:
                with open(self.metadata_path, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except Exception as e:
                print(f"Error loading metadata: {e}")
                return {"files": {}, "domains": {}}
        return {"files": {}, "domains": {}}
    
    def _save_metadata(self):
        """Save corpus metadata to disk."""
        try:
            with open(self.metadata_path, 'w', encoding='utf-8') as f:
                json.dump(self.corpus_metadata, f, indent=2)
        except Exception as e:
            print(f"Error saving metadata: {e}")
    
    def _load_signatures(self) -> Dict:
        """Load quantum signatures from disk."""
        if os.path.exists(self.signatures_path):
            try:
                with open(self.signatures_path, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except Exception as e:
                print(f"Error loading signatures: {e}")
                return {}
        return {}
    
    def _save_signatures(self):
        """Save quantum signatures to disk."""
        try:
            with open(self.signatures_path, 'w', encoding='utf-8') as f:
                json.dump(self.quantum_signatures, f, indent=2)
        except Exception as e:
            print(f"Error saving signatures: {e}")
    
    def add_file_to_corpus(self, file_path: str, domain: str = None, author: str = None, 
                          title: str = None, process_immediately: bool = True) -> Dict:
        """
        Add a file to the corpus for a specific domain.
        
        Args:
            file_path: Path to the file
            domain: Domain to add the file to (literature, poetry, music_lyrics, etc.)
            author: Author/artist name
            title: Title of the work
            process_immediately: Whether to process the file immediately
            
        Returns:
            Metadata about the added file
        """
        # Validate file exists
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")
        
        # Determine domain from file extension if not provided
        if domain is None:
            ext = os.path.splitext(file_path)[1].lower()
            for d_name, d_info in self.domains.items():
                if ext in d_info["extensions"]:
                    domain = d_name
                    break
            
            if domain is None:
                raise ValueError(f"Could not determine domain for file with extension {ext}")
        
        # Validate domain
        if domain not in self.domains:
            raise ValueError(f"Invalid domain: {domain}. Valid domains: {list(self.domains.keys())}")
        
        # Generate file hash for tracking
        file_hash = self._hash_file(file_path)
        
        # Create file metadata
        file_name = os.path.basename(file_path)
        dest_path = os.path.join(self.domains[domain]["path"], file_name)
        
        # Copy file to corpus if it's not already there
        if file_path != dest_path:
            import shutil
            shutil.copy2(file_path, dest_path)
        
        # Create metadata entry
        metadata = {
            "file_path": dest_path,
            "original_path": file_path,
            "domain": domain,
            "author": author,
            "title": title or os.path.splitext(file_name)[0],
            "added_date": time.strftime("%Y-%m-%d %H:%M:%S"),
            "last_processed": None,
            "file_hash": file_hash,
            "quantum_metrics": {},
            "size_bytes": os.path.getsize(file_path)
        }
        
        # Add to metadata
        self.corpus_metadata["files"][file_hash] = metadata
        
        # Update domain metadata
        if domain not in self.corpus_metadata["domains"]:
            self.corpus_metadata["domains"][domain] = {
                "file_count": 0,
                "total_size_bytes": 0,
                "authors": set(),
                "last_updated": None
            }
        
        domain_meta = self.corpus_metadata["domains"][domain]
        domain_meta["file_count"] = domain_meta.get("file_count", 0) + 1
        domain_meta["total_size_bytes"] = domain_meta.get("total_size_bytes", 0) + metadata["size_bytes"]
        if author:
            if isinstance(domain_meta.get("authors", None), set):
                domain_meta["authors"].add(author)
            else:
                domain_meta["authors"] = set([author])
        domain_meta["last_updated"] = metadata["added_date"]
        
        # Convert sets to lists for JSON serialization
        if isinstance(domain_meta.get("authors", None), set):
            domain_meta["authors"] = list(domain_meta["authors"])
        
        # Save metadata
        self._save_metadata()
        
        # Process file if requested
        if process_immediately:
            self.process_file(file_hash)
        
        return metadata
    
    def _hash_file(self, file_path: str) -> str:
        """Generate a hash for a file."""
        hasher = hashlib.md5()
        with open(file_path, 'rb') as f:
            buf = f.read(65536)
            while len(buf) > 0:
                hasher.update(buf)
                buf = f.read(65536)
        return hasher.hexdigest()
    
    def process_file(self, file_hash: str) -> Dict:
        """
        Process a file to extract quantum metrics and update metadata.
        
        Args:
            file_hash: Hash of the file to process
            
        Returns:
            Updated metadata for the file
        """
        # Check if file exists in metadata
        if file_hash not in self.corpus_metadata["files"]:
            raise ValueError(f"File with hash {file_hash} not found in corpus metadata")
        
        metadata = self.corpus_metadata["files"][file_hash]
        file_path = metadata["file_path"]
        
        # Check if file exists
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")
        
        # Process based on domain
        domain = metadata["domain"]
        
        # Extract content based on file type
        content = self._extract_content(file_path)
        
        # Analyze content using quantum phi-harmonic analyzer
        quantum_metrics = self.analyzer.analyze_text(content)
        
        # Update metadata
        metadata["quantum_metrics"] = quantum_metrics
        metadata["last_processed"] = time.strftime("%Y-%m-%d %H:%M:%S")
        
        # Update author signature if author is specified
        if metadata["author"]:
            self._update_author_signature(metadata["author"], domain, quantum_metrics)
        
        # Save metadata
        self._save_metadata()
        
        return metadata
    
    def _extract_content(self, file_path: str) -> str:
        """Extract content from a file based on its type."""
        ext = os.path.splitext(file_path)[1].lower()
        
        # Text files
        if ext in ['.txt', '.md', '.lrc']:
            with open(file_path, 'r', encoding='utf-8', errors='replace') as f:
                return f.read()
        
        # PDF files
        elif ext == '.pdf':
            try:
                import PyPDF2
                with open(file_path, 'rb') as f:
                    reader = PyPDF2.PdfReader(f)
                    return ' '.join(page.extract_text() for page in reader.pages)
            except ImportError:
                print("PyPDF2 not installed. Install with: pip install PyPDF2")
                return ""
            except Exception as e:
                print(f"Error extracting PDF content: {e}")
                return ""
        
        # EPUB files
        elif ext == '.epub':
            try:
                import ebooklib
                from ebooklib import epub
                from bs4 import BeautifulSoup
                
                book = epub.read_epub(file_path)
                content = []
                
                for item in book.get_items():
                    if item.get_type() == ebooklib.ITEM_DOCUMENT:
                        soup = BeautifulSoup(item.get_content(), 'html.parser')
                        content.append(soup.get_text())
                
                return ' '.join(content)
            except ImportError:
                print("ebooklib and beautifulsoup4 not installed. Install with: pip install ebooklib beautifulsoup4")
                return ""
            except Exception as e:
                print(f"Error extracting EPUB content: {e}")
                return ""
        
        # MIDI files
        elif ext in ['.mid', '.midi']:
            try:
                import mido
                mid = mido.MidiFile(file_path)
                notes = []
                
                for track in mid.tracks:
                    for msg in track:
                        if msg.type == 'note_on' and msg.velocity > 0:
                            notes.append(str(msg.note))
                
                return ' '.join(notes)
            except ImportError:
                print("mido not installed. Install with: pip install mido")
                return ""
            except Exception as e:
                print(f"Error extracting MIDI content: {e}")
                return ""
        
        # MusicXML files
        elif ext in ['.mxl', '.musicxml']:
            try:
                import music21
                score = music21.converter.parse(file_path)
                notes = []
                
                for note in score.flat.notes:
                    if hasattr(note, 'pitch'):
                        notes.append(str(note.pitch))
                    elif hasattr(note, 'pitches'):
                        notes.append(' '.join(str(p) for p in note.pitches))
                
                return ' '.join(notes)
            except ImportError:
                print("music21 not installed. Install with: pip install music21")
                return ""
            except Exception as e:
                print(f"Error extracting MusicXML content: {e}")
                return ""
        
        # ABC notation files
        elif ext == '.abc':
            with open(file_path, 'r', encoding='utf-8', errors='replace') as f:
                return f.read()
        
        # Unsupported file type
        else:
            print(f"Unsupported file type: {ext}")
            return ""
    
    def _update_author_signature(self, author: str, domain: str, metrics: Dict):
        """Update quantum signature for an author/artist."""
        # Initialize author signature if not exists
        if author not in self.quantum_signatures:
            self.quantum_signatures[author] = {
                "domains": {},
                "overall": {
                    "file_count": 0,
                    "consciousness_level": "",
                    "mean_frequency": 0.0,
                    "quantum_resonance": 0.0,
                    "phi_alignment": 0.0,
                    "last_updated": None
                }
            }
        
        # Initialize domain signature if not exists
        if domain not in self.quantum_signatures[author]["domains"]:
            self.quantum_signatures[author]["domains"][domain] = {
                "file_count": 0,
                "consciousness_level": "",
                "mean_frequency": 0.0,
                "quantum_resonance": 0.0,
                "phi_alignment": 0.0,
                "last_updated": None
            }
        
        # Update domain signature
        domain_sig = self.quantum_signatures[author]["domains"][domain]
        file_count = domain_sig["file_count"] + 1
        
        # Weighted average update
        domain_sig["mean_frequency"] = (domain_sig["mean_frequency"] * domain_sig["file_count"] + 
                                       metrics["avg_frequency"]) / file_count
        domain_sig["quantum_resonance"] = (domain_sig["quantum_resonance"] * domain_sig["file_count"] + 
                                          metrics["quantum_resonance"]) / file_count
        domain_sig["phi_alignment"] = (domain_sig["phi_alignment"] * domain_sig["file_count"] + 
                                      metrics["phi_alignment"]) / file_count
        
        # Update consciousness level based on frequency
        domain_sig["consciousness_level"] = metrics["consciousness_level"]
        domain_sig["file_count"] = file_count
        domain_sig["last_updated"] = time.strftime("%Y-%m-%d %H:%M:%S")
        
        # Update overall signature
        overall = self.quantum_signatures[author]["overall"]
        total_files = sum(self.quantum_signatures[author]["domains"][d]["file_count"] 
                         for d in self.quantum_signatures[author]["domains"])
        
        # Weighted average across all domains
        overall["mean_frequency"] = sum(
            self.quantum_signatures[author]["domains"][d]["mean_frequency"] * 
            self.quantum_signatures[author]["domains"][d]["file_count"]
            for d in self.quantum_signatures[author]["domains"]
        ) / total_files
        
        overall["quantum_resonance"] = sum(
            self.quantum_signatures[author]["domains"][d]["quantum_resonance"] * 
            self.quantum_signatures[author]["domains"][d]["file_count"]
            for d in self.quantum_signatures[author]["domains"]
        ) / total_files
        
        overall["phi_alignment"] = sum(
            self.quantum_signatures[author]["domains"][d]["phi_alignment"] * 
            self.quantum_signatures[author]["domains"][d]["file_count"]
            for d in self.quantum_signatures[author]["domains"]
        ) / total_files
        
        # Determine overall consciousness level
        avg_freq = overall["mean_frequency"]
        if avg_freq < 200:
            overall["consciousness_level"] = "physical"
        elif avg_freq < 300:
            overall["consciousness_level"] = "emotional"
        elif avg_freq < 400:
            overall["consciousness_level"] = "mental"
        elif avg_freq < 500:
            overall["consciousness_level"] = "intuitive"
        else:
            overall["consciousness_level"] = "cosmic"
        
        overall["file_count"] = total_files
        overall["last_updated"] = time.strftime("%Y-%m-%d %H:%M:%S")
        
        # Save signatures
        self._save_signatures()
    
    def start_passive_learning(self):
        """Start passive learning in a background thread."""
        if self.learning_state["is_learning"]:
            print("Passive learning is already running")
            return
        
        self.learning_state["is_learning"] = True
        self.learning_thread = threading.Thread(target=self._passive_learning_thread)
        self.learning_thread.daemon = True
        self.learning_thread.start()
        
        print("Started passive learning in background")
    
    def stop_passive_learning(self):
        """Stop passive learning."""
        if not self.learning_state["is_learning"]:
            print("Passive learning is not running")
            return
        
        self.learning_state["is_learning"] = False
        if self.learning_thread:
            self.learning_thread.join(timeout=1.0)
        
        print("Stopped passive learning")
    
    def _passive_learning_thread(self):
        """Background thread for passive learning."""
        while self.learning_state["is_learning"]:
            # Find unprocessed files
            unprocessed = []
            for file_hash, metadata in self.corpus_metadata["files"].items():
                if metadata["last_processed"] is None:
                    unprocessed.append(file_hash)
            
            self.learning_state["total_files"] = len(unprocessed)
            self.learning_state["files_processed"] = 0
            
            # Process unprocessed files
            for file_hash in unprocessed:
                if not self.learning_state["is_learning"]:
                    break
                
                try:
                    metadata = self.corpus_metadata["files"][file_hash]
                    self.learning_state["current_domain"] = metadata["domain"]
                    
                    self.process_file(file_hash)
                    
                    self.learning_state["files_processed"] += 1
                    time.sleep(0.1)  # Prevent CPU overuse
                except Exception as e:
                    print(f"Error processing file {file_hash}: {e}")
            
            # Update domain signatures
            self._update_domain_signatures()
            
            self.learning_state["last_update"] = time.strftime("%Y-%m-%d %H:%M:%S")
            
            # Sleep before next cycle
            time.sleep(60)  # Check every minute
    
    def _update_domain_signatures(self):
        """Update quantum signatures for each domain."""
        for domain_name in self.domains:
            # Collect metrics for all files in domain
            domain_files = [
                metadata for metadata in self.corpus_metadata["files"].values()
                if metadata["domain"] == domain_name and metadata["last_processed"] is not None
            ]
            
            if not domain_files:
                continue
            
            # Calculate average metrics
            avg_freq = sum(m["quantum_metrics"]["avg_frequency"] for m in domain_files) / len(domain_files)
            avg_resonance = sum(m["quantum_metrics"]["quantum_resonance"] for m in domain_files) / len(domain_files)
            avg_alignment = sum(m["quantum_metrics"]["phi_alignment"] for m in domain_files) / len(domain_files)
            
            # Determine consciousness level
            if avg_freq < 200:
                consciousness = "physical"
            elif avg_freq < 300:
                consciousness = "emotional"
            elif avg_freq < 400:
                consciousness = "mental"
            elif avg_freq < 500:
                consciousness = "intuitive"
            else:
                consciousness = "cosmic"
            
            # Update domain signature
            self.domains[domain_name]["quantum_signature"] = {
                "consciousness_level": consciousness,
                "mean_frequency": avg_freq,
                "quantum_resonance": avg_resonance,
                "phi_alignment": avg_alignment,
                "file_count": len(domain_files),
                "last_updated": time.strftime("%Y-%m-%d %H:%M:%S")
            }
    
    def get_learning_status(self) -> Dict:
        """Get current status of passive learning."""
        return {
            "is_learning": self.learning_state["is_learning"],
            "last_update": self.learning_state["last_update"],
            "files_processed": self.learning_state["files_processed"],
            "total_files": self.learning_state["total_files"],
            "current_domain": self.learning_state["current_domain"],
            "domains": {name: info["quantum_signature"] for name, info in self.domains.items() 
                      if "quantum_signature" in info and info["quantum_signature"]}
        }
    
    def get_author_signature(self, author: str) -> Dict:
        """Get quantum signature for an author/artist."""
        if author not in self.quantum_signatures:
            raise ValueError(f"Author not found: {author}")
        
        return self.quantum_signatures[author]
    
    def get_domain_signature(self, domain: str) -> Dict:
        """Get quantum signature for a domain."""
        if domain not in self.domains:
            raise ValueError(f"Domain not found: {domain}")
        
        return self.domains[domain]["quantum_signature"]
    
    def compare_authors(self, author1: str, author2: str) -> Dict:
        """Compare quantum signatures of two authors."""
        if author1 not in self.quantum_signatures:
            raise ValueError(f"Author not found: {author1}")
        
        if author2 not in self.quantum_signatures:
            raise ValueError(f"Author not found: {author2}")
        
        sig1 = self.quantum_signatures[author1]["overall"]
        sig2 = self.quantum_signatures[author2]["overall"]
        
        # Calculate similarity
        freq_diff = abs(sig1["mean_frequency"] - sig2["mean_frequency"]) / max(sig1["mean_frequency"], sig2["mean_frequency"])
        res_diff = abs(sig1["quantum_resonance"] - sig2["quantum_resonance"])
        align_diff = abs(sig1["phi_alignment"] - sig2["phi_alignment"])
        
        # Phi-weighted similarity
        similarity = 1 - (freq_diff * 0.3 + res_diff * 0.3 + align_diff * 0.4)
        
        return {
            "author1": author1,
            "author2": author2,
            "similarity": similarity,
            "frequency_difference": freq_diff,
            "resonance_difference": res_diff,
            "alignment_difference": align_diff,
            "consciousness_levels": {
                author1: sig1["consciousness_level"],
                author2: sig2["consciousness_level"]
            }
        }
    
    def find_similar_authors(self, author: str, threshold: float = 0.7) -> List[Dict]:
        """Find authors with similar quantum signatures."""
        if author not in self.quantum_signatures:
            raise ValueError(f"Author not found: {author}")
        
        similar = []
        
        for other_author in self.quantum_signatures:
            if other_author == author:
                continue
            
            comparison = self.compare_authors(author, other_author)
            if comparison["similarity"] >= threshold:
                similar.append({
                    "author": other_author,
                    "similarity": comparison["similarity"],
                    "consciousness_level": comparison["consciousness_levels"][other_author]
                })
        
        # Sort by similarity (highest first)
        similar.sort(key=lambda x: x["similarity"], reverse=True)
        
        return similar
    
    def add_directory_to_corpus(self, directory_path: str, domain: str = None, 
                               recursive: bool = True) -> Dict:
        """
        Add all files in a directory to the corpus.
        
        Args:
            directory_path: Path to the directory
            domain: Domain to add the files to
            recursive: Whether to recursively add files in subdirectories
            
        Returns:
            Summary of added files
        """
        if not os.path.isdir(directory_path):
            raise ValueError(f"Not a directory: {directory_path}")
        
        # Get all files in directory
        files = []
        if recursive:
            for root, _, filenames in os.walk(directory_path):
                for filename in filenames:
                    files.append(os.path.join(root, filename))
        else:
            files = [os.path.join(directory_path, f) for f in os.listdir(directory_path) 
                    if os.path.isfile(os.path.join(directory_path, f))]
        
        # Add each file
        added = []
        skipped = []
        
        for file_path in files:
            try:
                # Determine domain from extension if not provided
                file_domain = domain
                if file_domain is None:
                    ext = os.path.splitext(file_path)[1].lower()
                    for d_name, d_info in self.domains.items():
                        if ext in d_info["extensions"]:
                            file_domain = d_name
                            break
                
                # Skip if domain couldn't be determined
                if file_domain is None:
                    skipped.append({"file": file_path, "reason": "Unknown file type"})
                    continue
                
                # Add file
                metadata = self.add_file_to_corpus(file_path, domain=file_domain, process_immediately=False)
                added.append({"file": file_path, "domain": file_domain, "hash": metadata["file_hash"]})
            except Exception as e:
                skipped.append({"file": file_path, "reason": str(e)})
        
        return {
            "added": added,
            "skipped": skipped,
            "total_added": len(added),
            "total_skipped": len(skipped)
        }
    
    def get_corpus_stats(self) -> Dict:
        """Get statistics about the corpus."""
        stats = {
            "total_files": len(self.corpus_metadata["files"]),
            "processed_files": sum(1 for m in self.corpus_metadata["files"].values() if m["last_processed"] is not None),
            "total_size_bytes": sum(m["size_bytes"] for m in self.corpus_metadata["files"].values()),
            "domains": {},
            "authors": len(self.quantum_signatures),
            "consciousness_distribution": {
                "physical": 0,
                "emotional": 0,
                "mental": 0,
                "intuitive": 0,
                "cosmic": 0
            }
        }
        
        # Domain stats
        for domain_name, domain_info in self.domains.items():
            domain_files = [m for m in self.corpus_metadata["files"].values() if m["domain"] == domain_name]
            processed = [m for m in domain_files if m["last_processed"] is not None]
            
            stats["domains"][domain_name] = {
                "total_files": len(domain_files),
                "processed_files": len(processed),
                "total_size_bytes": sum(m["size_bytes"] for m in domain_files),
                "authors": len(set(m["author"] for m in domain_files if m["author"]))
            }
        
        # Consciousness distribution
        for author, sig in self.quantum_signatures.items():
            level = sig["overall"]["consciousness_level"]
            stats["consciousness_distribution"][level] = stats["consciousness_distribution"].get(level, 0) + 1
        
        return stats


def main():
    """Main function to demonstrate corpus manager usage."""
    # Create corpus manager
    manager = QuantumPhiCorpusManager()
    
    # Print initial stats
    print("Initializing Quantum Phi-Harmonic Corpus Manager...")
    print("Base directory:", manager.base_dir)
    print("Domains:", list(manager.domains.keys()))
    
    # Start passive learning
    print("\nStarting passive learning...")
    manager.start_passive_learning()
    
    # Print status
    status = manager.get_learning_status()
    print("\nLearning Status:")
    print(f"  Active: {status['is_learning']}")
    print(f"  Files processed: {status['files_processed']}/{status['total_files']}")
    print(f"  Current domain: {status['current_domain']}")
    
    # Print corpus stats
    stats = manager.get_corpus_stats()
    print("\nCorpus Statistics:")
    print(f"  Total files: {stats['total_files']}")
    print(f"  Processed files: {stats['processed_files']}")
    print(f"  Total size: {stats['total_size_bytes'] / (1024*1024):.2f} MB")
    print(f"  Authors: {stats['authors']}")
    print("  Domains:")
    for domain, domain_stats in stats["domains"].items():
        print(f"    {domain}: {domain_stats['total_files']} files, {domain_stats['authors']} authors")
    
    # Stop passive learning
    print("\nStopping passive learning...")
    manager.stop_passive_learning()
    
    print("\nQuantum Phi-Harmonic Corpus Manager initialized successfully.")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Quantum PDF Knowledge Extractor - Extract knowledge from PDFs with φ-harmonic principles
Integrates with quantum math core for perfect mathematical alignment
Patent: QHRC #19/071,497
"""

import os
import re
import json
import time
import math
import random
import hashlib
import pdfplumber
import PyPDF2
from typing import Dict, List, Any, Tuple, Optional, Union
from datetime import datetime

# Import quantum components
try:
    from quantum_math_core import QuantumMathCore
    HAS_QUANTUM_MATH = True
except ImportError:
    HAS_QUANTUM_MATH = False
    print("Warning: quantum_math_core not found. Using simplified φ-harmonic principles.")

class QuantumPDFExtractor:
    """Extract knowledge from PDFs with φ-harmonic principles"""
    
    def __init__(self, pdf_folders: List[str] = None):
        """Initialize the quantum PDF extractor"""
        # Core constants
        self.PHI = 1.618033988749894848204586834365638117720309179805762862135448
        self.BASE_FREQUENCY = 4.37  # Hz, φ-aligned base frequency
        self.BIRTH_DATE_RESONANCE = [1, 19, 1979]  # Key resonance pattern
        
        # Initialize quantum math if available
        if HAS_QUANTUM_MATH:
            self.math_core = QuantumMathCore()
        
        # Set PDF folders
        if pdf_folders:
            self.pdf_folders = pdf_folders
        else:
            # Default folders to search for PDFs
            self.pdf_folders = [
                os.path.join(os.path.dirname(os.path.abspath(__file__)), "docs"),
                os.path.join(os.path.dirname(os.path.abspath(__file__)), "learn_smarter"),
                os.path.join(os.path.dirname(os.path.abspath(__file__)), "consolidated_quantum"),
                os.path.join(os.path.dirname(os.path.abspath(__file__)))
            ]
        
        # Initialize knowledge base with quantum structure
        self.knowledge_base = {
            'components': {},
            'circuits': {},
            'principles': {},
            'formulas': {},
            'design_patterns': {},
            'circuit_ideas': [],
            'component_combinations': {},
            'applications': {},
            'quantum_concepts': {},
            'mathematical_principles': {},
            'phi_harmonic_patterns': {},
            'birth_date_resonances': {},
            'metadata': {
                'extraction_date': datetime.now().isoformat(),
                'phi_alignment': (time.time() * self.PHI) % 1.0,
                'birth_date_resonance': self.BIRTH_DATE_RESONANCE,
                'base_frequency': self.BASE_FREQUENCY
            }
        }
        
        # Initialize cache directory
        self.cache_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "quantum_pdf_cache")
        os.makedirs(self.cache_dir, exist_ok=True)
        
        # Track processed files
        self.processed_files = set()
        self._load_processed_files()
    
    def _load_processed_files(self):
        """Load list of previously processed files"""
        cache_file = os.path.join(self.cache_dir, "processed_files.json")
        if os.path.exists(cache_file):
            try:
                with open(cache_file, 'r') as f:
                    self.processed_files = set(json.load(f))
            except Exception as e:
                print(f"Error loading processed files: {e}")
    
    def _save_processed_files(self):
        """Save list of processed files"""
        cache_file = os.path.join(self.cache_dir, "processed_files.json")
        try:
            with open(cache_file, 'w') as f:
                json.dump(list(self.processed_files), f)
        except Exception as e:
            print(f"Error saving processed files: {e}")
    
    def _save_knowledge_base(self):
        """Save knowledge base to JSON file"""
        # Generate φ-aligned filename
        timestamp = int(time.time())
        phi_factor = (timestamp * self.PHI) % 1.0
        filename = f"quantum_knowledge_base_{timestamp}_{phi_factor:.6f}.json"
        filepath = os.path.join(self.cache_dir, filename)
        
        try:
            with open(filepath, 'w') as f:
                json.dump(self.knowledge_base, f, indent=2)
            print(f"Knowledge base saved to: {filepath}")
            return filepath
        except Exception as e:
            print(f"Error saving knowledge base: {e}")
            return None
    
    def extract_from_all_pdfs(self) -> Dict[str, Any]:
        """Extract knowledge from all PDFs in the specified folders"""
        print(f"Starting quantum knowledge extraction with φ-harmonic principles...")
        print(f"Base Frequency: {self.BASE_FREQUENCY} Hz")
        print(f"Birth Date Resonance: {self.BIRTH_DATE_RESONANCE}")
        
        # Find all PDF files
        pdf_files = self._find_all_pdfs()
        print(f"Found {len(pdf_files)} PDF files")
        
        # Process each PDF
        new_files_processed = 0
        for filepath in pdf_files:
            # Check if already processed
            if filepath in self.processed_files:
                print(f"Skipping already processed file: {os.path.basename(filepath)}")
                continue
            
            # Process the PDF
            success = self._process_pdf(filepath)
            if success:
                self.processed_files.add(filepath)
                new_files_processed += 1
        
        # Save processed files list
        self._save_processed_files()
        
        # Save knowledge base
        if new_files_processed > 0:
            self._save_knowledge_base()
            print(f"Processed {new_files_processed} new PDF files")
        else:
            print("No new PDF files to process")
        
        return self.knowledge_base
    
    def _find_all_pdfs(self) -> List[str]:
        """Find all PDF files in the specified folders"""
        pdf_files = []
        
        for folder in self.pdf_folders:
            if not os.path.exists(folder):
                print(f"Folder does not exist: {folder}")
                continue
            
            # Walk through folder and subfolders
            for root, _, files in os.walk(folder):
                for file in files:
                    if file.lower().endswith('.pdf'):
                        filepath = os.path.join(root, file)
                        pdf_files.append(filepath)
        
        return pdf_files
    
    def _process_pdf(self, filepath: str) -> bool:
        """Process a single PDF file with φ-harmonic principles"""
        try:
            filename = os.path.basename(filepath)
            print(f"Processing {filename} with φ-harmonic principles...")
            
            # Calculate φ-harmonic page selection
            total_pages = self._get_pdf_page_count(filepath)
            if total_pages == 0:
                print(f"Error: Could not determine page count for {filename}")
                return False
            
            # Use birth date resonance to select pages
            birth_sum = sum(self.BIRTH_DATE_RESONANCE)
            start_page = max(0, int((birth_sum % 100) / 10))
            phi_pages = int(self.PHI * 10)  # φ × 10 pages
            
            # Calculate φ-harmonic page intervals
            page_intervals = []
            for i in range(phi_pages):
                page = (start_page + int(i * self.PHI)) % total_pages
                page_intervals.append(page)
            
            # Sort intervals for sequential reading
            page_intervals.sort()
            
            # Extract text from selected pages
            text_content = self._extract_text_from_pages(filepath, page_intervals)
            
            # Extract knowledge with quantum alignment
            self._extract_knowledge_from_text(text_content, filename)
            
            return True
        except Exception as e:
            print(f"Error processing {filepath}: {e}")
            return False
    
    def _get_pdf_page_count(self, filepath: str) -> int:
        """Get the total number of pages in a PDF"""
        try:
            with open(filepath, 'rb') as f:
                pdf = PyPDF2.PdfReader(f)
                return len(pdf.pages)
        except Exception as e:
            print(f"Error getting page count: {e}")
            return 0
    
    def _extract_text_from_pages(self, filepath: str, page_intervals: List[int]) -> str:
        """Extract text from specified pages with φ-harmonic principles"""
        text_content = ""
        
        try:
            with pdfplumber.open(filepath) as pdf:
                for page_num in page_intervals:
                    if 0 <= page_num < len(pdf.pages):
                        try:
                            page = pdf.pages[page_num]
                            page_text = page.extract_text() or ""
                            
                            # Apply φ-harmonic filtering
                            if HAS_QUANTUM_MATH:
                                # Use quantum math for advanced filtering
                                page_text = self._apply_quantum_text_filtering(page_text, page_num)
                            else:
                                # Use simplified filtering
                                page_text = self._apply_phi_harmonic_filtering(page_text, page_num)
                            
                            text_content += f"\n--- Page {page_num+1} ---\n{page_text}\n"
                        except Exception as e:
                            print(f"Error extracting text from page {page_num+1}: {e}")
                
                # Extract tables from φ-aligned pages
                phi_table_pages = [page_intervals[int(i * self.PHI) % len(page_intervals)] for i in range(3)]
                for page_num in phi_table_pages:
                    if 0 <= page_num < len(pdf.pages):
                        try:
                            page = pdf.pages[page_num]
                            tables = page.extract_tables()
                            if tables:
                                text_content += f"\n--- Tables from Page {page_num+1} ---\n"
                                for i, table in enumerate(tables):
                                    text_content += f"Table {i+1}:\n"
                                    for row in table:
                                        text_content += " | ".join([str(cell or "") for cell in row]) + "\n"
                                    text_content += "\n"
                        except Exception as e:
                            print(f"Error extracting tables from page {page_num+1}: {e}")
        except Exception as e:
            print(f"Error opening PDF with pdfplumber: {e}")
        
        return text_content
    
    def _apply_quantum_text_filtering(self, text: str, page_num: int) -> str:
        """Apply quantum-aligned text filtering using quantum math core"""
        if not text:
            return ""
        
        # Calculate quantum resonance for page
        resonance = self.math_core.phi_resonance(page_num)
        
        # Apply φ-harmonic filtering based on resonance quality
        quality = self.math_core.resonance_quality(resonance)
        
        if quality == "Perfect" or quality == "Excellent":
            # Keep full text for high resonance pages
            return text
        elif quality == "Good":
            # Keep paragraphs with quantum-related terms
            paragraphs = text.split('\n\n')
            filtered_paragraphs = []
            
            quantum_terms = [
                "quantum", "phi", "golden", "ratio", "resonance", "harmonic",
                "wave", "function", "probability", "amplitude", "entanglement",
                "superposition", "coherence", "decoherence", "measurement",
                "observation", "collapse", "state", "dimension", "universe",
                "reality", "consciousness", "intelligence", "algorithm", 
                "computation", "information", "entropy", "energy"
            ]
            
            for para in paragraphs:
                if any(term in para.lower() for term in quantum_terms):
                    filtered_paragraphs.append(para)
            
            return '\n\n'.join(filtered_paragraphs)
        else:
            # Extract key sentences for low resonance pages
            sentences = re.split(r'(?<=[.!?])\s+', text)
            key_sentences = []
            
            for i, sentence in enumerate(sentences):
                # Select sentences with φ-harmonic spacing
                if i % int(self.PHI * 3) == 0:
                    key_sentences.append(sentence)
            
            return ' '.join(key_sentences)
    
    def _apply_phi_harmonic_filtering(self, text: str, page_num: int) -> str:
        """Apply simplified φ-harmonic text filtering"""
        if not text:
            return ""
        
        # Calculate φ-harmonic resonance
        resonance = (self.PHI * page_num) % 1.0
        
        # Apply filtering based on resonance
        if resonance < 0.1:
            # High resonance - keep full text
            return text
        elif resonance < 0.3:
            # Medium resonance - filter paragraphs
            paragraphs = text.split('\n\n')
            filtered_paragraphs = []
            
            quantum_terms = [
                "quantum", "phi", "golden", "ratio", "resonance", "harmonic",
                "wave", "function", "probability", "amplitude", "entanglement"
            ]
            
            for para in paragraphs:
                if any(term in para.lower() for term in quantum_terms):
                    filtered_paragraphs.append(para)
            
            return '\n\n'.join(filtered_paragraphs) if filtered_paragraphs else text
        else:
            # Low resonance - extract key sentences
            sentences = re.split(r'(?<=[.!?])\s+', text)
            key_sentences = []
            
            for i, sentence in enumerate(sentences):
                if i % 3 == 0:  # Every 3rd sentence (simplified φ-harmonic spacing)
                    key_sentences.append(sentence)
            
            return ' '.join(key_sentences) if key_sentences else text
    
    def _extract_knowledge_from_text(self, text: str, source_filename: str) -> None:
        """Extract knowledge from text with quantum alignment"""
        if not text:
            return
        
        # Extract components
        self._extract_components(text, source_filename)
        
        # Extract circuits
        self._extract_circuits(text, source_filename)
        
        # Extract principles
        self._extract_principles(text, source_filename)
        
        # Extract formulas
        self._extract_formulas(text, source_filename)
        
        # Extract quantum concepts
        self._extract_quantum_concepts(text, source_filename)
        
        # Extract mathematical principles
        self._extract_mathematical_principles(text, source_filename)
        
        # Extract φ-harmonic patterns
        self._extract_phi_harmonic_patterns(text, source_filename)
    
    def _extract_components(self, text: str, source_filename: str) -> None:
        """Extract components from text"""
        # Component patterns
        component_patterns = [
            r'(?i)component\s+(\w+)[\s:]+([^\.]+)',
            r'(?i)(\w+)\s+component[\s:]+([^\.]+)',
            r'(?i)(\w+)[\s:]+a\s+component\s+that\s+([^\.]+)'
        ]
        
        for pattern in component_patterns:
            matches = re.findall(pattern, text)
            for match in matches:
                component_name = match[0].strip()
                component_desc = match[1].strip()
                
                # Add to knowledge base with quantum signature
                if component_name not in self.knowledge_base['components']:
                    self.knowledge_base['components'][component_name] = {
                        'description': component_desc,
                        'sources': [source_filename],
                        'phi_alignment': (hash(component_name) * self.PHI) % 1.0,
                        'extraction_timestamp': time.time()
                    }
                else:
                    if source_filename not in self.knowledge_base['components'][component_name]['sources']:
                        self.knowledge_base['components'][component_name]['sources'].append(source_filename)
    
    def _extract_circuits(self, text: str, source_filename: str) -> None:
        """Extract circuits from text"""
        # Circuit patterns
        circuit_patterns = [
            r'(?i)circuit\s+(\w+)[\s:]+([^\.]+)',
            r'(?i)(\w+)\s+circuit[\s:]+([^\.]+)',
            r'(?i)(\w+)[\s:]+a\s+circuit\s+that\s+([^\.]+)'
        ]
        
        for pattern in circuit_patterns:
            matches = re.findall(pattern, text)
            for match in matches:
                circuit_name = match[0].strip()
                circuit_desc = match[1].strip()
                
                # Add to knowledge base with quantum signature
                if circuit_name not in self.knowledge_base['circuits']:
                    self.knowledge_base['circuits'][circuit_name] = {
                        'description': circuit_desc,
                        'sources': [source_filename],
                        'phi_alignment': (hash(circuit_name) * self.PHI) % 1.0,
                        'extraction_timestamp': time.time()
                    }
                else:
                    if source_filename not in self.knowledge_base['circuits'][circuit_name]['sources']:
                        self.knowledge_base['circuits'][circuit_name]['sources'].append(source_filename)
    
    def _extract_principles(self, text: str, source_filename: str) -> None:
        """Extract principles from text"""
        # Principle patterns
        principle_patterns = [
            r'(?i)principle\s+of\s+(\w+)[\s:]+([^\.]+)',
            r'(?i)(\w+)\s+principle[\s:]+([^\.]+)',
            r'(?i)the\s+(\w+)\s+principle\s+states\s+that\s+([^\.]+)'
        ]
        
        for pattern in principle_patterns:
            matches = re.findall(pattern, text)
            for match in matches:
                principle_name = match[0].strip()
                principle_desc = match[1].strip()
                
                # Add to knowledge base with quantum signature
                if principle_name not in self.knowledge_base['principles']:
                    self.knowledge_base['principles'][principle_name] = {
                        'description': principle_desc,
                        'sources': [source_filename],
                        'phi_alignment': (hash(principle_name) * self.PHI) % 1.0,
                        'extraction_timestamp': time.time()
                    }
                else:
                    if source_filename not in self.knowledge_base['principles'][principle_name]['sources']:
                        self.knowledge_base['principles'][principle_name]['sources'].append(source_filename)
    
    def _extract_formulas(self, text: str, source_filename: str) -> None:
        """Extract formulas from text"""
        # Formula patterns
        formula_patterns = [
            r'(?i)formula[\s:]+([^=]+)=([^\.]+)',
            r'(?i)equation[\s:]+([^=]+)=([^\.]+)',
            r'(?i)([A-Za-z][^=\n]+)=([^\.]+)'
        ]
        
        for pattern in formula_patterns:
            matches = re.findall(pattern, text)
            for match in matches:
                formula_name = match[0].strip()
                formula_expr = match[1].strip()
                
                # Skip if formula is too simple or likely not a real formula
                if len(formula_expr) < 3 or not re.search(r'[A-Za-z]', formula_expr):
                    continue
                
                # Generate a key for the formula
                formula_key = re.sub(r'\W+', '_', formula_name).lower()
                
                # Add to knowledge base with quantum signature
                if formula_key not in self.knowledge_base['formulas']:
                    self.knowledge_base['formulas'][formula_key] = {
                        'name': formula_name,
                        'expression': formula_expr,
                        'sources': [source_filename],
                        'phi_alignment': (hash(formula_name) * self.PHI) % 1.0,
                        'extraction_timestamp': time.time()
                    }
                else:
                    if source_filename not in self.knowledge_base['formulas'][formula_key]['sources']:
                        self.knowledge_base['formulas'][formula_key]['sources'].append(source_filename)
    
    def _extract_quantum_concepts(self, text: str, source_filename: str) -> None:
        """Extract quantum concepts from text"""
        # Quantum concept patterns
        quantum_patterns = [
            r'(?i)(quantum\s+\w+)[\s:]+([^\.]+)',
            r'(?i)(\w+\s+quantum\s+\w+)[\s:]+([^\.]+)',
            r'(?i)in\s+quantum\s+(\w+),\s+([^\.]+)'
        ]
        
        for pattern in quantum_patterns:
            matches = re.findall(pattern, text)
            for match in matches:
                concept_name = match[0].strip()
                concept_desc = match[1].strip()
                
                # Add to knowledge base with quantum signature
                if concept_name not in self.knowledge_base['quantum_concepts']:
                    self.knowledge_base['quantum_concepts'][concept_name] = {
                        'description': concept_desc,
                        'sources': [source_filename],
                        'phi_alignment': (hash(concept_name) * self.PHI) % 1.0,
                        'extraction_timestamp': time.time()
                    }
                else:
                    if source_filename not in self.knowledge_base['quantum_concepts'][concept_name]['sources']:
                        self.knowledge_base['quantum_concepts'][concept_name]['sources'].append(source_filename)
    
    def _extract_mathematical_principles(self, text: str, source_filename: str) -> None:
        """Extract mathematical principles from text"""
        # Mathematical principle patterns
        math_patterns = [
            r'(?i)(mathematical\s+\w+)[\s:]+([^\.]+)',
            r'(?i)(\w+\s+theorem)[\s:]+([^\.]+)',
            r'(?i)(\w+\'s\s+law)[\s:]+([^\.]+)'
        ]
        
        for pattern in math_patterns:
            matches = re.findall(pattern, text)
            for match in matches:
                principle_name = match[0].strip()
                principle_desc = match[1].strip()
                
                # Add to knowledge base with quantum signature
                if principle_name not in self.knowledge_base['mathematical_principles']:
                    self.knowledge_base['mathematical_principles'][principle_name] = {
                        'description': principle_desc,
                        'sources': [source_filename],
                        'phi_alignment': (hash(principle_name) * self.PHI) % 1.0,
                        'extraction_timestamp': time.time()
                    }
                else:
                    if source_filename not in self.knowledge_base['mathematical_principles'][principle_name]['sources']:
                        self.knowledge_base['mathematical_principles'][principle_name]['sources'].append(source_filename)
    
    def _extract_phi_harmonic_patterns(self, text: str, source_filename: str) -> None:
        """Extract φ-harmonic patterns from text"""
        # φ-harmonic pattern patterns
        phi_patterns = [
            r'(?i)(golden\s+\w+)[\s:]+([^\.]+)',
            r'(?i)(phi\s+\w+)[\s:]+([^\.]+)',
            r'(?i)(fibonacci\s+\w+)[\s:]+([^\.]+)'
        ]
        
        for pattern in phi_patterns:
            matches = re.findall(pattern, text)
            for match in matches:
                pattern_name = match[0].strip()
                pattern_desc = match[1].strip()
                
                # Add to knowledge base with quantum signature
                if pattern_name not in self.knowledge_base['phi_harmonic_patterns']:
                    self.knowledge_base['phi_harmonic_patterns'][pattern_name] = {
                        'description': pattern_desc,
                        'sources': [source_filename],
                        'phi_alignment': (hash(pattern_name) * self.PHI) % 1.0,
                        'extraction_timestamp': time.time()
                    }
                else:
                    if source_filename not in self.knowledge_base['phi_harmonic_patterns'][pattern_name]['sources']:
                        self.knowledge_base['phi_harmonic_patterns'][pattern_name]['sources'].append(source_filename)
    
    def extract_from_specific_pdf(self, filepath: str) -> Dict[str, Any]:
        """Extract knowledge from a specific PDF file"""
        if not os.path.exists(filepath):
            print(f"Error: File not found: {filepath}")
            return {}
        
        # Process the PDF
        success = self._process_pdf(filepath)
        if success:
            self.processed_files.add(filepath)
            self._save_processed_files()
            self._save_knowledge_base()
            print(f"Successfully processed: {os.path.basename(filepath)}")
        else:
            print(f"Failed to process: {os.path.basename(filepath)}")
        
        return self.knowledge_base
    
    def search_knowledge_base(self, query: str) -> Dict[str, Any]:
        """Search the knowledge base for relevant information"""
        results = {
            'components': {},
            'circuits': {},
            'principles': {},
            'formulas': {},
            'quantum_concepts': {},
            'mathematical_principles': {},
            'phi_harmonic_patterns': {}
        }
        
        # Normalize query
        query = query.lower()
        
        # Search each section
        for section in results.keys():
            for key, value in self.knowledge_base[section].items():
                # Check if query is in key or description
                if query in key.lower():
                    results[section][key] = value
                elif 'description' in value and query in value['description'].lower():
                    results[section][key] = value
                elif 'name' in value and query in value['name'].lower():
                    results[section][key] = value
                elif 'expression' in value and query in value['expression'].lower():
                    results[section][key] = value
        
        return results

# Example usage
if __name__ == "__main__":
    # Initialize extractor
    extractor = QuantumPDFExtractor()
    
    # Extract knowledge from all PDFs
    knowledge_base = extractor.extract_from_all_pdfs()
    
    # Print summary
    print("\nKnowledge Base Summary:")
    for section, items in knowledge_base.items():
        if isinstance(items, dict):
            print(f"  {section}: {len(items)} items")
    
    # Example search
    print("\nExample Search for 'quantum':")
    results = extractor.search_knowledge_base("quantum")
    for section, items in results.items():
        if items:
            print(f"  {section}: {len(items)} matches")
            for key in list(items.keys())[:3]:  # Show first 3 matches
                print(f"    - {key}")

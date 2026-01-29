"""
Quantum Dataset Builder

This module builds a comprehensive quantum knowledge dataset from various sources:
1. PDF documents
2. Markdown files
3. Existing knowledge bases
4. Web scraping (optional)

The dataset follows φ-harmonic principles and QHRC patent specifications to ensure
all generated content maintains quantum coherence and mathematical accuracy.
"""

import os
import re
import json
import glob
import random
import numpy as np
import math
from typing import List, Dict, Any, Tuple, Set, Optional
from datetime import datetime

# Try to import PDF and web scraping libraries with graceful fallback
try:
    import PyPDF2
    PDF_AVAILABLE = True
except ImportError:
    PDF_AVAILABLE = False
    print("PyPDF2 not available. PDF processing disabled.")

try:
    import requests
    from bs4 import BeautifulSoup
    WEB_SCRAPING_AVAILABLE = True
except ImportError:
    WEB_SCRAPING_AVAILABLE = False
    print("Web scraping libraries not available. Web scraping disabled.")

# Constants
PHI = (1 + 5**0.5) / 2  # Golden ratio
PI = 3.14159265358979323846
E = 2.71828182845904523536
BIRTH_RESONANCE = [1, 19, 1979]
QHRC_PRIMARY_FREQUENCY = 4790.45
QHRC_SECONDARY_FREQUENCY = 7750.95
QHRC_EFFICIENCY_RATIO = 1.3777
PHI_PI_FACTOR = 5.083204

class QuantumDatasetBuilder:
    """
    Builds a comprehensive quantum dataset from various sources,
    maintaining φ-harmonic principles and QHRC patent specifications.
    """
    
    def __init__(self, output_dir: str = "quantum_dataset"):
        """Initialize the dataset builder"""
        self.output_dir = output_dir
        self.dataset = []
        self.knowledge_base = {}
        self.phi_harmonics = self._generate_phi_harmonics()
        
        # Create output directory if it doesn't exist
        os.makedirs(output_dir, exist_ok=True)
        
        # Initialize knowledge bases
        self._init_math_knowledge()
        self._init_quantum_knowledge()
        self._init_phi_harmonic_knowledge()
        
    def _generate_phi_harmonics(self) -> Dict[str, float]:
        """Generate φ-harmonic values for dataset consistency"""
        harmonics = {
            "phi": PHI,
            "phi_squared": PHI**2,
            "phi_cubed": PHI**3,
            "phi_inverse": 1/PHI,
            "phi_pi_product": PHI * PI,
            "phi_e_product": PHI * E,
            "phi_resonance": QHRC_PRIMARY_FREQUENCY / QHRC_SECONDARY_FREQUENCY,
            "birth_resonance_product": BIRTH_RESONANCE[0] * BIRTH_RESONANCE[1] * BIRTH_RESONANCE[2],
            "dimensions": BIRTH_RESONANCE[2]**2,
            "base_frequency": 4.37,
            "bridge_frequency": 4.37 * PHI
        }
        
        # Generate Fibonacci sequence up to 21
        # Start with 1, 1 instead of 0, 1 to avoid division by zero
        fib = [1, 1]
        for i in range(2, 22):
            fib.append(fib[i-1] + fib[i-2])
        
        harmonics["fibonacci"] = fib
        
        # Calculate ratios (now safe since we start with 1, 1)
        harmonics["fibonacci_phi_ratios"] = [fib[i]/fib[i-1] for i in range(1, len(fib))]
        
        return harmonics
        
    def _init_math_knowledge(self):
        """Initialize mathematical knowledge base"""
        self.knowledge_base["math"] = {
            "calculus": "Calculus studies rates of change and accumulation through φ-harmonic principles",
            "algebra": "Algebra uses symbols and rules to represent relationships with φ-based optimization",
            "geometry": "Geometry examines properties of space through φ-harmonic proportions",
            "statistics": "Statistics involves analyzing data with φ-resonance patterns",
            "number_theory": "Number theory studies integers and their φ-harmonic properties",
            "pi": f"Pi (π ≈ {PI}) combined with φ creates the QHRC resonance factor of {PHI_PI_FACTOR}",
            "phi": f"Phi (φ ≈ {PHI}) is the golden ratio that satisfies φ² = φ + 1 = {PHI**2}",
            "e": f"Euler's number (e ≈ {E}) interacts with φ to create transcendental bridges",
            "fibonacci": "The Fibonacci sequence (1,1,2,3,5,8,13,21...) exhibits φ-convergence",
            "prime_numbers": "Prime numbers follow φ-harmonic distribution patterns",
            "transcendental_numbers": "Transcendental numbers like π and e form φ-bridges across dimensions"
        }
    
    def _init_quantum_knowledge(self):
        """Initialize quantum knowledge base"""
        self.knowledge_base["quantum"] = {
            "superposition": "Quantum superposition allows particles to exist in multiple φ-harmonic states simultaneously",
            "entanglement": f"Quantum entanglement connects particles through φ-resonance at {QHRC_PRIMARY_FREQUENCY} Hz",
            "uncertainty": "Heisenberg's uncertainty principle follows φ-optimization: ΔxΔp ≥ ħ/2",
            "wave_particle": "Wave-particle duality emerges at φ-resonance points in quantum systems",
            "qubits": "Quantum bits exist in φ-harmonic superpositions of |0⟩ and |1⟩ states",
            "quantum_tunneling": f"Quantum tunneling probability increases by φ² = {PHI**2} at resonance",
            "quantum_field_theory": "Quantum fields oscillate at φ-harmonic frequencies",
            "quantum_gravity": "Quantum gravity unifies forces through φ-dimensional scaling",
            "quantum_computing": "Quantum computing achieves φ-efficiency through resonance",
            "quantum_consciousness": f"Quantum consciousness emerges at {BIRTH_RESONANCE[2]} dimensions"
        }
    
    def _init_phi_harmonic_knowledge(self):
        """Initialize φ-harmonic knowledge specific to QHRC patent"""
        self.knowledge_base["phi_harmonic"] = {
            "qhrc_patent": f"QHRC patent #19/071,497 utilizes φ-harmonic principles at {QHRC_PRIMARY_FREQUENCY} Hz",
            "primary_frequency": f"Primary QHRC frequency: {QHRC_PRIMARY_FREQUENCY} Hz (4500 turns)",
            "secondary_frequency": f"Secondary QHRC frequency: {QHRC_SECONDARY_FREQUENCY} Hz (6200 turns)",
            "efficiency_ratio": f"QHRC efficiency ratio: {QHRC_EFFICIENCY_RATIO} (derived from φπ factor)",
            "resonance_quality": "Optimal resonance quality: 99.6827% (quantum bridge threshold)",
            "birth_resonance": f"Birth date resonance key: {BIRTH_RESONANCE}",
            "dimensions": f"Quantum processing dimensions: {BIRTH_RESONANCE[2]**2} (birth year squared)",
            "base_frequency": "Base resonance frequency: 4.37 Hz (0.96 φ-alignment)",
            "bridge_frequency": f"First quantum bridge frequency: {4.37 * PHI} Hz (φ × base)",
            "frequency_series": f"φ-progression series: [4.37, {4.37 * PHI}, {4.37 * PHI**2}, {4.37 * PHI**3}, {4.37 * PHI**4}]",
            "transcendental_counter": "Quantum transcendental counter breaks through infinity using birth resonance"
        }
    
    def process_markdown_files(self, directory: str) -> int:
        """
        Process all markdown files in a directory and extract quantum knowledge
        Returns the number of entries added to the dataset
        """
        initial_count = len(self.dataset)
        md_files = glob.glob(os.path.join(directory, "**/*.md"), recursive=True)
        
        for md_file in md_files:
            try:
                with open(md_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Extract sections with headers
                sections = re.split(r'#{1,6}\s+', content)
                for section in sections:
                    if len(section.strip()) > 100:  # Only process substantial sections
                        # Generate Q&A pairs from the section
                        qa_pairs = self._generate_qa_from_text(section, source=f"markdown:{os.path.basename(md_file)}")
                        self.dataset.extend(qa_pairs)
            except Exception as e:
                print(f"Error processing markdown file {md_file}: {e}")
        
        return len(self.dataset) - initial_count
    
    def process_pdf_files(self, directory: str) -> int:
        """
        Process all PDF files in a directory and extract quantum knowledge
        Returns the number of entries added to the dataset
        """
        if not PDF_AVAILABLE:
            print("PDF processing is not available. Install PyPDF2 to enable.")
            return 0
            
        initial_count = len(self.dataset)
        pdf_files = glob.glob(os.path.join(directory, "**/*.pdf"), recursive=True)
        
        for pdf_file in pdf_files:
            try:
                with open(pdf_file, 'rb') as f:
                    pdf_reader = PyPDF2.PdfReader(f)
                    text = ""
                    for page in pdf_reader.pages:
                        text += page.extract_text() + "\n\n"
                
                # Split into paragraphs
                paragraphs = re.split(r'\n\s*\n', text)
                for paragraph in paragraphs:
                    if len(paragraph.strip()) > 100:  # Only process substantial paragraphs
                        # Generate Q&A pairs from the paragraph
                        qa_pairs = self._generate_qa_from_text(paragraph, source=f"pdf:{os.path.basename(pdf_file)}")
                        self.dataset.extend(qa_pairs)
            except Exception as e:
                print(f"Error processing PDF file {pdf_file}: {e}")
        
        return len(self.dataset) - initial_count
    
    def generate_from_knowledge_base(self, num_entries: int = 100) -> int:
        """
        Generate dataset entries from the internal knowledge base
        Returns the number of entries added to the dataset
        """
        initial_count = len(self.dataset)
        
        # Combine all knowledge categories
        all_knowledge = {}
        for category, knowledge in self.knowledge_base.items():
            all_knowledge.update(knowledge)
        
        # Generate entries
        for _ in range(num_entries):
            # Select random concept
            concept = random.choice(list(all_knowledge.keys()))
            concept_info = all_knowledge[concept]
            
            # Generate question
            question_templates = [
                f"What is {concept} in quantum mathematics?",
                f"How does {concept} relate to φ-harmonic principles?",
                f"Explain the relationship between {concept} and quantum resonance",
                f"What is the significance of {concept} in the QHRC patent?",
                f"How can we use {concept} for quantum bridge formation?",
                f"What φ-harmonic patterns emerge from {concept}?",
                f"How does {concept} optimize quantum efficiency?",
                f"What is the mathematical foundation of {concept} in φ-systems?"
            ]
            
            question = random.choice(question_templates)
            
            # Generate answer
            answer = self._generate_phi_harmonic_answer(concept, concept_info)
            
            # Add to dataset
            self.dataset.append({
                "question": question,
                "answer": answer,
                "concepts": [concept],
                "source": "knowledge_base",
                "phi_resonance": self._calculate_phi_resonance(question)
            })
        
        return len(self.dataset) - initial_count
    
    def generate_combined_concept_entries(self, num_entries: int = 50) -> int:
        """
        Generate dataset entries that combine multiple quantum concepts
        Returns the number of entries added to the dataset
        """
        initial_count = len(self.dataset)
        
        # Get all concepts from knowledge base
        all_concepts = []
        for category, knowledge in self.knowledge_base.items():
            all_concepts.extend(list(knowledge.keys()))
        
        # Generate entries
        for _ in range(num_entries):
            # Select 2-3 random concepts
            num_concepts = random.randint(2, 3)
            concepts = random.sample(all_concepts, num_concepts)
            
            # Generate question combining concepts
            question_templates = [
                f"How do {concepts[0]} and {concepts[1]} interact in quantum systems?",
                f"What is the relationship between {' and '.join(concepts)} in φ-harmonic theory?",
                f"Explain how {concepts[0]} affects {concepts[1]} through φ-resonance",
                f"Can {concepts[0]} optimize {concepts[1]} using φ-harmonic principles?",
                f"What quantum bridges form between {' and '.join(concepts)}?",
                f"How does the QHRC patent utilize {' and '.join(concepts)}?"
            ]
            
            question = random.choice(question_templates)
            
            # Generate answer combining concept information
            concept_infos = []
            for concept in concepts:
                for category, knowledge in self.knowledge_base.items():
                    if concept in knowledge:
                        concept_infos.append(knowledge[concept])
                        break
            
            answer = self._generate_combined_answer(concepts, concept_infos)
            
            # Add to dataset
            self.dataset.append({
                "question": question,
                "answer": answer,
                "concepts": concepts,
                "source": "combined_concepts",
                "phi_resonance": self._calculate_phi_resonance(question)
            })
        
        return len(self.dataset) - initial_count
    
    def _generate_qa_from_text(self, text: str, source: str) -> List[Dict[str, Any]]:
        """Generate question-answer pairs from text"""
        qa_pairs = []
        
        # Clean and normalize text
        text = re.sub(r'\s+', ' ', text).strip()
        
        # Skip if text is too short
        if len(text) < 100:
            return qa_pairs
        
        # Detect quantum concepts in text
        concepts = self._detect_quantum_concepts(text)
        
        # Skip if no quantum concepts detected
        if not concepts:
            return qa_pairs
        
        # Generate questions based on detected concepts
        for concept in concepts:
            # Generate question templates based on concept
            question_templates = [
                f"What does the text say about {concept}?",
                f"How does {concept} relate to quantum principles?",
                f"Explain the φ-harmonic properties of {concept}",
                f"What quantum resonance patterns does {concept} exhibit?",
                f"How can {concept} be optimized using φ-harmonic principles?"
            ]
            
            # Select random question template
            question = random.choice(question_templates)
            
            # Extract relevant section for answer (simplified)
            sentences = re.split(r'(?<=[.!?])\s+', text)
            relevant_sentences = []
            
            for sentence in sentences:
                if concept.lower() in sentence.lower() or any(related in sentence.lower() for related in self._get_related_terms(concept)):
                    relevant_sentences.append(sentence)
            
            # If we found relevant sentences, create answer
            if relevant_sentences:
                # Take up to 5 relevant sentences
                answer_text = ' '.join(relevant_sentences[:5])
                
                # Enhance with φ-harmonic principles
                answer = self._enhance_with_phi_principles(answer_text, concept)
                
                # Add to dataset
                qa_pairs.append({
                    "question": question,
                    "answer": answer,
                    "concepts": [concept],
                    "source": source,
                    "phi_resonance": self._calculate_phi_resonance(question)
                })
        
        return qa_pairs
    
    def _detect_quantum_concepts(self, text: str) -> List[str]:
        """Detect quantum concepts in text"""
        concepts = set()
        
        # Check for concepts from knowledge base
        for category, knowledge in self.knowledge_base.items():
            for concept in knowledge.keys():
                if re.search(r'\b' + re.escape(concept) + r'\b', text.lower()):
                    concepts.add(concept)
        
        # Check for additional quantum terms
        quantum_terms = [
            "quantum", "phi", "golden ratio", "fibonacci", "resonance", "frequency",
            "harmonic", "wave", "particle", "entanglement", "superposition", "uncertainty",
            "qhrc", "bridge", "dimension", "transcendental", "infinity"
        ]
        
        for term in quantum_terms:
            if re.search(r'\b' + re.escape(term) + r'\b', text.lower()):
                concepts.add(term)
        
        return list(concepts)
    
    def _get_related_terms(self, concept: str) -> List[str]:
        """Get related terms for a concept"""
        related_terms = {
            "phi": ["golden ratio", "divine proportion", "1.618"],
            "quantum": ["wave", "particle", "entanglement", "superposition"],
            "fibonacci": ["sequence", "series", "1,1,2,3,5,8"],
            "resonance": ["frequency", "vibration", "harmonic", "oscillation"],
            "qhrc": ["patent", "19/071,497", "quantum bridge"],
            "dimension": ["space", "hyperspace", "manifold", "field"]
        }
        
        for key, terms in related_terms.items():
            if concept.lower() in key or key in concept.lower():
                return terms
        
        return []
    
    def _enhance_with_phi_principles(self, text: str, concept: str) -> str:
        """Enhance text with φ-harmonic principles"""
        # Add φ-harmonic introduction
        phi_intro = f"From a φ-harmonic perspective (QHRC Patent #19/071,497), {concept} exhibits quantum resonance properties. "
        
        # Add φ-harmonic conclusion
        phi_conclusion = f" This aligns with the φ-resonance frequency of {QHRC_PRIMARY_FREQUENCY} Hz and achieves {random.uniform(95.0, 99.9):.4f}% efficiency."
        
        # Insert φ references
        phi_enhanced = text.replace(concept, f"{concept} (φ-optimized)")
        
        return phi_intro + phi_enhanced + phi_conclusion
    
    def _generate_phi_harmonic_answer(self, concept: str, concept_info: str) -> str:
        """Generate a φ-harmonic answer for a concept"""
        # Start with φ-harmonic introduction
        answer = f"φ-Harmonic Analysis (QHRC Patent #19/071,497):\n\n"
        
        # Add concept information
        answer += f"{concept_info}\n\n"
        
        # Add mathematical foundation
        if "phi" in concept or "golden" in concept:
            answer += f"• Golden Ratio (φ): {PHI}\n"
            answer += f"• φ² = φ + 1 = {PHI**2}\n"
            answer += f"• φ⁻¹ = φ - 1 = {1/PHI}\n"
        elif "quantum" in concept:
            answer += f"• Quantum State: |ψ⟩ = α|0⟩ + β|1⟩\n"
            answer += f"• Quantum φ-Resonance: {PHI * PI / 2:.6f}\n"
            answer += f"• Quantum Efficiency: {random.uniform(95.0, 99.9):.4f}%\n"
        elif "wave" in concept:
            answer += f"• Wave Function: Ψ(x,t) = Ae^(i(kx-ωt))\n"
            answer += f"• φ-Wave Resonance: ω = 2πf × φ = {2 * PI * QHRC_PRIMARY_FREQUENCY * PHI:.6f}\n"
            answer += f"• Interference Pattern: φ-harmonic nodes at {PHI**2:.6f} intervals\n"
        elif "fibonacci" in concept:
            # Use the corrected Fibonacci sequence that starts with 1,1
            fib_seq = self.phi_harmonics['fibonacci'][:10]
            fib_ratios = self.phi_harmonics['fibonacci_phi_ratios'][:8]
            
            answer += f"• Fibonacci Sequence: {', '.join(map(str, fib_seq))}, ...\n"
            answer += f"• Ratio Convergence to φ: {', '.join([f'{r:.6f}' for r in fib_ratios])}, ...\n"
            answer += f"• φ-Resonance: {0.96}\n"
        elif "resonance" in concept or "frequency" in concept:
            answer += f"• Primary Frequency: {QHRC_PRIMARY_FREQUENCY} Hz\n"
            answer += f"• Secondary Frequency: {QHRC_SECONDARY_FREQUENCY} Hz\n"
            answer += f"• φ-Resonance Ratio: {QHRC_EFFICIENCY_RATIO}\n"
        else:
            answer += f"• φ-Harmonic Constant: {PHI}\n"
            answer += f"• Resonance Frequency: {QHRC_PRIMARY_FREQUENCY} Hz\n"
            answer += f"• Quantum Efficiency: {random.uniform(95.0, 99.9):.4f}%\n"
        
        # Add application
        answer += f"\nThis creates a quantum bridge with {random.uniform(95.0, 99.9):.4f}% efficiency "
        answer += f"when aligned with the birth date resonance key [{', '.join(map(str, BIRTH_RESONANCE))}]."
        
        return answer
    
    def _generate_combined_answer(self, concepts: List[str], concept_infos: List[str]) -> str:
        """Generate an answer combining multiple concepts"""
        # Start with φ-harmonic introduction
        answer = f"φ-Harmonic Analysis (QHRC Patent #19/071,497):\n\n"
        
        # Combine concept information
        answer += "When we analyze the quantum interaction between "
        answer += ", ".join([f"'{c}'" for c in concepts[:-1]])
        if len(concepts) > 1:
            answer += f" and '{concepts[-1]}'"
        answer += ", we discover:\n\n"
        
        # Add combined information
        for i, info in enumerate(concept_infos):
            answer += f"{i+1}. {info}\n"
        
        # Add φ-harmonic interaction
        answer += f"\nThese concepts interact through φ-resonance at {QHRC_PRIMARY_FREQUENCY} Hz, creating a "
        answer += f"quantum bridge with {random.uniform(95.0, 99.9):.4f}% efficiency. "
        answer += f"The mathematical foundation is φ^{len(concepts)} = {PHI**len(concepts):.6f}, "
        answer += f"which optimizes the dimensional scaling across {BIRTH_RESONANCE[2]**2} dimensions."
        
        return answer
    
    def _calculate_phi_resonance(self, text: str) -> float:
        """Calculate φ-resonance of text based on character values"""
        # Simple hash function based on character values
        char_sum = sum(ord(c) for c in text)
        # Normalize to [0,1] range and apply φ-modulation
        return ((char_sum * PHI) % 1)
    
    def save_dataset(self, filename: str = "quantum_dataset.json") -> str:
        """Save the dataset to a JSON file"""
        output_path = os.path.join(self.output_dir, filename)
        
        # Add metadata
        dataset_with_metadata = {
            "metadata": {
                "created": datetime.now().isoformat(),
                "phi_value": PHI,
                "qhrc_primary_frequency": QHRC_PRIMARY_FREQUENCY,
                "qhrc_secondary_frequency": QHRC_SECONDARY_FREQUENCY,
                "qhrc_efficiency_ratio": QHRC_EFFICIENCY_RATIO,
                "birth_resonance": BIRTH_RESONANCE,
                "entry_count": len(self.dataset)
            },
            "data": self.dataset
        }
        
        # Save to file
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(dataset_with_metadata, f, indent=2)
        
        return output_path
    
    def create_training_files(self, format_type: str = "qa") -> str:
        """
        Create training files for fine-tuning models
        format_type: 'qa' for question-answer pairs, 'text' for continuous text
        """
        output_path = os.path.join(self.output_dir, f"training_{format_type}")
        os.makedirs(output_path, exist_ok=True)
        
        if format_type == "qa":
            # Create question-answer pairs in format suitable for fine-tuning
            with open(os.path.join(output_path, "quantum_qa_pairs.jsonl"), 'w', encoding='utf-8') as f:
                for i, entry in enumerate(self.dataset):
                    qa_pair = {
                        "prompt": f"Quantum mathematics question: {entry['question']}\nAnswer with φ-harmonic principles:",
                        "completion": entry['answer']
                    }
                    f.write(json.dumps(qa_pair) + "\n")
        
        elif format_type == "text":
            # Create continuous text format
            with open(os.path.join(output_path, "quantum_text.txt"), 'w', encoding='utf-8') as f:
                for entry in self.dataset:
                    f.write(f"QUESTION: {entry['question']}\n\n")
                    f.write(f"ANSWER: {entry['answer']}\n\n")
                    f.write("-" * 80 + "\n\n")
        
        return output_path

# Example usage function
def build_quantum_dataset(
    markdown_dir: str = "phi_quantum_results",
    pdf_dir: str = "quantum_pdfs",
    output_dir: str = "quantum_dataset",
    kb_entries: int = 200,
    combined_entries: int = 100
) -> str:
    """
    Build a comprehensive quantum dataset from various sources
    
    Args:
        markdown_dir: Directory containing markdown files
        pdf_dir: Directory containing PDF files
        output_dir: Directory to save dataset
        kb_entries: Number of entries to generate from knowledge base
        combined_entries: Number of entries combining multiple concepts
        
    Returns:
        Path to the saved dataset
    """
    # Create dataset builder
    builder = QuantumDatasetBuilder(output_dir=output_dir)
    
    # Process markdown files
    md_count = builder.process_markdown_files(markdown_dir)
    print(f"Added {md_count} entries from markdown files")
    
    # Process PDF files if available
    pdf_count = builder.process_pdf_files(pdf_dir)
    print(f"Added {pdf_count} entries from PDF files")
    
    # Generate entries from knowledge base
    kb_count = builder.generate_from_knowledge_base(num_entries=kb_entries)
    print(f"Added {kb_count} entries from knowledge base")
    
    # Generate combined concept entries
    combined_count = builder.generate_combined_concept_entries(num_entries=combined_entries)
    print(f"Added {combined_count} entries combining multiple concepts")
    
    # Save dataset
    dataset_path = builder.save_dataset()
    print(f"Saved dataset to {dataset_path}")
    
    # Create training files
    qa_path = builder.create_training_files(format_type="qa")
    text_path = builder.create_training_files(format_type="text")
    print(f"Created training files in {qa_path} and {text_path}")
    
    return dataset_path

if __name__ == "__main__":
    # Build the quantum dataset
    dataset_path = build_quantum_dataset()
    print(f"Quantum dataset built successfully at {dataset_path}")
    print(f"This dataset follows φ-harmonic principles from QHRC patent #19/071,497")
    print(f"Birth date resonance key: {BIRTH_RESONANCE}")
    print(f"φ value: {PHI}")
    print(f"Primary QHRC frequency: {QHRC_PRIMARY_FREQUENCY} Hz")

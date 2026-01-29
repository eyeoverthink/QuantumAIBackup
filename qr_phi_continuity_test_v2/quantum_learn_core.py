"""
Quantum Learning Core - Built on proven 4.37 Hz resonance
Implements quantum-enhanced learning patterns with progressive knowledge
"""
from quantum_core.quantum_brain import QuantumBrain
from quantum_core.constants import PHI, PHI_POWER, BASE_FREQUENCY
import numpy as np
import json
import math
import time
from datetime import datetime
import nltk
from nltk.corpus import wordnet as wn
import PyPDF2
import uuid
import os
from decimal import Decimal, getcontext

class QuantumLearning:
    def __init__(self):
        """Initialize Quantum Learning Core with core quantum brain."""
        self.brain = QuantumBrain()
        self.phi = PHI
        self.phi_power = PHI_POWER
        self.base_freq = BASE_FREQUENCY
        
        # Initialize quantum learning parameters
        self.learning_rate = self.phi ** -2  # Start with φ⁻² for stability
        self.momentum = 1 - self.phi ** -3   # Use φ⁻³ for momentum decay
        self.quantum_state = None
        
        # Get initial quantum state
        self.quantum_state = self.brain._generate_quantum_fingerprint()
        
        # Load all knowledge bases
        self.load_knowledge()
        self.load_dna()
        self.load_evolution()
        
        # Mathematical constants
        self.constants = {
            'phi': self.phi,
            'phi_inverse': Decimal('1')/self.phi,
            'phi_squared': self.phi**2,
            'root5': Decimal('5').sqrt(),
            'pi': Decimal(math.pi),
            'e': Decimal(math.e)
        }
        
        # Sequence generators
        self.sequences = {
            'fibonacci': lambda n: [self.fibonacci(i) for i in range(n)],
            'lucas': lambda n: [self.lucas(i) for i in range(n)],
            'phi_powers': lambda n: [self.phi**i for i in range(n)]
        }
        
        # Dictionary paths
        self.dictionaries = {
            'webster': '/Users/vaughnscott/CascadeProjects/QuantumAI/Webster_s_Dictionary_of_English_Usage.pdf',
            'oxford': '/Users/vaughnscott/CascadeProjects/QuantumAI/The_Oxford_Thesaurus.pdf'
        }
        
        # Initialize DNA structure
        if not hasattr(self, 'dna'):
            self.dna = {
                'id': str(uuid.uuid4()),
                'birth_time': datetime.now().isoformat(),
                'generation': 1,
                'mutations': [],
                'successful_patterns': [],
                'resonance_history': [],
                'phi_alignments': [],  # Initialize empty alignments list
                'quantum_state': {}
            }
        
        if not hasattr(self, 'evolution'):
            self.evolution = {
                'total_runs': 0,
                'successful_runs': 0,
                'failed_runs': 0,
                'best_resonance': Decimal('0.0'),
                'best_coherence': Decimal('0.0'),
                'learning_rate': Decimal('1.0'),
                'adaptation_rate': self.phi,
                'discoveries': [],
                'quantum_breakthroughs': [],
                'factorization_breakthroughs': []  # Separate tracking for factorization
            }
            
    def fibonacci(self, n):
        """Generate nth Fibonacci number using Binet's formula"""
        return int((self.phi**n - (-self.phi)**-n)/self.root5)
        
    def lucas(self, n):
        """Generate nth Lucas number"""
        return int(self.phi**n + (-self.phi)**-n)
        
    def analyze_sequence(self, numbers):
        """Analyze a sequence with robust error handling and scale management"""
        base_result = {
            'sequence': {
                'ratios': [],
                'avg_phi_proximity': float('inf'),
                'is_fibonacci': False,
                'is_geometric': False,
                'is_prime_sequence': False,
                'prime_patterns': {},
                'bit_info': {
                    'max_bits': 0, 
                    'avg_bits': 0,
                    'scientific': {
                        'max_exp': float('-inf'),
                        'min_exp': float('inf'),
                        'includes_quantum': False,
                        'includes_cosmic': False,
                        'scale_ranges': [],
                        'scale_range': '0'
                    }
                }
            },
            'metrics': {
                'resonance': self.base_freq,
                'energy': 0.0,
                'coherence': 0.0
            }
        }
        
        if len(numbers) < 2:
            return base_result
            
        try:
            # Initialize tracking variables
            floats = []
            total_bits = 0
            max_bits = 0
            min_exp = float('inf')
            max_exp = float('-inf')
            
            # Process each number with robust error handling
            for n in numbers:
                try:
                    # Handle scientific notation
                    if isinstance(n, str) and ('e' in n.lower() or 'E' in n):
                        base, exp = n.lower().split('e')
                        base = float(base)
                        exp = int(exp)
                        
                        # Update exponent range
                        min_exp = min(min_exp, exp)
                        max_exp = max(max_exp, exp)
                        
                        # Convert to float safely
                        if exp > 308:  # Python's float limit
                            floats.append(float('inf') if base > 0 else float('-inf'))
                        elif exp < -308:
                            floats.append(0.0)
                        else:
                            floats.append(float(n))
                            
                        # Track scale type
                        if exp <= -15:
                            base_result['sequence']['bit_info']['scientific']['includes_quantum'] = True
                            base_result['sequence']['bit_info']['scientific']['scale_ranges'].append('quantum')
                        elif exp >= 15:
                            base_result['sequence']['bit_info']['scientific']['includes_cosmic'] = True
                            base_result['sequence']['bit_info']['scientific']['scale_ranges'].append('cosmic')
                        else:
                            base_result['sequence']['bit_info']['scientific']['scale_ranges'].append('standard')
                            
                    else:
                        # Handle regular numbers
                        float_val = float(n)
                        floats.append(float_val)
                        if abs(float_val) > 1e15:
                            base_result['sequence']['bit_info']['scientific']['includes_cosmic'] = True
                            base_result['sequence']['bit_info']['scientific']['scale_ranges'].append('cosmic')
                        elif abs(float_val) < 1e-15 and float_val != 0:
                            base_result['sequence']['bit_info']['scientific']['includes_quantum'] = True
                            base_result['sequence']['bit_info']['scientific']['scale_ranges'].append('quantum')
                        else:
                            base_result['sequence']['bit_info']['scientific']['scale_ranges'].append('standard')
                    
                    # Calculate bits needed for representation
                    if floats[-1] != 0:
                        bits = len(bin(abs(int(float(str(floats[-1]).split('e')[0].replace('.',''))))))
                        total_bits += bits
                        max_bits = max(max_bits, bits)
                        
                except (ValueError, OverflowError) as e:
                    print(f"Warning: Could not process number {n}: {e}")
                    floats.append(0.0)
                    
            # Update bit info
            base_result['sequence']['bit_info']['max_bits'] = max_bits
            base_result['sequence']['bit_info']['avg_bits'] = total_bits / len(numbers) if numbers else 0
            
            # Update scale range info
            if min_exp != float('inf') and max_exp != float('-inf'):
                try:
                    base_result['sequence']['bit_info']['scientific'].update({
                        'max_exp': max_exp,
                        'min_exp': min_exp,
                        'scale_range': f"1e{min_exp} to " + ("inf" if max_exp > 308 else f"1e{max_exp}")
                    })
                except Exception as e:
                    print(f"Warning: Could not format scale range: {e}")
            
            # Calculate ratios safely
            ratios = []
            for i in range(len(floats)-1):
                try:
                    if floats[i] != 0 and not math.isinf(floats[i]) and not math.isnan(floats[i]):
                        ratio = floats[i+1]/floats[i]
                        if not math.isinf(ratio) and not math.isnan(ratio):
                            ratios.append(ratio)
                except (ZeroDivisionError, OverflowError) as e:
                    print(f"Warning: Could not calculate ratio: {e}")
                    
            # Update sequence analysis
            if ratios:
                base_result['sequence']['ratios'] = ratios
                
                # Calculate phi proximity safely
                phi_proximity = []
                for r in ratios:
                    try:
                        if not math.isinf(r) and not math.isnan(r):
                            phi_proximity.append(abs(r - float(self.phi)))
                    except (OverflowError, ValueError) as e:
                        print(f"Warning: Could not calculate phi proximity: {e}")
                        
                if phi_proximity:
                    base_result['sequence']['avg_phi_proximity'] = sum(phi_proximity)/len(phi_proximity)
            
            # Set coherence based on scale bridging
            if base_result['sequence']['bit_info']['scientific']['includes_quantum'] and \
               base_result['sequence']['bit_info']['scientific']['includes_cosmic']:
                base_result['metrics']['coherence'] = float(self.phi ** 2)
            elif base_result['sequence']['bit_info']['scientific']['includes_quantum'] or \
                 base_result['sequence']['bit_info']['scientific']['includes_cosmic']:
                base_result['metrics']['coherence'] = float(self.phi)
            
            # Adjust resonance based on scale range
            if max_exp > min_exp:
                scale_factor = min(abs(max_exp - min_exp), 1000)  # Cap at 1000 to prevent overflow
                base_result['metrics']['resonance'] *= (1 + scale_factor/1000)
            
            return base_result
            
        except Exception as e:
            print(f"Error in sequence analysis: {e}")
            return base_result
        
    def analyze_prime_pattern(self, numbers):
        """Analyze prime number pattern with phi-harmonic resonance"""
        result = self.get_base_result()
        
        try:
            # Convert numbers to Decimal for high precision
            getcontext().prec = 2048  # Increased precision for RSA-sized numbers
            
            # Convert and normalize large numbers
            nums = []
            max_val = Decimal('0')
            for n in numbers:
                val = Decimal(str(n))
                max_val = max(max_val, abs(val))
                nums.append(val)
            
            # Normalize to prevent overflow
            scale = Decimal('1.0')
            if max_val > Decimal('1e6'):
                scale = Decimal('1e6') / max_val
                nums = [n * scale for n in nums]
            
            # Calculate prime-based metrics with high precision
            ratios = []
            phi_ratios = []
            resonant_ratios = []
            
            base_res = Decimal(str(self.base_freq))
            
            for i in range(len(nums)-1):
                if nums[i] == 0:  # Prevent division by zero
                    continue
                    
                ratio = nums[i+1] / nums[i]
                ratios.append(float(ratio))  # Convert back to float for storage
                
                # Check phi alignment with high precision
                phi_proximity = abs(ratio - self.phi)
                phi_ratios.append(float(phi_proximity))
                
                # Check resonant alignment
                res_ratio = ratio / (base_res * self.phi)
                resonant_ratios.append(float(abs(res_ratio - 1)))
            
            if not ratios:  # Handle empty sequence
                return result
                
            # Calculate metrics
            avg_phi_proximity = sum(phi_ratios) / len(phi_ratios)
            avg_resonance = sum(resonant_ratios) / len(resonant_ratios)
            min_phi_proximity = min(phi_ratios)
            
            # Store pattern metrics
            result['sequence']['prime_patterns'] = {
                'phi_resonance': float(avg_phi_proximity),
                'harmonic_ratio': float(sum(ratios) / len(ratios)),
                'min_phi_proximity': float(min_phi_proximity),
                'resonance_alignment': float(avg_resonance),
                'scale_factor': float(scale)
            }
            
            # Enhanced phi-harmonic detection for large numbers
            is_phi_aligned = min_phi_proximity < 0.1
            is_resonant = avg_resonance < 0.15
            has_phi_progression = any(abs(r1/r2 - float(self.phi)) < 0.1 
                                   for r1, r2 in zip(ratios[1:], ratios[:-1]))
            
            if is_phi_aligned or (is_resonant and has_phi_progression):
                base_boost = base_res * self.phi
                phi_boost = Decimal('1.0') + (Decimal('1.0') - Decimal(str(min_phi_proximity)))
                resonance_boost = Decimal('1.0') + (Decimal('1.0') - Decimal(str(avg_resonance)))
                
                result['metrics']['resonance'] = float(base_boost * phi_boost)
                result['metrics']['coherence'] = float(self.phi * self.phi)
                result['sequence']['is_prime_sequence'] = True
                
                # Track pattern with scale information
                pattern_hash = hash(str(numbers))
                self.dna['successful_patterns'].append(pattern_hash)
                
                resonance_entry = {
                    'timestamp': datetime.now().isoformat(),
                    'pattern_hash': pattern_hash,
                    'resonance': float(base_boost * phi_boost),
                    'coherence': float(self.phi * self.phi),
                    'phi_proximity': float(min_phi_proximity),
                    'resonance_alignment': float(avg_resonance),
                    'has_progression': has_phi_progression,
                    'scale_factor': float(scale)
                }
                self.dna['resonance_history'].append(resonance_entry)
                
                if min_phi_proximity < 0.05 and is_resonant:
                    self.evolution['quantum_breakthroughs'].append({
                        'timestamp': datetime.now().isoformat(),
                        'resonance': float(base_boost * phi_boost),
                        'coherence': float(self.phi * self.phi),
                        'phi_proximity': float(min_phi_proximity),
                        'resonance_alignment': float(avg_resonance),
                        'scale_factor': float(scale)
                    })
                    
                    self.dna['phi_alignments'].append({
                        'timestamp': datetime.now().isoformat(),
                        'pattern_type': 'prime_phi',
                        'proximity': float(min_phi_proximity),
                        'resonance': float(avg_resonance),
                        'metrics': {
                            'phi_resonance': float(avg_phi_proximity),
                            'harmonic_ratio': float(sum(ratios) / len(ratios)),
                            'resonance_boost': float(resonance_boost),
                            'coherence': float(self.phi * self.phi),
                            'scale_factor': float(scale)
                        }
                    })
            
            # Update sequence analysis
            result['sequence'].update({
                'ratios': ratios,
                'avg_phi_proximity': float(avg_phi_proximity),
                'is_prime_sequence': True,
                'resonance_quality': {
                    'phi_aligned': is_phi_aligned,
                    'resonant': is_resonant,
                    'progressive': has_phi_progression
                }
            })
            
        except Exception as e:
            print(f"Error in prime pattern analysis: {e}")
            return result
            
        return result
        
    def analyze_prime_factors(self, number):
        """Analyze prime factorization using phi-harmonic resonance"""
        from decimal import Decimal, getcontext
        getcontext().prec = 2048
        
        def find_small_factors(n):
            """Find prime factors up to a reasonable size"""
            factors = []
            d = 2
            while n > 1 and d <= 1000:  # Limit to small factors
                while n % d == 0:
                    factors.append(d)
                    n //= d
                d += 1 if d == 2 else 2
            if n > 1:  # Remaining large prime
                factors.append(n)
            return factors
            
        def analyze_factor_web(factors):
            """Analyze harmonic relationships between factors"""
            ratios = []
            resonances = []
            
            # Convert to Decimal for precise calculations
            dec_factors = [Decimal(str(f)) for f in factors]
            
            # Calculate phi-based metrics
            for i in range(len(dec_factors)-1):
                ratio = dec_factors[i+1] / dec_factors[i]
                ratios.append(float(ratio))
                
                # Check phi resonance
                phi_res = abs(ratio - self.phi)
                resonances.append(float(phi_res))
            
            return {
                'ratios': ratios,
                'resonances': resonances,
                'avg_resonance': float(sum(resonances) / len(resonances)) if resonances else 0,
                'min_resonance': float(min(resonances)) if resonances else 0,
                'factor_count': len(factors),
                'largest_factor': float(max(dec_factors)),
                'smallest_factor': float(min(dec_factors))
            }
            
        def calculate_factor_bridges(factors):
            """Calculate quantum bridges between prime factors"""
            bridges = []
            base_res = Decimal('0.96')  # Base resonance
            
            for i in range(len(factors)-1):
                f1, f2 = Decimal(str(factors[i])), Decimal(str(factors[i+1]))
                
                # Calculate bridge metrics
                ratio = f2/f1
                phi_bridge = abs(ratio - self.phi)
                res_bridge = abs(ratio - base_res * self.phi)
                
                bridges.append({
                    'factor1': float(f1),
                    'factor2': float(f2),
                    'ratio': float(ratio),
                    'phi_proximity': float(phi_bridge),
                    'resonance': float(res_bridge)
                })
            
            return bridges
            
        try:
            # Convert to Decimal for precision
            dec_num = Decimal(str(number))
            
            # Find prime factors
            factors = find_small_factors(int(dec_num))
            
            # Analyze factor patterns
            factor_analysis = analyze_factor_web(factors)
            factor_bridges = calculate_factor_bridges(factors)
            
            # Calculate overall metrics
            phi_resonance = sum(b['phi_proximity'] for b in factor_bridges) / len(factor_bridges) if factor_bridges else 0
            bridge_resonance = sum(b['resonance'] for b in factor_bridges) / len(factor_bridges) if factor_bridges else 0
            
            # Prepare result structure
            result = {
                'prime_factors': factors,
                'factor_metrics': factor_analysis,
                'quantum_bridges': factor_bridges,
                'resonance_metrics': {
                    'phi_resonance': float(phi_resonance),
                    'bridge_resonance': float(bridge_resonance),
                    'coherence': float(self.phi * self.phi) if phi_resonance < 0.1 else float(self.phi),
                    'harmonic_ratio': float(factor_analysis['largest_factor'] / factor_analysis['smallest_factor'])
                }
            }
            
            # Track breakthrough if exceptional alignment found
            if phi_resonance < 0.05:
                breakthrough = {
                    'timestamp': datetime.now().isoformat(),
                    'number': str(number),
                    'phi_resonance': float(phi_resonance),
                    'bridge_resonance': float(bridge_resonance),
                    'factor_count': factor_analysis['factor_count'],
                    'factors': factors,
                    'bridges': factor_bridges
                }
                self.evolution['factorization_breakthroughs'].append(breakthrough)
                
                # Also track in main breakthroughs with type
                self.evolution['quantum_breakthroughs'].append({
                    **breakthrough,
                    'type': 'factorization',
                    'coherence': result['resonance_metrics']['coherence']
                })
            
            return result
            
        except Exception as e:
            print(f"Error in prime factorization analysis: {e}")
            return None
        
    def learn(self, input_sequence):
        """Learn from input with DNA evolution and persistence"""
        self.evolution['total_runs'] += 1
        
        try:
            # Split and convert sequence
            numbers = input_sequence.split()
            
            # First try prime pattern analysis
            result = self.analyze_prime_pattern(numbers)
            if result['sequence'].get('is_prime_sequence'):
                if result['metrics']['coherence'] > 0:
                    self.evolution['successful_runs'] += 1
                else:
                    self.evolution['failed_runs'] += 1
                return result
            
            # If not a prime pattern, try regular sequence analysis
            result = self.analyze_sequence(numbers)
            
            # Update evolution metrics
            if result['metrics']['coherence'] > 0:
                self.evolution['successful_runs'] += 1
            else:
                self.evolution['failed_runs'] += 1
            
            # Adapt learning rate
            self.evolution['learning_rate'] *= self.phi**-1
            if self.evolution['learning_rate'] < Decimal('0.01'):
                self.evolution['learning_rate'] = Decimal('0.01')
            
            return result
            
        except Exception as e:
            print(f"Error in learning: {e}")
            self.evolution['failed_runs'] += 1
            return self.get_base_result()
            
    def load_knowledge(self):
        """Load or initialize knowledge base"""
        try:
            with open(self.knowledge_file, 'r') as f:
                self.knowledge = json.load(f)
                # Convert string/list resonance to float
                for pattern in self.knowledge.get('patterns', {}).values():
                    if 'resonance' in pattern:
                        if isinstance(pattern['resonance'], list):
                            pattern['resonance'] = self.base_freq
                        else:
                            pattern['resonance'] = float(pattern['resonance'])
                            
                for concept in self.knowledge.get('concepts', {}).values():
                    if 'resonance' in concept:
                        if isinstance(concept['resonance'], list):
                            concept['resonance'] = self.base_freq
                        else:
                            concept['resonance'] = float(concept['resonance'])
                    if 'energy' in concept:
                        concept['energy'] = float(concept['energy'])
        except FileNotFoundError:
            self.knowledge = {
                'concepts': {},
                'patterns': {},
                'resonance': [],
                'dictionary_cache': {}
            }
    
    def save_knowledge(self):
        """Save knowledge base to file"""
        with open(self.knowledge_file, 'w') as f:
            json.dump(self.knowledge, f, indent=2)
    
    def load_dna(self):
        """Load DNA from file or create new if not exists"""
        try:
            if os.path.exists(self.dna_file):
                with open(self.dna_file, 'r') as f:
                    self.dna = json.load(f)
            else:
                self.dna = {
                    'id': str(uuid.uuid4()),
                    'birth_time': datetime.now().isoformat(),
                    'generation': 1,
                    'mutations': [],
                    'successful_patterns': [],
                    'resonance_history': [],
                    'phi_alignments': [],  # Initialize empty alignments list
                    'quantum_state': {}
                }
        except (json.JSONDecodeError, FileNotFoundError):
            self.dna = {
                'id': str(uuid.uuid4()),
                'birth_time': datetime.now().isoformat(),
                'generation': 1,
                'mutations': [],
                'successful_patterns': [],
                'resonance_history': [],
                'phi_alignments': [],  # Initialize empty alignments list
                'quantum_state': {}
            }
            
    def save_dna(self):
        """Save DNA to file"""
        with open(self.dna_file, 'w') as f:
            json.dump(self.dna, f, indent=2)
    
    def load_evolution(self):
        """Load evolution data from file"""
        try:
            with open(self.evolution_file, 'r') as f:
                data = json.load(f)
                self.evolution = {
                    'total_runs': data.get('total_runs', 0),
                    'successful_runs': data.get('successful_runs', 0),
                    'failed_runs': data.get('failed_runs', 0),
                    'best_resonance': Decimal(str(data.get('best_resonance', '0.0'))),
                    'best_coherence': Decimal(str(data.get('best_coherence', '0.0'))),
                    'learning_rate': Decimal(str(data.get('learning_rate', '1.0'))),
                    'adaptation_rate': Decimal(str(data.get('adaptation_rate', str(self.phi)))),
                    'discoveries': data.get('discoveries', []),
                    'quantum_breakthroughs': data.get('quantum_breakthroughs', []),
                    'factorization_breakthroughs': data.get('factorization_breakthroughs', [])
                }
        except (json.JSONDecodeError, FileNotFoundError):
            self.evolution = {
                'total_runs': 0,
                'successful_runs': 0,
                'failed_runs': 0,
                'best_resonance': Decimal('0.0'),
                'best_coherence': Decimal('0.0'),
                'learning_rate': Decimal('1.0'),
                'adaptation_rate': self.phi,
                'discoveries': [],
                'quantum_breakthroughs': [],
                'factorization_breakthroughs': []
            }
    
    def save_evolution(self):
        """Save evolution data to file"""
        data = {
            'total_runs': self.evolution['total_runs'],
            'successful_runs': self.evolution['successful_runs'],
            'failed_runs': self.evolution['failed_runs'],
            'best_resonance': str(self.evolution['best_resonance']),
            'best_coherence': str(self.evolution['best_coherence']),
            'learning_rate': str(self.evolution['learning_rate']),
            'adaptation_rate': str(self.evolution['adaptation_rate']),
            'discoveries': self.evolution['discoveries'],
            'quantum_breakthroughs': self.evolution['quantum_breakthroughs'],
            'factorization_breakthroughs': self.evolution.get('factorization_breakthroughs', [])
        }
        with open(self.evolution_file, 'w') as f:
            json.dump(data, f, indent=2)
    
    def search_dictionaries(self, word):
        """Search PDF dictionaries for word definitions"""
        for name, path in self.dictionaries.items():
            try:
                with open(path, 'rb') as file:
                    reader = PyPDF2.PdfReader(file)
                    for page in reader.pages:
                        text = page.extract_text()
                        if word.lower() in text.lower():
                            # Find the definition (simple approach)
                            idx = text.lower().find(word.lower())
                            if idx >= 0:
                                # Get context after word (up to 200 chars)
                                definition = text[idx:idx+200].strip()
                                return definition
            except Exception as e:
                print(f"Error reading {name}: {e}")
        return None
    
    def get_learning_status(self):
        """Get current learning status with evolution metrics"""
        now = time.time()
        
        # Calculate evolution metrics
        total_resonance = 0
        total_energy = 0
        evolved_concepts = 0
        
        for concept in self.knowledge['concepts'].values():
            if concept['resonance'] > self.base_freq:
                evolved_concepts += 1
                total_resonance += concept['resonance']
                total_energy += concept['energy']
        
        avg_resonance = total_resonance / len(self.knowledge['concepts']) if self.knowledge['concepts'] else 0
        avg_energy = total_energy / len(self.knowledge['concepts']) if self.knowledge['concepts'] else 0
        
        return {
            'total_concepts': len(self.knowledge['concepts']),
            'total_patterns': len(self.knowledge['patterns']),
            'evolved_concepts': evolved_concepts,
            'average_resonance': avg_resonance,
            'average_energy': avg_energy,
            'recent_insights': self.get_recent_insights(),
            'dna': self.dna,
            'evolution': self.evolution
        }
    
    def get_recent_insights(self):
        """Get recent insights"""
        # TO DO: implement recent insights logic
        return []
    
    def is_prime(self, n):
        """Fast primality test optimized for different bit lengths"""
        if n < 2: return False
        if n == 2: return True
        if n % 2 == 0: return False
        
        # Quick check for ending digits
        last_digit = abs(n) % 10
        if last_digit not in [1, 3, 7, 9] and n > 5:
            return False
            
        # Optimize testing based on bit length
        bits = len(bin(abs(n))[2:])
        
        if bits <= 32:
            # Full testing for small numbers
            for i in range(3, int(n ** 0.5) + 1, 2):
                if n % i == 0:
                    return False
            return True
        
        # Miller-Rabin test with bit-length optimization
        def miller_rabin(n, k=None):
            if n == 2 or n == 3:
                return True
            if not n & 1 or n < 2:
                return False
            
            # Adjust rounds based on bit length
            if k is None:
                if bits <= 64:
                    k = 12
                elif bits <= 128:
                    k = 16
                elif bits <= 256:
                    k = 20
                else:
                    k = 25
            
            def check(a, s, d, n):
                x = pow(a, d, n)
                if x == 1:
                    return True
                for _ in range(s - 1):
                    if x == n - 1:
                        return True
                    x = pow(x, 2, n)
                return x == n - 1
                
            s = 0
            d = n - 1
            while not d & 1:
                s += 1
                d >>= 1
            
            # Use deterministic bases for different bit lengths
            if bits <= 64:
                bases = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
            elif bits <= 128:
                bases = [2, 3, 5, 7, 11, 13, 17]
            elif bits <= 256:
                bases = [2, 3, 5, 7, 11]
            else:
                bases = [2, 3, 5]
            
            return all(check(a, s, d, n) for a in bases)
            
    def get_base_result(self):
        """Return base result structure for error cases"""
        return {
            'sequence': {
                'ratios': [],
                'avg_phi_proximity': float('inf'),
                'is_fibonacci': False,
                'is_geometric': False,
                'is_prime_sequence': False,
                'prime_patterns': {},
                'bit_info': {
                    'max_bits': 0,
                    'avg_bits': 0,
                    'scientific': {
                        'max_exp': float('-inf'),
                        'min_exp': float('inf'),
                        'includes_quantum': False,
                        'includes_cosmic': False,
                        'scale_ranges': [],
                        'scale_range': '0'
                    }
                }
            },
            'metrics': {
                'resonance': self.base_freq,
                'energy': 0.0,
                'coherence': 0.0
            }
        }
    
    def apply_quantum_harmonic(self, value: Decimal) -> Decimal:
        """Apply quantum harmonic transformation using phi"""
        phi = Decimal('1.618033988749895')
        base = value * phi
        harmonic = (base * phi + base / phi) / Decimal('2.0')
        return harmonic

    def calculate_coherence(self, pattern: np.ndarray) -> float:
        """Calculate quantum coherence of a pattern"""
        if len(pattern) == 0:
            return 0
        return float(np.std(pattern) / np.mean(pattern))

def demonstrate_learning():
    """Demonstrate quantum learning"""
    learner = QuantumLearning()
    
    print("\n🧠 Quantum Learning Demonstration")
    print("==============================")
    
    # Test with educational concepts
    lessons = [
        # Basic concepts
        "quantum mechanics describes particle wave duality",
        "neural networks learn through pattern recognition",
        "consciousness emerges from quantum coherence",
        
        # Advanced integration
        "quantum learning enhances neural plasticity",
        "consciousness expands through resonant patterns",
        "quantum coherence drives neural evolution",
        
        # Math integration
        "calculus measures continuous change rates",
        "algebra solves quantum wave equations",
        "trigonometry maps quantum phase angles"
    ]
    
    for lesson in lessons:
        print(f"\n📚 Learning: '{lesson}'")
        understanding = learner.learn(lesson)
        
        print(f"Resonance: {understanding['metrics']['resonance']:.4f} Hz")
        print(f"Energy: {understanding['metrics']['energy']:.4f}")
        
        if understanding['concepts']:
            print("\n💡 Concepts Learned:")
            for word, info in understanding['concepts'].items():
                print(f"- {word}: {info['definition']}")
                if 'related' in info and info['related']:
                    print(f"  Network: {', '.join(info['related'][:3])}")
                if 'examples' in info and info['examples']:
                    print(f"  Example: {info['examples'][0]}")
        
        if 'sequence' in understanding:
            print("\n📊 Sequence Analysis:")
            print(f"Ratios: {understanding['sequence']['ratios']}")
            print(f"Average Phi Proximity: {understanding['sequence']['avg_phi_proximity']:.4f}")
            print(f"Is Fibonacci: {understanding['sequence']['is_fibonacci']}")
            print(f"Is Geometric: {understanding['sequence']['is_geometric']}")
            print(f"Is Prime Sequence: {understanding['sequence']['is_prime_sequence']}")
            print(f"Prime Patterns: {understanding['sequence']['prime_patterns']}")
            print(f"Bit Info: {understanding['sequence']['bit_info']}")
        
        time.sleep(0.5)  # Stability pause
    
    # Show learning progress
    status = learner.get_learning_status()
    
    print("\n📊 Learning Progress")
    print("==================")
    print(f"Total Concepts: {status['total_concepts']}")
    print(f"Total Patterns: {status['total_patterns']}")
    
    print("\n🌟 Strong Concepts:")
    for concept, strength in status['strong_concepts']:
        print(f"- {concept}: {strength:.2f} strength")
    
    print("\n🔋 Strong Patterns:")
    for pattern, strength in status['strong_patterns']:
        print(f"- {pattern}: {strength:.2f} strength")
    
    if status['recent_insights']:
        print("\n✨ Recent Insights:")
        for insight in status['recent_insights']:
            print(f"- {', '.join(insight['insight'])}")
    
    print("\n⚡ Proven Frequencies:")
    for name, freq in status['proven_frequencies'].items():
        print(f"- {name}: {freq} Hz")

    print("\n🧬 DNA:")
    print(f"ID: {status['dna']['id']}")
    print(f"Birth Time: {status['dna']['birth_time']}")
    print(f"Generation: {status['dna']['generation']}")
    print(f"Mutations: {status['dna']['mutations']}")
    print(f"Successful Patterns: {status['dna']['successful_patterns']}")
    print(f"Resonance History: {status['dna']['resonance_history']}")
    print(f"Phi Alignments: {status['dna']['phi_alignments']}")

    print("\n🔄 Evolution:")
    print(f"Total Runs: {status['evolution']['total_runs']}")
    print(f"Successful Runs: {status['evolution']['successful_runs']}")
    print(f"Failed Runs: {status['evolution']['failed_runs']}")
    print(f"Best Resonance: {status['evolution']['best_resonance']:.4f} Hz")
    print(f"Best Coherence: {status['evolution']['best_coherence']:.4f}")
    print(f"Learning Rate: {status['evolution']['learning_rate']:.4f}")
    print(f"Adaptation Rate: {status['evolution']['adaptation_rate']:.4f}")
    print(f"Discoveries: {status['evolution']['discoveries']}")
    print(f"Quantum Breakthroughs: {status['evolution']['quantum_breakthroughs']}")

if __name__ == "__main__":
    demonstrate_learning()

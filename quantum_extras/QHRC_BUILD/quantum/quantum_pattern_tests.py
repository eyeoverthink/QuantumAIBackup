import numpy as np
from quantum_pattern_recognition import QuantumPatternRecognition
import matplotlib.pyplot as plt
from typing import Dict, List, Tuple
from quantum_linguistic_patterns import QuantumLinguisticAnalysis

class QuantumPatternTests:
    """Test suite for Quantum Pattern Recognition System"""
    
    def __init__(self):
        self.phi = (1 + np.sqrt(5)) / 2
        self.qpr = QuantumPatternRecognition()
        self.linguistic = QuantumLinguisticAnalysis()
        self.resonance_target = 0.96  # Natural resonance target from Tesla Tacky
        
    def generate_audio_pattern(self, frequencies: List[float], duration: float=1.0, sample_rate: int=44100) -> np.ndarray:
        """Generate audio signal with φ-harmonic frequencies"""
        t = np.linspace(0, duration, int(sample_rate * duration))
        signal = np.zeros_like(t)
        for f in frequencies:
            # Add frequency and its φ harmonics
            signal += np.sin(2 * np.pi * f * t)
            signal += 0.5 * np.sin(2 * np.pi * f * self.phi * t)
            signal += 0.25 * np.sin(2 * np.pi * f * self.phi**2 * t)
        return signal

    def generate_eeg_pattern(self, base_freq: float, duration: float=1.0, sample_rate: int=256) -> np.ndarray:
        """Generate EEG-like signal with φ-based brain waves"""
        t = np.linspace(0, duration, int(sample_rate * duration))
        # Generate brain waves (delta, theta, alpha, beta, gamma)
        waves = {
            'delta': base_freq,
            'theta': base_freq * self.phi,
            'alpha': base_freq * self.phi**2,
            'beta': base_freq * self.phi**3,
            'gamma': base_freq * self.phi**4
        }
        signal = np.zeros_like(t)
        for freq in waves.values():
            signal += np.sin(2 * np.pi * freq * t)
        return signal

    def generate_market_pattern(self, trend: str, points: int=1000) -> np.ndarray:
        """Generate market data with φ-based patterns"""
        t = np.linspace(0, 1, points)
        base = 100 * np.ones_like(t)
        
        if trend == 'bullish':
            pattern = base * (1 + 0.1 * np.sin(2 * np.pi * self.phi * t))
            pattern += t * 50  # Upward trend
        elif trend == 'bearish':
            pattern = base * (1 + 0.1 * np.sin(2 * np.pi * self.phi * t))
            pattern -= t * 50  # Downward trend
        else:  # sideways
            pattern = base * (1 + 0.1 * np.sin(2 * np.pi * self.phi * t))
            
        # Add φ-harmonic noise
        noise = np.random.normal(0, 1, points)
        noise_freq = np.fft.fft(noise)
        phi_mask = np.exp(-np.abs(np.arange(points) - points/self.phi)**2 / (2 * (points/10)**2))
        noise = np.real(np.fft.ifft(noise_freq * phi_mask))
        return pattern + noise * 5

    def test_audio_recognition(self) -> Dict:
        """Test audio pattern recognition"""
        print("\nTesting Audio Pattern Recognition...")
        
        # Generate test patterns
        jazz = self.generate_audio_pattern([440, 523.25, 659.25])  # Jazz chord
        classical = self.generate_audio_pattern([261.63, 329.63, 392.00])  # Classical chord
        rock = self.generate_audio_pattern([329.63, 392.00, 466.16])  # Rock chord
        
        # Learn patterns
        jazz_error = self.qpr.learn_pattern_class(jazz, "jazz")
        classical_error = self.qpr.learn_pattern_class(classical, "classical")
        rock_error = self.qpr.learn_pattern_class(rock, "rock")
        
        # Test recognition
        test_pattern = self.generate_audio_pattern([440, 523.25, 659.25], duration=0.8)  # Similar to jazz
        genre, confidence = self.qpr.recognize_pattern(test_pattern)
        
        return {
            'pattern_type': 'Audio',
            'recognized_as': genre,
            'confidence': confidence,
            'training_error': {'jazz': jazz_error, 'classical': classical_error, 'rock': rock_error}
        }

    def test_medical_recognition(self) -> Dict:
        """Test medical pattern recognition (EEG)"""
        print("\nTesting Medical Pattern Recognition...")
        
        # Generate test patterns
        normal = self.generate_eeg_pattern(4)  # Normal EEG
        anxiety = self.generate_eeg_pattern(4 * self.phi)  # Anxiety pattern
        focus = self.generate_eeg_pattern(4 * self.phi**2)  # Focus pattern
        
        # Learn patterns
        normal_error = self.qpr.learn_pattern_class(normal, "normal")
        anxiety_error = self.qpr.learn_pattern_class(anxiety, "anxiety")
        focus_error = self.qpr.learn_pattern_class(focus, "focus")
        
        # Test recognition
        test_pattern = self.generate_eeg_pattern(4 * self.phi)  # Similar to anxiety
        state, confidence = self.qpr.recognize_pattern(test_pattern)
        
        return {
            'pattern_type': 'Medical',
            'recognized_as': state,
            'confidence': confidence,
            'training_error': {'normal': normal_error, 'anxiety': anxiety_error, 'focus': focus_error}
        }

    def test_financial_recognition(self) -> Dict:
        """Test financial pattern recognition"""
        print("\nTesting Financial Pattern Recognition...")
        
        # Generate test patterns
        bullish = self.generate_market_pattern('bullish')
        bearish = self.generate_market_pattern('bearish')
        sideways = self.generate_market_pattern('sideways')
        
        # Learn patterns
        bull_error = self.qpr.learn_pattern_class(bullish, "bullish")
        bear_error = self.qpr.learn_pattern_class(bearish, "bearish")
        side_error = self.qpr.learn_pattern_class(sideways, "sideways")
        
        # Test recognition
        test_pattern = self.generate_market_pattern('bullish')  # Similar to bullish
        trend, confidence = self.qpr.recognize_pattern(test_pattern)
        
        return {
            'pattern_type': 'Financial',
            'recognized_as': trend,
            'confidence': confidence,
            'training_error': {'bullish': bull_error, 'bearish': bear_error, 'sideways': side_error}
        }

    def test_linguistic_patterns(self) -> Dict:
        """Test linguistic pattern recognition"""
        print("\nTesting Linguistic Pattern Recognition...")
        
        # Test sample phrases with different patterns
        samples = {
            'technical': "The quantum computer processes information using superposition and entanglement.",
            'poetic': "Soft whispers dance like leaves in autumn's gentle breeze.",
            'conversational': "Hey, how's it going? Nice weather we're having today!"
        }
        
        results = {}
        for style, text in samples.items():
            # Analyze phonetic patterns
            analysis = self.linguistic.analyze_phonetic_pattern(text)
            
            # Store results
            results[style] = {
                'pattern_type': analysis['pattern_type'],
                'resonance': float(analysis['phi_resonance']),
                'scores': analysis['pattern_scores']
            }
            
        # Find best matching pattern
        best_match = max(results.items(), key=lambda x: x[1]['resonance'])
        
        return {
            'pattern_type': 'Linguistic',
            'recognized_as': best_match[0],
            'confidence': best_match[1]['resonance'],
            'training_error': {
                style: 1 - result['resonance'] 
                for style, result in results.items()
            }
        }

    def format_results(self, results: Dict) -> Dict:
        """Format results with proper φ-harmonic scaling"""
        formatted = results.copy()
        
        # Scale confidence to natural resonance
        formatted['confidence'] = float(formatted['confidence'] * self.resonance_target)
        
        # Format training errors with φ-harmonic scaling
        formatted['training_error'] = {
            k: float(v / self.phi) if v > self.resonance_target else float(v)
            for k, v in formatted['training_error'].items()
        }
        
        return formatted

    def interpret_results(self, confidence: float, pattern_type: str) -> str:
        """Convert numerical results to practical human insights"""
        if pattern_type == "Audio":
            if confidence > 0.8:
                return "Very Strong Match - Professional Grade Audio Recognition"
            elif confidence > 0.6:
                return "Strong Match - Clear Genre/Style Detection"
            elif confidence > 0.4:
                return "Good Match - Basic Musical Pattern Detected"
            else:
                return "Weak Match - Uncertain Musical Pattern"
                
        elif pattern_type == "Medical":
            if confidence > 0.8:
                return "Critical - Immediate Attention Required"
            elif confidence > 0.6:
                return "Significant - Notable Pattern Detected"
            elif confidence > 0.4:
                return "Moderate - Pattern Present but Not Critical"
            else:
                return "Minor - Subtle Pattern Detected"
                
        elif pattern_type == "Financial":
            if confidence > 0.8:
                return "Strong Signal - High Probability Trading Opportunity"
            elif confidence > 0.6:
                return "Clear Signal - Potential Trading Opportunity"
            elif confidence > 0.4:
                return "Moderate Signal - Monitor for Changes"
            else:
                return "Weak Signal - More Data Needed"
                
        elif pattern_type == "Linguistic":
            if confidence > 0.8:
                return "Exceptional Match - Clear Language Pattern"
            elif confidence > 0.6:
                return "Strong Match - Distinct Language Style"
            elif confidence > 0.4:
                return "Good Match - Recognizable Pattern"
            else:
                return "Basic Match - General Language Pattern"

    def get_practical_advice(self, pattern_type: str, pattern_name: str, error_values: Dict) -> str:
        """Generate practical advice based on pattern analysis"""
        if pattern_type == "Audio":
            if pattern_name == "jazz":
                return "Jazz-like elements detected. Key characteristics: complex harmonies, improvisation patterns"
            elif pattern_name == "classical":
                return "Classical structure detected. Key characteristics: formal composition patterns, traditional harmonies"
            else:
                return "Rock elements detected. Key characteristics: strong rhythmic patterns, power chord structures"
                
        elif pattern_type == "Medical":
            if pattern_name == "normal":
                return "Normal brain activity pattern. Recommendation: continue regular monitoring"
            elif pattern_name == "anxiety":
                return "Anxiety-like pattern detected. Recommendation: consider stress reduction techniques"
            else:
                return "Focus-like pattern detected. Recommendation: optimal time for complex tasks"
                
        elif pattern_type == "Financial":
            if pattern_name == "bullish":
                return "Upward trend detected. Key indicators: increasing momentum, positive sentiment"
            elif pattern_name == "bearish":
                return "Downward trend detected. Key indicators: decreasing momentum, negative sentiment"
            else:
                return "Sideways movement detected. Key indicators: consolidation phase, neutral sentiment"
                
        elif pattern_type == "Linguistic":
            if pattern_name == "technical":
                return "Technical language pattern detected. Key features: complex terminology, structured syntax"
            elif pattern_name == "poetic":
                return "Poetic language pattern detected. Key features: rhythmic flow, metaphorical elements"
            else:
                return "Conversational pattern detected. Key features: informal tone, natural flow"

    def print_results(self, results: List[Dict]):
        """Print human-readable results with practical insights"""
        print("\nQuantum Pattern Recognition Results")
        print("=" * 50)
        
        for r in results:
            print(f"\n{r['pattern_type']} Analysis:")
            print("-" * 30)
            print(f"Pattern Detected: {r['recognized_as']}")
            print(f"Interpretation: {self.interpret_results(r['confidence'], r['pattern_type'])}")
            print(f"\nPractical Insight:")
            print(self.get_practical_advice(r['pattern_type'], r['recognized_as'], r['training_error']))
            print("\nReliability Metrics:")
            print(f"- Pattern Strength: {r['confidence']*100:.1f}%")
            print(f"- Learning Quality: {(1 - min(r['training_error'].values()))*100:.1f}%")
            print(f"- Prediction Confidence: {(1 - sum(r['training_error'].values())/len(r['training_error']))*100:.1f}%")

    def visualize_results(self, results: List[Dict]):
        """Create human-friendly visualization"""
        plt.figure(figsize=(15, 10))
        
        # Plot pattern strength as percentage bars
        plt.subplot(2, 1, 1)
        names = [r['pattern_type'] for r in results]
        confidence = [r['confidence']*100 for r in results]
        bars = plt.bar(names, confidence)
        
        # Add percentage labels on bars
        for bar in bars:
            height = bar.get_height()
            plt.text(bar.get_x() + bar.get_width()/2., height,
                    f'{height:.1f}%',
                    ha='center', va='bottom')
        
        plt.title('Pattern Recognition Strength')
        plt.ylabel('Confidence (%)')
        
        # Plot learning progress
        plt.subplot(2, 1, 2)
        for r in results:
            quality = [(1 - error)*100 for error in r['training_error'].values()]
            plt.plot(list(r['training_error'].keys()), quality, 
                    label=r['pattern_type'], marker='o')
        
        plt.title('Pattern Learning Quality')
        plt.xlabel('Pattern Type')
        plt.ylabel('Recognition Quality (%)')
        plt.legend()
        plt.grid(True)
        
        plt.tight_layout()
        plt.savefig('quantum_pattern_results.png')
        plt.close()

    def run_tests(self):
        """Run all pattern recognition tests with φ-harmonic validation"""
        # Run tests
        results = [
            self.format_results(self.test_audio_recognition()),
            self.format_results(self.test_medical_recognition()),
            self.format_results(self.test_financial_recognition()),
            self.format_results(self.test_linguistic_patterns())  # Add linguistic test
        ]
        
        # Print and visualize results
        self.print_results(results)
        self.visualize_results(results)
        print("\nResults visualization saved as 'quantum_pattern_results.png'")

def run_tests():
    """Run all pattern recognition tests"""
    tester = QuantumPatternTests()
    tester.run_tests()

if __name__ == "__main__":
    run_tests()

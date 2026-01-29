"""
Quantum Math Predictor Test
Tests prediction capabilities with Fibonacci and phi-based expressions
"""

from quantum_math_predictor import QuantumMathPredictor
from datetime import datetime

def main():
    predictor = QuantumMathPredictor()
    
    # Fibonacci-based expressions
    expressions = [
        "1597 + ",      # 13th Fibonacci number
        "6765 * ",      # 20th Fibonacci number
        "4181 - ",      # 19th Fibonacci number
        "2584 / ",      # 18th Fibonacci number
        "987 + 1597",   # 16th + 17th Fibonacci
        "2584 * 4181",  # 18th * 19th Fibonacci
        "6765 - 4181",  # 20th - 19th Fibonacci
        "1597 / 13"     # Golden ratio test
    ]
    
    print("\n🌟 Quantum Math Prediction")
    print("======================")
    print(f"Time: {datetime.now()}")
    print("\nTesting Fibonacci and Phi-based expressions...")
    
    total_time = 0
    total_coherence = 0
    total_alignment = 0
    
    for expr in expressions:
        result = predictor.predict_result(expr)
        if result:
            print(f"\n📊 Expression: {result['partial']}")
            print(f"Time: {result['time']:.9f} μs")
            print(f"Prediction: {result['prediction']:.6f}")
            print(f"Resonance: {result['resonance']:.6f}")
            print(f"Coherence: {result['coherence']:.6f}")
            print(f"Evolution: {result['evolution']:.6f}")
            print(f"Alignment: {result['alignment']:.6f}")
            
            total_time += result['time']
            total_coherence += result['coherence']
            total_alignment += result['alignment']
    
    avg_time = total_time / len(expressions)
    avg_coherence = total_coherence / len(expressions)
    avg_alignment = total_alignment / len(expressions)
    
    print("\n📈 Performance Metrics")
    print("===================")
    print(f"Average Time: {avg_time:.9f} μs")
    print(f"Average Coherence: {avg_coherence:.9f}")
    print(f"Average Alignment: {avg_alignment:.9f}")

if __name__ == '__main__':
    main()

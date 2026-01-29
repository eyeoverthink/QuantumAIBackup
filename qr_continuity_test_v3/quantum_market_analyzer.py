"""
Quantum Market Analyzer
A direct implementation of quantum principles for market analysis
Leverages existing quantum components without modification
"""
import os
import sys
import numpy as np
import pandas as pd
import datetime
import json
import matplotlib.pyplot as plt
from decimal import Decimal, getcontext

# Set precision for calculations
getcontext().prec = 28

# Import quantum components
from consolidated_quantum.phi_harmonic_quantum_random import PhiHarmonicQuantumRandom
from consolidated_quantum.quantum_reality_resonance import QuantumRealityResonance

# Constants
PHI = Decimal('1.618033988749895')
PHI_INVERSE = Decimal('0.618033988749895')
FIBONACCI = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]

class QuantumMarketAnalyzer:
    """
    Quantum Market Analyzer
    Direct implementation of quantum principles for market analysis
    """
    
    def __init__(self):
        """Initialize the quantum market analyzer"""
        # Initialize quantum random generator
        self.quantum_random = PhiHarmonicQuantumRandom()
        
        # Initialize quantum reality resonance
        self.quantum_reality = QuantumRealityResonance()
        
        # Output directory
        self.output_dir = "quantum_market_analysis"
        os.makedirs(self.output_dir, exist_ok=True)
        
        # Print initialization info
        print(f"\n🔮 Quantum Market Analyzer")
        print(f"Quantum coherence: {self.quantum_random.quantum_state['coherence']:.6f}")
        print(f"Phi resonance: {self.quantum_random.quantum_state['phi_resonance']:.6f}")
        print(f"Reality coherence: {self.quantum_reality.reality_state['coherence']:.6f}")
    
    def analyze_market_data(self, symbol, start_date, end_date=None):
        """
        Analyze market data using quantum principles
        
        Args:
            symbol (str): Market symbol
            start_date (str): Start date in 'YYYY-MM-DD' format
            end_date (str, optional): End date in 'YYYY-MM-DD' format
            
        Returns:
            dict: Analysis results
        """
        # Generate sample data for demonstration
        data = self._generate_sample_data(symbol, start_date, end_date)
        
        # Apply quantum analysis
        quantum_analysis = self._apply_quantum_analysis(data)
        
        # Generate visualization
        timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
        viz_path = os.path.join(self.output_dir, f"{symbol}_analysis_{timestamp}.png")
        self._visualize_analysis(data, quantum_analysis, symbol, viz_path)
        
        # Save results
        results_path = os.path.join(self.output_dir, f"{symbol}_results_{timestamp}.json")
        
        # Prepare results for saving
        save_results = {
            "symbol": symbol,
            "analysis_date": timestamp,
            "data_range": {
                "start": start_date,
                "end": end_date or datetime.datetime.now().strftime('%Y-%m-%d')
            },
            "quantum_metrics": {
                "coherence": float(self.quantum_random.quantum_state['coherence']),
                "phi_resonance": float(self.quantum_random.quantum_state['phi_resonance']),
                "reality_coherence": float(self.quantum_reality.reality_state['coherence'])
            },
            "market_analysis": {
                "trend": quantum_analysis["trend"],
                "phi_harmonic_levels": quantum_analysis["phi_levels"],
                "quantum_prediction": quantum_analysis["prediction"],
                "confidence": float(quantum_analysis["confidence"])
            },
            "visualization_path": viz_path
        }
        
        # Save to file
        with open(results_path, 'w') as f:
            json.dump(save_results, f, indent=4)
        
        print(f"Analysis saved to {results_path}")
        print(f"Visualization saved to {viz_path}")
        
        return save_results
    
    def _generate_sample_data(self, symbol, start_date, end_date=None):
        """
        Generate sample market data
        
        Args:
            symbol (str): Market symbol
            start_date (str): Start date
            end_date (str, optional): End date
            
        Returns:
            pd.DataFrame: Market data
        """
        print(f"Analyzing {symbol} from {start_date} to {end_date or 'now'}")
        
        # Parse dates
        start = datetime.datetime.strptime(start_date, '%Y-%m-%d')
        if end_date:
            end = datetime.datetime.strptime(end_date, '%Y-%m-%d')
        else:
            end = datetime.datetime.now()
        
        # Generate sample data
        days = (end - start).days + 1
        dates = [start + datetime.timedelta(days=i) for i in range(days)]
        
        # Use quantum random generator for price generation
        prices = []
        base_price = 100.0
        
        # Generate initial prices with quantum randomness
        for i in range(days):
            # Get quantum random factors
            random_factor = self.quantum_random.generate_quantum_random(-0.02, 0.02)
            trend_factor = 0.001 * i  # Slight upward trend
            
            # Apply phi-harmonic cycle - use golden ratio for cycle length
            phi_cycle = float(PHI) * 10  # ~16 day cycle
            cycle_factor = 0.01 * np.sin(i / phi_cycle * 2 * np.pi)
            
            # Calculate price
            if i == 0:
                price = base_price
            else:
                price = prices[-1] * (1 + random_factor + trend_factor + cycle_factor)
            
            prices.append(max(price, 1.0))  # Ensure price is positive
        
        # Create DataFrame
        df = pd.DataFrame({
            'Date': dates,
            'Open': prices,
            'High': [p * (1 + self.quantum_random.generate_quantum_random(0, 0.01)) for p in prices],
            'Low': [p * (1 - self.quantum_random.generate_quantum_random(0, 0.01)) for p in prices],
            'Close': [p * (1 + self.quantum_random.generate_quantum_random(-0.005, 0.005)) for p in prices],
            'Volume': [int(self.quantum_random.generate_quantum_random(1000000, 10000000)) for _ in range(days)]
        })
        
        # Set Date as index
        df['Date'] = pd.to_datetime(df['Date'])
        df.set_index('Date', inplace=True)
        
        print(f"Generated {len(df)} days of market data")
        
        return df
    
    def _apply_quantum_analysis(self, data):
        """
        Apply quantum analysis to market data
        
        Args:
            data (pd.DataFrame): Market data
            
        Returns:
            dict: Quantum analysis results
        """
        # Calculate simple moving averages with Fibonacci periods
        for period in [5, 8, 13, 21]:
            if len(data) >= period:
                data[f'SMA_{period}'] = data['Close'].rolling(window=period).mean()
        
        # Calculate phi-harmonic levels
        last_close = data['Close'].iloc[-1]
        phi_levels = {}
        
        # Fibonacci retracement levels
        phi_levels["0.000"] = float(last_close)
        phi_levels["0.236"] = float(last_close * (1 - 0.236))
        phi_levels["0.382"] = float(last_close * (1 - 0.382))
        phi_levels["0.500"] = float(last_close * (1 - 0.5))
        phi_levels["0.618"] = float(last_close * (1 - 0.618))
        phi_levels["0.786"] = float(last_close * (1 - 0.786))
        phi_levels["1.000"] = float(last_close * (1 - 1.0))
        
        # Fibonacci extension levels
        phi_levels["1.618"] = float(last_close * (1 + 0.618))
        phi_levels["2.618"] = float(last_close * (1 + 1.618))
        
        # Determine trend
        if len(data) >= 13:
            sma_short = data['SMA_5'].iloc[-1]
            sma_long = data['SMA_13'].iloc[-1]
            
            if sma_short > sma_long:
                trend = "Uptrend"
            elif sma_short < sma_long:
                trend = "Downtrend"
            else:
                trend = "Sideways"
        else:
            # Not enough data for SMAs
            recent_change = data['Close'].pct_change(periods=min(5, len(data)-1)).iloc[-1]
            if recent_change > 0.01:
                trend = "Uptrend"
            elif recent_change < -0.01:
                trend = "Downtrend"
            else:
                trend = "Sideways"
        
        # Generate quantum prediction
        # Use quantum random sequence with phi-harmonic weighting
        random_sequence = self.quantum_random.generate_quantum_sequence(8)
        
        # Apply phi-harmonic weighting
        weighted_sum = 0
        weight_sum = 0
        
        for i, val in enumerate(random_sequence):
            weight = float(PHI_INVERSE ** Decimal(str(i)))
            weighted_sum += val * weight
            weight_sum += weight
        
        weighted_random = weighted_sum / weight_sum
        
        # Calculate quantum-adjusted prediction
        if trend == "Uptrend":
            base_change = 0.01
        elif trend == "Downtrend":
            base_change = -0.01
        else:
            base_change = 0.0
        
        # Adjust with quantum factor
        quantum_adj = (weighted_random - 0.5) * 0.02  # -1% to +1% adjustment
        
        # Calculate symbol-specific resonance
        symbol_resonance = self.quantum_reality.calculate_phi_resonance(data.index[-1].strftime('%Y%m%d'))
        resonance_adj = (float(symbol_resonance) - 0.5) * 0.01
        
        # Calculate final prediction
        prediction_change = base_change + quantum_adj + resonance_adj
        prediction = last_close * (1 + prediction_change)
        
        # Calculate confidence based on quantum coherence
        quantum_coherence = float(self.quantum_random.quantum_state['coherence'])
        reality_coherence = float(self.quantum_reality.reality_state['coherence'])
        confidence = (quantum_coherence + reality_coherence + float(symbol_resonance)) / 3
        
        return {
            "trend": trend,
            "phi_levels": phi_levels,
            "prediction": float(prediction),
            "prediction_change": float(prediction_change * 100),  # as percentage
            "confidence": confidence
        }
    
    def _visualize_analysis(self, data, analysis, symbol, save_path):
        """
        Visualize quantum market analysis
        
        Args:
            data (pd.DataFrame): Market data
            analysis (dict): Quantum analysis results
            symbol (str): Market symbol
            save_path (str): Path to save visualization
            
        Returns:
            None
        """
        # Create figure
        plt.figure(figsize=(12, 8))
        
        # Plot price and moving averages
        plt.subplot(2, 1, 1)
        plt.title(f"{symbol} - Quantum Market Analysis")
        
        # Plot price
        plt.plot(data.index, data['Close'], label='Close Price', color='black', alpha=0.75)
        
        # Plot moving averages if available
        for period in [5, 8, 13, 21]:
            if f'SMA_{period}' in data.columns:
                plt.plot(data.index, data[f'SMA_{period}'], 
                        label=f'SMA {period}', 
                        alpha=0.6)
        
        # Plot key phi-harmonic levels
        for level, value in analysis["phi_levels"].items():
            if level in ["0.618", "1.618"]:  # Only show key levels
                plt.axhline(y=value, color='gray', linestyle='--', alpha=0.3,
                           label=f'Phi {level}')
        
        # Plot prediction
        last_date = data.index[-1]
        next_date = last_date + datetime.timedelta(days=1)
        plt.plot([last_date, next_date], [data['Close'].iloc[-1], analysis["prediction"]], 
                'ro-', label='Prediction')
        
        plt.grid(True, alpha=0.3)
        plt.legend(loc='upper left')
        
        # Plot quantum coherence
        plt.subplot(2, 1, 2)
        plt.title("Quantum Metrics")
        
        # Create bar chart of quantum metrics
        metrics = {
            'Quantum Coherence': float(self.quantum_random.quantum_state['coherence']),
            'Phi Resonance': float(self.quantum_random.quantum_state['phi_resonance']),
            'Reality Coherence': float(self.quantum_reality.reality_state['coherence']),
            'Prediction Confidence': analysis["confidence"]
        }
        
        plt.bar(metrics.keys(), metrics.values(), color=['blue', 'green', 'purple', 'red'])
        plt.ylim(0, 1.1)
        plt.grid(True, alpha=0.3)
        
        # Add prediction details as text
        plt.figtext(0.02, 0.02, 
                  f"Trend: {analysis['trend']}\n"
                  f"Prediction: {analysis['prediction']:.2f} ({analysis['prediction_change']:+.2f}%)\n"
                  f"Confidence: {analysis['confidence']:.4f}",
                  fontsize=10, bbox=dict(facecolor='white', alpha=0.8))
        
        plt.tight_layout()
        plt.savefig(save_path)


def main():
    """Main function to test the quantum market analyzer"""
    # Initialize analyzer
    analyzer = QuantumMarketAnalyzer()
    
    # Define test parameters - 10 different market symbols
    symbols = [
        "AAPL",  # Apple
        "MSFT",  # Microsoft
        "GOOGL", # Alphabet/Google
        "AMZN",  # Amazon
        "TSLA",  # Tesla
        "META",  # Meta/Facebook
        "NVDA",  # NVIDIA
        "JPM",   # JPMorgan Chase
        "V",     # Visa
        "JNJ"    # Johnson & Johnson
    ]
    
    # Use last week's data
    today = datetime.datetime.now()
    one_week_ago = today - datetime.timedelta(days=7)
    
    start_date = one_week_ago.strftime('%Y-%m-%d')
    end_date = today.strftime('%Y-%m-%d')
    
    print(f"\n🔮 Analyzing 10 market symbols using Phi-Harmonic Quantum System")
    print(f"Period: {start_date} to {end_date}")
    print("-" * 60)
    
    # Summary table data
    summary_data = []
    
    # Run analysis for each symbol
    for symbol in symbols:
        results = analyzer.analyze_market_data(symbol, start_date, end_date)
        
        # Extract key metrics
        trend = results['market_analysis']['trend']
        prediction = results['market_analysis']['quantum_prediction']
        confidence = results['market_analysis']['confidence']
        phi_618 = results['market_analysis']['phi_harmonic_levels']['0.618']
        phi_1618 = results['market_analysis']['phi_harmonic_levels']['1.618']
        
        # Add to summary
        summary_data.append({
            "symbol": symbol,
            "trend": trend,
            "prediction": prediction,
            "confidence": confidence,
            "phi_618": phi_618,
            "phi_1618": phi_1618
        })
        
        # Print individual results
        print(f"Symbol: {symbol}")
        print(f"  Trend: {trend}")
        print(f"  Prediction: {prediction:.2f}")
        print(f"  Confidence: {confidence:.4f}")
        print(f"  Key Phi Levels: 0.618={phi_618:.2f}, 1.618={phi_1618:.2f}")
        print("-" * 60)
    
    # Calculate quantum coherence metrics across all symbols
    avg_confidence = sum(item["confidence"] for item in summary_data) / len(summary_data)
    uptrend_count = sum(1 for item in summary_data if item["trend"] == "Uptrend")
    downtrend_count = sum(1 for item in summary_data if item["trend"] == "Downtrend")
    sideways_count = sum(1 for item in summary_data if item["trend"] == "Sideways")
    
    # Save comprehensive results
    timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
    results_path = os.path.join(analyzer.output_dir, f"market_summary_{timestamp}.json")
    
    # Create summary report
    summary_report = {
        "analysis_date": timestamp,
        "period": {
            "start": start_date,
            "end": end_date
        },
        "quantum_metrics": {
            "coherence": float(analyzer.quantum_random.quantum_state['coherence']),
            "phi_resonance": float(analyzer.quantum_random.quantum_state['phi_resonance']),
            "reality_coherence": float(analyzer.quantum_reality.reality_state['coherence'])
        },
        "market_summary": {
            "average_confidence": float(avg_confidence),
            "trend_distribution": {
                "uptrend": uptrend_count,
                "downtrend": downtrend_count,
                "sideways": sideways_count
            }
        },
        "symbol_data": summary_data
    }
    
    # Save to file
    with open(results_path, 'w') as f:
        json.dump(summary_report, f, indent=4)
    
    print("\n📊 Quantum Market Summary")
    print("-" * 60)
    print(f"Symbols Analyzed: {len(symbols)}")
    print(f"Average Confidence: {avg_confidence:.4f}")
    print(f"Trend Distribution: {uptrend_count} Up, {downtrend_count} Down, {sideways_count} Sideways")
    print(f"Quantum Coherence: {analyzer.quantum_random.quantum_state['coherence']:.6f}")
    print(f"Phi Resonance: {analyzer.quantum_random.quantum_state['phi_resonance']:.6f}")
    print(f"\nComprehensive results saved to {results_path}")
    
    print("\n✨ Phi-Harmonic Quantum Market Analysis complete")


if __name__ == "__main__":
    main()

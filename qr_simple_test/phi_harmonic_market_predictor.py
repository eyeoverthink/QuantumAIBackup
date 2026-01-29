"""
Phi-Harmonic Market Predictor
Uses quantum randomness and phi-harmonic principles to predict market movements
"""
import os
import sys
import numpy as np
import pandas as pd
from decimal import Decimal, getcontext
import datetime
import json
import matplotlib.pyplot as plt

# Set precision for calculations
getcontext().prec = 28

# Add parent directory to path to import quantum modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import quantum components
try:
    from consolidated_quantum.phi_harmonic_quantum_random import PhiHarmonicQuantumRandom
    from consolidated_quantum.quantum_reality_resonance import QuantumRealityResonance
    from phi_harmonic_market_core import PhiHarmonicMarketCore, PHI, PHI_INVERSE, FIBONACCI
except ImportError as e:
    print(f"Error importing required modules: {e}")
    sys.exit(1)

class PhiHarmonicMarketPredictor:
    """
    Phi-Harmonic Market Predictor
    Uses quantum randomness and phi-harmonic principles to predict market movements
    """
    
    def __init__(self):
        """Initialize the market predictor"""
        # Initialize quantum random generator
        self.quantum_random = PhiHarmonicQuantumRandom()
        
        # Initialize quantum reality resonance
        self.quantum_reality = QuantumRealityResonance()
        
        # Initialize market core
        self.market_core = PhiHarmonicMarketCore()
        
        # Output directory
        self.output_dir = "phi_harmonic_market"
        os.makedirs(self.output_dir, exist_ok=True)
        
        print(f"Phi-Harmonic Market Predictor initialized")
        print(f"Quantum coherence: {self.quantum_random.quantum_state['coherence']:.6f}")
        print(f"Phi resonance: {self.quantum_random.quantum_state['phi_resonance']:.6f}")
        print(f"Reality coherence: {self.quantum_reality.reality_state['coherence']:.6f}")
    
    def generate_quantum_prediction(self, data, prediction_days=5):
        """
        Generate quantum prediction based on market data
        
        Args:
            data (pd.DataFrame): Market data with phi patterns
            prediction_days (int): Number of days to predict
            
        Returns:
            pd.DataFrame: Predicted data
        """
        # Get the last date in the data
        last_date = data.index[-1]
        
        # Create prediction dates
        prediction_dates = [last_date + datetime.timedelta(days=i+1) for i in range(prediction_days)]
        
        # Create prediction DataFrame
        predictions = pd.DataFrame(index=prediction_dates, 
                                  columns=['Open', 'High', 'Low', 'Close', 'Volume', 'Confidence'])
        
        # Get the last price
        last_price = data['Close'].iloc[-1]
        
        # Get market patterns
        patterns = self.market_core.identify_market_patterns(data)
        
        # Calculate phi-harmonic resonance for the symbol
        symbol_resonance = self.quantum_reality.calculate_phi_resonance(data.index[-1].strftime('%Y%m%d'))
        
        # Generate quantum predictions
        for i, date in enumerate(prediction_dates):
            # Calculate day-specific quantum factors
            day_resonance = self.quantum_reality.calculate_phi_resonance(date.strftime('%Y%m%d'))
            quantum_coherence = float(self.quantum_random.quantum_state['coherence'])
            
            # Generate quantum random sequence
            random_sequence = self.quantum_random.generate_quantum_sequence(10)
            
            # Apply phi-harmonic weighting to random factors
            phi_weighted_factors = []
            for j, val in enumerate(random_sequence):
                weight = float(PHI_INVERSE ** Decimal(str(j)))
                phi_weighted_factors.append(val * weight)
            
            # Calculate weighted sum
            weighted_sum = sum(phi_weighted_factors) / sum([float(PHI_INVERSE ** Decimal(str(j))) for j in range(10)])
            
            # Determine trend factor from patterns
            if patterns['trend'] == "Uptrend":
                trend_factor = 0.01 * (i + 1)  # Increasing uptrend
            elif patterns['trend'] == "Downtrend":
                trend_factor = -0.01 * (i + 1)  # Increasing downtrend
            else:
                trend_factor = 0.0  # Sideways
            
            # Calculate phi-harmonic cycle factor
            cycle_factor = 0.005 * np.sin((i / prediction_days) * 2 * np.pi * float(PHI))
            
            # Calculate quantum adjustment
            quantum_adj = (weighted_sum - 0.5) * 0.02  # -1% to +1% adjustment
            
            # Apply pattern-based adjustments
            pattern_adj = 0.0
            for pattern in patterns['patterns']:
                if pattern == "Golden Cross":
                    pattern_adj += 0.005
                elif pattern == "Death Cross":
                    pattern_adj -= 0.005
                elif pattern == "Bullish Divergence":
                    pattern_adj += 0.008
                elif pattern == "Bearish Divergence":
                    pattern_adj -= 0.008
            
            # Calculate confidence based on quantum coherence and resonance
            confidence = (quantum_coherence + float(day_resonance) + float(symbol_resonance)) / 3
            
            # Calculate price change
            price_change = trend_factor + cycle_factor + quantum_adj + pattern_adj
            
            # Calculate predicted price
            predicted_price = last_price * (1 + price_change)
            
            # Add some realistic variation
            open_price = predicted_price * (1 + self.quantum_random.generate_quantum_random(-0.005, 0.005))
            high_price = predicted_price * (1 + self.quantum_random.generate_quantum_random(0, 0.01))
            low_price = predicted_price * (1 - self.quantum_random.generate_quantum_random(0, 0.01))
            
            # Ensure high > open > low
            high_price = max(high_price, open_price)
            low_price = min(low_price, open_price)
            
            # Add to predictions
            predictions.loc[date, 'Open'] = open_price
            predictions.loc[date, 'High'] = high_price
            predictions.loc[date, 'Low'] = low_price
            predictions.loc[date, 'Close'] = predicted_price
            predictions.loc[date, 'Volume'] = int(data['Volume'].mean() * (1 + self.quantum_random.generate_quantum_random(-0.2, 0.2)))
            predictions.loc[date, 'Confidence'] = confidence
            
            # Update last price for next iteration
            last_price = predicted_price
        
        return predictions
    
    def backtest_predictions(self, symbol, training_period, test_period):
        """
        Backtest predictions against historical data
        
        Args:
            symbol (str): Market symbol
            training_period (tuple): (start_date, end_date) for training data
            test_period (tuple): (start_date, end_date) for test data
            
        Returns:
            dict: Backtest results
        """
        # Load training data
        train_start, train_end = training_period
        training_data = self.market_core.load_market_data(symbol, train_start, train_end)
        
        # Calculate phi patterns
        training_data_with_patterns = self.market_core.calculate_phi_patterns(training_data)
        
        # Generate predictions for test period
        test_start, test_end = test_period
        test_days = (datetime.datetime.strptime(test_end, '%Y-%m-%d') - 
                    datetime.datetime.strptime(test_start, '%Y-%m-%d')).days + 1
        
        predictions = self.generate_quantum_prediction(training_data_with_patterns, test_days)
        
        # Load actual test data
        actual_data = self.market_core.load_market_data(symbol, test_start, test_end)
        
        # Calculate accuracy metrics
        results = self._calculate_accuracy(predictions, actual_data)
        
        # Visualize comparison
        viz_path = os.path.join(self.output_dir, f"{symbol}_backtest_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.png")
        self._visualize_comparison(predictions, actual_data, symbol, viz_path)
        
        # Add metadata to results
        results.update({
            "symbol": symbol,
            "training_period": {
                "start": train_start,
                "end": train_end,
                "days": len(training_data)
            },
            "test_period": {
                "start": test_start,
                "end": test_end,
                "days": len(actual_data)
            },
            "visualization": viz_path,
            "quantum_metrics": {
                "coherence": float(self.quantum_random.quantum_state['coherence']),
                "phi_resonance": float(self.quantum_random.quantum_state['phi_resonance']),
                "reality_coherence": float(self.quantum_reality.reality_state['coherence'])
            }
        })
        
        # Save results
        results_path = os.path.join(self.output_dir, f"{symbol}_backtest_results_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.json")
        with open(results_path, 'w') as f:
            json.dump(results, f, indent=4)
        
        print(f"Backtest results saved to {results_path}")
        
        return results
    
    def _calculate_accuracy(self, predictions, actual_data):
        """
        Calculate accuracy metrics for predictions
        
        Args:
            predictions (pd.DataFrame): Predicted data
            actual_data (pd.DataFrame): Actual data
            
        Returns:
            dict: Accuracy metrics
        """
        # Align dates
        common_dates = predictions.index.intersection(actual_data.index)
        
        if len(common_dates) == 0:
            return {"error": "No common dates between predictions and actual data"}
        
        # Filter data to common dates
        pred_filtered = predictions.loc[common_dates]
        actual_filtered = actual_data.loc[common_dates]
        
        # Calculate price difference
        price_diff = pred_filtered['Close'] - actual_filtered['Close']
        
        # Calculate percentage error
        pct_error = (price_diff / actual_filtered['Close']) * 100
        
        # Calculate direction accuracy
        pred_direction = pred_filtered['Close'].pct_change().fillna(0)
        actual_direction = actual_filtered['Close'].pct_change().fillna(0)
        
        direction_match = (pred_direction * actual_direction) > 0
        direction_accuracy = direction_match.mean() * 100
        
        # Calculate metrics
        metrics = {
            "mean_absolute_error": float(abs(price_diff).mean()),
            "mean_percentage_error": float(abs(pct_error).mean()),
            "direction_accuracy": float(direction_accuracy),
            "correlation": float(pred_filtered['Close'].corr(actual_filtered['Close'])),
            "common_days": len(common_dates)
        }
        
        # Calculate phi-harmonic accuracy
        phi_error = abs(pct_error.mean()) / 100
        phi_accuracy = 1 - phi_error
        
        # Apply phi-harmonic scaling - convert to Decimal first
        phi_accuracy_decimal = Decimal(str(phi_accuracy))
        phi_scaled_accuracy = float(phi_accuracy_decimal * PHI)
        
        metrics["phi_harmonic_accuracy"] = float(phi_scaled_accuracy)
        
        return metrics
    
    def _visualize_comparison(self, predictions, actual_data, symbol, save_path):
        """
        Visualize comparison between predictions and actual data
        
        Args:
            predictions (pd.DataFrame): Predicted data
            actual_data (pd.DataFrame): Actual data
            symbol (str): Market symbol
            save_path (str): Path to save visualization
            
        Returns:
            str: Path to saved visualization
        """
        # Create figure
        plt.figure(figsize=(15, 10))
        
        # Plot prices
        plt.subplot(2, 1, 1)
        plt.title(f"{symbol} - Quantum Prediction vs Actual")
        
        # Plot actual data
        plt.plot(actual_data.index, actual_data['Close'], label='Actual', color='blue', linewidth=2)
        
        # Plot predicted data
        plt.plot(predictions.index, predictions['Close'], label='Predicted', color='red', linestyle='--', linewidth=2)
        
        # Add confidence bands - ensure numeric values
        upper_band = predictions['Close'] * (1 + predictions['Confidence'].astype(float) * 0.1)
        lower_band = predictions['Close'] * (1 - predictions['Confidence'].astype(float) * 0.1)
        
        # Convert to numeric and handle NaN values
        upper_band = pd.to_numeric(upper_band, errors='coerce')
        lower_band = pd.to_numeric(lower_band, errors='coerce')
        
        # Fill NaN values with the Close price
        upper_band = upper_band.fillna(predictions['Close'])
        lower_band = lower_band.fillna(predictions['Close'])
        
        plt.fill_between(predictions.index, lower_band, upper_band, color='red', alpha=0.1)
        
        plt.grid(True, alpha=0.3)
        plt.legend()
        
        # Plot error
        plt.subplot(2, 1, 2)
        plt.title("Prediction Error")
        
        # Align dates
        common_dates = predictions.index.intersection(actual_data.index)
        
        if len(common_dates) > 0:
            # Filter data to common dates
            pred_filtered = predictions.loc[common_dates]
            actual_filtered = actual_data.loc[common_dates]
            
            # Calculate percentage error
            pct_error = ((pred_filtered['Close'] - actual_filtered['Close']) / actual_filtered['Close']) * 100
            
            # Plot error
            plt.bar(common_dates, pct_error, color='gray', alpha=0.7)
            plt.axhline(y=0, color='black', linestyle='-', alpha=0.3)
            
            # Calculate and display accuracy
            direction_match = (pred_filtered['Close'].pct_change() * actual_filtered['Close'].pct_change()) > 0
            direction_accuracy = direction_match.mean() * 100
            
            plt.text(0.02, 0.95, f"Direction Accuracy: {direction_accuracy:.2f}%", 
                    transform=plt.gca().transAxes, fontsize=12)
            plt.text(0.02, 0.90, f"Mean Abs Error: {abs(pct_error).mean():.2f}%", 
                    transform=plt.gca().transAxes, fontsize=12)
        
        plt.grid(True, alpha=0.3)
        
        plt.tight_layout()
        plt.savefig(save_path)
        
        print(f"Comparison visualization saved to {save_path}")
        
        return save_path


def main():
    """Main function to test the market predictor"""
    print("\n🔮 Phi-Harmonic Market Predictor")
    print("=" * 60)
    
    # Initialize predictor
    predictor = PhiHarmonicMarketPredictor()
    
    # Define test parameters
    symbol = "AAPL"  # Example symbol
    
    # For a real backtest, we'd use actual historical dates
    # Here we're using last week's data to predict this week
    today = datetime.datetime.now()
    one_week_ago = today - datetime.timedelta(days=7)
    two_weeks_ago = today - datetime.timedelta(days=14)
    
    training_start = two_weeks_ago.strftime('%Y-%m-%d')
    training_end = one_week_ago.strftime('%Y-%m-%d')
    
    test_start = one_week_ago.strftime('%Y-%m-%d')
    test_end = today.strftime('%Y-%m-%d')
    
    print(f"\nBacktesting {symbol}")
    print(f"Training period: {training_start} to {training_end}")
    print(f"Test period: {test_start} to {test_end}")
    
    # Run backtest
    results = predictor.backtest_predictions(
        symbol, 
        (training_start, training_end), 
        (test_start, test_end)
    )
    
    # Print results
    print("\n📊 Backtest Results")
    print("-" * 60)
    print(f"Direction Accuracy: {results['direction_accuracy']:.2f}%")
    print(f"Mean Absolute Error: {results['mean_absolute_error']:.4f}")
    print(f"Mean Percentage Error: {results['mean_percentage_error']:.2f}%")
    print(f"Correlation: {results['correlation']:.4f}")
    print(f"Phi-Harmonic Accuracy: {results['phi_harmonic_accuracy']:.4f}")
    
    print("\n✨ Quantum Market Prediction complete")
    print("=" * 60)


if __name__ == "__main__":
    main()

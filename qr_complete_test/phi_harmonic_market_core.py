"""
Phi-Harmonic Market Core
Core functionality for market prediction using phi-harmonic principles
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

# Constants
PHI = Decimal('1.618033988749895')  # Golden ratio
PHI_INVERSE = Decimal('0.618033988749895')  # 1/φ
FIBONACCI = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987]

class PhiHarmonicMarketCore:
    """
    Core functionality for market prediction using phi-harmonic principles
    """
    
    def __init__(self):
        """Initialize the market core"""
        # Output directory
        self.output_dir = "phi_harmonic_market"
        os.makedirs(self.output_dir, exist_ok=True)
        
        print(f"Phi-Harmonic Market Core initialized")
    
    def load_market_data(self, symbol, start_date, end_date=None):
        """
        Load market data for a symbol
        
        Args:
            symbol (str): Market symbol (e.g., 'AAPL')
            start_date (str): Start date in 'YYYY-MM-DD' format
            end_date (str, optional): End date in 'YYYY-MM-DD' format
            
        Returns:
            pd.DataFrame: Market data
        """
        # For demonstration, we'll use sample data
        # In a real implementation, this would use an API like yfinance
        
        # Parse dates
        start = datetime.datetime.strptime(start_date, '%Y-%m-%d')
        if end_date:
            end = datetime.datetime.strptime(end_date, '%Y-%m-%d')
        else:
            end = datetime.datetime.now()
        
        # Generate sample data
        days = (end - start).days + 1
        dates = [start + datetime.timedelta(days=i) for i in range(days)]
        
        # Create sample price data with a realistic pattern
        base_price = 100.0
        prices = []
        for i in range(days):
            # Add some randomness and trend
            trend = 0.001 * i  # Slight upward trend
            seasonal = 5 * np.sin(i / 30 * 2 * np.pi)  # 30-day cycle
            noise = np.random.normal(0, 1)  # Random noise
            
            price = base_price * (1 + trend + seasonal / 100 + noise / 100)
            prices.append(max(price, 1.0))  # Ensure price is positive
        
        # Create DataFrame
        df = pd.DataFrame({
            'Date': dates,
            'Open': prices,
            'High': [p * (1 + np.random.uniform(0, 0.02)) for p in prices],
            'Low': [p * (1 - np.random.uniform(0, 0.02)) for p in prices],
            'Close': [p * (1 + np.random.normal(0, 0.005)) for p in prices],
            'Volume': [int(np.random.uniform(1000000, 10000000)) for _ in range(days)]
        })
        
        # Set Date as index
        df['Date'] = pd.to_datetime(df['Date'])
        df.set_index('Date', inplace=True)
        
        print(f"Loaded market data for {symbol} from {start_date} to {end_date or 'now'}")
        print(f"Data points: {len(df)}")
        
        return df
    
    def calculate_phi_patterns(self, data):
        """
        Calculate phi-harmonic patterns in market data
        
        Args:
            data (pd.DataFrame): Market data
            
        Returns:
            pd.DataFrame: Data with phi patterns
        """
        # Create a copy of the data
        df = data.copy()
        
        # Calculate Fibonacci retracement levels
        df['Fib_0'] = df['Close']
        df['Fib_236'] = df['Close'] * (1 - 0.236)
        df['Fib_382'] = df['Close'] * (1 - 0.382)
        df['Fib_500'] = df['Close'] * (1 - 0.5)
        df['Fib_618'] = df['Close'] * (1 - 0.618)
        df['Fib_786'] = df['Close'] * (1 - 0.786)
        df['Fib_1000'] = df['Close'] * (1 - 1.0)
        
        # Calculate Fibonacci extension levels
        df['Ext_0'] = df['Close']
        df['Ext_618'] = df['Close'] * (1 + 0.618)
        df['Ext_1000'] = df['Close'] * (1 + 1.0)
        df['Ext_1618'] = df['Close'] * (1 + 1.618)
        df['Ext_2618'] = df['Close'] * (1 + 2.618)
        
        # Calculate phi-harmonic indicators
        # Simple Moving Average with Fibonacci periods
        for period in [5, 8, 13, 21, 34, 55]:
            df[f'SMA_{period}'] = df['Close'].rolling(window=period).mean()
        
        # Phi-weighted Moving Average
        df['Phi_MA'] = 0.0
        for i, period in enumerate([5, 8, 13, 21]):
            weight = float(PHI_INVERSE ** Decimal(str(i+1)))
            df['Phi_MA'] += df['Close'].rolling(window=period).mean() * weight
        df['Phi_MA'] = df['Phi_MA'] / sum([float(PHI_INVERSE ** Decimal(str(i+1))) for i in range(4)])
        
        # Calculate price momentum
        df['Momentum'] = df['Close'].pct_change(periods=5)
        
        # Calculate phi-harmonic oscillator
        df['Phi_Osc'] = (df['Close'] - df['SMA_13']) / df['SMA_13']
        
        # Calculate golden ratio crossover signals
        df['Golden_Cross'] = np.where(df['SMA_8'] > df['SMA_13'], 1, 0)
        df['Death_Cross'] = np.where(df['SMA_8'] < df['SMA_13'], 1, 0)
        
        return df
    
    def identify_market_patterns(self, data):
        """
        Identify market patterns in the data
        
        Args:
            data (pd.DataFrame): Market data with phi patterns
            
        Returns:
            dict: Identified patterns
        """
        # Create a copy of the data
        df = data.copy()
        
        # Identify trend
        sma_short = df['SMA_8'].iloc[-1]
        sma_long = df['SMA_34'].iloc[-1]
        
        if sma_short > sma_long:
            trend = "Uptrend"
        elif sma_short < sma_long:
            trend = "Downtrend"
        else:
            trend = "Sideways"
        
        # Identify support and resistance levels
        recent_data = df.iloc[-30:]  # Last 30 days
        
        # Find local minima (support)
        support_levels = []
        for i in range(1, len(recent_data)-1):
            if recent_data['Low'].iloc[i] < recent_data['Low'].iloc[i-1] and \
               recent_data['Low'].iloc[i] < recent_data['Low'].iloc[i+1]:
                support_levels.append(recent_data['Low'].iloc[i])
        
        # Find local maxima (resistance)
        resistance_levels = []
        for i in range(1, len(recent_data)-1):
            if recent_data['High'].iloc[i] > recent_data['High'].iloc[i-1] and \
               recent_data['High'].iloc[i] > recent_data['High'].iloc[i+1]:
                resistance_levels.append(recent_data['High'].iloc[i])
        
        # Identify key Fibonacci levels
        current_price = df['Close'].iloc[-1]
        fib_levels = {
            "0.0": float(df['Fib_0'].iloc[-1]),
            "0.236": float(df['Fib_236'].iloc[-1]),
            "0.382": float(df['Fib_382'].iloc[-1]),
            "0.5": float(df['Fib_500'].iloc[-1]),
            "0.618": float(df['Fib_618'].iloc[-1]),
            "0.786": float(df['Fib_786'].iloc[-1]),
            "1.0": float(df['Fib_1000'].iloc[-1]),
            "1.618": float(df['Ext_1618'].iloc[-1]),
            "2.618": float(df['Ext_2618'].iloc[-1])
        }
        
        # Identify phi-harmonic patterns
        patterns = []
        
        # Check for golden cross
        if df['Golden_Cross'].iloc[-1] == 1 and df['Golden_Cross'].iloc[-2] == 0:
            patterns.append("Golden Cross")
        
        # Check for death cross
        if df['Death_Cross'].iloc[-1] == 1 and df['Death_Cross'].iloc[-2] == 0:
            patterns.append("Death Cross")
        
        # Check for phi-harmonic divergence
        price_change = df['Close'].pct_change(periods=5).iloc[-1]
        momentum_change = df['Momentum'].diff().iloc[-1]
        
        if price_change > 0 and momentum_change < 0:
            patterns.append("Bearish Divergence")
        elif price_change < 0 and momentum_change > 0:
            patterns.append("Bullish Divergence")
        
        # Compile results
        results = {
            "trend": trend,
            "current_price": float(current_price),
            "support_levels": [float(level) for level in support_levels],
            "resistance_levels": [float(level) for level in resistance_levels],
            "fibonacci_levels": fib_levels,
            "patterns": patterns
        }
        
        return results
    
    def visualize_market_data(self, data, title="Market Analysis", save_path=None):
        """
        Visualize market data with phi-harmonic patterns
        
        Args:
            data (pd.DataFrame): Market data with phi patterns
            title (str): Plot title
            save_path (str, optional): Path to save the visualization
            
        Returns:
            str: Path to saved visualization
        """
        # Create figure
        plt.figure(figsize=(15, 10))
        
        # Plot price and moving averages
        plt.subplot(2, 1, 1)
        plt.title(f"{title} - Phi-Harmonic Analysis")
        plt.plot(data.index, data['Close'], label='Close Price', color='black', alpha=0.75)
        plt.plot(data.index, data['SMA_8'], label='SMA 8', color='blue', alpha=0.6)
        plt.plot(data.index, data['SMA_13'], label='SMA 13', color='red', alpha=0.6)
        plt.plot(data.index, data['SMA_21'], label='SMA 21', color='green', alpha=0.6)
        plt.plot(data.index, data['Phi_MA'], label='Phi-Weighted MA', color='purple', linestyle='--', alpha=0.8)
        
        # Plot Fibonacci retracement levels for the last point
        last_idx = data.index[-1]
        plt.axhline(y=data['Fib_0'].iloc[-1], color='gray', linestyle='--', alpha=0.3)
        plt.axhline(y=data['Fib_236'].iloc[-1], color='gray', linestyle='--', alpha=0.3)
        plt.axhline(y=data['Fib_382'].iloc[-1], color='gray', linestyle='--', alpha=0.3)
        plt.axhline(y=data['Fib_500'].iloc[-1], color='gray', linestyle='--', alpha=0.3)
        plt.axhline(y=data['Fib_618'].iloc[-1], color='gray', linestyle='--', alpha=0.3)
        
        plt.grid(True, alpha=0.3)
        plt.legend()
        
        # Plot phi-harmonic oscillator
        plt.subplot(2, 1, 2)
        plt.title("Phi-Harmonic Oscillator")
        plt.plot(data.index, data['Phi_Osc'], label='Phi Oscillator', color='blue')
        plt.axhline(y=0, color='black', linestyle='-', alpha=0.3)
        plt.axhline(y=0.05, color='red', linestyle='--', alpha=0.3)
        plt.axhline(y=-0.05, color='green', linestyle='--', alpha=0.3)
        
        # Plot golden and death crosses
        plt.scatter(data[data['Golden_Cross'] == 1].index, 
                   data[data['Golden_Cross'] == 1]['Phi_Osc'],
                   color='green', marker='^', label='Golden Cross')
        plt.scatter(data[data['Death_Cross'] == 1].index, 
                   data[data['Death_Cross'] == 1]['Phi_Osc'],
                   color='red', marker='v', label='Death Cross')
        
        plt.grid(True, alpha=0.3)
        plt.legend()
        
        plt.tight_layout()
        
        # Save if path provided
        if save_path:
            plt.savefig(save_path)
            print(f"Visualization saved to {save_path}")
        
        return save_path
    
    def save_analysis(self, symbol, data, patterns, save_path=None):
        """
        Save market analysis to file
        
        Args:
            symbol (str): Market symbol
            data (pd.DataFrame): Market data
            patterns (dict): Identified patterns
            save_path (str, optional): Path to save the analysis
            
        Returns:
            str: Path to saved analysis
        """
        # Create timestamp for filename
        timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
        
        if not save_path:
            save_path = os.path.join(self.output_dir, f"{symbol}_analysis_{timestamp}.json")
        
        # Prepare data for saving
        analysis = {
            "symbol": symbol,
            "timestamp": timestamp,
            "data_points": len(data),
            "date_range": {
                "start": data.index[0].strftime('%Y-%m-%d'),
                "end": data.index[-1].strftime('%Y-%m-%d')
            },
            "last_price": float(data['Close'].iloc[-1]),
            "patterns": patterns
        }
        
        # Save to file
        with open(save_path, 'w') as f:
            json.dump(analysis, f, indent=4)
        
        print(f"Analysis saved to {save_path}")
        
        return save_path

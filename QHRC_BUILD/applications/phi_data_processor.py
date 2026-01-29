import numpy as np
from typing import List, Dict, Tuple, Optional
import math

class PhiDataProcessor:
    def __init__(self):
        self.phi = (1 + np.sqrt(5)) / 2
        self.base_freq = 4.37  # Proven base frequency
        self.resonance = 0.96  # Target resonance
        
    def phi_compress(self, data: np.ndarray) -> Tuple[np.ndarray, Dict]:
        """Compress data using φ-based patterns"""
        # Calculate φ-based frequency components
        fft_data = np.fft.fft(data)
        
        # Calculate magnitude spectrum
        magnitude = np.abs(fft_data)
        
        # Find φ-based threshold
        threshold = np.max(magnitude) / self.phi
        
        # Keep only components above threshold
        mask = magnitude > threshold
        compressed_fft = fft_data * mask
        
        # Store compression metadata
        metadata = {
            'original_size': data.size,
            'compressed_size': np.count_nonzero(mask),
            'phi_ratio': self.phi,
            'threshold': threshold,
            'compression_ratio': data.size / np.count_nonzero(mask)
        }
        
        return compressed_fft, metadata
    
    def phi_decompress(self, compressed_fft: np.ndarray, metadata: Dict) -> np.ndarray:
        """Decompress φ-compressed data"""
        # Inverse FFT to recover data
        return np.fft.ifft(compressed_fft).real
    
    def phi_pattern_match(self, data: np.ndarray, pattern: np.ndarray) -> List[int]:
        """Find pattern matches using φ-based correlation"""
        # Calculate correlation
        correlation = np.correlate(data, pattern, mode='valid')
        
        # Find φ-based threshold
        threshold = np.max(correlation) / self.phi
        
        # Find matches
        matches = np.where(correlation > threshold)[0]
        
        return matches.tolist()
    
    def phi_filter(self, data: np.ndarray, level: int) -> np.ndarray:
        """Apply φ-based filter to data"""
        # Calculate FFT
        fft_data = np.fft.fft(data)
        
        # Create φ-based filter
        n = len(data)
        filter_mask = np.zeros(n)
        
        # Set cutoff frequency based on φ
        cutoff = int(n / (self.phi ** level))
        filter_mask[:cutoff] = 1
        
        # Apply filter
        filtered_fft = fft_data * filter_mask
        
        # Inverse FFT
        return np.fft.ifft(filtered_fft).real
    
    def phi_cluster(self, data: np.ndarray, k: int, max_iter: int = 100) -> Tuple[np.ndarray, np.ndarray]:
        """Cluster data using φ-based k-means"""
        n_samples, n_features = data.shape
        
        # Initialize centroids with φ-based spacing
        indices = np.random.choice(n_samples, 1)
        centroids = data[indices]
        
        for i in range(1, k):
            # Calculate distances to existing centroids
            distances = np.min(np.sum((data[:, np.newaxis, :] - centroids[np.newaxis, :, :]) ** 2, axis=2), axis=1)
            
            # Choose next centroid with φ-weighted probability
            phi_weights = distances ** self.phi
            phi_weights /= np.sum(phi_weights)
            next_centroid = np.random.choice(n_samples, 1, p=phi_weights)
            centroids = np.vstack([centroids, data[next_centroid]])
        
        # Run φ-based k-means
        for _ in range(max_iter):
            # Assign points to clusters
            distances = np.sum((data[:, np.newaxis, :] - centroids[np.newaxis, :, :]) ** 2, axis=2)
            labels = np.argmin(distances, axis=1)
            
            # Update centroids
            new_centroids = np.zeros_like(centroids)
            for j in range(k):
                if np.sum(labels == j) > 0:
                    new_centroids[j] = np.mean(data[labels == j], axis=0)
            
            # Check convergence with φ-based threshold
            shift = np.sum((new_centroids - centroids) ** 2)
            if shift < 1.0 / self.phi:
                break
                
            centroids = new_centroids
        
        return centroids, labels
    
    def phi_forecast(self, data: np.ndarray, horizon: int) -> np.ndarray:
        """Forecast time series using φ-based patterns"""
        n = len(data)
        
        # Find φ-based pattern length
        pattern_length = int(n / self.phi)
        
        # Extract recent pattern
        recent = data[-pattern_length:]
        
        # Calculate φ-weighted forecast
        forecast = np.zeros(horizon)
        
        for i in range(horizon):
            # Use φ-weighted combination of patterns
            weights = np.power(self.phi, -np.arange(1, pattern_length+1))
            weights = weights / np.sum(weights)
            
            # Circular pattern matching with φ-based weighting
            idx = i % pattern_length
            forecast[i] = np.sum(recent * np.roll(weights, idx))
        
        return forecast

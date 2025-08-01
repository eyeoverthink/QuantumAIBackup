"""
Real-time Video Stream Processor with φ-Harmonic Scaling
"""

import cv2
import numpy as np
from typing import Tuple, Dict
from quantum_phi_scaling import QuantumPhiScaling
from quantum_memory_test import QuantumMemoryTest

class VideoStreamProcessor:
    def __init__(self, buffer_size: int = 1024 * 1024):
        self.memory = QuantumMemoryTest(initial_size=buffer_size)
        self.scaler = QuantumPhiScaling()
        self.phi = (1 + np.sqrt(5)) / 2
        
        # Frame buffer parameters
        self.frame_count = 0
        self.quality = 100  # Initial JPEG quality
        
    def compress_frame(self, frame: np.ndarray, quality: int) -> Tuple[bytes, float]:
        """Compress frame using JPEG with φ-harmonic quality scaling"""
        encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), quality]
        result, encoded = cv2.imencode('.jpg', frame, encode_param)
        
        if not result:
            raise ValueError("Frame compression failed")
            
        compression_ratio = len(encoded.tobytes()) / (frame.shape[0] * frame.shape[1] * frame.shape[2])
        return encoded.tobytes(), compression_ratio
        
    def decompress_frame(self, frame_data: bytes) -> np.ndarray:
        """Decompress frame data back to numpy array"""
        nparr = np.frombuffer(frame_data, np.uint8)
        return cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        
    def process_frame(self, frame: np.ndarray) -> Dict:
        """Process a single video frame with φ-harmonic scaling"""
        self.frame_count += 1
        
        # Get current memory stats
        stats = self.memory.get_memory_stats()
        
        # Adjust quality based on memory pressure
        if stats['utilization'] > 0.8:
            # Scale down quality by φ
            self.quality = int(self.quality / self.phi)
        elif stats['utilization'] < 0.5:
            # Scale up quality toward 100, but not exceeding it
            self.quality = min(100, int(self.quality * self.phi))
            
        # Compress frame with current quality
        frame_data, compression_ratio = self.compress_frame(frame, self.quality)
        
        # Store in memory with auto-scaling
        warning, results = self.memory.add_data(list(frame_data))
        
        if warning:
            # Clean up old frames if needed
            self.cleanup_old_frames()
            
        return {
            'frame_number': self.frame_count,
            'quality': self.quality,
            'compression_ratio': compression_ratio,
            'memory_utilization': results['after']['utilization'],
            'phi_efficiency': results['after']['phi_efficiency']
        }
        
    def cleanup_old_frames(self):
        """Remove oldest frames using φ-harmonic pattern"""
        stats = self.memory.get_memory_stats()
        
        # Calculate cleanup target using φ
        cleanup_target = int(stats['total_used'] / self.phi)
        
        # Remove oldest blocks until we reach target
        while stats['total_used'] > cleanup_target and self.memory.blocks:
            oldest_block = self.memory.blocks[0]
            self.memory.blocks.pop(0)
            stats = self.memory.get_memory_stats()

def process_video(video_path: str, output_path: str = None):
    """Process a video file with φ-harmonic scaling"""
    # Initialize video capture
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        raise ValueError("Could not open video file")
        
    # Get video properties
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    
    # Initialize processor
    processor = VideoStreamProcessor(buffer_size=frame_width * frame_height * 3)  # 3 channels (RGB)
    
    # Initialize output video if path provided
    out = None
    if output_path:
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        out = cv2.VideoWriter(output_path, fourcc, fps, (frame_width, frame_height))
    
    print("\nProcessing Video with φ-Harmonic Scaling")
    print("=======================================")
    print(f"Resolution: {frame_width}x{frame_height}")
    print(f"FPS: {fps}")
    
    try:
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
                
            # Process frame
            stats = processor.process_frame(frame)
            
            # Display stats every 30 frames
            if stats['frame_number'] % 30 == 0:
                print(f"\nFrame {stats['frame_number']}:")
                print(f"Quality: {stats['quality']}%")
                print(f"Compression: {stats['compression_ratio']:.3f}")
                print(f"Memory Used: {stats['memory_utilization']*100:.1f}%")
                print(f"φ-Efficiency: {stats['phi_efficiency']:.3f}")
            
            # Write output frame if needed
            if out is not None:
                out.write(frame)
                
    finally:
        cap.release()
        if out is not None:
            out.release()
        cv2.destroyAllWindows()
        
    # Final stats
    final_stats = processor.memory.get_memory_stats()
    print("\nFinal Processing Stats:")
    print(f"Frames Processed: {processor.frame_count}")
    print(f"Final Quality: {processor.quality}%")
    print(f"Memory Blocks: {final_stats['block_count']}")
    print(f"Compressed Blocks: {final_stats['compressed_blocks']}")
    print(f"φ-Efficiency: {final_stats['phi_efficiency']:.3f}")

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python video_processor.py <input_video> [output_video]")
        sys.exit(1)
        
    input_path = sys.argv[1]
    output_path = sys.argv[2] if len(sys.argv) > 2 else None
    
    process_video(input_path, output_path)

#!/usr/bin/env python3
"""
Test file lacking self-evolution capabilities for MoA integration testing.
"""

class DataProcessor:
    """A simple data processor class without evolution capabilities."""
    
    def __init__(self):
        self.data = []
        self.processed = False
    
    def load_data(self, data):
        """Load data into the processor."""
        self.data = data
        self.processed = False
    
    def process(self):
        """Process the loaded data."""
        if not self.data:
            return []
        
        result = []
        for item in self.data:
            result.append(item * 2)
        
        self.processed = True
        return result
    
    def get_status(self):
        """Get the processor status."""
        return {
            "data_loaded": len(self.data) > 0,
            "processed": self.processed
        }

if __name__ == "__main__":
    processor = DataProcessor()
    processor.load_data([1, 2, 3, 4, 5])
    result = processor.process()
    print(f"Processed data: {result}")
    print(f"Status: {processor.get_status()}")

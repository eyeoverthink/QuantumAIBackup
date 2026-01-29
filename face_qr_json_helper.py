#!/usr/bin/env python3
"""
Face QR JSON Helper

This module provides JSON serialization helpers for the Face-QR system,
ensuring that all data structures can be properly serialized and deserialized.
"""

import json
import numpy as np
from datetime import datetime

class FaceQRJSONEncoder(json.JSONEncoder):
    """
    Custom JSON encoder for Face-QR data structures.
    Handles special data types like numpy arrays, datetime objects, etc.
    """
    
    def default(self, obj):
        """
        Handle special data types for JSON serialization.
        
        Args:
            obj: Object to serialize
            
        Returns:
            JSON serializable object
        """
        # Handle numpy arrays
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        
        # Handle numpy data types
        if isinstance(obj, (np.int_, np.intc, np.intp, np.int8, np.int16, np.int32,
                           np.int64, np.uint8, np.uint16, np.uint32, np.uint64)):
            return int(obj)
        
        if isinstance(obj, (np.float_, np.float16, np.float32, np.float64)):
            return float(obj)
        
        if isinstance(obj, np.bool_):
            return bool(obj)
        
        # Handle datetime objects
        if isinstance(obj, datetime):
            return obj.isoformat()
        
        # Let the base class handle it (or raise TypeError)
        return super().default(obj)

def json_dump(obj, fp, **kwargs):
    """
    Dump object to JSON file with custom encoder.
    
    Args:
        obj: Object to serialize
        fp: File-like object
        **kwargs: Additional arguments for json.dump
    """
    return json.dump(obj, fp, cls=FaceQRJSONEncoder, **kwargs)

def json_dumps(obj, **kwargs):
    """
    Dump object to JSON string with custom encoder.
    
    Args:
        obj: Object to serialize
        **kwargs: Additional arguments for json.dumps
        
    Returns:
        str: JSON string
    """
    return json.dumps(obj, cls=FaceQRJSONEncoder, **kwargs)

def json_load(fp, **kwargs):
    """
    Load JSON from file.
    
    Args:
        fp: File-like object
        **kwargs: Additional arguments for json.load
        
    Returns:
        Deserialized object
    """
    return json.load(fp, **kwargs)

def json_loads(s, **kwargs):
    """
    Load JSON from string.
    
    Args:
        s: JSON string
        **kwargs: Additional arguments for json.loads
        
    Returns:
        Deserialized object
    """
    return json.loads(s, **kwargs)

# Test function
if __name__ == "__main__":
    # Test data with various types
    test_data = {
        "int": 42,
        "float": 3.14159,
        "bool": True,
        "str": "Hello, world!",
        "list": [1, 2, 3, 4, 5],
        "dict": {"a": 1, "b": 2},
        "numpy_int": np.int64(42),
        "numpy_float": np.float64(3.14159),
        "numpy_bool": np.bool_(True),
        "numpy_array": np.array([1, 2, 3, 4, 5]),
        "datetime": datetime.now()
    }
    
    # Test serialization
    json_str = json_dumps(test_data, indent=2)
    print("Serialized JSON:")
    print(json_str)
    
    # Test deserialization
    deserialized = json_loads(json_str)
    print("\nDeserialized data:")
    print(deserialized)

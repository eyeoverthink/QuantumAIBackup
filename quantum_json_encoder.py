"""
Custom JSON encoder for quantum system data types
"""

import json
import numpy as np

class QuantumJSONEncoder(json.JSONEncoder):
    """Custom JSON encoder that handles numpy arrays and other complex types"""
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        if isinstance(obj, (np.integer, np.int64)):
            return int(obj)
        if isinstance(obj, (np.floating, np.float64)):
            return float(obj)
        if isinstance(obj, np.bool_):
            return bool(obj)
        if isinstance(obj, np.complex_):
            return str(obj)
        if hasattr(obj, 'tolist'):
            return obj.tolist()
        return str(obj)

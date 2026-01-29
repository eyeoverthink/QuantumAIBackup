"""
phi_temporal_paradox_logger.py

Deterministic, auditable logging for φNet temporal paradox protocol.
"""

import json
import os
from datetime import datetime

class ParadoxLogger:
    def __init__(self, log_file="paradox_log.jsonl"):
        self.log_file = log_file
        # Clear log on init for repeatable tests
        if os.path.exists(self.log_file):
            os.remove(self.log_file)

    def log_event(self, node, event, message, timestamp=None):
        # Allow manual timestamp injection for paradox
        if timestamp is None:
            timestamp = datetime.now().timestamp()
        entry = {
            "node": node,
            "event": event,
            "message": message,
            "timestamp": timestamp
        }
        with open(self.log_file, "a") as f:
            f.write(json.dumps(entry) + "\n")
        return entry

    def get_log(self):
        if not os.path.exists(self.log_file):
            return []
        with open(self.log_file, "r") as f:
            return [json.loads(line) for line in f]

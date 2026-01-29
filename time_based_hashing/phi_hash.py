import hashlib
import datetime
from .temporal_key import TemporalKey

class PhiHasher:
    """
    Creates a time-dependent hash of data using a TemporalKey.
    """
    def __init__(self, data: str, timestamp: datetime.datetime = None):
        """
        Initializes the hasher.

        Args:
            data (str): The data to be hashed.
            timestamp (datetime.datetime, optional): The timestamp for the hash.
                If None, the current time is used.
        """
        self.data = data
        self.timestamp = timestamp or datetime.datetime.now(datetime.timezone.utc)
        self.temporal_key = TemporalKey(self.timestamp)
        self.hash = self._generate_hash()

    def _generate_hash(self) -> str:
        """
        Generates the final phi-hash.

        The process is:
        1. Get the secret key from the TemporalKey.
        2. Concatenate the key with the input data.
        3. Hash the combined string with SHA-256.
        """
        key = self.temporal_key.get_key()
        
        # Combine the key and data
        combined_data = f"{key}:{self.data}"
        
        # Hash the combined data
        hasher = hashlib.sha256(combined_data.encode('utf-8'))
        return hasher.hexdigest()

    def get_hash(self) -> str:
        """Returns the generated phi-hash."""
        return self.hash

    def __repr__(self) -> str:
        return f"PhiHash(timestamp='{self.timestamp.isoformat()}', hash='{self.hash}')"

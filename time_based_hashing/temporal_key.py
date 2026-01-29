import datetime
from decimal import Decimal, getcontext
import hashlib

# --- Constants ---
getcontext().prec = 100
PHI = (Decimal(1) + Decimal(5).sqrt()) / Decimal(2)

class TemporalKey:
    """
    Generates a dynamic, time-sensitive key based on phi-harmonic principles.
    The key's value is derived from the precise number of seconds elapsed since
    the Unix epoch, modulated by the golden ratio.
    """
    def __init__(self, timestamp: datetime.datetime = None):
        """
        Initializes the temporal key.

        Args:
            timestamp (datetime.datetime, optional): The timestamp to use.
                If None, the current UTC time is used.
        """
        self.timestamp = timestamp or datetime.datetime.now(datetime.timezone.utc)
        self.key = self._generate_key()

    def _generate_key(self) -> str:
        """
        Creates the key by combining the timestamp with PHI.

        The process involves:
        1. Getting the high-precision timestamp in seconds.
        2. Multiplying it by PHI to create a phi-harmonic value.
        3. Hashing the result to create a secure, fixed-length key.
        """
        # Get timestamp as a high-precision Decimal
        ts_decimal = Decimal(self.timestamp.timestamp())

        # Modulate with PHI
        phi_modulated_value = ts_decimal * PHI

        # Convert to string for hashing
        value_str = str(phi_modulated_value)

        # Hash using SHA-256 for a secure, fixed-length key
        hasher = hashlib.sha256(value_str.encode('utf-8'))
        return hasher.hexdigest()

    def __repr__(self) -> str:
        return f"TemporalKey(timestamp='{self.timestamp.isoformat()}', key='{self.key[:12]}...')"

    def get_key(self) -> str:
        """Returns the generated key."""
        return self.key

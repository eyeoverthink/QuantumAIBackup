import socket
import datetime

# Get the computer's hostname
hostname = socket.gethostname()

# Get the current timestamp
timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Print the result
print(f"Hello {hostname}! Timestamp: {timestamp}")

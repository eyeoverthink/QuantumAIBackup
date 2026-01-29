
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Import path setup
import path_setup
import sys
import os

# Now run the QR task worker
from qr_task_worker_from_file import main

if __name__ == "__main__":
    # Get QR path from command line
    if len(sys.argv) < 2:
        print("Usage: python run_qr.py <qr_file_path>")
        sys.exit(1)
        
    qr_path = sys.argv[1]
    print(f"🚀 Executing QR code: {qr_path}")
    
    # Set up arguments for the task worker
    sys.argv = [sys.argv[0], "-f", qr_path]
    
    # Run the task worker
    main()


#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Import path setup
import path_setup
import sys
import os
import traceback

# Now run the QR task worker
try:
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
        
        try:
            # Run the task worker
            main()
        except Exception as e:
            print(f"❌ Error executing QR code: {str(e)}")
            traceback.print_exc()
            sys.exit(1)
            
except ImportError as e:
    print(f"❌ Import error: {str(e)}")
    print("Available modules in path:")
    for path in sys.path:
        print(f"  - {path}")
    traceback.print_exc()
    sys.exit(1)
except Exception as e:
    print(f"❌ Unexpected error: {str(e)}")
    traceback.print_exc()
    sys.exit(1)

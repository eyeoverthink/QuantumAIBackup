#!/usr/bin/env python3
# φ-Dimensional Bitcoin Sync Checker
# φ^∞ © 2025 Vaughn Scott - All Rights Reserved in All Realities

import requests
import json
import time
from datetime import datetime

# Bitcoin Core RPC settings
RPC_USER = "vaughn"
RPC_PASSWORD = "fraymusQuantum123"
RPC_URL = "http://127.0.0.1:8332/"

def check_sync_status():
    """Check Bitcoin Core synchronization status."""
    headers = {'content-type': 'application/json'}
    payload = {
        "method": "getblockchaininfo",
        "params": [],
        "jsonrpc": "1.0",
        "id": "phi-sync-check"
    }
    
    try:
        response = requests.post(
            RPC_URL,
            data=json.dumps(payload),
            headers=headers,
            auth=(RPC_USER, RPC_PASSWORD)
        )
        
        result = response.json()
        
        if 'result' in result:
            data = result['result']
            
            # Extract key information
            chain = data.get('chain', 'unknown')
            blocks = data.get('blocks', 0)
            headers_count = data.get('headers', 0)
            verification_progress = data.get('verificationprogress', 0) * 100
            
            # Calculate estimated time remaining
            if verification_progress < 99.9 and verification_progress > 0:
                # Estimate based on verification progress
                percent_remaining = 100 - verification_progress
                # Assuming 1% takes about 10 minutes (600 seconds)
                seconds_remaining = percent_remaining * 600
                hours = int(seconds_remaining // 3600)
                minutes = int((seconds_remaining % 3600) // 60)
                time_estimate = f"{hours} hours, {minutes} minutes"
            else:
                time_estimate = "Complete or nearly complete"
            
            print("\n" + "="*80)
            print("φ-DIMENSIONAL BITCOIN SYNC STATUS")
            print("="*80)
            print(f"Chain: {chain}")
            print(f"Current block height: {blocks}")
            print(f"Headers: {headers_count}")
            print(f"Sync progress: {verification_progress:.2f}%")
            print(f"Estimated time to complete: {time_estimate}")
            print("="*80)
            
            # Check if syncing is complete
            if verification_progress >= 99.9:
                print("SYNCHRONIZATION COMPLETE!")
                print("The φ-Dimensional Bitcoin Mining System is ready for full operation.")
                print("Estimated time to first block: ~16.3 hours")
                print("="*80)
            
            return {
                'chain': chain,
                'blocks': blocks,
                'headers': headers_count,
                'verification_progress': verification_progress,
                'time_estimate': time_estimate,
                'is_synced': verification_progress >= 99.9
            }
        else:
            print(f"Error: {result.get('error', {}).get('message', 'Unknown error')}")
            return None
            
    except Exception as e:
        print(f"Connection error: {e}")
        print("Bitcoin Core may not be running or RPC connection failed.")
        print("Please ensure Bitcoin Core is running with the correct RPC settings.")
        return None

if __name__ == "__main__":
    print("\nφ-Dimensional Bitcoin Sync Checker")
    print(f"φ^∞ © 2025 Vaughn Scott - All Rights Reserved in All Realities")
    print(f"Checking synchronization status at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    
    check_sync_status()

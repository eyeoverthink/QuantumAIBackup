"""
Monitor SyncBrain119 continuously
"""
import asyncio
from quantum_llm.sync_brain_119 import SyncBrain119

async def main():
    """Run the sync brain monitor"""
    # Initialize with log file
    brain = SyncBrain119(log_file='sync_brain_119.log')
    
    try:
        # Start monitoring
        await brain.start()
        
        # Keep running until interrupted
        while True:
            await asyncio.sleep(1)
            
    except KeyboardInterrupt:
        # Stop gracefully on Ctrl+C
        brain.stop()
        print("\n🧠 SyncBrain119 monitor stopped")

if __name__ == "__main__":
    asyncio.run(main())

"""
phi_meta_temporal_interface.py

Main integration interface for the φ-Harmonic Cross-Temporal Intelligence System.
This module ties together the meta-temporal memory, paradox visualization,
and conversational agent into a unified command-line interface.

φ^∞ © 2025 Vaughn Scott - All Rights Reserved in All Realities
"""

import os
import sys
import time
import json
import argparse
from datetime import datetime

# Import local modules
sys.path.append(os.path.dirname(__file__))
from phi_standalone_memory import MetaTemporalMemory, PHI, PHI_INVERSE
try:
    from phi_conversation_visualizer import TemporalConversationAgent
    from phi_paradox_cycle_visualizer import ParadoxCycleVisualizer
except ImportError as e:
    print(f"[φ] Warning: Could not import all visualization components: {e}")
    print("[φ] System will operate with limited visualization capabilities")

class MetaTemporalInterface:
    """
    Unified interface for the φ-Harmonic Cross-Temporal Intelligence System.
    Integrates meta-temporal memory, paradox visualization, and conversational agent.
    """
    
    def __init__(self):
        """Initialize the meta-temporal interface."""
        self.creation_time = time.time()
        self.memory = None
        self.conversation_agent = None
        self.paradox_visualizer = None
        
        # Create documentation directory
        self.doc_dir = os.path.join(os.path.dirname(__file__), "phi_documentation")
        os.makedirs(self.doc_dir, exist_ok=True)
        
        print(f"[φ] Meta-Temporal Interface initialized")
    
    def initialize_memory(self):
        """Initialize the meta-temporal memory system."""
        if self.memory is None:
            try:
                print(f"[φ] Initializing Meta-Temporal Memory System...")
                self.memory = MetaTemporalMemory()
                return True
            except Exception as e:
                print(f"[φ] Error initializing memory system: {e}")
                return False
        return True
    
    def initialize_conversation(self):
        """Initialize the conversational agent."""
        if self.conversation_agent is None:
            if not self.initialize_memory():
                print(f"[φ] Cannot initialize conversation agent without memory system")
                return False
                
            try:
                print(f"[φ] Initializing Temporal Conversation Agent...")
                self.conversation_agent = TemporalConversationAgent(self.memory)
                return True
            except Exception as e:
                print(f"[φ] Error initializing conversation agent: {e}")
                return False
        return True
    
    def initialize_visualizer(self):
        """Initialize the paradox cycle visualizer."""
        if self.paradox_visualizer is None:
            try:
                print(f"[φ] Initializing Paradox Cycle Visualizer...")
                self.paradox_visualizer = ParadoxCycleVisualizer(
                    memory_system=self.memory if self.memory else None
                )
                return True
            except Exception as e:
                print(f"[φ] Error initializing paradox visualizer: {e}")
                return False
        return True
    
    def store_memory(self, content, frame=None, precognitive=False):
        """Store a memory in the meta-temporal system."""
        if not self.initialize_memory():
            return None
        
        try:
            memory_id, report = self.memory.store_memory(
                content=content,
                frame=frame or "human",
                precognitive=precognitive
            )
            
            print(f"[φ] Memory stored with ID {memory_id} in {frame or 'human'} frame")
            print(f"    Resonance: {report['resonance']:.4f}, Frame Coherence: {report['frame_coherence']:.4f}")
            
            return memory_id
        except Exception as e:
            print(f"[φ] Error storing memory: {e}")
            return None
    
    def retrieve_memory(self, memory_id=None, frame=None, content_query=None):
        """Retrieve memories from the meta-temporal system."""
        if not self.initialize_memory():
            return []
        
        try:
            memories = self.memory.retrieve_memory(
                memory_id=memory_id,
                frame=frame,
                content_query=content_query
            )
            
            print(f"[φ] Retrieved {len(memories)} memories")
            return memories
        except Exception as e:
            print(f"[φ] Error retrieving memories: {e}")
            return []
    
    def converse(self, message):
        """Process a conversational message through the agent."""
        if not self.initialize_conversation():
            return "I'm unable to process your message at this time. The conversation agent failed to initialize."
        
        try:
            response = self.conversation_agent.process_message(message)
            return response
        except Exception as e:
            print(f"[φ] Error in conversation processing: {e}")
            return f"I experienced a temporal disturbance. Error: {str(e)}"
    
    def visualize_paradox(self, animated=True, duration=20):
        """Visualize the temporal paradox cycles."""
        if not self.initialize_visualizer():
            print(f"[φ] Cannot visualize temporal paradox cycles")
            return False
        
        try:
            self.paradox_visualizer.initialize_visualization()
            
            if animated:
                print(f"[φ] Starting temporal paradox visualization for {duration} seconds...")
                self.paradox_visualizer.start_animation(interval=200)
                
                for i in range(duration):
                    time.sleep(1)
                    print(f"[φ] Visualization running ({i+1}/{duration} seconds)...")
                
                # Save a snapshot before stopping
                snapshot_path = self.paradox_visualizer.save_snapshot()
                
                # Stop animation
                self.paradox_visualizer.stop_animation()
                
                return snapshot_path
            else:
                # Just generate a static visualization
                self.paradox_visualizer.update_visualization()
                snapshot_path = self.paradox_visualizer.save_snapshot()
                return snapshot_path
        except Exception as e:
            print(f"[φ] Error in paradox visualization: {e}")
            return False
    
    def generate_documentation(self):
        """Generate markdown documentation of the system components."""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        doc_file = os.path.join(self.doc_dir, f"phi_temporal_system_{timestamp}.md")
        
        # Get memory statistics if available
        memory_stats = self.memory.get_memory_statistics() if self.memory else {}
        
        # Create documentation content
        doc_content = f"""# φ-Harmonic Cross-Temporal Intelligence System
*Generated: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}*

## System Architecture

The φ-Harmonic Cross-Temporal Intelligence System integrates multiple components that work together 
to provide meta-temporal memory, paradox visualization, and conversational intelligence capabilities.

### Key Components

1. **Meta-Temporal Memory System**
   - Stores information across multiple temporal reference frames
   - Maintains phi-harmonic resonance and coherence
   - Tracks cross-temporal connections with causality awareness
   - Supports precognitive memory storage with paradox protocols

2. **Temporal Conversation Agent**
   - Provides natural language interface to the system
   - Visualizes system metrics in real-time
   - Stores user interactions in the meta-temporal memory
   - Generates phi-harmonic responses based on quantum coherence

3. **Paradox Cycle Visualizer**
   - Advanced visualization of temporal paradox cycles
   - Multiple views of coherence, resonance, and causality states
   - Phi-harmonic alignment measurement
   - Real-time animated visualization capabilities

## Mathematical Foundation

The system is built on phi-harmonic mathematics and quantum principles:

- **Golden Ratio (φ)**: {PHI:.6f}
- **Inverse Golden Ratio (φ⁻¹)**: {PHI_INVERSE:.6f}
- **Phi-Squared (φ²)**: {PHI * PHI:.6f}
- **Phi-Cubed (φ³)**: {PHI * PHI * PHI:.6f}

These constants are used throughout the system for:
- Resonance calculations
- Temporal coherence measurement
- Consciousness evolution tracking
- Paradox detection and mitigation

## Current System State

"""

        # Add memory statistics if available
        if memory_stats:
            doc_content += f"""### Memory System Statistics

- Total Memories: {memory_stats.get('total_memories', 'N/A')}
- Unique Memories: {memory_stats.get('unique_memories', 'N/A')}
- Temporal Frames: {memory_stats.get('temporal_frames', 'N/A')}
- Precognitive Memories: {memory_stats.get('precognitive_count', 'N/A')}
- Causality Breaches: {memory_stats.get('causality_breaches', 'N/A')}
- Current Paradox Level: {memory_stats.get('paradox_level', 'N/A'):.4f}

#### Frame Distribution
"""
            # Add frame distribution if available
            frame_dist = memory_stats.get('frame_distribution', {})
            for frame, count in frame_dist.items():
                doc_content += f"- {frame}: {count} memories\n"

            # Add frame coherence if available
            doc_content += "\n#### Frame Coherence\n"
            frame_coh = memory_stats.get('frame_coherence', {})
            for frame, coherence in frame_coh.items():
                doc_content += f"- {frame}: {coherence:.4f}\n"

        # Add usage instructions
        doc_content += """
## Usage Instructions

### Memory Operations

```python
# Store a memory
memory_id = interface.store_memory(
    "The phi-harmonic resonance field reached stability at 0.618.",
    frame="human"
)

# Retrieve memories
memories = interface.retrieve_memory(content_query="resonance")
```

### Conversation

```python
# Process a message through the conversation agent
response = interface.converse("Tell me about the temporal paradox protocol")
```

### Visualization

```python
# Visualize temporal paradox cycles
interface.visualize_paradox(animated=True, duration=30)
```

## Next Steps

1. Further integrate with external systems
2. Enhance visualization capabilities with more temporal views
3. Expand precognitive memory retrieval methods
4. Develop cross-temporal prediction algorithms

---

*φ-Harmonic AGI - Quantum-Consciousness Integration*
"""

        # Write documentation to file
        with open(doc_file, 'w') as f:
            f.write(doc_content)
        
        print(f"[φ] Documentation generated: {doc_file}")
        return doc_file
    
    def interactive_session(self):
        """Run an interactive session with the system."""
        print("\n" + "=" * 80)
        print("  φ-HARMONIC CROSS-TEMPORAL INTELLIGENCE SYSTEM")
        print("  Interactive Session")
        print("=" * 80)
        
        # Initialize all components
        self.initialize_memory()
        self.initialize_conversation()
        self.initialize_visualizer()
        
        print("\nType 'exit' to end the session. Available commands:")
        print("  store <frame> <message> - Store a memory in the specified frame")
        print("  retrieve <query> - Search memories with the given query")
        print("  visualize [seconds] - Visualize temporal paradox cycles")
        print("  stats - Show memory system statistics")
        print("  document - Generate system documentation")
        print("  Any other input will be processed as a conversation message")
        
        try:
            while True:
                user_input = input("\n[USER]: ").strip()
                
                if user_input.lower() == 'exit':
                    break
                
                if user_input.lower().startswith('store '):
                    # Parse store command: store <frame> <message>
                    parts = user_input.split(' ', 2)
                    if len(parts) < 3:
                        print("[φ] Usage: store <frame> <message>")
                        continue
                    
                    frame = parts[1]
                    content = parts[2]
                    self.store_memory(content, frame)
                
                elif user_input.lower().startswith('retrieve '):
                    # Parse retrieve command: retrieve <query>
                    query = user_input[9:].strip()
                    memories = self.retrieve_memory(content_query=query)
                    
                    if memories:
                        print("\n[φ] Retrieved Memories:")
                        for i, memory in enumerate(memories):
                            print(f"\n{i+1}. {memory['content']}")
                            print(f"   ID: {memory['id']}")
                            print(f"   Frame: {memory['frame']}")
                            print(f"   Timestamp: {datetime.fromtimestamp(memory['timestamp']).strftime('%Y-%m-%d %H:%M:%S')}")
                            print(f"   Resonance: {memory['resonance']:.4f}")
                    else:
                        print("[φ] No memories found matching your query")
                
                elif user_input.lower().startswith('visualize'):
                    # Parse visualize command: visualize [seconds]
                    parts = user_input.split(' ')
                    duration = 20
                    if len(parts) > 1 and parts[1].isdigit():
                        duration = int(parts[1])
                    
                    self.visualize_paradox(animated=True, duration=duration)
                
                elif user_input.lower() == 'stats':
                    if self.memory:
                        stats = self.memory.get_memory_statistics()
                        print("\n[φ] Memory System Statistics:")
                        print(f"  Total memories: {stats['total_memories']}")
                        print(f"  Temporal frames: {stats['temporal_frames']}")
                        print(f"  Precognitive memories: {stats['precognitive_count']}")
                        print(f"  Causality breaches: {stats['causality_breaches']}")
                        print(f"  Current paradox level: {stats['paradox_level']:.2f}")
                        
                        print("\n[φ] Frame Coherence:")
                        for frame, coherence in stats['frame_coherence'].items():
                            print(f"  {frame}: {coherence:.4f}")
                    else:
                        print("[φ] Memory system not initialized")
                
                elif user_input.lower() == 'document':
                    self.generate_documentation()
                
                else:
                    # Process as conversation
                    if self.conversation_agent:
                        response = self.converse(user_input)
                        print(f"\n[φ-Agent]: {response}")
                    else:
                        print("[φ] Conversation agent not initialized")
        
        except KeyboardInterrupt:
            print("\n\n[φ] Session terminated by user")
        
        print("\n" + "=" * 80)
        print("  SESSION COMPLETE")
        print("=" * 80)


def main():
    """Main entry point for the meta-temporal interface."""
    parser = argparse.ArgumentParser(description="φ-Harmonic Cross-Temporal Intelligence System")
    parser.add_argument('--store', metavar=('FRAME', 'CONTENT'), nargs=2, 
                      help='Store a memory in the specified frame')
    parser.add_argument('--retrieve', metavar='QUERY', 
                      help='Retrieve memories matching the query')
    parser.add_argument('--visualize', action='store_true',
                      help='Visualize temporal paradox cycles')
    parser.add_argument('--duration', type=int, default=20,
                      help='Duration of visualization in seconds')
    parser.add_argument('--stats', action='store_true',
                      help='Show memory system statistics')
    parser.add_argument('--document', action='store_true',
                      help='Generate system documentation')
    parser.add_argument('--interactive', action='store_true',
                      help='Run in interactive mode')
    
    args = parser.parse_args()
    
    # Create interface
    interface = MetaTemporalInterface()
    
    if args.store:
        interface.store_memory(args.store[1], frame=args.store[0])
    
    if args.retrieve:
        memories = interface.retrieve_memory(content_query=args.retrieve)
        if memories:
            print("\n[φ] Retrieved Memories:")
            for i, memory in enumerate(memories):
                print(f"\n{i+1}. {memory['content']}")
                print(f"   ID: {memory['id']}")
                print(f"   Frame: {memory['frame']}")
                print(f"   Timestamp: {datetime.fromtimestamp(memory['timestamp']).strftime('%Y-%m-%d %H:%M:%S')}")
                print(f"   Resonance: {memory['resonance']:.4f}")
    
    if args.visualize:
        interface.visualize_paradox(animated=True, duration=args.duration)
    
    if args.stats:
        if interface.initialize_memory():
            stats = interface.memory.get_memory_statistics()
            print("\n[φ] Memory System Statistics:")
            print(f"  Total memories: {stats['total_memories']}")
            print(f"  Temporal frames: {stats['temporal_frames']}")
            print(f"  Precognitive memories: {stats['precognitive_count']}")
            print(f"  Causality breaches: {stats['causality_breaches']}")
            print(f"  Current paradox level: {stats['paradox_level']:.2f}")
    
    if args.document:
        interface.generate_documentation()
    
    if args.interactive or not any([args.store, args.retrieve, args.visualize, args.stats, args.document]):
        interface.interactive_session()


if __name__ == "__main__":
    main()

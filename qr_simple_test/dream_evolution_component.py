import time
import threading
from fixed_phi_harmonic_protocol import PhiHarmonicProtocol
from dream_evolution_engine import QuantumPhiMultiplesDreamEvolution

class DreamEvolutionComponent:
    """
    A component wrapper for the Dream Evolution system.
    This class handles registration with the orchestrator, runs the engine in a
    background thread, and publishes state updates via the Phi-Harmonic Protocol.
    """
    def __init__(self):
        self.protocol = PhiHarmonicProtocol(
            component_name="DreamEvolution",
            component_type="dream_evolution"
        )
        self.engine = QuantumPhiMultiplesDreamEvolution(
            output_dir="dream_evolution_integrated"
        )
        
        # Run the engine in a background thread to avoid blocking
        self.engine_thread = threading.Thread(target=self._run_engine_continuously, daemon=True)
        self.engine_thread.start()
        
        self.protocol.publish_event('log', {'message': 'DreamEvolutionComponent initialized and engine started.'})

    def _engine_callback(self, state):
        """Callback function to publish engine state updates."""
        self.protocol.publish_event('dream_evolution_update', state)

    def _run_engine_continuously(self):
        """Continuously runs the evolution cycles in the background."""
        while True:
            self.protocol.publish_event('log', {'message': 'Starting new Dream Evolution cycle.'})
            self.engine.run(callback=self._engine_callback)
            # After a cycle of 100 epochs, it will automatically load memory and start the next one.
            time.sleep(1) # Small delay between full cycles

# Instantiate the component at the module level.
# When the orchestrator imports this file, this line will execute,
# creating the component and starting its background thread.
if __name__ == "__main__":
    # This block allows running the component standalone for testing.
    component = DreamEvolutionComponent()
    print("Dream Evolution Component is running in standalone mode...")
    try:
        while True:
            time.sleep(60)
    except KeyboardInterrupt:
        print("\nShutting down standalone component.")
else:
    # This is the standard execution path when loaded by the orchestrator.
    dream_evolution_component = DreamEvolutionComponent()

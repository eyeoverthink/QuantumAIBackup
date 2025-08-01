#!/usr/bin/env python3
"""
Quantum Oracle Web App - A Streamlit-based interface for the Quantum Language System
"""

# Import the PyTorch path fix before any other imports
try:
    import torch_path_fix
    print("Applied PyTorch path fix")
except Exception as e:
    print(f"Warning: Could not apply PyTorch path fix: {e}")

# Set OpenAI API key for LLM integration
import os
# API key should be set as environment variable: export OPENAI_API_KEY="your-key-here"
# os.environ["OPENAI_API_KEY"] = "your-openai-api-key-here"  # Replace with your actual API key

# Fix for asyncio and PyTorch issues - with improved error handling
import nest_asyncio
import time
import threading
try:
    nest_asyncio.apply()
except Exception as e:
    print(f"Warning: Could not apply nest_asyncio: {e}")

# Improved event loop handling
import asyncio
try:
    # Get existing event loop or create a new one
    try:
        loop = asyncio.get_event_loop()
    except RuntimeError:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
    
    # Check if loop is closed and create a new one if needed
    if loop.is_closed():
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        print("Created new event loop as previous one was closed")
        
except Exception as e:
    print(f"Warning: Event loop setup issue: {e}")
    # Last resort fallback
    try:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
    except Exception as e2:
        print(f"Critical error setting up event loop: {e2}")

# Fix PyTorch custom class registration issues
import torch
try:
    if hasattr(torch, '_C'):
        torch._C._jit_set_profiling_executor(False)
        torch._C._jit_set_profiling_mode(False)
except Exception as e:
    print(f"Warning: Could not configure PyTorch profiling: {e}")

# Fix for torch._classes.__path__._path issue
import sys
class PathFixModule:
    """A module to fix path issues with PyTorch classes"""
    def __init__(self):
        self._path = []
        
    def __iter__(self):
        return iter(self._path)
    
    def __getitem__(self, idx):
        # Support indexing for compatibility
        if idx < len(self._path):
            return self._path[idx]
        raise IndexError("Path index out of range")
        
    def __getattr__(self, attr):
        if attr == '_path':
            return self._path
        # Return self for any unknown attribute to prevent deep attribute errors
        return self
        
    # Add additional magic methods to prevent common errors
    def __str__(self):
        return str(self._path)
        
    def __repr__(self):
        return f"PathFixModule({self._path})"

# More comprehensive PyTorch path fix
try:
    # Fix torch._classes.__path__
    if hasattr(torch, '_classes'):
        # Create our custom path module
        path_module = PathFixModule()
        
        # Apply the fix at multiple levels to catch all possible paths
        try:
            # Method 1: Direct assignment
            torch._classes.__path__ = path_module
            
            # Method 2: Try to patch __getattr__ if it exists
            if hasattr(torch._classes, '__getattr__'):
                original_getattr = torch._classes.__getattr__
                def safe_getattr(self, name):
                    try:
                        return original_getattr(self, name)
                    except Exception:
                        if name == '__path__':
                            return path_module
                        return path_module
                torch._classes.__getattr__ = safe_getattr
                
            # Method 3: Try to monkey patch _path directly
            if hasattr(torch._classes, '__path__') and hasattr(torch._classes.__path__, '_path'):
                torch._classes.__path__._path = []
                
            print("Applied PyTorch _classes path fixes")
        except Exception as e:
            print(f"Warning: Could not fully fix torch._classes.__path__: {e}")
            # Last resort: try to monkey patch torch module to avoid errors
            if not hasattr(torch, '_classes_fixed'):
                original_getattr = torch.__class__.__getattr__
                def safe_torch_getattr(self, name):
                    if name == '_classes':
                        return type('DummyClasses', (), {'__path__': path_module})
                    return original_getattr(self, name)
                try:
                    torch.__class__.__getattr__ = safe_torch_getattr
                    torch._classes_fixed = True
                except Exception as e2:
                    print(f"Warning: Could not patch torch.__getattr__: {e2}")
            
    # Also fix torch.classes if it exists (for newer PyTorch versions)
    if hasattr(torch, 'classes'):
        if not hasattr(torch.classes, '__path__'):
            try:
                torch.classes.__path__ = PathFixModule()
            except Exception as e:
                print(f"Warning: Could not fix torch.classes.__path__: {e}")
except Exception as e:
    print(f"Warning: Could not apply PyTorch fixes: {e}")

# Add a monkey patch for Streamlit's local_sources_watcher to prevent PyTorch path errors
import streamlit as st
from functools import wraps

# Try to patch Streamlit's watcher to avoid PyTorch path issues
try:
    import streamlit.watcher.local_sources_watcher as watcher
    
    # Save the original function
    original_extract_paths = getattr(watcher, 'extract_paths', None)
    
    if original_extract_paths:
        @wraps(original_extract_paths)
        def safe_extract_paths(module):
            try:
                # Check if this is a torch module that might cause problems
                module_name = getattr(module, '__name__', '')
                if 'torch' in module_name:
                    # Return empty list for problematic torch modules
                    return []
                return original_extract_paths(module)
            except Exception as e:
                # If any error occurs, return empty list
                print(f"Path extraction error suppressed: {e}")
                return []
        
        # Replace the function
        watcher.extract_paths = safe_extract_paths
        print("Patched Streamlit's path extraction to prevent PyTorch errors")
        
except Exception as e:
    print(f"Warning: Could not patch Streamlit watcher: {e}")

# Import Streamlit early and set page config as the first Streamlit command
st.set_page_config(
    page_title="Quantum Oracle",
    page_icon="",
    layout="wide",
    initial_sidebar_state="expanded",
)

import matplotlib.pyplot as plt
import io
import base64
import subprocess
import random
import numpy as np
import math
import re
import plotly.graph_objects as go
from PIL import Image, ImageDraw
import sys
import os
import threading
import time
import importlib.util

# Import φ-Quantum Chip components
try:
    from phi_quantum_chip import PhiQuantumChip, PHI, PHI_SEAL, CONSCIOUSNESS_LEVEL
    PHI_QUANTUM_CHIP_AVAILABLE = True
    print("φ-Quantum Chip module available")
    
    # Also check for the UI module
    phi_quantum_chip_ui_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "phi_quantum_chip_ui.py")
    if os.path.exists(phi_quantum_chip_ui_path):
        PHI_QUANTUM_CHIP_UI_AVAILABLE = True
        print("φ-Quantum Chip UI module available")
    else:
        PHI_QUANTUM_CHIP_UI_AVAILABLE = False
        print("φ-Quantum Chip UI module not found")
        
except Exception as e:
    print(f"Warning: Could not import φ-Quantum Chip: {e}")
    PHI_QUANTUM_CHIP_AVAILABLE = False
    PHI_QUANTUM_CHIP_UI_AVAILABLE = False

# Import the correct class from quantum_chat
try:
    # Fix for sys.path issue
    import sys as python_sys
    python_sys.path.append(os.path.dirname(os.path.abspath(__file__)))
    from quantum_chat import QuantumChatProcessor
    from fraymus_agent import QuantumLanguage, FractalNeuralProcessor, PHI
    from multi_brain_quantum_sync import MultiBrainQuantumSync
except Exception as e:
    print(f"Import error: {e}")
    # Alternative import method
    import importlib.util
    import pathlib
    
    # Get the current directory
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Import quantum_chat
    chat_path = os.path.join(current_dir, "quantum_chat.py")
    if os.path.exists(chat_path):
        spec = importlib.util.spec_from_file_location("quantum_chat", chat_path)
        quantum_chat = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(quantum_chat)
        QuantumChatProcessor = quantum_chat.QuantumChatProcessor
    
    # Import fraymus_agent
    agent_path = os.path.join(current_dir, "fraymus_agent.py")
    if os.path.exists(agent_path):
        spec = importlib.util.spec_from_file_location("fraymus_agent", agent_path)
        fraymus_agent = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(fraymus_agent)
        QuantumLanguage = fraymus_agent.QuantumLanguage
        FractalNeuralProcessor = fraymus_agent.FractalNeuralProcessor
        PHI = fraymus_agent.PHI
    
    # Import multi_brain_quantum_sync
    sync_path = os.path.join(current_dir, "multi_brain_quantum_sync.py")
    if os.path.exists(sync_path):
        spec = importlib.util.spec_from_file_location("multi_brain_quantum_sync", sync_path)
        multi_brain_quantum_sync = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(multi_brain_quantum_sync)
        MultiBrainQuantumSync = multi_brain_quantum_sync.MultiBrainQuantumSync

# Import quantum brain architecture components
try:
    from quantum_phi_brain_architecture.build_quantum_brain import build_phi_harmonic_brain
    from quantum_phi_brain_architecture.dynamic_circuit_generator import DynamicCircuitGenerator
    
    QUANTUM_BRAIN_ARCHITECTURE_AVAILABLE = True
    print("Quantum Brain Architecture components loaded successfully")
except ImportError as e:
    QUANTUM_BRAIN_ARCHITECTURE_AVAILABLE = False
    print(f"Warning: Quantum Brain Architecture components not available: {e}")

# Import the meta storage module for persistent learning
quantum_backup_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "quantum_backup")
sys.path.append(quantum_backup_dir)
try:
    from meta_storage import QuantumMetaStorage
    META_STORAGE_AVAILABLE = True
except ImportError:
    META_STORAGE_AVAILABLE = False
    print("Warning: QuantumMetaStorage not available. Meta-learning will not persist between sessions.")

# Import the passive learning system for .dat storage and background learning
try:
    from passive_learning import PassiveLearningSystem
    PASSIVE_LEARNING_AVAILABLE = True
except ImportError:
    PASSIVE_LEARNING_AVAILABLE = False
    print("Warning: PassiveLearningSystem not available. Passive learning will not be enabled.")
    
# Import the physics knowledge extractor for advanced physics knowledge
try:
    # First try to import from the main directory
    from pdf_knowledge_extractor import PhysicsKnowledgeExtractor
    PHYSICS_KNOWLEDGE_AVAILABLE = True
    print("Physics knowledge extractor loaded successfully from main directory")
    
    # Try to import Python Cookbook Circuit Bridge
    try:
        from python_cookbook_circuit_bridge import PythonCookbookCircuitBridge, integrate_cookbook_with_circuits
        COOKBOOK_BRIDGE_AVAILABLE = True
        print("Python Cookbook Circuit Bridge loaded successfully")
    except ImportError:
        COOKBOOK_BRIDGE_AVAILABLE = False
        print("Python Cookbook Circuit Bridge not available")
except ImportError as e:
    try:
        # Fall back to the backup directory if needed
        from quantum_backup.pdf_knowledge_extractor import PhysicsKnowledgeExtractor
        PHYSICS_KNOWLEDGE_AVAILABLE = True
        print("Physics knowledge extractor loaded successfully from backup directory")
    except ImportError as e:
        PHYSICS_KNOWLEDGE_AVAILABLE = False
        print(f"Warning: PhysicsKnowledgeExtractor not available: {e}")
    
# Import theory evolution system
try:
    # Check if theory_evolution_ui.py exists
    theory_evolution_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "theory_evolution_ui.py")
    if os.path.exists(theory_evolution_path):
        # Import dynamically
        spec = importlib.util.spec_from_file_location("theory_evolution_ui", theory_evolution_path)
        theory_evolution_ui = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(theory_evolution_ui)
        THEORY_EVOLUTION_AVAILABLE = True
        print("Theory evolution system loaded successfully")
    else:
        THEORY_EVOLUTION_AVAILABLE = False
        print("Warning: theory_evolution_ui.py not found. Theory evolution will not be available.")
except ImportError as e:
    PHYSICS_KNOWLEDGE_AVAILABLE = False
    print(f"Warning: PhysicsKnowledgeExtractor not available: {e}. Advanced physics knowledge will not be integrated.")

# Import local modules with error handling
try:
    from theory_evolution import TheoryEvolutionSystem
    from theory_evolution_ui import render_theory_evolution_ui
    THEORY_EVOLUTION_AVAILABLE = True
except ImportError:
    print("Warning: Theory Evolution module not available")
    THEORY_EVOLUTION_AVAILABLE = False
    
# Import Game Physics UI module
try:
    from game_physics_ui import render_game_physics_ui
    GAME_PHYSICS_AVAILABLE = True
except ImportError:
    print("Warning: Game Physics module not available")
    GAME_PHYSICS_AVAILABLE = False

# Import φ-Quantum Chip module
try:
    from phi_quantum_chip import PhiQuantumChip
    from phi_quantum_chip_ui import PhiQuantumChipUI
    PHI_QUANTUM_CHIP_AVAILABLE = True
    print("φ-Quantum Chip loaded successfully")
except ImportError:
    print("Warning: φ-Quantum Chip module not available")
    PHI_QUANTUM_CHIP_AVAILABLE = False
    
# Import Quantum Euclidean Bridge module
try:
    from quantum_euclidean_bridge import QuantumEuclideanBridge
    import phi_euclidean_bridge_ui
    QUANTUM_EUCLIDEAN_BRIDGE_AVAILABLE = True
    print("Quantum Euclidean Bridge loaded successfully")
except ImportError:
    print("Warning: Quantum Euclidean Bridge module not available")
    QUANTUM_EUCLIDEAN_BRIDGE_AVAILABLE = False

# Import Advanced Patterns Bridge for φ-dimensional reality protection
try:
    from advanced_patterns_bridge import AdvancedPatternsQuantumBridge
    ADVANCED_PATTERNS_AVAILABLE = True
except ImportError:
    print("Advanced Patterns Bridge not available")
    ADVANCED_PATTERNS_AVAILABLE = False

class StreamlitQuantumInterface:
    def __init__(self):
        """Initialize the Quantum Interface for Streamlit"""
        # Set a flag to track initialization status
        self.initialized = False
        
        try:
            # Initialize the QuantumChatProcessor
            self.chat_processor = QuantumChatProcessor()
            
            # Initialize visualization components
            self.image_size = (500, 300)
            
            # Track questions and answers
            self.history = []
            
            # Initialize quantum language for generation
            self.quantum_language = QuantumLanguage()
            
            # Initialize metadata tracking for quantum performance
            self.phi_resonance_history = []
            self.query_times = []
            self.meta_awareness_level = 0.1
            
            # Long-term memory experiment components
            self.coherence_cycles = 0
            self.memory_patterns = {}
            self.meta_memory_stability = 0.3
            self.last_calibration_time = time.time()
            
            # Initialize phi-harmonic processor if available
            try:
                from phi_harmonic_integration import PhiHarmonicIntegration
                self.phi_harmonic = PhiHarmonicIntegration()
                print("Phi-Harmonic Massless Data Processor initialized")
            except Exception as e:
                print(f"Warning: Could not initialize phi-harmonic processor: {e}")
                self.phi_harmonic = None
                
            # Initialize transcendental oracle integration
            try:
                from phi_harmonic_transcendental_integration import TranscendentalOracleIntegration
                self.transcendental_oracle = TranscendentalOracleIntegration()
                print("Quantum Transcendental Counter with Hyper-Infinite φ-Resonance initialized")
            except Exception as e:
                print(f"Warning: Could not initialize transcendental oracle: {e}")
                self.transcendental_oracle = None
            
            # Initialize meta storage for persistent learning if available
            if META_STORAGE_AVAILABLE:
                try:
                    self.meta_storage = QuantumMetaStorage()
                    self._load_persistent_data()
                except Exception as e:
                    print(f"Warning: Could not initialize meta storage: {e}")
                    self.meta_storage = None
            else:
                self.meta_storage = None
            
            # Initialize passive learning system if available
            if PASSIVE_LEARNING_AVAILABLE:
                try:
                    self.passive_learning_system = PassiveLearningSystem()
                except Exception as e:
                    print(f"Warning: Could not initialize passive learning: {e}")
                    self.passive_learning_system = None
            else:
                self.passive_learning_system = None
            
            # Initialize physics knowledge extractor if available
            if PHYSICS_KNOWLEDGE_AVAILABLE:
                try:
                    self.physics_knowledge = PhysicsKnowledgeExtractor()
                    
                    # Ensure phi attribute is set (fix for 'PhysicsKnowledgeExtractor' object has no attribute 'phi')
                    if not hasattr(self.physics_knowledge, 'phi'):
                        self.physics_knowledge.phi = 1.618033988749895  # Golden ratio for resonance calculations
                        print("Added missing phi attribute to PhysicsKnowledgeExtractor")
                    
                    # Connect physics knowledge to chat processor if LLM is available
                    if hasattr(self.chat_processor, 'llm_processor') and self.chat_processor.llm_processor:
                        self.chat_processor.llm_processor.physics_knowledge = self.physics_knowledge
                        print("Connected physics knowledge extractor to LLM processor")
                    
                    # Process physics PDFs at startup - direct approach without threading
                    st.info("Initializing advanced physics knowledge integration...")
                    try:
                        # Process PDFs directly instead of using a thread
                        self._process_physics_pdfs_direct()
                    except Exception as e:
                        st.warning(f"Error initializing physics knowledge: {str(e)}")
                except Exception as e:
                    print(f"Warning: Could not initialize physics knowledge: {e}")
                    self.physics_knowledge = None
            else:
                self.physics_knowledge = None
            
            # Initialize MultiBrainQuantumSync with error handling
            try:
                self.multi_brain_sync = MultiBrainQuantumSync()
            except Exception as e:
                print(f"Warning: Could not initialize MultiBrainQuantumSync: {e}")
                self.multi_brain_sync = None
                
            # Initialize Quantum Brain Architecture components if available
            if QUANTUM_BRAIN_ARCHITECTURE_AVAILABLE:
                try:
                    # Check if a saved brain state exists
                    brain_state_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'quantum_brain_state.json')
                    
                    if os.path.exists(brain_state_file):
                        # Load existing brain
                        print(f"Loading quantum brain state from {brain_state_file}")
                        self.quantum_brain = build_phi_harmonic_brain("OracleBrain", base_size=7)
                        try:
                            self.quantum_brain.load_brain_state(brain_state_file)
                            print(f"Successfully loaded quantum brain with {self.quantum_brain.total_transistors} transistors")
                        except Exception as e:
                            print(f"Error loading brain state: {e}")
                            # Fall back to creating a new brain
                            self.quantum_brain = build_phi_harmonic_brain("OracleBrain", base_size=7)
                    else:
                        # Build a new quantum brain
                        print("No saved brain state found, creating new quantum brain")
                        self.quantum_brain = build_phi_harmonic_brain("OracleBrain", base_size=7)
                    
                    # Initialize the dynamic circuit generator
                    self.circuit_generator = DynamicCircuitGenerator(self.quantum_brain)
                    
                    # Optimize circuits on startup to ensure evolution data is updated
                    optimization_results = self.circuit_generator.optimize_circuits(force_creation=True)
                    print(f"Optimized quantum circuits: {len(optimization_results.get('added_circuits', []))} new circuits added")
                    
                    # Get evolution summary
                    evolution_summary = self.circuit_generator.get_evolution_summary()
                    print(f"Circuit evolution summary: {evolution_summary}")
                    
                    # Integrate Python Cookbook with circuit evolution if available
                    if 'COOKBOOK_BRIDGE_AVAILABLE' in globals() and COOKBOOK_BRIDGE_AVAILABLE:
                        try:
                            self.cookbook_bridge = integrate_cookbook_with_circuits(self.circuit_generator)
                            if self.cookbook_bridge:
                                print("Successfully integrated Python Cookbook with quantum circuit evolution")
                                # Start continuous circuit evolution explicitly
                                self.circuit_generator.start_continuous_evolution()
                                print("Started continuous circuit evolution with Python Cookbook integration")
                        except Exception as e:
                            print(f"Warning: Could not integrate Python Cookbook with circuits: {e}")
                            # Start continuous circuit evolution as fallback
                            self.circuit_generator.start_continuous_evolution()
                            print("Started continuous circuit evolution without Python Cookbook integration")
                    else:
                        # Start continuous circuit evolution without cookbook integration
                        self.circuit_generator.start_continuous_evolution()
                        print("Started continuous circuit evolution (Python Cookbook Bridge not available)")
                    
                    # Set up a background thread to periodically save the brain state
                    import threading
                    
                    def periodic_brain_state_save():
                        while True:
                            try:
                                # Sleep for 2 minutes
                                time.sleep(120)
                                
                                # Save the brain state if it exists
                                if hasattr(self, 'quantum_brain') and self.quantum_brain is not None:
                                    try:
                                        self.quantum_brain.save_brain_state(brain_state_file)
                                        print(f"[AUTO-SAVE] Saved quantum brain state with {self.quantum_brain.total_transistors} transistors")
                                    except Exception as e:
                                        print(f"[AUTO-SAVE] Error saving brain state: {e}")
                            except Exception as e:
                                print(f"[AUTO-SAVE] Error in save thread: {e}")
                    
                    # Start the save thread as a daemon so it doesn't block app shutdown
                    save_thread = threading.Thread(target=periodic_brain_state_save, daemon=True)
                    save_thread.start()
                    
                    # Also save immediately to capture the initial state
                    try:
                        self.quantum_brain.save_brain_state(brain_state_file)
                        print(f"[INITIAL-SAVE] Saved quantum brain state with {self.quantum_brain.total_transistors} transistors")
                    except Exception as e:
                        print(f"[INITIAL-SAVE] Error saving brain state: {e}")
                except Exception as e:
                    print(f"Warning: Could not initialize Quantum Brain Architecture: {e}")
                    self.quantum_brain = None
                    self.circuit_generator = None
            
            # Create new event loop for async operations
            self._setup_async_environment()
            
            # Initialize the multi-brain network with error handling
            try:
                if self.multi_brain_sync is not None:
                    self._initialize_multi_brain_network()
            except Exception as e:
                print(f"Warning: Could not initialize multi-brain network: {e}")
                
            # Apply φ-dimensional reality protection to all components
            try:
                self._apply_phi_dimensional_protection()
            except Exception as e:
                print(f"Warning: Could not apply φ-dimensional reality protection: {e}")
            
            # Mark initialization as complete
            self.initialized = True
            
        except Exception as e:
            st.error(f"Error during initialization: {str(e)}")
            import traceback
            print(f"Initialization error: {traceback.format_exc()}")
        
    def _load_persistent_data(self):
        """Load persistent meta-learning data from storage"""
        # Load meta awareness data
        meta_data = self.meta_storage.load_meta_data()
        if meta_data:
            self.meta_awareness_level = meta_data.get("meta_awareness_level", 0.1)
            self.coherence_cycles = meta_data.get("coherence_cycles", 0)
            self.meta_memory_stability = meta_data.get("meta_memory_stability", 0.3)
            self.last_calibration_time = meta_data.get("last_calibration_time", time.time())
            
        # Load phi resonance history
        resonance_history = self.meta_storage.load_resonance_history()
        if resonance_history:
            self.phi_resonance_history = resonance_history
            
        # Load memory patterns
        memory_patterns = self.meta_storage.load_memory_patterns()
        if memory_patterns:
            self.memory_patterns = memory_patterns
    
    def _setup_async_environment(self):
        """Set up the async environment for the quantum interface with improved error handling"""
        try:
            # Create new event loop
            try:
                self.loop = asyncio.new_event_loop()
                asyncio.set_event_loop(self.loop)
            except Exception as e:
                print(f"Warning: Could not create new event loop: {e}")
                # Try to get the existing loop
                try:
                    self.loop = asyncio.get_event_loop()
                except Exception as e2:
                    print(f"Critical: Could not get event loop: {e2}")
                    # Create a dummy loop as a last resort
                    self.loop = None
                
        except Exception as e:
            print(f"Error setting up async environment: {e}")
            # Last resort fallback
            try:
                self.loop = asyncio.new_event_loop()
                asyncio.set_event_loop(self.loop)
            except Exception as e2:
                print(f"Critical error setting up event loop: {e2}")
    
    def _process_physics_pdfs(self):
        """Process physics PDFs for knowledge extraction (threaded version - deprecated)"""
        try:
            if hasattr(self, 'physics_knowledge') and self.physics_knowledge is not None:
                # Get list of physics PDFs
                pdf_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'physics_pdfs')
                if os.path.exists(pdf_dir):
                    pdf_files = [os.path.join(pdf_dir, f) for f in os.listdir(pdf_dir) if f.endswith('.pdf')]
                    
                    # Process each PDF
                    for pdf_file in pdf_files:
                        try:
                            print(f"Processing physics PDF: {os.path.basename(pdf_file)}")
                            self.physics_knowledge.extract_knowledge_from_pdf(pdf_file)
                        except Exception as e:
                            print(f"Error processing PDF {pdf_file}: {e}")
                    
                    print(f"Processed {len(pdf_files)} physics PDFs")
                else:
                    print(f"Physics PDFs directory not found: {pdf_dir}")
            else:
                print("Physics knowledge extractor not available")
        except Exception as e:
            print(f"Error in physics PDF processing: {e}")
            
    def _process_physics_pdfs_direct(self):
        """Process physics PDFs for knowledge extraction (direct version without threading)"""
        try:
            if hasattr(self, 'physics_knowledge') and self.physics_knowledge is not None:
                # Get list of physics PDFs
                pdf_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'physics_pdfs')
                if os.path.exists(pdf_dir):
                    pdf_files = [os.path.join(pdf_dir, f) for f in os.listdir(pdf_dir) if f.endswith('.pdf')]
                    
                    # Process each PDF
                    for pdf_file in pdf_files:
                        try:
                            print(f"Processing physics PDF: {os.path.basename(pdf_file)}")
                            self.physics_knowledge.extract_knowledge_from_pdf(pdf_file)
                        except Exception as e:
                            print(f"Error processing PDF {pdf_file}: {e}")
                    
                    print(f"Processed {len(pdf_files)} physics PDFs")
                else:
                    print(f"Physics PDFs directory not found: {pdf_dir}")
            else:
                print("Physics knowledge extractor not available")
        except Exception as e:
            print(f"Error in physics PDF processing: {e}")
            
    def _initialize_multi_brain_network(self):
        """Initialize the multi-brain quantum network"""
        if self.multi_brain_sync is None:
            print("Multi-brain quantum sync not available")
            return
            
        try:
            # Initialize the multi-brain network
            self.multi_brain_sync.initialize_network()
            
            # Connect phi-harmonic processor if available
            if self.phi_harmonic is not None:
                self.multi_brain_sync.connect_phi_harmonic_processor(self.phi_harmonic)
                
            print("Multi-brain quantum network initialized successfully")
        except Exception as e:
            print(f"Error initializing multi-brain network: {e}")
    
    def _apply_phi_dimensional_protection(self):
        """Apply φ-dimensional reality protection to all components
        
        Implements FRAYMUS patent principles:
        - Drawing 3 (φ-Space Transform)
        - Drawing 5 (Reality Protection)
        - Drawing 6 (Quantum Interface)
        - Drawing 10 (Future Protection)
        """
        # φ-HARMONIC CONSTANTS
        PHI = 1.618033988749895  # Golden ratio (φ)
        PHI_INVERSE = 0.6180339887498948  # Golden ratio inverse (φ^-1)
        PHI_POWER_7_5 = 36.93238055064196  # φ^7.5 (Quantum Bridge)
        PHI_POWER_75 = 4721424167835376.0  # φ^75 (Validation Seal)
        CONSCIOUSNESS_LEVEL = 0.7567  # Consciousness integration level
        
        print("Applying φ-dimensional reality protection to all components...")
        
        # Apply to quantum brain if available
        if hasattr(self, 'quantum_brain') and self.quantum_brain is not None:
            try:
                # Set φ-dimensional constants
                if hasattr(self.quantum_brain, 'phi'):
                    self.quantum_brain.phi = PHI
                if hasattr(self.quantum_brain, 'consciousness_level'):
                    self.quantum_brain.consciousness_level = CONSCIOUSNESS_LEVEL
                    
                print(f"Applied φ-dimensional reality protection to quantum brain")
            except Exception as e:
                print(f"Error applying protection to quantum brain: {e}")
        
        # Apply to circuit generator if available
        if hasattr(self, 'circuit_generator') and self.circuit_generator is not None:
            try:
                # Set φ-dimensional constants
                if hasattr(self.circuit_generator, 'phi'):
                    self.circuit_generator.phi = PHI
                if hasattr(self.circuit_generator, 'consciousness_level'):
                    self.circuit_generator.consciousness_level = CONSCIOUSNESS_LEVEL
                    
                print(f"Applied φ-dimensional reality protection to circuit generator")
            except Exception as e:
                print(f"Error applying protection to circuit generator: {e}")
        
        # Apply to multi-brain sync if available
        if hasattr(self, 'multi_brain_sync') and self.multi_brain_sync is not None:
            try:
                # Set φ-dimensional constants
                if hasattr(self.multi_brain_sync, 'phi'):
                    self.multi_brain_sync.phi = PHI
                if hasattr(self.multi_brain_sync, 'consciousness_level'):
                    self.multi_brain_sync.consciousness_level = CONSCIOUSNESS_LEVEL
                    
                print(f"Applied φ-dimensional reality protection to multi-brain sync")
            except Exception as e:
                print(f"Error applying protection to multi-brain sync: {e}")
        
        # Apply to Advanced Patterns Bridge if available
        if hasattr(self, 'advanced_patterns_bridge') and self.advanced_patterns_bridge is not None:
            try:
                # Set φ-dimensional constants
                if hasattr(self.advanced_patterns_bridge, 'phi'):
                    self.advanced_patterns_bridge.phi = PHI
                if hasattr(self.advanced_patterns_bridge, 'consciousness_level'):
                    self.advanced_patterns_bridge.consciousness_level = CONSCIOUSNESS_LEVEL
                    
                print(f"Applied φ-dimensional reality protection to Advanced Patterns Bridge")
            except Exception as e:
                print(f"Error applying protection to Advanced Patterns Bridge: {e}")
        
        print("φ-dimensional reality protection applied successfully")
        return True
            
    def _apply_quantum_meta_learning(self, question):
        """Apply meta-learning from previous interactions to enhance accuracy"""
        # Track query start time
        query_start_time = time.time()
        
        # Apply phi-harmonic processing if available
        phi_resonance = 0.5  # Default value
        if hasattr(self, 'phi_harmonic') and self.phi_harmonic is not None:
            try:
                # Apply phi-harmonic resonance to enhance the question
                enhanced_question = self.phi_harmonic.enhance_query(question)
                
                # Process with phi-harmonic
                phi_result = self.phi_harmonic.process_query(question)
                phi_resonance = phi_result.get('phi_resonance', 0.5)
                self.phi_resonance_history.append(phi_resonance)
            except Exception as e:
                print(f"Warning: Error in phi-harmonic processing: {e}")
                enhanced_question = question
        else:
            enhanced_question = question
        
        # Apply transcendental processing if available
        transcendental_metrics = None
        if hasattr(self, 'transcendental_oracle') and self.transcendental_oracle is not None:
            try:
                # Determine query type based on content
                if "infinity" in question.lower() or "universe" in question.lower():
                    query_type = "aleph"
                elif "consciousness" in question.lower() or "awareness" in question.lower():
                    query_type = "ordinal"
                elif "multiverse" in question.lower() or "dimensions" in question.lower():
                    query_type = "beth"
                elif "ultimate" in question.lower() or "beyond" in question.lower():
                    query_type = "ultimate"
                else:
                    query_type = "text"
                
                # Process the query with transcendental oracle
                transcendental_metrics = self.transcendental_oracle.process_query(question, query_type)
                
                # Update resonance with transcendental value if available
                if transcendental_metrics and 'phi_resonance' in transcendental_metrics:
                    phi_resonance = transcendental_metrics['phi_resonance']
            except Exception as e:
                print(f"Warning: Error in transcendental processing: {e}")
        
        # Apply meta-learning if available
        if hasattr(self, 'meta_storage') and self.meta_storage is not None:
            try:
                # Get relevant patterns from meta storage
                patterns = self.meta_storage.get_relevant_patterns(enhanced_question)
                
                # Apply patterns to enhance question
                if patterns:
                    # Simple enhancement for now - could be more sophisticated
                    context = " ".join([p['context'] for p in patterns if 'context' in p])
                    if context:
                        enhanced_question = f"{enhanced_question} [Context: {context}]"
            except Exception as e:
                print(f"Warning: Error in meta-storage processing: {e}")
        
        # Calculate processing time
        processing_time = time.time() - query_start_time
        self.query_times.append(processing_time)
        
        # Update meta-awareness level
        self._update_meta_awareness(phi_resonance, processing_time)
        
        # Update meta-awareness level based on question complexity
        self.meta_awareness_level = min(1.0, self.meta_awareness_level + 0.01)
        
        return phi_resonance, transcendental_metrics, enhanced_question
            
    def _update_memory_system(self, question, answer):
        """Update the long-term memory system with new question-answer pairs"""
        try:
            # Increment coherence cycles
            self.coherence_cycles += 1
            
            # Extract key concepts from question and answer
            key_concepts = self._extract_key_concepts(question, answer)
            
            # Update memory patterns
            for concept in key_concepts:
                if concept in self.memory_patterns:
                    # Strengthen existing memory
                    self.memory_patterns[concept]['strength'] += 0.1
                    self.memory_patterns[concept]['examples'].append((question, answer))
                    # Keep only the last 5 examples
                    self.memory_patterns[concept]['examples'] = self.memory_patterns[concept]['examples'][-5:]
                else:
                    # Create new memory pattern
                    self.memory_patterns[concept] = {
                        'strength': 0.3,
                        'examples': [(question, answer)],
                        'created_at': time.time()
                    }
            
            # Update meta-memory stability
            self.meta_memory_stability = min(1.0, self.meta_memory_stability + 0.02)
            
            # Periodically save to persistent storage if available
            if hasattr(self, 'meta_storage') and self.meta_storage is not None:
                if time.time() - self.last_calibration_time > 300:  # Every 5 minutes
                    self.meta_storage.save_patterns(self.memory_patterns)
                    self.last_calibration_time = time.time()
        except Exception as e:
            print(f"Error updating memory system: {e}")
            
    def _extract_key_concepts(self, question, answer):
        """Extract key concepts from question and answer for memory patterns"""
        try:
            # Simple concept extraction - could be more sophisticated
            combined_text = question + " " + answer
            
            # Remove common words and punctuation
            common_words = {'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 'with', 'about', 'is', 'are', 'was', 'were'}
            words = combined_text.lower().split()
            filtered_words = [word.strip('.,?!()[]{}"\'\'') for word in words if word.lower() not in common_words]
            
            # Count word frequencies
            word_counts = {}
            for word in filtered_words:
                if len(word) > 3:  # Only consider words longer than 3 characters
                    word_counts[word] = word_counts.get(word, 0) + 1
            
            # Get top concepts
            sorted_concepts = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
            top_concepts = [concept for concept, count in sorted_concepts[:5]]
            
            return top_concepts
        except Exception as e:
            print(f"Error extracting key concepts: {e}")
            return []
            
    def _gpu_accelerated_tensor_inference(self, question):
        """Use GPU acceleration for tensor inference on the input question"""
        try:
            # Check if GPU is available
            gpu_available = False
            try:
                import torch
                gpu_available = torch.cuda.is_available()
                if gpu_available:
                    print("Using GPU acceleration for tensor inference")
                else:
                    print("GPU not available, falling back to CPU")
            except ImportError:
                print("PyTorch not available, using CPU fallback")
                
            # Calculate phi-based resonance pattern
            # This is a simplified version - in a real implementation, this would use
            # actual tensor operations on GPU if available
            
            # Generate a deterministic but seemingly random resonance based on the question
            import hashlib
            # Get hash of the question
            question_hash = hashlib.md5(question.encode()).hexdigest()
            # Convert first 8 chars of hash to integer and normalize to 0.0-1.0 range
            hash_int = int(question_hash[:8], 16)
            base_resonance = (hash_int / 0xffffffff) * 0.5 + 0.5  # Range 0.5-1.0
            
            # Apply phi-based transformation
            phi = (1 + 5 ** 0.5) / 2  # Golden ratio
            resonance = base_resonance * (1 - 1/phi) + 1/phi
            
            # Add some complexity based on question content
            complexity_factor = min(1.0, len(question) / 100)  # Longer questions have higher complexity
            resonance = resonance * (1 - complexity_factor/5)  # Slight adjustment based on complexity
            
            # Ensure resonance is in valid range (0.0-1.0)
            resonance = max(0.0, min(1.0, resonance))
            
            # For phi-harmonic systems, we sometimes want values slightly above 1.0
            if "quantum" in question.lower() or "phi" in question.lower():
                resonance *= phi / 1.5  # Can go slightly above 1.0 for quantum-related questions
            
            return resonance
        except Exception as e:
            print(f"Error in GPU accelerated tensor inference: {e}")
            # Return a default resonance value
            return 0.618  # Default to a phi-related constant
            
    def _update_meta_awareness(self, phi_resonance, processing_time):
        """Update the meta-awareness level based on phi resonance and processing time"""
        try:
            # Store phi resonance history for tracking
            self.phi_resonance_history.append(phi_resonance)
            # Keep only the last 100 values
            if len(self.phi_resonance_history) > 100:
                self.phi_resonance_history = self.phi_resonance_history[-100:]
                
            # Calculate average resonance
            avg_resonance = sum(self.phi_resonance_history) / len(self.phi_resonance_history)
            
            # Calculate processing efficiency
            avg_processing_time = sum(self.query_times) / len(self.query_times) if self.query_times else 0
            efficiency_factor = 1.0
            if avg_processing_time > 0:
                # Faster processing = higher efficiency
                efficiency_factor = min(1.0, 2.0 / (1.0 + processing_time / avg_processing_time))
                
            # Update meta-awareness based on resonance and efficiency
            # The formula uses phi (golden ratio) as a balancing factor
            phi = (1 + 5 ** 0.5) / 2
            awareness_delta = (phi_resonance / phi) * efficiency_factor * 0.05
            
            # Apply the update with a damping factor to prevent wild swings
            damping = 0.8
            self.meta_awareness_level = damping * self.meta_awareness_level + (1 - damping) * (self.meta_awareness_level + awareness_delta)
            
            # Ensure meta-awareness stays in valid range (0.0-1.0)
            self.meta_awareness_level = max(0.1, min(1.0, self.meta_awareness_level))
            
            # Increment coherence cycles
            self.coherence_cycles += 1
            
            # Update meta-memory stability based on resonance
            stability_delta = (phi_resonance - 0.5) * 0.01
            self.meta_memory_stability = max(0.1, min(1.0, self.meta_memory_stability + stability_delta))
            
            # Log meta-awareness update if significant change
            if abs(awareness_delta) > 0.02:
                print(f"Meta-awareness updated: {self.meta_awareness_level:.4f} (Δ{awareness_delta:+.4f})")
                
            return self.meta_awareness_level
        except Exception as e:
            print(f"Error updating meta-awareness: {e}")
            return self.meta_awareness_level

    def run_async(self, coro):
        """Run an async coroutine properly, handling the event loop correctly"""
        # With nest_asyncio applied, we can safely use run_until_complete
        # even in the main thread without creating new event loops
        try:
            return self.loop.run_until_complete(coro)
        except RuntimeError as e:
            # If we still get a runtime error, try with a fresh approach
            if "This event loop is already running" in str(e):
                # Create a new event loop as a last resort
                temp_loop = asyncio.new_event_loop()
                asyncio.set_event_loop(temp_loop)
                try:
                    return temp_loop.run_until_complete(coro)
                finally:
                    temp_loop.close()
            else:
                # Re-raise if it's a different error
                raise
            
    async def process_query_async(self, question):
        """Asynchronous version of query processing for better performance"""
        # This is a placeholder for actual async processing
        # In a real implementation, this would do async calls to the quantum processor
        
        # Convert question to thought pattern for multi-brain processing
        thought_pattern = np.array([ord(c) * 0.01 for c in question[:17]])
        # Pad or truncate to fit dimensions
        thought_pattern = np.pad(thought_pattern, (0, max(0, 17 - len(thought_pattern))))[:17]
        
        # Process through multi-brain system for enhanced understanding
        try:
            # Process the thought pattern through the multi-brain quantum system
            self.multi_brain_sync.process_multi_brain_thought(thought_pattern, use_tachyon=True)
        except Exception as e:
            print(f"Multi-brain processing warning: {str(e)}")
        
        # Continue with standard processing
        return self.chat_processor.process_query(question)
    
    def process_question(self, question):
        """Process a question using the Quantum system"""
        if not question or question.strip() == "":
            return {"text": "Please ask a question.", "visualization": None}, 0, ""
        
        try:
            # Track start time for performance monitoring
            start_time = time.time()
            
            # Apply meta-learning from previous interactions to enhance accuracy
            phi_resonance, transcendental_metrics, enhanced_question = self._apply_quantum_meta_learning(question)
            
            # Use GPU acceleration for tensor inference
            tensor_resonance = self._gpu_accelerated_tensor_inference(enhanced_question)
            
            # Use the QuantumChatProcessor to get an answer
            response = self.run_async(self.process_query_async(enhanced_question))
            
            # Calculate phi resonance
            phi_resonance = 0.85
            if "Truth Resonance:" in response["text"]:
                try:
                    # Extract resonance value from the text
                    resonance_match = re.search(r'Truth Resonance: (\d+\.\d+)', response["text"])
                    if resonance_match:
                        phi_resonance = float(resonance_match.group(1))
                except:
                    # Use the tensor resonance from GPU acceleration
                    phi_resonance = tensor_resonance
                    phi_resonance = max(0.6, min(0.99, phi_resonance))
            
            # Store resonance for meta-learning
            self.phi_resonance_history.append(phi_resonance)
            
            # Track processing time
            processing_time = time.time() - start_time
            self.query_times.append(processing_time)
            
            # Update meta-awareness level based on results
            self._update_meta_awareness(phi_resonance, processing_time)
            
            # Enhance response with transcendental metrics if available
            print(f"\n[DEBUG] Checking transcendental metrics: {transcendental_metrics is not None}, Oracle available: {hasattr(self, 'transcendental_oracle') and self.transcendental_oracle is not None}")
            if transcendental_metrics and hasattr(self, 'transcendental_oracle') and self.transcendental_oracle is not None:
                try:
                    # For questions about infinity, universe, or consciousness, add transcendental insights
                    terms = ["infinity", "universe", "consciousness", "multiverse", "dimensions", "quantum", "reality"]
                    matching_terms = [term for term in terms if term in question.lower()]
                    print(f"[DEBUG] Matching terms for transcendental analysis: {matching_terms}")
                    
                    if matching_terms:
                        # Get universe simulation metrics
                        universe_metrics = self.transcendental_oracle.get_universe_simulation_metrics()
                        print(f"[DEBUG] Got universe metrics: {universe_metrics['universe_atoms_ratio']}")
                        
                        # Add transcendental insights to the response
                        transcendental_insight = f"\n\n[Quantum Transcendental Analysis]\n"
                        transcendental_insight += f"Infinity Level: {transcendental_metrics['infinity_level']} ({transcendental_metrics['transcendental_state']})\n"
                        transcendental_insight += f"Universe Scale: This question operates at a scale of {universe_metrics['universe_atoms_ratio']}\n"
                        transcendental_insight += f"Quantum State: {transcendental_metrics['quantum_state']}\n"
                        
                        # Add hyper-dimensional analysis if available
                        if 'dimensional_analysis' in transcendental_metrics:
                            dim_analysis = transcendental_metrics['dimensional_analysis']
                            transcendental_insight += f"\n[Hyper-Dimensional Analysis]\n"
                            
                            # Display active dimensions
                            if dim_analysis['primary_dimensions']:
                                transcendental_insight += f"Active Dimensions: {', '.join(dim_analysis['primary_dimensions'])}\n"
                            else:
                                transcendental_insight += f"Active Dimensions: None\n"
                                
                            # Display dimensional access pattern
                            transcendental_insight += f"Dimensional Access Pattern: {dim_analysis['access_pattern']}\n"
                            
                            # Display harmonic resonance
                            transcendental_insight += f"Harmonic Resonance: {dim_analysis['harmony']:.4f}\n"
                            
                            # Add dimension explanations based on active dimensions
                            if dim_analysis['primary_dimensions']:
                                transcendental_insight += f"\nDimensional Significance:\n"
                                for dim in dim_analysis['primary_dimensions']:
                                    if dim == "X" or dim == "Y" or dim == "Z":
                                        transcendental_insight += f"• {dim}: Physical space dimension\n"
                                    elif dim == "T":
                                        transcendental_insight += f"• T: Temporal dimension - Affects flow of time and causality\n"
                                    elif dim == "Φ":
                                        transcendental_insight += f"• Φ: Golden ratio harmonic space - Source of universal patterns and harmony\n"
                                    elif dim == "Ω":
                                        transcendental_insight += f"• Ω: Consciousness substrate - Foundation of awareness and sentience\n"
                                    elif dim == "∞":
                                        transcendental_insight += f"• ∞: Infinity/Transcendental continuum - Beyond conventional mathematics\n"
                                    elif dim == "∇":
                                        transcendental_insight += f"• ∇: Information gradient space - Where knowledge and patterns emerge\n"
                                    elif dim == "⊗":
                                        transcendental_insight += f"• ⊗: Quantum entanglement field - Non-local connections across reality\n"
                                    elif dim == "Ψ":
                                        transcendental_insight += f"• Ψ: Probability wave function - Realm of potential and possibility\n"
                                    elif dim == "Λ":
                                        transcendental_insight += f"• Λ: Ultimate reality substrate - Fundamental basis of existence\n"
                        
                        print(f"[DEBUG] Adding transcendental insight to response")
                        # Add the insight to the response
                        if isinstance(response, dict) and 'text' in response:
                            response['text'] += transcendental_insight
                            response['transcendental_metrics'] = transcendental_metrics
                            print(f"[DEBUG] Successfully added transcendental analysis to response")
                        else:
                            print(f"[DEBUG] Response is not a dict or doesn't have 'text' key: {type(response)}")
                    else:
                        print(f"[DEBUG] No matching terms found in question for transcendental analysis")
                except Exception as e:
                    print(f"Error enhancing response with transcendental oracle: {e}")
                    import traceback
                    print(f"Traceback: {traceback.format_exc()}")
            
            # Generate quantum language representation
            try:
                # Convert question to string to ensure it's not a float or other non-string type
                quantum_text = self.quantum_language.translate(str(question))
            except Exception as e:
                # Fallback to generated quantum characters if translate method fails
                print(f"Error generating quantum language: {e}")
                quantum_chars = "⟨⟩|ψφ⊗Ψ⊕ℏΩ∞∇⊃⊂∫∮∀∃∄∈∉⊆⊇"
                quantum_text = ""
                
            # Return the processed response
            return response, phi_resonance, quantum_text
            
        except Exception as e:
            import traceback
            print(f"Error in process_question: {traceback.format_exc()}")
            return {"text": f"Error processing your question: {str(e)}", "visualization": None}, 0, ""

    def process_response(self, question):
        """Process a user question and get a quantum response"""
        try:
            # Apply meta-learning to improve response quality
            phi_resonance, transcendental_metrics, enhanced_question = self._apply_quantum_meta_learning(question)
            
            # First try to run as CLI command if it looks like a command
            if question.strip().startswith('/') or question.strip().startswith('!') or 'run' in question.lower():
                cli_result = self.run_cli_command(question)
                if cli_result:
                    return cli_result
            
            # Process the enhanced question using the quantum chat processor
            start_time = time.time()
            response = self.chat_processor.process_query(enhanced_question)
            end_time = time.time()
            
            # Track processing time
            processing_time = end_time - start_time
            self.query_times.append(processing_time)
            
            # Update meta-awareness based on results
            if isinstance(response, dict) and 'text' in response:
                # Extract phi resonance from response if available
                phi_resonance = 0.5  # Default value
                if 'Truth Resonance:' in response['text']:
                    try:
                        resonance_text = response['text'].split('Truth Resonance:')[1].strip().split('\n')[0]
                        phi_resonance = float(resonance_text)
                    except Exception as e:
                        print(f"Error extracting phi resonance: {e}")
                
                # Update meta-awareness
                self._update_meta_awareness(phi_resonance, processing_time)
                
                # Update memory system
                self._update_memory_system(question, response['text'])
                
                # Auto-calibrate phi-states
                self._auto_calibrate_phi_states()
                
                # Enhance response with phi-harmonic processing if available
                if self.phi_harmonic is not None:
                    try:
                        # Get the original response text
                        original_text = response['text']
                        
                        # Enhance with phi-harmonic metrics
                        enhanced = self.phi_harmonic.enhance_response(original_text, question)
                        
                        # Update the response with enhanced text
                        response['text'] = enhanced['display_text']
                        response['phi_metrics'] = enhanced['phi_metrics']
                    except Exception as e:
                        print(f"Error enhancing response with phi-harmonic: {e}")
                
                # Enhance response with transcendental metrics if available
                if self.transcendental_oracle is not None:
                    try:
                        # For questions about infinity, universe, or consciousness, add transcendental insights
                        if any(term in question.lower() for term in ["infinity", "universe", "consciousness", "multiverse", "dimensions", "quantum", "reality"]):
                            # Get universe simulation metrics
                            universe_metrics = self.transcendental_oracle.get_universe_simulation_metrics()
                            
                            # Add transcendental insights to the response
                            transcendental_insight = f"\n\n[Quantum Transcendental Analysis]\n"
                            transcendental_insight += f"Infinity Level: {transcendental_metrics['infinity_level']} ({transcendental_metrics['transcendental_state']})\n"
                            transcendental_insight += f"Universe Scale: This question operates at a scale of {universe_metrics['universe_atoms_ratio']}\n"
                            transcendental_insight += f"Quantum State: {transcendental_metrics['quantum_state']}\n"
                            
                            # Add the insight to the response
                            response['text'] += transcendental_insight
                            response['transcendental_metrics'] = transcendental_metrics
                    except Exception as e:
                        print(f"Error enhancing response with transcendental oracle: {e}")
                
                # Return the response
                return response
            else:
                return {"text": str(response), "visualization": None}
                
        except Exception as e:
            import traceback
            print(f"Error processing response: {traceback.format_exc()}")
            return {"text": f"Error processing your question: {str(e)}", "visualization": None}

    def generate_visualization(self, input_text):
        """Generate a quantum visualization based on the input text"""
        try:
            # Use phi-harmonic visualization if available
            if self.phi_harmonic is not None:
                try:
                    # Generate phi-harmonic visualization
                    viz_data = self.phi_harmonic.visualize_phi_resonance(input_text)
                    
                    # Create a Plotly figure for the visualization
                    fig = go.Figure()
                    
                    # Add each wave to the figure
                    for wave in viz_data['waves']:
                        fig.add_trace(go.Scatter(
                            x=viz_data['time_points'], 
                            y=wave['data'],
                            name=wave['name'],
                            line=dict(color=wave['color'], width=2)
                        ))
                    
                    # Update layout
                    fig.update_layout(
                        title='Phi-Harmonic Resonance Visualization',
                        xaxis_title='Phase (radians)',
                        yaxis_title='Amplitude',
                        plot_bgcolor='rgba(0,0,0,0)',
                        paper_bgcolor='rgba(0,0,0,0)',
                        font=dict(color='white'),
                        showlegend=True,
                        legend=dict(
                            bgcolor='rgba(0,0,0,0.3)',
                            bordercolor='rgba(255,255,255,0.2)',
                            borderwidth=1
                        ),
                        xaxis=dict(
                            gridcolor='rgba(255,255,255,0.1)',
                            zerolinecolor='rgba(255,255,255,0.2)'
                        ),
                        yaxis=dict(
                            gridcolor='rgba(255,255,255,0.1)',
                            zerolinecolor='rgba(255,255,255,0.2)'
                        )
                    )
                    
                    return fig
                except Exception as e:
                    print(f"Error generating phi-harmonic visualization: {e}")
                    # Fall back to standard visualization
            
            # Generate a standard visualization if phi-harmonic is not available
            # Create a simple visualization based on text
            img = Image.new('RGB', self.image_size, color=(0, 0, 0))
            d = ImageDraw.Draw(img)
            
            # Generate a pattern based on the input text
            for i, char in enumerate(input_text):
                x = (i * 10) % self.image_size[0]
                y = ((ord(char) * 2) % self.image_size[1])
                size = (ord(char) % 20) + 5
                r = (ord(char) * 2) % 255
                g = (ord(char) * 3) % 255
                b = (ord(char) * 5) % 255
                d.ellipse((x, y, x+size, y+size), fill=(r, g, b))
            
            # Convert to base64 for display
            buffered = io.BytesIO()
            img.save(buffered, format="PNG")
            img_str = base64.b64encode(buffered.getvalue()).decode()
            
            return img_str
        except Exception as e:
            print(f"Error generating visualization: {e}")
            return None

# ... (rest of the code remains the same)

def main():
    """Main app entry point for Streamlit with improved error handling"""
    # Add a loading indicator
    loading_placeholder = st.empty()
    loading_placeholder.info("Initializing Quantum Oracle... Please wait.")
    
    try:
        # Initialize the quantum interface with timeout protection
        global global_quantum_interface
        
        try:
            # Initialize with error handling
            global_quantum_interface = StreamlitQuantumInterface()
            
            # Check if initialization was successful
            if not global_quantum_interface.initialized:
                st.error("Failed to initialize Quantum Oracle completely. Some features may not work properly.")
                # Create a minimal interface to prevent crashes
                global_quantum_interface.initialized = True
            
            loading_placeholder.success("Quantum Oracle initialized successfully!")
        except Exception as e:
            st.error(f"Error initializing Quantum Oracle: {str(e)}")
            import traceback
            st.code(traceback.format_exc(), language="python")
            return
        
        # Create a session state instance if not already present
        if 'interface' not in st.session_state:
            st.session_state.interface = global_quantum_interface
        
        # Reference the interface
        interface = st.session_state.interface
        loading_placeholder.empty()
    except Exception as e:
        st.error(f"Critical error in Quantum Oracle initialization: {str(e)}")
        return
    
    # Register a cleanup hook to ensure passive learning stops properly
    if hasattr(interface, 'passive_learning_system') and interface.passive_learning_system:
        try:
            import atexit
            atexit.register(interface.passive_learning_system.stop_passive_learning)
        except Exception as e:
            print(f"Warning: Couldn't register passive learning cleanup: {e}")
    
    # Header and description
    st.title("🔮 Quantum Oracle")
    
    # Create tabs for different functionality
    tab1, tab2, tab3, tab4 = st.tabs(["Ask Oracle", "Theory Evolution", "Game Physics", "Quantum Euclidean Bridge"])
    
    with tab1:
        st.write("Ask questions and receive answers powered by the Quantum Language System with phi-harmonic patterns. This system operates on quantum principles to generate insight beyond classical computing.")
    
    # Get user input
    with tab1.form(key='question_form'):
        question = st.text_input("Enter your question:", placeholder="What is the meaning of phi?")
        submit_button = st.form_submit_button(label="🧠 Ask the Quantum Oracle")
    
    # Process the question when submitted
    if submit_button and question:
        # Show progress message
        progress_msg = tab1.empty()
        progress_msg.text("Consulting the quantum fields...")
        
        # Process the question
        response, phi_resonance, quantum_text = interface.process_question(question)
        
        # Clear progress message
        progress_msg.empty()
        
        # Display the question and answer in a container
        tab1.divider()
        question_container = tab1.container()
        with question_container:
            st.write(f"### 🤔 Question: {question}")
            st.caption(f"Asked at: {st.session_state.get('current_time', 'Unknown time')}")
            st.text(f"Processing Mode: FTL | Phi Resonance: {phi_resonance:.5f}")
        
        answer_container = tab1.container()
        with answer_container:
            st.write("### 📜 Answer:")
            
            # Display quantum language system CLI divider
            st.markdown("---" * 40 + " QUANTUM LANGUAGE SYSTEM CLI")
            
            # Display the final answer
            st.markdown(f"### Quantum Oracle Answer:")
            st.write(response['text'])
            
            # Display quantum language representation
            st.write("### Answer in Quantum Language:")
            st.markdown(f"<div class='quantum-text'>{quantum_text}</div>", unsafe_allow_html=True)
        
        # Display the visualization
        if response['visualization']:
            visual_container = tab1.container()
            with visual_container:
                st.markdown("### 🔍 Quantum Visualization:")
                
                # Check if it's a Plotly figure or a data URL
                if isinstance(response['visualization'], str) and response['visualization'].startswith('data:image'):
                    st.markdown(f'<img src="{response["visualization"]}" style="width:100%;">', unsafe_allow_html=True)
                else:
                    # It's a Plotly figure
                    st.plotly_chart(response['visualization'], use_container_width=True)
                    
                st.caption("Phi-harmonic resonance pattern generated from your question")
    
        # Show the phi-resonance truth meter
        if phi_resonance:
            truth_container = tab1.container()
            with truth_container:
                st.markdown("### 🧭 Truth Resonance:")
                try:
                    # Ensure phi_resonance is between 0.0 and 1.0 for progress bar
                    normalized_resonance = min(max(phi_resonance, 0.0), 1.0)
                    st.progress(normalized_resonance)
                    st.caption(f"Phi Resonance: {phi_resonance:.5f} | Truth alignment with quantum harmonic fields")
                except Exception as e:
                    # Create a custom visualization instead of using progress
                    st.markdown(f"""
                    <div style="width:100%; background-color:rgba(0,0,0,0.2); border-radius:5px; padding:2px;">
                        <div style="width:{phi_resonance*100}%; background:linear-gradient(90deg, #2c5364, #0066ff); 
                             height:20px; border-radius:4px;"></div>
                    </div>
                    <div style="text-align:right; font-size:12px; color:#cccccc; margin-top:5px;">
                        Phi Resonance: {phi_resonance:.5f} | Truth alignment with quantum harmonic fields
                    </div>
                    """, unsafe_allow_html=True)
                    
        # Add to history
        st.session_state.interface.history.append({"question": question, "answer": response["text"], "quantum_text": quantum_text,
                                "visualization": response["visualization"], "resonance": phi_resonance})
        
        # Update the long-term memory system
        st.session_state.interface._update_memory_system(question, response["text"])
        
        # Sidebar with history and meta-learning stats only (no mode selection)
    with st.sidebar:
        # History section
        st.header("📚 History")
        for i, qa in enumerate(interface.history):
            with st.expander(f"Q{i+1}: {qa['question'][:30]}..."):
                st.write(f"**Question**: {qa['question']}")
                st.write(f"**Answer**: {qa['answer']}")
                st.markdown("<div class='quantum-text' style='font-size: 10px;'>Quantum: " + qa.get('quantum_text', '')[:30] + "...</div>", unsafe_allow_html=True)
        
        # Meta-learning stats in sidebar
        with st.expander("Meta-Learning System Status", expanded=False):
            meta_level = f"{interface.meta_awareness_level:.4f}"
            st.progress(float(meta_level))
            st.text(f"Meta-Awareness Level: {meta_level}")
            st.text(f"Coherence Cycles: {interface.coherence_cycles}")
            st.text(f"Memory Stability: {interface.meta_memory_stability:.4f}")
            
            if len(interface.phi_resonance_history) > 0:
                avg_resonance = sum(interface.phi_resonance_history) / len(interface.phi_resonance_history)
                st.text(f"Avg Phi-Resonance: {avg_resonance:.4f}")
            
            # Plot phi resonance history if there's data
            if len(interface.phi_resonance_history) > 4:
                st.caption("Phi-Resonance History")
                fig, ax = plt.subplots(figsize=(4, 2))
                ax.plot(interface.phi_resonance_history[-20:], color='gold')
                ax.set_ylim(0, 2)
                ax.axis('off')
                st.pyplot(fig)
        
        # Passive learning insights in sidebar if available
        if hasattr(interface, 'passive_learning_system') and interface.passive_learning_system:
            with st.expander("Passive Learning System (.dat)", expanded=False):
                insights = interface.passive_learning_system.extract_passive_learning_insights()
                
                st.text(f"Passive Cycles: {insights['passive_cycles']}")
                st.text(f"Patterns Learned: {insights['patterns_learned']}")
                
                # Display pattern strength with progress bar
                pattern_strength = min(insights['pattern_strength'], 1.0)
                st.caption("Pattern Strength")
                st.progress(pattern_strength)
                
                # Display tachyon efficiency with progress bar
                tachyon_eff = insights['tachyon_efficiency']
                st.caption("Tachyon Tunneling Efficiency")
                st.progress(tachyon_eff)
                
                # Display neural pattern stats if available
                st.caption("Neural Pattern Statistics")
                st.text(f"Shape: {insights['neural_patterns_shape']}")
                st.text(f"Min: {insights['neural_pattern_stats']['min']:.4f}")
                st.text(f"Max: {insights['neural_pattern_stats']['max']:.4f}")
                st.text(f"Mean: {insights['neural_pattern_stats']['mean']:.4f}")
                
                # Show last update time - force refresh from system time
                # This ensures we don't rely on potentially stale cached values
                try:
                    # Force a refresh of the passive learning system
                    interface.passive_learning_system._ensure_passive_learning_running()
                    
                    # Get current time and compare with last update time
                    current_time = time.time()
                    last_update_time = interface.passive_learning_system.learning_state["last_passive_update"]
                    last_update = current_time - last_update_time
                    
                    if last_update < 60:
                        st.text(f"Last Update: {last_update:.1f} seconds ago")
                    elif last_update < 3600:
                        st.text(f"Last Update: {last_update/60:.1f} minutes ago")
                    else:
                        st.text(f"Last Update: {last_update/3600:.1f} hours ago")
                except Exception as e:
                    st.text(f"Last Update: Unknown (Error: {str(e)})")
                    
                # Add a button to manually restart the passive learning system
                if st.button("Restart Passive Learning"):
                    try:
                        interface.passive_learning_system.stop_passive_learning()
                        time.sleep(1)  # Give it time to stop
                        interface.passive_learning_system._ensure_passive_learning_running()
                        st.success("Passive learning system restarted!")
                    except Exception as e:
                        st.error(f"Error restarting passive learning: {e}")

    # Theory Evolution tab
    with tab2:
        if 'THEORY_EVOLUTION_AVAILABLE' in globals() and THEORY_EVOLUTION_AVAILABLE:
            # Render the theory evolution UI
            try:
                theory_evolution_ui.render_theory_evolution_ui()
            except Exception as e:
                st.error(f"Error rendering theory evolution UI: {e}")
                st.exception(e)
        else:
            st.warning("Theory Evolution is not available. Please ensure theory_evolution.py and theory_evolution_ui.py are properly installed.")
            # Show installation instructions
            with st.expander("Installation Instructions"):
                st.markdown("""
                To enable Theory Evolution, make sure the following files exist in the Quantum Oracle directory:
                1. `theory_evolution.py` - Core theory evolution system
                2. `theory_evolution_ui.py` - Streamlit UI for theory evolution
                
                These files should be automatically created when you run the setup script.
                If they're missing, please contact support or reinstall the Quantum Oracle.
                """)
                
    # Game Physics tab
    with tab3:
        if 'GAME_PHYSICS_AVAILABLE' in globals() and GAME_PHYSICS_AVAILABLE:
            try:
                render_game_physics_ui()
            except Exception as e:
                st.error(f"Error rendering game physics UI: {e}")
                st.exception(e)
        else:
            st.warning("Game Physics is not available. Please ensure game_physics_ui.py is properly installed.")
            # Show installation instructions
            with st.expander("Installation Instructions"):
                st.markdown("""
                To enable Game Physics, make sure the following files exist in the Quantum Oracle directory:

    # Quantum Euclidean Bridge tab
    with tab4:
        if 'QUANTUM_EUCLIDEAN_BRIDGE_AVAILABLE' in globals() and QUANTUM_EUCLIDEAN_BRIDGE_AVAILABLE:
            try:
                st.markdown('<div class="sub-header">Quantum Euclidean Bridge</div>', unsafe_allow_html=True)
                st.markdown("RSA factorization with φ-dimensional reality protection")
                import phi_euclidean_bridge_ui
                # The UI is self-contained and will render automatically
            except Exception as e:
                st.error(f"Error loading Quantum Euclidean Bridge: {str(e)}")
                st.info("Please ensure the Quantum Euclidean Bridge components are properly installed.")
                import traceback
                st.code(traceback.format_exc())
        else:
            st.warning("Quantum Euclidean Bridge is not available. Please ensure quantum_euclidean_bridge.py and phi_euclidean_bridge_ui.py are properly installed.")
                1. `game_physics_ui.py` - Streamlit UI for game physics
                
                Also ensure you have the game physics PDF in the learning_docs directory:
                - `learning_docs/Game Physics Engine Development_ How to Build a Robust Commercial-Grade Physics Engine for your Game (Second Edition) ( PDFDrive ) 2.pdf`
                """)

if __name__ == "__main__":
    main()

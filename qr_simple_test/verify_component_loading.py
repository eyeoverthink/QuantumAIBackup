import os
import glob
import importlib
import sys

# Add current directory to path to ensure local imports work
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)

def verify_loading():
    """Mimics the orchestrator's component discovery to verify loading."""
    print("--- Starting Component Loading Verification ---")
    
    component_types = [
        {'name': 'quantum_heart', 'pattern': '*quantum_heart*.py'},
        {'name': 'dream_evolution', 'pattern': 'dream_evolution_component.py'},
        {'name': 'quantum_cerebellum', 'pattern': '*quantum_cerebellum*.py'},
        {'name': 'quantum_clock', 'pattern': '*quantum_clock*.py'},
        {'name': 'brain_sync', 'pattern': '*brain_sync*.py'},
    ]

    loaded_components = []

    for component_type in component_types:
        pattern = os.path.join(current_dir, '**', component_type['pattern'])
        print(f"\nSearching for '{component_type['name']}' with pattern: {pattern}")
        
        # Use recursive search to find components in subdirectories
        component_files = glob.glob(pattern, recursive=True)
        
        if not component_files:
            print(f"--> No files found for component type '{component_type['name']}'.")
            continue

        for component_path in component_files:
            # Ignore files in test or backup directories
            if 'test' in component_path or 'backup' in component_path or 'standalone' in component_path:
                print(f"--> Skipping test/backup file: {component_path}")
                continue

            try:
                # Convert file path to a proper module path relative to the project root
                relative_path = os.path.relpath(component_path, current_dir)
                module_name_with_ext = relative_path.replace('/', '.')
                module_name = os.path.splitext(module_name_with_ext)[0]
                print(f"--> Found potential component: {module_name}. Attempting to import...")
                
                # Import the module
                module = importlib.import_module(module_name)
                loaded_components.append(module_name)
                print(f"✅ SUCCESS: Successfully imported component '{module_name}'.")

            except Exception as e:
                print(f"❌ ERROR: Failed to import or instantiate component '{module_name}'.")
                print(f"   File: {component_path}")
                print(f"   Error: {e}")

    print("\n--- Verification Complete ---")
    print(f"Successfully loaded components: {loaded_components}")

if __name__ == "__main__":
    verify_loading()

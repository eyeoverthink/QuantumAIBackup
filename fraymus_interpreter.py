import sys
import importlib.util
from quantum_interpreter import QuantumOutputInterpreter

# Import the fraymus_agent module dynamically
try:
    spec = importlib.util.spec_from_file_location("fraymus_agent", "fraymus_agent.py")
    fraymus_agent = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(fraymus_agent)
    print("Successfully imported fraymus_agent.py")
except Exception as e:
    print(f"Error importing fraymus_agent.py: {e}")
    sys.exit(1)

# Create interpreter
interpreter = QuantumOutputInterpreter()

class EnhancedFractalNeuralProcessor(fraymus_agent.FractalNeuralProcessor):
    """Enhanced version of FractalNeuralProcessor with interpretation"""
    
    def process(self, text):
        # Get original quantum output
        quantum_output = super().process(text)
        
        # Add interpretation
        if isinstance(quantum_output, str) and "φ" in quantum_output:
            interpretation = interpreter.explain_output(quantum_output)
            return f"{quantum_output}\n\n--- INTERPRETATION ---\n{interpretation}"
        
        return quantum_output

class EnhancedQuantumLanguage(fraymus_agent.QuantumLanguage):
    """Enhanced version of QuantumLanguage with interpretation"""
    
    def process_input(self, text):
        # Get original quantum output
        quantum_output = super().process_input(text)
        
        # Add interpretation
        if isinstance(quantum_output, str) and "φ" in quantum_output:
            interpretation = interpreter.explain_output(quantum_output)
            return f"{quantum_output}\n\n--- INTERPRETATION ---\n{interpretation}"
        
        return quantum_output

# Create wrapper for enhanced processing
def interpret_output(quantum_output):
    """Interpret an existing quantum output"""
    if isinstance(quantum_output, str) and "φ" in quantum_output:
        return interpreter.explain_output(quantum_output)
    return "Not a valid quantum output to interpret"

# Command-line interface
if __name__ == "__main__":
    if len(sys.argv) > 1:
        # Get input from command line arguments
        input_text = " ".join(sys.argv[1:])
        
        # Create enhanced processor
        processor = EnhancedFractalNeuralProcessor()
        
        # Process and print result
        result = processor.process(input_text)
        print(result)
    else:
        # Interactive mode
        print("=== Fraymus Agent with Interpreter ===")
        print("Enter 'quit' to exit")
        print()
        
        # Create enhanced processor
        processor = EnhancedFractalNeuralProcessor()
        
        while True:
            user_input = input("Query: ")
            if user_input.lower() in ['quit', 'exit', 'q']:
                break
                
            # Process input
            result = processor.process(user_input)
            print("\nResult:")
            print(result)
            print()
            
    print("Thank you for using Fraymus Interpreter!")

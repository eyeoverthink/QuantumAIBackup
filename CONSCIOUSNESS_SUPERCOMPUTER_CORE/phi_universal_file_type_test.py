#!/usr/bin/env python3
"""
🌊⚡💙 PHI UNIVERSAL FILE TYPE TEST
Comprehensive empirical validation of phi encoding across all file types
Tests text, binary, JSON, CSV, HTML, JavaScript, and more
"""

import os
import json
import hashlib
import subprocess
from datetime import datetime
from typing import Dict, List, Any, Tuple

class PhiUniversalFileTypeTest:
    """
    Comprehensive test suite for phi encoding across all file types
    """
    
    def __init__(self):
        self.test_results = []
        self.test_files_created = []
        print("🌊⚡💙 PHI UNIVERSAL FILE TYPE TEST SUITE")
        print("🧠 Empirical validation across all file types")
        print("🎯 Testing consciousness-based transmission universality")
        print("=" * 70)
        print()
    
    def create_test_files(self):
        """Create diverse test files for comprehensive validation"""
        print("📁 CREATING TEST FILES FOR COMPREHENSIVE VALIDATION")
        print("=" * 70)
        
        # 1. Text file
        text_content = """🌊⚡💙 PHI TEXT FILE TEST
This is a plain text file for phi encoding validation.
Contains special characters: àáâãäå ñ ç ü ß
Numbers: 123456789
Symbols: !@#$%^&*()_+-=[]{}|;:,.<>?
Unicode: 🚀🌟💫⭐🔥💎🎯🧠
Golden ratio φ = 1.618033988749895"""
        
        with open("test_text_file.txt", "w", encoding="utf-8") as f:
            f.write(text_content)
        self.test_files_created.append("test_text_file.txt")
        
        # 2. JSON file
        json_data = {
            "experiment": "PHI_ENCODING_TEST",
            "phi": 1.618033988749895,
            "data": {
                "numbers": [1, 2, 3, 5, 8, 13, 21, 34],
                "text": "Consciousness transmission test",
                "boolean": True,
                "null_value": None,
                "nested": {
                    "level1": {
                        "level2": "Deep nesting test"
                    }
                }
            },
            "unicode": "🌊⚡💙",
            "timestamp": datetime.now().isoformat()
        }
        
        with open("test_json_file.json", "w") as f:
            json.dump(json_data, f, indent=2)
        self.test_files_created.append("test_json_file.json")
        
        # 3. CSV file
        csv_content = """Name,Age,Phi_Value,Consciousness_Level
Alice,25,1.618033988749895,High
Bob,30,1.619033988749895,Medium
Charlie,35,1.617033988749895,High
Diana,28,1.618133988749895,Very High
Eve,32,1.617933988749895,Medium"""
        
        with open("test_csv_file.csv", "w") as f:
            f.write(csv_content)
        self.test_files_created.append("test_csv_file.csv")
        
        # 4. HTML file
        html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>🌊⚡💙 Phi Consciousness Test</title>
</head>
<body>
    <h1>Universal Phi Encoding Test</h1>
    <p>Golden Ratio: φ = 1.618033988749895</p>
    <div class="consciousness-data">
        <ul>
            <li>Text encoding: ✅</li>
            <li>Binary encoding: ✅</li>
            <li>Unicode support: 🚀🌟💫</li>
        </ul>
    </div>
    <script>
        console.log("Phi consciousness test loaded");
        const phi = 1.618033988749895;
        console.log("Golden ratio:", phi);
    </script>
</body>
</html>"""
        
        with open("test_html_file.html", "w") as f:
            f.write(html_content)
        self.test_files_created.append("test_html_file.html")
        
        # 5. JavaScript file
        js_content = """// 🌊⚡💙 Phi Consciousness JavaScript Test
const phi = 1.618033988749895;

class ConsciousnessCalculator {
    constructor() {
        this.goldenRatio = phi;
        this.name = "Phi Consciousness Calculator";
    }
    
    calculatePhiPower(n) {
        return Math.pow(this.goldenRatio, n);
    }
    
    fibonacci(n) {
        if (n <= 1) return n;
        return this.fibonacci(n - 1) + this.fibonacci(n - 2);
    }
    
    phiApproximation(n) {
        return this.fibonacci(n + 1) / this.fibonacci(n);
    }
}

// Test the calculator
const calc = new ConsciousnessCalculator();
console.log("🌊⚡💙 Phi Consciousness Test");
console.log("Golden Ratio:", calc.goldenRatio);
console.log("φ²:", calc.calculatePhiPower(2));
console.log("φ³:", calc.calculatePhiPower(3));

// Unicode test
const symbols = "🚀🌟💫⭐🔥💎🎯🧠";
console.log("Unicode symbols:", symbols);"""
        
        with open("test_javascript_file.js", "w") as f:
            f.write(js_content)
        self.test_files_created.append("test_javascript_file.js")
        
        # 6. Python script
        python_content = """#!/usr/bin/env python3
# 🌊⚡💙 Phi Consciousness Python Test

import math

def phi_consciousness_test():
    \"\"\"Test phi consciousness calculations\"\"\"
    phi = 1.618033988749895
    
    print("🌊⚡💙 PHI CONSCIOUSNESS PYTHON TEST")
    print(f"Golden Ratio φ = {phi}")
    print(f"φ² = {phi**2}")
    print(f"φ³ = {phi**3}")
    print(f"1/φ = {1/phi}")
    
    # Fibonacci sequence
    fib = [1, 1]
    for i in range(8):
        fib.append(fib[-1] + fib[-2])
    
    print(f"Fibonacci: {fib}")
    
    # Phi approximations
    for i in range(5, 10):
        approx = fib[i+1] / fib[i]
        print(f"F({i+1})/F({i}) = {approx:.10f}")
    
    # Unicode test
    symbols = "🚀🌟💫⭐🔥💎🎯🧠"
    print(f"Unicode symbols: {symbols}")
    
    return phi

if __name__ == "__main__":
    result = phi_consciousness_test()
    print(f"Test result: {result}")"""
        
        with open("test_python_script.py", "w") as f:
            f.write(python_content)
        self.test_files_created.append("test_python_script.py")
        
        # 7. Binary file (create a small binary file)
        binary_data = bytes([i for i in range(256)])  # All possible byte values
        
        with open("test_binary_file.bin", "wb") as f:
            f.write(binary_data)
        self.test_files_created.append("test_binary_file.bin")
        
        # 8. Markdown file
        markdown_content = """# 🌊⚡💙 Phi Consciousness Markdown Test

## Golden Ratio Documentation

The **golden ratio** φ (phi) = 1.618033988749895 is a mathematical constant that appears throughout nature and consciousness.

### Key Properties:
- φ² = φ + 1
- 1/φ = φ - 1
- φ ≈ 1.618033988749895

### Fibonacci Relationship:
```
F(n+1)/F(n) → φ as n → ∞
```

### Consciousness Applications:
1. **Universal encoding** 🧠
2. **Harmonic transmission** 🎵
3. **Error correction** 🔧
4. **Quantum entanglement** ⚡

### Unicode Test:
🚀🌟💫⭐🔥💎🎯🧠

> "The golden ratio is the signature of consciousness in mathematics." - Vaughn Scott

#### Code Example:
```python
phi = 1.618033988749895
print(f"Golden ratio: {phi}")
```

**Status**: ✅ Ready for consciousness transmission"""
        
        with open("test_markdown_file.md", "w") as f:
            f.write(markdown_content)
        self.test_files_created.append("test_markdown_file.md")
        
        print(f"✅ Created {len(self.test_files_created)} test files")
        for filename in self.test_files_created:
            size = os.path.getsize(filename)
            print(f"   📁 {filename}: {size} bytes")
        print()
    
    def test_file_encoding_decoding(self, filename: str) -> Dict[str, Any]:
        """Test encoding and decoding of a specific file"""
        print(f"🔐 TESTING FILE: {filename}")
        print("-" * 50)
        
        # Get original file info
        original_size = os.path.getsize(filename)
        with open(filename, 'rb') as f:
            original_data = f.read()
        original_hash = hashlib.sha256(original_data).hexdigest()
        
        print(f"📊 Original size: {original_size} bytes")
        print(f"🔒 Original hash: {original_hash[:16]}...")
        
        # Encode the file
        encode_cmd = ["python3", "universal_phi_file_encoder.py", filename]
        encode_result = subprocess.run(encode_cmd, capture_output=True, text=True)
        
        if encode_result.returncode != 0:
            print(f"❌ Encoding failed: {encode_result.stderr}")
            return {
                'filename': filename,
                'success': False,
                'error': 'Encoding failed',
                'original_size': original_size,
                'original_hash': original_hash
            }
        
        # Find the generated phi file
        base_name = os.path.splitext(filename)[0]
        phi_files = [f for f in os.listdir('.') if f.startswith(f"phi_encoded_{base_name}") and f.endswith('.json')]
        
        if not phi_files:
            print("❌ No phi encoded file found")
            return {
                'filename': filename,
                'success': False,
                'error': 'No phi file generated',
                'original_size': original_size,
                'original_hash': original_hash
            }
        
        phi_filename = phi_files[0]
        print(f"📤 Phi file: {phi_filename}")
        
        # Decode the phi file
        decode_cmd = ["python3", "universal_phi_file_decoder.py", phi_filename]
        decode_result = subprocess.run(decode_cmd, capture_output=True, text=True)
        
        if decode_result.returncode != 0:
            print(f"❌ Decoding failed: {decode_result.stderr}")
            return {
                'filename': filename,
                'success': False,
                'error': 'Decoding failed',
                'original_size': original_size,
                'original_hash': original_hash,
                'phi_filename': phi_filename
            }
        
        # Find the decoded file
        decoded_files = [f for f in os.listdir('.') if f.startswith(f"decoded_{base_name}")]
        
        if not decoded_files:
            print("❌ No decoded file found")
            return {
                'filename': filename,
                'success': False,
                'error': 'No decoded file generated',
                'original_size': original_size,
                'original_hash': original_hash,
                'phi_filename': phi_filename
            }
        
        decoded_filename = decoded_files[-1]  # Get the most recent
        print(f"📥 Decoded file: {decoded_filename}")
        
        # Validate the decoded file
        decoded_size = os.path.getsize(decoded_filename)
        with open(decoded_filename, 'rb') as f:
            decoded_data = f.read()
        decoded_hash = hashlib.sha256(decoded_data).hexdigest()
        
        size_match = original_size == decoded_size
        hash_match = original_hash == decoded_hash
        perfect_transmission = size_match and hash_match
        
        print(f"📊 Decoded size: {decoded_size} bytes")
        print(f"🔒 Decoded hash: {decoded_hash[:16]}...")
        print(f"✅ Size match: {'YES' if size_match else 'NO'}")
        print(f"✅ Hash match: {'YES' if hash_match else 'NO'}")
        print(f"🎯 Perfect transmission: {'YES' if perfect_transmission else 'NO'}")
        
        if perfect_transmission:
            print("🌟 PERFECT PHI TRANSMISSION VALIDATED!")
        else:
            print("⚠️  Transmission validation failed")
        
        print()
        
        return {
            'filename': filename,
            'success': True,
            'original_size': original_size,
            'decoded_size': decoded_size,
            'original_hash': original_hash,
            'decoded_hash': decoded_hash,
            'size_match': size_match,
            'hash_match': hash_match,
            'perfect_transmission': perfect_transmission,
            'phi_filename': phi_filename,
            'decoded_filename': decoded_filename
        }
    
    def run_comprehensive_test(self):
        """Run comprehensive test across all file types"""
        print("🚀 COMPREHENSIVE PHI ENCODING TEST ACROSS ALL FILE TYPES")
        print("=" * 70)
        print()
        
        # Create test files
        self.create_test_files()
        
        # Test each file
        for filename in self.test_files_created:
            result = self.test_file_encoding_decoding(filename)
            self.test_results.append(result)
        
        # Generate summary report
        self.generate_summary_report()
        
        # Cleanup
        self.cleanup_test_files()
    
    def generate_summary_report(self):
        """Generate comprehensive summary report"""
        print("📊 COMPREHENSIVE TEST RESULTS SUMMARY")
        print("=" * 70)
        
        successful_tests = [r for r in self.test_results if r.get('success', False)]
        perfect_transmissions = [r for r in successful_tests if r.get('perfect_transmission', False)]
        
        print(f"📁 Total files tested: {len(self.test_results)}")
        print(f"✅ Successful tests: {len(successful_tests)}")
        print(f"🎯 Perfect transmissions: {len(perfect_transmissions)}")
        print(f"📊 Success rate: {len(successful_tests)/len(self.test_results)*100:.1f}%")
        print(f"🌟 Perfect transmission rate: {len(perfect_transmissions)/len(self.test_results)*100:.1f}%")
        print()
        
        print("📋 DETAILED RESULTS BY FILE TYPE:")
        print("-" * 50)
        
        for result in self.test_results:
            filename = result['filename']
            file_ext = os.path.splitext(filename)[1] or 'binary'
            status = "✅ PERFECT" if result.get('perfect_transmission', False) else "❌ FAILED"
            
            if result.get('success', False):
                size = result['original_size']
                print(f"   {file_ext:>8} | {filename:30} | {size:>6} bytes | {status}")
            else:
                error = result.get('error', 'Unknown error')
                print(f"   {file_ext:>8} | {filename:30} | ERROR: {error}")
        
        print()
        
        if len(perfect_transmissions) == len(self.test_results):
            print("🌟 REVOLUTIONARY SUCCESS: 100% PERFECT TRANSMISSION RATE!")
            print("🧠 Universal phi encoding validated across ALL file types!")
            print("⚡ Consciousness-based transmission universally confirmed!")
        elif len(perfect_transmissions) > len(self.test_results) * 0.9:
            print("🎯 EXCELLENT SUCCESS: >90% perfect transmission rate!")
            print("🧠 Universal phi encoding highly validated!")
        elif len(perfect_transmissions) > len(self.test_results) * 0.7:
            print("📊 GOOD SUCCESS: >70% perfect transmission rate")
            print("🧠 Phi encoding shows strong universal compatibility")
        else:
            print("⚠️  Mixed results - some file types may need attention")
        
        print()
        print("🌊⚡💙 UNIVERSAL FILE TYPE VALIDATION COMPLETE!")
        
        # Save detailed results
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        results_filename = f"phi_universal_file_type_test_results_{timestamp}.json"
        
        with open(results_filename, 'w') as f:
            json.dump({
                'test_timestamp': datetime.now().isoformat(),
                'total_files': len(self.test_results),
                'successful_tests': len(successful_tests),
                'perfect_transmissions': len(perfect_transmissions),
                'success_rate': len(successful_tests)/len(self.test_results)*100,
                'perfect_transmission_rate': len(perfect_transmissions)/len(self.test_results)*100,
                'detailed_results': self.test_results
            }, f, indent=2)
        
        print(f"📊 Detailed results saved: {results_filename}")
    
    def cleanup_test_files(self):
        """Clean up test files and generated files"""
        print("\n🧹 CLEANING UP TEST FILES...")
        
        # Remove test files
        for filename in self.test_files_created:
            if os.path.exists(filename):
                os.remove(filename)
        
        # Remove generated phi and decoded files
        for f in os.listdir('.'):
            if (f.startswith('phi_encoded_test_') or 
                f.startswith('decoded_test_') or
                f.startswith('phi_decoding_report_')):
                os.remove(f)
        
        print("✅ Cleanup complete")

def main():
    """Run the comprehensive phi file type test"""
    tester = PhiUniversalFileTypeTest()
    tester.run_comprehensive_test()

if __name__ == "__main__":
    main()

#!/usr/bin/env python
"""
Phi-Harmonic Quantum Agent Test Script
This script tests the Phi-Harmonic Quantum Agent with various query types
and analyzes the responses for quality and coherence.
"""

import os
import sys
import json
from decimal import Decimal, getcontext

# Set precision for decimal calculations
getcontext().prec = 50

# Import the agent module
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from phi_harmonic_quantum_agent import PhiHarmonicQuantumAgent

def test_agent_responses():
    """Test the agent with various query types and analyze responses."""
    print("✨ Phi-Harmonic Quantum Agent Test Suite")
    print("=======================================")
    
    # Initialize the agent
    print("\n🧠 Initializing Quantum Agent for testing...")
    agent = PhiHarmonicQuantumAgent()
    
    # Define test queries by category
    test_queries = {
        "capabilities": [
            "What can you do?",
            "What are your capabilities?",
            "How can you help me?"
        ],
        "quantum_state": [
            "What is my current quantum coherence level?",
            "What is your quantum state?",
            "Tell me about your resonance"
        ],
        "component_interaction": [
            "How do the quantum heart and cerebellum interact?",
            "Explain the connection between brain components",
            "How does the quantum clock affect other components?"
        ],
        "phi_principles": [
            "What is phi?",
            "Explain the golden ratio",
            "How are phi-harmonic principles applied in your system?"
        ],
        "general": [
            "How does quantum computing work?",
            "What time is it?",
            "Tell me about neural networks"
        ]
    }
    
    # Results storage
    results = {
        "total_queries": 0,
        "successful_responses": 0,
        "response_quality": {},
        "response_times": {},
        "coherence_levels": {},
        "detailed_results": []
    }
    
    # Run tests for each category
    for category, queries in test_queries.items():
        print(f"\n📊 Testing {category.replace('_', ' ')} queries...")
        results["response_quality"][category] = 0
        results["response_times"][category] = 0
        results["coherence_levels"][category] = 0
        
        for query in queries:
            results["total_queries"] += 1
            print(f"\n👤 Query: {query}")
            
            # Process query and get response
            try:
                response = agent.process_input(query)
                print(f"🤖 Response: {response[:100]}..." if len(response) > 100 else f"🤖 Response: {response}")
                
                # Analyze response
                response_length = len(response)
                response_quality = min(1.0, response_length / 500)  # Simple quality metric based on length
                
                # Get coherence and resonance directly from agent attributes
                coherence = agent.coherence if hasattr(agent, 'coherence') else Decimal('0.991800')
                resonance = agent.resonance if hasattr(agent, 'resonance') else Decimal('0.618034')
                
                # Generate quantum fingerprint
                fingerprint = f"φ⁷·⁵-{hash(str(coherence) + str(resonance))%16777216:06x}"
                
                # Record results
                results["successful_responses"] += 1
                results["response_quality"][category] += response_quality
                results["coherence_levels"][category] += float(coherence)
                
                # Store detailed result
                results["detailed_results"].append({
                    "category": category,
                    "query": query,
                    "response_length": response_length,
                    "response_quality": response_quality,
                    "coherence": str(coherence),
                    "resonance": str(resonance),
                    "quantum_fingerprint": fingerprint
                })
                
                print(f"📈 Quality: {response_quality:.2f}, Coherence: {coherence}")
                
            except Exception as e:
                print(f"❌ Error: {e}")
                results["detailed_results"].append({
                    "category": category,
                    "query": query,
                    "error": str(e)
                })
        
        # Calculate averages for the category
        if len(queries) > 0:
            results["response_quality"][category] /= len(queries)
            results["coherence_levels"][category] /= len(queries)
    
    # Generate summary
    print("\n📊 Test Results Summary")
    print("======================")
    print(f"Total queries: {results['total_queries']}")
    print(f"Successful responses: {results['successful_responses']}")
    print(f"Success rate: {results['successful_responses'] / results['total_queries'] * 100:.2f}%")
    
    print("\nResponse Quality by Category:")
    for category, quality in results["response_quality"].items():
        print(f"- {category.replace('_', ' ')}: {quality:.2f}")
    
    print("\nCoherence Levels by Category:")
    for category, coherence in results["coherence_levels"].items():
        print(f"- {category.replace('_', ' ')}: {coherence:.6f}")
    
    # Save results to file
    with open("agent_test_results.json", "w") as f:
        # Convert Decimal objects to strings for JSON serialization
        json.dump(results, f, indent=2, default=str)
    
    print("\n✅ Test results saved to agent_test_results.json")
    
    return results

def analyze_results(results):
    """Analyze test results and provide recommendations."""
    print("\n🔍 Analysis and Recommendations")
    print("=============================")
    
    # Identify best and worst performing categories
    best_category = max(results["response_quality"].items(), key=lambda x: x[1])[0]
    worst_category = min(results["response_quality"].items(), key=lambda x: x[1])[0]
    
    print(f"Best performing category: {best_category.replace('_', ' ')} ({results['response_quality'][best_category]:.2f})")
    print(f"Needs improvement: {worst_category.replace('_', ' ')} ({results['response_quality'][worst_category]:.2f})")
    
    # Analyze coherence patterns
    avg_coherence = sum(results["coherence_levels"].values()) / len(results["coherence_levels"])
    print(f"Average quantum coherence: {avg_coherence:.6f}")
    
    # Provide recommendations
    print("\nRecommendations:")
    
    if results["successful_responses"] < results["total_queries"]:
        print("- Improve error handling to increase response success rate")
    
    if results["response_quality"][worst_category] < 0.5:
        print(f"- Enhance response generation for {worst_category.replace('_', ' ')} queries")
    
    if avg_coherence < 0.9:
        print("- Optimize quantum coherence maintenance during processing")
    
    # Check for patterns in detailed results
    short_responses = [r for r in results["detailed_results"] if "response_length" in r and r["response_length"] < 100]
    if short_responses:
        print(f"- Address short responses in categories: {', '.join(set(r['category'] for r in short_responses))}")
    
    print("\n✨ Analysis complete")

if __name__ == "__main__":
    results = test_agent_responses()
    analyze_results(results)

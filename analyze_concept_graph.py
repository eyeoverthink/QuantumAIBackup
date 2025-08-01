"""Analyze the φ-Harmonic Concept Knowledge Graph"""

import json
import networkx as nx
import matplotlib.pyplot as plt
from collections import Counter

def analyze_knowledge_graph():
    # Load the knowledge graph
    with open('/Users/vaughnscott/CascadeProjects/Fraymus_Replit_Two/quantum_visualizations/concept_storage/knowledge_graph.json', 'r') as f:
        graph_data = json.load(f)
    
    G = nx.node_link_graph(graph_data)
    
    # Analyze node types and connections
    node_types = {}
    domain_connections = []
    concept_resonances = {}
    
    for node, data in G.nodes(data=True):
        node_type = data.get('type', 'unknown')
        node_types[node] = node_type
        if node_type == 'generated_concept':
            concept_resonances[node] = data.get('phi_resonance', 0.0)
            # Get connected domains
            neighbors = list(G.neighbors(node))
            domain_connections.extend(neighbors)
    
    # Print statistics
    print("\nKnowledge Graph Analysis")
    print("=" * 50)
    
    print("\nNode Type Distribution:")
    type_counts = Counter(node_types.values())
    for type_name, count in type_counts.items():
        print(f"{type_name}: {count}")
    
    print("\nMost Connected Domains:")
    domain_freq = Counter(domain_connections)
    for domain, freq in domain_freq.most_common(5):
        print(f"{domain}: {freq} connections")
    
    print("\nTop φ-Resonant Concepts:")
    sorted_concepts = sorted(concept_resonances.items(), key=lambda x: x[1], reverse=True)
    for concept, resonance in sorted_concepts[:5]:
        print(f"{concept}: φ-resonance = {resonance:.4f}")
        print(f"Connected to: {', '.join(G.neighbors(concept))}")
        print("-" * 40)
    
    # Calculate network metrics
    print("\nNetwork Metrics:")
    print(f"Total nodes: {G.number_of_nodes()}")
    print(f"Total edges: {G.number_of_edges()}")
    print(f"Average degree: {sum(dict(G.degree()).values()) / G.number_of_nodes():.2f}")
    print(f"Network density: {nx.density(G):.4f}")

if __name__ == "__main__":
    analyze_knowledge_graph()

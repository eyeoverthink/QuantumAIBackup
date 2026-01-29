"""
Quantum Protein Visualizer - 3D visualization and PDB integration
"""
import py3Dmol
from Bio import PDB
import numpy as np
from typing import Dict, List, Tuple
import requests
import tempfile
import os

class QuantumProteinVisualizer:
    def __init__(self):
        self.pdb_parser = PDB.PDBParser(QUIET=True)
        self.colors = {
            'H': '0xff0000',  # Alpha helix - red
            'B': '0x00ff00',  # Beta sheet - green
            'C': '0x0000ff',  # Coil - blue
            'bridge': '0xffff00',  # Quantum bridge - yellow
            'binding': '0xff00ff'  # Binding site - purple
        }

    def fetch_pdb(self, pdb_id: str) -> str:
        """Fetch PDB file from RCSB database"""
        url = f"https://files.rcsb.org/download/{pdb_id}.pdb"
        response = requests.get(url)
        if response.status_code == 200:
            # Save to temporary file
            with tempfile.NamedTemporaryFile(delete=False, suffix='.pdb') as tmp:
                tmp.write(response.content)
                return tmp.name
        return None

    def create_visualization(self, structure_data: Dict, pdb_file: str = None) -> str:
        """Create 3D visualization of protein structure with quantum metrics"""
        view = py3Dmol.view(width=800, height=600)
        
        if pdb_file and os.path.exists(pdb_file):
            try:
                # Load PDB structure
                with open(pdb_file, 'r') as f:
                    view.addModel(f.read(), "pdb")
                
                # Basic protein representation
                view.setStyle({'cartoon': {'color': 'spectrum'}})
                
                # Add quantum bridges
                for bridge in structure_data.get('quantum_bridges', []):
                    pos1, pos2 = bridge['position']-1, bridge['position']
                    view.addCylinder({
                        'start': {'x': pos1*3, 'y': 0, 'z': 0},
                        'end': {'x': pos2*3, 'y': 0, 'z': 0},
                        'radius': 0.3,
                        'color': self.colors['bridge'],
                        'fromCap': 1,
                        'toCap': 1
                    })
                
                # Add binding sites
                for site in structure_data.get('binding_sites', []):
                    pos = site['position']
                    view.addSphere({
                        'center': {'x': pos*3, 'y': 0, 'z': 0},
                        'radius': 1.0,
                        'color': self.colors['binding'],
                        'alpha': 0.7
                    })
                
                # Add quantum metrics visualization
                self._add_quantum_metrics(view, structure_data)
                
                # Clean up PDB file after visualization is created
                os.unlink(pdb_file)
                
            except Exception as e:
                print(f"Error creating visualization: {e}")
                if os.path.exists(pdb_file):
                    os.unlink(pdb_file)
                return None
        
        return view

    def _add_quantum_metrics(self, view, structure_data: Dict):
        """Add quantum metrics visualization"""
        if 'resonance_pattern' in structure_data:
            # Create resonance surface
            points = []
            for i, res in enumerate(structure_data['resonance_pattern']):
                points.append({
                    'x': i*3,
                    'y': float(res),
                    'z': 0
                })
            
            # Add resonance surface
            view.addSurface(py3Dmol.VDW, {
                'points': points,
                'opacity': 0.5,
                'colorscheme': {
                    'gradient': 'rwb',
                    'min': min(structure_data['resonance_pattern']),
                    'max': max(structure_data['resonance_pattern'])
                }
            })

    def analyze_pdb_structure(self, pdb_id: str) -> Dict:
        """Analyze PDB structure and return quantum metrics"""
        pdb_file = self.fetch_pdb(pdb_id)
        if not pdb_file:
            print(f"Failed to fetch PDB file for {pdb_id}")
            return None
            
        try:
            # Parse structure
            structure = self.pdb_parser.get_structure(pdb_id, pdb_file)
            
            # Extract sequence and structure
            sequence = ""
            ss_elements = []
            
            for model in structure:
                for chain in model:
                    for res in chain:
                        if 'CA' in res:  # Only look at amino acids with alpha carbons
                            try:
                                aa = PDB.Polypeptide.protein_letters_3to1[res.get_resname()]
                                sequence += aa
                                # Simple secondary structure estimation based on phi/psi angles
                                if all(atom in res for atom in ['N', 'CA', 'C', 'O']):
                                    phi = PDB.calc_dihedral(res['N'].get_vector(),
                                                          res['CA'].get_vector(),
                                                          res['C'].get_vector(),
                                                          res['O'].get_vector())
                                    if -60 < phi < -45:  # Approximate alpha helix
                                        ss_elements.append('H')
                                    elif -120 < phi < -110:  # Approximate beta sheet
                                        ss_elements.append('B')
                                    else:
                                        ss_elements.append('C')
                                else:
                                    ss_elements.append('C')  # Default to coil if missing atoms
                            except Exception as e:
                                print(f"Warning: Could not process residue {res.get_resname()}: {e}")
                                continue
                    
                    if sequence:  # Only process first chain with valid sequence
                        break
                break  # Only process first model
            
            if not sequence:
                print("Warning: No valid amino acid sequence found in structure")
                return None
                
            print(f"Successfully extracted sequence of length {len(sequence)}")
            
            return {
                'pdb_id': pdb_id,
                'sequence': sequence,
                'secondary_structure': ss_elements,
                'structure_file': pdb_file  # Keep the file path
            }
            
        except Exception as e:
            print(f"Error analyzing PDB structure: {e}")
            if os.path.exists(pdb_file):
                os.unlink(pdb_file)
            return None

    def create_interactive_view(self, pdb_id: str, quantum_analysis: Dict) -> None:
        """Create interactive 3D view with quantum metrics"""
        # Fetch and analyze PDB
        pdb_data = self.analyze_pdb_structure(pdb_id)
        if not pdb_data:
            return None
            
        # Combine PDB and quantum analysis
        combined_data = {**pdb_data, **quantum_analysis}
        
        # Create visualization
        view = self.create_visualization(combined_data, pdb_data['structure_file'])
        if not view:
            return None
        
        # Add interactive elements
        view.zoomTo()
        
        # Instead of using a callback, we'll add hover info
        view.addStyle({},{'stick':{}})
        view.setStyle({'cartoon':{'color':'spectrum'}})
        
        # Add labels for quantum bridges
        for bridge in combined_data.get('quantum_bridges', []):
            pos = bridge['position']
            label = f"Bridge: {bridge['residues']}\nRatio: {bridge['ratio']:.3f}"
            view.addLabel(label, {'position': {'x': pos*3, 'y': 0, 'z': 0}})
        
        # Add labels for binding sites
        for site in combined_data.get('binding_sites', []):
            pos = site['position']
            label = f"Binding Site\nCoherence: {site['coherence']:.3f}"
            view.addLabel(label, {'position': {'x': pos*3, 'y': 2, 'z': 0}})
        
        return view

    def _on_click(self, atom, data: Dict) -> None:
        """Handle click events on the 3D structure"""
        if atom:
            res_num = atom.resi
            # Find quantum metrics for this residue
            metrics = self._get_residue_metrics(res_num, data)
            print(f"\nResidue {res_num} Quantum Metrics:")
            print(f"Resonance: {metrics['resonance']:.4f}")
            print(f"Coherence: {metrics['coherence']:.4f}")
            if metrics.get('bridge'):
                print(f"Quantum Bridge: {metrics['bridge']}")

    def _get_residue_metrics(self, res_num: int, data: Dict) -> Dict:
        """Get quantum metrics for a specific residue"""
        metrics = {
            'resonance': 0.0,
            'coherence': 0.0
        }
        
        if 'resonance_pattern' in data and res_num < len(data['resonance_pattern']):
            metrics['resonance'] = data['resonance_pattern'][res_num]
            
        # Check for quantum bridges
        for bridge in data.get('quantum_bridges', []):
            if bridge['position'] == res_num:
                metrics['bridge'] = bridge
                
        return metrics

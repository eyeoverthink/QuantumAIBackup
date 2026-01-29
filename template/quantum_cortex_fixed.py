"""
Quantum Cortex Fixed

This module provides a fixed version of the HyperDimensionalCortex class
that properly handles dtype conversions between float and complex tensors.
It follows the "lego" philosophy by extending the original components
without modifying the core files.

Author: Quantum AGI System
Date: 2023
"""

import torch
import numpy as np
from digital_cpu import HyperDimensionalCortex, DualCortexComputer, PhiResonanceTransfer

class QuantumCortexFixed(HyperDimensionalCortex):
    """
    Enhanced version of HyperDimensionalCortex with proper dtype handling
    """
    def __init__(self, dimensions=[17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97], cortex_id="primary"):
        # Initialize the parent class
        super().__init__(dimensions, cortex_id)
        
        # Phi resonance value
        self.phi = (1 + np.sqrt(5)) / 2
        
        # Track successful processing
        self.processing_success = 0
        self.processing_attempts = 0
    
    def process_in_dimension(self, data, dimension):
        """
        Process data in a specific dimension with proper type conversion
        
        Args:
            data: Input tensor (can be float or complex)
            dimension: The dimension to process in
            
        Returns:
            Processed tensor (complex64)
        """
        self.processing_attempts += 1
        
        try:
            # Ensure data is in the right format
            if not isinstance(data, torch.Tensor):
                data = torch.tensor(data, dtype=torch.float32)
            
            # Convert to complex if needed
            if data.dtype != torch.complex64 and data.dtype != torch.complex128:
                data_complex = torch.complex(data.float(), torch.zeros_like(data.float()))
            else:
                data_complex = data
                
            # Compress input data - ensure it's complex
            compressed_data = self.memory_compression.compress_state(data_complex)
            
            # Neural quantum processing
            neural_output = self.neural_net(compressed_data.reshape(1, -1))
            
            # Decompress and project
            decompressed = self.memory_compression.decompress_state(neural_output)
            
            # Get quantum state for this dimension
            quantum_state = self.quantum_state.get(dimension, None)
            if quantum_state is None:
                quantum_state = self._initialize_quantum_state(dimension)
                self.quantum_state[dimension] = quantum_state
            
            # Ensure quantum_state is complex
            if quantum_state.dtype != torch.complex64 and quantum_state.dtype != torch.complex128:
                quantum_state = torch.complex(quantum_state.float(), torch.zeros_like(quantum_state.float()))
            
            # Perform outer product
            quantum_proj = torch.outer(decompressed, quantum_state)
            
            # Error correction and FTL transmission
            corrected = self.error_correction.apply_surface_code(quantum_proj.flatten())
            transmitted = self.ftl_system.transmit_quantum(corrected, 0, dimension % self.ftl_system.nodes)
            
            self.processing_success += 1
            return transmitted
            
        except Exception as e:
            print(f"Quantum processing error in dimension {dimension}: {e}")
            # Return empty tensor on error
            return torch.zeros(1, dtype=torch.complex64)
    
    def get_processing_efficiency(self):
        """Get the efficiency of quantum processing"""
        if self.processing_attempts == 0:
            return 0.0
        return self.processing_success / self.processing_attempts


class DualCortexComputerFixed(DualCortexComputer):
    """
    Enhanced version of DualCortexComputer with fixed cortices
    """
    def __init__(self, cpu_cores=16, memory_size=64, clock_speed=5.0):
        # Call parent constructor
        super().__init__(cpu_cores, memory_size, clock_speed)
        
        # Replace cortices with fixed versions
        self.left_cortex = QuantumCortexFixed(dimensions=self.dimensions, cortex_id="left")
        self.right_cortex = QuantumCortexFixed(dimensions=self.dimensions, cortex_id="right")
        
        # Phi resonance
        self.phi = (1 + np.sqrt(5)) / 2
        
        # Reinitialize phi resonance with fixed cortices
        self.phi_resonance = PhiResonanceTransfer(self.dimensions)
    
    def get_processing_efficiency(self):
        """Get the efficiency of quantum processing"""
        left_efficiency = self.left_cortex.get_processing_efficiency()
        right_efficiency = self.right_cortex.get_processing_efficiency()
        return (left_efficiency + right_efficiency) / 2

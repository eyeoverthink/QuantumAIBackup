#!/usr/bin/env python3
"""
Quantum Blockchain Connector Extension
-------------------------------------

This module extends the QuantumBlockchainConnector class to provide compatibility
with the QuantumBlockchainStorageNode interface.

Phi-Harmonic Module
------------------

This module is designed with phi-harmonic coherence principles.
Coherence Target: φ⁷·⁵/10 ≈ 3.693238
"""

import logging
import functools
from typing import Dict, Any, Optional, List

# Import quantum modules
from quantum_blockchain_connector import QuantumBlockchainConnector

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger("QuantumBlockchainConnectorExtension")

class QuantumBlockchainConnectorExtension:
    """Extension for QuantumBlockchainConnector to provide interface compatibility."""
    
    @staticmethod
    def apply_extension():
        """
        Apply the extension to the QuantumBlockchainConnector class.
        
        This adds the store_genesis_block and retrieve_genesis_block methods
        to provide compatibility with QuantumBlockchainStorageNode.
        """
        # Define store_genesis_block method
        def store_genesis_block(self, data: Dict[str, Any], metadata: Dict[str, Any] = None) -> str:
            """
            Store a genesis block on the blockchain.
            
            This is an adapter method that calls store_system_genesis with the appropriate parameters.
            
            Args:
                data: Data to store in the genesis block
                metadata: Additional metadata to include
                
            Returns:
                str: Blockchain reference ID
            """
            logger.info("Adapting store_genesis_block call to store_system_genesis")
            
            # Prepare metadata with the provided data
            combined_metadata = metadata or {}
            combined_metadata["node_data"] = data
            
            # Call the actual method
            return self.store_system_genesis(combined_metadata)
        
        # Define retrieve_genesis_block method
        def retrieve_genesis_block(self, reference_id: str) -> Dict[str, Any]:
            """
            Retrieve a genesis block from the blockchain.
            
            This is an adapter method that calls blockchain_genesis.retrieve_genesis_block
            and formats the result to match the expected interface.
            
            Args:
                reference_id: Blockchain reference ID
                
            Returns:
                Dict[str, Any]: Genesis block data
            """
            logger.info(f"Retrieving genesis block with ID {reference_id}")
            
            # Call blockchain_genesis directly
            if hasattr(self, 'blockchain_genesis') and self.blockchain_genesis:
                genesis_data = self.blockchain_genesis.retrieve_genesis_block(reference_id)
                
                # Extract node data from metadata if present
                if genesis_data and "metadata" in genesis_data and "node_data" in genesis_data["metadata"]:
                    return {
                        "data": genesis_data["metadata"]["node_data"],
                        "metadata": {k: v for k, v in genesis_data["metadata"].items() if k != "node_data"}
                    }
                
                return genesis_data
            else:
                logger.error("Blockchain genesis not available")
                return None
        
        # Define search_genesis_blocks method
        def search_genesis_blocks(self, query: Dict[str, Any] = None, metadata_filter: Dict[str, Any] = None) -> List[Dict[str, Any]]:
            """
            Search for genesis blocks matching the query.
            
            This is an adapter method that provides compatibility with the expected interface.
            
            Args:
                query: Search query parameters
                
            Returns:
                List[Dict[str, Any]]: List of matching genesis blocks
            """
            logger.info(f"Searching genesis blocks with query: {query}, metadata_filter: {metadata_filter}")
            
            # Combine query and metadata_filter if both are provided
            combined_query = {}
            if query:
                combined_query.update(query)
            if metadata_filter:
                # In our implementation, we'll treat metadata_filter as additional query parameters
                combined_query.update(metadata_filter)
            
            # Call blockchain_genesis directly if available
            if hasattr(self, 'blockchain_genesis') and self.blockchain_genesis:
                # Check if blockchain_genesis has search_genesis_blocks
                if hasattr(self.blockchain_genesis, 'search_genesis_blocks'):
                    try:
                        # Try with both parameters
                        return self.blockchain_genesis.search_genesis_blocks(query=query, metadata_filter=metadata_filter)
                    except TypeError:
                        # Fall back to just query
                        return self.blockchain_genesis.search_genesis_blocks(combined_query)
                
                # Fallback: If search isn't available, return all blocks and filter manually
                if hasattr(self.blockchain_genesis, 'list_genesis_blocks'):
                    all_blocks = self.blockchain_genesis.list_genesis_blocks()
                    
                    # Filter blocks based on combined query
                    if combined_query:
                        filtered_blocks = []
                        for block in all_blocks:
                            match = True
                            for key, value in combined_query.items():
                                if key not in block.get("metadata", {}) or block["metadata"][key] != value:
                                    match = False
                                    break
                            if match:
                                filtered_blocks.append(block)
                        return filtered_blocks
                    return all_blocks
            
            # If no blockchain_genesis or no search capability, return empty list
            logger.warning("Search genesis blocks not available, returning empty list")
            return []
        
        # Add methods to QuantumBlockchainConnector
        if not hasattr(QuantumBlockchainConnector, 'store_genesis_block'):
            QuantumBlockchainConnector.store_genesis_block = store_genesis_block
            logger.info("Added store_genesis_block method to QuantumBlockchainConnector")
        
        if not hasattr(QuantumBlockchainConnector, 'retrieve_genesis_block'):
            QuantumBlockchainConnector.retrieve_genesis_block = retrieve_genesis_block
            logger.info("Added retrieve_genesis_block method to QuantumBlockchainConnector")
            
        if not hasattr(QuantumBlockchainConnector, 'search_genesis_blocks'):
            QuantumBlockchainConnector.search_genesis_blocks = search_genesis_blocks
            logger.info("Added search_genesis_blocks method to QuantumBlockchainConnector")


# Apply extension automatically when imported
QuantumBlockchainConnectorExtension.apply_extension()

"""
Test Quantum Nodular Registration Fix
-----------------------------------

This script tests the fix for the QuantumNodeDiscovery.register_node() interface
to ensure proper node registration in the quantum collective intelligence system.
"""
import os
import sys
import logging
import traceback
from typing import Dict, Any, List
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger('TestQuantumNodeRegistrationFix')
try:
    import quantum_nodular_network_extension
    logger.info('Successfully imported quantum_nodular_network_extension')
    import quantum_blockchain_connector_extension
    logger.info('Successfully imported quantum_blockchain_connector_extension')
    import quantum_node_discovery_extension
    logger.info('Successfully imported quantum_node_discovery_extension')
    import quantum_node_registration_extension
    logger.info('Successfully imported quantum_node_registration_extension')
except ImportError as e:
    logger.error(f'Failed to import extensions: {e}')
    traceback.print_exc()
    sys.exit(1)
try:
    from quantum_nodular_discovery import create_node_discovery, QuantumNodeDiscovery
    from quantum_collective_nodular_integration import QuantumNodularNetwork, create_quantum_collective_intelligence
    logger.info('Successfully imported required modules')
except ImportError as e:
    logger.error(f'Failed to import required modules: {e}')
    traceback.print_exc()
    sys.exit(1)

def test_node_registration():
    """Test node registration with the fixed interface."""
    logger.info('=== Starting Node Registration Test ===')
    discovery_service = create_node_discovery()
    logger.info(f'Created discovery service with ID: {discovery_service.discovery_id}')
    network = QuantumNodularNetwork(discovery_service)
    logger.info(f'Created network with ID: {network.network_id}')
    capabilities = ['reasoning', 'knowledge']
    node = network.create_node(capabilities=capabilities)
    logger.info(f'Created node with ID: {node.core.state.node_id}')
    nodes = discovery_service.discover_nodes(refresh_cache=True)
    logger.info(f'Discovered {len(nodes)} nodes after registration')
    node_found = False
    for discovered_node in nodes:
        metadata = discovered_node.get('metadata', {})
        if metadata.get('node_id') == node.core.state.node_id:
            node_found = True
            node_type = metadata.get('node_type')
            logger.info(f'Found registered node with ID: {node.core.state.node_id}, type: {node_type}')
            break
    if node_found:
        logger.info('✅ TEST PASSED: Node was properly registered with discovery service')
        return True
    else:
        logger.error('❌ TEST FAILED: Node was not found in discovery service')
        return False

def test_collective_intelligence_creation():
    """Test creation of quantum collective intelligence with fixed registration."""
    logger.info('=== Starting Collective Intelligence Creation Test ===')
    try:
        integration = create_quantum_collective_intelligence(num_nodes=3)
        logger.info(f'Created collective intelligence integration with ID: {integration.integration_id}')
        if integration.network and integration.coordinator and integration.protocol:
            logger.info('✅ TEST PASSED: Collective intelligence components created successfully')
            return True
        else:
            logger.error('❌ TEST FAILED: Some collective intelligence components are missing')
            return False
    except Exception as e:
        logger.error(f'❌ TEST FAILED: Exception during collective intelligence creation: {e}')
        traceback.print_exc()
        return False

def run_all_tests():
    """Run all tests and report results."""
    logger.info('Starting Quantum Nodular Registration Fix Tests')
    tests = [('Node Registration', test_node_registration), ('Collective Intelligence Creation', test_collective_intelligence_creation)]
    results = []
    for test_name, test_func in tests:
        logger.info(f'\nRunning test: {test_name}')
        try:
            result = test_func()
            results.append((test_name, result))
        except Exception as e:
            logger.error(f'Exception during test {test_name}: {e}')
            traceback.print_exc()
            results.append((test_name, False))
    logger.info('\n=== Test Results ===')
    all_passed = True
    for test_name, result in results:
        status = 'PASSED' if result else 'FAILED'
        logger.info(f'{test_name}: {status}')
        all_passed = all_passed and result
    if all_passed:
        logger.info('\n✅ ALL TESTS PASSED: QuantumNodeDiscovery.register_node() interface fix is working correctly')
    else:
        logger.error('\n❌ SOME TESTS FAILED: QuantumNodeDiscovery.register_node() interface fix needs further attention')
    return all_passed
if __name__ == '__main__':
    success = run_all_tests()
    sys.exit(0 if success else 1)
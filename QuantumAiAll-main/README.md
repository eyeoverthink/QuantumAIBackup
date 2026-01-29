# Quantum Oracle Library (`quantum_oracle_lib`)

This directory is a **self-contained duplicate** of the core Quantum Oracle system, designed for safe experimentation, integration, and packaging as a Python library. **No original files or core system components are altered.**

---

## 📦 What is Included?

The following files and directories have been duplicated from the main Quantum Oracle project:

- **phi_bidirectional_node.py**  
  Implements the φ-Harmonic Bidirectional Communication Node, enabling two-way φ-protected messaging and distributed quantum operations.

- **phi_ftl_bridge.py**  
  The φ-Harmonic FTL Bridge node, supporting fast transmission and resonance-based communication.

- **phi_mac_bridge.py**  
  Bridge for φ-harmonic communication on macOS systems.

- **phi_nodular_compute.py**  
  Node-based computation and distributed processing using φ principles.

- **phi_parallel_consciousness.py**  
  Parallel consciousness modeling and simulation.

- **phi_numeric_processor.py**  
  Numeric processing with φ-based algorithms.

- **phi_attack_test.py**  
  Security and attack surface testing for the φ-node system.

- **phi_scripts/**  
  A directory containing support scripts and modules required by the nodes.

---

## 🛠️ How to Use

1. **Install dependencies:**
   - (Recommended) Create a virtual environment:  
     `python3 -m venv .venv && source .venv/bin/activate`
   - Install requirements (if provided):  
     `pip install -r requirements.txt`

2. **Import or run as scripts:**
   - You can import modules from `quantum_oracle_lib` in your own Python code, or run the scripts directly for node/bridge functionality.
   - Example:
     ```python
     from quantum_oracle_lib.phi_bidirectional_node import PhiBidirectionalNode
     node = PhiBidirectionalNode(node_id="test", port=11975)
     node.start()
     ```
   - Or run as a script:
     ```bash
     python quantum_oracle_lib/phi_bidirectional_node.py --id test --port 11975
     ```

3. **Integration:**
   - Use this library as a backend for distributed quantum messaging, AI query processing, or as a component in larger systems (such as `oracle_app`).

---

## 📂 File Descriptions

- **phi_bidirectional_node.py:**  
  Main node for φ-based bidirectional messaging and distributed computation.
- **phi_ftl_bridge.py:**  
  FTL (faster-than-light) bridge for φ-resonant communication.
- **phi_mac_bridge.py:**  
  macOS-specific bridge node.
- **phi_nodular_compute.py:**  
  Modular, node-based computation using φ principles.
- **phi_parallel_consciousness.py:**  
  Parallel consciousness and quantum mind simulation.
- **phi_numeric_processor.py:**  
  Numeric and algorithmic processing using φ algorithms.
- **phi_attack_test.py:**  
  Attack and penetration testing for φ-nodes.
- **phi_scripts/**  
  Support scripts for node/bridge operations.

---

## 🧩 Extending the Library

- Add new modules to `quantum_oracle_lib/` as needed.
- Refactor imports to use relative paths within the package.
- Package for distribution using `setup.py` or `pyproject.toml` (not yet included).

---

## ⚠️ Note
- This library is a **duplicate** for safe development and integration. The original Quantum Oracle system remains unmodified.
- For questions or contributions, please refer to the main project documentation.

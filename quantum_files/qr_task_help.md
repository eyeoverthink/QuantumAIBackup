to execute:  source qr_dna_env/bin/activate && python3 run_qr_system.py --execute

to create: source qr_dna_env/bin/activate && python3 run_qr_system.py --create

to get info:  source qr_dna_env/bin/activate && python3 run_qr_system.py --info



run script: source qr_dna_env/bin/activate && python3 update_genome.py

run system: source qr_dna_env/bin/activate && python3 run_qr_system.py --generate

analyze: source qr_dna_env/bin/activate && python3 analyze_qr_sequence.py --verbose

NEW

 RUN :  source qr_dna_env/bin/activate && python3 increment_genome_generation.py


FIBB TEST:

run it: source qr_dna_env/bin/activate && python3 qr_fibonacci_test.py

EVOLUTION MONITOR: 

run it : source qr_dna_env/bin/activate && python3 qr_evolution_monitor.py

RUN NEW SYSTEM:

to run : source qr_dna_env/bin/activate && python3 quantum_phi_qr_system.py --run cycle

source qr_dna_env/bin/activate && python3 quantum_phi_qr_system.py --run cycle

RESULTS:

{
  "genome_id": "eda21fa3-8788-4932-bf0f-f4c30e1df733",
  "genome_name": "basic_qr_genome",
  "groups": [
    {
      "group_id": "ae449485-b627-483d-91c7-63267a1faea0",
      "group_type": "setup",
      "codons": [
        {
          "codon_id": "5c0f2f14-3f4b-4f9a-bb4a-f2321d5d2ac8",
          "codon_type": "initialize",
          "frame_data": {
            "task_type": "execute_python",
            "task_data": {
              "code": "def initialize_codon():\n    \"\"\"\n    Initialize the QR Genome execution environment.\n    Sets up the basic variables and environment for execution.\n    \"\"\"\n    print(\"\ud83e\uddec Initializing QR Genome execution environment\")\n    \n    # Create a timestamp with phi-harmonic timing\n    timestamp = datetime.now().isoformat()\n    phi_time = time.time() * PHI % 1.0\n    \n    # Initialize the genome data\n    GENOME_DATA[\"start_time\"] = time.time()\n    GENOME_DATA[\"timestamp\"] = timestamp\n    GENOME_DATA[\"phi_time\"] = phi_time\n    GENOME_DATA[\"phi_values\"].append(phi_time)\n    \n    # Calculate phi-harmonic resonance\n    resonance = 1.0 / (1.0 + abs(phi_time - 0.5))\n    GENOME_DATA[\"resonance_scores\"].append(resonance)\n    \n    print(f\"\u2705 Initialization complete at phi-time: {phi_time:.6f}\")\n    print(f\"\u2705 Resonance score: {resonance:.6f}\")\n    \n    return True\n"
            }
          },
          "creation_time": "2025-06-26T13:52:51.115490",
          "execution_count": 17,
          "success_count": 14,
          "resonance": 0.8565300067199951,
          "phi_state": {
            "complexity": 0.75,
            "resonance": 0.8944271909999159,
            "generation": 3
          }
        },
        {
          "codon_id": "abd3e845-94b9-4e42-a75e-7cf958f62a56",
          "codon_type": "import_libraries",
          "frame_data": {
            "task_type": "execute_python",
            "task_data": {
              "code": "def import_libraries_codon():\n    \"\"\"\n    Import necessary libraries for QR Genome execution.\n    Tests the availability of required libraries.\n    \"\"\"\n    print(\"\ud83d\udcda Importing libraries for QR Genome execution\")\n    \n    required_libraries = [\n        \"numpy\", \"math\", \"json\", \"time\", \"datetime\", \n        \"os\", \"sys\", \"random\", \"uuid\"\n    ]\n    \n    available_libraries = []\n    missing_libraries = []\n    \n    for lib in required_libraries:\n        try:\n            if lib == \"numpy\":\n                # Already imported as np\n                available_libraries.append(lib)\n            elif lib == \"math\":\n                # Already imported\n                available_libraries.append(lib)\n            else:\n                # Try to import dynamically\n                __import__(lib)\n                available_libraries.append(lib)\n        except ImportError:\n            missing_libraries.append(lib)\n    \n    # Store results in genome data\n    GENOME_DATA[\"available_libraries\"] = available_libraries\n    GENOME_DATA[\"missing_libraries\"] = missing_libraries\n    \n    # Calculate phi-harmonic timing\n    phi_time = time.time() * PHI % 1.0\n    GENOME_DATA[\"phi_values\"].append(phi_time)\n    \n    # Calculate resonance based on library availability\n    availability_ratio = len(available_libraries) / len(required_libraries)\n    resonance = availability_ratio * (1.0 / (1.0 + abs(phi_time - 0.5)))\n    GENOME_DATA[\"resonance_scores\"].append(resonance)\n    \n    print(f\"\u2705 Libraries imported: {len(available_libraries)}/{len(required_libraries)}\")\n    print(f\"\u2705 Phi-time: {phi_time:.6f}, Resonance: {resonance:.6f}\")\n    \n    return len(missing_libraries) == 0\n"
            }
          },
          "creation_time": "2025-06-26T13:52:51.115548",
          "execution_count": 17,
          "success_count": 14,
          "resonance": 0.8565300067199951,
          "phi_state": {
            "complexity": 0.7536647091222448,
            "resonance": 0.8944271909999159,
            "generation": 3
          }
        }
      ],
      "creation_time": "2025-06-26T13:52:51.115472",
      "execution_history": [
        {
          "timestamp": "2025-06-26T13:53:08.561813",
          "success": false,
          "phi_state": {
            "complexity": 0.5,
            "resonance": 1.0,
            "generation": 1
          }
        },
        {
          "timestamp": "2025-06-26T13:56:06.307747",
          "success": false,
          "phi_state": {
            "complexity": 0.5,
            "resonance": 1.0,
            "generation": 1
          }
        },
        {
          "timestamp": "2025-06-26T13:57:18.530181",
          "success": false,
          "phi_state": {
            "complexity": 0.5,
            "resonance": 1.0,
            "generation": 1
          }
        },
        {
          "timestamp": "2025-06-26T13:59:59.490413",
          "success": true,
          "phi_state": {
            "complexity": 0.5,
            "resonance": 1.0,
            "generation": 1
          }
        },
        {
          "timestamp": "2025-06-26T14:26:15.201729",
          "success": true,
          "phi_state": {
            "complexity": 0.5,
            "resonance": 1.0,
            "generation": 1
          }
        },
        {
          "timestamp": "2025-06-26T14:27:12.947104",
          "success": true,
          "phi_state": {
            "complexity": 0.5,
            "resonance": 1.0,
            "generation": 1
          }
        },
        {
          "timestamp": "2025-06-26T14:27:59.664526",
          "success": true,
          "phi_state": {
            "complexity": 0.5911156031163314,
            "resonance": 0.9937795081373617,
            "generation": 1
          }
        },
        {
          "timestamp": "2025-06-26T17:19:49.345131",
          "success": true,
          "phi_state": {
            "complexity": 0.5911156031163314,
            "resonance": 0.9937795081373617,
            "generation": 1
          }
        },
        {
          "timestamp": "2025-06-26T17:26:55.281447",
          "success": true,
          "phi_state": {
            "complexity": 0.5911156031163314,
            "resonance": 0.9937795081373617,
            "generation": 1
          }
        },
        {
          "timestamp": "2025-06-26T17:27:30.599829",
          "success": true,
          "phi_state": {
            "complexity": 0.5911156031163314,
            "resonance": 0.9937795081373617,
            "generation": 1
          }
        },
        {
          "timestamp": "2025-06-26T17:28:46.761511",
          "success": true,
          "phi_state": {
            "complexity": 0.5911156031163314,
            "resonance": 0.9937795081373617,
            "generation": 1
          }
        },
        {
          "timestamp": "2025-06-26T17:28:54.323586",
          "success": true,
          "phi_state": {
            "complexity": 0.5911156031163314,
            "resonance": 0.9937795081373617,
            "generation": 1
          }
        },
        {
          "timestamp": "2025-06-26T17:29:01.990810",
          "success": true,
          "phi_state": {
            "complexity": 0.5911156031163314,
            "resonance": 0.9937795081373617,
            "generation": 1
          }
        },
        {
          "timestamp": "2025-06-26T17:29:10.152896",
          "success": true,
          "phi_state": {
            "complexity": 0.5911156031163314,
            "resonance": 0.9937795081373617,
            "generation": 1
          }
        },
        {
          "timestamp": "2025-06-26T17:29:17.586060",
          "success": true,
          "phi_state": {
            "complexity": 0.5911156031163314,
            "resonance": 0.9937795081373617,
            "generation": 1
          }
        },
        {
          "timestamp": "2025-06-26T17:36:37.581644",
          "success": true,
          "phi_state": {
            "complexity": 0.7,
            "resonance": 0.9916056032054714,
            "generation": 2
          }
        },
        {
          "timestamp": "2025-06-26T17:41:14.145717",
          "success": true,
          "phi_state": {
            "complexity": 0.7,
            "resonance": 0.9916056032054714,
            "generation": 2
          }
        }
      ],
      "phi_state": {
        "complexity": 0.7,
        "resonance": 0.9916056032054714,
        "generation": 2
      }
    },
    {
      "group_id": "0ab4bdc9-41db-40b1-8b8a-7c998df3bd33",
      "group_type": "process",
      "codons": [
        {
          "codon_id": "6a8b9dc4-88c2-459a-b362-6b87188250f8",
          "codon_type": "data_processing",
          "frame_data": {
            "task_type": "execute_python",
            "task_data": {
              "code": "def data_processing_codon():\n    \"\"\"\n    Process data using phi-harmonic principles.\n    Generates test data based on Fibonacci sequence and golden ratio.\n    \"\"\"\n    print(\"\ud83d\udd04 Processing data with phi-harmonic principles\")\n    \n    # Generate Fibonacci sequence\n    def fibonacci(n):\n        sequence = [0, 1]\n        for i in range(2, n):\n            sequence.append(sequence[i-1] + sequence[i-2])\n        return sequence\n    \n    # Generate data\n    fib_sequence = fibonacci(20)\n    phi_approximations = [fib_sequence[i+1] / fib_sequence[i] for i in range(1, 19)]\n    \n    # Calculate phi-harmonic resonance for each approximation\n    resonance_values = [1.0 / (1.0 + abs((x - PHI) / PHI)) for x in phi_approximations]\n    \n    # Store results\n    GENOME_DATA[\"fibonacci_sequence\"] = fib_sequence\n    GENOME_DATA[\"phi_approximations\"] = phi_approximations\n    GENOME_DATA[\"approximation_resonance\"] = resonance_values\n    \n    # Calculate current phi-harmonic timing\n    phi_time = time.time() * PHI % 1.0\n    GENOME_DATA[\"phi_values\"].append(phi_time)\n    \n    # Calculate overall resonance\n    avg_resonance = sum(resonance_values) / len(resonance_values)\n    current_resonance = avg_resonance * (1.0 / (1.0 + abs(phi_time - 0.5)))\n    GENOME_DATA[\"resonance_scores\"].append(current_resonance)\n    \n    print(f\"\u2705 Processed {len(fib_sequence)} Fibonacci numbers\")\n    print(f\"\u2705 Average phi approximation: {sum(phi_approximations) / len(phi_approximations):.6f}\")\n    print(f\"\u2705 Phi-time: {phi_time:.6f}, Resonance: {current_resonance:.6f}\")\n    \n    return True\n"
            }
          },
          "creation_time": "2025-06-26T13:52:51.115575",
          "execution_count": 17,
          "success_count": 14,
          "resonance": 0.8565300067199951,
          "phi_state": {
            "complexity": 0.7314246287465143,
            "resonance": 0.8944271909999159,
            "generation": 3
          }
        },
        {
          "codon_id": "77ef04aa-cfdb-4093-9bf3-db15f71098c3",
          "codon_type": "calculation",
          "frame_data": {
            "task_type": "execute_python",
            "task_data": {
              "code": "def calculation_codon():\n    \"\"\"\n    Perform phi-harmonic calculations.\n    Calculates resonance patterns and quantum-inspired metrics.\n    \"\"\"\n    print(\"\ud83e\uddee Performing phi-harmonic calculations\")\n    \n    # Get data from previous codons\n    phi_approx = GENOME_DATA.get(\"phi_approximations\", [PHI] * 10)\n    resonance_values = GENOME_DATA.get(\"approximation_resonance\", [0.5] * 10)\n    \n    # Calculate quantum-inspired metrics\n    quantum_states = []\n    for i, phi in enumerate(phi_approx):\n        # Calculate quantum state vector\n        theta = phi * math.pi % (2 * math.pi)\n        amplitude = resonance_values[i]\n        \n        # Quantum state as (amplitude, phase)\n        quantum_state = (amplitude, theta)\n        quantum_states.append(quantum_state)\n    \n    # Calculate interference pattern\n    interference = 0\n    for state in quantum_states:\n        amplitude, phase = state\n        interference += amplitude * math.cos(phase)\n    \n    # Normalize interference\n    interference = interference / len(quantum_states)\n    \n    # Calculate phi-harmonic resonance\n    phi_time = time.time() * PHI % 1.0\n    resonance = abs(interference) * (1.0 / (1.0 + abs(phi_time - 0.5)))\n    \n    # Store results\n    GENOME_DATA[\"quantum_states\"] = quantum_states\n    GENOME_DATA[\"interference\"] = interference\n    GENOME_DATA[\"phi_values\"].append(phi_time)\n    GENOME_DATA[\"resonance_scores\"].append(resonance)\n    \n    print(f\"\u2705 Calculated {len(quantum_states)} quantum states\")\n    print(f\"\u2705 Interference pattern: {interference:.6f}\")\n    print(f\"\u2705 Phi-time: {phi_time:.6f}, Resonance: {resonance:.6f}\")\n    \n    return True\n"
            }
          },
          "creation_time": "2025-06-26T13:52:51.115585",
          "execution_count": 17,
          "success_count": 14,
          "resonance": 0.8565300067199951,
          "phi_state": {
            "complexity": 0.7530368949844273,
            "resonance": 0.8944271909999159,
            "generation": 3
          }
        }
      ],
      "creation_time": "2025-06-26T13:52:51.115565",
      "execution_history": [
        {
          "timestamp": "2025-06-26T13:53:08.562868",
          "success": false,
          "phi_state": {
            "complexity": 0.5,
            "resonance": 1.0,
            "generation": 1
          }
        },
        {
          "timestamp": "2025-06-26T13:56:06.309218",
          "success": false,
          "phi_state": {
            "complexity": 0.5,
            "resonance": 1.0,
            "generation": 1
          }
        },
        {
          "timestamp": "2025-06-26T13:57:18.531490",
          "success": false,
          "phi_state": {
            "complexity": 0.5,
            "resonance": 1.0,
            "generation": 1
          }
        },
        {
          "timestamp": "2025-06-26T13:59:59.580245",
          "success": true,
          "phi_state": {
            "complexity": 0.5,
            "resonance": 1.0,
            "generation": 1
          }
        },
        {
          "timestamp": "2025-06-26T14:26:15.279832",
          "success": true,
          "phi_state": {
            "complexity": 0.5,
            "resonance": 1.0,
            "generation": 1
          }
        },
        {
          "timestamp": "2025-06-26T14:27:13.016657",
          "success": true,
          "phi_state": {
            "complexity": 0.5,
            "resonance": 1.0,
            "generation": 1
          }
        },
        {
          "timestamp": "2025-06-26T14:27:59.733505",
          "success": true,
          "phi_state": {
            "complexity": 0.5911156031163314,
            "resonance": 0.9937795081373617,
            "generation": 1
          }
        },
        {
          "timestamp": "2025-06-26T17:19:49.412057",
          "success": true,
          "phi_state": {
            "complexity": 0.5911156031163314,
            "resonance": 0.9937795081373617,
            "generation": 1
          }
        },
        {
          "timestamp": "2025-06-26T17:26:55.345745",
          "success": true,
          "phi_state": {
            "complexity": 0.5911156031163314,
            "resonance": 0.9937795081373617,
            "generation": 1
          }
        },
        {
          "timestamp": "2025-06-26T17:27:30.668017",
          "success": true,
          "phi_state": {
            "complexity": 0.5911156031163314,
            "resonance": 0.9937795081373617,
            "generation": 1
          }
        },
        {
          "timestamp": "2025-06-26T17:28:46.827079",
          "success": true,
          "phi_state": {
            "complexity": 0.5911156031163314,
            "resonance": 0.9937795081373617,
            "generation": 1
          }
        },
        {
          "timestamp": "2025-06-26T17:28:54.389310",
          "success": true,
          "phi_state": {
            "complexity": 0.5911156031163314,
            "resonance": 0.9937795081373617,
            "generation": 1
          }
        },
        {
          "timestamp": "2025-06-26T17:29:02.106673",
          "success": true,
          "phi_state": {
            "complexity": 0.5911156031163314,
            "resonance": 0.9937795081373617,
            "generation": 1
          }
        },
        {
          "timestamp": "2025-06-26T17:29:10.220179",
          "success": true,
          "phi_state": {
            "complexity": 0.5911156031163314,
            "resonance": 0.9937795081373617,
            "generation": 1
          }
        },
        {
          "timestamp": "2025-06-26T17:29:17.654323",
          "success": true,
          "phi_state": {
            "complexity": 0.5911156031163314,
            "resonance": 0.9937795081373617,
            "generation": 1
          }
        },
        {
          "timestamp": "2025-06-26T17:36:37.653537",
          "success": true,
          "phi_state": {
            "complexity": 0.7,
            "resonance": 0.9916056032054714,
            "generation": 2
          }
        },
        {
          "timestamp": "2025-06-26T17:41:14.304365",
          "success": true,
          "phi_state": {
            "complexity": 0.7,
            "resonance": 0.9916056032054714,
            "generation": 2
          }
        }
      ],
      "phi_state": {
        "complexity": 0.7,
        "resonance": 0.9916056032054714,
        "generation": 2
      }
    },
    {
      "group_id": "39821bb7-f270-4f0e-ad86-925a206a1025",
      "group_type": "evolve",
      "codons": [
        {
          "codon_id": "1c42368a-8816-4b8e-96c6-67260093fac1",
          "codon_type": "mutate",
          "frame_data": {
            "task_type": "execute_python",
            "task_data": {
              "code": "def mutate_codon():\n    \"\"\"\n    Apply phi-harmonic mutations to the genome data.\n    Simulates evolution of the genome based on resonance patterns.\n    \"\"\"\n    print(\"\ud83e\uddec Applying phi-harmonic mutations\")\n    \n    # Get resonance scores\n    resonance_scores = GENOME_DATA.get(\"resonance_scores\", [0.5, 0.6, 0.7])\n    \n    # Calculate mutation probability based on resonance\n    avg_resonance = sum(resonance_scores) / len(resonance_scores)\n    mutation_prob = 1.0 - avg_resonance  # Lower resonance = higher mutation\n    \n    # Generate mutation vectors\n    mutation_vectors = []\n    for i in range(5):\n        # Calculate phi-harmonic direction\n        phi_angle = (i * PHI) % 1.0 * 2 * math.pi\n        \n        # Create mutation vector (direction, magnitude)\n        vector = (\n            math.cos(phi_angle),  # x component\n            math.sin(phi_angle),  # y component\n            mutation_prob * (0.5 + 0.5 * math.sin(phi_angle))  # magnitude\n        )\n        mutation_vectors.append(vector)\n    \n    # Calculate phi-harmonic timing\n    phi_time = time.time() * PHI % 1.0\n    \n    # Store results\n    GENOME_DATA[\"mutation_probability\"] = mutation_prob\n    GENOME_DATA[\"mutation_vectors\"] = mutation_vectors\n    GENOME_DATA[\"phi_values\"].append(phi_time)\n    \n    # Calculate resonance\n    resonance = (1.0 - mutation_prob) * (1.0 / (1.0 + abs(phi_time - 0.5)))\n    GENOME_DATA[\"resonance_scores\"].append(resonance)\n    \n    print(f\"\u2705 Mutation probability: {mutation_prob:.6f}\")\n    print(f\"\u2705 Generated {len(mutation_vectors)} mutation vectors\")\n    print(f\"\u2705 Phi-time: {phi_time:.6f}, Resonance: {resonance:.6f}\")\n    \n    return True\n"
            }
          },
          "creation_time": "2025-06-26T13:52:51.115671",
          "execution_count": 17,
          "success_count": 14,
          "resonance": 0.8565300067199951,
          "phi_state": {
            "complexity": 0.7351610372914618,
            "resonance": 0.8944271909999159,
            "generation": 3
          }
        },
        {
          "codon_id": "2341e4aa-4e5d-4c45-b8d8-a71023e92d75",
          "codon_type": "select",
          "frame_data": {
            "task_type": "execute_python",
            "task_data": {
              "code": "def select_codon():\n    \"\"\"\n    Select optimal phi-harmonic states based on resonance.\n    Simulates natural selection in the genome evolution.\n    \"\"\"\n    print(\"\ud83d\udd0d Selecting optimal phi-harmonic states\")\n    \n    # Get resonance scores and phi values\n    resonance_scores = GENOME_DATA.get(\"resonance_scores\", [0.5, 0.6, 0.7])\n    phi_values = GENOME_DATA.get(\"phi_values\", [0.3, 0.4, 0.5])\n    \n    # Pair phi values with resonance scores\n    phi_resonance_pairs = list(zip(phi_values, resonance_scores))\n    \n    # Sort by resonance (highest first)\n    sorted_pairs = sorted(phi_resonance_pairs, key=lambda x: x[1], reverse=True)\n    \n    # Select top 3 phi states\n    top_states = sorted_pairs[:min(3, len(sorted_pairs))]\n    \n    # Calculate average of top phi states\n    optimal_phi = sum(state[0] for state in top_states) / len(top_states)\n    \n    # Calculate phi-harmonic timing\n    phi_time = time.time() * PHI % 1.0\n    \n    # Store results\n    GENOME_DATA[\"optimal_phi_states\"] = top_states\n    GENOME_DATA[\"optimal_phi\"] = optimal_phi\n    GENOME_DATA[\"phi_values\"].append(phi_time)\n    \n    # Calculate selection pressure (how much better top states are)\n    if len(resonance_scores) > 0:\n        avg_resonance = sum(resonance_scores) / len(resonance_scores)\n        top_resonance = sum(state[1] for state in top_states) / len(top_states)\n        selection_pressure = top_resonance / avg_resonance if avg_resonance > 0 else 1.0\n    else:\n        selection_pressure = 1.0\n    \n    GENOME_DATA[\"selection_pressure\"] = selection_pressure\n    \n    # Calculate resonance\n    resonance = selection_pressure * (1.0 / (1.0 + abs(phi_time - 0.5)))\n    GENOME_DATA[\"resonance_scores\"].append(resonance)\n    \n    print(f\"\u2705 Selected {len(top_states)} optimal phi states\")\n    print(f\"\u2705 Optimal phi value: {optimal_phi:.6f}\")\n    print(f\"\u2705 Selection pressure: {selection_pressure:.6f}\")\n    print(f\"\u2705 Phi-time: {phi_time:.6f}, Resonance: {resonance:.6f}\")\n    \n    return True\n"
            }
          },
          "creation_time": "2025-06-26T13:52:51.115681",
          "execution_count": 17,
          "success_count": 14,
          "resonance": 0.8565300067199951,
          "phi_state": {
            "complexity": 0.7342014014286546,
            "resonance": 0.8944271909999159,
            "generation": 3
          }
        }
      ],
      "creation_time": "2025-06-26T13:52:51.115650",
      "execution_history": [
        {
          "timestamp": "2025-06-26T13:53:08.564180",
          "success": false,
          "phi_state": {
            "complexity": 0.5,
            "resonance": 1.0,
            "generation": 1
          }
        },
        {
          "timestamp": "2025-06-26T13:56:06.310670",
          "success": false,
          "phi_state": {
            "complexity": 0.5,
            "resonance": 1.0,
            "generation": 1
          }
        },
        {
          "timestamp": "2025-06-26T13:57:18.533028",
          "success": false,
          "phi_state": {
            "complexity": 0.5,
            "resonance": 1.0,
            "generation": 1
          }
        },
        {
          "timestamp": "2025-06-26T13:59:59.679067",
          "success": true,
          "phi_state": {
            "complexity": 0.5,
            "resonance": 1.0,
            "generation": 1
          }
        },
        {
          "timestamp": "2025-06-26T14:26:15.365667",
          "success": true,
          "phi_state": {
            "complexity": 0.5,
            "resonance": 1.0,
            "generation": 1
          }
        },
        {
          "timestamp": "2025-06-26T14:27:13.086110",
          "success": true,
          "phi_state": {
            "complexity": 0.5,
            "resonance": 1.0,
            "generation": 1
          }
        },
        {
          "timestamp": "2025-06-26T14:27:59.814472",
          "success": true,
          "phi_state": {
            "complexity": 0.5911156031163314,
            "resonance": 0.9937795081373617,
            "generation": 1
          }
        },
        {
          "timestamp": "2025-06-26T17:19:49.481381",
          "success": true,
          "phi_state": {
            "complexity": 0.5911156031163314,
            "resonance": 0.9937795081373617,
            "generation": 1
          }
        },
        {
          "timestamp": "2025-06-26T17:26:55.409799",
          "success": true,
          "phi_state": {
            "complexity": 0.5911156031163314,
            "resonance": 0.9937795081373617,
            "generation": 1
          }
        },
        {
          "timestamp": "2025-06-26T17:27:30.738335",
          "success": true,
          "phi_state": {
            "complexity": 0.5911156031163314,
            "resonance": 0.9937795081373617,
            "generation": 1
          }
        },
        {
          "timestamp": "2025-06-26T17:28:46.894050",
          "success": true,
          "phi_state": {
            "complexity": 0.5911156031163314,
            "resonance": 0.9937795081373617,
            "generation": 1
          }
        },
        {
          "timestamp": "2025-06-26T17:28:54.455130",
          "success": true,
          "phi_state": {
            "complexity": 0.5911156031163314,
            "resonance": 0.9937795081373617,
            "generation": 1
          }
        },
        {
          "timestamp": "2025-06-26T17:29:02.217658",
          "success": true,
          "phi_state": {
            "complexity": 0.5911156031163314,
            "resonance": 0.9937795081373617,
            "generation": 1
          }
        },
        {
          "timestamp": "2025-06-26T17:29:10.287795",
          "success": true,
          "phi_state": {
            "complexity": 0.5911156031163314,
            "resonance": 0.9937795081373617,
            "generation": 1
          }
        },
        {
          "timestamp": "2025-06-26T17:29:17.722432",
          "success": true,
          "phi_state": {
            "complexity": 0.5911156031163314,
            "resonance": 0.9937795081373617,
            "generation": 1
          }
        },
        {
          "timestamp": "2025-06-26T17:36:37.725981",
          "success": true,
          "phi_state": {
            "complexity": 0.7,
            "resonance": 0.9916056032054714,
            "generation": 2
          }
        },
        {
          "timestamp": "2025-06-26T17:41:14.447066",
          "success": true,
          "phi_state": {
            "complexity": 0.7,
            "resonance": 0.9916056032054714,
            "generation": 2
          }
        }
      ],
      "phi_state": {
        "complexity": 0.7,
        "resonance": 0.9916056032054714,
        "generation": 2
      }
    },
    {
      "group_id": "ef0a5f6b-4b5a-4226-bb22-83e6d639e857",
      "group_type": "respond",
      "codons": [
        {
          "codon_id": "10124b6b-9b4e-4681-82bf-ee93aabce77e",
          "codon_type": "generate_output",
          "frame_data": {
            "task_type": "execute_python",
            "task_data": {
              "code": "def generate_output_codon():\n    \"\"\"\n    Generate output data from the genome execution.\n    Creates a summary of the execution results.\n    \"\"\"\n    print(\"\ud83d\udcca Generating output from genome execution\")\n    \n    # Calculate execution time\n    start_time = GENOME_DATA.get(\"start_time\", time.time() - 1)\n    execution_time = time.time() - start_time\n    \n    # Get resonance scores\n    resonance_scores = GENOME_DATA.get(\"resonance_scores\", [])\n    avg_resonance = sum(resonance_scores) / len(resonance_scores) if resonance_scores else 0\n    \n    # Get phi values\n    phi_values = GENOME_DATA.get(\"phi_values\", [])\n    optimal_phi = GENOME_DATA.get(\"optimal_phi\", 0)\n    \n    # Create output summary\n    output = {\n        \"timestamp\": datetime.now().isoformat(),\n        \"execution_time\": execution_time,\n        \"resonance_scores\": resonance_scores,\n        \"average_resonance\": avg_resonance,\n        \"phi_values\": phi_values,\n        \"optimal_phi\": optimal_phi,\n        \"mutation_probability\": GENOME_DATA.get(\"mutation_probability\", 0),\n        \"selection_pressure\": GENOME_DATA.get(\"selection_pressure\", 1),\n    }\n    \n    # Calculate phi-harmonic timing\n    phi_time = time.time() * PHI % 1.0\n    \n    # Store results\n    GENOME_DATA[\"output_data\"] = output\n    GENOME_DATA[\"phi_values\"].append(phi_time)\n    \n    # Calculate resonance\n    resonance = avg_resonance * (1.0 / (1.0 + abs(phi_time - 0.5)))\n    GENOME_DATA[\"resonance_scores\"].append(resonance)\n    \n    # Try to save output to file\n    try:\n        output_dir = \"qr_genome_output\"\n        os.makedirs(output_dir, exist_ok=True)\n        output_file = os.path.join(output_dir, f\"genome_output_{int(time.time())}.json\")\n        \n        with open(output_file, \"w\") as f:\n            json.dump(output, f, indent=2)\n        \n        print(f\"\u2705 Output saved to {output_file}\")\n    except Exception as e:\n        print(f\"\u26a0\ufe0f Could not save output to file: {e}\")\n    \n    print(f\"\u2705 Execution time: {execution_time:.6f} seconds\")\n    print(f\"\u2705 Average resonance: {avg_resonance:.6f}\")\n    print(f\"\u2705 Phi-time: {phi_time:.6f}, Final resonance: {resonance:.6f}\")\n    \n    return True\n"
            }
          },
          "creation_time": "2025-06-26T13:52:51.115705",
          "execution_count": 17,
          "success_count": 14,
          "resonance": 0.8565300067199951,
          "phi_state": {
            "complexity": 0.7389273881328192,
            "resonance": 0.8944271909999159,
            "generation": 3
          }
        },
        {
          "codon_id": "aeddb61c-69f9-4c8d-9128-060b0dac79e6",
          "codon_type": "visualize",
          "frame_data": {
            "task_type": "execute_python",
            "task_data": {
              "code": "def visualize_codon():\n    \"\"\"\n    Visualize the genome execution results.\n    Creates a simple text-based visualization of resonance patterns.\n    \"\"\"\n    print(\"\ud83d\udcc8 Visualizing genome execution results\")\n    \n    # Get resonance scores and phi values\n    resonance_scores = GENOME_DATA.get(\"resonance_scores\", [])\n    phi_values = GENOME_DATA.get(\"phi_values\", [])\n    \n    if not resonance_scores or not phi_values:\n        print(\"\u26a0\ufe0f No data available for visualization\")\n        return False\n    \n    # Create simple ASCII visualization\n    print(\"\\n\" + \"=\"*60)\n    print(\"PHI-HARMONIC RESONANCE PATTERN\")\n    print(\"=\"*60)\n    \n    # Normalize values for display\n    max_resonance = max(resonance_scores) if resonance_scores else 1\n    normalized_resonance = [r/max_resonance for r in resonance_scores]\n    \n    # Display resonance pattern\n    for i, (phi, res, norm_res) in enumerate(zip(phi_values, resonance_scores, normalized_resonance)):\n        bar_length = int(norm_res * 40)\n        bar = \"\u2588\" * bar_length\n        print(f\"Step {i+1:2d} | Phi: {phi:.6f} | Res: {res:.6f} | {bar}\")\n    \n    print(\"=\"*60)\n    \n    # Calculate phi-harmonic timing\n    phi_time = time.time() * PHI % 1.0\n    \n    # Store visualization data\n    GENOME_DATA[\"visualization_data\"] = {\n        \"resonance_pattern\": list(zip(phi_values, resonance_scores)),\n        \"phi_time\": phi_time\n    }\n    \n    # Calculate final resonance\n    if resonance_scores:\n        final_resonance = resonance_scores[-1] * (1.0 / (1.0 + abs(phi_time - 0.5)))\n    else:\n        final_resonance = 0.5\n    \n    print(f\"\u2705 Visualized {len(resonance_scores)} resonance points\")\n    print(f\"\u2705 Phi-time: {phi_time:.6f}, Final resonance: {final_resonance:.6f}\")\n    \n    return True\n"
            }
          },
          "creation_time": "2025-06-26T13:52:51.115713",
          "execution_count": 17,
          "success_count": 14,
          "resonance": 0.8565300067199951,
          "phi_state": {
            "complexity": 0.7533007746773551,
            "resonance": 0.8944271909999159,
            "generation": 3
          }
        }
      ],
      "creation_time": "2025-06-26T13:52:51.115696",
      "execution_history": [
        {
          "timestamp": "2025-06-26T13:53:08.565557",
          "success": false,
          "phi_state": {
            "complexity": 0.5,
            "resonance": 1.0,
            "generation": 1
          }
        },
        {
          "timestamp": "2025-06-26T13:56:06.312645",
          "success": false,
          "phi_state": {
            "complexity": 0.5,
            "resonance": 1.0,
            "generation": 1
          }
        },
        {
          "timestamp": "2025-06-26T13:57:18.536178",
          "success": false,
          "phi_state": {
            "complexity": 0.5,
            "resonance": 1.0,
            "generation": 1
          }
        },
        {
          "timestamp": "2025-06-26T13:59:59.761341",
          "success": true,
          "phi_state": {
            "complexity": 0.5,
            "resonance": 1.0,
            "generation": 1
          }
        },
        {
          "timestamp": "2025-06-26T14:26:15.436331",
          "success": true,
          "phi_state": {
            "complexity": 0.5,
            "resonance": 1.0,
            "generation": 1
          }
        },
        {
          "timestamp": "2025-06-26T14:27:13.179240",
          "success": true,
          "phi_state": {
            "complexity": 0.5,
            "resonance": 1.0,
            "generation": 1
          }
        },
        {
          "timestamp": "2025-06-26T14:27:59.892928",
          "success": true,
          "phi_state": {
            "complexity": 0.5911156031163314,
            "resonance": 0.9937795081373617,
            "generation": 1
          }
        },
        {
          "timestamp": "2025-06-26T17:19:49.550804",
          "success": true,
          "phi_state": {
            "complexity": 0.5911156031163314,
            "resonance": 0.9937795081373617,
            "generation": 1
          }
        },
        {
          "timestamp": "2025-06-26T17:26:55.474224",
          "success": true,
          "phi_state": {
            "complexity": 0.5911156031163314,
            "resonance": 0.9937795081373617,
            "generation": 1
          }
        },
        {
          "timestamp": "2025-06-26T17:27:30.807027",
          "success": true,
          "phi_state": {
            "complexity": 0.5911156031163314,
            "resonance": 0.9937795081373617,
            "generation": 1
          }
        },
        {
          "timestamp": "2025-06-26T17:28:46.961680",
          "success": true,
          "phi_state": {
            "complexity": 0.5911156031163314,
            "resonance": 0.9937795081373617,
            "generation": 1
          }
        },
        {
          "timestamp": "2025-06-26T17:28:54.520722",
          "success": true,
          "phi_state": {
            "complexity": 0.5911156031163314,
            "resonance": 0.9937795081373617,
            "generation": 1
          }
        },
        {
          "timestamp": "2025-06-26T17:29:02.327377",
          "success": true,
          "phi_state": {
            "complexity": 0.5911156031163314,
            "resonance": 0.9937795081373617,
            "generation": 1
          }
        },
        {
          "timestamp": "2025-06-26T17:29:10.356104",
          "success": true,
          "phi_state": {
            "complexity": 0.5911156031163314,
            "resonance": 0.9937795081373617,
            "generation": 1
          }
        },
        {
          "timestamp": "2025-06-26T17:29:17.789481",
          "success": true,
          "phi_state": {
            "complexity": 0.5911156031163314,
            "resonance": 0.9937795081373617,
            "generation": 1
          }
        },
        {
          "timestamp": "2025-06-26T17:36:37.807240",
          "success": true,
          "phi_state": {
            "complexity": 0.7,
            "resonance": 0.9916056032054714,
            "generation": 2
          }
        },
        {
          "timestamp": "2025-06-26T17:41:14.601322",
          "success": true,
          "phi_state": {
            "complexity": 0.7,
            "resonance": 0.9916056032054714,
            "generation": 2
          }
        }
      ],
      "phi_state": {
        "complexity": 0.7,
        "resonance": 0.9916056032054714,
        "generation": 2
      }
    }
  ],
  "creation_time": "2025-06-26T13:52:51.115444",
  "generation": 3,
  "mutation_rate": 0.05,
  "phi_state": {
    "complexity": 0.8,
    "resonance": 0.7802668171276792,
    "generation": 3
  }
}
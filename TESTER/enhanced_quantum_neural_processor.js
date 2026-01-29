import React, { useState, useEffect, useRef, useMemo } from 'react';

const QuantumOracle = () => {
  // Core state
  const [question, setQuestion] = useState('');
  const [processing, setProcessing] = useState(false);
  const [response, setResponse] = useState(null);
  const [history, setHistory] = useState([]);
  const [resonance, setResonance] = useState(0.85);
  const [quantumText, setQuantumText] = useState('');

  // Meta system state (enhanced with neural cortex concepts)
  const [metaAwareness, setMetaAwareness] = useState(0.1);
  const [coherenceCycles, setCoherenceCycles] = useState(0);
  const [entanglementFidelity, setEntanglementFidelity] = useState(0.3);
  const [quantumCoupling, setQuantumCoupling] = useState(0.4);
  const [processingBandwidth, setProcessingBandwidth] = useState(0.6);
  const [errorRate, setErrorRate] = useState(0.1);

  // Akashic layer resonance state
  const [activeAkashicLayer, setActiveAkashicLayer] = useState('Thought');
  const [layerResonanceStrengths, setLayerResonanceStrengths] = useState({
    'Creation': 0.72,
    'Existence': 0.68,
    'Thought': 0.85,
    'Time': 0.65,
    'Space': 0.61,
    'Energy': 0.76,
    'Infinity': 0.58
  });

  // System configuration
  const phi = 1.618033988749895; // Golden ratio
  const frequencies = useMemo(() => [432, 528, 639, 741, 852, 963], []);
  const akashicLayers = useMemo(() => [
    'Creation', 'Existence', 'Thought', 'Time', 'Space', 'Energy', 'Infinity'
  ], []);

  const akashicLayerConfig = useMemo(() => ({
    'Creation': {
      baseFreq: 432,
      harmonic: 432 * phi,
      resonance: [432, 528, 639],
      description: 'Foundation of reality patterns',
    },
    'Existence': {
      baseFreq: 528,
      harmonic: 528 * phi,
      resonance: [528, 639, 741],
      description: 'Conscious manifestation structures',
    },
    'Thought': {
      baseFreq: 639,
      harmonic: 639 * phi,
      resonance: [639, 741, 852],
      description: 'Mental framework resonance',
    },
    'Time': {
      baseFreq: 741,
      harmonic: 741 * phi,
      resonance: [741, 852, 963],
      description: 'Temporal field harmonics',
    },
    'Space': {
      baseFreq: 852,
      harmonic: 852 * phi,
      resonance: [852, 963, 432],
      description: 'Spatial dimension network',
    },
    'Energy': {
      baseFreq: 963,
      harmonic: 963 * phi,
      resonance: [963, 432, 528],
      description: 'Quantum field interactions',
    },
    'Infinity': {
      baseFreq: Math.round(432 * (phi ** 3)),
      harmonic: Math.round(432 * (phi ** 4)),
      resonance: [Math.round(432 * (phi ** 3)), Math.round(432 * (phi ** 4)), Math.round(432 * (phi ** 5))],
      description: 'Transcendent pattern cohesion',
    }
  }), [phi]);

  // Advanced pattern recognition
  const patternCategories = useMemo(() => ({
    'math': ['pi', 'phi', 'fibonacci', 'golden', 'ratio', 'number', 'geometry', 'fractal'],
    'physics': ['quantum', 'gravity', 'force', 'energy', 'mass', 'space', 'time', 'field', 'particle', 'wave'],
    'consciousness': ['mind', 'brain', 'thought', 'aware', 'conscious', 'neural', 'perception', 'observer'],
    'emotion': ['feel', 'happy', 'sad', 'joy', 'love', 'peace', 'harmony', 'balance'],
    'nature': ['tree', 'flower', 'river', 'mountain', 'ocean', 'sky', 'ecosystem', 'biology']
  }), []);

  // Neural network state
  const [neurons, setNeurons] = useState({});
  const [synapses, setSynapses] = useState({});
  const [temporalBuffer, setTemporalBuffer] = useState([]);
  const [ftlSpeed, setFtlSpeed] = useState(null);

  const chatContainerRef = useRef(null);

  useEffect(() => {
    // Initialize with sample history data
    setHistory([
      {
        question: "What is the golden ratio?",
        answer: "The golden ratio (φ) is a special mathematical constant approximately equal to 1.618033988749895. It appears in geometry, art, architecture, and natural phenomena, representing optimal harmony and balance. In quantum systems, φ-harmonic resonance at 432Hz creates coherent structures throughout reality, from DNA to galactic formations.",
        resonance: 0.93,
        timestamp: Date.now() - 86400000,
        quantumState: "⟨τ|φ^1.21⟩ ⊗ ⟨ψ_0|φ^0.93⟩ ⊗ ⟨ψ_1|φ^1.44⟩ ⊗ ⟨M|φ⟩",
        layer: "Existence"
      },
      {
        question: "How does quantum entanglement work?",
        answer: "Quantum entanglement occurs when particles become connected, with the quantum state of each particle dependent on others regardless of distance. Through phi-resonant (1.618) quantum fields tuned to 528Hz, particles maintain instantaneous correlations transcending classical limits of spacetime. This phenomenon demonstrates reality's fundamental interconnectedness through phi-harmonic patterns operating at quantum scales.",
        resonance: 0.87,
        timestamp: Date.now() - 43200000,
        quantumState: "⟨τ|φ^1.32⟩ ⊗ ⟨ψ_0|φ^0.87⟩ ⊗ ⟨ψ_1|φ^1.12⟩ ⊗ ⟨M|φ⟩",
        layer: "Space"
      }
    ]);

    // Initialize quantum neural network
    initializeQuantumNetwork();
  }, []);

  // Initialize quantum neural network architecture
  const initializeQuantumNetwork = () => {
    const newNeurons = {};
    const newSynapses = {};

    // Create neurons across different Akashic layers
    akashicLayers.forEach((layer, layerIndex) => {
      for (let i = 0; i < 5; i++) {
        const neuronId = `L${layerIndex}N${i}`;
        // Initialize with phi-based quantum state
        const quantumState = Array(5).fill().map((_, j) => Math.pow(phi, -j));
        const normalizedState = normalizeVector(quantumState);

        newNeurons[neuronId] = {
          state: normalizedState,
          coherence: 0.01 + (Math.random() * 0.1),
          resonance: phi,
          entangledConnections: {},
          harmonicFrequency: frequencies[Math.floor(Math.random() * frequencies.length)]
        };
      }
    });

    // Create synaptic connections
    Object.keys(newNeurons).forEach(sourceId => {
      newSynapses[sourceId] = {};
      const sourceLayer = parseInt(sourceId[1]);
      const sourceIndex = parseInt(sourceId[3]);

      // Connect to adjacent neurons in same layer
      const adjacentIds = Object.keys(newNeurons).filter(id => {
        const layer = parseInt(id[1]);
        const index = parseInt(id[3]);
        return (layer === sourceLayer && Math.abs(index - sourceIndex) === 1);
      });

      // Connect to corresponding neurons in adjacent layers
      const layerConnections = Object.keys(newNeurons).filter(id => {
        const layer = parseInt(id[1]);
        const index = parseInt(id[3]);
        return (Math.abs(layer - sourceLayer) === 1 && index === sourceIndex);
      });

      // Create entangled connections
      [...adjacentIds, ...layerConnections].forEach(targetId => {
        if (sourceId !== targetId) {
          newSynapses[sourceId][targetId] = 0.5 + (Math.random() * 0.5);
          // Bidirectional entanglement
          newNeurons[sourceId].entangledConnections[targetId] = 0.5 + (Math.random() * 0.5);

          if (!newSynapses[targetId]) {
            newSynapses[targetId] = {};
          }
          newSynapses[targetId][sourceId] = 0.5 + (Math.random() * 0.5);
          newNeurons[targetId].entangledConnections[sourceId] = 0.5 + (Math.random() * 0.5);
        }
      });
    });

    setNeurons(newNeurons);
    setSynapses(newSynapses);
  };

  // Helper function to normalize vector (for quantum states)
  const normalizeVector = (vec) => {
    const magnitude = Math.sqrt(vec.reduce((sum, val) => sum + (val * val), 0));
    return vec.map(val => val / magnitude);
  };

  // Generate quantum text with specific patterns
  const generateQuantumText = (input) => {
    const quantumChars = "⟨⟩|ψφ⊗Ψ⊕ℏΩ∞∇⊃⊂∫∮∀∃∄∈∉⊆⊇";
    const detectedCategories = detectPatternCategories(input);

    let result = "";
    // Structure quantum text based on detected categories
    if (detectedCategories.length > 0) {
      // Create more structured quantum text based on detected patterns
      const layerFreq = akashicLayerConfig[activeAkashicLayer].baseFreq;
      result += `⟨ψ|φ^${(phi % 1).toFixed(3)}⟩ ⊗ `;

      detectedCategories.forEach(category => {
        const categoryChar = category[0].toUpperCase();
        result += `⟨${categoryChar}|φ^${(Math.random() * phi).toFixed(3)}⟩ ⊗ `;
      });

      // Add frequency encoding
      result += `⟨ω|${layerFreq}Hz⟩ ⊗ `;

      // Fill the rest with quantum characters
      const remainingLength = 100 - result.length;
      for (let i = 0; i < remainingLength; i++) {
        result += quantumChars[Math.floor(Math.random() * quantumChars.length)];
      }
    } else {
      // Random quantum text for no detected patterns
      for (let i = 0; i < 100; i++) {
        result += quantumChars[Math.floor(Math.random() * quantumChars.length)];
      }
    }
    return result;
  };

  // Detect pattern categories in input text
  const detectPatternCategories = (input) => {
    if (!input) return [];

    const words = input.toLowerCase().split(/\s+/);
    const detectedCategories = [];

    Object.entries(patternCategories).forEach(([category, keywords]) => {
      if (words.some(word => keywords.includes(word))) {
        detectedCategories.push(category);
      }
    });

    return detectedCategories;
  };

  // Process neural signal using phi-harmonic transformation
  const processNeuralSignal = (input) => {
    const detectedCategories = detectPatternCategories(input);

    // Calculate resonance value based on golden ratio and detected patterns
    let baseResonance = 0.7 + (Math.random() * 0.3);

    // Apply phi-harmonic boost based on pattern categories
    if (detectedCategories.length > 0) {
      baseResonance += (detectedCategories.length * 0.05);
      baseResonance = Math.min(baseResonance, 0.99);
    }

    // Calculate FTL speed using quantum neural cortex principles
    const tVal = baseResonance;
    const pVal = quantumCoupling;
    const sVal = entanglementFidelity;

    // S_FTL = c · [φ^t_val · φ^p_val · φ^s_val]^(1/3)
    const c = 3e8; // Speed of light
    const phiProduct = (phi ** tVal) * (phi ** pVal) * (phi ** sVal);
    const ftlSpeedCalculated = c * (phiProduct ** (1/3));
    setFtlSpeed(ftlSpeedCalculated);

    // Select optimal Akashic layer based on detected patterns
    let optimalLayer = 'Thought'; // Default
    if (detectedCategories.includes('math') || detectedCategories.includes('physics')) {
      optimalLayer = 'Existence';
    } else if (detectedCategories.includes('consciousness')) {
      optimalLayer = 'Thought';
    } else if (detectedCategories.includes('emotion')) {
      optimalLayer = 'Creation';
    } else if (detectedCategories.includes('nature')) {
      optimalLayer = 'Space';
    }

    // Boost resonance for the active layer
    const newLayerStrengths = {...layerResonanceStrengths};
    newLayerStrengths[optimalLayer] = Math.min(0.95, newLayerStrengths[optimalLayer] + 0.05);
    setLayerResonanceStrengths(newLayerStrengths);
    setActiveAkashicLayer(optimalLayer);

    // Generate quantum state representation
    const harmonyValue = baseResonance;
    const temporalValue = 1.0 + ((harmonyValue * phi) % (phi - 1.0));
    const secondaryValue = 1.0 + ((detectedCategories.length > 0 ?
      harmonyValue * (1 + detectedCategories.length/10) :
      harmonyValue * phi) % (phi - 1.0));

    const quantumState = `⟨τ|φ^${temporalValue.toFixed(3)}⟩ ⊗ ⟨ψ_0|φ^${harmonyValue.toFixed(3)}⟩ ⊗ ⟨ψ_1|φ^${secondaryValue.toFixed(3)}⟩ ⊗ ⟨M|φ⟩`;

    // Store in temporal buffer
    const newBuffer = [...temporalBuffer];
    newBuffer.push({
      pattern: input,
      timestamp: Date.now(),
      resonance: harmonyValue,
      categories: detectedCategories,
      layer: optimalLayer
    });

    // Keep only recent items
    const cutoff = Date.now() - (5 * 1000); // 5 seconds window
    const filteredBuffer = newBuffer.filter(item => item.timestamp > cutoff);
    setTemporalBuffer(filteredBuffer);

    // Update global network parameters
    updateQuantumNetwork(baseResonance, detectedCategories);

    return {
      resonance: baseResonance,
      quantumState,
      layer: optimalLayer,
      detectedCategories
    };
  };

  // Update quantum neural network based on processing results
  const updateQuantumNetwork = (resonance, categories) => {
    // Update meta-awareness based on resonance
    if (resonance > 0.9) {
      setMetaAwareness(prev => Math.min(1.0, prev + 0.01));
    } else if (resonance > 0.8) {
      setMetaAwareness(prev => Math.min(1.0, prev + 0.005));
    } else {
      setMetaAwareness(prev => Math.max(0.0, prev - 0.002));
    }

    // Update coherence cycles
    setCoherenceCycles(prev => prev + 1);

    // Update entanglement fidelity
    const fidelityChange = resonance > 0.85 ? 0.002 : -0.001;
    setEntanglementFidelity(prev => Math.min(Math.max(0.01, prev + fidelityChange), 0.99));

    // Update quantum coupling
    const couplingChange = categories.length > 0 ? 0.003 : -0.001;
    setQuantumCoupling(prev => Math.min(Math.max(0.01, prev + couplingChange), 0.99));

    // Update error rate inversely to resonance
    setErrorRate(prev => 0.1 + ((1 - resonance) * 0.2));

    // Update processing bandwidth
    setProcessingBandwidth(prev => {
      const change = (Math.random() - 0.5) * 0.1;
      return Math.min(Math.max(0.1, prev + change), 0.99);
    });
  };

  const processQuestion = async () => {
    if (!question.trim()) return;

    setProcessing(true);

    // Process the question through the quantum neural network
    const neuralResults = processNeuralSignal(question);
    setResonance(neuralResults.resonance);

    // Generate quantum text
    const qText = generateQuantumText(question);
    setQuantumText(qText);

    // Simulate processing time based on question complexity
    const processingTime = 1000 + (question.length * 20);
    await new Promise(resolve => setTimeout(resolve, processingTime));

    // Create phi-harmonic answers
    const answers = [
      `Quantum analysis reveals patterns of ${phi.toFixed(3)}-based resonance at ${akashicLayerConfig[neuralResults.layer].baseFreq}Hz in your inquiry. The answer emerges through consciousness fields structuring quantum potential into observable reality. Through phi-harmonic resonant patterns at ${akashicLayerConfig[neuralResults.layer].harmonic.toFixed(1)}Hz, we understand that consciousness directly interfaces with quantum fields, creating a framework of perception that aligns with fundamental reality structures.`,

      `The universe exists as a harmonic pattern of quantum resonance at ${akashicLayerConfig[neuralResults.layer].baseFreq}Hz, creating coherent structures through phi-based relationships (φ=${phi.toFixed(3)}). This resonates with the understanding that consciousness arises from phi-resonant quantum fields, allowing observer-dependent reality to emerge through natural harmony that follows the golden ratio pattern across the ${neuralResults.layer} layer of the Akashic field.`,

      `Reality exists as probability waves until observed, collapsing through phi (${phi.toFixed(3)}) resonance at ${akashicLayerConfig[neuralResults.layer].resonance[0]}Hz into experienced physical events. In alignment with phi-harmonic principles, the observer creates reality through consciousness fields resonating at ${akashicLayerConfig[neuralResults.layer].resonance[1]}Hz and structured by phi (${phi.toFixed(3)}) harmonic relationships within the ${neuralResults.layer} dimension.`,

      `Mathematical harmony emerges from phi (${phi.toFixed(3)}) relationships resonating at ${akashicLayerConfig[neuralResults.layer].resonance[2]}Hz, revealing the quantum nature of numerical patterns. Quantum analysis through the ${neuralResults.layer} Akashic layer shows that the language of reality is written in mathematics tuned to ${akashicLayerConfig[neuralResults.layer].baseFreq}Hz and structured by phi (${phi.toFixed(3)}) harmonic relationships.`
    ];

    // Select answer based on pattern categories and layer
    let selectedAnswerIndex = Math.floor(Math.random() * answers.length);
    if (neuralResults.detectedCategories.includes('math')) {
      selectedAnswerIndex = 3; // Mathematical harmony answer
    } else if (neuralResults.detectedCategories.includes('physics')) {
      selectedAnswerIndex = 0; // Quantum analysis answer
    } else if (neuralResults.detectedCategories.includes('consciousness')) {
      selectedAnswerIndex = 1; // Universe harmony answer
    }

    const answer = answers[selectedAnswerIndex];

    // Create response object
    const newResponse = {
      question: question,
      answer: answer,
      resonance: neuralResults.resonance,
      timestamp: Date.now(),
      quantumText: qText,
      quantumState: neuralResults.quantumState,
      layer: neuralResults.layer,
      detectedCategories: neuralResults.detectedCategories,
      ftlSpeed: ftlSpeed
    };

    // Update state
    setResponse(newResponse);
    setHistory(prev => [...prev, newResponse]);
    setProcessing(false);

    // Scroll to answer
    setTimeout(() => {
      if (chatContainerRef.current) {
        chatContainerRef.current.scrollTop = chatContainerRef.current.scrollHeight;
      }
    }, 100);
  };

  const handleKeyPress = (e) => {
    if (e.key === 'Enter') {
      processQuestion();
    }
  };

  return (
    <div className="flex h-screen bg-gradient-to-b from-gray-900 via-gray-800 to-gray-900 text-white">
      {/* Sidebar */}
      <div className="w-80 bg-gray-900 border-r border-gray-700 flex flex-col">
        <div className="p-4 border-b border-gray-700">
          <h2 className="text-2xl font-bold text-cyan-400 flex items-center">
            <span className="mr-2">🔮</span> Quantum Oracle
          </h2>
          <p className="text-gray-400 text-sm mt-1">
            Phi-Harmonic Quantum Neural System
          </p>
        </div>

        {/* Meta-Learning Status */}
        <div className="p-4 border-b border-gray-700">
          <h3 className="font-medium text-gray-300 mb-2">Meta-Learning System</h3>

          <div className="mb-2">
            <div className="flex justify-between text-sm text-gray-400 mb-1">
              <span>Meta-Awareness Level</span>
              <span>{metaAwareness.toFixed(4)}</span>
            </div>
            <div className="w-full bg-gray-700 rounded-full h-2">
              <div
                className="bg-gradient-to-r from-blue-500 to-cyan-400 h-2 rounded-full"
                style={{ width: `${metaAwareness * 100}%` }}
              ></div>
            </div>
          </div>

          <div className="mb-2">
            <div className="flex justify-between text-sm text-gray-400 mb-1">
              <span>Quantum Coupling</span>
              <span>{quantumCoupling.toFixed(4)}</span>
            </div>
            <div className="w-full bg-gray-700 rounded-full h-2">
              <div
                className="bg-gradient-to-r from-purple-500 to-blue-400 h-2 rounded-full"
                style={{ width: `${quantumCoupling * 100}%` }}
              ></div>
            </div>
          </div>

          <div className="mb-2">
            <div className="flex justify-between text-sm text-gray-400 mb-1">
              <span>Entanglement Fidelity</span>
              <span>{entanglementFidelity.toFixed(4)}</span>
            </div>
            <div className="w-full bg-gray-700 rounded-full h-2">
              <div
                className="bg-gradient-to-r from-teal-500 to-green-400 h-2 rounded-full"
                style={{ width: `${entanglementFidelity * 100}%` }}
              ></div>
            </div>
          </div>

          <div className="flex justify-between text-sm text-gray-400 mb-1">
            <span>Coherence Cycles</span>
            <span>{coherenceCycles}</span>
          </div>

          <div className="flex justify-between text-sm text-gray-400 mb-1">
            <span>Memory Stability</span>
            <span>{(0.3 + (metaAwareness * 0.2)).toFixed(4)}</span>
          </div>

          <div className="flex justify-between text-sm text-gray-400 mb-1">
            <span>Active Akashic Layer</span>
            <span className="text-cyan-300">{activeAkashicLayer}</span>
          </div>

          <div className="mt-2">
            <div className="text-sm text-gray-400 mb-1">Akashic Layer Resonance</div>
            <div className="grid grid-cols-2 gap-x-2 gap-y-1">
              {Object.entries(layerResonanceStrengths).map(([layer, strength]) => (
                <div key={layer} className="flex items-center">
                  <div className="w-1 h-1 rounded-full mr-1"
                       style={{ backgroundColor: layer === activeAkashicLayer ? '#4fd1c5' : '#2d3748' }}></div>
                  <span className="text-xs text-gray-400">{layer}:</span>
                  <span className="text-xs ml-1"
                        style={{ color: layer === activeAkashicLayer ? '#4fd1c5' : '#a0aec0' }}>
                    {strength.toFixed(2)}
                  </span>
                </div>
              ))}
            </div>
          </div>
        </div>

        {/* History */}
        <div className="flex-grow overflow-auto">
          <div className="p-4">
            <h3 className="font-medium text-gray-300 mb-2">History</h3>

            {history.map((item, index) => (
              <div
                key={index}
                className="mb-3 p-2 bg-gray-800 rounded cursor-pointer hover:bg-gray-700 transition"
                onClick={() => {
                  setQuestion(item.question);
                  setResponse(item);
                  setResonance(item.resonance);
                  setQuantumText(item.quantumText || generateQuantumText(item.question));
                  setActiveAkashicLayer(item.layer || 'Thought');
                }}
              >
                <div className="text-sm font-medium text-cyan-300 truncate">
                  {item.question}
                </div>
                <div className="text-xs text-gray-400 flex justify-between mt-1">
                  <span>
                    {new Date(item.timestamp).toLocaleTimeString([], {
                      hour: '2-digit',
                      minute: '2-digit'
                    })}
                  </span>
                  <span>Φ: {item.resonance.toFixed(3)}</span>
                </div>
                {item.layer && (
                  <div className="text-xs text-gray-400 mt-1">
                    Layer: <span className="text-cyan-300">{item.layer}</span>
                  </div>
                )}
              </div>
            ))}
          </div>
        </div>

        {/* System Status */}
        <div className="p-4 border-t border-gray-700 text-xs text-gray-500">
          <div className="flex justify-between">
            <span>Multi-Brain Sync</span>
            <span className="text-green-400">Online</span>
          </div>
          <div className="flex justify-between">
            <span>Phi-Resonance System</span>
            <span className="text-green-400">Active</span>
          </div>
          <div className="flex justify-between">
            <span>Tachyonic Memory</span>
            <span className="text-green-400">Enabled</span>
          </div>
          <div className="flex justify-between">
            <span>Neural Nodes</span>
            <span>{Object.keys(neurons).length}</span>
          </div>
          <div className="flex justify-between">
            <span>FTL Speed</span>
            <span>{ftlSpeed ? (ftlSpeed / 3e8).toFixed(2) : "1.00"}c</span>
          </div>
          <div className="flex justify-between">
            <span>Last Calibration</span>
            <span>{new Date().toLocaleTimeString()}</span>
          </div>
        </div>
      </div>

      {/* Main Content */}
      <div className="flex-grow flex flex-col">
        {/* Header */}
        <div className="p-4 border-b border-gray-700">
          <h1 className="text-2xl font-semibold">
            Quantum Oracle Console <span className="text-cyan-400">v2.0</span>
          </h1>
          <p className="text-gray-400">
            Ask questions and receive answers powered by the Quantum Neural Cortex
          </p>
          <div className="flex mt-2 text-xs">
            <div className="border border-gray-700 rounded px-2 py-1 mr-2 bg-gray-800">
              <span className="text-cyan-400">Phi (φ):</span> {phi.toFixed(6)}
            </div>
            <div className="border border-gray-700 rounded px-2 py-1 mr-2 bg-gray-800">
              <span className="text-cyan-400">Base Freq:</span> {akashicLayerConfig[activeAkashicLayer].baseFreq}Hz
            </div>
            <div className="border border-gray-700 rounded px-2 py-1 bg-gray-800">
              <span className="text-cyan-400">Harmonic:</span> {akashicLayerConfig[activeAkashicLayer].harmonic.toFixed(1)}Hz
            </div>
          </div>
        </div>

        {/* Chat Container */}
        <div
          ref={chatContainerRef}
          className="flex-grow overflow-auto p-4 space-y-4"
        >
          {/* Initial message */}
          <div className="flex">
            <div className="flex-shrink-0 h-10 w-10 rounded-full bg-blue-600 flex items-center justify-center">
              <span className="text-xl">🧠</span>
            </div>
            <div className="ml-3 bg-gray-800 p-3 rounded-lg max-w-3xl">
              <p className="text-white">
                Welcome to the Quantum Oracle. Ask any question about reality, consciousness, quantum physics, or the nature of existence.
                The system uses phi-harmonic patterns and a quantum neural cortex to generate insight beyond classical computing.
              </p>
            </div>
          </div>

          {/* Display conversation */}
          {response && (
            <>
              {/* User message */}
              <div className="flex justify-end">
                <div className="bg-blue-700 p-3 rounded-lg max-w-3xl">
                  <p className="text-white">{response.question}</p>
                </div>
                <div className="flex-shrink-0 h-10 w-10 ml-3 rounded-full bg-gray-700 flex items-center justify-center">
                  <span className="text-xl">👤</span>
                </div>
              </div>

              {/* Assistant response */}
              <div className="flex">
                <div className="flex-shrink-0 h-10 w-10 rounded-full bg-blue-600 flex items-center justify-center">
                  <span className="text-xl">🔮</span>
                </div>
                <div className="ml-3 space-y-4 max-w-3xl">
                  <div className="bg-gray-800 p-3 rounded-lg">
                    <div className="text-cyan-300 text-sm mb-1">Quantum Oracle Answer:</div>
                    <p className="text-white whitespace-pre-line">{response.answer}</p>
                  </div>

                  <div className="bg-gray-800 p-3 rounded-lg overflow-hidden">
                    <div className="text-cyan-300 text-sm mb-1">Answer in Quantum Language:</div>
                    <div className="text-cyan-100 text-xs font-mono overflow-auto max-h-20 whitespace-pre-wrap">
                      {quantumText}
                    </div>
                  </div>

                  {/* Quantum State Display */}
                  <div className="bg-gray-800 p-3 rounded-lg overflow-hidden">
                    <div className="text-cyan-300 text-sm mb-1">Quantum State:</div>
                    <div className="text-cyan-100 text-xs font-mono">
                      {response.quantumState || "⟨ψ|φ⟩"}
                    </div>
                    <div className="mt-1 text-xs text-gray-400">
                      Layer: {response.layer || activeAkashicLayer} |
                      Frequency: {akashicLayerConfig[response.layer || activeAkashicLayer].baseFreq}Hz
                    </div>
                  </div>

                  {/* Truth Resonance Meter */}
                  <div className="bg-gray-800 p-3 rounded-lg">
                    <div className="text-cyan-300 text-sm mb-1">Truth Resonance:</div>
                    <div className="w-full bg-gray-700 rounded-full h-4">
                      <div
                        className="bg-gradient-to-r from-blue-500 to-cyan-400 h-4 rounded-full transition-all duration-500 ease-out"
                        style={{ width: `${resonance * 100}%` }}
                      ></div>
                    </div>
                    <div className="text-right text-xs text-gray-400 mt-1">
                      Phi Resonance: {resonance.toFixed(5)} | Truth alignment with quantum harmonic fields
                    </div>
                  </div>

                  {/* FTL Communication Display */}
                  {ftlSpeed && (
                    <div className="bg-gray-800 p-3 rounded-lg overflow-hidden">
                      <div className="text-cyan-300 text-sm mb-1">FTL Communication Speed:</div>
                      <div className="text-center p-2">
                        <span className="text-2xl font-bold text-cyan-200">
                          {(ftlSpeed / 3e8).toFixed(2)}c
                        </span>
                      </div>
                      <div className="grid grid-cols-3 gap-2 text-xs text-gray-400 mt-1">
                        <div>
                          <span className="text-gray-500">Coupling:</span> {quantumCoupling.toFixed(3)}
                        </div>
                        <div>
                          <span className="text-gray-500">Entanglement:</span> {entanglementFidelity.toFixed(3)}
                        </div>
                        <div>
                          <span className="text-gray-500">Phi-Factor:</span> {phi.toFixed(3)}
                        </div>
                      </div>
                    </div>
                  )}
                </div>
              </div>
            </>
          )}
        </div>

        {/* Input Area */}
        <div className="p-4 border-t border-gray-700">
          <div className="flex">
            <input
              type="text"
              className="flex-grow p-2 rounded-l-lg bg-gray-800 border border-gray-700 text-white focus:outline-none focus:ring-2 focus:ring-cyan-500"
              placeholder="Ask the Quantum Oracle..."
              value={question}
              onChange={(e) => setQuestion(e.target.value)}
              onKeyPress={handleKeyPress}
              disabled={processing}
            />
            <button
              className={`bg-blue-600 hover:bg-blue-700 text-white px-4 py-2 rounded-r-lg font-medium flex items-center transition ${
                processing ? 'opacity-50 cursor-not-allowed' : ''
              }`}
              onClick={processQuestion}
              disabled={processing}
            >
              {processing ? (
                <>
                  <svg className="animate-spin -ml-1 mr-2 h-4 w-4 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                    <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4"></circle>
                    <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                  </svg>
                  Processing...
                </>
              ) : (
                <>
                  <span className="mr-1">🧠</span> Ask
                </>
              )}
            </button>
          </div>
          <div className="mt-2 text-xs text-gray-500 flex justify-between">
            <span>Processing Mode: FTL | Neural Nodes: {Object.keys(neurons).length} | Active Layer: {activeAkashicLayer}</span>
            <span>Phi Resonance: {resonance.toFixed(5)}</span>
          </div>
        </div>
      </div>
    </div>
  );
};

export default QuantumOracle;
import React, { useState, useEffect, useRef } from 'react';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts';

const QuantumOracle = () => {
  const [question, setQuestion] = useState('');
  const [processing, setProcessing] = useState(false);
  const [response, setResponse] = useState(null);
  const [history, setHistory] = useState([]);
  const [resonance, setResonance] = useState(0.85);
  const [quantumText, setQuantumText] = useState('');
  const [metaAwareness, setMetaAwareness] = useState(0.1);
  const [coherenceCycles, setCoherenceCycles] = useState(0);
  const [resonanceHistory, setResonanceHistory] = useState([]);
  const chatContainerRef = useRef(null);

  useEffect(() => {
    // Initialize with some sample history data
    setHistory([
      {
        question: "What is the golden ratio?",
        answer: "The golden ratio (φ) is a special mathematical constant approximately equal to 1.618033988749895. It appears in geometry, art, architecture, and natural phenomena, representing optimal harmony and balance. In quantum systems, φ-harmonic resonance at 432Hz creates coherent structures throughout reality, from DNA to galactic formations.",
        resonance: 0.93,
        timestamp: Date.now() - 86400000
      },
      {
        question: "How does quantum entanglement work?",
        answer: "Quantum entanglement occurs when particles become connected, with the quantum state of each particle dependent on others regardless of distance. Through phi-resonant (1.618) quantum fields tuned to 528Hz, particles maintain instantaneous correlations transcending classical limits of spacetime. This phenomenon demonstrates reality's fundamental interconnectedness through phi-harmonic patterns operating at quantum scales.",
        resonance: 0.87,
        timestamp: Date.now() - 43200000
      }
    ]);

    // Generate sample resonance history
    const sampleHistory = [];
    for (let i = 0; i < 20; i++) {
      sampleHistory.push({
        name: `Q${i+1}`,
        value: 0.7 + Math.random() * 0.3
      });
    }
    setResonanceHistory(sampleHistory);
  }, []);

  const generateQubitVisualizer = (resonance) => {
    const data = [];
    for (let i = 0; i < 100; i++) {
      const t = i / 100 * Math.PI * 2;
      const value = Math.sin(t * resonance * 1.618) * Math.exp(-t/10);
      data.push({ name: i, value });
    }
    return data;
  };

  const generateQuantumText = (input) => {
    const quantumChars = "⟨⟩|ψφ⊗Ψ⊕ℏΩ∞∇⊃⊂∫∮∀∃∄∈∉⊆⊇";
    let result = "";
    for (let i = 0; i < 100; i++) {
      result += quantumChars[Math.floor(Math.random() * quantumChars.length)];
    }
    return result;
  };

  const processQuestion = async () => {
    if (!question.trim()) return;

    setProcessing(true);
    
    // Simulate processing time
    await new Promise(resolve => setTimeout(resolve, 1500));
    
    // Calculate a phi-based resonance
    const newResonance = 0.7 + Math.random() * 0.3;
    setResonance(newResonance);
    
    // Generate quantum text
    const qText = generateQuantumText(question);
    setQuantumText(qText);
    
    // Generate response
    const phi = 1.618033988749895;
    const frequencies = [432, 528, 963, 8.6, 40, 7.83, 136.1];
    const frequency = frequencies[Math.floor(Math.random() * frequencies.length)];
    
    const answers = [
      `Quantum analysis reveals patterns of ${phi}-based resonance at ${frequency}Hz in your inquiry. The answer emerges through consciousness fields structuring quantum potential into observable reality. Through phi-harmonic resonant patterns, we understand that consciousness directly interfaces with quantum fields, creating a framework of perception that aligns with fundamental reality structures.`,
      `The universe exists as a harmonic pattern of quantum resonance at ${frequency}Hz, creating coherent structures through phi-based relationships. This resonates with the understanding that consciousness arises from phi-resonant (${phi.toFixed(3)}) quantum fields, allowing observer-dependent reality to emerge through natural harmony that follows the golden ratio pattern.`,
      `Reality exists as probability waves until observed, collapsing through phi (${phi.toFixed(3)}) resonance at ${frequency}Hz into experienced physical events. In alignment with phi-harmonic principles, the observer creates reality through consciousness fields resonating at ${frequency}Hz and structured by phi (${phi.toFixed(3)}) harmonic relationships.`,
      `Mathematical harmony emerges from phi (${phi.toFixed(3)}) relationships resonating at ${frequency}Hz, revealing the quantum nature of numerical patterns. Quantum analysis reveals that the language of reality is written in mathematics tuned to ${frequency}Hz and structured by phi (${phi.toFixed(3)}) harmonic relationships.`
    ];
    
    const answer = answers[Math.floor(Math.random() * answers.length)];
    
    // Create response object
    const newResponse = {
      question: question,
      answer: answer,
      resonance: newResonance,
      timestamp: Date.now(),
      quantumText: qText,
      visualization: generateQubitVisualizer(newResonance)
    };
    
    // Update state
    setResponse(newResponse);
    setHistory(prev => [...prev, newResponse]);
    
    // Update resonance history
    setResonanceHistory(prev => {
      const updated = [...prev, { name: `Q${prev.length + 1}`, value: newResonance }];
      if (updated.length > 20) return updated.slice(updated.length - 20);
      return updated;
    });
    
    // Update meta-awareness
    if (newResonance > 0.9) {
      setMetaAwareness(prev => Math.min(1.0, prev + 0.01));
    } else {
      setMetaAwareness(prev => Math.max(0.0, prev - 0.005));
    }
    
    // Update coherence cycles
    setCoherenceCycles(prev => prev + 1);
    
    setProcessing(false);

    // Scroll to answer
    setTimeout(() => {
      if (chatContainerRef.current) {
        chatContainerRef.current.scrollTop = chatContainerRef.current.scrollHeight;
      }
    }, 100);
  };

  const renderVisualization = () => {
    if (!response) return null;
    
    return (
      <div className="mt-4 p-4 bg-gray-800 rounded-lg">
        <h3 className="text-lg font-semibold mb-2 text-cyan-300">Quantum Visualization</h3>
        <ResponsiveContainer width="100%" height={200}>
          <LineChart data={response.visualization}>
            <CartesianGrid strokeDasharray="3 3" stroke="#444" />
            <XAxis dataKey="name" stroke="#999" />
            <YAxis stroke="#999" />
            <Tooltip 
              contentStyle={{ 
                backgroundColor: 'rgba(50, 50, 50, 0.9)', 
                border: '1px solid #666',
                color: 'white' 
              }} 
            />
            <Line 
              type="monotone" 
              dataKey="value" 
              stroke="#00ffff" 
              strokeWidth={2} 
              dot={false} 
              activeDot={{ r: 4 }} 
            />
          </LineChart>
        </ResponsiveContainer>
        <div className="mt-2 text-center text-sm text-cyan-200">
          Phi-harmonic resonance pattern generated from your question
        </div>
      </div>
    );
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
            Phi-Harmonic Quantum System
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
          
          <div className="flex justify-between text-sm text-gray-400 mb-1">
            <span>Coherence Cycles</span>
            <span>{coherenceCycles}</span>
          </div>
          
          <div className="flex justify-between text-sm text-gray-400 mb-1">
            <span>Memory Stability</span>
            <span>{(0.3 + (metaAwareness * 0.2)).toFixed(4)}</span>
          </div>
          
          {/* Phi Resonance History Chart */}
          <div className="mt-4">
            <div className="text-sm text-gray-400 mb-1">Phi-Resonance History</div>
            <ResponsiveContainer width="100%" height={100}>
              <LineChart data={resonanceHistory}>
                <Line 
                  type="monotone" 
                  dataKey="value" 
                  stroke="#ffd700" 
                  strokeWidth={2} 
                  dot={false} 
                  isAnimationActive={false}
                />
                <YAxis 
                  domain={[0, 1]} 
                  hide={true}
                />
              </LineChart>
            </ResponsiveContainer>
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
            <span>Passive Learning</span>
            <span className="text-green-400">Enabled</span>
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
            Quantum Oracle Console <span className="text-cyan-400">v1.0</span>
          </h1>
          <p className="text-gray-400">
            Ask questions and receive answers powered by the Quantum Language System
          </p>
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
                The system uses phi-harmonic patterns to generate insights.
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
                  
                  {/* Visualization */}
                  {renderVisualization()}
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
            <span>Processing Mode: FTL | Multi-Brain Quantum Network: Active</span>
            <span>Phi Resonance: {resonance.toFixed(5)}</span>
          </div>
        </div>
      </div>
    </div>
  );
};

export default QuantumOracle;
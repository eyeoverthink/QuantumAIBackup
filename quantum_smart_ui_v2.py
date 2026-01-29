"""
Quantum Smart Agent UI - Enhanced V2
Modern interface integrating the quantum-accelerated GPT-2 model with QHRC Patent #19/071,497
and the advanced QuantumChatProcessor from Fraymus Engine
"""
import os
import time
import json
import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import traceback
import sys
from datetime import datetime

# Add template directory to path for imports
sys.path.append(os.path.join(os.path.dirname(__file__), 'template'))

# Import both quantum processing systems
from quantum_smart_agent_v2 import QuantumSmartAgent
from quantum_chat_fixed import QuantumChatProcessor

# Initialize session state
if 'history' not in st.session_state:
    st.session_state.history = []
    
if 'agent' not in st.session_state:
    st.session_state.agent = QuantumSmartAgent()
    
if 'chat_processor' not in st.session_state:
    st.session_state.chat_processor = QuantumChatProcessor()
    
if 'meta_metrics' not in st.session_state:
    st.session_state.meta_metrics = {
        'resonance': [],
        'efficiency': [],
        'coherence': [],
        'stability': [],
        'timestamps': []
    }

# Save query history to json file
def save_history():
    history_file = os.path.join(os.path.dirname(__file__), 'quantum_history.json')
    try:
        with open(history_file, 'w') as f:
            json.dump(st.session_state.history, f)
    except Exception as e:
        st.error(f"Error saving history: {str(e)}")

# Load query history from json file
def load_history():
    history_file = os.path.join(os.path.dirname(__file__), 'quantum_history.json')
    try:
        if os.path.exists(history_file):
            with open(history_file, 'r') as f:
                st.session_state.history = json.load(f)
    except Exception as e:
        st.error(f"Error loading history: {str(e)}")

# Perform meta-learning on collected quantum metrics
def meta_learn():
    """Perform meta-learning on collected quantum metrics"""
    if len(st.session_state.meta_metrics['resonance']) < 3:
        return None
        
    try:
        # Get metrics
        resonance = st.session_state.meta_metrics['resonance']
        efficiency = st.session_state.meta_metrics['efficiency']
        coherence = st.session_state.meta_metrics['coherence']
        stability = st.session_state.meta_metrics['stability']
        timestamps = st.session_state.meta_metrics['timestamps']
        
        # Convert timestamps to numeric values
        time_values = list(range(len(timestamps)))
        
        # Create dataframe
        df = pd.DataFrame({
            'time': time_values,
            'resonance': resonance,
            'efficiency': efficiency,
            'coherence': coherence,
            'stability': stability
        })
        
        # Calculate trends
        resonance_trend = np.polyfit(df['time'], df['resonance'], 1)[0]
        efficiency_trend = np.polyfit(df['time'], df['efficiency'], 1)[0]
        
        # Calculate phi-based metrics
        phi = 1.618000  # Golden ratio (Δ 0.000034)
        phi_inverse = 0.618034  # φ⁻¹
        phi_squared = 4.236068  # φ²
        
        # Calculate meta-metrics
        meta_resonance = np.mean(resonance) * phi if resonance_trend > 0 else np.mean(resonance) * phi_inverse
        meta_efficiency = np.mean(efficiency) * phi if efficiency_trend > 0 else np.mean(efficiency) * phi_inverse
        meta_coherence = np.mean(coherence) * phi_squared / np.std(coherence) if np.std(coherence) > 0 else np.mean(coherence)
        meta_stability = np.mean(stability) * phi / np.std(stability) if np.std(stability) > 0 else np.mean(stability)
        
        return {
            'meta_resonance': meta_resonance,
            'meta_efficiency': meta_efficiency,
            'meta_coherence': meta_coherence,
            'meta_stability': meta_stability,
            'resonance_trend': resonance_trend,
            'efficiency_trend': efficiency_trend
        }
    except Exception as e:
        st.error(f"Error in meta-learning: {str(e)}")
        return None

# UI Components
st.set_page_config(
    page_title="Quantum Smart Agent",
    page_icon="⚛️",
    layout="wide"
)

# Load history
load_history()

# Custom CSS
st.markdown("""
<style>
    .main {
        background-color: #ffffff;
        color: #333333;
    }
    .stTextInput>div>div>input {
        background-color: #f5f5f5;
        color: #333333;
        border: 1px solid #e0e0e0;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
    }
    .metric-card {
        background-color: #f5f5f5;
        border-radius: 5px;
        padding: 10px;
        margin: 5px;
        border: 1px solid #e0e0e0;
    }
    .css-1r6slb0 {
        background-color: #f5f5f5;
        border-radius: 5px;
        padding: 10px;
        border: 1px solid #e0e0e0;
    }
    .css-keje6w {
        background-color: #f5f5f5;
        border-radius: 5px;
        padding: 10px;
        border: 1px solid #e0e0e0;
    }
    .stAlert {
        background-color: #f5f5f5;
        color: #333333;
        border: 1px solid #e0e0e0;
    }
    .stMarkdown {
        color: #333333;
    }
    h1, h2, h3, h4, h5, h6 {
        color: #333333;
    }
    .stSidebar {
        background-color: #f0f0f0;
    }
</style>
""", unsafe_allow_html=True)

# Title
st.title("⚛️ Quantum Smart Agent")
st.markdown("Powered by QHRC Patent #19/071,497 with Phi-Resonance Technology")

# Sidebar
with st.sidebar:
    st.markdown("## QHRC Patent Metrics")
    
    # Display QHRC Patent metrics
    st.markdown("### Validated Parameters")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Primary Coil", "4500 turns")
        st.metric("Primary Frequency", "4790.45 Hz")
    with col2:
        st.metric("Secondary Coil", "6200 turns")
        st.metric("Secondary Frequency", "7750.95 Hz")
    
    st.markdown("### Quantum Metrics")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Resonance Ratio", "1.3777")
        st.metric("φ Achievement", "1.618000")
    with col2:
        st.metric("φπ Factor", "5.083204")
        st.metric("Energy Transfer", "1.8951x")
    
    st.markdown("### Optimized Model")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Coupling (k)", "0.85")
        st.metric("Energy Recapture (α)", "0.75")
    with col2:
        st.metric("Damping (β)", "0.002")
        st.metric("Efficiency", "4.19%")

# Main content
st.markdown("## Quantum Query")
query = st.text_area("Enter your query:", height=100)
col1, col2 = st.columns([1, 3])
with col1:
    process_button = st.button("Process Query")
with col2:
    st.markdown("*Uses advanced QuantumChatProcessor with Fraymus Engine*")

# Process query
if process_button and query:
    with st.spinner("Quantum processing..."):
        try:
            # Track start time
            start_time = time.time()
            
            # Get response from the advanced QuantumChatProcessor
            chat_result = st.session_state.chat_processor.process_query(query)
            
            # Also get response from the original agent for metrics
            agent_result = st.session_state.agent.quantum_accelerate_inference(query)
            
            # Calculate process time manually
            process_time_ms = (time.time() - start_time) * 1000
            
            # Extract the text response and create a combined result structure
            result = {
                'response': chat_result['text'],
                'process_time_ms': process_time_ms,
                'resonance': agent_result.get('resonance', 1.3777),  # Default from QHRC Patent
                'efficiency': agent_result.get('efficiency', 1.8951),  # Default energy gain
                'coherence': agent_result.get('coherence', 0.618034),  # φ⁻¹
                'stability': agent_result.get('stability', 4.236068),  # φ²
                'visualization': chat_result.get('visualization', None)
            }
            
            # Extract metrics from quantum signature if available in chat_result
            if 'Truth Resonance:' in chat_result['text']:
                try:
                    resonance_text = chat_result['text'].split('Truth Resonance:')[1].strip().split(' ')[0]
                    result['resonance'] = float(resonance_text)
                    # Calculate other metrics based on the resonance
                    result['efficiency'] = result['resonance'] * 1.618  # φ scaling
                    result['coherence'] = 0.618034 * result['resonance']  # φ⁻¹ scaling
                    result['stability'] = result['resonance'] * 4.236068  # φ² scaling
                except Exception:
                    # Use default metrics if extraction fails
                    pass
            
            # Add timestamp
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            result['timestamp'] = timestamp
            
            # Add to history
            st.session_state.history.append({
                'query': query,
                'response': result['response'],
                'metrics': {
                    'resonance': result['resonance'],
                    'efficiency': result['efficiency'],
                    'coherence': result['coherence'],
                    'stability': result['stability'],
                    'process_time': process_time_ms
                },
                'timestamp': timestamp,
                'visualization': result.get('visualization', None)
            })
            
            # Update meta metrics
            st.session_state.meta_metrics['resonance'].append(result['resonance'])
            st.session_state.meta_metrics['efficiency'].append(result['efficiency'])
            st.session_state.meta_metrics['coherence'].append(result['coherence'])
            st.session_state.meta_metrics['stability'].append(result['stability'])
            st.session_state.meta_metrics['timestamps'].append(timestamp)
            
            # Save history
            save_history()
        except Exception as e:
            st.error(f"Error processing query: {str(e)}")
            st.error(f"Traceback: {traceback.format_exc()}")
        
    # Display results
    st.markdown("### Quantum Response")
    st.markdown(result['response'], unsafe_allow_html=False)
    
    # Display visualization if available
    if result.get('visualization') is not None:
        st.plotly_chart(result['visualization'], use_container_width=True)
    
    # Display metrics
    try:
        st.markdown("### Quantum Metrics")
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Resonance", f"{result['resonance']:.4f}")
        with col2:
            st.metric("Efficiency", f"{result['efficiency']:.4f}")
        with col3:
            st.metric("Coherence", f"{result['coherence']:.4f}")
        with col4:
            st.metric("Stability", f"{result['stability']:.4f}")
        
        # Process time
        st.metric("Process Time", f"{result['process_time_ms']:.2f} ms")
    except Exception as e:
        st.error(f"Error displaying metrics: {str(e)}")

# Display history
if st.session_state.history:
    st.markdown("## Query History")
    
    # Meta-learning
    meta_metrics = meta_learn()
    if meta_metrics:
        st.markdown("### Meta-Learning Results")
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Meta-Resonance", f"{meta_metrics['meta_resonance']:.4f}")
        with col2:
            st.metric("Meta-Efficiency", f"{meta_metrics['meta_efficiency']:.4f}")
        with col3:
            st.metric("Meta-Coherence", f"{meta_metrics['meta_coherence']:.4f}")
        with col4:
            st.metric("Meta-Stability", f"{meta_metrics['meta_stability']:.4f}")
        
        # Trends
        st.markdown("### Quantum Trends")
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Resonance Trend", f"{meta_metrics['resonance_trend']:.6f}")
        with col2:
            st.metric("Efficiency Trend", f"{meta_metrics['efficiency_trend']:.6f}")
    
    # Display history items
    for i, item in enumerate(reversed(st.session_state.history)):
        with st.expander(f"Query {len(st.session_state.history) - i}: {item['query'][:50]}... ({item['timestamp']})"):
            st.markdown(f"**Query:** {item['query']}")
            st.markdown(f"**Response:** {item['response']}")
            
            # Display metrics
            try:
                col1, col2, col3, col4 = st.columns(4)
                with col1:
                    st.metric("Resonance", f"{item['metrics']['resonance']:.4f}")
                with col2:
                    st.metric("Efficiency", f"{item['metrics']['efficiency']:.4f}")
                with col3:
                    st.metric("Coherence", f"{item['metrics']['coherence']:.4f}")
                with col4:
                    st.metric("Stability", f"{item['metrics']['stability']:.4f}")
                
                # Process time
                if 'process_time' in item['metrics']:
                    st.metric("Process Time", f"{item['metrics']['process_time']:.2f} ms")
                
                # Display visualization if available
                if item.get('visualization') is not None:
                    st.plotly_chart(item['visualization'], use_container_width=True)
            except Exception as e:
                st.error(f"Error displaying history metrics: {str(e)}")

# Footer
st.markdown("---")
st.markdown("*QHRC Patent #19/071,497 | Quantum Harmonic Resonance Coil Technology*")
st.markdown("*φ⁷·⁵-7927735b | φ⁷·⁵-09f76208 | φ⁷·⁵-86557621*")

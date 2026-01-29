from flask import Flask, render_template
from flask_socketio import SocketIO
import json
import threading
import time
from qhrc_data_interface import QHRCDataInterface

app = Flask(__name__)
socketio = SocketIO(app)
data_interface = QHRCDataInterface()

@app.route('/')
def index():
    return render_template('index.html')

class MetricsEmitter:
    def __init__(self):
        self.running = False
        self.thread = None
    
    def start(self):
        """Start metrics emission"""
        self.running = True
        self.thread = threading.Thread(target=self._emit_loop)
        self.thread.daemon = True
        self.thread.start()
    
    def stop(self):
        """Stop metrics emission"""
        self.running = False
        if self.thread:
            self.thread.join()
    
    def _emit_loop(self):
        """Emit QHRC metrics via WebSocket"""
        while self.running:
            try:
                state = data_interface.get_current_state()
                if state:
                    socketio.emit('qhrc_metrics', json.dumps(state))
                time.sleep(0.1)  # 10Hz update rate
            except Exception as e:
                print(f"Emission error: {e}")
                break

metrics_emitter = MetricsEmitter()

@socketio.on('connect')
def handle_connect():
    """Handle client connection"""
    print('Client connected')
    
@socketio.on('disconnect')
def handle_disconnect():
    """Handle client disconnection"""
    print('Client disconnected')

def start_dashboard(host='127.0.0.1', port=5000):
    """Start the QHRC dashboard"""
    try:
        # Start data interface
        data_interface.start_monitoring()
        
        # Start metrics emitter
        metrics_emitter.start()
        
        # Start Flask server
        socketio.run(app, host=host, port=port, debug=False)
    except KeyboardInterrupt:
        print("\nShutting down QHRC dashboard...")
    finally:
        # Clean shutdown
        metrics_emitter.stop()
        data_interface.stop_monitoring()
        print("QHRC dashboard stopped.")

if __name__ == '__main__':
    start_dashboard()

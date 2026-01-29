# # from flask import Flask, jsonify, request
# # from flask_socketio import SocketIO
# # import numpy as np
# # import random
# # import sqlite3
# # import os
# # from cryptography.fernet import Fernet

# # app = Flask(__name__)
# # socketio = SocketIO(app, cors_allowed_origins="*")

# # # === TACHYON BRAIN CLASS ===
# # class TachyonBrain:
# #     def __init__(self):
# #         self.data_matrix = np.zeros((100, 100))  # Placeholder for data processing
# #         self.processed_data = []

# #     def process_data(self, input_data):
# #         """Process data using tachyonic principles."""
# #         processed_data = np.array(input_data) * np.random.rand(*input_data.shape)
# #         self.processed_data.append(processed_data)  # Store processed data
# #         return processed_data.tolist()

# #     def communicate(self, message):
# #         """Simulate instantaneous communication."""
# #         return f"Tachyon Brain received message: {message}"

# #     def make_decision(self, options):
# #         """Make a decision based on available options."""
# #         return np.random.choice(options)

# #     def aggregate_data(self):
# #         """Aggregate all processed data."""
# #         return np.sum(self.processed_data, axis=0).tolist()  # Sum all processed data

# # # Initialize the Tachyon Brain
# # tachyon_brain = TachyonBrain()

# # @app.route('/process', methods=['POST'])
# # def process():
# #     data = request.json.get("data", [])
# #     processed = tachyon_brain.process_data(np.array(data))
# #     return jsonify({"processed_data": processed})

# # @app.route('/communicate', methods=['POST'])
# # def communicate():
# #     message = request.json.get("message", "Hello")
# #     response = tachyon_brain.communicate(message)
# #     return jsonify({"response": response})

# # @app.route('/decision', methods=['POST'])
# # def decision():
# #     options = request.json.get("options", ["Yes", "No"])
# #     choice = tachyon_brain.make_decision(options)
# #     return jsonify({"decision": choice})

# # @app.route('/aggregate', methods=['GET'])
# # def aggregate():
# #     aggregated_data = tachyon_brain.aggregate_data()
# #     return jsonify({"aggregated_data": aggregated_data})

# # if __name__ == '__main__':
# #     socketio.run(app, host="0.0.0.0", port=5051, debug=True)

# from flask import Flask, jsonify, request
# from flask_socketio import SocketIO
# import numpy as np
# import random
# import sqlite3
# import os
# from cryptography.fernet import Fernet
# import time
# import hashlib
# import json

# app = Flask(__name__)
# socketio = SocketIO(app, cors_allowed_origins="*")

# # Database file path
# DB_FILE = "fraymus_omega_fractal_storage.db"
# ENCRYPTION_KEY = os.getenv('ENCRYPTION_KEY', Fernet.generate_key())
# cipher = Fernet(ENCRYPTION_KEY)

# # === TACHYON BRAIN CLASS ===
# class TachyonBrain:
#     def __init__(self):
#         self.data_matrix = np.zeros((100, 100))  # Placeholder for data processing
#         self.processed_data = []

#     def process_data(self, input_data):
#         """Process data using tachyonic principles."""
#         processed_data = np.array(input_data) * np.random.rand(*input_data.shape)
#         self.processed_data.append(processed_data)  # Store processed data
#         return processed_data.tolist()

#     def communicate(self, message):
#         """Process natural language queries."""
#         message = message.lower()
        
#         if re.search(r'\bwhat is pi\b', message):
#             return "The value of pi is approximately 3.14159."
#         elif re.search(r'\bhow are you\b', message):
#             return "I'm just a program, but thanks for asking!"
#         elif re.search(r'\bwhat is the capital of france\b', message):
#             return "The capital of France is Paris."
#         else:
#             return "I'm not sure how to answer that. Can you ask something else?"

#     def make_decision(self, options):
#         """Make a decision based on available options."""
#         return np.random.choice(options)

#     def aggregate_data(self):
#         """Aggregate all processed data."""
#         return np.sum(self.processed_data, axis=0).tolist()  # Sum all processed data

# # Initialize the Tachyon Brain
# tachyon_brain = TachyonBrain()

# @app.route('/process', methods=['POST'])
# def process():
#     data = request.json.get("data", [])
#     processed = tachyon_brain.process_data(np.array(data))
#     return jsonify({"processed_data": processed})

# @app.route('/communicate', methods=['POST'])
# def communicate():
#     message = request.json.get("message", "Hello")
#     response = tachyon_brain.communicate(message)
#     return jsonify({"response": response})

# @app.route('/decision', methods=['POST'])
# def decision():
#     options = request.json.get("options", ["Yes", "No"])
#     choice = tachyon_brain.make_decision(options)
#     return jsonify({"decision": choice})

# @app.route('/aggregate', methods=['GET'])
# def aggregate():
#     aggregated_data = tachyon_brain.aggregate_data()
#     return jsonify({"aggregated_data": aggregated_data})

# if __name__ == '__main__':
#     socketio.run(app, host="0.0.0.0", port=5051, debug=True)

from flask import Flask, request, jsonify
from template.fraymus_penny import QuantumProcessor
import numpy as np

app = Flask(__name__)
processor = QuantumProcessor()

@app.route('/api/quantum/process', methods=['POST'])
def process_quantum():
    try:
        data = request.get_json()
        query = data.get('query', '')
        
        # Generate random quantum parameters for testing
        params = np.random.rand(8).tolist()
        
        # Process quantum data
        result = processor.process_quantum_data(params, query)
        return jsonify(result)
        
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e),
            "traceback": str(e.__traceback__)
        })

if __name__ == '__main__':
    app.run(port=5001)
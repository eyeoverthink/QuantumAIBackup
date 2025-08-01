from flask import Flask, render_template, request, jsonify
import time

app = Flask(__name__)

class TachyonBrain:
    def __init__(self):
        self.memory = {}

    def ask(self, question):
        """Process the question and return an AI response"""
        time.sleep(0.5)  # Simulate processing
        response = f"Fraymus AI Response: {question[::-1]}"  # Reverse text for fun
        self.memory[question] = response
        return response

fraymus_ai = TachyonBrain()

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/query', methods=['POST'])
def query():
    data = request.get_json()
    question = data.get("question", "")
    response = fraymus_ai.ask(question)
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)
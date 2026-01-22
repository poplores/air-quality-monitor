from flask import Flask, request, jsonify
from datetime import datetime
import json
import os

app = Flask(__name__)

# Simple file-based storage for now
DATA_FILE = 'sensor_data.json'

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    return []

def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f)

@app.route('/api/data', methods=['POST'])
def receive_data():
    data = request.json
    data['timestamp'] = datetime.now().isoformat()
    
    all_data = load_data()
    all_data.append(data)
    save_data(all_data)
    
    return jsonify({"status": "success"}), 200

@app.route('/api/data', methods=['GET'])
def get_data():
    return jsonify(load_data())

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
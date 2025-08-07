# src/analyzer.py
from flask import Flask, request, jsonify
from sklearn.ensemble import IsolationForest
import pandas as pd
import numpy as np

app = Flask(__name__)

# In a real application, this model would be trained and loaded.
# This is a placeholder model for demonstration.
model = IsolationForest(contamination=0.01)
# Fit the model with some dummy normal data
normal_data = np.random.rand(100, 5) 
model.fit(normal_data)


@app.route('/analyze', methods=['POST'])
def analyze():
    """
    Receives log data from the Go proxy and returns an anomaly score.
    """
    log_data = request.get_json()
    
    # --- Feature Engineering (Simplified) ---
    # A real implementation would convert IP, endpoint, etc., into numerical features.
    # Here, we just generate random features for the simulation.
    features = np.random.rand(1, 5)
    
    # --- Anomaly Detection ---
    prediction = model.predict(features)
    score = model.decision_function(features)
    
    is_anomaly = prediction[0] == -1
    
    response = {
        'is_anomaly': bool(is_anomaly),
        'anomaly_score': round(score[0], 4)
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True, port=5001)

from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS  # CORS için
from joblib import load
import numpy as np

app = Flask(__name__)
CORS(app)  # Tüm origin'lere izin ver

# Modeli yükle
model = load('icecream_model.joblib')

# Ana sayfa için HTML dosyasını sun
@app.route('/')
def home():
    return send_from_directory('static', 'index.html')

# Tahmin endpoint'i
@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        temperature = float(data['temperature'])
        prediction = model.predict(np.array([[temperature]]))
        return jsonify({
            'temperature': temperature,
            'predicted_sales': round(float(prediction[0]), 2)
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
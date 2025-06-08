from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)
model = joblib.load('../data/rf_model.joblib')

@app.route('/predict', methods=['POST'])
def predict():
  data = request.get_json(force=True)
  features = [
    data['humidity'],
    data['win_speed'],
    data['dayofyear'],
    data['year']
  ]
  pred = model.predict([features])[0]
  return jsonify({'predicted_temperature': pred})

if __name__ == '__main__':
  app.run(debug=True)
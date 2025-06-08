from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)
model = joblib.load('data/rf_model.joblib')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    try:
        humidity = float(data['humidity'])
        wind_speed = float(data['wind_speed'])
        dayofyear = int(data['dayofyear'])
        year = int(data['year'])
    except Exception as e:
        return jsonify({'error': str(e)}), 400

    X_new = pd.DataFrame([[humidity, wind_speed, dayofyear, year]],
                        columns=['humidity', 'wind_speed', 'dayofyear', 'year'])
    prediction = model.predict(X_new)[0]
    return jsonify({'predicted_temperature': round(float(prediction), 2)})

if __name__ == '__main__':
    app.run(debug=True)
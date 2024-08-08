from flask import Flask, request, jsonify
import joblib
import pandas as pd

# Initialize Flask app
app = Flask(__name__)

# Load the pre-trained model from the .pkl file
model = joblib.load('model/model.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    # Get JSON data from the request
    data = request.json
    print(f"Received data: {data}")

    # Create a DataFrame with the correct feature names
    features = pd.DataFrame([data], columns=['SMA_50', 'SMA_200'])
    print(f"Extracted features: {features}")

    # Use the pre-trained model to make a prediction
    prediction = model.predict(features)
    print(f"Prediction: {prediction[0]}")

    # Return the prediction as a JSON response
    return jsonify({'prediction': float(prediction[0])})

if __name__ == '__main__':
    # Run the Flask app
    app.run(port=5000)

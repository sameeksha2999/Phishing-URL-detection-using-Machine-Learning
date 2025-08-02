import pandas as pd
import joblib

# Load the trained model
model = joblib.load("phishing_model.pkl")

# Function to predict URL type
def predict_url(url):
    # Example feature extraction - very basic for now
    features = [len(url), url.count('.'), url.count('-'), 'https' in url]
    prediction = model.predict([features])
    return "Phishing" if prediction[0] == 1 else "Legitimate"

# Simple test
if  __name__ == "_main_":
    user_url = input("Enter a URL to check: ")
    result = predict_url(user_url)
    print(f"The URL is likely: {result}")
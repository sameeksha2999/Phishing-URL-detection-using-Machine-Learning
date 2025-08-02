import pandas as pd
import pickle
from model import extract_features

# Load the trained model
with open('phishing_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Load URLs from input CSV
df = pd.read_csv('urls.csv')  # Make sure this file has a 'url' column
urls = df['url']

# Predict and collect results
results = []
for url in urls:
    features = extract_features(url)
    result = model.predict([features])[0]
    results.append({'url': url, 'prediction': 'Phishing' if result == 1 else 'Legitimate'})

# Save to CSV
output_df = pd.DataFrame(results)
output_df.to_csv('predictions.csv', index=False)

print("✅ Predictions saved to 'predictions.csv'")

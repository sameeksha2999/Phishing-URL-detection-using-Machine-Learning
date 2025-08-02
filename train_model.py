import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib
from urllib.parse import urlparse

# Feature extraction function
def extract_features(url):
    return [
        len(url),
        url.count('.'),
        url.count('-'),
        int('https' in url),
        int('@' in url),
        int(len(urlparse(url).netloc) > 15)
    ]

# Load dataset
df = pd.read_csv("dataset.csv")

# Generate features
X = df['url'].apply(extract_features).tolist()
y = df['label']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save model
joblib.dump(model, "phishing_model.pkl")
print("✅ Model trained and saved as phishing_model.pkl.")

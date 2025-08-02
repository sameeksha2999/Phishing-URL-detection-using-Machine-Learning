import pandas as pd
import pickle
from urllib.parse import urlparse
import re
from sklearn.ensemble import RandomForestClassifier

# --------- Feature Extraction Function ---------
def extract_features(url):
    import re
import urllib.parse

def extract_features(url):
    parsed_url = urllib.parse.urlparse(url)
    domain = parsed_url.netloc
    path = parsed_url.path

    return [
        len(url),
        url.count('.'),
        url.count('-'),
        url.count('@'),
        url.count('https'),
        len(domain),
        len(path),
        1 if re.search(r'\d+\.\d+\.\d+\.\d+', domain) else 0,  # IP address
        domain.count('.') - 1,  # subdomain count
        1 if any(short in url for short in ['bit.ly', 'tinyurl.com', 'goo.gl']) else 0  # shortener
    ]
# --------- Load Dataset ---------
df = pd.read_csv('data.csv')
df = df.dropna(subset=['url', 'label'])  # drop rows with missing URL or label

X = [extract_features(url) for url in df['url']]
y = df['label']  # This should be 0 for Legitimate, 1 for Phishing

# --------- Train Model ---------
model = RandomForestClassifier()
model.fit(X, y)

# --------- Save Model ---------
with open('phishing_model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("✅ Model trained and saved to phishing_model.pkl")

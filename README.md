🛡 Phishing URL Detection Using Machine Learning

🚀 A complete machine learning project with a real-time desktop application to detect phishing URLs using Python.
 

📌 Project Overview
This project focuses on building a phishing URL detector using machine learning and deploying it with a Tkinter-based GUI. The model analyzes structural patterns in URLs to determine whether they are legitimate or phishing.

The system supports both real-time predictions via a graphical interface and bulk URL analysis using CSV files. It demonstrates practical application of ML in the domain of cybersecurity.


🎯 Objectives
Detect phishing websites based on URL features
Train a predictive ML model with labeled data
Design a GUI for user interaction
Provide functionality for bulk URL prediction


🧠 Technologies Used
🐍 Python
🧪 scikit-learn
📊 pandas
💾 joblib
🖼 Tkinter (GUI)


🗂 Project Structure

📁 phishing-url-detector/
├── gui_app.py            → GUI application (main interface)
├── train_model.py        → Trains and saves the ML model
├── model.py              → Feature extraction & prediction logic
├── bulk_predict.py       → CSV-based bulk prediction
├── phishing_model.pkl    → Pretrained ML model
├── data.csv              → Training dataset
├── urls.csv              → Sample test URLs



⚙ How to Run the Project
✅ Step 1: Install Dependencies
Make sure Python is installed, then run:
pip install pandas scikit-learn joblib



✅ Step 2: Run the GUI Application
python gui_app.py
A window will open. Enter a URL and click "Check URL" to see the result.


🔁 Optional: Retrain the Model
python train_model.py
This will use data.csv to retrain the model and update phishing_model.pkl.


📂 Optional: Bulk Prediction
python bulk_predict.py
Make sure urls.csv contains a list of URLs to evaluate.


🔎 Example URLs to Test

✅ https://www.google.com
⚠ http://secure-login-alert.ru
✅ https://github.com
⚠ http://verify-paypal-login.in



🎓 Learning Outcomes
Applied machine learning for a real-world problem
Extracted and engineered URL-based features
Built and deployed a predictive model using scikit-learn
Created an interactive GUI using Python’s Tkinter library
Understood how phishing attempts can be detected programmatically


📌 Summary

This project highlights how machine learning can be applied to cybersecurity. It demonstrates the full development cycle from data preprocessing to user-friendly deployment, making it a practical and educational tool for understanding phishing detection.

import tkinter as tk
from tkinter import messagebox
import pickle
from model import extract_features

# Load the trained model
with open('phishing_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Predict Function
def check_url():
    url = url_entry.get().strip()
    if not url:
        messagebox.showwarning("Input Error", "Please enter a URL.")
        return
    try:
        features = extract_features(url)
        prediction = model.predict([features])[0]
        if prediction == 1:
            result_label.config(text="⚠ Phishing URL", fg="red")
        else:
            result_label.config(text="✅ Legitimate URL", fg="green")
    except Exception as e:
        messagebox.showerror("Error", f"Something went wrong:\n{e}")

# GUI Setup
window = tk.Tk()
window.title("Phishing URL Detector")
window.geometry("400x200")
window.configure(bg="#f4f4f4")

title = tk.Label(window, text="🔍 Phishing URL Detector", font=("Arial", 16), bg="#f4f4f4")
title.pack(pady=10)

url_entry = tk.Entry(window, width=50)
url_entry.pack(pady=5)

check_button = tk.Button(window, text="Check URL", command=check_url)
check_button.pack(pady=10)

result_label = tk.Label(window, text="", font=("Arial", 14), bg="#f4f4f4")
result_label.pack(pady=10)

window.mainloop()

import joblib
model = joblib.load("model.pkl")

import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import re
import pandas as pd

# --- Assume model and clean_text() are already defined above ---

# Function to predict abuse
def predict_message_gui(message):
    msg_df = pd.DataFrame({'tweet': [message]})
    msg_df = clean_text(msg_df, 'tweet')
    prediction = model.predict(msg_df['tweet'])[0]
    return 'Abusive' if prediction == 1 else 'Safe'

# Function to detect privacy breach
def detect_privacy_leak(message):
    phone_regex = r"\b\d{10}\b"
    email_regex = r"\b\S+@\S+\.\S+\b"
    return re.findall(phone_regex, message) + re.findall(email_regex, message)

# GUI Functionality
def analyze_message():
    message = entry.get()
    abuse_result = predict_message_gui(message)
    privacy_info = detect_privacy_leak(message)
    
    abuse_label['text'] = f"Abuse Detection: {abuse_result}"
    abuse_label['fg'] = 'red' if abuse_result == 'Abusive' else 'green'
    
    if privacy_info:
        privacy_label['text'] = f"Privacy Breach: {', '.join(privacy_info)}"
        privacy_label['fg'] = 'orange'
    else:
        privacy_label['text'] = "No privacy issue."
        privacy_label['fg'] = 'green'
    
    # Logging
    log_message(message, abuse_result, privacy_info)

# Function to log message
def log_message(msg, abuse, leaks):
    log_entry = f"{datetime.now()},\"{msg}\",{abuse},{';'.join(leaks) if leaks else 'None'}\n"
    with open("cybershield_logs.csv", "a", encoding='utf-8') as f:
        f.write(log_entry)

# GUI setup
root = tk.Tk()
root.title("CyberShield: Online Safety Assistant")

tk.Label(root, text="Enter message:", font=("Helvetica", 12)).pack(pady=5)

entry = tk.Entry(root, width=70)
entry.pack(pady=5)

tk.Button(root, text="Analyze", command=analyze_message, bg="blue", fg="white").pack(pady=5)

abuse_label = tk.Label(root, text="Abuse Detection: ", font=("Helvetica", 12))
abuse_label.pack()

privacy_label = tk.Label(root, text="Privacy Breach: ", font=("Helvetica", 12))
privacy_label.pack()

# Report and Block buttons (demo purpose only)
def report():
    messagebox.showinfo("Reported", "User has been reported.")

def block():
    messagebox.showinfo("Blocked", "User has been blocked.")

btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Report", command=report, bg="red", fg="white").grid(row=0, column=0, padx=10)
tk.Button(btn_frame, text="Block", command=block, bg="black", fg="white").grid(row=0, column=1, padx=10)

root.mainloop()

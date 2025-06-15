##  CyberShield: Smart Online Safety Assistant

> AI-powered tool to detect and flag abusive content for safer digital interactions.



**CyberShield** – An AI-powered desktop tool that helps detect and flag online abuse, enabling users to take safety actions like blocking and reporting. Built for enhancing safety in digital communication platforms.




###  2. Project Description

CyberShield is an intelligent local assistant that identifies potentially harmful or abusive text content using a trained machine learning model. It provides a simple graphical interface to classify messages, and if necessary, allows users to take quick action—like logging the incident, getting help, or blocking the sender.

The project combines natural language processing (NLP) with a Tkinter GUI to create a lightweight safety application that works offline, offering privacy and speed.

Core Features:
1. AI-Powered Abuse Detection
Uses a trained NLP model to classify messages as abusive or non-abusive.
Model trained using SGDClassifier on real-world labeled tweets.

2. Text Cleaning & Preprocessing
Automatically cleans input text by removing:

Mentions (e.g., @username)

URLs

Special characters

Case inconsistencies

Helps standardize data before classification.

3. Data Balancing (Upsampling)
Ensures fair model training by balancing abusive and non-abusive samples using resample() from scikit-learn.

4. High Accuracy
Achieves an impressive F1 score of ~0.97, indicating reliable performance in real-world use cases.

GUI Features:

5. Interactive Desktop Interface (Tkinter)
Clean, simple GUI built with Tkinter.

Input any sentence to instantly get a classification.

Visual cues to show results ("Abusive" / "Not Abusive").

6. Real-Time Message Analysis
Classifies messages on-the-fly.

Could be extended to monitor messages in live chat applications.

Potential Features to Add:
7. User Reporting and Blocking System
Ability to report, block, or mute users after detecting abuse.

8. Real-Time Monitoring Dashboard
Live stream of flagged messages, users, or accounts.

9. Context-Aware Learning
Enhances abuse detection by analyzing tone, context, or repeated behavior.

10. Multilingual Support
Detect abusive content across different Indian and international languages.

11. Integration with Social Platforms
APIs to connect with Twitter, Instagram, or Discord to auto-monitor DMs or posts.

####  Why These Technologies?

* **Python** for rapid development and robust NLP ecosystem
* **Scikit-learn** for fast, interpretable ML modeling
* **Tkinter** for cross-platform GUI without external dependencies
* **Pandas/CSV** for quick logging and audit trails

####  Challenges & Future Enhancements

* Improving accuracy on nuanced or coded abuse
* Integrating real-time chat app monitoring
* Moving to a Transformer-based model (e.g., BERT)
* Deploying as a browser plugin or mobile app


###  4. How to Install and Run the Project

####  Requirements:

* Python 3.8+
* Libraries: `pandas`, `scikit-learn`, `joblib`

#### 🔧 Setup:

1. Clone the repository or download the ZIP.
2. Install dependencies:

```bash
pip install pandas scikit-learn
```

3. Ensure `model.pkl` (your trained model) is in the same folder as `cybershield_gui.py`.
4. Run the GUI:

```bash
python cybershield_gui.py
```

> You can train and export your model using the code in your Colab notebook:

```python
import joblib
joblib.dump(model, 'model.pkl')

### 🖱️ 5. How to Use the Project

1. Launch the application.
2. Paste or type a message into the input box.
3. Click **“Classify”** to check if the message is abusive.
4. If flagged:

   * Choose **“Block”**, **“Report”**, or **“Get Help”**.
   * The entry is logged in `cybershield_logs.csv`.


#### 📚 References:

* Kaggle Datasets on Online Harassment & Hate Speech
* [Scikit-learn Documentation](https://scikit-learn.org/stable/documentation.html)
* [Tkinter GUI Guide](https://docs.python.org/3/library/tkinter.html)

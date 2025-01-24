# Sentiment Analysis Web App

A Flask powered web app that classifies text sentiment as **Positive** or **Negative** using a machine learning model (Logistic Regression) trained on an IMDb dataset of 50,000 movies reviews. 

Disclaimer: This project represents my initial dive into machine learning. It probably contains inaccuracies and / or suboptimal coding patterns. Please treat this repository as a learning experiment and avoid using it as a reference for any production or critical work whatsoever. Feedback is welcome!

---

## Table of Contents

1. [Project Overview](#project-overview)
2. [Quick Start](#quick-start)  
3. [Usage](#usage)
4. [Quick Start](#quick-start)  
5. [How It Works](#how-it-works)  
6. [To Do](#to-do)

---

## Project Overview

This project aims to showcase an ML pipeline for sentiment analysis on text data.

Key steps involved:
- Data loading and exploratory data analysis (EDA).
- Text preprocessing (cleaning, tokenization).
- Model building using scikit-learn (Logistic Regression).
- Saving the model and vectorizer to disk.
- Deploying a Flask web app to serve predictions.

---

### Quick Start

```bash
# 1. Clone
git clone https://github.com/your-username/my_sentiment_app.git

# 2. Run the Flask app
python app.py

# 3. Visit in your browser
http://127.0.0.1:5000
```

---

## Usage

1. **Run the Flask app**:
   ```bash
   python app.py
   ```
2. **Open a web browser** and go to `http://127.0.0.1:5000/`.
3. **Enter your text** in the input box and click **Analyze**.
4. The sentiment (e.g., “Positive” / “Negative”) is displayed on the results page.

---

## How It Works

1. **Data Preprocessing**:
   - Removes noise (lowercasing, etc.).
   - Uses `TfidfVectorizer` to transform text into numerical vectors. (Tfidf is not ideal for this case but was simple to use for this example)
2. **Model Training**:
   - `LogisticRegression` class from scikit-learn is trained on 80% of the dataset; 20% is used for testing.
   - Accuracy is reported on the test set.
3. **Model Saving**:
   - The trained `LogisticRegression` model and `TfidfVectorizer` are pickled using `joblib.dump()`.
4. **Flask Inference**:
   - On page load, `app.py` loads the model and vectorizer.
   - When user inputs text and hits “Analyze,” the text is vectorized (`vectorizer.transform()`) and passed to the model’s `.predict()` method.
   - The result is returned and displayed on a new page.

---

## To Do

- **Replace scikit-learn with Tensorflow**
- **Tokenization Improvements**: Use better tokenization
- **User Interface**: Build better UI, maybe React frontend
- **Deployment**: Deploy to Heroku
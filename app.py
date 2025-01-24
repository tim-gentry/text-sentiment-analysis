from flask import Flask, request, render_template
import joblib

app = Flask(__name__)

model = joblib.load('./models/sentiment_model.pkl')
vectorizer = joblib.load('./models/vectorizer.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    user_text = request.form['user_text']

    user_text_features = vectorizer.transform([user_text])

    prediction = model.predict(user_text_features)[0]

    return render_template('result.html', prediction=prediction, text=user_text)

if __name__ == '__main__':
    app.run(debug=True)
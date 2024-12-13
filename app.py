from flask import Flask, render_template, request,redirect, url_for
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.preprocessing.text import tokenizer_from_json

app = Flask(__name__)

# Load the trained model
model = load_model('model.h5')

# Load the tokenizer
with open('tokenizer.json', 'r') as f:
    tokenizer = tokenizer_from_json(f.read())

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        url = request.form['url']
        return redirect(url_for('loading', url=url))
    return render_template('index.html')
    
@app.route('/loading')
def loading():
    url = request.args.get('url')
    return redirect(url_for('predict', url=url))

@app.route('/predict', methods=['POST'])
def predict():
    review = request.form['review']
    sequence = tokenizer.texts_to_sequences([review])
    padded_sequence = pad_sequences(sequence, maxlen=100)
    prediction = model.predict(padded_sequence)
    category = 'good product' if prediction > 0.5 else 'worst product'
    return render_template('result.html', review=review, category=category)

if __name__ == '__main__':
    app.run(debug=True)

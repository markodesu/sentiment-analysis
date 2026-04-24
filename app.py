from flask import Flask, render_template, request, jsonify
import joblib
import os
from src.preprocess import clean_text

app = Flask(__name__)

# Load the trained model and vectorizer
model_path = 'outputs/sentiment_model.pkl'
vectorizer_path = 'outputs/vectorizer.pkl'

if os.path.exists(model_path) and os.path.exists(vectorizer_path):
    model = joblib.load(model_path)
    vectorizer = joblib.load(vectorizer_path)
else:
    model = None
    vectorizer = None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json
        review_text = data.get('text', '').strip()
        
        if not review_text:
            return jsonify({'error': 'Please enter some text'}), 400
        
        if model is None or vectorizer is None:
            return jsonify({'error': 'Model not loaded. Please train the model first.'}), 500
        
        # Preprocess the text
        cleaned_text = clean_text(review_text)
        
        # Vectorize
        features = vectorizer.transform([cleaned_text])
        
        # Predict
        prediction = model.predict(features)[0]
        confidence = max(model.predict_proba(features)[0])
        
        # Get probability for each class
        proba = model.predict_proba(features)[0]
        class_names = model.classes_
        
        probabilities = {
            class_names[i]: float(proba[i]) * 100 
            for i in range(len(class_names))
        }
        
        # Determine emoji and color based on sentiment
        emoji_map = {
            'positive': '😊',
            'negative': '😢',
            'neutral': '😐'
        }
        
        color_map = {
            'positive': '#4CAF50',
            'negative': '#f44336',
            'neutral': '#FF9800'
        }
        
        return jsonify({
            'sentiment': prediction,
            'confidence': round(confidence * 100, 2),
            'emoji': emoji_map.get(prediction, '🤔'),
            'color': color_map.get(prediction, '#2196F3'),
            'probabilities': probabilities,
            'cleaned_text': cleaned_text
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)

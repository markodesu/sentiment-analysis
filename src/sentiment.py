from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib
import os

def train_sentiment_model(data):
    # Map ratings to sentiment labels
    def rating_to_sentiment(rating):
        if rating <= 2:
            return 'negative'
        elif rating == 3:
            return 'neutral'
        else:
            return 'positive'
    
    data['label'] = data['rating'].apply(rating_to_sentiment)
    
    # Vectorize text
    vectorizer = TfidfVectorizer(max_features=5000, stop_words='english')
    X = vectorizer.fit_transform(data['clean_text'])
    y = data['label']
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Train model
    model = LogisticRegression(random_state=42)
    model.fit(X_train, y_train)
    
    # Evaluate
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Model accuracy: {accuracy:.2f}")
    
    # Save model and vectorizer
    joblib.dump(model, 'outputs/sentiment_model.pkl')
    joblib.dump(vectorizer, 'outputs/vectorizer.pkl')
    
    return model, vectorizer

def get_sentiment(text, model=None, vectorizer=None):
    if model is None:
        if os.path.exists('outputs/sentiment_model.pkl'):
            model = joblib.load('outputs/sentiment_model.pkl')
            vectorizer = joblib.load('outputs/vectorizer.pkl')
        else:
            # Fallback to VADER
            from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
            analyzer = SentimentIntensityAnalyzer()
            score = analyzer.polarity_scores(text)
            compound = score['compound']
            if compound > 0.05:
                return 'positive'
            elif compound < -0.05:
                return 'negative'
            else:
                return 'neutral'
    
    X = vectorizer.transform([text])
    pred = model.predict(X)[0]
    return pred

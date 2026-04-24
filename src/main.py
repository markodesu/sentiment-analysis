from data_loader import load_data
from preprocess import clean_text
from sentiment import train_sentiment_model, get_sentiment
from trend import predict_trend

import matplotlib.pyplot as plt

# Load data
data = load_data("data/37000_reviews_of_thread_app.csv")

# Sort by date
data = data.sort_values('date').reset_index(drop=True)

# Clean text
data['clean_text'] = data['text'].apply(clean_text)

# Train sentiment model
model, vectorizer = train_sentiment_model(data)

# Sentiment analysis
data['sentiment'] = data['clean_text'].apply(lambda x: get_sentiment(x, model, vectorizer))

# For trend, map to numeric
sentiment_map = {'negative': -1, 'neutral': 0, 'positive': 1}
data['sentiment_score'] = data['sentiment'].map(sentiment_map)

# Prediction
prediction = predict_trend(data)

print("Predicted sentiment score for next day:", prediction)

# Plot daily averages
daily_sentiment = data.groupby(data['date'].dt.date)['sentiment_score'].mean().reset_index()
plt.figure(figsize=(10, 6))
plt.plot(daily_sentiment['date'], daily_sentiment['sentiment_score'], marker='o', linestyle='-')
plt.xticks(rotation=45)
plt.title("Daily Sentiment Trend Over Time")
plt.xlabel("Date")
plt.ylabel("Average Sentiment Score")
plt.grid(True)
plt.savefig('outputs/sentiment_trend.png')
# plt.show()  # Comment out to avoid timeout

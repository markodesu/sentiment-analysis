from sklearn.linear_model import LinearRegression
import numpy as np
import pandas as pd

def predict_trend(data):
    # Group by date and average sentiment
    daily_sentiment = data.groupby(data['date'].dt.date)['sentiment_score'].mean().reset_index()
    daily_sentiment['day'] = range(len(daily_sentiment))

    X = daily_sentiment[['day']]
    y = daily_sentiment['sentiment_score']

    model = LinearRegression()
    model.fit(X, y)

    next_day = np.array([[len(daily_sentiment)]])
    prediction = model.predict(next_day)

    return prediction[0]

# Sentiment Trend Analysis for Threads App

This project analyzes sentiment in Threads app reviews and predicts future trends.

## Setup

1. Create virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the main script:
```bash
python3 src/main.py
```

This will:
- Load and clean the dataset
- Train a sentiment classification model
- Analyze daily sentiment trends
- Predict next day's sentiment
- Save a trend plot to `outputs/sentiment_trend.png`

## Files

- `src/main.py`: Main execution script
- `src/data_loader.py`: Data loading and cleaning
- `src/preprocess.py`: Text preprocessing
- `src/sentiment.py`: Sentiment analysis model
- `src/trend.py`: Trend prediction
- `data/37000_reviews_of_thread_app.csv`: Dataset
- `outputs/`: Model files and plots
- `SRS.md`: Software Requirements Specification
- `Task_Distribution.md`: Team task assignments

## Results

- Model accuracy: ~79%
- Daily sentiment trends visualized
- Linear regression prediction for future sentiment
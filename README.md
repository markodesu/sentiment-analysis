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

### Option 1: Run the Analysis Pipeline

```bash
python3 src/main.py
```

This will:
- Load and clean the dataset
- Train a sentiment classification model
- Analyze daily sentiment trends
- Predict next day's sentiment
- Save a trend plot to `outputs/sentiment_trend.png`

### Option 2: Launch Interactive Web Interface

```bash
python3 app.py
```

Then open your browser and navigate to:
```
http://localhost:5000
```

The web interface allows you to:
- Enter custom text or reviews
- See real-time sentiment predictions
- View confidence scores and probability distributions
- Explore preprocessed text
- Test the model with example inputs

### Option 3: Launch Interactive Jupyter Notebook

```bash
jupyter notebook notebooks/analysis.ipynb
```

This notebook provides a step-by-step walkthrough of:
- Data loading and exploration
- Data cleaning and preprocessing
- Feature engineering
- Model training and evaluation
- Visualization and insights

## Files

- `src/main.py`: Main execution script
- `src/data_loader.py`: Data loading and cleaning
- `src/preprocess.py`: Text preprocessing
- `src/sentiment.py`: Sentiment analysis model training
- `src/trend.py`: Trend prediction
- `app.py`: Flask web application
- `templates/index.html`: Interactive web interface
- `data/37000_reviews_of_thread_app.csv`: Dataset
- `outputs/`: Model files and plots
- `notebooks/analysis.ipynb`: Interactive analysis notebook
- `SRS.md`: Software Requirements Specification
- `Task_Distribution.md`: Team task assignments
- `COMPREHENSIVE_REPORT.md`: Full project report

## Results

- Model accuracy: ~79%
- Daily sentiment trends visualized
- Linear regression prediction for future sentiment
- Interactive web demo for real-time testing

## Project Structure

```
sentiment-trend-project/
├── app.py
├── Dockerfile
├── Procfile
├── README.md
├── requirements.txt
├── runtime.txt
├── .env.example
├── .dockerignore
├── data/
│   └── 37000_reviews_of_thread_app.csv
├── docs/
│   ├── COMPREHENSIVE_REPORT.md
│   ├── DEPLOYMENT_GUIDE.md
│   ├── PRESENTATION_SLIDES.md
│   ├── SRS.md
│   ├── Task_Distribution.md
│   └── AI reqs
├── notebooks/
│   └── analysis.ipynb
├── outputs/
│   ├── sentiment_model.pkl
│   ├── vectorizer.pkl
│   └── sentiment_trend.png
├── src/
│   ├── main.py
│   ├── data_loader.py
│   ├── preprocess.py
│   ├── sentiment.py
│   └── trend.py
├── templates/
│   └── index.html
└── README.md
```
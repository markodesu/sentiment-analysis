# Software Requirements Specification (SRS)

## 1. Introduction

### 1.1 Purpose
This document specifies the requirements for the AI Sentiment Analysis and Trend Prediction System for Threads social media platform reviews. The system analyzes user reviews to determine sentiment and predict future trends.

### 1.2 Scope
The system will:
- Load and preprocess review data from Google Play Store
- Perform sentiment analysis on review text
- Track sentiment trends over time
- Predict future sentiment trends using machine learning
- Visualize results

### 1.3 Definitions
- Sentiment: Positive, negative, or neutral opinion expressed in text
- Trend: Pattern of sentiment change over time
- Prediction: Forecast of future sentiment based on historical data

## 2. Overall Description

### 2.1 Product Perspective
The system is a standalone Python application that processes CSV data of app reviews. It uses NLP for sentiment analysis and ML for trend prediction.

### 2.2 Product Functions
- Data loading and cleaning
- Text preprocessing
- Sentiment scoring
- Trend analysis and visualization
- Future trend prediction

### 2.3 User Characteristics
- Computer Science students: Technical users who understand code
- Communications/Media students: Domain experts who interpret results

### 2.4 Constraints
- Data limited to English reviews from US users
- Time period: July-August 2023
- Simple ML models as per course requirements

## 3. Specific Requirements

### 3.1 External Interface Requirements

#### 3.1.1 User Interfaces
- Command-line interface for running the system
- Matplotlib plots for visualization

#### 3.1.2 Software Interfaces
- Python 3.10+
- Libraries: pandas, vaderSentiment, scikit-learn, matplotlib

### 3.2 Functional Requirements

#### 3.2.1 Data Loading
- Load CSV file with review data
- Clean and preprocess data (remove missing values, combine title/description)

#### 3.2.2 Text Preprocessing
- Convert to lowercase
- Remove URLs and special characters
- Keep only alphabetic characters and spaces

#### 3.2.3 Sentiment Analysis
- Use VADER sentiment analyzer
- Return compound sentiment score (-1 to 1)

#### 3.2.4 Trend Analysis
- Group reviews by date
- Calculate daily average sentiment

#### 3.2.5 Prediction
- Use linear regression on daily sentiment over time
- Predict next day's average sentiment

#### 3.2.6 Visualization
- Plot daily sentiment trend
- Show predicted value

### 3.3 Non-Functional Requirements

#### 3.3.1 Performance
- Process 37,000 reviews in under 5 minutes

#### 3.3.2 Reliability
- Handle missing data gracefully
- Accurate sentiment analysis (>80% correlation with ratings)

#### 3.3.3 Usability
- Clear code structure and documentation
- Easy to run and interpret results

#### 3.3.4 Security
- No sensitive data handling

## 4. Appendices

### 4.1 Data Dictionary
- text: Review description (string)
- rating: User rating (1-5)
- date: Review date (datetime)
- sentiment: Compound score (-1 to 1)

### 4.2 Assumptions
- All reviews are in English
- Data is from reliable source (Kaggle)
- Linear trend assumption holds</content>
<parameter name="filePath">/home/student/projects/sentiment-trend-project/SRS.md
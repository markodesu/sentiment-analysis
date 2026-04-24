# Presentation Slides: Sentiment Analysis & Trend Prediction System

**Date:** April 27, 2026  
**Course:** COMP1073 - Introduction to Computer Science  
**Team:** 3 CS Students + 2 Communications/Media Students  
**Topic:** AI Sentiment Analysis + Trend Prediction for Threads App Reviews

---

## Slide 1: Title Slide

### Speech:
"Good morning everyone. Today we're excited to present our AI-powered sentiment analysis and trend prediction system for the Threads social media platform. This project demonstrates how artificial intelligence can transform user feedback into actionable business intelligence. My name is [Your Name], and I'm joined by my teammates [Team Member Names]."

### Bullet Points:
- **Project Title:** Sentiment Analysis & Trend Prediction System
- **Platform:** Threads Social Media App
- **Team:** 3 Computer Science + 2 Communications/Media Students
- **Course:** COMP1073 - Introduction to Computer Science
- **Date:** April 27, 2026

### Canva AI Prompt:
"Create a modern, professional title slide with a purple gradient background. Include the title 'Sentiment Analysis & Trend Prediction System' in large white text, subtitle 'Threads Social Media Platform' in smaller text, team names and course info at the bottom. Add subtle social media icons (threads logo, AI brain icon) in the corners. Use clean, modern typography."

---

## Slide 2: Problem Statement

### Speech:
"Imagine you're Meta, the company behind Threads. In the first month of launch, you receive 36,943 reviews on the Google Play Store. How do you understand what users really think? How do you predict if sentiment will improve or decline? Traditional methods of reading reviews manually are impossible at this scale. This is the problem our AI system solves."

### Bullet Points:
- **Challenge:** 36,943 reviews in first month - impossible to analyze manually
- **Business Need:** Understand user sentiment and predict trends
- **Current Methods:** Time-consuming, subjective, incomplete
- **Our Solution:** AI-powered automated sentiment analysis and prediction

### Canva AI Prompt:
"Create a problem-solution slide with a split design. Left side shows a confused person surrounded by piles of paper (representing reviews), right side shows a clean dashboard with graphs and AI icons. Use red tones for the problem side, green for the solution. Include the question 'How do we analyze 36,943 reviews?' prominently."

---

## Slide 3: System Overview

### Speech:
"Our system is an end-to-end AI pipeline that takes raw review text and produces sentiment insights and trend predictions. It starts with data collection, moves through preprocessing and AI analysis, and ends with visualizations and predictions. The system is built with Python and uses machine learning algorithms to classify sentiment and predict future trends."

### Bullet Points:
- **Input:** Raw review text from Google Play Store
- **Process:** Data cleaning → Text preprocessing → AI analysis → Prediction
- **Output:** Sentiment scores, trend graphs, future predictions
- **Technology:** Python, Flask, scikit-learn, TF-IDF, Logistic Regression
- **Architecture:** Modular design with separate components for each step

### Canva AI Prompt:
"Create a flowchart-style slide showing the system architecture. Use a horizontal flow from left to right: Raw Data → Cleaning → Preprocessing → AI Model → Results. Include icons for each step (database, cleaning brush, gears, brain, charts). Use blue and purple color scheme with connecting arrows."

---

## Slide 4: Data Analysis Overview

### Speech:
"We analyzed 36,943 reviews from July 5 to August 7, 2023 - the critical first month of Threads' launch. The data shows a polarized user base with strong opinions. 46% of users rated 5 stars, while 31% rated 1 star. This polarization indicates users either love the platform or hate it - there's little middle ground."

### Bullet Points:
- **Dataset Size:** 36,943 reviews
- **Time Period:** July 5 - August 7, 2023 (34 days)
- **Geographic Scope:** United States users only
- **Rating Distribution:**
  - 5 stars: 46% (17,000 reviews)
  - 1 star: 31% (11,282 reviews)
  - 3 stars: 8% (neutral opinions)
- **Key Insight:** Highly polarized user base

### Canva AI Prompt:
"Create a data visualization slide with a large bar chart showing rating distribution (1-5 stars). Use purple bars, include percentage labels on each bar. Add a world map highlighting the US. Include key statistics in text boxes. Use a clean, data-focused design with subtle background pattern."

---

## Slide 5: Data Cleaning Process

### Speech:
"Data cleaning is crucial for AI accuracy. Our system removes irrelevant information, handles missing values, and standardizes text. For example, we combine review titles with descriptions, remove URLs and special characters, and convert everything to lowercase. This ensures our AI model focuses on meaningful content rather than formatting noise."

### Bullet Points:
- **Step 1:** Remove unnecessary columns (developer responses, app versions)
- **Step 2:** Handle missing values (fill thumbs_up with 0)
- **Step 3:** Combine title + description into single text field
- **Step 4:** Text normalization (lowercase, remove URLs, special characters)
- **Result:** Clean, standardized text ready for AI analysis

### Canva AI Prompt:
"Create a step-by-step process slide with 4 circular icons connected by arrows. Each circle represents a cleaning step with a simple icon (trash can for removal, merge icon for combining, brush for cleaning, checkmark for result). Use green-to-blue gradient background. Include brief descriptions under each step."

---

## Slide 6: AI Model Architecture

### Speech:
"At the heart of our system is a machine learning model trained on 36,943 reviews. We use TF-IDF vectorization to convert text into numerical features, then train a logistic regression classifier. The model achieves 79% accuracy in classifying reviews as positive, negative, or neutral. This is the same technology used by companies like Netflix and Amazon for recommendation systems."

### Bullet Points:
- **Text Vectorization:** TF-IDF transforms text into 5,000 numerical features
- **Algorithm:** Logistic Regression (proven, interpretable)
- **Training Data:** 80% of reviews (29,554 samples)
- **Testing Data:** 20% of reviews (7,389 samples)
- **Performance:** 79% accuracy, 63% precision for neutral class
- **Model Size:** 2.1 MB (efficient for deployment)

### Canva AI Prompt:
"Create a technical architecture slide with a central 'brain' icon representing the AI model. Show input (text reviews) flowing into TF-IDF vectorization, then into the logistic regression model, outputting sentiment predictions. Include accuracy metrics in floating text boxes. Use tech-inspired colors (blues, greens) with circuit board pattern background."

---

## Slide 7: Sentiment Classification Results

### Speech:
"Our model successfully classifies sentiment with 79% accuracy. For positive reviews, it achieves 80% precision - meaning when it says a review is positive, it's correct 80% of the time. The model struggles most with neutral reviews, which is common since neutral opinions are ambiguous even for humans. Overall, this performance is excellent for a real-world application."

### Bullet Points:
- **Overall Accuracy:** 79%
- **Positive Reviews:** 80% precision, 84% recall
- **Negative Reviews:** 81% precision, 87% recall
- **Neutral Reviews:** 63% precision, 32% recall (challenging category)
- **Business Impact:** Reliable for identifying satisfied/dissatisfied users
- **Model Confidence:** Provides probability scores for each prediction

### Canva AI Prompt:
"Create a results slide with three colored bars (green for positive, red for negative, yellow for neutral) showing precision and recall metrics. Include a large '79%' accuracy badge. Add icons for each sentiment type (smiley face, sad face, neutral face). Use a clean, metric-focused design with subtle grid background."

---

## Slide 8: Trend Analysis

### Speech:
"Beyond individual reviews, we analyzed sentiment trends over time. User satisfaction declined from 3.15 stars in the first week to 2.88 stars by the final week - an 8.6% decrease. This suggests initial excitement wore off as users discovered limitations. We used linear regression to predict this trend would continue declining."

### Bullet Points:
- **Daily Analysis:** Aggregated sentiment by date
- **Trend Pattern:** Declining satisfaction over 34 days
- **Key Metrics:**
  - Week 1: 3.15 average rating
  - Week 4: 2.88 average rating
  - Change: -8.6%
- **Prediction Method:** Linear regression on daily averages
- **Business Insight:** Early adopter enthusiasm vs. long-term satisfaction

### Canva AI Prompt:
"Create a trend visualization slide with a line graph showing declining sentiment over time (July to August). Use purple line with data points. Include trend arrow pointing downward. Add key statistics in callout boxes. Background should be subtle grid with time markers. Include calendar icons for date range."

---

## Slide 9: Live Demonstration

### Speech:
"Now I'd like to show you our system in action. We'll use the live web interface to analyze some sample reviews. This demonstrates how anyone can use our AI without technical knowledge."

*[Open browser to live demo URL]*

### Bullet Points:
- **Demo URL:** [Insert live URL here]
- **Features:**
  - Real-time sentiment analysis
  - Confidence scores and probabilities
  - Preprocessed text display
  - Example reviews to try
- **User Experience:** Simple, intuitive interface
- **Technical Backend:** Flask API with trained ML model

### Canva AI Prompt:
"Create a demonstration slide with a mockup of the web interface (show the purple gradient design, input box, and result display). Include a 'LIVE DEMO' badge and arrow pointing to browser window. Add screenshots of the interface. Use action-oriented design with call-to-action styling."

---

## Slide 10: Business Insights

### Speech:
"What does this mean for Meta and the Threads platform? Our analysis reveals declining user satisfaction, with technical issues being the primary complaint. The platform retains a core audience of satisfied users, but needs to address bugs and missing features to prevent further decline. This type of analysis helps companies make data-driven decisions about product improvements."

### Bullet Points:
- **Key Findings:**
  - Declining sentiment trend (-8.6% over month)
  - Technical issues dominate complaints
  - Core user base remains satisfied
- **Business Recommendations:**
  - Prioritize bug fixes and stability
  - Add missing features quickly
  - Monitor sentiment trends weekly
- **Market Impact:** Early indicator of platform adoption challenges

### Canva AI Prompt:
"Create an insights slide with business-focused icons (lightbulb, chart, target). Use a split design: left side shows problems (red), right side shows solutions (green). Include key metrics and recommendations in bullet points. Add business-themed background with subtle dollar signs and graphs."

---

## Slide 11: Technical Implementation

### Speech:
"From a technical perspective, our system is built with modern Python tools. We used pandas for data processing, scikit-learn for machine learning, and Flask for the web interface. The model is trained on TF-IDF features and deployed as a REST API. This modular architecture makes it easy to maintain and scale."

### Bullet Points:
- **Tech Stack:**
  - Python 3.10, pandas, scikit-learn
  - Flask web framework
  - TF-IDF vectorization
  - Logistic regression algorithm
- **Code Structure:** Modular design (data_loader.py, sentiment.py, etc.)
- **Deployment:** Ready for cloud platforms (Render, Railway, PythonAnywhere)
- **Performance:** Processes 36,943 reviews in under 3 minutes
- **Scalability:** Can handle larger datasets with same architecture

### Canva AI Prompt:
"Create a technical slide with code-like elements. Show icons for Python, Flask, scikit-learn. Include a simplified code snippet in a code block style. Use developer-friendly colors (dark background with colored syntax highlighting). Add gear icons and technical diagrams."

---

## Slide 12: Challenges and Solutions

### Speech:
"Building this system wasn't without challenges. We faced issues with text preprocessing, model training time, and deployment complexity. For example, neutral reviews were hard to classify because they're inherently ambiguous. We solved this by using larger feature sets and careful validation."

### Bullet Points:
- **Challenge 1:** Text preprocessing complexity
  - **Solution:** Systematic cleaning pipeline
- **Challenge 2:** Neutral sentiment classification
  - **Solution:** Additional feature engineering
- **Challenge 3:** Model deployment
  - **Solution:** Flask API with proper error handling
- **Challenge 4:** Team coordination (CS + Media students)
  - **Solution:** Clear task division and regular meetings

### Canva AI Prompt:
"Create a challenges-solutions slide with a balance scale design. Left side shows challenges (red warning icons), right side shows solutions (green checkmark icons). Connect each challenge to its solution with arrows. Use a problem-solving theme with lightbulb icons and 'VS' divider."

---

## Slide 13: Ethical Considerations

### Speech:
"AI systems like ours raise important ethical questions. Our model could potentially be misused to manipulate reviews or spread misinformation. We designed our system with transparency in mind, showing users exactly how their text is processed and providing confidence scores. We also considered bias in our training data and the limitations of automated analysis."

### Bullet Points:
- **Transparency:** Shows preprocessed text and confidence scores
- **Bias Awareness:** US-only data may not represent global opinions
- **Privacy:** No personal data collection or storage
- **Limitations:** AI should supplement, not replace, human judgment
- **Responsible Use:** Designed for genuine business insights, not manipulation

### Canva AI Prompt:
"Create an ethics slide with balanced scales and ethical icons (shield, eye, balance). Use thoughtful colors (blues and greens). Include key ethical principles as bullet points. Add a subtle background pattern suggesting responsibility and transparency."

---

## Slide 14: Future Improvements

### Speech:
"Our system is a solid foundation, but there's always room for improvement. Future enhancements could include real-time analysis, multi-language support, and more advanced prediction models. We could also integrate with social media APIs for live monitoring."

### Bullet Points:
- **Short-term:** Add more example datasets, improve neutral classification
- **Medium-term:** Real-time analysis, multi-language support
- **Long-term:** Advanced models (BERT, LSTM), social media API integration
- **Scalability:** Handle millions of reviews with distributed processing
- **User Experience:** Mobile app, API for third-party integration

### Canva AI Prompt:
"Create a future vision slide with a timeline design. Show current state, near future, and long-term goals with icons. Use upward arrows and growth symbols. Include innovation-themed elements like rockets and lightbulbs. Background should suggest progress and expansion."

---

## Slide 15: Conclusion

### Speech:
"In conclusion, our sentiment analysis system successfully demonstrates how AI can transform user feedback into business intelligence. We processed 36,943 reviews, achieved 79% accuracy, and provided actionable insights about Threads' user sentiment. This project shows the real-world application of computer science concepts in solving business problems."

### Bullet Points:
- **Achievements:**
  - 79% accurate sentiment classification
  - Trend analysis over 34 days
  - Interactive web demonstration
  - Production-ready deployment
- **Learning Outcomes:**
  - Data processing and cleaning
  - Machine learning implementation
  - Web development and deployment
  - Cross-disciplinary collaboration
- **Impact:** Practical AI solution for real business needs

### Canva AI Prompt:
"Create a conclusion slide with a summary infographic. Show key metrics (79% accuracy, 36,943 reviews) in large badges. Include team photo or icons. Use celebratory colors (gold, blue) with checkmark icons. Add a call-to-action for questions."

---

## Slide 16: Q&A

### Speech:
"Thank you for your attention. We're now happy to take any questions about our system, the technical implementation, or the business insights we discovered."

### Bullet Points:
- **Questions Welcome About:**
  - Technical implementation details
  - Data analysis methodology
  - Business insights and recommendations
  - Future development plans
  - Team collaboration experience
- **Contact Information:**
  - GitHub: https://github.com/markodesu/sentiment-analysis
  - Live Demo: [Insert deployment URL]

### Canva AI Prompt:
"Create a Q&A slide with question mark icons and open discussion symbols. Include contact information prominently. Use an inviting, conversational design with speech bubbles and microphone icons. Background should be warm and welcoming."

---

## Presentation Notes

### Timing Guidelines:
- **Total Time:** 15-20 minutes presentation + 5-10 minutes Q&A
- **Slide Timing:** 45-60 seconds per slide
- **Demo Time:** 3-5 minutes for live demonstration

### Speaker Tips:
- Practice transitions between technical and business explanations
- Have live demo ready and tested
- Prepare for questions about model accuracy and limitations
- Emphasize real-world business value
- Show enthusiasm for the project

### Backup Plan:
- If live demo fails, show screenshots
- Have GitHub repository ready to share
- Prepare offline version of web interface

### Team Coordination:
- **CS Students:** Handle technical questions and code explanations
- **Media Students:** Handle business insights and presentation flow
- **All Members:** Understand high-level system overview

### Materials to Bring:
- Laptop with presentation
- Backup USB drive
- Printed handouts (optional)
- Business cards or contact info

---

## Canva Design Theme

**Overall Theme:** Modern, professional, tech-focused
**Color Palette:** Purple gradient (#667eea to #764ba2), white text, dark backgrounds
**Typography:** Clean sans-serif fonts, bold headings, readable body text
**Icons:** Social media, AI brain, data charts, technical gears
**Style:** Minimalist, data-driven, trustworthy and innovative

**Canva Template Suggestions:**
- Use "Modern Business" or "Tech Startup" templates
- Apply consistent color scheme across all slides
- Include subtle animations for data visualizations
- Add company logos and project branding

---

## Emergency Backup Slides

### Slide A: Technical Backup
*If technical demo fails, show this slide with screenshots*

### Slide B: Code Snippets
*Show key code examples for technical audience*

### Slide C: Alternative Demo
*Link to video demonstration if live demo unavailable*
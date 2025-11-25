
# Sentiment Analysis using NLTK

import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Make sure lexicon is available
nltk.download('vader_lexicon')

# Initialize analyzer
sia = SentimentIntensityAnalyzer()


# Example Text

text = "I love this product! It is amazing and works perfectly."

# Perform sentiment analysis
score = sia.polarity_scores(text)

print("Sentiment Scores:", score)


# Final classification

if score['compound'] >= 0.05:
    print("Overall Sentiment: Positive 😊")
elif score['compound'] <= -0.05:
    print("Overall Sentiment: Negative 😡")
else:
    print("Overall Sentiment: Neutral 😐")

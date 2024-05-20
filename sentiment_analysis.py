import warnings
from transformers import pipeline

def analyze_sentiment():
    # Suppress warnings
    warnings.filterwarnings("ignore")
    
    # Sentiment Analysis
    sentiment_classifier = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")
    user_input = input("Enter text to analyze sentiment: ")
    sentiment_result = sentiment_classifier(user_input)
    print("Sentiment Analysis Result:")
    for result in sentiment_result:
        print(f"The sentiment of the input is: {result['label']} with a confidence score of {result['score']}")

# Run the function
analyze_sentiment()

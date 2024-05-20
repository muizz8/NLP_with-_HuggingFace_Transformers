import warnings
from transformers import pipeline

def summarize_text():
    # Suppress warnings
    warnings.filterwarnings("ignore")
    
    # Text Summarization
    summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")
    user_input = input("Enter text to summarize: ")
    summary_result = summarizer(user_input)
    print("Text Summarization Result:")
    print(summary_result[0]['summary_text'])

# Run the function
summarize_text()

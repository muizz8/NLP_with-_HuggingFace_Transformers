from flask import Flask, render_template, request, jsonify
from transformers import MarianMTModel, MarianTokenizer, pipeline

app = Flask(__name__)

# Initialize sentiment classifier
sentiment_classifier = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

# Initialize translation models and tokenizers
translation_models = {
    "French": {
        "tokenizer": MarianTokenizer.from_pretrained("Helsinki-NLP/opus-mt-en-fr"),
        "model": MarianMTModel.from_pretrained("Helsinki-NLP/opus-mt-en-fr")
    },
    "Urdu": {
        "tokenizer": MarianTokenizer.from_pretrained("Helsinki-NLP/opus-mt-en-ur"),
        "model": MarianMTModel.from_pretrained("Helsinki-NLP/opus-mt-en-ur")
    }
}

# Initialize text summarization pipeline
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

# Initialize text generation pipeline
text_generator = pipeline("text-generation", model="gpt2")

@app.route('/')
def home():
    """Render the home page."""
    return render_template('results.html')

@app.route('/generate', methods=['POST'])
def generate_text():
    """Generate text based on user input."""
    user_input = request.json.get('user_input')
    generated_text = generate_text_function(user_input)
    return jsonify({'result': generated_text})

@app.route('/translate', methods=['POST'])
def translate_text():
    """Translate text based on user input and target language."""
    user_input = request.json.get('user_input')
    target_language = request.json.get('target_language')
    try:
        translated_text = translate_text_function(user_input, target_language)
        return jsonify({'result': translated_text})
    except ValueError as e:
        return jsonify({'error': str(e)}), 400

@app.route('/analyze', methods=['POST'])
def analyze_sentiment():
    """Analyze sentiment of user input."""
    user_input = request.json.get('user_input')
    sentiment_result = sentiment_classifier(user_input)
    return jsonify({'result': sentiment_result})

@app.route('/summarize', methods=['POST'])
def summarize_text():
    """Summarize user input text."""
    user_input = request.json.get('user_input')
    summary_result = summarizer(user_input)
    return jsonify({'result': summary_result[0]['summary_text']})

def translate_text_function(text, target_language):
    """Translate input text to the target language."""
    if target_language not in translation_models:
        raise ValueError(f"Unsupported target language: {target_language}")
    
    tokenizer = translation_models[target_language]["tokenizer"]
    model = translation_models[target_language]["model"]

    inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True)
    translated_tokens = model.generate(**inputs)
    translated_text = tokenizer.decode(translated_tokens[0], skip_special_tokens=True)
    return translated_text

    

    tokenizer = translation_models[target_language]["tokenizer"]
    model = translation_models[target_language]["model"]

    inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True)
    translated_tokens = model.generate(**inputs)
    translated_text = tokenizer.decode(translated_tokens[0], skip_special_tokens=True)
    return translated_text

def generate_text_function(prompt):
    """Generate text based on user prompt."""
    generated_text = text_generator(prompt, max_length=100, num_return_sequences=1, do_sample=True)[0]['generated_text']
    return generated_text

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)

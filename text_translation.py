from transformers import MarianMTModel, MarianTokenizer

def translate_text(text, target_language):
    # Define model name based on the target language
    if target_language == "French":
        model_name = "Helsinki-NLP/opus-mt-en-fr"
    elif target_language == "Urdu":
        model_name = "Helsinki-NLP/opus-mt-en-ur"

    # Load translation model and tokenizer
    model = MarianMTModel.from_pretrained(model_name)
    tokenizer = MarianTokenizer.from_pretrained(model_name)

    # Tokenize the input text
    inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True)

    # Perform translation
    translated_tokens = model.generate(**inputs)

    # Decode the translated tokens
    translated_text = tokenizer.decode(translated_tokens[0], skip_special_tokens=True)
    return translated_text

def main():
    target_language = input("Enter the target language (French/Urdu): ").capitalize()
    if target_language not in ["French", "Urdu"]:
        print("Invalid target language. Please choose either 'French' or 'Urdu'.")
        return

    user_input = input(f"Enter text to translate from English to {target_language}: ")
    translated_text = translate_text(user_input, target_language)
    print("Translated Text:")
    print(translated_text)

# Run the function
if __name__ == "__main__":
    main()

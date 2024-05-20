from transformers import pipeline

def generate_text(prompt):
    # Text Generator
    generator = pipeline("text-generation", model="gpt2")
    generated_text = generator(prompt, max_length=100, num_return_sequences=1, do_sample=True)[0]['generated_text']
    return generated_text

def main():
    user_input = input("Enter a prompt: ")
    generated_text = generate_text(user_input)
    print("Generated Text:")
    print(generated_text)

# Run the function
if __name__ == "__main__":
    main()

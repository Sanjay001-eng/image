import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()  # Load from .env file
api_key = os.getenv("GEMINI_API_KEY") 


# Set your Gemini API key as an environment variable. Replace with your key.
os.environ["GEMINI_API_KEY"] = api_key

# Configure and initialize the Gemini client
genai.configure(api_key=os.environ["GEMINI_API_KEY"])

def ask_gemini(question):
    # Use the 'gemini' model (free version) for text generation
    model = genai.GenerativeModel("gemini-pro") 

    # Get the response from Gemini
    response = model.generate_content(question)

    # Print the response text
    print(response.text)

if __name__ == "__main__":
    while True:
        question = input("Ask your question: ")
        if question.lower() == "exit":
            break
        ask_gemini(question)

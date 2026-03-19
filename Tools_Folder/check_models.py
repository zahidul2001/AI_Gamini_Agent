import google.generativeai as genai # Gemini AI library
import os # Operating system functions
from dotenv import load_dotenv # Environment variables loader

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=GEMINI_API_KEY) 

# List available models #এটি Google এর সার্ভারে request করে এবং সব Available Models এর information নিয়ে আসে
for model in genai.list_models():
    print(f"Model: {model.name}")
    print(f"Supported methods: {model.supported_generation_methods}")
    print("---")
 
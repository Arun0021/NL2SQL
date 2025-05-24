import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def list_models():
    return genai.list_models()

models = list_models()
for model in models:
    print(model)

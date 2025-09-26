import google.generativeai as genai
from config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)

print("📦 Modelos disponibles:")
for model in genai.list_models():
    print(f"- {model.name}")
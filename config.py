import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# print(f"[DEBUG] Clave cargada: {GEMINI_API_KEY}")

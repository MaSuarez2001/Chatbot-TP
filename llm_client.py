import requests
from config import GEMINI_API_KEY

def ask_gemini(prompt: str) -> str:
    if not GEMINI_API_KEY:
        return "⚠️ Clave de API no encontrada."

    url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent"
    headers = {
        "Content-Type": "application/json"
    }
    params = {
        "key": GEMINI_API_KEY
    }
    data = {
        "contents": [
            {
                "parts": [
                    {"text": prompt}
                ]
            }
        ]
    }

    try:
        response = requests.post(url, headers=headers, params=params, json=data)
        response.raise_for_status()
        return response.json()["candidates"][0]["content"]["parts"][0]["text"]
    except Exception as e:
        return f"❌ Error al consultar Gemini: {e}"
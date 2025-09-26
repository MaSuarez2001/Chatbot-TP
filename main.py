import os
import sys

sys.stderr = open(os.devnull, 'w')

from llm_client import ask_gemini

def main():
    print("🤖 Bienvenido al Chatbot Gemini. Escribí tu pregunta o 'salir' para terminar.\n")

    while True:
        prompt = input("📝 Tu pregunta: ")
        if prompt.lower() in ["salir", "exit", "quit"]:
            print("👋 Hasta luego, Humano.")
            break

        respuesta = ask_gemini(prompt)
        print(f"\n🌸 Gemini responde:\n{respuesta}\n")

if __name__ == "__main__":
    main()
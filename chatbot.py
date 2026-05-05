import requests

chat_history = []

def chat_with_bot(prompt):
    chat_history.append(f"User: {prompt}")

    full_prompt = "\n".join(chat_history) + "\nBot:"

    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "llama3",
                "prompt": full_prompt,
                "stream": False
            }
        )

        bot_reply = response.json()["response"]
        chat_history.append(f"Bot: {bot_reply}")

        return bot_reply

    except Exception as e:
        return "Error: Make sure Ollama is running."

while True:
    user_input = input("You: ")

    if user_input.lower() in ["quit", "exit"]:
        print("Chat ended.")
        break

    print("Bot:", chat_with_bot(user_input))
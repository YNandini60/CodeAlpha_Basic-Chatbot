import datetime
import random

def chatbot():
    print("🤖 Simple Chatbot")
    print("Type 'bye' to exit.\n")

    jokes = [
        "Why don’t programmers like nature? Too many bugs! ",
        "Why do Java developers wear glasses? Because they don’t C#!",
        "Debugging: Removing the needles from the haystack. "
    ]

    while True:
        user_input = input("You: ").lower()

        if user_input in ["hello", "hi", "hey"]:
            print("Bot: Hello there! 👋")
        elif user_input == "how are you":
            print("Bot: I'm doing great, thanks for asking! How about you?")
        elif "time" in user_input:
            now = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"Bot: The current time is {now} ⏰")
        elif "date" in user_input:
            today = datetime.date.today().strftime("%B %d, %Y")
            print(f"Bot: Today is {today} 📅")
        elif "joke" in user_input:
            print("Bot:", random.choice(jokes))
        elif "your name" in user_input:
            print("Bot: I'm ChatBot 🤖.")
        elif user_input == "bye":
            print("Bot: Goodbye! 👋 Have a wonderful day!")
            break
        else:
            print("Bot: Sorry, I don’t understand that. Try asking me the time, date, or a joke!")

# Run chatbot
if __name__ == "__main__":
    chatbot()
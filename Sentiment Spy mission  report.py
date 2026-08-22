from textblob import TextBlob
from colorama import Fore, Style, init

init(autoreset=True)

positive = 0
negative = 0
neutral = 0
history = []


def analyze_sentiment(text):
    global positive, negative, neutral

    blob = TextBlob(text)
    polarity = blob.sentiment.polarity

    if polarity > 0:
        sentiment = "Positive"
        positive += 1
        print(Fore.GREEN + "Sentiment: Positive 😊")

    elif polarity < 0:
        sentiment = "Negative"
        negative += 1
        print(Fore.RED + "Sentiment: Negative 😟")

    else:
        sentiment = "Neutral"
        neutral += 1
        print(Fore.YELLOW + "Sentiment: Neutral 😐")

    history.append((text, sentiment))

    print(Fore.CYAN + f"Polarity: {polarity:.2f}")


print(Fore.CYAN + "=" * 45)
print(Fore.CYAN + "          SENTIMENT SPY")
print(Fore.CYAN + "=" * 45)

print("Welcome to Sentiment Spy!")
print("Type a message and I will analyze its sentiment.")
print()
print("Commands:")
print("/stats   - Show statistics")
print("/history - Show previous messages")
print("/reset   - Reset the data")
print("/help    - Show commands")
print("/exit    - Exit the program")

while True:

    user_input = input(Fore.WHITE + "\nYou: ")

    if user_input.lower() == "/exit":
        print(Fore.CYAN + "\nMission complete!")
        print(f"Positive: {positive}")
        print(f"Negative: {negative}")
        print(f"Neutral: {neutral}")
        break

    elif user_input.lower() == "/stats":
        print(Fore.CYAN + "\n--- SENTIMENT STATISTICS ---")
        print(Fore.GREEN + f"Positive: {positive}")
        print(Fore.RED + f"Negative: {negative}")
        print(Fore.YELLOW + f"Neutral: {neutral}")

    elif user_input.lower() == "/history":
        print(Fore.CYAN + "\n--- CONVERSATION HISTORY ---")

        if len(history) == 0:
            print("No messages yet.")

        else:
            for message, sentiment in history:
                print(f"Message: {message}")
                print(f"Sentiment: {sentiment}")
                print()

    elif user_input.lower() == "/reset":
        positive = 0
        negative = 0
        neutral = 0
        history = []

        print(Fore.GREEN + "All data has been reset!")

    elif user_input.lower() == "/help":
        print(Fore.CYAN + "\n--- COMMANDS ---")
        print("/stats   - Show statistics")
        print("/history - Show conversation history")
        print("/reset   - Reset data")
        print("/help    - Show commands")
        print("/exit    - Exit")

    elif user_input.strip() == "":
        print(Fore.RED + "Please enter something.")

    else:
        analyze_sentiment(user_input)
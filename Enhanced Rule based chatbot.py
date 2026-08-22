
import re
import random
from colorama import Fore, Style, init
from datetime import datetime

init(autoreset=True)

responses = {
    "greeting": [
        "Hello! How can I help you?",
        "Hi there! What would you like to know?",
        "Hey! Nice to meet you!"
    ],
    "how_are_you": [
        "I'm doing great!",
        "I'm fine, thanks for asking!",
        "I'm ready to chat with you!"
    ],
    "goodbye": [
        "Goodbye! Have a great day!",
        "See you later!",
        "Bye! Thanks for chatting with me!"
    ],
    "thanks": [
        "You're welcome!",
        "No problem!",
        "Glad I could help!"
    ]
}


def get_weather(city):
    weather_data = {
        "lahore": ["Sunny", "32°C"],
        "karachi": ["Partly cloudy", "30°C"],
        "islamabad": ["Cloudy", "27°C"],
        "london": ["Rainy", "18°C"],
        "new york": ["Sunny", "25°C"]
    }

    city = city.lower()

    if city in weather_data:
        condition, temperature = weather_data[city]
        return f"The weather in {city.title()} is {condition} with a temperature of {temperature}."
    else:
        return f"Sorry, I don't have weather information for {city.title()}."


def get_news():
    news = [
        "Scientists have announced a new space research mission.",
        "A new technology competition has started for students.",
        "Schools are using more technology to improve learning.",
        "Scientists are working on new ways to protect the environment."
    ]

    return random.choice(news)


def get_time(city):
    current_time = datetime.now().strftime("%I:%M %p")
    return f"The current local time for {city.title()} is approximately {current_time}."


def remember_name(user_input):
    match = re.search(r"my name is ([A-Za-z]+)", user_input, re.IGNORECASE)

    if match:
        return match.group(1)

    return None


def chatbot(user_input, memory):
    text = user_input.lower().strip()

    name = remember_name(user_input)

    if name:
        memory["name"] = name
        return f"Nice to meet you, {name}!"

    if re.search(r"\b(hello|hi|hey|salam|assalam)\b", text):
        if memory["name"]:
            return f"Hello {memory['name']}! How can I help you?"

        return random.choice(responses["greeting"])

    if re.search(r"\b(how are you|how r u|how do you feel)\b", text):
        return random.choice(responses["how_are_you"])

    if re.search(r"\b(weather|temperature|forecast)\b", text):
        city_match = re.search(r"(?:in|for)\s+([A-Za-z ]+)", text)

        if city_match:
            city = city_match.group(1).strip()
            return get_weather(city)

        return "Please tell me a city. Example: weather in Lahore"

    if re.search(r"\b(news|headlines|updates)\b", text):
        return "Latest news: " + get_news()

    if re.search(r"\b(time|clock)\b", text):
        city_match = re.search(r"(?:in|for)\s+([A-Za-z ]+)", text)

        if city_match:
            city = city_match.group(1).strip()
            return get_time(city)

        return "The current time is " + datetime.now().strftime("%I:%M %p")

    if re.search(r"\b(what is my name|do you know my name|remember my name)\b", text):
        if memory["name"]:
            return f"Your name is {memory['name']}."

        return "You haven't told me your name yet."

    if re.search(r"\b(thanks|thank you|thx)\b", text):
        return random.choice(responses["thanks"])

    if re.search(r"\b(help|what can you do|commands)\b", text):
        return (
            "I can help with:\n"
            "- Greetings\n"
            "- Weather information\n"
            "- News updates\n"
            "- Local time\n"
            "- Remembering your name\n"
            "- Basic conversation"
        )

    if re.search(r"\b(bye|goodbye|exit|quit|see you)\b", text):
        return random.choice(responses["goodbye"])

    unknown_responses = [
        "I'm not sure I understand. Try asking for help.",
        "Sorry, I don't know how to answer that yet.",
        "Could you say that in another way?",
        "Interesting! I'm still learning about that."
    ]

    return random.choice(unknown_responses)


def start_chatbot():
    memory = {
        "name": None
    }

    print(Fore.CYAN + "=" * 50)
    print(Fore.YELLOW + "        ENHANCED RULE-BASED CHATBOT")
    print(Fore.CYAN + "=" * 50)

    print(Fore.GREEN + "Type 'help' to see what I can do.")
    print(Fore.RED + "Type 'bye' to exit.")

    while True:
        user_input = input(Fore.BLUE + "\nYou: " + Style.RESET_ALL)

        response = chatbot(user_input, memory)

        print(Fore.GREEN + "Bot: " + response)

        if re.search(r"\b(bye|goodbye|exit|quit|see you)\b",
                     user_input.lower()):
            break


if __name__ == "__main__":
    start_chatbot()


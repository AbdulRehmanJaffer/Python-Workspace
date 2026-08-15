import colorama
from colorama import fore, style
from textblob import Textblob

colorama.init()

print(f"{fore.CYAN} Welcome to Sentiment AI! {Style.RESET_ALL}")

user_name = input(f"{fore.MAGENTA} Please enter your name: {Style.rESET_ALL}")
if not user_name:
    user_name = "Mystery Agent"

conversation_history = []

print(f"\n{fore.CYAN}Hello, Agent {user_name}!")
print(f"Type a sentence and I will analyza you sentence with Textblob and show you the sentiment. ")
print(f"Type {fore.YELLOW}reset{fore.CYAN}, {fore.YELLOW}History{fore.CYAN}, "
      f" {fore.YELLOW}exit{fore.CYAN} to quit.{Style.RESET_ALL}\n")
while True:
    user_input = input(f"{fore.GREEN}>> {Style.RESET_ALL}").strip()

    if not user_input:
        print(f"{fore.RED} Please enter some text or a valid command {Style.RESET_ALL}")
        continue

    if user_input.lower() == "exit":
        print(f"\n{fore.BLUE} Exiting Sentiment AI. farewell, Agent {user_name} ! {Style.RESET_ALL}")
        break

    elif user_input.lower() == "reset":
        conversation_history.clear()
        print(f"{fore.CYAN} All conversation history cleared!{Style.RESET_ALL}")
        continue


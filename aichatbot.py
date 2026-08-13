

print("Hello! I am PyBot, your Python chatbot.")
print("Type 'help' to see what I can do.")
print("Type 'bye' to exit.")
print("")

name = input(" What is your name? ")

print("")
print(f"PyBot: Nice to meet you, {name}!")
print("PyBot: How can I help you today?")
print("")

while True:

    user_input = input(f"{name}: ")
    message = user_input.lower()

    if message == "hello":
        print(f"PyBot: Hello {name}! ")

    elif message == "hi":
        print(f"PyBot: Hi {name}! How are you?")

    elif message == "hey":
        print(f"PyBot: Hey {name}! ")

    elif "good morning" in message:
        print(f"PyBot: Good morning, {name}! ")

    elif "good afternoon" in message:
        print(f"PyBot: Good afternoon, {name}!")

    elif "good evening" in message:
        print(f"PyBot: Good evening, {name}!")


    elif "how are you" in message:
        print("PyBot: I'm doing great! Thanks for asking.")

    elif "what are you doing" in message:
        print("PyBot: I'm chatting with you!")

    elif "who are you" in message:
        print("PyBot: I am PyBot, a chatbot made with Python.")

    elif "your name" in message:
        print("PyBot: My name is PyBot.")

    elif "my name" in message:
        print(f"PyBot: Your name is {name}!")

    elif "are you real" in message:
        print("PyBot: I'm a computer program, so I'm not a human.")

    elif "are you ai" in message:
        print("PyBot: Yes! I'm a simple AI-style chatbot.")


    elif message == "help":
        print("")
        print("========== PYBOT HELP ==========")
        print("You can say:")
        print("- hello")
        print("- how are you")
        print("- who are you")
        print("- tell me a joke")
        print("- tell me a fact")
        print("- calculate")
        print("- play a game")
        print("- favorite color")
        print("- favorite food")
        print("- thank you")
        print("- bye")
        print("================================")


    elif "joke" in message:
        print("PyBot: Why did the computer go to the doctor?")
        print("PyBot: Because it had a virus! ")

    elif "another joke" in message:
        print("PyBot: Why was the computer cold?")
        print("PyBot: It left its Windows open! ")

    elif "funny" in message:
        print("PyBot: Why do programmers prefer dark mode?")
        print("PyBot: Because light attracts bugs! ")

    elif "fact" in message:
        print("PyBot: Here is a fact:")
        print("PyBot: Python was created by Guido van Rossum.")

    elif "space fact" in message:
        print("PyBot: A day on Venus is longer than a year on Venus.")

    elif "computer fact" in message:
        print("PyBot: The first computer mouse was made of wood.")

    elif "python fact" in message:
        print("PyBot: Python was first released in 1991.")

    elif "ai fact" in message:
        print("PyBot: AI can be used for tasks like recognizing images and text.")


    elif "favorite color" in message:
        print("PyBot: I like blue. It reminds me of technology! ")

    elif "favorite food" in message:
        print("PyBot: I don't eat, but pizza sounds pretty good! ")

    elif "favorite game" in message:
        print("PyBot: I would probably enjoy a coding game!")


    elif message == "calculate":

        print("")
        print("========== PYBOT CALCULATOR ==========")

        number1 = float(input("Enter first number: "))
        operator = input("Enter +, -, *, or /: ")
        number2 = float(input("Enter second number: "))

        if operator == "+":
            answer = number1 + number2
            print(f"PyBot: {number1} + {number2} = {answer}")

        elif operator == "-":
            answer = number1 - number2
            print(f"PyBot: {number1} - {number2} = {answer}")

        elif operator == "*":
            answer = number1 * number2
            print(f"PyBot: {number1} × {number2} = {answer}")

        elif operator == "/":

            if number2 == 0:
                print("PyBot: You cannot divide by zero.")

            else:
                answer = number1 / number2
                print(f"PyBot: {number1} ÷ {number2} = {answer}")

        else:
            print(f"PyBot: I don't recognize the operator '{operator}'.")


    elif "play a game" in message:

        print("")
        print("========== 🎮 NUMBER GAME ==========")
        print("I'm thinking of a number from 1 to 5.")

        secret_number = 3

        guess = int(input("Your guess: "))

        if guess == secret_number:
            print(f"PyBot: Correct, {name}! ")
            print("PyBot: You won the game!")

        elif guess < secret_number:
            print("PyBot: Too low!")

        elif guess > secret_number:
            print("PyBot: Too high!")

        print(f"PyBot: The number was {secret_number}.")


    elif "what is my name" in message:
        print(f"PyBot: Your name is {name}.")

    elif "remember my name" in message:
        print(f"PyBot: Yes! Your name is {name}.")


    elif "thank you" in message:
        print(f"PyBot: You're welcome, {name}! ")

    elif "thanks" in message:
        print("PyBot: No problem!")


    elif message == "bye":
        print(f"PyBot: Goodbye, {name}! ")
        print("PyBot: Thanks for chatting with me!")
        break

    elif message == "exit":
        print("PyBot: Shutting down...")
        break

    elif message == "quit":
        print(f"PyBot: Goodbye, {name}!")
        break


    else:
        print(f"PyBot: Sorry {name}, I don't understand that yet.")
        print("PyBot: Type 'help' to see what I can do.")

    print("")
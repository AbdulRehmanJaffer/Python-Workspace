print("Hello! I am AI bot, What is your name?")

name = input()

print(f"nice to meet you {name}!")
print("How are you feeling today? (good/bad)")
mood = input().lower()


if mood == "good":
    print("I'm glad to hear that!")
elif mood == "bad":
    print("i'm sorry to hear that. Hope things will get better soon.")
elif mood == "decent":
    print("Ïts good to hear that its not a bad day")
elif mood == "Exhausting":
    print("Its alright, you should go get some rest and freshen up a bit!")

else:
    print("I see. sometimes feelings are hard to put into words.")

print("How is the weather today?")
weather = input()

if weather == "sunny":
    print("that is a good waather, Go outside and enjoy some Vitamin D!")
elif weather == "rainy":
    print("Sit down next to the window and drink some hot chocolate. :D")
elif weather == "chilly":
    print("Go sit next to fthe fireplace and enjoy some meals!")

print("How old are you?")
age = input()

if age == "10":
    print("Did you reach 4 foot 11??")
elif age == "13":
    print("Did you go do something productive today?")
elif age == "18":
    print("Did you get you ID?")

print("Did you go to school today?")
school = input()

if school == "Yes":
    print("Nice, I hope you learnt alot of stuff!")
elif school == "No":
    print("Im guessing you were either sick, I hope you get better!")
else:
    print("Please say either yes or no.")

print("Did you get 8 hours of sleep?")
sleep = input()

if sleep == "Yes":
    print("You must be refreshed and energized!")
elif sleep == "no":
    print("You must be exhausted, Go get some sleep and freshen up!")
else:
    print("You should maintain you sleep cycle. :D")

print(f"It was nice chatting with you {name}. Goodbye!")
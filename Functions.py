#def sum(a, b):
#    print(a+b)

#sum(5, 6)

"""def information(name, place):
    print("my name is", name)
    print("my place is", place)

information("Ali", "islamabad")"""

#activity 1

"""def weather():
    print("The weather in autumn is mildly cold ")
    print("The weather in spring is mildly hot ")

weather()"""

def add(a,b):
    print(a+b)

def subtract(a,b):
    print(a-b)

def multiply(a,b):
    print(a*b)

def divide(a,b):
    print(a/b)

num_1 = int(input("Enter a number: "))
num_2 = int(input("Enter a second number: "))

print("Here are the options: \n 1) addition: \n 2) Subtraction: \n 3) Multiplication: \n 4) Division: ")
choice = int(input("Enter a choice between the 4 options"))

if choice == 1:
    add(num_1,num_2)

elif choice == 2:
    subtract(num_1,num_2)

elif choice == 3:
    multiply(num_1,num_2)

elif choice == 4:
    divide(num_1,num_2)

else:
    print("Invalid choice")


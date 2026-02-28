i = 13

if (i == 13):
    if (i < 15):
        print("i is less than 15")
    if (i < 13):
        print("i is less than 13")
    else:
        print("i is greater than 12 and less than 15")

n = int(input("Enter a number"))

if (n == 0):
    print("no. is 0")
else:
    if (n > 0):
        print("Number is positive")
    elif (n < 0):
        print("It is negative")
    else:
        print("Its not a number")

answer = input("Do you have a medical cause?")


if answer == "yes":
    print("Student has medical cause. They can skip")
else:
    attendance = int(input("Enter your attendance in percentage:"))
    if attendance >= 75:
        print("Allowed to take the exam")
    else:
        print("Not allowed")

choice = int(input("Choose a ride"))
print("1. car")
print("2. bike")

if choice == 1:
    print("You have selected Car")
    choice2 = int(input("Which car will you choose.1)SUV 2)Sudan"))
    if choice2 == 1:
        print("You have chosen SUV")
        print("For 1 hour the charge will be PKR 150")
    else:
        print("You have chosen Sudan")
        print("For 1 hour the charge will be PKR 300")
else:
    print("You have seklected bike")
    choice3 = int(input("Select a bike 1)Kawasaki 2)Honda"))
    if choice3 == 1:
        print("You have chosen Kawasaki")
    else:
        print("You have chosen Honda")



    
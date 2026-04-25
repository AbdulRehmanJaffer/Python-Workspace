"""import random"""
"""print(random.choice("Python"))"""
"""random.random()"""
"""print(random.randint(0,10))"""

"""playing = True
number = str(random.randint(0,9))

print("Here is the guessing game, i will generate a number from 0,9, you will have to guess it! ")
print("Game ends when you get 1 score")

while playing:
    guess = input("Give it you best shot!: ")
    if number == guess:
        print("You guessed correct!")
        print("The number was:",number)
    else:
        print("You got it wrong how about you try again! \n")   """

import math

print("The Floor and ceiling value of 23.56 are: " + str(math.ceil(23.56))), str(math.floor(23.56))

x = 10
y = -15

print("The sign of x after copying the sign of y is:"+ str(math.copysign(x,y)))
print("\n")
print("The absolute value of -96 and 56 are: "+ str(math.fabs(-96))+ str(math.fabs(56)))
print("\n")
print("The GCD value of 24 and 56 are: "+ str(math.gcd(24,56)))

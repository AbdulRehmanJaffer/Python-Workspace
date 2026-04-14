try:
    age = int(input("enter a number: "))
    
    if age < 0:
        raise ValueError("Number must not be negative")
    elif age % 2 == 0:
        print("It is even")
    else:
        print("It is odd")

except ValueError as error:
    print("Error: ", error)

finally:
    print("Done!")
test_dict = {"Codingal": 3, "is": 2, "best": 2, "for": 2, "coding": 1}

print(test_dict)

value = int(input("Enter the a value to check: "))

frequency = 0

for i in test_dict:
    if test_dict[i] == value:
        frequency += 1

print("The frequency of", value, "is:", frequency)

num = int(input("Enter a number: "))

odd_numbers = [x for x in range(num) if x % 2 != 0]

even_numbers = [x for x in range(num) if x % 2 == 0]

print("Odd Numbers:", odd_numbers)
print("Even Numbers:", even_numbers)

fruits = ["apple", "banana", "mango", "orange"]

updated_fruits = [fruit.capitalize() for fruit in fruits]

print("Updated Fruits List:", updated_fruits)
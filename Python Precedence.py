#Acivity 1
v = 4
w = 5
x = 8
y = 2
z = 0
z = (v+w) * x / y
print("Value Of (v+w) is:", z)
#activity 2
name = "Alex"
age = 0

if name == "Alex" or "John" and age >= 2:
    print("Hello, Welcome")
else:
    print("Goodbye")
#activity 3
x = int(input("Enter a number:"))
y = int(input("Enter a denominator"))

if x%y == 0:
    print("It is Divisible")
else:
    print("It it not divisible")
#Activity 4
mean_1 = 38
wrong_number = 36
correct_number = 56
total_number = 40

sum = mean_1*total_number
print("The sum of the forty numbers:", sum)

sum2 = sum-(wrong_number)-(correct_number)
print("sum-(wrong number)-(correct numer):", sum2)

mean_2 = sum2/total_number
print(mean_2)
#activity 5
speed_1 = 10
speed_2 = 20
speed_3 = 30

avg = (speed_1 + speed_2 + speed_3)/3
print(avg)

if speed_1 < avg and speed_2 < avg:
    print("Speed_1 and speed 2 are slower than avg speed")

elif speed_3 < avg:
    print("Speed 3 slower than avg")
else:
    print("")
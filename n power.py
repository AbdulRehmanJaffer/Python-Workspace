base = int(input("Enter a base number: "))
power = int(input("Enter a power/exponent: "))
result = 0

for i in range(power):
    print(i)
    result = result * base
    print(result)
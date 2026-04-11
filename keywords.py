"""def add(a,b):
    return(a+b)

sum = add(5,6)
print(sum)"""

#activity 1
"""a = input("Enter a word: ")

for i in (a):
    if i == 'a':
        print("A is found")
        break
    print("A is not found")
    print(i)"""
#activity 2
"""num = 11
while num > 0:
    num -= 1
    if num == 5:
        continue
    print(num)"""
#activity 3
for i in range(10):
    if i % 20 == 0:
        print("twist")
    elif i % 15 == 0:
        pass
    elif i % 5 == 0:
        print("Fizz")
    elif i % 3 == 0:
        print("Buzz")
    else:
        print(i)
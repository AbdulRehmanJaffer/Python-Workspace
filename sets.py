"""my_set = {1, 2, 3, 4, 5}
my_set.add(6)
print(my_set)"""
#activity 1
"""my_set = {2, "Codingal", 6, "Billy"}
my_set.add("Python")
my_set.pop()
print(my_set)"""

#activity 2
"""setx = {"green", "blue", "orange", "yellow"}
sety = {"blue", "yellow", "majenta", "green"}
print(setx)
print(sety)

setz = setx.symmetric_difference(sety)
print(setz)"""

import array as arr

a = arr.array('i', [1,2,3])

print("The new array created is : ", end="")
for i in range(0,3):
    print(a[i])
print()
#float type
"""b = arr.array('d', [2.5, 3.5, 4.5])

for i in range(0,3):
    print(b[i])
print()

a.insert(4, 4)

for i in(a):
    print(i)
print()

b.append(4.4)
for i in(b):
    print(i)
print()"""




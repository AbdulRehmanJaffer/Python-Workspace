tuple1 = ("P", "Y", "T", "H", "O", "N", "E", "I")

tuple2 = [1, 2, 3]
tuple2[1] = "b"
print(tuple2)

tuple1[2] = "a"
print(tuple1)

nest_tup = (1, 2,("P", "Y"), [4, 5, "Python", 5, 6])

print(nest_tup[3][2])

#activity 1

weather = 0
sunny = 0
rainy = 0

weather = tuple(int(input()) for i in range(7))

for i in range(7):

    weather[i]
    if weather[i] == 0:
        sunny += 1
    else:
        rainy += 1

if sunny > rainy:
    print("It was good weather")
else:
    print("It was rainy weather")

tuple1 = ("P", "Y", "T", "H", "O", "N", "E", "I")

tuple2 = [1, 2, 3]
tuple2[1] = "b"
print(tuple2)

tuple1[2] = "a"
print(tuple1)

nest_tup = (1, 2,("P", "Y"), [4, 5, "Python", 5, 6])

print(nest_tup[3][2])
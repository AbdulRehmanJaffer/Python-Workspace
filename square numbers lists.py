x = [1, 4, 9, 16, 25]

odd_squares = []
even_squares = []

for i in x:
    if i % 2 == 0:
        even_squares.append(i)
    else:
        odd_squares.append(i)

print("The even squares were: ",even_squares)
print("The odd squares were: ",odd_squares)
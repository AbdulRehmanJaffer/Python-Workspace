n = 5
i = 0

for i in range(n + i + 1):          # <--- because i is 0 and it goes from left to right and 0 is a blank space so it goes from blank to a star
    print(' ', end=' ')       # <--- until here this is for the blank space
    for j in range(i+1):      # <--- from here starts the stars
        print('*', end=' ')
    print()

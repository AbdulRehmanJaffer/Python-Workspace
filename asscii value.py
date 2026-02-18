print("ASCII value checker")
print("="*40)

char = input("Enter a single character")
if type(char) is str and len(char) == 1:
    print("Valid Input")
else:
    print("Please enter a SINGLE number.")

ascii_val = ord(char)

if ascii_val >= 65 and ascii_val <= 90:
    print("Uppercase Letter")
elif ascii_val >= 97 and ascii_val <= 122:
    print("Lowercase Letter")
elif ascii_val >= 48 and ascii_val <= 57:
    print("Digit")
elif ascii_val == 32:
    print("Space")
else:
    print("Type a SPecial character")
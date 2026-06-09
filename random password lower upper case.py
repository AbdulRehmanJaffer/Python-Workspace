import random
import string

length = 10

lower = string.ascii_lowercase
upper = string.ascii_uppercase
digits = string.digits

password_list = [
    random.choice(lower),
    random.choice(upper),
    random.choice(digits)
]

all_chars = lower + upper + digits
for i in range(length - 3):
    password_list.append(random.choice(all_chars))

random.shuffle(password_list)

password = ''.join(password_list)

print("Generated Password:", password)
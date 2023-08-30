# Random Password Generator in Python

import random
import string

def generate_random_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

password_length = int(input("Enter the desired password length: "))
random_password = generate_random_password(password_length)
print("Random Password:", random_password)

# Enter the desired password length: 8
# Random Password: `H5]6Ql>

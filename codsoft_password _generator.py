import random
import string

length = int(input("Enter password length: "))

chars = string.ascii_letters + string.punctuation + string.digits

password = " "
for i in range(length):
    password += random.choice(chars)

print("Your password is:", password)

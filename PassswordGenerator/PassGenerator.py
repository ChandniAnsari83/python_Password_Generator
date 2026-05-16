import random
import string
values = string.ascii_letters + string.digits + string.punctuation
passLength = int(input("Enter password length: "))
password = ""
for i in range(passLength):
    password += random.choice(values)
print("Password is generated: ", password)

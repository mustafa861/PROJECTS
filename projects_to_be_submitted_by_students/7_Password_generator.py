import random

print("Welcome To Your Password Generator")

alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*().,?0123456789"

number = int(input("Amount of passwords to generate: "))
length = int(input("Input your password length: "))

print("Here are your passwords:")

for abc in range(number):
    password = ""
    for xyz in range(length):
        password += random.choice(alphabet)  # Corrected variable name
    print(password)
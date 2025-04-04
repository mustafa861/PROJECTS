import random

def num():
    
    return random.randint(0, 99)

guess_num = num()

while True:

    try:

        user_num = int(input("Enter a number between 0 and 99: "))

        if user_num < 0 or user_num > 99:

            print("Please enter a number within the range 0–99.")

            continue

        if user_num < guess_num:

            print("You guessed a low number.")

        elif user_num > guess_num:

            print("You guessed a high number.")

        else:

            print(f"Congratulations! Your guess {user_num} is correct.")

            break

    except ValueError:

        print("Please enter a valid integer.")
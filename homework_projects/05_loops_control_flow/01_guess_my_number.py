import random

random_Number = random.randint(1, 99)

user_guess =input("Guess a number between 1 and 99: ")

while not user_guess.isdigit():  

        print("❌ Invalid input! Please enter a number.")


        user_guess =input("Guess a number between 1 and 99: ")

user_guess = int(user_guess)  

while user_guess != random_Number:

        if user_guess < random_Number:

            print("Your guess is too low.")

        else:

            print("Your guess is too high.")  

        user_guess =input("Enter a new guess: ")

        while not user_guess.isdigit():  

            print("❌ Invalid input! Please enter a number.")

            user_guess = input("Enter a new guess: ")
        
        user_guess = int(user_guess)  

print(f"🎉 Correct! You guessed {user_guess} correctly.")


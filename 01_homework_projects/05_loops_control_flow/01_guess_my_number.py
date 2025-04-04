import random

def main():
    """ A Program that makes the user guess a number between 1 and 99 """
    random_Number = random.randint(1, 99)

    # Ensure the user enters a valid number
    user_guess =input("Guess a number between 1 and 99: ")
    while not user_guess.isdigit():  # Check if input is a number
        print("❌ Invalid input! Please enter a number.")
        #This below line with "int" will work correctly as long as the user enters a valid number.
        user_guess =input("Guess a number between 1 and 99: ")
    #Because int(input(...)) immediately tries to convert the input into an integer, and if it's not a valid number
    # Python throws an error so we use to convert user_guess into =int(user_guess)
    user_guess = int(user_guess)  # Convert valid input to integer

    while user_guess != random_Number:
        if user_guess < random_Number:
            print("Your guess is too low.")
        else:
            print("Your guess is too high.")  

        # Ensure the user enters a valid number
        user_guess =input("Enter a new guess: ")
        while not user_guess.isdigit():  # Check if input is a number
            print("❌ Invalid input! Please enter a number.")
            user_guess = input("Enter a new guess: ")
        
        user_guess = int(user_guess)  # Convert valid input to integer

    print(f"🎉 Correct! You guessed {user_guess} correctly.")

if __name__ == "__main__":
    main()

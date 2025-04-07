import random

def number_guess():
  guess_number = random.randint(1,100)
  number_guess = 0
  while number_guess != guess_number:
    number_guess = int(input(f"Guess a number between{1,100}:"))
    if number_guess < guess_number:
      print("Sorry try one more time.Your guess is two low")
    elif number_guess > guess_number:
      print("Sorry try one more time.Your guess is two high")
    else:
      print(f"Congratulations! {guess_number} is a correct guess")
number_guess()
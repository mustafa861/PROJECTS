import random

def hangman():
    words = ["apple", "banana", "orange", "grape", "peach"]
    word = random.choice(words)
    guessed = "_" * len(word)
    attempts = 6
    guessed_letters = []

    print("Welcome to Hangman!")
    print(guessed)

    while attempts > 0 and "_" in guessed:
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("Correct!")
        else:
            attempts -= 1
            print("Wrong! Attempts left:", attempts)

        guessed = ""
        for letter in word:
            if letter in guessed_letters:
                guessed += letter
            else:
                guessed += "_"

        print("Word:", guessed)

    if "_" not in guessed:
        print("You won! 🎉")
    else:
        print("You lost. The word was:", word)

hangman()
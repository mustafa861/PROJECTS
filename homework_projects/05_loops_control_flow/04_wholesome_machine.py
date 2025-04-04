AFFIRMATION = "I am capable of doing anything I put my mind to."

def main():
    """Prompt the user to type the affirmation correctly until they get it right."""
    print(f"Please type the following affirmation: {AFFIRMATION}")

    user_prompt = input()  # Get user input

    while user_prompt != AFFIRMATION:  # If the input is incorrect, keep asking
        print("That's not the correct affirmation.")
        user_prompt = input()  # Ask for input again

    print("Now you typed the correct affirmation!")

if __name__ == '__main__':
    main()

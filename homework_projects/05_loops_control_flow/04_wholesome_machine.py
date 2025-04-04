AFFIRMATION = "I am capable of doing anything I put my mind to."

print(f"Please type the following affirmation: {AFFIRMATION}")

user_prompt = input()  

while user_prompt != AFFIRMATION:  

        print("That's not the correct affirmation.")

        user_prompt = input()  

print("Now you typed the correct affirmation!")


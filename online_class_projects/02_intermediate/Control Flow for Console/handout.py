import random

rounds = 5  # Total rounds to play

def num_gen(min=1, max=100):
    """ A High Low game of 5 rounds having 'min-value =1' and 'max_value=100'generate two number randomly and then ask the 
    user for their guess fo second number high or low and add score 1 after each round ."""
    return random.randint(min, max)

def game():
    score = 0
    
    print("Welcome to NailaAdnan GameZone!")
    print("Click to start the High-Low Game!\n")
    
    for i in range(rounds):
        print(f"Round {i + 1}") 
        
        
        user_num = num_gen()
        comp_num = num_gen()
        
        print(f"Your number is: {user_num}\n")
        
        print("Try to guess if your number is higher or lower than the computer's number!\n")
        guess = input("Your guess ('higher' or 'lower'): ").strip().lower()
        
        # Check if the user's guess is correct
        if (guess == 'higher' and user_num > comp_num) or (guess == 'lower' and user_num < comp_num):
            print(f"The computer's number was: {comp_num} and your number was {user_num}.\n")
            score += 1
            print("So it's Correct! You get a point! 😊\n")
        else:
            print(f"The computer's number was: {comp_num} and your number was {user_num}.\n")
            print("So it's Wrong! No point for you. 😞\n")
            
        
        print(f"Your score after round {i + 1} is {score}\n")
    
    # Final message after all rounds
    print(f"Game Over! Your final score is: {score}/{rounds}")
    if score == rounds:
        print("Wow! You played perfectly!")
    elif score > rounds // 2:
        print("Good job, you played really well!")
    else:
        print("Better luck next time!")


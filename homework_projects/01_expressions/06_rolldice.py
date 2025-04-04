import random

# Define number of sides on a die
DICE_SIDES = 6

def roll_dice():
    """Simulates rolling two dice and prints the results of each roll as well as the total."""

    # Roll two dice
    die1 = random.randint(1, DICE_SIDES)  
    die2 = random.randint(1, DICE_SIDES)  
    total = die1 + die2  

    # Display results
    print("\n=== Dice Roll Simulation ===")
    print(f"Die 1: {die1}")
    print(f"Die 2: {die2}")
    print(f"Total: {total}")

if __name__ == '__main__':  
    roll_dice()

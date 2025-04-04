import random

# Define the number of sides on each die (easy to change)
NUM_SIDES = 6

def roll_dice():
    """Simulates rolling two dice and returns their values and total."""
    die1 = random.randint(1, NUM_SIDES)  # Roll first die
    die2 = random.randint(1, NUM_SIDES)  # Roll second die
    total = die1 + die2  # Sum both dice
    return die1, die2, total  # Return values

def main():
    """Main function to roll dice three times and print results."""
    print("🎲 Rolling two dice three times... 🎲\n")

    for i in range(1, 4):  # Loop exactly 3 times
        die1, die2, total = roll_dice()  # Call roll_dice() function
        print(f"Roll {i}: 🎲 {die1} and 🎲 {die2} (Total: {total})")

    print("\n🎲 Done rolling! 🎲")

# Run the program only if the script is executed directly
if __name__ == '__main__':
    main()

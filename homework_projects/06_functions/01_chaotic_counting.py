import random

def chaotic_counting():
    """Counts from 1 to 10 but may stop early with a 30% chance at each step."""
    DONE_LIKELIHOOD = 0.3  # 30% chance to stop
    print("I'm going to count until 10 or until I feel like stopping, whichever comes first.")
    
    for num in range(1, 11):  # Loop from 1 to 10
        if random.random() < DONE_LIKELIHOOD:  # 30% chance to stop early
            break  # Stop the loop immediately
        print(num)
    
    print("I'm done.")

# Run the function
chaotic_counting()

import random

def chaotic_counting():
   
    DONE_LIKELIHOOD = 0.3 

    print("I'm going to count until 10 or until I feel like stopping, whichever comes first.")
    
    for num in range(1, 11): 

        if random.random() < DONE_LIKELIHOOD:  

            break 

        print(num)
    
    print("I'm done.")

chaotic_counting()

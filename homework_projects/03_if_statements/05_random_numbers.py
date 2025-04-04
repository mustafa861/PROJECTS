import random

def random_num():
    """ A program  to Print 10 random numbers between 1 and 100."""
    for _ in range(10):  # Loop 10 times
        print(random.randint(1, 100))  # Generate and print a random number

if __name__ == '__main__':
    random_num()

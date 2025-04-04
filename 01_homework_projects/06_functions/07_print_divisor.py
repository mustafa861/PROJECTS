
def print_divisors(num: int):
    """Print all divisors of a number with no remainder."""  
    for i in range(1, num + 1):  # Loop through numbers from 1 to num (inclusive)
        if num % i == 0:  # Check if 'i' is a divisor of 'num' (i.e., num divided by i gives remainder 0)
            print(i, end=" ")  # Print the divisor, keeping everything on the same line

def main():
    numb = int(input("Enter a number: "))  # Take user input as a string, then convert it to an integer
    print("Divisors of", numb, "are:", end=" ")  # Print a message before listing the divisors
    print_divisors(numb)  # Call the function to print all divisors of 'numb'

if __name__ == '__main__':  # Ensures the script runs only when executed directly, not when imported
    main()  # Calls the main function to start the program
    
    
def in_range(n: int, low: int, high: int) -> bool:
    """Returns True if n is between low and high (inclusive)."""
    return low <= n <= high  # Simplified condition

def main():
    """Gets input from the user and checks if the number is in range."""
    n = int(input("Enter a number: "))
    low = int(input("Enter the lower bound: "))
    high = int(input("Enter the upper bound: "))

    if in_range(n, low, high):  # Calls the function
        print(f"{n} is in the range [{low}, {high}].")
    else:
        print(f"{n} is NOT in the range [{low}, {high}].")

if __name__ == '__main__':
    main()  # Call main() when the script runs

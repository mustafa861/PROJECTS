def main():
    """Asks the user to enter a number, doubles it until the value reaches 100 or more."""
    user_number = int(input("Enter a number to be doubled: "))  # Convert input to integer

    while user_number < 100:  # Keep doubling until 100 or more
        user_number *= 2  # Double the number once it will cross 100 it will stops
        print(f"Doubled value: {user_number}")  # Print the result

if __name__ == '__main__':
    main()

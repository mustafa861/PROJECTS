MIN_HEIGHT: int = 50  # Minimum height requirement

def main():
    """ A program to check if the user meets the minimum height requirement."""
    user_height = float(input(" Please Enter your height: "))

    if user_height >= MIN_HEIGHT:
        print("You meet the height requirement for the ride!")
    else:
        print("Sorry, you do not meet the height requirement for the ride.")

if __name__ == '__main__':
    main()

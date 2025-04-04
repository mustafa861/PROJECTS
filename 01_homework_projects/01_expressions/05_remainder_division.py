def main():
    """A program that asks the user for two numbers, divides the first number by the second, 
    and calculates the remainder of the division."""
    
    # Get user input
    dividend = int(input("Enter the dividend (number to be divided): "))
    divisor = int(input("Enter the divisor (number to divide by): "))

    # Perform calculations
    quotient = dividend // divisor  # Integer division
    remainder = dividend % divisor  # Modulo (remainder)

    # Display results
    print("\n=== Division Result ===")
    print(f"{dividend} ÷ {divisor} = {quotient} ")
    print(f"The Quotient for {dividend} divided by {divisor} is {quotient} and Remainder is {remainder}")


if __name__ == '__main__':
    main()

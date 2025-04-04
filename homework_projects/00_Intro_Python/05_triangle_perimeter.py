def main():
    """A program to prompt the user to enter the lengths of each side of a triangle 
    and then calculate and print the perimeter of the triangle."""
    
    # Taking input and converting to float
    length_side1 = float(input("Enter first side length: "))
    length_side2 = float(input("Enter second side length: "))
    length_side3 = float(input("Enter third side length: "))

    # Calculating perimeter
    perimeter = length_side1 + length_side2 + length_side3

    # Displaying the result
    print(f"\nThe perimeter of the triangle is {perimeter}\n")

# Ensuring the function runs only when the script is executed directly
if __name__ == '__main__':
    main()
 
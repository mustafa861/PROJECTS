def count_even():
    """Prompts the user for integers and counts the number of even numbers in the list."""
    num_list = []  # Create an empty list
    count = 0  # Initialize even number count

    while True:  # Loop to get user input until they stop
        user_input = input("Enter an integer (or press Enter to stop): ")

        if user_input == "":  # If the user presses Enter, stop taking input
            break
        
        try:
            number = int(user_input)  # Convert input to integer
            num_list.append(number)  # Add number to list
            
            if number % 2 == 0:  # Check if the number is even
                count += 1  # Increment count of even numbers
                
        except ValueError:  # Handle non-integer inputs
            print("Please enter a valid integer.")
    
    print(f"Number of even numbers entered: {count}")

# Run the function
if __name__ == '__main__':
    count_even()

def numbers_added(numberss: list[int]):
    """
    A function that takes a list of numbers and returns the sum of those numbers.
    
    Parameters:
    numberss (list[int]): A list of integers.

    Returns:
    int: The sum of all numbers in the list.
    """

    total_numbers: int = 0  # Initialize the total sum as 0

    for number in numberss:  # Loop through each number in the list
        total_numbers += number  # Add the current number to total_numbers

    return total_numbers  # Return the final sum

def main():
    """
    The main function that creates a list of numbers, 
    calls numbers_added() to find the sum, and prints the result.
    """

    numbers: list[int] = [1, 2, 3, 4, 5]  # Define a list of numbers
    sum_of_numbers: int = numbers_added(numbers)  # Call numbers_added() and store the sum
    print(sum_of_numbers)  # Print the sum of numbers
   
    # we can add as many lists as we want by using numbers_added function again and again  
    no:list[int] =[67,87,87]
    sum:int=numbers_added(no)
    print(sum)

# This ensures the script runs only when executed directly
if __name__ == '__main__':
    main()

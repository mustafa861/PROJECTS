def double_list(numbers: list[int]):
    """
    A function that takes a list of numbers and returns a new list 
    where each number is doubled.
    
    Parameters:
    numbers (list[int]): A list of integers.
    
    Returns:
    list[int]: A new list with each number doubled.
    """
    doubled_numbers = [number * 2 for number in numbers]  # Double each number in the list
    return doubled_numbers  # Return the new list


def main():
    """
    The main function that creates a list of numbers,
    calls double_list() to get the doubled numbers, and prints them.
    """
    numbers_list: list[int] = [2, 3, 4, 5, 6,7]  # Define a list of numbers
    doubled_result = double_list(numbers_list)  # Call double_list() and store result
    print(doubled_result)  # Print the doubled list



if __name__ == '__main__':
    main()
    
    


def double_list(numbers: list[int]):

    doubled_numbers = [number * 2 for number in numbers]  # Double each number in the list

    return doubled_numbers  # Return the new list

    numbers_list: list[int] = [2, 3, 4, 5, 6,7]  # Define a list of numbers

    doubled_result = double_list(numbers_list)  # Call double_list() and store result

    print(doubled_result)  # Print the doubled list

def get_user_numbers():
    """
    Ask the user to input numbers and store them in a list."""
    user_numbers = []
    while True:
        user_input = input("Enter a number (or press Enter to stop): ")
        
        if user_input == "": 
            break
        
        if user_input.lstrip('-').isdigit():  # Check if input is a valid number (including negatives)
            user_numbers.append(int(user_input))
        else:
            print("Invalid input. Please enter a valid number.")
    
    return user_numbers

def count_nums(num_lst):
    """
    Count occurrences of each number in a list using a dictionary.
    """
    num_dict = {}
    for num in num_lst:
        num_dict[num] = num_dict.get(num, 0) + 1  # Cleaner way to count occurrences
    
    return num_dict

def print_counts(num_dict):
    """
    Print each number and its count.
    """
    for num, count in num_dict.items():
        print(f"{num} appears {count} times.")  # Using f-strings for better readability

def main():
    """
    Collect numbers from the user and print their frequency.
    """
    user_numbers = get_user_numbers()
    num_dict = count_nums(user_numbers)
    print_counts(num_dict)

if __name__ == '__main__':
    main()

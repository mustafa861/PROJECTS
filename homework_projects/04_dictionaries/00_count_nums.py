
def get_user_numbers():
    
    user_numbers = []

    while True:

        user_input = input("Enter a number (or press Enter to stop): ")
        
        if user_input == "": 

            break
        
        if user_input.lstrip('-').isdigit():  

            user_numbers.append(int(user_input))

        else:

            print("Invalid input. Please enter a valid number.")
    
    return user_numbers

def count_nums(num_lst):

    num_dict = {}
    
    for num in num_lst:
    
        num_dict[num] = num_dict.get(num, 0) + 1  
    
    return num_dict

def print_counts(num_dict):
    
    for num, count in num_dict.items():
    
        print(f"{num} appears {count} times.")  


    user_numbers = get_user_numbers()
    num_dict = count_nums(user_numbers)
    print_counts(num_dict)


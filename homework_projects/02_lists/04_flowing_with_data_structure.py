# 1st sir zia's method
# def add_three_copies(my_list, data):
#     for i in range(3):
#         my_list.append(data)

# def main():
#     message = input("Enter a message to copy: ")
#     my_list = []
#     print("List before:", my_list)
#     add_three_copies(my_list, message)
#     print("List after:", my_list)

# if __name__ == "__main__":
#     main()
# 2nd method

def add_three_copies(data):
    """A program to take user input as a list and copy it three times and show before and after list"""
    return [data] * 3  # Creates a list with three copies of data

def main():
    message = input("Enter a message to copy: ")
    my_list = [] 
    print("List before:", my_list)
    my_list = add_three_copies(message)  # Assigns the new list with three copies
    print("List after:", my_list)

if __name__ == "__main__":
    main()

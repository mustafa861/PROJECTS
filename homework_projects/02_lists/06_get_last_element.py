def user_list():
    """Gets a list from the user and prints the last element."""
    lst = []  
    while True:
        element = input("Enter an element of the list or press Enter to stop: ")
        if element == "":
            break  # Stop taking input when the user presses Enter
        lst.append(element)
        print("List:", lst)  

    if lst:
        print("Last Element:", lst[-1])  # Print the last element if the list is not empty
    else:
        print("The list is empty!")  # No need for extra logic here

# Run the function
user_list()

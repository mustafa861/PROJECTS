def get_first_element(lst):
    """
    Prints the first element of a provided list.
    """
    if lst:
        print("First element:", lst[0])
    else:
        print("The list is empty!")

def get_lst():
    """
    Prompts the user to enter one element of the list at a time and returns the resulting list.
    """
    lst = []
    elem: str = input("Please enter an element of the list or press Enter to stop: ")
    while elem != "":
        lst.append(elem)   
        print("Current list:", lst)  # Print the list after appending an element
        elem = input("Please enter an element of the list or press Enter to stop: ")
    return lst

def main():
    lst = get_lst()
    get_first_element(lst)

if __name__ == '__main__':
    main()

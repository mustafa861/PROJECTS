
def get_first_element(lst):
   
    if lst:
        print("First element:", lst[0])
    else:
        print("The list is empty!")

def get_lst():
   
    lst = []
    elem: str = input("Please enter an element of the list or press Enter to stop: ")
    while elem != "":
        lst.append(elem)   
        print("Current list:", lst) 
        elem = input("Please enter an element of the list or press Enter to stop: ")
    return lst

    lst = get_lst()
   
    get_first_element(lst)


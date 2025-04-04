
def user_list():
    
    lst = []  

    while True:
    
        element = input("Enter an element of the list or press Enter to stop: ")
    
        if element == "":
    
            break  
    
        lst.append(element)
    
        print("List:", lst)  

    if lst:
    
        print("Last Element:", lst[-1])  
    else:
    
        print("The list is empty!")  

user_list()

max_length=5
def shorten_list():
    """ A program shorten(list) which removes elements from the end of lst,and show the elemnt and list too"""
    user_list=[]
    while True:
        elem=(input("Enter the list value or press enter to stop"))
        if elem == "":
            break
        user_list.append(elem)
    print(user_list)
    
    # now removing from the last elemnt if the lenght is more tha 5
    # we use while instead of if bcz "while" will continue removing till the max length achieved
    # but "if" will remove only once
    # if len(user_list) >= max_length:
    while len(user_list) > max_length:
        removed_list=user_list.pop()
        #  [:: -1]removed elements appear in the order they were originally entered.
        print(f"Removed_elements:" ,removed_list)
        
       
    if user_list:    
        print("Final_list:" , user_list)
    else:
        print("No values added in the list")    
if __name__ == '__main__':
    shorten_list()

# removed_elements.append(user_list.pop())  # Store removed elements so ife want them in a list we sholud use this
     
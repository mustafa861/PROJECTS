def main():
    """program which continuously asks the user to enter values which are added one by one into a list.
    When the user presses enter without typing anything, print the list."""
        
    user_Input_list=[]
    while True:
        elemnts=(input("Enter the list value "))
        user_Input_list.append(elemnts)
        if elemnts == "" :
            break
       
    if user_Input_list:
         print("list:",user_Input_list)
    else:
        print(" No list values")
    
        
if __name__ == '__main__':
        main()        


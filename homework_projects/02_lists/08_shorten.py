
max_length=5

def shorten_list():
    
    user_list=[]

    while True:

        elem=(input("Enter the list value or press enter to stop"))

        if elem == "":

            break

        user_list.append(elem)
   
    print(user_list)
    
    while len(user_list) > max_length:
    
        removed_list=user_list.pop()
      
        print(f"Removed_elements:" ,removed_list)
           
    if user_list:    
        
        print("Final_list:" , user_list)
    
    else:
        
        print("No values added in the list")    

     
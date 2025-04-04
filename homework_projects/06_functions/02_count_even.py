
def count_even():
   
    num_list = [] 
    
    count = 0  
    
    while True:  
    
        user_input = input("Enter an integer (or press Enter to stop): ")

        if user_input == "":  

            break
        
        try:
            number = int(user_input)  

            num_list.append(number) 
            
            if number % 2 == 0:  

                count += 1  
                
        except ValueError: 

            print("Please enter a valid integer.")
    
    print(f"Number of even numbers entered: {count}")

count_even()

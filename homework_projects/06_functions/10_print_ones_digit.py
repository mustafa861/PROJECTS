def print_ones_digit(value): 
  
    return value % 10  

user_input = int(input("Enter a number: "))  

ones_digit = print_ones_digit(user_input) 

print(f"The ones digit is {ones_digit}")  

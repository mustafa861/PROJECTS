def print_ones_digit(value): 
    return value % 10  

def main():
    user_input = int(input("Enter a number: "))  
    ones_digit = print_ones_digit(user_input)  # Passing user_input inside the function and saving it in a variable
    print(f"The ones digit is {ones_digit}")  

if __name__ == '__main__':
    main()

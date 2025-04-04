def curr_val(num:int):
    """A program that asks a user to enter a number. Your program will then double that
    number until the value is 100 or greater and print it."""
    return num*2 
def main():
    user_number=int(input("Enter a number you want to double"))
    while user_number < 100:
        double_val=curr_val(user_number)
    # curr_value=num*2
        print(f"double_val={double_val}")
        user_number=double_val
if __name__ == '__main__':
    main()
   
    
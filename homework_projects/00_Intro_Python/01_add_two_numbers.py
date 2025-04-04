   
def main():
        """This function takes two numbers as input,
            adds them, and prints the sum."""
print("This program adds two numbers.")
    
    # Taking input and converting to integers
user_input1:str=(input("Enter the first number: "))
num1:int=int(user_input1)
    
user_input2:str=(input("Enter the second number: "))
num2:int=int(user_input2)

    # Calculating sum
sum = num1 + num2

    # Displaying the result using f-string
print(f"The sum of {num1} and {num2} is {sum}.")

# Ensures the main function runs only when the script is executed directly
if __name__ == '__main__':
    main()


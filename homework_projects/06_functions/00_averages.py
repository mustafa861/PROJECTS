# simple average code
# def main():
#     """ a function that takes two numbers and finds the average between the two."""
#     user_input_1:int=input("Enter a number:")
#     user_input_2:int=input("Enter a number:")
#     avg=user_input_1 + user_input_2 
#     avg=int(avg)
#     avgg=avg/2
#     print(avgg)
# if __name__ == '__main__':
#     main()

""" second code using function for multiple numbers average"""


# Function to calculate the average of two numbers
def calculate_average(num1: float, num2: float):
    """Returns the average of two numbers."""
    total = num1 + num2
    return total / 2

def main():
    """Computes multiple averages and then finds their average."""
    first_avg = calculate_average(0, 10)
    second_avg = calculate_average(8, 10)

    final_avg = calculate_average(first_avg, second_avg)

    print("First Average:", first_avg)
    print("Second Average:", second_avg)
    print("Final Average:", final_avg)

if __name__ == '__main__':
    main()

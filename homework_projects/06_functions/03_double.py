def double_num(num: int):
    return num * 2
""" A program that takes input from user and uses double(num) function to return the result ofinput multiplying num by 2"""


def main():
    try:
        num = int(input("Enter a number: ")) 
        num_doubled = double_num(num)
        print(f"The double of {num} is {num_doubled}")
    except ValueError:  # Handle non-integer inputs
        print("Please enter a valid integer.")
    

if __name__ == '__main__':
    main()
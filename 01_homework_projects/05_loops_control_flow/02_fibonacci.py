max_value:int =10000
def main():
    """Write a program to print terms in the Fibonacci sequence up to a maximum value 10,000"""
    current_value=0
    next_value=1
    while current_value <= max_value:
        print(current_value)
        value_after_next = current_value + next_value 
        current_value = next_value
        next_value = value_after_next
if __name__ == '__main__':
    main()
#Stops at 6765 because the next value (10946) is greater than 10,000.
def double_num(num: int):

    return num * 2



try:

    num = int(input("Enter a number: ")) 

    num_doubled = double_num(num)

    print(f"The double of {num} is {num_doubled}")

except ValueError:  
    
    print("Please enter a valid integer.")


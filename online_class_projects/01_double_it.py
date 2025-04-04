def curr_val(num:int):

    return num*2 


user_number=int(input("Enter a number you want to double: "))

while user_number < 100:

    double_val=curr_val(user_number)

    print(f"double_val={double_val}")

    user_number=double_val

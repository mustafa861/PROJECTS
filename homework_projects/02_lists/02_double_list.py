
def double_list(numbers: list[int]):

    doubled_numbers = [number * 2 for number in numbers]  

    return doubled_numbers  

numbers_list: list[int] = [2, 3, 4, 5, 6,7] 

doubled_result = double_list(numbers_list) 

print(doubled_result)  

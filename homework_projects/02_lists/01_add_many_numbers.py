
def numbers_added(numberss: list[int]):

    total_numbers: int = 0 

    for number in numberss:

        total_numbers += number 

    return total_numbers  

    numbers: list[int] = [1, 2, 3, 4, 5]  
    
    sum_of_numbers: int = numbers_added(numbers)  
    
    print(sum_of_numbers)  
   
    no:list[int] =[67,87,87]
    
    sum:int=numbers_added(no)
    
    print(sum)

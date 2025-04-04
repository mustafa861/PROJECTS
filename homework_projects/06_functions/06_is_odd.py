max_num:list=list(range(11,20))

def is_odd(num:int):

    return num % 2 != 0 

    for num in max_num:
        if is_odd(num):
         print(f"{num} is odd") 
        else:
            print(f"{num} is even")
        

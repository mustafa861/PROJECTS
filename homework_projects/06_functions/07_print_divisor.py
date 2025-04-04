
def print_divisors(num: int):

    
    for i in range(1, num + 1):  
    
        if num % i == 0:  
    
            print(i, end=" ")  


    numb = int(input("Enter a number: ")) 

    print("Divisors of", numb, "are:", end=" ")  

    print_divisors(numb)  
    
    
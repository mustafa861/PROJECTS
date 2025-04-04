def print_multiples(message: str, repeat_count: int) -> str:
   
    return message * repeat_count


message: str = input("Enter a message: ")
 
repeat_count: int = int(input("Enter the number of times to repeat: "))
    
result = print_multiples(message, repeat_count)

print(result)


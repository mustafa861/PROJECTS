def print_multiples(message: str, repeat_count: int) -> str:
    """ A program to Returns the message repeated multiple times."""
    return message * repeat_count

def main():
    message: str = input("Enter a message: ")
    repeat_count: int = int(input("Enter the number of times to repeat: "))
    
    result = print_multiples(message, repeat_count)
    print(result)

if __name__ == '__main__':  
    main()

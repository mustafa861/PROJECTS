def main():
    """this function ask the user to enter favourite animal and 
    then responding the user that your favourite animal is also same as
    the user input"""
    user_input:str=input("Enter your favourite animal ? \t")
    print(f"your favourite animal is {user_input}")
    
    print(f"\nMy favourite animal is also {user_input}!\n")
    
if __name__ == '__main__':

    main()
# def jokebot():
#     """A program to  Call the function to get the joke"""
#     return "hey he hey"  

# def main():
#     joke = jokebot()  # Call the function to get the joke
#     prompt = input("What do you want to print? ")

#     if prompt.lower() == "joke":  
#         print(joke)
#     else:
#         print("Sorry, I only print jokes.")

# if __name__ == '__main__':
#     main()

# second way
prompt:str="What do you Want to print?"
joke:str="Why do Java developers wear glasses?Because they don’t C#! 😆👓"
sorry:str="Sorry ! I only print jokes"
def main():
    user_input=input(prompt)
    # print(prompt)
    if user_input == "joke":
        print(joke)
    else:
        print(sorry)
if __name__ == '__main__':
    main()

        


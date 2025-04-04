def main():
 """ A program that prompts the user for a number and print its square (the product of the number times itself)."""
 user_input:int=int(input ("Enter a number to square :"))
 square:int=(user_input*user_input)
 print(f"{user_input} square is {square}")

 if __name__ == '__main__':
     main()
 
 
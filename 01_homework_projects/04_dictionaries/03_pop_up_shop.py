
def main():
    """A simple program to calculate the total cost of fruits based on user input."""
    fruits = {
        'apple': 1.5, 
        'durian': 50, 
        'jackfruit': 80, 
        'kiwi': 1, 
        'rambutan': 1.5, 
        'mango': 5
    }
    
    total_cost = 0

    for fruit_name, price in fruits.items():  # Iterate cleanly using .items()
        amount_bought = input(f"How many ({fruit_name}) do you want to buy?: ").strip()
        while not amount_bought.isdigit():
            print("please enter a valid number of fruit")
            amount_bought = input(f"How many ({fruit_name}) do you want to buy?: ").strip()
    total_cost += price * int(amount_bought)

    print(f"Your total is ${total_cost:.2f}")  # Format total cost with two decimal places


# Run the program
if __name__ == '__main__':
    main()

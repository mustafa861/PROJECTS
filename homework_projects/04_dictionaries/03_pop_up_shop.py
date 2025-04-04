
fruits = {
        'dragon fruit': 1.5, 
        
        'banana': 50, 
        
        'jackfruit': 80, 
        
        'kiwi': 1, 
        
        'apple': 1.5, 
        
        'mango': 5
    }
    
total_cost = 0

for fruit_name, price in fruits.items():  

        amount_bought = input(f"How many ({fruit_name}) do you want to buy?: ").strip()

        while not amount_bought.isdigit():

            print("please enter a valid number of fruit")

            amount_bought = input(f"How many ({fruit_name}) do you want to buy?: ").strip()

total_cost += price * int(amount_bought)

print(f"Your total is ${total_cost:.2f}")  




fruits_in_stock = {

    "pear": 1000,

    "lychee": 800,

    "oranges": 0

}

def in_stock(fruit_name,fruits_in_stock):

    quantity = fruits_in_stock.get(fruit_name)  # Get quantity, returns None if not found
    
    if quantity is None:

        return f"{fruit_name.capitalize()} is not available in stock."

    elif quantity > 0:

        return f"{fruit_name.capitalize()} is available, quantity: {quantity}"

    return f"{fruit_name} is out of stock."


user_fruit = input("Enter the fruit you want to check in fruit stock: ").lower()
print(in_stock(user_fruit, fruits_in_stock))  # Directly print result

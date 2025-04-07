
import time
def main(cars_list = ["Toyota", "Honda", "Ford", "BMW", "Audi", "Mercedes"]):
    """ A program to create a list called cars_list, print its length, 
    add 'Fortuner' in the list and print the updated list."""
    
    # Print the length of the car list
    cars_length = len(cars_list)
    print(f"Length of cars list: {cars_length}")

    # Add 'Fortuner' at the end of the list
    cars_list.append('Bugati')

    # Print the updated list
    print("\nUpdated car list:")
    for car in cars_list:
        time.sleep(1)
        print(car)
if __name__ == '__main__':
    main()  # Calling the main function

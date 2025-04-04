greeting = "Hello, Eid Mubarak"  # Global greeting message

def greet(name: str):
    """Returns a greeting message with the given name."""
    return f"{greeting}, {name}!"  # Corrected to return a full greeting

def main():
    """Asks the user for their name and calls greet()."""
    person_name = input("Enter your name: ")  # Get user input
    greets = greet(person_name)  # Corrected function call
    print(greets)  # Print the returned greeting message

if __name__ == '__main__':
    main()

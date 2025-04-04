def data():
    """A program to create a student list, save data, print it, and look up student details."""
    studentsList = {}  # Create an empty dictionary to store student names and numbers
    
    while True:  # Infinite loop to take user input continuously
        name = input("Enter name or press Enter to stop: ").strip()  # Remove extra spaces
        if not name:  # Stop if user enters nothing
            break
        
        number = input(f"Enter number for {name}: ").strip()  # Ask for the student's number
        studentsList[name] = number  # Store name-number pair in the dictionary
    
    return studentsList  # Return the completed student list


def print_data(studentsList):
    """Prints the student list in a formatted way."""
    if not studentsList:  # Check if the dictionary is empty
        print("List not found")
        return
    
    # Loop through dictionary and format output correctly
    for name, number in studentsList.items():
        print(f"The student {name} has this roll number: {number}")  # Print directly


def lookup_data(studentsList):
    """Find a student by their roll number."""
    while True:
        name = input("\nEnter a name to look up (or press Enter to stop): ").strip()
        if not name:  # Stop the loop if the user presses Enter
            break
        if name in studentsList:
            print(f"{name} is in the student list with roll number {studentsList[name]}")
        else:
            print(f"{name} is not in the student list.")  


def main():
    students_data = data()  # Collect student data
    print("\nStudent List:")
    print_data(students_data)  # Call function correctly
    lookup_data(students_data)  # Call function correctly


# Run the program
if __name__ == '__main__':
    main()

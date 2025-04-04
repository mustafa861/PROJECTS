def data():
    """A program to create students list save ,print and find out later any student detail"""
    # Create an empty dictionary to store student names and numbers
    studentsList = {}
    
    while True:  # Infinite loop to take user input continuously
        name = input("Enter name or press Enter to stop: ").strip()  # Remove extra spaces from input
        if not name:  # If the user presses Enter without typing a name, break the loop
            break
        
        number = input(f"Enter number for {name}: ").strip()  # Ask for the student's number
        studentsList[name] = number  # Store name-number pair in the dictionary
    
    return studentsList  # Return the completed student list

    
def print_data(studentsList):
    # Check if the dictionary is empty
    if not studentsList:
        print("List not found")
        return
    
    # Loop through dictionary and format output
    for name, number in studentsList.items():  # Fixed .items() to properly iterate over dictionary
        print( f"The student {name} has this roll number: {number}")
        
def lookup_data(studentsList):
    """ find out a student with it roll no"""
    while True:
        name = input("\nEnter a name to look up (or press Enter to stop): ").strip()
        if not name:
            break
        if name in studentsList:
            print(f"{name} is in the studentlist having roll no{studentsList[name]}")
        else:
            print(f"{name} is not in the studentsList.")  
              
        
        
def main():
    students_data = data()  # Collect student data
    print_data(students_data)
    lookup_data(students_data)
    
if __name__ == '__main__':
    main()

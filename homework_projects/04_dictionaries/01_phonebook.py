studentsList = {}      

while True:
   
    name = input("Enter name or press Enter to stop: ").strip()
   
    if not name:
   
        break
    
    number = input(f"Enter number for {name}: ").strip()
   
    studentsList[name] = number  

print("\n=== Student List ===")

for name, number in studentsList.items():

    print(f"{name}: {number}")

def print_data(studentsList):

    if not studentsList:  

        print("List not found")

        return
    
    for name, number in studentsList.items():

        print(f"The student {name} has this roll number: {number}")  

def lookup_data(studentsList):

    while True:

        name = input("\nEnter a name to look up (or press Enter to stop): ").strip()

        if not name:

            break
        
        if name in studentsList:

            print(f"{name} is in the student list with roll number {studentsList[name]}")

        else:

            print(f"{name} is not in the student list.")  

    students_data = studentsList  

    print("\nStudent List:")

    print_data(students_data)  

    lookup_data(students_data)  


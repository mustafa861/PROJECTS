
def data():
    
    studentsList = {}
    
    while True:  
       
        name = input("Enter name or press Enter to stop: ").strip()  
        
        if not name: 
            break
        
        number = input(f"Enter number for {name}: ").strip() 
        
        studentsList[name] = number  
    
    return studentsList  
    
def print_data(studentsList):
  
    if not studentsList:
        
        print("List not found")
        
        return
    
   
    for name, number in studentsList.items(): 
        
        print( f"The student {name} has this roll number: {number}")
        
def lookup_data(studentsList):
    
    while True:
    
        name = input("\nEnter a name to look up (or press Enter to stop): ").strip()
    
        if not name:
    
            break
    
        if name in studentsList:
    
            print(f"{name} is in the studentlist having roll no{studentsList[name]}")
    
        else:
    
            print(f"{name} is not in the studentsList.")  
              
        
        

    students_data = data()  

    print_data(students_data)

    lookup_data(students_data)
    

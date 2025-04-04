greeting = "Hello, Eid Mubarak" 

def greet(name: str):
    
    return f"{greeting}, {name}!"  

   
person_name = input("Enter your name: ")  

greets = greet(person_name)  

print(greets)  


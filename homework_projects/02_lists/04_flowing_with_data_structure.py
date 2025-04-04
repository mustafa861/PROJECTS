
def add_three_copies(data):

    return [data] * 3  

message = input("Enter a message to copy: ")

my_list = [] 

print("List before:", my_list)

my_list = add_three_copies(message)  

print("List after:", my_list)

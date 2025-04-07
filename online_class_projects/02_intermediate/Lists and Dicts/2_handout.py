def access_elem(list_items, indexno):
    try:
        return list_items[indexno]
    except IndexError:
        return "Index out of range."

def modify_elem(list_items, indexno, new_elem):
    try:
        list_items[indexno] = new_elem  # Modify the element at the specified index
        return f"Element at index {indexno} updated to '{new_elem}'."
    except IndexError:
        return "Index out of range."
      
def slice_list(list_items , start ,end):
    try:
        start = int(start)
        end = int(end)
        return list_items[start :end] 
    except IndexError:
        return "Invalid Indicies."

def index_game():
    list_items =  ["Transport", "Fruits", "Vegetables", "Technology", "Nature", "Books"] # Example list
    print("Current list:", list_items)
    print("Choose an operation: access, modify, slice")
    options = input("Select an  option: ").strip().lower()
    if options == "access":
        index = int(input("Enter index to access: "))
        print(access_elem(list_items ,index))
    elif options == "modify":
        index=int(input("Enter index no you want to modify: "))
        new_value = input("Enter new value: ")
        print(modify_elem(list_items,index ,new_value))
        print(f"Modiified list={list_items}")
    elif options == "slice":
        start=input("Enter index no to start")
        end=input("Enter index no to end")
        sliced=(slice_list(list_items ,start,end))
        print(list_items)
        print(sliced)
    else:
        print("Invalid operation.")

index_game()    


        
max_value:int =10000

current_value=0

next_value=1

while current_value <= max_value:

        print(current_value)

        value_after_next = current_value + next_value 

        current_value = next_value

        next_value = value_after_next

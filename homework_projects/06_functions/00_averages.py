

def calculate_average(num1: float, num2: float):
 
    total = num1 + num2
 
    return total / 2
 
first_avg = calculate_average(0, 10)
second_avg = calculate_average(8, 10)

final_avg = calculate_average(first_avg, second_avg)

print("First Average:", first_avg)
print("Second Average:", second_avg)
print("Final Average:", final_avg)

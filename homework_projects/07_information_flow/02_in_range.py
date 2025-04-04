def in_range(n: int, low: int, high: int) -> bool:
    
    return low <= n <= high



n = int(input("Enter a number: "))

low = int(input("Enter the lower bound: "))

high = int(input("Enter the upper bound: "))

if in_range(n, low, high):  # Calls the function

    print(f"{n} is in the range [{low}, {high}].")

else:

    print(f"{n} is NOT in the range [{low}, {high}].")

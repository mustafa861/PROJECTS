def is_adult(age: int) :
    """Checks if the given age is adult age (18 or older)."""
    return age >= 18  # Returns True if 18 or older

def main():
    user_age = int(input("Enter your age: "))  # Get age from user
    age = is_adult(user_age)  # ✅ Pass 'user_age' to function

    if age:  
        print("Entered age is adult age.")  
    else:
        print("Entered age is not an adult age.")  

if __name__ == '__main__':
    main() 

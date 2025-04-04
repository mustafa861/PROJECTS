def is_adult(age: int) :
 
    return age >= 18  


user_age = int(input("Enter your age: "))  # Get age from user

age = is_adult(user_age)  # ✅ Pass 'user_age' to function

if age:  

    print("Entered age is adult age.")  

else:

    print("Entered age is not an adult age.") 

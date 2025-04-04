def get_user_info():
    
    return {
        
        "first_name": input("What is your first name?: "),
        
        "last_name": input("What is your last name?: "),
        
        "email_address": input("What is your email address?: ")
    }  

user_data = get_user_info()

print("Received the following user data:", user_data)  


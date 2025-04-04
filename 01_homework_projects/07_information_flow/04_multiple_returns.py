def get_user_info():
    return {
        "first_name": input("What is your first name?: "),
        "last_name": input("What is your last name?: "),
        "email_address": input("What is your email address?: ")
    }  # Returns a dictionary

def main():
    user_data = get_user_info()
    print("Received the following user data:", user_data)  # Prints a dictionary

if __name__ == "__main__":
    main()

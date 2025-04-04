
from hashlib import sha256

def hash_password(password):

    return sha256(password.encode()).hexdigest()

stored_logins = {

    "example@gmail.com": hash_password("password123"),  

    "user2@yahoo.com": hash_password("helloWorld"),

    "admin@test.com": hash_password("admin123")
}

def login(email, password):

    if email in stored_logins and stored_logins[email] == hash_password(password):

        return "✅ Login successful!"

    else:

        return "❌ Invalid email or password."

print(login("example@gmail.com", "password123"))  
print(login("user2@yahoo.com", "wrongpass"))      
print(login("not_in_list@test.com", "hello"))     
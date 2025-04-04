from hashlib import sha256

# Function to hash passwords
def hash_password(password):
    """Fill out the login(...) function for a website that hashes their passwords. Login should return True
    if an email's stored password hash in stored_logins is the same as the hash of password_to_check."""
    return sha256(password.encode()).hexdigest()

# Stored emails and **hashed** passwords
stored_logins = {
    "example@gmail.com": hash_password("password123"),  
    "user2@yahoo.com": hash_password("helloWorld"),
    "admin@test.com": hash_password("admin123")
}

def login(email, password):
    """Check if email and password match the stored hashed password."""
    if email in stored_logins and stored_logins[email] == hash_password(password):
        return "✅ Login successful!"
    else:
        return "❌ Invalid email or password."

# Test the login system
print(login("example@gmail.com", "password123"))  # ✅ Correct password
print(login("user2@yahoo.com", "wrongpass"))      # ❌ Wrong password
print(login("not_in_list@test.com", "hello"))     # ❌ Email not found

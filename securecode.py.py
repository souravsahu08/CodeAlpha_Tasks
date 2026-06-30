import hashlib

print("=== Secure Login System ===")

username = input("Enter username: ")
password = input("Enter password: ")

# Hash user entered password
hashed_password = hashlib.sha256(password.encode()).hexdigest()

# Stored secure credentials
stored_username = "admin"
stored_password = hashlib.sha256("Admin@123".encode()).hexdigest()

# Authentication
if username == stored_username and hashed_password == stored_password:
    print("Login Successful")
else:
    print("Invalid Credentials")

print("Security Check Completed")
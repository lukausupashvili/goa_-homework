def is_valid_email(email):
    """Simple email validation."""
    return "@" in email and "." in email

def is_valid_password(password):
    """Check if the password meets the criteria."""
    return len(password) >= 6

def register_user():
    """User registration function."""
    print("Welcome to the Registration System!")

    while True:
        username = input("Enter your username: ")
        if len(username) < 3:
            print("Username must be at least 3 characters long. Please try again.")
            continue

        email = input("Enter your email: ")
        if not is_valid_email(email):
            print("Invalid email format. Please try again.")
            continue

        password = input("Enter your password (minimum 6 characters): ")
        if not is_valid_password(password):
            print("Password too short. Please try again.")
            continue

        confirm_password = input("Confirm your password: ")
        if password != confirm_password:
            print("Passwords do not match. Please try again.")
            continue

        print("Registration successful!")
        
        break

if __name__ == "__main__":
    register_user()
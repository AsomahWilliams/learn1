import re

def validate_username(username):
    """Validate the username."""
    if len(username) < 5:
        raise ValueError("Username should be at least 5 characters long.")
    return username

def validate_password(password):
    """Validate the password."""
    if not re.search(r"\d", password):
        raise ValueError("Password should contain at least one number.")
    if not re.search(r"[^A-Za-z0-9]", password):
        raise ValueError("Password should contain at least one special character.")
    return password

def get_user_input():
    """Get user input and validate it."""
    while True:
        username = input("Enter your username: ")
        try:
            validate_username(username)
            break
        except ValueError as e:
            print(e)

    while True:
        password = input("Enter your password: ")
        try:
            validate_password(password)
            break
        except ValueError as e:
            print(e)

    return username, password

def main():
    """Main function."""
    username, password = get_user_input()
    print("Registration successful!")
    print(f"Username: {username}")
    print(f"Password: {'*' * len(password)}")

if __name__ == "__main__":
    main()
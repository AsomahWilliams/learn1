import re

def check_password_strength(password):
    # Check if the password is at least 8 characters long
    if len(password) < 8:
        return False

    # Check if the password contains both uppercase and lowercase letters
    if not re.search("[a-z]", password) or not re.search("[A-Z]", password):
        return False

    # Check if the password includes at least one number
    if not re.search("[0-9]", password):
        return False

    return True

def main():
    # Ask the user to input a password
    password = input("Enter a password: ")

    # Check the password strength
    if check_password_strength(password):
        print("Your password is strong.")
    else:
        print("Your password is weak. Please ensure it meets the following criteria:")
        print("* Be at least 8 characters long")
        print("* Contain both uppercase and lowercase letters")
        print("* Include at least one number")

if __name__ == "__main__":
    main()
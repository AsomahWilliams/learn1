def is_valid_email(email):
    """Check if the email contains '@' and '.' in the correct order."""
    if "@" in email and "." in email:
        at_index = email.index("@")
        dot_index = email.rindex(".")  # Using rindex to find the last '.'
        
        # Ensure '@' comes before the last '.' and they are not at the start or end
        if 0 < at_index < dot_index < len(email) - 1:
            return True
    return False

# Get user input
email = input("Enter your email address: ")

# Validate email and display result
if is_valid_email(email):
    print("Valid email address!")
else:
    print("Invalid email address. Please enter a proper email.")
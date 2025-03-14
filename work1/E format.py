def format_email_addresses(names):
    email_addresses = []
    domain = "@company.com"
    
    for name in names:
        # Split the name into first and last
        first_last = name.split()
        
        # Check if the name has both first and last parts
        if len(first_last) == 2:
            first, last = first_last
            # Format the email address
            email = f"{first.lower()}.{last.lower()}{domain}"
            email_addresses.append(email)
        else:
            print(f"Invalid name format: {name}")
    
    return email_addresses


if __name__ == "__main__":
    employee_names = [
        "John Doe",
        "Jane Smith",
        "Alice Johnson",
        "Bob Brown"
    ]
    
    formatted_emails = format_email_addresses(employee_names)
    
    # Print the formatted email addresses
    for email in formatted_emails:
        print(email)
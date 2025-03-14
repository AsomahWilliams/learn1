from datetime import datetime

def check_due_date(return_date):
    # Convert the return date string to a datetime object
    return_date_obj = datetime.strptime(return_date, "%Y-%m-%d")
    # Get today's date
    today = datetime.now()
    
    # Check if the book is overdue
    if return_date_obj < today:
        # Calculate the number of days overdue
        overdue_days = (today - return_date_obj).days
        return True, overdue_days
    else:
        return False, 0

def main():
    # Ask the user for the return date
    return_date = input("Enter the return date (YYYY-MM-DD): ")
    
    try:
        # Check if the book is overdue
        is_overdue, overdue_days = check_due_date(return_date)
        
        if is_overdue:
            print(f"The book is overdue by {overdue_days} days.")
        else:
            print("The book is not overdue.")
    
    except ValueError:
        print("Please enter a valid date in the format YYYY-MM-DD.")

if __name__ == "__main__":
    main()
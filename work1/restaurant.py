def calculate_tip(bill_amount, tip_percentage):
    """Calculate the tip amount."""
    tip_amount = (bill_amount / 100) * tip_percentage
    return tip_amount

def calculate_total_amount(bill_amount, tip_amount):
    """Calculate the total amount to be paid."""
    total_amount = bill_amount + tip_amount
    return total_amount

def main():
    """Main function."""
    print("Restaurant Tip Calculator")
    print("-------------------------")

    # Get the bill amount from the user
    while True:
        try:
            bill_amount = float(input("Enter the bill amount: $"))
            if bill_amount < 0:
                print("Bill amount cannot be negative.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    # Get the tip percentage from the user
    while True:
        try:
            tip_percentage = float(input("Enter the tip percentage (e.g., 10, 15, 20): %"))
            if tip_percentage < 0:
                print("Tip percentage cannot be negative.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    # Calculate the tip amount and the total amount
    tip_amount = calculate_tip(bill_amount, tip_percentage)
    total_amount = calculate_total_amount(bill_amount, tip_amount)

    # Display the results
    print("\nResults:")
    print(f"Bill Amount: ${bill_amount:.2f}")
    print(f"Tip Percentage: {tip_percentage}%")
    print(f"Tip Amount: ${tip_amount:.2f}")
    print(f"Total Amount: ${total_amount:.2f}")

if __name__ == "__main__":
    main()
def atm_withdrawal():
    # Get the initial balance from the user
    while True:
        try:
            balance = float(input("Enter your initial balance: $"))
            if balance < 0:
                print("Balance cannot be negative. Please try again.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    # Get the withdrawal amount from the user
    while True:
        try:
            withdrawal_amount = float(input("Enter the amount you want to withdraw: $"))
            if withdrawal_amount < 0:
                print("Withdrawal amount cannot be negative. Please try again.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    # Check if the withdrawal amount exceeds the available balance
    if withdrawal_amount > balance:
        print("Insufficient funds.")
    else:
        # Calculate and display the new balance after withdrawal
        new_balance = balance - withdrawal_amount
        print(f"Withdrawal successful. Your new balance is: ${new_balance:.2f}")

if __name__ == "__main__":
    atm_withdrawal()
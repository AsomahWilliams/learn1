def follower_growth_calculator():
    # Ask the user for the number of followers at the beginning and end of the month
    try:
        old_followers = int(input("Enter the number of followers at the beginning of the month: "))
        new_followers = int(input("Enter the number of followers at the end of the month: "))

        # Calculate the percentage growth
        if old_followers <= 0:
            print("The number of followers at the beginning of the month must be greater than zero.")
            return

        growth = ((new_followers - old_followers) / old_followers) * 100

        # Display the result
        if growth > 0:
            print(f"\nPercentage increase in followers: {growth:.2f}%")
        elif growth < 0:
            print(f"\nPercentage decrease in followers: {abs(growth):.2f}%")
        else:
            print("\nNo change in followers.")

    except ValueError:
        print("Invalid input. Please enter numeric values for the number of followers.")

# Example usage
if __name__ == "__main__":
    follower_growth_calculator()
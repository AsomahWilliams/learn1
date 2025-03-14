def shopping_cart():
    total_cost = 0.0

    print("Welcome to the Online Shopping Cart System!")
    print("Enter the price of each item. Type 'CHECKOUT' to finish and see the total cost.")

    while True:
        user_input = input("Enter item price (or 'CHECKOUT' to finish): ")

        if user_input.upper() == "CHECKOUT":
            break  # Exit the loop if the user types "CHECKOUT"

        try:
            price = float(user_input)  # Convert the input to a float
            if price < 0:
                print("Please enter a valid price (positive number).")
            else:
                total_cost += price  # Add the price to the total cost
        except ValueError:
            print("Invalid input. Please enter a numeric value for the price.")

    # Display the total cost
    print(f"\nTotal cost of items: ${total_cost:.2f}")

# Example usage
if __name__ == "__main__":
    shopping_cart()
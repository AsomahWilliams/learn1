def book_movie_tickets():
    # Get the number of tickets from the user
    while True:
        try:
            num_tickets = int(input("How many movie tickets do you want to buy? "))
            if num_tickets < 0:
                print("Number of tickets cannot be negative. Please try again.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    # Define the ticket price
    ticket_price = 12.0

    # Calculate the total amount to be paid
    total_amount = num_tickets * ticket_price

    # Apply a 10% discount if the user buys more than 4 tickets
    if num_tickets > 4:
        discount = 0.1 * total_amount
        total_amount -= discount
        print(f"You are eligible for a 10% discount. Your discount amount is: ${discount:.2f}")

    # Display the total amount to be paid
    print(f"\nNumber of Tickets: {num_tickets}")
    print(f"Ticket Price: ${ticket_price:.2f}")
    print(f"Total Amount: ${total_amount:.2f}")

if __name__ == "__main__":
    book_movie_tickets()
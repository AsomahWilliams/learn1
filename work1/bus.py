def calculate_bus_fare():
    # Get the user's age
    while True:
        try:
            age = int(input("Enter your age: "))
            if age < 0:
                print("Age cannot be negative. Please try again.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a valid age.")

    # Calculate the bus fare based on age
    if age < 5:
        fare = "Free"
    elif 5 <= age <= 18:
        fare = "$2.00"
    elif 19 <= age <= 60:
        fare = "$3.00"
    else:
        fare = "$1.50"

    # Print the bus fare
    print(f"Your bus fare is: {fare}")

if __name__ == "__main__":
    calculate_bus_fare()
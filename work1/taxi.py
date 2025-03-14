def calculate_taxi_fare():
    # Constants for fare calculation
    BASE_FARE = 3.00
    PER_MILE_RATE = 2.00

    # Ask the user for the number of miles traveled
    try:
        miles_traveled = float(input("Enter the number of miles traveled: "))
        
        if miles_traveled < 0:
            print("Please enter a valid number of miles (non-negative).")
            return
        
        # Calculate the total fare
        total_fare = BASE_FARE + (PER_MILE_RATE * miles_traveled)

        # Display the total fare
        print(f"\nTotal Fare: ${total_fare:.2f}")

    except ValueError:
        print("Invalid input. Please enter a numeric value for the miles traveled.")

# Example usage
if __name__ == "__main__":
    calculate_taxi_fare()
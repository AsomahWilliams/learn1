def celsius_to_fahrenheit(celsius):
    """
    Convert Celsius to Fahrenheit.
    
    Parameters:
    celsius (float): Temperature in Celsius.
    
    Returns:
    float: Equivalent temperature in Fahrenheit.
    """
    fahrenheit = celsius * (9/5) + 32
    return fahrenheit

def main():
    # Ask the user for the temperature in Celsius
    try:
        celsius = float(input("Enter the temperature in Celsius: "))
        
        # Convert to Fahrenheit
        fahrenheit = celsius_to_fahrenheit(celsius)
        
        # Display the result
        print(f"{celsius:.2f}°C is equivalent to {fahrenheit:.2f}°F.")
    
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    main()
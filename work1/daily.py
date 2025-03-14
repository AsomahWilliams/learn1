def daily_step_counter():
    # Ask the user for the number of steps walked
    try:
        steps_walked = int(input("How many steps did you walk today? "))
        
        # Provide feedback based on the number of steps
        if steps_walked < 5000:
            print("Try to walk more!")
        elif 5000 <= steps_walked <= 10000:
            print("Good job! Keep it up!")
        else:  # steps_walked > 10000
            print("Excellent! You're crushing your goal!")
    
    except ValueError:
        print("Invalid input. Please enter a numeric value for the number of steps.")

# Example usage
if __name__ == "__main__":
    daily_step_counter()
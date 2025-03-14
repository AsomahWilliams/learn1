def calculate_grade():
    # Ask the user for three test scores
    try:
        score1 = float(input("Enter the first test score: "))
        score2 = float(input("Enter the second test score: "))
        score3 = float(input("Enter the third test score: "))
    except ValueError:
        print("Invalid input. Please enter numeric values for the scores.")
        return

    # Calculate the average score
    average_score = (score1 + score2 + score3) / 3

    # Determine the letter grade
    if 90 <= average_score <= 100:
        letter_grade = 'A'
    elif 80 <= average_score < 90:
        letter_grade = 'B'
    elif 70 <= average_score < 80:
        letter_grade = 'C'
    elif 60 <= average_score < 70:
        letter_grade = 'D'
    else:
        letter_grade = 'F'

    # Display the final average and letter grade
    print(f"\nFinal Average: {average_score:.2f}")
    print(f"Letter Grade: {letter_grade}")

# Example usage
if __name__ == "__main__":
    calculate_grade()
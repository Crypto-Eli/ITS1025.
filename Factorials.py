def calculate_factorial(number):
    """Calculates the factorial of a non-negative integer.

    Args:
        number: The non-negative integer for which to calculate the factorial.

    Returns:
        The factorial of the number, or None if the input is invalid.
    """
    if number < 0:
        return None  # Factorial is not defined for negative numbers
    if number == 0:
        return 1  # Base case: 0! = 1

    factorial = 1
    for i in range(1, number + 1):
        factorial *= i
    return factorial

def main():
    """Main function to interact with the user and calculate factorial."""

    print("Welcome to the Factorial Calculation program!")

    while True:
        try:
            user_input = input("Enter a non-negative integer to calculate its factorial: ")
            number = int(user_input)

            if number < 0:
                print("Error: Please enter a non-negative integer.")
                continue #restart the loop

            factorial_result = calculate_factorial(number)

            if factorial_result is not None:
                print(f"The factorial of {number} is: {factorial_result}")
                break #exit the loop
            else:
                print("An error occurred. Please try again.")

        except ValueError:
            print("Error: Invalid input. Please enter a valid integer.")
            continue #restart the loop

if __name__ == "__main__":
    main()

# Function to calculate factorial
def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    elif n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Taking input from the user
user_input = input("Enter a non-negative integer: ")

# Validate input
if user_input.isdigit():
    number = int(user_input)
    print(f"The factorial of {number} is {factorial(number)}.")
else:
    print("Please enter a valid non-negative integer.")


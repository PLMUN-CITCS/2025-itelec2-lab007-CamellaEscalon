import math  # Import math module for advanced math functions

# Step 1: Get numerical input from the user
user_number = float(input("Enter a number to perform operations on: "))

# Step 2: Perform arithmetic operations
addition = user_number + 10
subtraction = user_number - 5
multiplication = user_number * 2
division = user_number / 3

# Step 3: Use math library functions
# Calculate the square root, but handle negative input
if user_number >= 0:
    sqrt_value = math.sqrt(user_number)
else:
    sqrt_value = "Undefined for negative numbers"

# Calculate the sine of the user input (convert degrees to radians first)
sine_value = math.sin(math.radians(user_number))

# Step 4: Display the results with formatted output
print("\nArithmetic Operations:")
print(f"User number + 10 = {addition:.2f}")
print(f"User number - 5  = {subtraction:.2f}")
print(f"User number * 2  = {multiplication:.2f}")
print(f"User number / 3  = {division:.2f}")

print("\nMath Library Functions:")
print(f"Square root of {user_number:.2f} is: {sqrt_value}")
print(f"Sine of {user_number:.2f} degrees is: {sine_value:.4f}")

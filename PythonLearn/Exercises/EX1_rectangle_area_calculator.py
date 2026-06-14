# EXERCISE 1 Rectangle Area Calculator
# Calculates the area of a rectangle based on user input length, width, and measurement.

# Measurement Values
length = input("Enter length: ")
width = input("Enter width: ")
measurement = input("Enter unit of measurement: ")

# Input handling, if measurement values are letters
while length.isalpha() and width.isalpha() == 1:
    print("Error, you can only enter numbers.")
    while length.isalpha() == 1:
        print("Re-enter length")
        length = input("Enter length: ")
    while width.isalpha() == 1:
        width = input("Enter width: ")
        print("Re-enter width")

# Area of a rectangle formula
area = float(length) * float(width)
print(f"The area of your rectangle is: {area:.2f}{measurement}²")

# TODO:
# - [easy] Add validation so length and width must be positive numbers.
# - [medium] Add support for different shapes (e.g., triangle, circle, square).
# - [hard] Create a menu-driven calculator where the user can pick which shape’s area to calculate.

# UPDATE LOG:
# 1.2.0 (2026-06-05) [feature] [easy] – Completed TODO: Allowed decimal numbers for rectangle length and width.
# 1.1.0 (2025-08-27) [feature] – Added error handling so users cannot enter letters for length/width.
# 1.0.0 (N/A) [init] – Initial working version (basic rectangle area calculator).

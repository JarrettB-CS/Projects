# EXERCISE 1 Rectangle Area Calculator
# Calculates the area of a rectangle based on user input length, width, and measurement.

length = input("Enter length: ")
width = input("Enter width: ")

while length.isdigit() == False or width.isdigit() == False:
    print("Error, you can only enter numbers.")
    if length.isdigit() == False:
        length = input("Re-enter length: ")
    if width.isdigit() == False:
        width = input("Re-enter width: ")

measurement = input("Enter measurement: ")

area = float(length) * float(width)
print(f"The area of your rectangle is: {area}{measurement}²")

# TODO:
# - [easy] Allow decimal numbers (currently only whole digits are accepted by isdigit()).
# - [medium] Add support for different shapes (e.g., triangle, circle, square).
# - [hard] Create a menu-driven calculator where the user can pick which shape’s area to calculate.

# UPDATE LOG:
# 1.1.0 (2025-08-27) [feature] – Added error handling so users cannot enter letters for length/width.
# 1.0.0 (N/A) [init] – Initial working version (basic rectangle area calculator).




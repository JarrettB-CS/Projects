# Exercise 4 circumference of a circle calculator
# Exercise 5 area of a circle
# Calculates the circumference and area of a circle using either radius or diameter input.

import math

choice = input("Do you know the radius or the diameter (r/d):")

if choice == "r":
    radius = float(input("Enter the radius in cm: "))
    diameter = 2 * radius
elif choice == "d":
    diameter = float(input("Enter the diameter in cm: "))
    radius = diameter / 2

circumference = 2 * math.pi * radius
area = math.pi * radius ** 2


print(f"The circumference of the circle is {round(circumference, 3)}cm.")
print(f"The area of the circle is {round(area, 3)}cm².")

# TODO:
# - [easy] Format the output with consistent decimal places instead of rounding.
# - [medium] Let the user choose the number of decimal places for the result.
# - [hard] Expand into a full geometry calculator that also handles spheres, cylinders, etc.

# UPDATE LOG:
# 1.1.0 (2025-09-06) [feature] – Added option to accept either radius or diameter from the user.
# 1.0.0 (N/A) [init] – Initial working version (circumference and area from radius only).

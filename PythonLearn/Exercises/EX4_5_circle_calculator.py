# Exercise 4 circumference of a circle calculator
# Exercise 5 area of a circle
# Calculates the circumference and area of a circle using either radius or diameter input.

import math

choice = input("Do you know the radius or the diameter (r/d):")

# Get the diameter from the radius or vice versa
if choice == "r":
    radius = float(input("Enter the radius in cm: "))
    diameter = 2 * radius
elif choice == "d":
    diameter = float(input("Enter the diameter in cm: "))
    radius = diameter / 2

# Circumference and Area calculations
circumference = 2 * math.pi * radius
area = math.pi * radius ** 2

print(f"The circumference of the circle is {circumference:.3f}cm.")
print(f"The area of the circle is {area:.3f}cm².")

# TODO:
# - [easy] Add input validation so choice only accepts "r" or "d".
# - [medium] Let the user choose the number of decimal places for the result.
# - [hard] Expand into a full geometry calculator that also handles spheres, cylinders, etc.

# UPDATE LOG
# 1.2.0 (2026-06-14) [feature] [easy] – Completed TODO: Formatted output with consistent decimal places instead of using round().
# 1.1.0 (N/A) [feature] [easy] – Completed TODO: Added option to accept either radius or diameter from the user.
# 1.0.0 (N/A) [init] – Initial working version (calculations from radius only).

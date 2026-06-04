# Exercise 6 – Hypotenuse of Right Triangle Calculator
# Calculates the hypotenuse of a right triangle using the Pythagorean theorem.


import math

side = input("Enter the side length of triangle: ")
base = input("Enter base length of triangle: ")

while side.isalpha() or  base.isalpha():
    print("Please enter a number")
    side = input("Enter the side length of triangle: ")
    base = input("Enter base length of triangle: ")

side = float(side)
base = float(base)

while side <= 0 or base <= 0:
    print("Please enter a positive number.")
    side = input("Enter the side length of triangle: ")
    base = input("Enter the base length of triangle: ")

hypotenuse = math.sqrt((side ** 2) + (base ** 2))

print(f"The hypotenuse is: {round(hypotenuse, 4)}")

# TODO:
# - [easy] Format the output to show units (e.g., "cm") consistently alongside the hypotenuse result.
# - [medium] Allow users to calculate side or base if the hypotenuse and one side are given.
# - [hard] Expand into a full Pythagorean theorem solver that handles all three cases with a menu.

# UPDATE LOG:
# 1.1.0 (2025-09-06) [feature] – Added input validation for non-numeric and non-positive values.
# 1.0.0 (N/A) [init] – Initial working version (hypotenuse calculator).

# Exercise 7 python arithmetic calculator
# Performs basic arithmetic operations and allows multiple calculations in one session.

calculate = input("Do you want to perform a calculation? (y/n): ")
while calculate.lower() == "y":

    arithmetic_operation = input("Enter the arithmetic operation: ")
    num_1 = float(input("Enter the first number: "))
    num_2 = float(input("Enter the second number: "))

    if arithmetic_operation == "+":
        print(num_1 + num_2)
    elif arithmetic_operation == "-":
        print(num_1 - num_2)
    elif arithmetic_operation == "*":
        print(num_1 * num_2)
    elif arithmetic_operation == "/":
        print(num_1 / num_2)
    elif arithmetic_operation == "**":
        print(num_1 ** num_2)
    elif arithmetic_operation == "%":
        (print(num_1 % num_2))
    else:
        print(f"{arithmetic_operation} is not a valid arithmetic operation")

    calculate = input("Do you want to perform another calculation? (y/n): ")
else:
    exit(0)

# TODO:
# - [easy] Add input validation so users can’t enter invalid numbers or divide by zero.
# - [medium] Add a results history that shows all previous calculations before exit.
# - [hard] Support advanced math functions like square root, factorial, sine, cosine, etc., using the math module.

# UPDATE LOG:
# 1.1.0 (2025-10-06) [feature] [medium] – Completed TODO: Added loop to allow multiple calculations in one run.
# 1.0.0 (N/A) [init] – Initial working version (basic arithmetic calculator).

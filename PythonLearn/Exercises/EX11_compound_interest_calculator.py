# Exercise 11 – Compound Interest Calculator
# Calculates compound interest and checks if a user’s investment goal has been reached.

goal = float(input('Enter the goal: '))
principle = float(input('Enter the principle: '))
rate = float(input('Enter the rate: '))
time = float(input('Enter the time: '))

final_amount = principle * pow((1 + rate / 100), time)

while final_amount < goal:
    print(f"You have not reached your goal, ${final_amount:.2f} / ${goal:.2f}.")
    principle = float(input('Enter the principle: '))
    rate = float(input('Enter the rate: '))
    time = float(input('Enter the time: '))
    final_amount = principle * pow((1 + rate / 100), time)

if final_amount >= goal:
    print("You have reached you're goal")
    print(f"${final_amount:.2f} out of ${goal:.2f}")

# TODO:
# - [easy] Add commas for large numbers (e.g., 10,000 → 10,000.00).
# - [medium] Let the user choose to calculate either final amount *or* required time to reach a goal.
# - [hard] Expand into a full financial calculator with simple interest, continuous compounding, and investment projections.

# UPDATE LOG:
# 1.1.0 (2025-10-26) [feature] [easy] – Completed TODO: Fixed grammar and formatted output with two decimal places for monetary values.
# 1.0.0 (N/A) [init] – Initial working version (basic compound interest calculator).

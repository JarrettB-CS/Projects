# Exercise 18 number guessing game
# User tries to guess a randomly generated number within a limited number of attempts.

import random

cpu = random.randint(1,100)

count = 0
while count <= 7:
    user = input("Enter a number 1-100: ")

    while not user.isdigit():
        print("Your input is not a number.")
        user = (input("Enter a number 1-100: "))

    user = int(user)

    while user not in range(1,101):
        print("Your number is not in range")
        user = int(input("Enter a number 1-100: "))


    if user == cpu:
        print("You guessed right!")
        break
    elif user < cpu:
        print("You guessed too low!")
        count += 1
        print(f"You have {7 - count} tries left")
        if count == 7:
            print(f"You lost! The number was {cpu}")
            break
    elif user > cpu:
        print("You guessed too high!")
        count += 1
        print(f"You have {7 - count} tries left")
        if count == 7:
            print(f"You lost! The number was {cpu}")
            break


# TODO:
# - [easy] Prevent repeated guesses (warn if the user enters the same number again).
# - [medium] Add difficulty modes (easy/normal/hard) that change range and attempts.
# - [hard] Add a “high score” system (fewest guesses) stored to a file.

# UPDATE LOG:
# 1.1.0 (2026-01-15) [feature] [easy] – Completed TODO: Added input validation for non-numeric entries and out-of-range guesses (1–100).
# 1.0.0 (2025/08/27) [init] – Initial working version.






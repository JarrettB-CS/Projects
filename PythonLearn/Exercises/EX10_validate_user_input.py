# Exercise 10 validate user input
# Validates a username by removing spaces, rejecting numbers/symbols, and enforcing a max length.

username = input("Enter username: ")
username = username.replace(" ", "")

numbers = ("0","1","2","3","4","5","6","7","8","9")
symbols = ("!","@","#","$","%","^","&","*")

for number in numbers:
    while number in username:
        print("Username can't contain numbers")
        username = input("Enter username: ")
        break

for symbol in symbols:
    while symbol in username:
        print("Username can't contain symbols")
        username = input("Enter username: ")
        break

while len(username) > 12:
    print("Username is too long")
    username = input("Enter username: ")

print(f"Welcome {username}")

# TODO:
# - [easy] Allow underscores (_) in usernames but still block other symbols or numbers.
# - [medium] Add password validation (e.g., minimum length, required symbol, uppercase, etc.).
# - [hard] Build a user registration system that stores valid usernames and passwords in a file.

# UPDATE LOG:
# 1.1.0 (2025-10-25) [feature] [easy] – Completed TODO: Added interactive re-prompting for invalid input (numbers, symbols, or length > 12).
# 1.0.0 (N/A) [init] – Initial working version (basic username validation).


# EXERCISE 22 phone number
# Simple phone number formatter that combines user input into a standard structure.

def get_phone_number(country, area, first, last):
    return f"{country}-{area}-{first}-{last}"

country = input("Enter country phone code: ")
area = input("Enter area code: ")
first = input("Enter first phone number: ")
last = input("Enter last phone number: ")

print(get_phone_number(country, area, first, last))


# TODO:
# - [easy] Validate that each input is numeric before building the phone number.
# - [medium] Format output to include parentheses or spacing (e.g., +1 (555) 123-4567).
# - [hard] Support multiple countries with different phone number structures.

# UPDATE LOG:
# 1.0.0 (2025-09-01) [init] – Initial working version


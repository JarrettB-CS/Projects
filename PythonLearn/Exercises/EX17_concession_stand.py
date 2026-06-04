# Exercise 17 – Concession Stand
# Displays a menu, allows users to select items, and calculates a total cost.

menu = {"popcorn" : 6.00,
        "hot dog" : 4.50,
        "nachos" : 5.00,
        "pretzel" : 3.75,
        "soda" : 3.25}

cart =[]
total = 0

commands = "(cart, checkout, commands)"
print("----- MENU -----")

for key, value in menu.items():
    print(f"{key:8}: ${value:.2f}")
print()

print("To checkout type 'checkout', enter 'commands' for more.")

while True:
    user_food = input("What would you like today?: ").lower()

    if menu.get(user_food) is not None:
        cart.append(user_food)
    if user_food == "commands":
        print(f"{commands}")
    if user_food == "cart":
        for food in cart:
            print(food)
    if user_food == "checkout":
        break

for food in cart:
    total += menu.get(food)

print(f"Your total is: ${total:.2f}")

# TODO:
# - [easy] Prevent duplicate items from being added to the cart.
# - [medium] Allow users to enter quantities for each item.
# - [hard] Add item removal and a running total that updates after each selection.

# UPDATE LOG:
# 1.1.0 (2025-12-27) [feature] [easy] – Completed TODO: Added cart display and command-based interaction before checkout.
# 1.0.0 (N/A) [init] – Initial working version (basic concession stand ordering system).











#

#1.1
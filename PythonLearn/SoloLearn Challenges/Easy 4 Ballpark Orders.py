# Sololearn Code Challenge Easy 4 - Ballpark Orders
# Determine the total cost of four concession stand orders.
# Any item not found on the menu is replaced with a Coke.
# Apply 7% sales tax and print the final total.

# Get order and turn into list
order = input("What would you like to order? ")
order = order.split(" ")

# Menu prices
menu = {"Nachos": 6,
        "Pizza": 6,
        "Cheeseburger": 10,
        "Water": 4,
        "Coke": 5
        }

# Check if ordered item is on the menu and adds prices
total = 0
for item in order:
    if item in menu:
        total += menu.get(item)
    else:
        total += menu.get("Coke")

# Math for total cost
tax = total * .07
amount = total + tax
print(amount)

# TODO:
# - [easy] Format the final amount as currency (e.g., $26.75).
# - [medium] Accept menu items regardless of capitalization (e.g., pizza, PIZZA, Pizza).
# - [hard] Display an itemized receipt showing each item, its price, subtotal, tax, and total.

# UPDATE LOG:
# 1.0.0 (2026-06-03) [init] – Initial working version. Accepts a space-separated order, checks items against a menu dictionary, substitutes Coke for invalid items, and calculates tax and final total.

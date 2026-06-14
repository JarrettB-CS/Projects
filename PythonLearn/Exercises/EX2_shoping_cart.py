# EXERCISE 2 Shopping cart program
# Simple shopping cart calculator for a single item with quantity and total cost.


shopping_list = []
prices = []
quantities = []
final = 0
more_items = "yes"

while more_items == "yes":
    item = input("Enter item: ")
    shopping_list.append(item)

    price = float(input("Enter price: "))
    prices.append(price)

    quantity = int(input("Enter quantity: "))
    quantities.append(quantity)

    total = price * quantity
    final += total
    more_items = input("Would you like to add another: ")

print()
x = 0
for item in shopping_list:
    print(f"{quantities[x]} x {shopping_list[x]} ${prices[x]:.2f}")
    x = x + 1

print(f"Your total is ${final:.2f}")

# TODO:
# - [easy] Validate that quantity is a positive whole number.
# - [medium] Improve the receipt to show unit price, quantity, line total, and final total.
# - [hard] Add discounts, tax, and receipt totals with a clear breakdown.

# UPDATE LOG:
# 1.2.0 (2026-06-14) [feature] [medium] – Completed TODO: Allowed multiple items to be added and printed a cart-style receipt.
# 1.1.0 (N/A) [feature] [easy] – Completed TODO: Added price formatting to always display two decimal places.
# 1.0.0 (N/A) [init] – Initial working version (basic shopping cart calculator).

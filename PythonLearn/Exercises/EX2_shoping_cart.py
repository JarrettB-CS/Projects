# EXERCISE 2 Shopping cart program
# Simple shopping cart calculator for a single item with quantity and total cost.

item = input("Enter item: ")
price = float(input("Enter price: "))
quantity = int(input("Enter quantity: "))

total = price * quantity

print(f"You have purchased {quantity} {item}.")
print(f"Your total is ${total:.2f}")

# TODO:
# - [easy] Add input validation so price and quantity must be positive numbers.
# - [medium] Allow multiple items to be added and show a receipt with line totals.
# - [hard] Add tax/discount options and display a final formatted bill.

# UPDATE LOG:
# 1.1.0 (2025-08-31) [feature] – Added price formatting to always display two decimal places.
# 1.0.0 (N/A) [init] – Initial working version (basic shopping cart calculator).

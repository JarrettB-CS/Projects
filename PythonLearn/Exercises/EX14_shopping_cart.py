# Exercise 14 – Shopping Cart Program
# Have users input food items and prices, then display their cart and total.

foods = []
prices = []
total = 0

while True:
    food = input("Enter a food (q to quit): ")
    if food.lower() == "q":
        break
    else:
        price = float(input(f"Enter the price of a {food}: $ "))
        foods.append(food)
        prices.append(price)

print("----- CART -----")
for food in foods:
    print(food)

for price in prices:
    total += price

print("----- Total -----")
print(f"${total:.2f}")

# TODO:
# - [easy] Validate that price inputs are positive numbers only.
# - [medium] Display each food item alongside its price in the cart summary.
# - [hard] Allow item removal, quantity updates, and a running total that updates dynamically.

# UPDATE LOG:
# 1.1.0 (2025-11-06) [feature] [easy] – Completed TODO: Formatted total to display two decimal places.
# 1.0.0 (N/A) [init] – Initial working version (basic shopping cart with total).

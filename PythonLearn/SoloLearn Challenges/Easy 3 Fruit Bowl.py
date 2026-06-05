# Sololearn Code Challenge Easy 3 - Fruit Bowl
# Determine how many whole apple pies can be made from the fruit bowl.
# Half of the fruit are apples and each pie requires 3 apples.
# Output the total number of whole pies that can be made.

import math

# Calculate whole apple pies using total fruit
fruit = int(input())
apples = fruit / 2
apple_pies = math.floor(apples / 3)

print(apple_pies)

# TODO:
# - [easy] Display the number of apples remaining after making pies.
# - [medium] Show the intermediate apple count before calculating pies.
# - [hard] Allow the number of apples required per pie to be customized.
#
# UPDATE LOG:
# 1.0.0 (2026-06-04) [init] – Calculated the number of whole apple pies that can be made by determining the number of apples in the fruit bowl and rounding down to the nearest whole pie.

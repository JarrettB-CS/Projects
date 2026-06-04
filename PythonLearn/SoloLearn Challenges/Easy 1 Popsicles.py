# Sololearn Code Challenge Easy 1 - Popsicles
# Determine if popsicles can be evenly distributed among siblings.
# Print "give away" if everyone gets the same amount.
# Otherwise, print "eat them yourself".

# Get popsicle & siblings count
siblings = int(input("How many siblings do you have? "))
popsicles = int(input("How many popsicles do you have? "))


# Distribute popsicles if you have an even amount
if popsicles % siblings == 0:
    print("give away")
else:
    print("eat them yourself")

# TODO:
# - [easy] Validate that both inputs are positive integers.
# - [medium] Display how many popsicles each sibling receives when divisible.
# - [hard] Support multiple test cases in a single run.

# UPDATE LOG:
# 1.0.0 (2026-06-03) [init] – Completed working solution using modulo to determine whether popsicles can be evenly distributed among siblings.
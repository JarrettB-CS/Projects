# Exercise 13 – Make Rectangle with Symbols
# Draws a rectangle using a chosen symbol, with options for filled or hollow styles.

symbol = input("Enter a symbol: ")
rows = int(input("Enter number of rows: "))
columns = int(input("Enter number of columns: "))
fill_type = (input("Enter fill type (fill/hollow): "))
num_spaces = columns - 2

if fill_type == "fill":
    for x in range(rows):
        for y in range(columns):
            print(symbol, end="")
        print()

if fill_type == "hollow":
    for x in range(columns):
        print(symbol, end="")
    print()
    for x in range(rows - 2):
        print(f"{symbol}{" " * num_spaces}{symbol}")
    for x in range(columns):
        print(symbol, end="")

# TODO:
# - [easy] Add input validation for rows/columns (positive integers only).
# - [medium] Add a “border-only” mode where only the outer frame is drawn.
# - [hard] Allow colored output using ANSI escape codes or support multiple symbols per edge.

# UPDATE LOG:
# 1.1.0 (2025-10-27) [feature] [medium] – Completed TODO: Added support for filled or hollow rectangle types.
# 1.0.0 (N/A) [init] – Initial working version (basic symbol rectangle generator).

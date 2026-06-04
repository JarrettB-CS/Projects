# EX 15 2D list Keypad
# Displays a keypad layout using a 2D list with formatted borders.Displays a keypad layout using a 2D list with formatted borders.

keypad = (("| 1 |", "2", "| 3 |"),
          ("| 4 |", "5", "| 6 |"),
          ("| 7 |", "8", "| 9 |"),
          ("| * |", "0", "| # |"))

line_break = "|---+---+---|"

print("+-----------+")
for row in keypad:
    for key in row:
        print(key, end=" ")
    print()
    print(line_break, end=" ")
    print()

# TODO:
# - [easy] Improve key alignment so all keys display with equal width.
# - [medium] Allow user input to simulate pressing keys and show the sequence entered.
# - [hard] Build an interactive keypad system that validates a passcode or phone number entry.

# UPDATE LOG:
# 1.1.0 (2025-11-25) [feature] [easy] – Completed TODO: Added keypad formatting with borders and aligned output.
# 1.0.0 (N/A) [init] – Initial working version (basic 2D keypad display).


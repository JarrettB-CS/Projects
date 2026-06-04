# EXERCISE 20 Dice Roller Program

import random

dice_symbol = ("⚀", "⚁", "⚂", "⚃", "⚄", "⚅")
dice_art = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘" ),
    2: ("┌─────────┐",
        "│ ●       │",
        "│         │",
        "│       ● │",
        "└─────────┘" ),
    3: ("┌─────────┐",
        "│ ●       │",
        "│    ●    │",
        "│       ● │",
        "└─────────┘"  ),
    4: ("┌─────────┐",
        "│ ●     ● │",
        "│         │",
        "│ ●     ● │",
        "└─────────┘"  ),
    5: ("┌─────────┐",
        "│ ●     ● │",
        "│    ●    │",
        "│ ●     ● │",
        "└─────────┘"  ),
    6: ("┌─────────┐",
        "│ ●     ● │",
        "│ ●     ● │",
        "│ ●     ● │",
        "└─────────┘"  )
}
dice = (dice_symbol, dice_art)

select = int(input("Which dice would you like to roll? 1:Symbol 2:Art  "))
selection = dice[select - 1]

dice_number = int(input("How many dice would you like to roll: "))
count = 0

while count < dice_number:
    if selection == dice[0]:
        roll1 = random.choice(dice_symbol)
        print(roll1)
        count += 1
    if selection == dice[1]:
        roll_key = random.randint(1, 6)
        roll2 = dice_art.get(roll_key)
        for line in roll2:
            print(line)
        count += 1

# TODO:
# - [easy]
# - [medium]
# - [hard]

# UPDATE LOG:
# 1.0.0 (N/A) [init] – Initial working version.


#print("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518") ● ┌ ─ ┐ │ └ ┘


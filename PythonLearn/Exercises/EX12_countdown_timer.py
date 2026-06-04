# Exercise 12 – Countdown Timer
# Counts down from a user-defined time and announces when halfway and finished.

import time

timer = int(input("Enter the time in seconds: "))

for x in range(timer, 0, -1):
    seconds = x % 60
    minutes = int(x / 60) % 60
    hours = int(x / 3600)
    print(f"[{hours:02}H:{minutes:02}M:{seconds:02}S]")
    if timer / 2 == x:
        print("HALFWAY!")
    if timer % 2 == 1:
        halfway = timer / 2 + 0.5
        if halfway == x:
            print("HALFWAY!")
    time.sleep(1)

print("Times Up!")

# TODO:
# - [easy] Add input validation to ensure users enter a positive number.
# - [medium] Add a “last 10 seconds” alert or countdown tone before completion.
# - [hard] Create a formatted GUI version using tkinter with start/pause/reset buttons.

# UPDATE LOG:
# 1.1.0 (2025-10-26) [feature] [medium] – Completed TODO: Added halfway alert for both even and odd durations.
# 1.0.0 (N/A) [init] – Initial working version (basic countdown timer).


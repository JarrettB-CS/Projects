# EXERCISE 21 count up timer

import time

def count(seconds):
    for x in range(seconds):
        print(x + 1)
        time.sleep(1)

user = int(input("Enter a number: "))
count(user)

# TODO:
# - [easy] Format output to show elapsed time in mm:ss instead of plain seconds.
# - [medium] Add a stop/pause option so the user can interrupt the timer midway.
# - [hard] Turn this into a stopwatch that shows hours:minutes:seconds with start/stop/reset options.

# UPDATE LOG:
# 1.0.0 (2025-08-31) [init] – Initial working version


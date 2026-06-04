# Exercise 3 Madlibs game
# Interactive madlibs generator where the user fills in words to complete a story.

story_pick = int(input("Enter story 1-2: ")) - 1

# descriptor
adjective1 = input("Enter an adjective: ")
adjective2 = input("Enter an adjective: ")
adjective3 = input("Enter an adjective: ")

# person,place or thing
noun1 = input("Enter a noun: ")
noun2 = input("Enter a noun: ")
noun3 = input("Enter a noun: ")

# what is it doing
verb1 = input("Enter a verb: ")
verb2 = input("Enter a verb: ")
verb3 = input("Enter a verb: ")

story1 = ( f"Today I went to a {adjective1} zoo.",
           f"In one of the enclosures, I saw a {noun1}.",
           f"{noun1} was {adjective2} and {verb1}.",
           f"I was {adjective3}.",
           f"I also saw a {noun2} and a {noun3}.",
           f"It was a good zoo trip but the exit guards were weird.",
           f"One was {verb2} and the other was {verb3}" )

story2 = ( f"Last night I went to a {adjective1} restaurant.",
           f"The waiter recommended the {noun1}.",
           f"When it arrived, the {noun1} was {adjective2} and {verb1}.",
           f"I was {adjective3} about it.",
           f"For dessert, I ordered a {noun2} and my friend got a {noun3}.",
           f"It was a good meal, but the chef was unusual.",
           f"One chef was {verb2} while the other was {verb3}." )

stories = (story1, story2,)

for line in (stories[story_pick]):
    print(line)

# TODO:
# - [easy] Add input validation so users can’t leave blanks when entering words.
# - [medium] Allow more than two stories (e.g., let the user pick from 3–5 options).
# - [hard] Load stories dynamically from a file so you can keep adding new ones without changing the code.

# UPDATE LOG:
# 1.1.0 (2025-08-31) [feature] – Added a second story for the user to choose from.
# 1.0.0 (N/A) [init] – Initial working version (single madlibs story).


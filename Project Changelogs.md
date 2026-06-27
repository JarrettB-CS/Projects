# Python Exercise Headers and Footers

This file gathers the current reusable headers and footers for each tracked Python exercise.

Each section includes:
- **Header:** the title and short project description for the top of the file.
- **Footer:** the current TODO list and UPDATE LOG for the bottom of the file.

---

## Exercise 1 – Rectangle Area Calculator

### Header

```python
# Exercise 1 – Rectangle Area Calculator
# Calculates the area of a rectangle from user input length, width, and measurement unit.
```

### Footer

```python
# TODO:
# - [easy] Accept decimal numbers cleanly (and reject empty input).
# - [medium] Let the user run multiple calculations in one session.
# - [hard] Add a history/summary at the end (all rectangles + areas).

# UPDATE LOG:
# 1.1.0 (N/A) [feature] [easy] – Completed TODO: Added error handling so users cannot enter letters for length/width.
# 1.0.0 (N/A) [init] – Initial working version (basic rectangle area calculator).
```

---

## Exercise 2 – Shopping Cart Program (Single Item)

### Header

```python
# Exercise 2 – Shopping Cart Program
# Calculates total cost from a single item’s price and quantity.
```

### Footer

```python
# TODO:
# - [easy] Validate that quantity is a positive whole number.
# - [medium] Allow multiple items (build a cart) and print a receipt.
# - [hard] Add discounts, tax, and receipt totals with a clear breakdown.

# UPDATE LOG:
# 1.1.0 (N/A) [feature] [easy] – Completed TODO: Added price formatting to always display two decimal places.
# 1.0.0 (N/A) [init] – Initial working version (basic shopping cart calculator).
```

---

## Exercise 3 – Madlibs Game

### Header

```python
# Exercise 3 – Madlibs Game
# Prompts the user for words and prints a generated story.
```

### Footer

```python
# TODO:
# - [easy] Validate story selection (only allow valid choices).
# - [medium] Add a replay option without restarting the program.
# - [hard] Randomize prompts and load stories from a file.

# UPDATE LOG:
# 1.1.0 (N/A) [feature] [easy] – Completed TODO: Added a second story for the user to choose from.
# 1.0.0 (N/A) [init] – Initial working version (single Madlibs story).
```

---

## Exercise 4 & 5 – Circle Calculators

### Header

```python
# Exercise 4 & 5 – Circle Calculators
# Calculates the circumference and area of a circle using either radius or diameter.
```

### Footer

```python
# TODO:
# - [easy] Validate choice input (only r/d) and re-prompt when invalid.
# - [medium] Let the user choose rounding precision (e.g., 2, 3, 4 decimals).
# - [hard] Support multiple circles in one run and print a summary table.

# UPDATE LOG:
# 1.1.0 (N/A) [feature] [easy] – Completed TODO: Added option to accept either radius or diameter from the user.
# 1.0.0 (N/A) [init] – Initial working version (calculations from radius only).
```

---

## Exercise 6 – Hypotenuse of Right Triangle Calculator

### Header

```python
# Exercise 6 – Hypotenuse of Right Triangle Calculator
# Calculates the hypotenuse of a right triangle using the Pythagorean theorem.
```

### Footer

```python
# TODO:
# - [easy] Add units support (user enters units and output includes units consistently).
# - [medium] Allow users to calculate side or base if the hypotenuse and one side are given.
# - [hard] Expand into a full Pythagorean theorem solver that handles all three cases with a menu.

# UPDATE LOG:
# 1.1.0 (N/A) [feature] [easy] – Completed TODO: Added input validation for non-numeric and non-positive values.
# 1.0.0 (N/A) [init] – Initial working version (hypotenuse calculator).
```

---

## Exercise 7 – Python Arithmetic Calculator

### Header

```python
# Exercise 7 – Python Arithmetic Calculator
# Performs basic arithmetic operations and supports multiple calculations in one session.
```

### Footer

```python
# TODO:
# - [easy] Add input validation (invalid numbers and division by zero).
# - [medium] Add a results history that shows all previous calculations before exit.
# - [hard] Support advanced math functions (e.g., sqrt, factorial, trig) via a menu.

# UPDATE LOG:
# 1.1.0 (2025-10-06) [feature] [medium] – Completed TODO: Added loop to allow multiple calculations in one run.
# 1.0.0 (N/A) [init] – Initial working version (basic arithmetic calculator).
```

---

## Exercise 8 – Weight Converter

### Header

```python
# Exercise 8 – Weight Converter
# Converts weight between kilograms, pounds, grams, and ounces.
```

### Footer

```python
# TODO:
# - [easy] Make unit input case-insensitive (accept KG, Kg, LB, etc.).
# - [medium] Add a loop allowing multiple conversions in one run.
# - [hard] Expand into a full unit converter with categories (distance, temperature, volume).

# UPDATE LOG:
# 1.1.0 (2025-10-08) [feature] [medium] – Completed TODO: Added support for grams and ounces in addition to kg and lbs.
# 1.0.0 (N/A) [init] – Initial working version (basic kg ↔ lbs converter).
```

---

## Exercise 9 – Temperature Conversion

### Header

```python
# Exercise 9 – Temperature Conversion
# Converts temperature between Celsius and Fahrenheit.
```

### Footer

```python
# TODO:
# - [easy] Make the output sentence clearer and consistent (same wording for both conversions).
# - [medium] Add Kelvin support (C ↔ F ↔ K).
# - [hard] Build a conversion menu with brief formula explanations.

# UPDATE LOG:
# 1.1.0 (2025-10-10) [feature] [easy] – Completed TODO: Made input case-insensitive so “c/C” and “f/F” both work.
# 1.0.0 (N/A) [init] – Initial working version (C ↔ F converter).
```

---

## Exercise 10 – Validate User Input

### Header

```python
# Exercise 10 – Validate User Input
# Validates a username by removing spaces, rejecting numbers/symbols, and enforcing a max length.
```

### Footer

```python
# TODO:
# - [easy] Allow underscores (_) in usernames but still block other symbols or numbers.
# - [medium] Add password validation (minimum length + required character rules).
# - [hard] Build a simple registration system that stores users in a file.

# UPDATE LOG:
# 1.1.0 (2025-10-25) [feature] [easy] – Completed TODO: Added interactive re-prompting for invalid input (numbers, symbols, or length > 12).
# 1.0.0 (N/A) [init] – Initial working version (basic username validation).
```

---

## Exercise 11 – Compound Interest Calculator

### Header

```python
# Exercise 11 – Compound Interest Calculator
# Calculates compound interest and checks whether a goal amount has been reached.
```

### Footer

```python
# TODO:
# - [easy] Add commas for large numbers (e.g., 10000.00 → 10,000.00).
# - [medium] Let the user choose to calculate either final amount or required time to reach the goal.
# - [hard] Expand into a full financial calculator (simple interest, continuous compounding, projections).

# UPDATE LOG:
# 1.1.0 (2025-10-26) [feature] [easy] – Completed TODO: Fixed grammar and formatted output with two decimal places for monetary values.
# 1.0.0 (N/A) [init] – Initial working version (basic compound interest calculator).
```

---

## Exercise 12 – Countdown Timer

### Header

```python
# Exercise 12 – Countdown Timer
# Counts down from a user-defined time and announces halfway and completion.
```

### Footer

```python
# TODO:
# - [easy] Add input validation to ensure users enter a positive number.
# - [medium] Add a “last 10 seconds” alert.
# - [hard] Create a GUI version (start/pause/reset).

# UPDATE LOG:
# 1.1.0 (2025-10-26) [feature] [medium] – Completed TODO: Added halfway alert for both even and odd durations.
# 1.0.0 (N/A) [init] – Initial working version (basic countdown timer).
```

---

## Exercise 13 – Make Rectangle with Symbols

### Header

```python
# Exercise 13 – Make Rectangle with Symbols
# Draws a rectangle with a chosen symbol and supports filled or hollow styles.
```

### Footer

```python
# TODO:
# - [easy] Validate rows/columns as positive integers.
# - [medium] Add a third mode (e.g., border-only or checker pattern).
# - [hard] Support colored output (ANSI) and/or different symbols per edge.

# UPDATE LOG:
# 1.1.0 (2025-10-27) [feature] [medium] – Completed TODO: Added support for filled or hollow rectangle types.
# 1.0.0 (N/A) [init] – Initial working version (basic symbol rectangle generator).
```

---

## Exercise 14 – Shopping Cart Program

### Header

```python
# Exercise 14 – Shopping Cart Program
# Allows users to enter food items and prices, then displays the cart and a formatted total.
```

### Footer

```python
# TODO:
# - [easy] Validate that price inputs are positive numbers.
# - [medium] Display each cart item alongside its price in the cart summary.
# - [hard] Add quantities + item removal + a running total that updates during ordering.

# UPDATE LOG:
# 1.1.0 (2025-11-06) [feature] [easy] – Completed TODO: Formatted total to display two decimal places.
# 1.0.0 (N/A) [init] – Initial working version (basic shopping cart with total).
```

---

## Exercise 15 – 2D List Keypad

### Header

```python
# Exercise 15 – 2D List Keypad
# Displays a keypad layout using a 2D structure and formatted borders.
```

### Footer

```python
# TODO:
# - [easy] Improve key alignment so all keys display with equal width.
# - [medium] Allow user input to simulate pressing keys and show the sequence entered.
# - [hard] Validate a passcode or phone number entry using the keypad.

# UPDATE LOG:
# 1.1.0 (2025-11-25) [feature] [easy] – Completed TODO: Added keypad formatting with borders and aligned output.
# 1.0.0 (N/A) [init] – Initial working version (basic 2D keypad display).
```

---

## Exercise 16 – Python Quiz Game

### Header

```python
# Exercise 16 – Python Quiz Game
# Runs a multiple-choice quiz and scores answers.
```

### Footer

```python
# TODO:
# - [easy] Display the percentage with consistent formatting (fixed decimals).
# - [medium] Show the correct answer when the user gets a question wrong.
# - [hard] Randomize question order and allow replay without restarting.

# UPDATE LOG:
# 1.1.0 (2025-12-24) [feature] [easy] – Completed TODO: Displayed final score as a percentage.
# 1.0.0 (N/A) [init] – Initial working version (basic quiz game with scoring).
```

---

## Exercise 17 – Concession Stand

### Header

```python
# Exercise 17 – Concession Stand
# Displays a menu, allows users to select items using commands, and calculates a total cost.
```

### Footer

```python
# TODO:
# - [easy] Prevent duplicate items from being added to the cart.
# - [medium] Allow users to enter quantities for each item.
# - [hard] Add item removal and a running total that updates after each selection.

# UPDATE LOG:
# 1.1.0 (2025-12-27) [feature] [easy] – Completed TODO: Added cart display and command-based interaction before checkout.
# 1.0.0 (N/A) [init] – Initial working version (basic concession stand ordering system).
```

---

## Exercise 18 – Number Guessing Game

### Header

```python
# Exercise 18 – Number Guessing Game
# User tries to guess a randomly generated number within a limited number of attempts.
```

### Footer

```python
# TODO:
# - [easy] Prevent repeated guesses (warn if the user enters the same number again).
# - [medium] Add difficulty modes (easy/normal/hard) that change range and attempts.
# - [hard] Add a “high score” system (fewest guesses) stored to a file.

# UPDATE LOG:
# 1.1.0 (2026-01-15) [feature] [easy] – Completed TODO: Added input validation for non-numeric entries and out-of-range guesses (1–100).
# 1.0.0 (2025/08/27) [init] – Initial working version.
```

---

## Exercise 19 – Rock Paper Scissors

### Header

```python
# Exercise 19 – Rock Paper Scissors
# Plays Rock–Paper–Scissors against the computer and announces the winner.
```

### Footer

```python
# TODO:
# - [easy] Add replay support (play again without restarting).
# - [medium] Track wins/losses/ties and show stats.
# - [hard] Add best-of series mode (e.g., first to 3 wins).

# UPDATE LOG:
# 1.0.0 (N/A) [init] – Initial working version.
```

---

## Exercise 21 – Count Up Timer

### Header

```python
# Exercise 21 – Count Up Timer
# Counts up in seconds until a user-specified number is reached.
```

### Footer

```python
# TODO:
# - [easy] Format output to show elapsed time in mm:ss instead of plain seconds.
# - [medium] Add a stop/pause option so the user can interrupt the timer midway.
# - [hard] Turn this into a stopwatch that shows hours:minutes:seconds with start/stop/reset options.

# UPDATE LOG:
# 1.0.0 (2025-08-31) [init] – Initial working version.
```

---

## Exercise 22 – Phone Number

### Header

```python
# Exercise 22 – Phone Number
# Simple phone number formatter that combines user input into a standard structure.
```

### Footer

```python
# TODO:
# - [easy] Validate that each input is numeric before building the phone number.
# - [medium] Format output to include parentheses or spacing (e.g., +1 (555) 123-4567).
# - [hard] Support multiple countries with different phone number structures.

# UPDATE LOG:
# 1.0.0 (2025-09-01) [init] – Initial working version.
```

---

## Missing / Not Yet Added

- Exercise 20 has not been provided yet.

---

# Sololearn Code Challenges

These challenge entries use the same header/footer format as the main Python exercises.

---

## Sololearn Code Challenge Easy 1 - Popsicles

### Header

```python
# Sololearn Code Challenge Easy 1 - Popsicles
# Determine if popsicles can be evenly distributed among siblings.
# Print "give away" if everyone gets the same amount.
# Otherwise, print "eat them yourself".
```

### Footer

```python
# TODO:
# - [easy] Validate that both inputs are positive integers.
# - [medium] Display how many popsicles each sibling receives when divisible.
# - [hard] Support multiple test cases in a single run.

# UPDATE LOG:
# 1.0.0 (2026-06-03) [init] – Completed working solution using modulo to determine whether popsicles can be evenly distributed among siblings.
```

---

## Sololearn Code Challenge Easy 2 - Halloween Candy

### Header

```python
# Sololearn Code Challenge Easy 2 - Halloween Candy
# Determine the probability that a random item from the bag is a dollar bill.
# Two houses give dollar bills, one gives a toothbrush, and the rest give candy.
# Output the percentage rounded up to the nearest whole number.
```

### Footer

```python
# TODO:
# - [easy] Display the raw probability before converting to a percentage.
# - [medium] Show the number of dollar-bill houses and non-dollar-bill houses.
# - [hard] Allow the number of dollar-bill and toothbrush houses to be customized.
#
# UPDATE LOG:
# 1.0.0 (2026-06-04) [init] – Calculated the probability of drawing a dollar bill and rounded the resulting percentage up to the nearest whole number.
```

---

## Sololearn Code Challenge Easy 3 - Fruit Bowl

### Header

```python
# Sololearn Code Challenge Easy 3 - Fruit Bowl
# Determine how many whole apple pies can be made from the fruit bowl.
# Half of the fruit are apples and each pie requires 3 apples.
# Output the total number of whole pies that can be made.
```

### Footer

```python
# TODO:
# - [easy] Display the number of apples remaining after making pies.
# - [medium] Show the intermediate apple count before calculating pies.
# - [hard] Allow the number of apples required per pie to be customized.
#
# UPDATE LOG:
# 1.0.0 (2026-06-04) [init] – Calculated the number of whole apple pies that can be made by determining the number of apples in the fruit bowl and rounding down to the nearest whole pie.
```

---

## Sololearn Code Challenge Easy 4 - Ballpark Orders

### Header

```python
# Sololearn Code Challenge Easy 4 - Ballpark Orders
# Determine the total cost of four concession stand orders.
# Any item not found on the menu is replaced with a Coke.
# Apply 7% sales tax and print the final total.
```

### Footer

```python
# TODO:
# - [easy] Format the final amount as currency (e.g., $26.75).
# - [medium] Accept menu items regardless of capitalization (e.g., pizza, PIZZA, Pizza).
# - [hard] Display an itemized receipt showing each item, its price, subtotal, tax, and total.

# UPDATE LOG:
# 1.0.0 (2026-06-03) [init] – Initial working version. Accepts a space-separated order, checks items against a menu dictionary, substitutes Coke for invalid items, and calculates tax and final total.
```

---

# Euler Problems

These entries track math-focused coding challenges that help connect programming practice with problem-solving.

---

## Euler's Problem 1 – Multiples of 3 or 5

### Problem

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get:

`3, 5, 6, 9`

The sum of these multiples is `23`.

Find the sum of all the multiples of 3 or 5 below `1000`.

### Completion

- **Answer:** 233168
- **Completed:** Sat, 30 Aug 2025, 11:30

### Footer

```python
# OPTIMIZATION TODO:
# - [easy] Re-solve using a different beginner-friendly loop structure.
# - [medium] Refactor into a reusable function that accepts any limit and list of multiples.
# - [hard] Solve using a mathematical formula instead of checking every number.

# UPDATE LOG:
# 1.0.0 (2025-08-30) [solved] – Solved problem and confirmed answer: 233168.
```

---

## Euler's Problem 2 – Even Fibonacci Numbers

### Problem

Each new term in the Fibonacci sequence is generated by adding the previous two terms.

Starting with `1` and `2`, the first 10 terms are:

`1, 2, 3, 5, 8, 13, 21, 34, 55, 89`

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

### Completion

- **Answer:** 4613732
- **Completed:** Sun, 31 Aug 2025, 12:05

### Footer

```python
# OPTIMIZATION TODO:
# - [easy] Re-solve using a different loop structure while clearly tracking each Fibonacci term.
# - [medium] Refactor into a reusable function that accepts any maximum Fibonacci value.
# - [hard] Optimize by generating only even Fibonacci numbers instead of checking every term.

# UPDATE LOG:
# 1.0.0 (2025-08-31) [solved] – Solved problem and confirmed answer: 4613732.
```

## CS Rebuild HQ – Support Ticket Summary Builder

**Description:** Collects basic support-ticket information from the user and prints a clean ticket summary.

### TODO
- [easy] Add spacing and separators to make the printed ticket easier to read.
- [medium] Validate the urgency rating so it only accepts values from 1 to 5.
- [hard] Add ticket IDs, timestamps, and support-priority labels.

### Update Log
- 1.0.0 (2026-06-27) [init] – Initial working version. Collected support ticket details and printed a clean ticket summary without using if statements.
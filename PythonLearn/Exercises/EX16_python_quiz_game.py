# Exercise 16 – Python Quiz Game
# Presents a multiple-choice quiz, tracks score, and evaluates user answers.

questions = (("Which planet in our solar system has the shortest day (rotates fastest)?"),
             ("The painting “The Starry Night” was created by which artist?"),
             ("What is the capital of Canada?"),
             ("In computing, what does the acronym “CPU” stand for?"),
             ("Which novel opens with the line, “It was the best of times, it was the worst of times”?"))

choices = (("A) Mercury", "B) Jupiter", "C) Mars", "D) Neptune"),
           ("A) Claude Monet", "B) Vincent van Gogh", "C) Pablo Picasso", "D) Paul Cézanne"),
           ("A) Toronto", "B) Vancouver", "C) Ottawa", "D) Montreal"),
           ("A) Central Processing Unit", "B) Computer Power Utility", "C) Core Program Usage", "D) Central Peripheral Unit"),
           ("A) Pride and Prejudice", "B) Moby-Dick", "C) A Tale of Two Cities", "D) Great Expectations"))

answers = ("B", "B", "C", "A", "C")

score = 0
x = 0

for question in questions:
    print(question)
    print(choices[x])
    user = input("Enter answer choice: ")

    if user.upper() == answers[x]:
        score += 1
    x += 1
    print()

print(f"Your score is {(score / len(questions)) * 100}%")

# TODO:
# - [easy] Display the score with a fixed decimal format (e.g., 80.0% instead of 80.0).
# - [medium] Display the correct answer when the user gets a question wrong.
# - [hard] Randomize question order and allow replay without restarting the program.

# UPDATE LOG:
# 1.1.0 (2025-12-24) [feature] [easy] – Completed TODO: Displayed final score as a percentage.
# 1.0.0 (N/A) [init] – Initial working version (basic quiz game with scoring).

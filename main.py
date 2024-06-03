#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
from art import logo
print(logo)

import random

answer = random.randint(1,100)

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
#print(f"Pssst, the correct answer is {answer}")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

guess_count = 0
if difficulty == "hard":
    guess_count = 5
elif difficulty == "easy":
    guess_count = 10
else:
    print("your input is invalid, try again")

while guess_count > 0:
    print(f"You have {guess_count} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))

    if guess == answer:
        guess_count = 0
        print(f"You got it! The answer was {answer}.")
    else:
        if guess > answer:
            print("Too high.")
        if guess < answer:
            print("Too low.")
        if guess_count > 1:
            print("Guess again.")
        guess_count -= 1

if guess_count == 0 and guess != answer:
    print("You've run out of guesses, you lose.")
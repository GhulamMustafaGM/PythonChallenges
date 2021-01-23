# Conditionals Challenge 19: Guess My Number App
import random

print("\nWelcome to the Guess My Number App")

# Get user input
name = input("\nHello! What is your name: ").title().strip()

# Pick a random integer from 1 to 20
print("Well " + name + ", I am thinking of a number between 1 and 20.")
number = random.randint(1,20)

# Guess the number 5 times
for guess_num in range(5):
    guess = int(input("\nTake a guess: "))

    if guess < number:
        print("Your guess is too low.\n")
    elif guess > number:
        print("Your guess is too high.\n")
    else:
        break

    # The game is done, recap winning or loosing
    if guess == number:
        print("\nGood job, " + name + "! You guessed my number in " + str(guess_num + 1) + " guesses!")
    else:
        print("\nGame Over. The number I was thinking of was " + str(number) + ".\n")

# Program output

# Welcome to the Guess My Number App

# Hello! What is your name: Issac
# Well Issac, I am thinking of a number between 1 and 20.

# Take a guess: 17
# Your guess is too high.

# Game Over. The number I was thinking of was 1.


# Take a guess: 13
# Your guess is too high.

# Game Over. The number I was thinking of was 1.


# Take a guess: 1
from art import logo
import random

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def level():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

    if difficulty == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def check(guess, secret, turns):
    """Check answer with guess and return the number of  guesses remaining"""
    if guess == secret:
        print(f"You got it! The answer was {secret}.")
    else:
        if guess < secret:
            print("Too low")
        else:
            print("Too High")
        print("Guess again")
        return turns - 1


def game():
    print(logo)

    print("Welcome to the Number Guessing Game! ")
    print("I'm thinking of a number between 1 and 100")

    secret = random.randint(1, 100)

    turns = level()

    guess = 0
    while guess != secret:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess : "))

        turns = check(guess, secret, turns)

        if turns == 0:
            print("You've run out og guesses, you lose")
            return


game()

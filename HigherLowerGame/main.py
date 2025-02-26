#print logo
import art
import random
from game_data import data

def formate_data(account):
    """Takes the account data and return printable format"""
    name = account['name']
    decc = account['description']
    country = account['country']
    return f"{name}, a {decc}, from {country}"

A = random.choice(data)
B = random.choice(data)
while A == B:
    B = random.choice(data)



game_over = False
score = 0

A_followers = A['follower_count']
B_followers = B['follower_count']


def check(answer):
    global score, game_over

    if A_followers > B_followers:
        correct_answer = 'a'
    else:
        correct_answer = 'b'

    if answer == correct_answer:
        score += 1
        return score, False
    else:
        return score, True


def game():
    global A, B, score, game_over

    while not game_over:
        print(art.logo)

        print(f"Compare A: {formate_data(A)}")

        print(art.vs)

        print(f"Against B: {formate_data(B)}")

        answer = input("Who has more followers? Type 'A' or 'B': ").lower()

        score, game_over = check(answer)

        A = B
        B = random.choice(data)
        while A == B:
            B = random.choice(data)

        print(" \n"*20)

    print(f"Sorry, that's wrong. Final score: {score}")


game()

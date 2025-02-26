rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random

game = [rock, paper, scissors]

user = int(input("Choose a number from 0,1,2 .\n"))

print("You selected")

if user >= 0 & user <= 2:
    print(game[user])

print("Computer selected")

com = random.randint(0,2)

print(game[com])

if user<0 | user>2:
    print("You selected ina wrong way. You lose")
elif user==0 & com ==2:
    print("You win")
elif user ==2 & com ==0:
    print("You lose")
elif user > com:
    print("You win")
elif user < com:
    print("You lose")
elif user == com:
    print("You draw")
import random

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

game = [rock,paper,scissors]
choice= int(input("what do you choose? type 0 for rock, 1 for paper or 2 for scissor. "))

if choice>=3:
    print("invalid input!!")
else:
    user_choice = game[choice]
    print(game[choice])
    print("computer chooses: \n")

    comp_choice= random.choice(game)
    print(comp_choice)
    if user_choice== comp_choice:
        print("IT'S A DRAW")

    elif user_choice==2 and comp_choice==0:
        print("you lose!!")
    elif user_choice==0 and comp_choice==2 :
        print("you win!!")
    elif comp_choice>user_choice:
        print("you lose!!")
    elif comp_choice<user_choice:
        print("you win!!")


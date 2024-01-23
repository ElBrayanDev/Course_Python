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

game_options = [rock, paper, scissors]

choice = int(
    input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
ran = random.randint(0, 2)

print("Your chose: ")
print(game_options[choice])

print("Computer chose: ")
print(game_options[ran])

if choice == ran:
    print("Tie")
elif choice == 0 and ran == 2:
    print("You win")
elif choice == 1 and ran == 0:
    print("You win")
elif choice == 2 and ran == 1:
    print("You win")
elif choice == 0 and ran == 1:
    print("You lose")
elif choice == 1 and ran == 2:
    print("You lose")
elif choice == 2 and ran == 0:
    print("You lose")

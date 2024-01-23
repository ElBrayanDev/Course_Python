from art import logo
import random

def guess(num:int()):
    if num == RANDOM_NUMBER:
        print(f"You nailed it!")
        return 0
    elif num > RANDOM_NUMBER:
        print(f"Too high")
    elif num < RANDOM_NUMBER:
        print(f"Too low")


RANDOM_NUMBER = random.randint(1, 100)
attempts = int()
print(logo)
print("I'm thinking of a number bewteen 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard':")
if difficulty == "easy":
    attempts = 10
elif difficulty == "hard":
    attempts = 5
else:
    print("Wrong input, try again")

while attempts != 0:
    print(f"You have {attempts} attempts remaining to guess the number.")
    guessed = guess(int(input("Make a guess: ")))
    if guessed == 0:
        break
    attempts -= 1
if guessed != 0:
    print(f"The number was {RANDOM_NUMBER}")
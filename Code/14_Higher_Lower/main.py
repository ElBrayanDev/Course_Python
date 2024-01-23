from art import logo, vs
from data import data
import random
import os

def getPersonA():
    a = random.choice(data)
    print(f"A: {a['name']}, {a['description']}, from {a['country']}")
    #print(f"Followers: {a['follower_count']}")
    data.remove(a)
    return a

# Changes the print with 'B'
def getPersonB(): 
    b = random.choice(data)
    print(f"B: {b['name']}, {b['description']}, from {b['country']}")
    #print(f"Followers: {a['follower_count']}")
    data.remove(b)
    return b

def compare(a: dict, b:dict):
    if a['follower_count'] > b['follower_count']:
        return "A"
    elif a['follower_count'] < b['follower_count']:
        return "B"
    elif a['follower_count'] == b['follower_count']:
        return

def printInfo(a: dict):
    print(f"A: {a['name']}, {a['description']}, from {a['country']}")
    #print(f"Followers: {a['follower_count']}")

score = int()
won = True
print(logo)
a = getPersonA()
print(vs)
b = getPersonB()

while won == True:
    if score > 0:
        printInfo(a)
        print(vs)
        b = getPersonB()

    guess = input("Who has more followers? Type 'A' or 'B': ")
    if compare(a, b) == guess:
        score += 1
        if guess == "B":
            a = b

        os.system('cls')
        print(logo)
        print(f"Correct! Your score is: {score}")
    else:
        os.system('cls')
        print(logo)
        print(f"That's wrong. Final score: {score}")
        won = False

    
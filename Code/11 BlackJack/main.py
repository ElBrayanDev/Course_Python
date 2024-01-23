############### Blackjack Project #####################

# Difficulty Normal 😎: Use all Hints below to complete the project.
# Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
# Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
# Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

# The deck is unlimited in size.
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The the Ace can count as 11 or 1.
# Use the following list as the deck of cards:
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.
# The computer is the dealer.

##################### Hints #####################

# Hint 1: Go to this website and try out the Blackjack game:
#   https://games.washingtonpost.com/games/blackjack/
# Then try out the completed Blackjack project here:
#   http://blackjack-final.appbrewery.repl.run


# Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

# Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

# Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.
import os
import random
from art import logo


def checkAce(cards1):
    if 11 in cards1 and sum(cards1) > 21:
        cards1.remove(11)
        cards1.append(1)


def drawStartingCards(user_cards, cuprier_cards):
    user_cards.append(random.choice(cards))
    user_cards.append(random.choice(cards))
    cuprier_cards.append(random.choice(cards))
    checkAce(user_cards)
    checkAce(cuprier_cards)


def drawCard(cards1):
    cards1.append(random.choice(cards))
    checkAce(cards1)


def count(count1, cards1):
    count1 = sum(cards1)
    return count1


def checkWinner(countUser: int, countCuprier: int):

    if countUser > 21:  # You are over 21
        return -3
    elif countCuprier > 21:  # Cuprier is over 21
        return 3
    # deuce
    elif countUser == countCuprier or (countUser > 21 and countCuprier > 21):
        return 0
    elif countCuprier == 21:  # Cuprier has a Blackjack
        return -1
    elif countUser == 21:  # You have a Blackjack
        return 1
    else:
        if (countUser - 21) < (countCuprier - 21):  # Cuprier is closer to 21
            return -2
        else:
            return 2  # You are closer to 21


def winner(num):
    if num == 0:
        print(f"Deuce")
    elif num == -1:
        print(f"You lose, cuprier has a Blackjack :(")
    elif num == 1:
        print(f"You win, you have a Blackjack :)")
    elif num == -3:
        print(f"You lose, you are over 21 :(")
    elif num == 3:
        print(f"You win, cuprier is over 21 :)")
    elif num == -2:
        print(f"You lose, cuprier is closer to 21 :(")
    elif num == 2:
        print(f"You win, you are closer to 21 :)")


def printCards(user_cards, cuprier_cards):
    print(f"Your cards: {user_cards}")
    print(f"Score: {countUser}")
    print(f"Cuprier cards: {cuprier_cards}")
    print(f"Score: {countCuprier}")


draw = ""
play = ""
countUser = 0
user_cards = []
countCuprier = 0
cuprier_cards = []

play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

while play == "y":
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    print(logo)
    drawStartingCards(user_cards, cuprier_cards)
    countUser = count(countUser, user_cards)
    countCuprier = count(countCuprier, cuprier_cards)

    if countUser == 21 or countCuprier == 21 or countUser > 21 or countCuprier > 21:
        drawCard(cuprier_cards)
        countCuprier = count(countCuprier, cuprier_cards)
        printCards(user_cards, cuprier_cards)
        winner(checkWinner(countUser, countCuprier))
        draw = "n"

    while draw != "n":
        printCards(user_cards, cuprier_cards)
        draw = input("Type 'y' to get another card, type 'n' to pass: ")
        if draw == "y":
            drawCard(user_cards)
            countUser = count(countUser, user_cards)
            countCuprier = count(countCuprier, cuprier_cards)

            if countUser == 21 or countCuprier == 21 or countUser > 21 or countCuprier > 21:
                while countCuprier < 17:
                    drawCard(cuprier_cards)
                    countCuprier = count(countCuprier, cuprier_cards)
                winner(checkWinner(countUser, countCuprier))
                draw = "n"
        else:
            if draw == "n":
                while countCuprier < 17:
                    drawCard(cuprier_cards)
                    countCuprier = count(countCuprier, cuprier_cards)
                printCards(user_cards, cuprier_cards)
                winner(checkWinner(countUser, countCuprier))

        if countUser == 21 or countCuprier == 21 or countUser > 21 or countCuprier > 21:
            printCards(user_cards, cuprier_cards)
            break

    play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if play == "y":
        user_cards = []
        cuprier_cards = []
        countUser = 0
        countCuprier = 0
        draw = ""
        os.system("cls")
os.system("cls")

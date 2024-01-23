# Step 1
import random
import hangman_art
import hangman_words
from turtle import clear

word_list = hangman_words.word_list
stages = hangman_art.stages

chosen_word = random.choice(word_list)
# print(f"{chosen_word}")

display = []
tries = []
display = ["_"] * len(chosen_word)

print(f"{hangman_art.logo}")
print(f"{' '.join(display)}")

lives = 7
hasWon = False
while not hasWon and lives > 0:

    enteredLetter = False
    guess = input("Enter a letter: ").lower()

    clear()

    if guess in tries:
        print(f"You have already entered the letter '{guess}'")
    else:
        if guess not in chosen_word:
            print(f"The letter '{guess}' is not on the word")
            lives -= 1

    tries.append(guess)

    i = 0
    for a in chosen_word:
        if guess == a:
            display[i] = guess
        i += 1

    print(f"{' '.join(display)}")
    print(f"Lives: {lives}")

    if "_" not in display:
        hasWon = True
        print("YOU WIN!")

    print(stages[lives - 1])

if lives <= 0:
    print("YOU LOSE!")
    print(f"The word was '{chosen_word}")

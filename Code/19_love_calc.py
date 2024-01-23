print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

score = 0
score2 = 0

name1 = name1.lower()
name2 = name2.lower()

true = "true"
love = "love"


for c in love:
    score2 += name1.count(c)
    score2 += name2.count(c)

for c in true:
    score += name1.count(c)
    score += name2.count(c)

final_score = str(score) + str(score2)
final_score = int(final_score)

if final_score < 10 or final_score > 90:
    print(
        f"Your score is {final_score}, you go together like coke and mentos.")
elif final_score >= 40 and final_score <= 50:
    print(f"Your score is {final_score}, you are alright together.")
else:
    print(f"Your score is {final_score}")

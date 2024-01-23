import random
row1 = ["⬜", "⬜", "⬜"]
row2 = ["⬜", "⬜", "⬜"]
row3 = ["⬜", "⬜", "⬜"]

ran1 = random.randint(1, 3)
ran2 = random.randint(1, 3)

matrix = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where's the treasure?")

if position == str(ran1) + ", " + str(ran2):
    print("You found the treasure!")
else:
    print("Wrong place")

matrix[ran2-1][ran1-1] = "X"

print(f"{row1}\n{row2}\n{row3}")

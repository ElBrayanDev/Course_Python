import random

name_string = input("Names separated by a comma. ")
names = name_string.split(", ")  # Splits the string into a list according to the key given as parameter
# ran = random.randint(0, len(names)-1)
# print(ran)
# print(f"{names[ran]} has to pay the bill.")

# or 
print(f"{random.choice(names)} has to pay the bill.")

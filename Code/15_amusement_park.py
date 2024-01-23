print("Welcome to the rollercoaster!")

height = int(input("What is your height? (cm)"))

if height < 120:
    print("You can't ride the rollercoaster ;(")
else:
    age = int(input("You can ride it :D \nHow old are you?"))
    if age < 18:
        ticket = 7
    else:
        ticket = 12
    print(f"You have to pay ${ticket} for the rollercoaster ticket\n\tEnjoy!")

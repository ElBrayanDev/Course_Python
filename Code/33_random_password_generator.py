# Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91


# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

total = nr_letters + nr_numbers + nr_symbols
rand = 0
list = [letters, numbers, symbols]
len_letters = len(letters) - 1
len_numbers = len(numbers) - 1
len_symbols = len(symbols) - 1
password = ""

while True:

    if nr_letters == 0 and nr_numbers == 0 and nr_symbols == 0:
        break
    else:
        temp = random.choice(list)
        if temp == letters:
            if nr_letters != 0:
                password = password + letters[random.randint(0, len_letters)]
                nr_letters = nr_letters - 1
        elif temp == numbers:
            if nr_numbers != 0:
                password = password + numbers[random.randint(0, len_numbers)]
                nr_numbers = nr_numbers - 1
        else:
            if nr_symbols != 0:
                password = password + symbols[random.randint(0, len_symbols)]
                nr_symbols = nr_symbols - 1
print(f"Your password is: {password}")

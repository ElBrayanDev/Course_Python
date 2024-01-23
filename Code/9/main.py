import os

from art import logo

def bid(name, amount):
    bids_dictionary[name] = int(amount)

print(logo)
print("Welcome to the secret auction program.")

bids_dictionary = {}
keep_bidding =  ""
more_bidders = True

while more_bidders:
    name = input("What is your name?: ")
    amount = int(input("What's your bid?: $"))
    bid(name, amount)

    while keep_bidding != "no" and keep_bidding != "yes":
        keep_bidding = input("Are there any other bidders? Type 'yes' or 'no'.")
        if keep_bidding == "no":
            more_bidders =  False
    os.system('cls')
    keep_bidding = ""

winner_bid = max(bids_dictionary.values())
winner_name = max(bids_dictionary, key=bids_dictionary.get)
print(f"The winner is {winner_name} with a bid of {winner_bid}")
print(bids_dictionary)
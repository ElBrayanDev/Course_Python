MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}

def insertCoins(dollars: int):
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    dollars = (pennies * 0.01) + (nickles * 0.05) + (dimes * 0.1) + (quarters * 0.25) 
    return dollars

def getChange(dollars: int, item_price: int):
    return dollars - item_price

def getCoffee(choice: str):
    if resources["water"] >= MENU[choice]["ingredients"]["water"] and resources["milk"] >= MENU[choice]["ingredients"]["milk"] and resources["coffee"] >= MENU[choice]["ingredients"]["coffee"]:
        resources["water"] = resources["water"] - MENU[choice]["ingredients"]["water"]
        resources["milk"] = resources["milk"] - MENU[choice]["ingredients"]["milk"]
        resources["coffee"] = resources["coffee"] - MENU[choice]["ingredients"]["coffee"]
        resources["money"] = resources["money"] + MENU[choice]["cost"]
        return True
    else:   
        if resources["water"] < MENU[choice]["ingredients"]["water"]:
            print(f"Sorry there is not enough water.")
        if resources["milk"] < MENU[choice]["ingredients"]["milk"] :
            print(f"Sorry there is not enough milk.")
        if resources["coffee"] < MENU[choice]["ingredients"]["coffee"]:
            print(f"Sorry there is not enough coffee.")
        return False

do = ""
dollars = int
change = int
can_continue = bool
while do != "off":
    choice = input(f"What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == "off":
        break
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${resources['money']}")
    elif choice == "espresso" or choice == "latte" or choice == "cappuccino":
        dollars = insertCoins(dollars)
        if dollars > MENU[choice]['cost']:
            can_continue =  getCoffee(choice)
            if can_continue == True:
                change = getChange(dollars, MENU[choice]['cost'])
                print(f"Here is ${change} in change.")
                print(f"Here is your {choice} ☕. Enjoy!")
        elif dollars == MENU[choice]['cost']:
            can_continue = getCoffee(choice)
            if can_continue == True:
                print(f"No change.")
                print(f"Here is your {choice} ☕. Enjoy!")
        elif dollars < MENU[choice]['cost']:
            print(f"Sorry that's not enough money. Money refunded")
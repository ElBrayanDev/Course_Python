from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

do = ""
dollars = int
change = int
can_continue = bool
while do != "off":
    choice = input(f"What would you like? ({menu.get_items()}): ").lower()
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
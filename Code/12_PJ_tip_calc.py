print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
tip = tip/100
people = int(input("How many people to split the bill? "))
total = bill + (bill*tip)
splited_pay = round(total/people, 2)
splited_pay = "{:.2f}".format(splited_pay)  # ! Format to .00 (two decimals) Ex: 33.60
print(f"Each person should pay: ${splited_pay}")

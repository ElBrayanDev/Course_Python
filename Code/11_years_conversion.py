# Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.

# It will take your current age as the input and output a message with our time left in this format:

# You have x days, y weeks, and z months left.

max_age = 90

age = int(input("What is your current age? "))
years_left = max_age - age

months = years_left*12
weeks = years_left*52
days = years_left*365


print(f"You have {days} days, {weeks} weeks, and {months} months left.")

print(6 + 4 / 2 - (1 * 2))

pi = 3.14159
n1 = 10
str1 = "Brayan"

list1 = [str1, n1, pi]

print(f"{list1}")
print(f"{list1[0]}")
print(f"{list1[-1]}")  # ! Access from the end of the list
list1.extend("Hello")
print(f"{list1}")

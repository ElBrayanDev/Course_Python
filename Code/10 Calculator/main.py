from art import logo
import os

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def calculator():
    keep_result = "y"
    diccionario_operaciones = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide,
    }
    a = float(input("What's the first number?: "))
    print("+\n-\n*\n/")
    
    while keep_result == "y":
        choice = input("Pick an operation: ")
        b = float(input("What's the next number?: "))
        result = diccionario_operaciones[choice](a, b)
        print(f"{a} {choice} {b} = {result}")

        keep_result = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")
        os.system('cls')

        if keep_result == "y":
            a = result
            print(f"{a}")
        else:
            calculator()


print(logo)
keep_result = "y"
calculator()
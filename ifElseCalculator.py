#Switch Case Calculator

import colorama
from colorama import Fore

#initialize colorama
colorama.init()

print(colorama.Fore.RED + "\n\t--------------------------" + colorama.Style.RESET_ALL)
print(colorama.Fore.RED + "\t| Switch Case Calculator |" + colorama.Style.RESET_ALL)
print(colorama.Fore.RED + "\t--------------------------" + colorama.Style.RESET_ALL)

#Deinitialize colorama
colorama.deinit()

name = input("\nHello there! Your name, please:  ")

print(f"\n{name}, please type:")

num1 = float(input("\nPlease enter 1st number: "))
num2 = float(input("\nPlease enter 2nd number: "))

print(colorama.Fore.BLUE + "\n===================================\n" ) 
print("  [+] if addition")
print("  [-] if subtraction")
print("  [*] if multiplication")
print("  [/] if division")
print("  [A] all of the operations above")
print("\n===================================\n\n" + colorama.Style.RESET_ALL)

choice = input("Please, enter your choice: ")

sum = num1 + num2
difference = num1 - num2
product = num1 * num2
quotient = num1 / num2

sum = round(sum, 2)
difference = round(difference, 2)
product = round(product, 2)
quotient = round(quotient, 2)

if choice == "+":
    print("\nYou chose ADDITION!")
    print(f"{num1} + {num2} = {sum}!\n")

elif choice == "-":
    print("\nYou chose SUBTRACTION!")
    print(f"{num1} - {num2} = {difference}!\n")

elif choice == "*":
    print("\nYou chose MULTIPLICATION!")
    print(f"{num1} * {num2} = {product}!\n")

elif choice == "/":
    print("\nYou chose DIVISION!")
    print(f"{num1} / {num2} = {quotient}!\n")

elif choice == "A" or choice == "a":
    print("\nYou chose EVERYTHING!")

    print(f"\n{num1} + {num2} = {sum}!")
    print(f"{num1} - {num2} = {difference}!")
    print(f"{num1} * {num2} = {product}!")
    print(f"{num1} / {num2} = {quotient}!\n")

else:
    print(f"\n{name}, not a valid choice! :(\n")

print(f"Thank you for using the calculator program, {name}! :D\n")
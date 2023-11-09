#Simple Calculator Program!

print("\nHello! This is a calculator program!")

num1 = float(input("Please, enter 1st number: "))
num2 = float(input("Please, enter 2nd number: "))

print("\n==============")

sum = num1 + num2
difference = num1 - num2
product = num1 * num2
quotient = num1 / num2

quotient = round(quotient, 2)

print(f"Addition: {num1} + {num2} = {sum}")
print(f"Difference: {num1} - {num2} = {difference}")
print(f"Product: {num1} * {num2} = {product}")
print(f"Quotient: {num1} / {num2} = {quotient}")

print("\n==============")
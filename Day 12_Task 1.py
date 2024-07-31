def addition(x, y):
    print(x + y)


def subtraction(x, y):
    print(x - y)


def multiplication(x, y):
    print(x * y)


def division(x, y):
    print(x / y)


def modulus(x, y):
    print(x % y)


x = int(input("Enter the number 1: "))
y = int(input("Enter the number 2: "))
condition = input("Choose which operation you need '+', '-', '*', '/', '%'. ")

if condition == "+":
    addition(x, y)
elif condition == "-":
    subtraction(x, y)
elif condition == "*":
    multiplication(x, y)
elif condition == "/":
    division(x, y)
elif condition == "%":
    modulus(x, y)
else:
    print("Choose your operation.")

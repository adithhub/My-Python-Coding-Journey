name = input("Enter your name: ")
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operation = int(input("Enter the operation you need. 1 = Addition. 2 = Subtraction. 3 = Multiplication.,"
                      " 4 = division. 5 = Modulus. 6 = Exponentiation. 7 = Floor division: "))
if operation == 1:
    print(num1 + num2, " is the output")
elif operation == 2:
    print(num1 - num2, " is the output")
elif operation == 3:
    print(num1 * num2, " is the output")
elif operation == 4:
    print(num1 / num2, " is the output")
elif operation == 5:
    print(num1 % num2, " is the output")
elif operation == 6:
    print(num1 ** num2, " is the output")
elif operation == 7:
    print(num1 // num2, " is the output")
else:
    print("No operations left please select 1 to 7.")

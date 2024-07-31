# print all even numbers from a given list

limit = int(input("Enter the limit: "))
numbers = []
for i in range(limit):
    num = int(input('Enter the values: '))
    if num % 2 == 0:
        numbers.append(num)
print(numbers)

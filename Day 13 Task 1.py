# sum of numbers in a list
limit = int(input("Enter the limit"))
numbers = []
for i in range(limit):
    num = int(input("Enter the value: "))
    numbers.append(num)


def calculate_sum(numbers):
    total = 0

    for number in numbers:
        total += number

    return total


result = calculate_sum(numbers)
print("Sum:", result)

"""
This module contains a function to print even numbers from a user-defined list.
"""


def print_even_numbers(numbers):
    """
    Print even numbers from the given list.

    Args:
        numbers (list): List of integers to check for even numbers.
    """
    even_numbers = []

    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)

    print("Even numbers in the list: ", even_numbers)


limit = int(input("Enter the limit: "))
numbers = []
for i in range(limit):
    num = int(input("Enter the value: "))
    numbers.append(num)

print_even_numbers(numbers)

# second-largest element in a tuple
limit = int(input("Enter the limit: "))
numbers = []

for i in range(limit):
    num = int(input('Enter the values: '))
    numbers.append(num)

numbers.sort()
my_tuple = tuple(numbers)
print(f"The second largest number of this set is {my_tuple[-2]}")

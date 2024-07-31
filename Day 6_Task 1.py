# Replace all odd numbers into & print it in reverse order
limit = int(input("Enter the limit: "))
numbers = []

# Input numbers into the list
for i in range(limit):
    num = int(input(f"Enter value {i+1}: "))
    numbers.append(num)

# Replace odd numbers with "&"
for i in range(limit):
    if numbers[i] % 2 != 0:
        numbers[i] = "&"

# Print the list in reverse order
print("Modified list in reverse order:")
# numbers.reverse()
# print(numbers)
print(numbers[::-1])

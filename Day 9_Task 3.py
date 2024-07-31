# print the most repeating number and if the most repeating number is 2, 3 the most repeating number should print 2, 3
# Input the limit
limit = int(input("Enter the limit: "))

# Initialize an empty list to store numbers
numbers = []

# Input numbers from user
for i in range(limit):
    num = int(input("Enter the value: "))
    numbers.append(num)

# Initialize an empty dictionary to count occurrences
count_dict = {}

# Count occurrences of each number
for num in numbers:
    if num in count_dict:
        count_dict[num] += 1
    else:
        count_dict[num] = 1

# Find the maximum occurrence count
max_occurrences = max(count_dict.values())

# Initialize a list to store the most repeating numbers
most_repeating_numbers = []

# Find numbers with the maximum count
for num, count in count_dict.items():
    if count == max_occurrences:
        most_repeating_numbers.append(num)

# Print the most repeating numbers
print(f"The most repeating number(s) is/are: {', '.join(map(str, most_repeating_numbers))}")

# Write a program to count the total number of unique elements in a list.
limit = int(input("Enter the limit: "))
my_list = []
for i in range(limit):
    num = int(input("Enter the value: "))
    my_list.append(num)
# Initialize an empty list to store unique elements
unique_elements = []

# Loop through each element in the list
for element in my_list:
    if element not in unique_elements:
        unique_elements.append(element)

# Count the number of unique elements
unique_count = len(unique_elements)

print(f"Total number of unique elements: {unique_count}")

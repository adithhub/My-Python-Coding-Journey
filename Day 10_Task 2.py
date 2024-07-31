# Write a program to delete all duplicate elements from a list.
limit = int(input("Enter the limit: "))
lst = []
for i in range(limit):
    num = int(input("Enter the value: "))
    lst.append(num)
# Initialize an empty list to store unique elements
unique_lst = []

# Loop through each element in the original list
for item in lst:
    # If the element is not already in the unique list, add it
    if item not in unique_lst:
        unique_lst.append(item)

# Print the original list and the list with duplicates removed
print("Original list:", lst)
print("List after removing duplicates:", unique_lst)

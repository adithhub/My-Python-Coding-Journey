# print values in tuple without duplication
limit = int(input("Enter the limit: "))
my_list = []

print(f"Enter the {limit} numbers")
for i in range(limit):
    num = int(input(f'Enter number {i + 1}: '))
    if num not in my_list:
        my_list.append(num)

my_tuple = tuple(my_list)
print(f"The tuple after deleting the duplication {my_tuple}")

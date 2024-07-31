# find the sum of the list except even numbers which are divisible by 3

# numbers = []
# for i in range(1, 5):
#     numbers.append(i)
# total = 0
# for num in numbers:
#     if num % 2 == 0 or num % 3 != 0:
#         total += num
# print(total)

limit = int(input("Enter the Limit"))
my_list = []
total_sum = 0

for i in range(limit):
    num = int(input("Enter the value"))
    if num % 2 != 0 or num % 3 != 0:
        my_list.append(num)
        total_sum += num
print(total_sum)

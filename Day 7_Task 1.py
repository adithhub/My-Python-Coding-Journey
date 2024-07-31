# calculate the sum of all odd numbers
limit = int(input("Enter the limit: "))
sum_of_odds = 0
my_list = []
# Iterate through numbers from 1 to limit
for num in range(limit):
    list_num = int(input("Enter the value: "))
    if list_num % 2 != 0:
        sum_of_odds += list_num

print(f"The sum of all odd numbers up to {limit} is: {sum_of_odds}")

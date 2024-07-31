num = int(input("Enter the numbers: "))
total = 0
count = 0
for i in range(num):
    print(i)
    number = float(input(f"Enter number {i + 1}: "))
    total += number
    count += 1
average = total/count
print(f"the average of {num} is: {average}")

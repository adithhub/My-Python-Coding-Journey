# replace multiples of 7 into % and multiples of 2 into @

number = []
for i in range(1, 11):
    number.append(i)
for i in range(len(number)):
    if number[i] % 7 == 0:
        number[i] = "%"
    elif number[i] % 2 == 0:
        number[i] = "@"
print(number)

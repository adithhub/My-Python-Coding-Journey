year = int(input("Enter the year: "))
if (year % 4 == 0 and year % 100 != 0):
    print("It's Leap Year")
else:
    print("It's not Leap year")

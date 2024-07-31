# Given a string S (input consisting) of ‘*’ and ‘#’. The length of the string is
# variable. The task is to find the minimum number of ‘*’ or ‘#’ to make it a
# valid string. The string is considered valid if the number of ‘*’ and ‘#’ are
# equal. The ‘*’ and ‘#’ can be at any position in the string.
# Note: The output will be a positive or negative integer based on number
# of ‘*’ and ‘#’ in the input string.
# 1. (*>#): positive integer
# 2. (#>*): negative integer
# 3. (#=*): 0
S = "**##*#*"

count_star = 0
count_hash = 0

# Count the number of '*' and '#'
for char in S:
    if char == '*':
        count_star += 1
    elif char == '#':
        count_hash += 1

# Calculate the difference
difference = count_star - count_hash

# Output the result based on the difference
if difference > 0:
    print(f"Positive integer: {difference}")
elif difference < 0:
    print(f"Negative integer: {difference}")
else:
    print("0")

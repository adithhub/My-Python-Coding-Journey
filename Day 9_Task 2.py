# *****
# ****
# ***
# **
# *

#      *
#     **
#    ***
#   ****
#  *****

row = 5
while row >= 1:
    print('* ' * row)
    row -= 1

row = 1
while row <= 5:
    spaces = '  ' * (5 - row)
    stars = '* ' * row
    print(spaces + stars)
    row += 1

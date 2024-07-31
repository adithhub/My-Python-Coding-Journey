thisList = ['Apple', 'Banana', 'Cherry', 'Watermelon', 'Gooseberry', 'Pineapple', 'Dragon fruit', 'Peach', 'Orange']
print(thisList[2:5])
print(thisList[4])
print(thisList[2:])
print(thisList[:5])
print(thisList[-1])
print(thisList[-7:-1])
print(thisList[-7:-4])

if "Apple" in thisList:
    print("Yes, Apple is given")
else:
    print("Sorry")
# it's for adding value to 2nd index
thisList[2] = "Blackcurrant"
print(thisList)
# it's for adding value to a group of index
thisList[3:5] = "Strawberry", "Avocado"
print(thisList)
# to insert a value on given index
thisList.insert(7, "Lemon")
print(thisList)
# to append the object to the list
thisList.append("Lime")
print(thisList)
# to extend a list with another list
extendingList = ['Mango', 'Kiwi', 'Blueberry']
thisList.extend(extendingList)
print(thisList)
# to extend a list with another tuple
extendingTuple = ('Fig', 'Papaya')
thisList.extend(extendingTuple)
print(thisList)

thisList.remove("Apple")
print(thisList)

thisList.pop(0)
print(thisList)

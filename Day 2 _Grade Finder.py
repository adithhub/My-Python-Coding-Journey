name = input("Enter your Name: ")
marks = int(input("Enter the total marks: "))
if marks >= 90:
    print("A Grade")
elif marks >= 80:
    print("B Grade")
elif marks >= 70:
    print("C Grade")
elif marks >= 60:
    print("D Grade")
else:
    print("Failed")

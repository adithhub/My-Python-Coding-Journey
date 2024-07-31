user_name = input("Enter your name. ")
user_email = input("Enter your email. ")
phone_number = int(input("Enter your phone number"))
course = input("Enter your course name. ")

with open(f"{user_name}.txt", "w") as f:
    f.write(f"user_name: {user_name} \nstudent's email: {user_email}\nstudent's phone number: "
            f"{phone_number} \ncourse name: {course}\n")
    f.close()

f = open(f"{user_name}.txt", "r")
print(f.read())
print("Registration done. Thanks for submitting. ")

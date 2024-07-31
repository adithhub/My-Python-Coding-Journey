import os

# import the os
operations = int(input("1. Create a file. 2. Read a file. 3. Delete a file. "))  # operations to do


def user_inputs():  # function to take user details.
    name = input("Enter your name: ")
    email = input('Enter your email: ')
    phone_number = input("Enter your phone number: ")
    course = input("Enter your course: ")
    details = input("Enter the content: ")
    return f"Name: {name}\nEmail: {email}\nPhone Number: {phone_number}\nCourse: {course}\nContent: {details}\n"


if operations == 1:
    data_to_write = user_inputs()
    file_name = input("Enter the file name: ")

    with open(file_name, "w") as f:
        f.write(data_to_write)
    print(f"Data has been written to {file_name}")


elif operations == 2:

    filename = input("Enter the name of the file to read: ")
    if os.path.exists(filename):
        with open(filename, "r") as f:
            content = f.read()
        print("Contents of '" + filename + "':\n" + content + "\n")
    else:
        print("File '" + filename + "' does not exist.\n")

elif operations == 3:
    filename = input("Enter the name of the file to delete: ")
    if os.path.exists(filename):
        os.remove(filename)
        print("File '" + filename + "' deleted successfully.\n")
    else:
        print("File '" + filename + "' does not exist.\n")

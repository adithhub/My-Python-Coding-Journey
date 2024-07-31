import os

# Operations to do
operations = int(input("1. Create a file. 2. Read a file. 3. Delete a file: "))


def user_inputs():
    """
    Function to take user details.
    Returns a formatted string with user details and content.
    """
    name = input("Enter your name: ")
    email = input('Enter your email: ')
    phone_number = input("Enter your phone number: ")
    course = input("Enter your course: ")
    details = input("Enter the content: ")
    return f"Name: {name}\nEmail: {email}\nPhone Number: {phone_number}\nCourse: {course}\nContent: {details}\n"


if operations == 1:
    # Writing to a file
    data_to_write = user_inputs()
    file_name = input("Enter the file name: ")

    with open(file_name, "w", encoding="utf-8") as f:
        f.write(data_to_write)
    print(f"Data has been written to {file_name}")

elif operations == 2:
    # Reading from a file
    filename = input("Enter the name of the file to read: ")
    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as f:
            content = f.read()
        print(f"Contents of '{filename}':\n{content}\n")
    else:
        print(f"File '{filename}' does not exist.\n")

elif operations == 3:
    # Deleting a file
    filename = input("Enter the name of the file to delete: ")
    if os.path.exists(filename):
        os.remove(filename)
        print(f"File '{filename}' deleted successfully.\n")
    else:
        print(f"File '{filename}' does not exist.\n")

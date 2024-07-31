import re


def email_validation(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email.strip())  # Strip whitespace around email


def phone_number_validation(number):
    pattern = r'^\d{10}$'
    return bool(re.match(pattern, number.strip()))  # Strip whitespace and return boolean


def password_validation(password):
    # Adjust the password pattern and criteria as needed
    pattern = r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$'
    return re.match(pattern, password.strip())


def register_student():
    user_name = input("Enter your name: ")
    user_password = ""
    while not password_validation(user_password):
        user_password = input("Enter your password (at least 8 characters including letters and numbers): ")
        if not password_validation(user_password):
            print("Password must be at least 8 characters long and include both letters and numbers.")

    user_email = ""
    while not email_validation(user_email):
        user_email = input("Enter your email: ")
        if not email_validation(user_email):
            print("Enter a valid email.")

    phone_number = ""
    while not phone_number_validation(phone_number):
        phone_number = input("Enter your phone number: ")
        if not phone_number_validation(phone_number):
            print("Enter a valid 10-digit phone number.")

    course = input("Enter your course name: ")

    filename = f"{user_name}.txt"
    try:
        with open(filename, "w") as f:
            f.write(f"user_name: {user_name}\nstudent's email: {user_email}\nstudent's phone number: "
                    f"{phone_number}\ncourse name: {course}\n")

        with open(filename, "r") as f:
            print(f.read())

        print("Registration done. Thanks for submitting.")
    except IOError as e:
        print(f"Error writing to file: {e}")


register_student()

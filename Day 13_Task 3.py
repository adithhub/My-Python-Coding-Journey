import re


def validate_email(email):
    """Validate email address using regular expression."""
    pattern = r'^[\w\.-]+@[\w\.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email)


def validate_phone(phone):
    """Validate phone number using regular expression."""
    pattern = r'^\d{3}-\d{3}-\d{4}$'  # XXX-XXX-XXXX format
    return re.match(pattern, phone)


def validate_username(username):
    """Validate username using regular expression."""
    pattern = r'^[a-zA-Z][a-zA-Z0-9_-]{2,15}$'
    return re.match(pattern, username)


def get_user_input(prompt, validator):
    """Prompt user for input and validate using the provided validator function."""
    while True:
        try:
            user_input = input(prompt)
            if validator(user_input):
                return user_input
            print("Invalid input. Please try again.")
        except Exception as e:
            print(f"Error: {e}. Please try again.")


def create_form():
    """Create a form to collect user information."""
    print("Welcome to the Form!")

    first_name = get_user_input("Enter your first name: ", lambda x: True)
    last_name = get_user_input("Enter your last name: ", lambda x: True)
    username = get_user_input(
        "Enter your username (3-16 characters starting with a letter, alphanumeric or underscore): ", validate_username)
    email = get_user_input("Enter your email address: ", validate_email)
    phone = get_user_input("Enter your phone number (XXX-XXX-XXXX format): ", validate_phone)

    password = get_user_input("Enter your password (at least 8 characters): ", lambda x: len(x) >= 8)
    get_user_input("Confirm your password: ", lambda x: x == password)

    print("\nForm submitted successfully!")
    print(f"First Name: {first_name}")
    print(f"Last Name: {last_name}")
    print(f"Username: {username}")
    print(f"Email: {email}")
    print(f"Phone: {phone}")
    # Note: Avoid printing passwords or sensitive information in real applications


# Call the function to create the form
create_form()

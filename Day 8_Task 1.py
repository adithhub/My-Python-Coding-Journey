# Check the string is palindrome

input_string = str(input("Enter a string: "))
if input_string == input_string[::-1]:
    # s = input_string.replace(" ", "").lower()
    print(f"{input_string} is a palindrome.")
elif input_string != input_string[::-1]:
    print(f"{input_string} is not a palindrome.")

rows = int(input("Enter the rows: "))  # Number of rows in the rectangle
columns = int(input("Enter the columns: "))  # Number of columns in the rectangle

for i in range(rows):  # Outer loop for rows
    for j in range(columns):  # Inner loop for columns
        print('*', end=' ')  # Print a star with a space after it
    print()  # Move to the next line after printing each row

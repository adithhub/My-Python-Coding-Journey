# SQL task with CRUD operations
import mysql.connector
from mysql.connector import Error

# Connect to the MySQL database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="Database1"
)
cursor = conn.cursor()
print("Database connection successful.")

# Create table if it doesn't exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS Workers (
    WORKER_ID INT PRIMARY KEY,
    FIRST_NAME VARCHAR(100),
    LAST_NAME VARCHAR(200),
    SALARY INT,
    JOINING_DATE DATE,
    DEPARTMENT VARCHAR(200)
)
""")


# Function to insert a new worker
def insert_worker(worker_id, first_name, last_name, salary, joining_date, department):
    try:
        cursor.execute("""
        INSERT INTO Workers (WORKER_ID, FIRST_NAME, LAST_NAME, SALARY, JOINING_DATE, DEPARTMENT)
        VALUES (%s, %s, %s, %s, %s, %s)
        """, (worker_id, first_name, last_name, salary, joining_date, department))
        conn.commit()
        print("Worker inserted successfully.")
    except Error as e:
        print(f"Error inserting worker: {e}")


# Function to update a worker's salary
def update_salary(worker_id, new_salary):
    cursor.execute("""
    UPDATE Workers SET SALARY = %s WHERE WORKER_ID = %s
    """, (new_salary, worker_id))
    conn.commit()
    print("Worker salary updated successfully.")


# Function to update a worker's joining date
def update_joining_date(worker_id, new_joining_date):
    cursor.execute("""
    UPDATE Workers SET JOINING_DATE = %s WHERE WORKER_ID = %s
    """, (new_joining_date, worker_id))
    conn.commit()
    print("Worker joining date updated successfully.")


# Function to update a worker's department
def update_department(worker_id, new_department):
    try:
        cursor.execute("""
        UPDATE Workers SET DEPARTMENT = %s WHERE WORKER_ID = %s
        """, (new_department, worker_id))
        conn.commit()
        print("Worker department updated successfully.")
    except Error as e:
        print(f"Error updating department: {e}")


# Function to delete a worker
def delete_worker(worker_id):
    try:
        cursor.execute("""
        DELETE FROM Workers WHERE WORKER_ID = %s
        """, (worker_id,))
        conn.commit()
        print("Worker deleted successfully.")
    except Error as e:
        print(f"Error deleting worker: {e}")


# Function to display workers based on worker_id and optional column
def display_workers():
    worker_id = input("Enter worker ID to display details (or press Enter to display all workers): ")

    if worker_id:
        try:
            worker_id = int(worker_id)
        except ValueError:
            print("Invalid worker ID. Please enter an integer.")
            return

        column = input("Enter column name to display (leave blank to display all columns): ").upper()

        columns = "WORKER_ID, FIRST_NAME, LAST_NAME, SALARY, JOINING_DATE, DEPARTMENT"
        if column:
            if column in ["WORKER_ID", "FIRST_NAME", "LAST_NAME", "SALARY", "JOINING_DATE", "DEPARTMENT"]:
                columns = column
            else:
                print("Invalid column name. Displaying all columns.")

        query = f"SELECT {columns} FROM Workers WHERE WORKER_ID = %s"
        cursor.execute(query, (worker_id,))
    else:
        cursor.execute("SELECT * FROM Workers")

    rows = cursor.fetchall()

    if rows:
        print("Workers:")
        for row in rows:
            print(row)
    else:
        print("No records found.")


# Main loop
while True:
    print("\nChoose an operation:")
    print("1. Insert a new worker")
    print("2. Update a worker's salary")
    print("3. Delete a worker")
    print("4. Display all workers")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        worker_id = int(input("Enter worker ID: "))
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        salary = int(input("Enter salary: "))
        joining_date = input("Enter joining date (YYYY-MM-DD): ")
        department = input("Enter department: ")
        insert_worker(worker_id, first_name, last_name, salary, joining_date, department)

    elif choice == '2':
        worker_id = int(input("Enter worker ID: "))
        which_col = int(
            input("Enter which column you need to update: 1 to salary, 2 to joining date, 3 to department: "))
        if which_col == 1:
            new_salary = int(input("Enter new salary: "))
            update_salary(worker_id, new_salary)
        elif which_col == 2:
            new_joining_date = input("Enter new joining date (YYYY-MM-DD): ")
            update_joining_date(worker_id, new_joining_date)
        elif which_col == 3:
            new_department = input("Enter the updated department: ")
            update_department(worker_id, new_department)
        else:
            print("Invalid column selection.")

    elif choice == '3':
        worker_id = int(input("Enter worker ID to delete: "))
        delete_worker(worker_id)

    elif choice == '4':
        display_workers()
    elif choice == '5':
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please try again.")

# Close the cursor and connection
cursor.close()
conn.close()

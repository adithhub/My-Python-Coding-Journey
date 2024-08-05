# CRUD operations in Mongodb with python
from pymongo import MongoClient
from datetime import datetime

# Connect to the MongoDB database
client = MongoClient('mongodb://localhost:27017')
db = client['Database1']
collection = db['Workers']
print("Database connection successful.")


# Function to insert a new worker
def insert_worker(worker_id, first_name, last_name, salary, joining_date, department):
    worker = {
        '_id': worker_id,
        'FIRST_NAME': first_name,
        'LAST_NAME': last_name,
        'SALARY': salary,
        'JOINING_DATE': datetime.strptime(joining_date, '%Y-%m-%d'),
        'DEPARTMENT': department
    }
    collection.insert_one(worker)
    print("Worker inserted successfully.")


# Function to update a worker's salary
def update_salary(worker_id, new_salary):
    collection.update_one(
        {'_id': worker_id},
        {'$set': {'SALARY': new_salary}}
    )
    print("Worker salary updated successfully.")


# Function to update a worker's joining date
def update_joining_date(worker_id, new_joining_date):
    collection.update_one(
        {'_id': worker_id},
        {'$set': {'JOINING_DATE': datetime.strptime(new_joining_date, '%Y-%m-%d')}}
    )
    print("Worker joining date updated successfully.")


# Function to update a worker's department
def update_department(worker_id, new_department):
    collection.update_one(
        {'_id': worker_id},
        {'$set': {'DEPARTMENT': new_department}}
    )
    print("Worker department updated successfully.")


# Function to delete a worker
def delete_worker(worker_id):
    collection.delete_one({'_id': worker_id})
    print("Worker deleted successfully.")


# Function to display workers based on worker_id and optional column
def display_workers():
    worker_id = input("Enter worker ID to display details (or press Enter to display all workers): ")

    if worker_id:
        worker_id = int(worker_id)

        column = input("Enter column name to display (leave blank to display all columns): ").upper()

        valid_columns = ["_id", "FIRST_NAME", "LAST_NAME", "SALARY", "JOINING_DATE", "DEPARTMENT"]
        if column and column in valid_columns:
            projection = {col: 1 for col in valid_columns if col == column}
        else:
            projection = {col: 1 for col in valid_columns}

        worker = collection.find_one({'_id': worker_id}, projection=projection)

        if worker:
            print("Worker details:")
            print(worker)
        else:
            print("No records found.")
    else:
        cursor = collection.find({}, projection={col: 1 for col in valid_columns})
        workers = list(cursor)

        if workers:
            print("Workers:")
            for worker in workers:
                print(worker)
        else:
            print("No records found.")


# Main loop
while True:
    print("\nChoose an operation:")
    print("1. Insert a new worker")
    print("2. Update a worker's salary, joining date, department")
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

# Close the database connection
client.close()

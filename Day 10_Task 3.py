# A doctor has a clinic where he serves his patients. The doctor’s
# consultation fees are different for different groups of patients depending
# on their age. If the patient’s age is below 17, fees is 200 INR. If the patient’s
# age is between 17 and 40, fees is 400 INR. If patient’s age is above 40, fees
# is 300 INR. Write a code to calculate earnings in a day for which one List
# of values representing age of patients visited on that day is passed as
# input.
# Note:
# 1. should not be zero or less than zero or above 120
# 2. Doctor consults a maximum of 20 patients a day
patient_ages = [10, 25, 30, 50, 15, 35, 42]

max_patients = 20
total_earnings = 0

for age in patient_ages:
    if age <= 0 or age > 120:
        print(f"Invalid age {age} encountered. Skipping.")
        continue

    if age < 17:
        total_earnings += 200
    elif age <= 40:
        total_earnings += 400
    else:
        total_earnings += 300

    if len(patient_ages) > max_patients:
        print("Doctor has exceeded the maximum patient limit.")

# Display earnings
print(f"Total earnings for the day: {total_earnings} INR")

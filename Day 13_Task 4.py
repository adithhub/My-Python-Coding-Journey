def calculate_simple_interest(principal, rate, time):
    """
    Function to calculate simple interest.

    Parameters:
    principal (float): The principal amount (initial amount of money).
    rate (float): The annual interest rate (in percentage).
    time (float): The time period (in years).

    Returns:
    float: The simple interest calculated.
    """
    # Calculate simple interest
    simple_interest = (principal * rate * time) / 100
    return simple_interest


principal_amount = int(input("Enter the principal amount: "))
annual_interest_rate = int(input("Enter the interest rate: "))
time_period_years = int(input("Enter the time period in years: "))

# Calculate simple interest
interest = calculate_simple_interest(principal_amount, annual_interest_rate, time_period_years)

# Print the result
print(f"The simple interest for ${principal_amount} at an annual interest rate of {annual_interest_rate}% "
      f"over {time_period_years} years is ${interest:.2f}")

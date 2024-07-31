# Sample data - closing prices for a week (Monday to Friday)
limit = int(input("Enter the limit: "))
stock_prices = []
for i in range(limit):
    price_assign = int(input("Enter the stock price: "))
    stock_prices.append(price_assign)
# Calculate daily price changes
price_changes = [0]  # Initialize with 0 for the first day
for i in range(1, len(stock_prices)):
    change = stock_prices[i] - stock_prices[i - 1]
    price_changes.append(change)

print("Daily Price Changes:", price_changes)
# Identify significant price drops (> 2%)
for i in range(1, len(stock_prices)):
    percent_drop = (stock_prices[i - 1] - stock_prices[i]) / stock_prices[i - 1] * 100
    if percent_drop > 2:
        print(f"Significant price drop of {percent_drop:.2f}% on day {i}")
# Output: Significant price drop of 2.21% on day 3
# Find longest upward trend
max_length = 0
current_length = 1
start_day = 0
end_day = 0

for i in range(1, len(stock_prices)):
    if stock_prices[i] > stock_prices[i - 1]:
        current_length += 1
    else:
        if current_length > max_length:
            max_length = current_length
            start_day = i - current_length
            end_day = i - 1
        current_length = 1

# Check if the longest trend extends to the end of the list
if current_length > max_length:
    max_length = current_length
    start_day = len(stock_prices) - current_length
    end_day = len(stock_prices) - 1

print(f"Longest upward trend: from day {start_day + 1} to day {end_day + 1}, length: {max_length} days")
# Output: Longest upward trend: from day 1 to day 4, length: 4 days

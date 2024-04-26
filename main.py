# Define the sales data as a dictionary (this is easier to work with)
sales_data = {
    "Bubblegum": 202,
    "Toffee": 118,
    "Ice cream": 2250,
    "Milk chocolate": 1680,
    "Doughnut": 1075,
    "Pancake": 80,
}

# Print the header
print("Earned amount:")

# Print each item and its earned amount
for item, amount in sales_data.items():
    print(f"{item}: ${amount}")

# Calculate the total income
total_income = sum(sales_data.values())

# Print the total income
print(f"Total Income: ${total_income}")

# Get Staff Expenses
print("Staff expenses:")
staff_expenses = int(input())

# Get Other Expenses
print("Other expenses:")
other_expenses = int(input())

# Calculate and Print Net Income
net_income = total_income - staff_expenses - other_expenses
print(f"Net Income: ${net_income}")
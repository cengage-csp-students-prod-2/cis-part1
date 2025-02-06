# Write your program here

# Prompt the user to enter the starting salary
starting_salary = float(input("Enter the starting salary: "))

# Prompt the user to enter the percentage increase
percentage_increase = float(input("Enter the percentage increase (as a percentage): ")) / 100

# Prompt the user to enter the number of years in the schedule
num_years = int(input("Enter the number of years in the schedule: "))

# Display the salary schedule
print("\nYear\tSalary")
print("----------------")

salary = starting_salary
for year in range(1, num_years + 1):
    print(f"{year:2d}    ${salary:,.2f}")
    salary += salary * percentage_increase
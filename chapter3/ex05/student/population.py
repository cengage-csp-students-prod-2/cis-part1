initial_organisms = int(input("Enter the initial number of organisms: "))

# Prompt the user to enter the rate of growth
growth_rate = float(input("Enter the rate of growth [a real number > 1]: "))

# Prompt the user to enter the number of hours to achieve the rate of growth
hours_to_achieve_growth = int(input("Enter the number of hours to achieve the rate of growth: "))

# Prompt the user to enter the total hours of growth
total_hours = int(input("Enter the total hours of growth: "))

# Calculate the number of growth periods
growth_periods = total_hours // hours_to_achieve_growth

# Calculate the total population
total_population = initial_organisms * (growth_rate ** growth_periods)

# Display the total population
print("The total population is ", total_population)
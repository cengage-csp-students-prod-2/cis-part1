# Prompt the user to enter the initial number of organisms
initial_organisms = int(input("Enter the initial number of organisms (must be > 0): "))
if initial_organisms <= 0:
    print("Error: The initial number of organisms must be greater than zero.")
    exit()

# Prompt the user to enter the rate of growth
growth_rate = float(input("Enter the rate of growth (a real number > 1): "))
if growth_rate <= 1:
    print("Error: The rate of growth must be greater than 1.")
    exit()

# Prompt the user to enter the number of hours to achieve the rate of growth
hours_to_achieve_growth = int(input("Enter the number of hours to achieve the rate of growth (must be > 0): "))
if hours_to_achieve_growth <= 0:
    print("Error: The number of hours to achieve growth must be greater than zero.")
    exit()

# Prompt the user to enter the total hours of growth
total_hours = int(input("Enter the total hours of growth (must be >= 0): "))
if total_hours < 0:
    print("Error: The total hours of growth must be zero or greater.")
    exit()

# Calculate the number of growth periods
growth_periods = total_hours // hours_to_achieve_growth

# Calculate the total population
total_population = initial_organisms * (growth_rate ** growth_periods)

# Format and display the total population as an integer if it's close to a whole number
if total_population.is_integer():
    total_population = int(total_population)  # Convert to an integer if it's a whole number
else:
    total_population = int(total_population)  # Otherwise, round it to two decimal places

print(f"The total population is {total_population}")

# Prompt the user to enter the number of iterations
iterations = int(input("Enter the number of iterations: "))

# Initialize variables
approximation = 0.0

# Calculate the approximation of π using the Leibniz formula
for i in range(iterations):
    term = (-1) ** i / (2 * i + 1)
    approximation += term

# Multiply by 4 to get the approximation of π
pi_approximation = 4 * approximation

# Display the resulting value of π
print(f"The approximation of π after {iterations} iterations is {pi_approximation}")
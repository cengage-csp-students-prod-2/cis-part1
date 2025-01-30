"""
Pseudocode:
1. Start
2. Prompt user for the mass
3. Prompt user for the velocity
4. Calculate momentum as mass * velocity
5. Display momentum
6. End
"""

# Prompt the user to enter the mass of the object
mass = float(input("Enter the mass of the object (in kilograms): "))

# Prompt the user to enter the velocity of the object
velocity = float(input("Enter the velocity of the object (in meters per second): "))

# Calculate the momentum
momentum = mass * velocity

# Display the calculated momentum
print(f"The momentum of the object is {momentum} kg·m/s")
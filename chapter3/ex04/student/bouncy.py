initial_height = int(input("Enter the height from which the ball is dropped: "))

# Prompt the user to enter the bounciness index
bounciness_index = float(input("Enter the bounciness index of the ball: "))

# Prompt the user to enter the number of bounces
num_bounces = int(input("Enter the number of times the ball is allowed to continue bouncing: "))

# Calculate the total distance traveled by the ball
total_distance = initial_height
current_height = initial_height

for _ in range(num_bounces):
    current_height *= bounciness_index
    total_distance += 2 * current_height

# Display the total distance traveled
print(f"Total distance traveled is: {total_distance:.3f} units.")
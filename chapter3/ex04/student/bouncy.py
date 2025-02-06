def calculate_total_distance(initial_height, bounciness_index, num_bounces):
    total_distance = 0
    current_height = initial_height

    for _ in range(num_bounces):
        total_distance += current_height  # Add the downward travel
        current_height *= bounciness_index  # Calculate the next height
        total_distance += current_height  # Add the upward travel

    return total_distance

def main():
    # Get user input
    initial_height = float(input("Enter the height from which the ball is dropped: "))
    bounciness_index = float(input("Enter the bounciness index of the ball (between 0 and 1): "))
    num_bounces = int(input("Enter the number of times the ball is allowed to continue bouncing: "))

    # Validate inputs
    if initial_height <= 0:
        print("Error: Initial height must be greater than zero.")
        return
    if not (0 < bounciness_index < 1):
        print("Error: Bounciness index must be between 0 and 1 (exclusive).")
        return
    if num_bounces < 0:
        print("Error: Number of bounces must be zero or greater.")
        return

    # Calculate total distance
    total_distance = calculate_total_distance(initial_height, bounciness_index, num_bounces)

    # Output the result
    print(f"Total distance traveled is: {total_distance} units.")

if __name__ == "__main__":
    main()

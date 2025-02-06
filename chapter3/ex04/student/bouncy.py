def calculate_total_distance(initial_height, bounciness_index, num_bounces):
    total_distance = initial_height  # Start with the initial drop
    current_height = initial_height * bounciness_index  # Height after the first bounce

    for _ in range(num_bounces):
        total_distance += current_height * 2  # Add the distance down and up
        current_height *= bounciness_index  # Calculate the height for the next bounce

    return total_distance

def main():
    # Get user input
    initial_height = float(input("Enter the height from which the ball is dropped: "))
    bounciness_index = float(input("Enter the bounciness index of the ball: "))
    num_bounces = int(input("Enter the number of times the ball is allowed to continue bouncing: "))

    # Calculate total distance
    total_distance = calculate_total_distance(initial_height, bounciness_index, num_bounces)

    # Output the result
    print(f"Total distance traveled is: {total_distance} units.")

if __name__ == "__main__":
    main()
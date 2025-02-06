# Initialize variables
numbers = []
total_sum = 0

# Prompt the user to enter numbers
print("Enter a series of numbers. Press Enter without typing a number to finish.")

while True:
    user_input = input("Enter a number: ")
    if user_input == "":
        break
    try:
        number = float(user_input)
        numbers.append(number)
        total_sum += number
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Calculate the average
if numbers:
    average = total_sum / len(numbers)
else:
    average = 0

# Display the sum and average
print(f"The sum of the numbers is: {total_sum}")
print(f"The average of the numbers is: {average}")
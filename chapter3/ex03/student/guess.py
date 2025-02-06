# Prompt the user to enter the lower and upper bounds
lower_bound = int(input("Enter the smaller number: "))
upper_bound = int(input("Enter the larger number: "))

# Calculate the maximum number of guesses needed
max_guesses = math.ceil(math.log2(upper_bound - lower_bound + 1))

print(f"\nThink of a number between {lower_bound} and {upper_bound} (inclusive).")
print(f"I will guess your number in no more than {max_guesses} tries.\n")

# Initialize the number of guesses
num_guesses = 0

while lower_bound <= upper_bound:
    # Calculate the midpoint
    guess = (lower_bound + upper_bound) // 2
    num_guesses += 1

    # Prompt the user for feedback
    print(f"Your number is {guess}")
    feedback = input("Enter =, <, or >: ")

    if feedback == "=":
        print(f"Hooray, I've got it in {num_guesses} tries!")
        break
    elif feedback == "<":
        upper_bound = guess - 1
    elif feedback == ">":
        lower_bound = guess + 1
    else:
        print("Invalid input. Please enter =, <, or >.")

    # Check if the user is cheating
    if lower_bound > upper_bound:
        print("I'm out of guesses, and you cheated!")
        break
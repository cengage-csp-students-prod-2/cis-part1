# Write your program here


# Prompt the user to enter two positive integers
a = int(input("Enter the first positive integer: "))
b = int(input("Enter the second positive integer: "))

# Ensure the inputs are positive integers
if a <= 0 or b <= 0:
    print("Error: Both numbers must be positive integers.")
    exit()

# Euclid's algorithm to find the GCD
print(f"Finding the GCD of {a} and {b} using Euclid's algorithm:")
while b != 0:
    remainder = a % b
    print(f"{a} % {b} = {remainder}")
    a, b = b, remainder

# The GCD is the last non-zero value of a
print(f"The GCD is {a}")
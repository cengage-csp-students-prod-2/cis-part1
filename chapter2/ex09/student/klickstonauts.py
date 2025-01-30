# Write your program here
KM_TO_NAUTICAL_MILE_CONVERSION = 1 / (1/10000 * 90 * 60)

# Prompt the user to enter the distance in kilometers
kilometers = int(input("Enter the distance in kilometers: "))

# Calculate the equivalent distance in nautical miles
nautical_miles = kilometers * KM_TO_NAUTICAL_MILE_CONVERSION

# Display the calculated distance in nautical miles
print(f"The distance in nautical miles is {nautical_miles}")
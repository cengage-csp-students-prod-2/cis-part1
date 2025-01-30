# Write your program here
SECONDS_PER_YEAR = 365 * 24 * 60 * 60  
SPEED_OF_LIGHT = 3 * 10**8  
num_of_years = int(input("Enter number of years: "))

distance = num_of_years * SPEED_OF_LIGHT * SECONDS_PER_YEAR

print(f"The distance light travels in {num_of_years} years is {distance} meters")


'''
1. Start
2. Prompt user for the radius
3. Calculate diameter as 2 * radius
4. Calculate circumference as 2 * pi * radius
5. Calculate surface area as 4 * pi * (radius ** 2)
6. Calculate volume as (4/3) * pi * (radius ** 3)
7. Display diameter, circumference, surface area, and volume
8. End
'''

import math

# Prompt the user to enter the radius of the sphere
radius = float(input("Enter the radius of the sphere: "))

# Calculate the diameter
diameter = 2 * radius

# Calculate the circumference
circumference = 2 * math.pi * radius

# Calculate the surface area
surface_area = 4 * math.pi * (radius ** 2)

# Calculate the volume
volume = (4/3) * math.pi * (radius ** 3)

# Display the calculated values
print(f"The diameter of the sphere is {diameter}")
print(f"The circumference of the sphere is {circumference}")
print(f"The surface area of the sphere is {surface_area}")
print(f"The volume of the sphere is {volume}")
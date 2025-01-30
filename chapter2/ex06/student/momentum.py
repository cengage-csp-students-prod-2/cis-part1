mass = float(input("Enter the mass of the object (in kilograms): "))

velocity = float(input("Enter the velocity of the object (in meters per second): "))

momentum = mass * velocity

kinetic_energy = 0.5 * mass * (velocity ** 2)

print(f"The momentum of the object is {momentum} kg·m/s")
print(f"The kinetic energy of the object is {kinetic_energy} joules")

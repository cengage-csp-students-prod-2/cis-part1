side1 = int(input("Enter the first side: "))
side2 = int(input("Enter the second side: "))
side3 = int(input("Enter the third side: "))

if side1**2 + side2**2 == side3**2:
    print("The triangle is a right triangle.")

else:
    print("The triangle is not a right triangle.")
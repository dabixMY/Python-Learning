import math

mass = float(input("Enter mass     >> "))
diameter = float(input("Enter diameter >> "))
length = float(input("Enter length   >> "))

pi = math.pi

density = (4 * mass) / (pi * diameter**2 * length)

print()
print(f"Density of this cylinder is computed as {density:.3f}.")

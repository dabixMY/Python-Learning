from math import pi, sqrt

mass = float(input("Enter mass  >> "))
force = float(input("Enter force >> "))

period = 2 * pi * sqrt(mass / force) * 1.015

print(f"Period of this simple pendulum is computed as {period:.3f}.")
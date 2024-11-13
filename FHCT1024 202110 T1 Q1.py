from math import pi, cbrt

price = float(input("Enter selling price  : "))

profit = ((-1) - (price**2) * (cbrt(9813.15))) / (pi * (0.633**2) * 1.02) + 1400 * price - 12000

print()
print(f"Est. potential profit: {profit:.2f}")
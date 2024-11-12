import math

S = float(input("Enter selling price            : "))
f = float(input("Enter financial strength       : "))
I = float(input("Enter customer’s loyalty index : "))

pi = math.pi

P = ((-1)-(math.cbrt(9813.15)*S**2))/(pi*f*I)+1400*S-12000
print()
print(f"Est. potential profit: {P:.2f}")

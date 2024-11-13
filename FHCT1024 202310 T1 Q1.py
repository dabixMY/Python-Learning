import math

r = float(input("Enter radius  >> "))
h = float(input("Enter height  >> "))
pi = math.pi

V = (((4/3)*pi*r**3)/2)+(2*pi*(r**2)*h)

print(f"Volume of half a sphere+cylinder is computed as {V:.4f}")
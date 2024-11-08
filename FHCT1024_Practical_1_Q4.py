import math

diameter_earth = 12730
radius_earth =  diameter_earth/2

"""
General Formula
The general formula for the distance a satellite travels in one orbit based on its altitude, h is:
D≈2π(R+h)km
"""

while True:
    try:
        height = float(input("Please key in the satellite’s altitude in kilometres: "))
        break
    except ValueError:
        pass
pi = math.pi
Distance = 2*pi*(radius_earth+height)
print("The distance a satellite travels in one rotation about the Earth is", Distance, "km")
